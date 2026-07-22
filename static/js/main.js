// DP-800 Study App – Main JavaScript

document.addEventListener('DOMContentLoaded', () => {
  // Animate progress bars on load
  document.querySelectorAll('.module-progress-fill, .hero-progress-bar').forEach(bar => {
    const w = bar.style.width;
    bar.style.width = '0';
    setTimeout(() => { bar.style.width = w; }, 150);
  });

  // Animate circular charts on load
  document.querySelectorAll('.circle-fill').forEach(path => {
    const da = path.getAttribute('stroke-dasharray');
    path.setAttribute('stroke-dasharray', '0, 100');
    setTimeout(() => { path.setAttribute('stroke-dasharray', da); }, 200);
  });

  // Smooth highlight.js re-run for dynamic content
  if (window.hljs) {
    document.querySelectorAll('pre code').forEach(block => {
      hljs.highlightElement(block);
    });
  }
});

// Copy code button
function copyCode(btn) {
  const pre = btn.closest('.sql-code-wrap').querySelector('code');
  navigator.clipboard.writeText(pre.textContent).then(() => {
    const orig = btn.innerHTML;
    btn.innerHTML = '<i class="fas fa-check me-1"></i>Copied!';
    btn.style.color = '#4caf50';
    setTimeout(() => {
      btn.innerHTML = orig;
      btn.style.color = '';
    }, 1800);
  });
}

// Sidebar for unit page (desktop open by default; mobile toggled)
function toggleSidebar() {
  document.getElementById('sidebar').classList.toggle('open');
}

// Keyboard navigation on unit page
document.addEventListener('keydown', e => {
  if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
  const prev = document.querySelector('.nav-prev');
  const next = document.querySelector('.nav-next');
  if (e.key === 'ArrowLeft' && prev) prev.click();
  if (e.key === 'ArrowRight' && next) next.click();
});
