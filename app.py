from flask import Flask, render_template, request, jsonify, redirect, url_for
import sqlite3, os, json, threading, webbrowser
from content import COURSE_DATA

app = Flask(__name__)
app.secret_key = 'dp800-sql-study-2024'
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'progress.db')


# ── database helpers ──────────────────────────────────────────────────────────

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    conn.execute('''CREATE TABLE IF NOT EXISTS progress (
        unit_id       TEXT PRIMARY KEY,
        completed     INTEGER DEFAULT 0,
        quiz_score    INTEGER,
        quiz_attempts INTEGER DEFAULT 0,
        last_accessed TEXT    DEFAULT (datetime('now'))
    )''')
    conn.commit()
    conn.close()


def get_all_progress():
    conn = get_db()
    rows = conn.execute('SELECT * FROM progress').fetchall()
    conn.close()
    return {r['unit_id']: dict(r) for r in rows}


def all_units():
    units = []
    for lp in COURSE_DATA['learning_paths']:
        for m in lp['modules']:
            for u in m['units']:
                units.append((u, m, lp))
    return units


def find_unit(unit_id):
    flat = all_units()
    for idx, (u, m, lp) in enumerate(flat):
        if u['id'] == unit_id:
            prev_u = flat[idx - 1][0] if idx > 0 else None
            next_u = flat[idx + 1][0] if idx < len(flat) - 1 else None
            return u, m, lp, prev_u, next_u
    return None, None, None, None, None


# ── routes ────────────────────────────────────────────────────────────────────

@app.route('/')
def index():
    progress = get_all_progress()
    total = sum(len(m['units']) for lp in COURSE_DATA['learning_paths'] for m in lp['modules'])
    done  = sum(1 for p in progress.values() if p['completed'])
    scores = [p['quiz_score'] for p in progress.values() if p.get('quiz_score') is not None]
    avg   = round(sum(scores) / len(scores)) if scores else None
    return render_template('index.html', course=COURSE_DATA, progress=progress,
                           total_units=total, completed=done, avg_score=avg)


@app.route('/mindmap')
def mindmap():
    return render_template('mindmap.html', course=COURSE_DATA)


@app.route('/unit/<unit_id>')
def unit_view(unit_id):
    unit, module, lp, prev_u, next_u = find_unit(unit_id)
    if not unit:
        return redirect(url_for('index'))
    conn = get_db()
    conn.execute('''INSERT INTO progress (unit_id, completed, quiz_attempts, last_accessed)
                    VALUES (?,0,0,datetime('now'))
                    ON CONFLICT(unit_id) DO UPDATE SET last_accessed=datetime('now')''',
                 (unit_id,))
    conn.commit()
    conn.close()
    progress     = get_all_progress()
    unit_prog    = progress.get(unit_id, {})
    # build sidebar nav data
    lp_progress  = {}
    for lp2 in COURSE_DATA['learning_paths']:
        done2 = sum(1 for m2 in lp2['modules']
                    for u2 in m2['units']
                    if progress.get(u2['id'], {}).get('completed'))
        total2 = sum(len(m2['units']) for m2 in lp2['modules'])
        lp_progress[lp2['id']] = {'done': done2, 'total': total2}
    return render_template('unit.html', unit=unit, module=module, lp=lp,
                           prev_unit=prev_u, next_unit=next_u,
                           unit_progress=unit_prog, course=COURSE_DATA,
                           progress=progress, lp_progress=lp_progress)


@app.route('/api/complete/<unit_id>', methods=['POST'])
def mark_complete(unit_id):
    conn = get_db()
    conn.execute('''INSERT INTO progress (unit_id, completed, quiz_attempts, last_accessed)
                    VALUES (?,1,0,datetime('now'))
                    ON CONFLICT(unit_id) DO UPDATE SET completed=1, last_accessed=datetime('now')''',
                 (unit_id,))
    conn.commit()
    conn.close()
    return jsonify({'success': True})


@app.route('/api/quiz/<unit_id>', methods=['POST'])
def submit_quiz(unit_id):
    data    = request.get_json()
    answers = data.get('answers', {})
    unit, _, _, _, _ = find_unit(unit_id)
    if not unit:
        return jsonify({'error': 'Not found'}), 404
    quiz = unit.get('quiz', [])
    if not quiz:
        return jsonify({'error': 'No quiz'}), 400
    score, results = 0, []
    for i, q in enumerate(quiz):
        user_ans = answers.get(str(i))
        correct  = (user_ans == q['correct']) if user_ans is not None else False
        if correct:
            score += 1
        results.append({'question': q['q'], 'options': q['opts'],
                        'user_answer': user_ans, 'correct_answer': q['correct'],
                        'is_correct': correct, 'explanation': q['explain']})
    pct = round((score / len(quiz)) * 100)
    conn = get_db()
    conn.execute('''INSERT INTO progress (unit_id, completed, quiz_score, quiz_attempts, last_accessed)
                    VALUES (?,1,?,1,datetime('now'))
                    ON CONFLICT(unit_id) DO UPDATE SET
                        completed=1,
                        quiz_score=MAX(COALESCE(quiz_score,0),?),
                        quiz_attempts=COALESCE(quiz_attempts,0)+1,
                        last_accessed=datetime('now')''',
                 (unit_id, pct, pct))
    conn.commit()
    conn.close()
    return jsonify({'score': score, 'total': len(quiz), 'percentage': pct,
                    'passed': pct >= 70, 'results': results})


@app.route('/api/reset', methods=['POST'])
def reset_progress():
    conn = get_db()
    conn.execute('DELETE FROM progress')
    conn.commit()
    conn.close()
    return jsonify({'success': True})


if __name__ == '__main__':
    init_db()
    threading.Timer(1.2, lambda: webbrowser.open('http://localhost:5000')).start()
    app.run(debug=False, port=5000)
