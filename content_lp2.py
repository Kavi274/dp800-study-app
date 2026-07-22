# DP-800 Learning Path 2 Content
# LP2: Secure, optimize, and deploy database solutions

LP2_DATA = {
    "id": "lp2",
    "title": "Secure, optimize, and deploy database solutions",
    "description": "Learn to secure SQL databases with encryption and access control, optimize performance, implement CI/CD pipelines, and integrate with Azure services.",
    "color": "#107c10",
    "icon": "fas fa-shield-alt",
    "modules": [

        # ══════════════════════════════════════════════════════════════
        # MODULE lp2-m5: Implement data security and compliance with SQL
        # ══════════════════════════════════════════════════════════════
        {
            "id": "lp2-m5",
            "title": "Implement data security and compliance with SQL",
            "description": "Learn to protect SQL databases using encryption, masking, row-level security, permissions, auditing, and secure access patterns for AI services.",
            "units": [

                # ── Unit 1: Introduction ────────────────────────────────
                {
                    "id": "lp2-m5-u1",
                    "title": "Introduction",
                    "description": "Overview of SQL data security concepts covered in this module.",
                    "estimated_time": 5,
                    "objectives": [
                        "Understand the scope of SQL database security",
                        "Preview the key topics: encryption, masking, RLS, permissions, auditing"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "What You Will Learn in This Module",
                            "body": "Securing a SQL database means protecting your data from unauthorized access — whether that's a hacker attacking the network, a rogue employee running SELECT *, or a compliance auditor asking for proof that sensitive columns are hidden.<br><br>In this module you will learn:<ul><li><strong>Transparent Data Encryption (TDE)</strong> — encrypts the entire database file on disk so stolen backup files are unreadable</li><li><strong>Always Encrypted</strong> — encrypts individual sensitive columns so even DBAs cannot read the plaintext</li><li><strong>Dynamic Data Masking (DDM)</strong> — hides sensitive column values from unauthorized users without changing the stored data</li><li><strong>Row-Level Security (RLS)</strong> — filters rows so each user sees only the rows they are allowed to see</li><li><strong>Permissions and Roles</strong> — GRANT/DENY/REVOKE control exactly what each user can do</li><li><strong>Auditing</strong> — logs database activity to prove compliance</li><li><strong>Secure AI service access</strong> — using Managed Identity and Azure AD to call external REST endpoints safely</li><li><strong>Secure API endpoints</strong> — protecting Data API Builder with HTTPS and Azure AD</li></ul>By the end you will be able to design a defense-in-depth security strategy for any SQL database on the DP-800 exam."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "Which SQL security feature encrypts the physical database files on disk?",
                            "opts": ["A. Dynamic Data Masking", "B. Transparent Data Encryption (TDE)", "C. Row-Level Security", "D. Always Encrypted"],
                            "correct": "B",
                            "explain": "TDE (Transparent Data Encryption) encrypts the entire database file and its backups at rest. It is 'transparent' because applications do not need to change — SQL Server handles encryption and decryption automatically."
                        },
                        {
                            "q": "Which feature hides sensitive column data from unauthorized users without changing the stored value?",
                            "opts": ["A. TDE", "B. Always Encrypted", "C. Dynamic Data Masking", "D. Column-level permissions"],
                            "correct": "C",
                            "explain": "Dynamic Data Masking (DDM) shows masked output (e.g., XXXX) to unauthorized users while the real data remains unchanged in the database. Privileged users with UNMASK permission see the real value."
                        },
                        {
                            "q": "What is the purpose of Row-Level Security (RLS)?",
                            "opts": ["A. Encrypt rows in a table", "B. Restrict which rows a user can see or modify", "C. Log row-level changes to an audit table", "D. Mask individual column values"],
                            "correct": "B",
                            "explain": "RLS uses a security predicate function to filter rows returned by queries (FILTER PREDICATE) or to block insert/update/delete (BLOCK PREDICATE) so each user only accesses rows they are authorized to see."
                        },
                        {
                            "q": "Which encryption feature ensures that even a DBA with full server access cannot read plaintext values of encrypted columns?",
                            "opts": ["A. TDE", "B. Dynamic Data Masking", "C. Always Encrypted", "D. Certificate-based TDE"],
                            "correct": "C",
                            "explain": "Always Encrypted stores the encryption keys in a client-side key store (like Windows Certificate Store or Azure Key Vault). The SQL Server engine never decrypts the data — only the application client with the correct key can decrypt."
                        },
                        {
                            "q": "Which of the following is used to record database activity for compliance purposes?",
                            "opts": ["A. Dynamic Data Masking", "B. SQL Auditing with Audit Specifications", "C. TDE certificates", "D. Row-Level Security"],
                            "correct": "B",
                            "explain": "SQL Auditing captures events (logins, SELECT, INSERT, schema changes, etc.) and writes them to a secure destination such as Azure Blob Storage or Log Analytics. Audit specifications define exactly which events to capture."
                        }
                    ]
                },

                # ── Unit 2: Encryption in SQL databases ────────────────
                {
                    "id": "lp2-m5-u2",
                    "title": "Encryption in SQL databases",
                    "description": "Understand and implement TDE and Always Encrypted to protect data at rest and in use.",
                    "estimated_time": 30,
                    "objectives": [
                        "Explain what TDE does and when to use it",
                        "Enable TDE on a SQL database",
                        "Explain Always Encrypted and the difference between deterministic and randomized encryption",
                        "Know when to choose TDE vs Always Encrypted"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Transparent Data Encryption (TDE) — Encrypting Data at Rest",
                            "body": "Imagine your database backup file gets stolen. Without encryption, anyone can attach it to another SQL Server and read all your data. <strong>TDE prevents this</strong> by encrypting the physical .mdf and .ldf files and all backup files.<br><br><strong>How TDE works:</strong><ul><li>SQL Server creates a <strong>Database Encryption Key (DEK)</strong> stored inside the database</li><li>The DEK is protected by a <strong>certificate</strong> in the master database</li><li>The certificate is protected by the <strong>Service Master Key</strong> (auto-managed by SQL Server)</li><li>All data pages are encrypted/decrypted in memory transparently — your app does not need to change at all</li></ul><strong>What TDE protects:</strong> database files at rest, backups<br><strong>What TDE does NOT protect:</strong> data in transit (use TLS for that), data in memory, logged-in user queries<br><br>In Azure SQL Database and Azure SQL Managed Instance, <strong>TDE is enabled by default</strong>."
                        },
                        {
                            "type": "sql_block",
                            "title": "Enable TDE on an On-Premises SQL Server Database",
                            "scenario": "You have a SQL Server database called SalesDB that stores customer credit card information. You need to enable TDE to comply with PCI-DSS requirements.",
                            "code": """-- Step 1: Create a master key in the master database (if it doesn't exist)
USE master;
GO
CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'StrongP@ssw0rd!2024';
GO

-- Step 2: Create a certificate to protect the Database Encryption Key
CREATE CERTIFICATE TDE_Cert
    WITH SUBJECT = 'TDE Certificate for SalesDB';
GO

-- Step 3: Switch to your user database
USE SalesDB;
GO

-- Step 4: Create the Database Encryption Key (DEK) using the certificate
CREATE DATABASE ENCRYPTION KEY
    WITH ALGORITHM = AES_256
    ENCRYPTION BY SERVER CERTIFICATE TDE_Cert;
GO

-- Step 5: Turn encryption ON for the database
ALTER DATABASE SalesDB
    SET ENCRYPTION ON;
GO

-- Step 6: Verify encryption is enabled
SELECT
    db.name,
    dek.encryption_state,
    dek.percent_complete,
    dek.encryptor_type
FROM sys.databases db
JOIN sys.dm_database_encryption_keys dek
    ON db.database_id = dek.database_id
WHERE db.name = 'SalesDB';""",
                            "explanation": "This 6-step process creates the encryption hierarchy: Service Master Key protects the Certificate, the Certificate protects the DEK, the DEK encrypts all database pages. Once SET ENCRYPTION ON runs, SQL Server begins encrypting in the background — percent_complete shows progress.",
                            "purpose": "Enable TDE so all database files and backups are encrypted at rest, protecting against theft of physical media.",
                            "breakdown": [
                                {"line": "CREATE MASTER KEY ENCRYPTION BY PASSWORD", "meaning": "Creates a symmetric key in the master database that protects certificates and keys. Only needs to be done once per server."},
                                {"line": "CREATE CERTIFICATE TDE_Cert WITH SUBJECT", "meaning": "Creates an X.509 certificate in master. This certificate will wrap (encrypt) the DEK. Back this up immediately!"},
                                {"line": "CREATE DATABASE ENCRYPTION KEY WITH ALGORITHM = AES_256", "meaning": "Creates the actual encryption key inside SalesDB. AES_256 is the strongest available algorithm — always use this."},
                                {"line": "ENCRYPTION BY SERVER CERTIFICATE TDE_Cert", "meaning": "Specifies that TDE_Cert will protect the DEK. If you lose this certificate, you lose access to the database."},
                                {"line": "ALTER DATABASE SalesDB SET ENCRYPTION ON", "meaning": "Switches TDE on. SQL Server starts encrypting all data pages in the background. The database remains online."},
                                {"line": "sys.dm_database_encryption_keys", "meaning": "A Dynamic Management View (DMV) that shows encryption status. encryption_state = 3 means fully encrypted."}
                            ],
                            "ssms_steps": [
                                "Open SSMS and connect to your SQL Server instance",
                                "Click 'New Query' in the toolbar",
                                "Paste the full script above into the query window",
                                "Press F5 (or click Execute) to run all steps",
                                "Watch the Messages tab — you should see 'Command(s) completed successfully'",
                                "To verify: run only the final SELECT from sys.dm_database_encryption_keys",
                                "Check that encryption_state = 3 (Encrypted) and percent_complete = 100"
                            ],
                            "exam_tip": "The exam may ask about the certificate backup requirement. After enabling TDE, you MUST back up the certificate (BACKUP CERTIFICATE TDE_Cert TO FILE ...) because if the server fails, you cannot restore the database without the original certificate."
                        },
                        {
                            "type": "theory",
                            "title": "Always Encrypted — Column-Level Encryption",
                            "body": "TDE protects files. <strong>Always Encrypted</strong> protects individual column values — even from DBAs and Azure administrators who have full database access.<br><br><strong>How it works:</strong><ul><li>Sensitive columns (e.g., SSN, credit card number) are encrypted <em>before</em> being sent to SQL Server</li><li>SQL Server stores and retrieves ciphertext — it never sees plaintext</li><li>Only the <strong>client application</strong> with access to the <strong>Column Master Key (CMK)</strong> can decrypt</li></ul><strong>Two encryption types:</strong><ul><li><strong>Deterministic</strong> — same plaintext always produces same ciphertext. Allows equality searches (WHERE SSN = '123-45-6789'). Use for columns you need to search or join.</li><li><strong>Randomized</strong> — same plaintext produces different ciphertext each time. More secure. Cannot search. Use for columns you only need to store and retrieve (e.g., salary, full SSN).</li></ul><strong>Key hierarchy:</strong> Column Encryption Key (CEK) encrypts the data. Column Master Key (CMK) encrypts the CEK. CMK lives in Azure Key Vault or Windows Certificate Store — never in SQL Server."
                        },
                        {
                            "type": "sql_block",
                            "title": "Create Always Encrypted Columns",
                            "scenario": "You need to protect the SSN and Salary columns in an Employee table so even database administrators cannot read them.",
                            "code": """-- Note: In practice, Always Encrypted keys are created via SSMS wizard
-- or Azure Portal (which stores CMK in Azure Key Vault).
-- The T-SQL below shows what gets generated.

-- Step 1: Create the Column Master Key metadata (CMK stored in Azure Key Vault)
CREATE COLUMN MASTER KEY CMK_Employee
WITH (
    KEY_STORE_PROVIDER_NAME = 'AZURE_KEY_VAULT',
    KEY_PATH = 'https://mykeyvault.vault.azure.net/keys/CMKEmployee/abc123'
);
GO

-- Step 2: Create a Column Encryption Key (CEK) protected by the CMK
CREATE COLUMN ENCRYPTION KEY CEK_Employee
WITH VALUES (
    COLUMN_MASTER_KEY = CMK_Employee,
    ALGORITHM = 'RSA_OAEP',
    ENCRYPTED_VALUE = 0x01700000... -- generated by SSMS/SDK
);
GO

-- Step 3: Create a table with encrypted columns
CREATE TABLE dbo.Employee (
    EmployeeID    INT IDENTITY(1,1) PRIMARY KEY,
    FullName      NVARCHAR(100),                -- not encrypted
    SSN           CHAR(11)
        ENCRYPTED WITH (
            COLUMN_ENCRYPTION_KEY = CEK_Employee,
            ENCRYPTION_TYPE = DETERMINISTIC,    -- allows WHERE SSN = ?
            ALGORITHM = 'AEAD_AES_256_CBC_HMAC_SHA_256'
        ),
    Salary        DECIMAL(10,2)
        ENCRYPTED WITH (
            COLUMN_ENCRYPTION_KEY = CEK_Employee,
            ENCRYPTION_TYPE = RANDOMIZED,       -- more secure, no searching
            ALGORITHM = 'AEAD_AES_256_CBC_HMAC_SHA_256'
        )
);
GO""",
                            "explanation": "Always Encrypted uses a two-key hierarchy. The Column Encryption Key (CEK) encrypts actual column data. The Column Master Key (CMK) encrypts the CEK and lives outside SQL Server in Azure Key Vault. SQL Server only ever sees encrypted bytes.",
                            "purpose": "Protect the most sensitive columns so not even a DBA or cloud admin can read them. Required for compliance with regulations like HIPAA and GDPR.",
                            "breakdown": [
                                {"line": "CREATE COLUMN MASTER KEY ... KEY_STORE_PROVIDER_NAME = 'AZURE_KEY_VAULT'", "meaning": "Registers the CMK metadata in SQL Server. The actual key lives in Azure Key Vault — SQL Server only knows its URL, not the key itself."},
                                {"line": "CREATE COLUMN ENCRYPTION KEY ... ENCRYPTED_VALUE", "meaning": "Stores the CEK encrypted by the CMK. SQL Server keeps this encrypted blob. Only a client with CMK access can decrypt it to get the CEK."},
                                {"line": "ENCRYPTION_TYPE = DETERMINISTIC", "meaning": "Same input always gives same encrypted output. This means you can do WHERE SSN = '123' but it is slightly less secure because patterns may be visible."},
                                {"line": "ENCRYPTION_TYPE = RANDOMIZED", "meaning": "Same input gives different ciphertext every time. Maximum security. Cannot use in WHERE clauses, ORDER BY, or GROUP BY."},
                                {"line": "ALGORITHM = 'AEAD_AES_256_CBC_HMAC_SHA_256'", "meaning": "The only supported Always Encrypted algorithm. AES-256 encryption with HMAC-SHA-256 authentication. Always use this exact string."}
                            ],
                            "ssms_steps": [
                                "Open SSMS and connect to your database",
                                "The easiest way to set up Always Encrypted is via the SSMS wizard:",
                                "Right-click your database → Tasks → Encrypt Columns",
                                "The wizard walks you through selecting columns, encryption type, and key storage",
                                "Choose 'Azure Key Vault' as the key store and sign in to Azure",
                                "The wizard generates and runs the T-SQL automatically",
                                "To view encrypted data: your connection string must include 'Column Encryption Setting=Enabled'"
                            ],
                            "exam_tip": "Key exam distinction: TDE is transparent to the application and protects files on disk. Always Encrypted is also transparent to the SQL engine — it cannot read the plaintext. The encryption/decryption happens on the CLIENT side. Always Encrypted protects against privileged insiders and cloud providers."
                        },
                        {
                            "type": "important",
                            "title": "TDE vs Always Encrypted — Choose the Right Tool",
                            "body": "<strong>Use TDE when:</strong> you need to protect database backups and files from physical theft or unauthorized access at the storage level. Simple to implement, no app changes.<br><br><strong>Use Always Encrypted when:</strong> you need to protect specific sensitive columns from DBAs, cloud admins, or anyone with database access. Requires app-side key management.<br><br><strong>They are complementary</strong> — use both: TDE for file-level encryption, Always Encrypted for the most sensitive columns."
                        },
                        {
                            "type": "tip",
                            "title": "Exam Tip: Azure SQL TDE is ON by Default",
                            "body": "In Azure SQL Database and Azure SQL Managed Instance, TDE is <strong>enabled by default</strong> with a service-managed key. You can optionally use a <strong>customer-managed key (CMK) in Azure Key Vault</strong> for 'Bring Your Own Key' (BYOK) scenarios. On-premises SQL Server requires manual TDE setup."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What does TDE (Transparent Data Encryption) protect?",
                            "opts": ["A. Individual column values from DBA queries", "B. Data in transit over the network", "C. Physical database files and backups at rest", "D. Row-level access based on user identity"],
                            "correct": "C",
                            "explain": "TDE encrypts the physical .mdf, .ldf, and backup files. It is called 'transparent' because the application does not need to change — SQL Server handles encryption/decryption in the background. It does NOT protect data in transit or from logged-in users."
                        },
                        {
                            "q": "In the TDE key hierarchy, what protects the Database Encryption Key (DEK)?",
                            "opts": ["A. A Column Master Key in Azure Key Vault", "B. A Server Certificate stored in the master database", "C. The sa login password", "D. A Windows DPAPI key"],
                            "correct": "B",
                            "explain": "The TDE hierarchy is: Service Master Key → Certificate (in master database) → Database Encryption Key (DEK). The certificate in master wraps the DEK. This is why you must back up the certificate — without it, you cannot restore the database elsewhere."
                        },
                        {
                            "q": "Which Always Encrypted encryption type allows equality searches on encrypted columns?",
                            "opts": ["A. Randomized", "B. Symmetric", "C. Deterministic", "D. AES-128"],
                            "correct": "C",
                            "explain": "Deterministic encryption always produces the same ciphertext for the same plaintext, so SQL Server can compare ciphertexts to evaluate WHERE column = value. Randomized encryption is more secure but prevents searching."
                        },
                        {
                            "q": "Where does the Column Master Key (CMK) in Always Encrypted reside?",
                            "opts": ["A. Inside the encrypted SQL database", "B. In the sys.certificates catalog view", "C. In an external key store like Azure Key Vault or Windows Certificate Store", "D. In the SQL Server master database"],
                            "correct": "C",
                            "explain": "This is the core security principle of Always Encrypted. The CMK never lives in SQL Server — it lives in an external key store (Azure Key Vault, Windows Certificate Store, or an HSM). SQL Server only knows the key's URL/path, not the actual key."
                        },
                        {
                            "q": "In Azure SQL Database, what is the default state of TDE?",
                            "opts": ["A. Disabled — must be enabled manually", "B. Enabled with a service-managed key", "C. Enabled only for Premium tier", "D. Available but requires a certificate upload first"],
                            "correct": "B",
                            "explain": "Azure SQL Database enables TDE by default using a service-managed key. You do not need to do anything. Optionally, you can switch to a customer-managed key (CMK) stored in Azure Key Vault for BYOK compliance."
                        }
                    ]
                },

                # ── Unit 3: Dynamic Data Masking ───────────────────────
                {
                    "id": "lp2-m5-u3",
                    "title": "Dynamic Data Masking",
                    "description": "Learn to hide sensitive column data from unauthorized users using Dynamic Data Masking (DDM).",
                    "estimated_time": 25,
                    "objectives": [
                        "Explain what Dynamic Data Masking does and how it differs from encryption",
                        "Apply mask functions: default(), email(), random(), partial()",
                        "Grant and revoke UNMASK permission"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "What Is Dynamic Data Masking?",
                            "body": "Imagine a call center agent needs to look up customer accounts but should not see full credit card numbers. Dynamic Data Masking (DDM) solves this: the data is stored in full, but certain users see a <strong>masked version</strong> (e.g., XXXX-XXXX-XXXX-1234).<br><br><strong>Key facts about DDM:</strong><ul><li>It is a <strong>presentation-layer</strong> security feature — the real data is unchanged in the database</li><li>Masking is applied at query time based on user permissions</li><li>Users with <strong>db_owner</strong> role or <strong>UNMASK</strong> permission always see the real data</li><li>DDM does NOT replace encryption — a DBA can always bypass it. Use DDM for application-level privacy, not security against privileged users</li></ul><strong>Four masking functions:</strong><ul><li><code>default()</code> — full mask: strings show XXXX, numbers show 0, dates show 1900-01-01 00:00:00</li><li><code>email()</code> — shows first letter + XXX@XXX.com format (e.g., kXXX@XXXX.com)</li><li><code>random(lower, upper)</code> — shows a random number in the specified range (for numeric columns)</li><li><code>partial(prefix, padding, suffix)</code> — shows first N and last N characters with custom padding in between</li></ul>"
                        },
                        {
                            "type": "sql_block",
                            "title": "Add Dynamic Data Masking to a Customer Table",
                            "scenario": "Your Customers table contains sensitive data. Call center agents (using the 'SupportUser' login) should see masked credit card numbers and phone numbers, but supervisors can see real data.",
                            "code": """-- Step 1: Create a sample Customers table
CREATE TABLE dbo.Customers (
    CustomerID   INT IDENTITY(1,1) PRIMARY KEY,
    FullName     NVARCHAR(100),
    Email        NVARCHAR(200),
    Phone        NVARCHAR(20),
    CreditCard   NVARCHAR(19),
    Salary       DECIMAL(10,2),
    BirthDate    DATE
);
GO

-- Step 2: Add masking to existing columns using ALTER TABLE
-- default() mask on CreditCard: shows XXXX for strings
ALTER TABLE dbo.Customers
    ALTER COLUMN CreditCard
    ADD MASKED WITH (FUNCTION = 'default()');
GO

-- email() mask on Email column
ALTER TABLE dbo.Customers
    ALTER COLUMN Email
    ADD MASKED WITH (FUNCTION = 'email()');
GO

-- partial() mask on Phone: show first 3 and last 2 digits, XXX in between
ALTER TABLE dbo.Customers
    ALTER COLUMN Phone
    ADD MASKED WITH (FUNCTION = 'partial(3, "XXX-XXX-", 2)');
GO

-- random() mask on Salary: show a random number between 10000 and 99999
ALTER TABLE dbo.Customers
    ALTER COLUMN Salary
    ADD MASKED WITH (FUNCTION = 'random(10000, 99999)');
GO

-- Step 3: Insert sample data
INSERT INTO dbo.Customers (FullName, Email, Phone, CreditCard, Salary, BirthDate)
VALUES ('Jane Smith', 'jane.smith@contoso.com', '555-867-5309', '4111-1111-1111-1234', 75000.00, '1990-05-15');
GO

-- Step 4: Create a low-privilege user to test masking
CREATE USER SupportUser WITHOUT LOGIN;
GRANT SELECT ON dbo.Customers TO SupportUser;
GO

-- Step 5: Query as SupportUser to see masked output
EXECUTE AS USER = 'SupportUser';
SELECT CustomerID, FullName, Email, Phone, CreditCard, Salary FROM dbo.Customers;
REVERT;
GO

-- Step 6: Grant UNMASK to a supervisor role so they see real data
CREATE USER SupervisorUser WITHOUT LOGIN;
GRANT SELECT ON dbo.Customers TO SupervisorUser;
GRANT UNMASK TO SupervisorUser;  -- This user sees real values
GO

-- Step 7: View all masks defined in the database
SELECT
    t.name AS TableName,
    c.name AS ColumnName,
    c.masking_function
FROM sys.masked_columns c
JOIN sys.tables t ON c.object_id = t.object_id;""",
                            "explanation": "DDM is applied at query time. SupportUser will see 'XXXX' for CreditCard, 'jXXX@XXXX.com' for Email, and '555XXXXXX09' for Phone. SupervisorUser with UNMASK permission sees real values. The data in the table never changes.",
                            "purpose": "Protect sensitive column values from unauthorized application users while keeping full data accessible to administrators and privileged roles.",
                            "breakdown": [
                                {"line": "ALTER COLUMN CreditCard ADD MASKED WITH (FUNCTION = 'default()')", "meaning": "Adds a mask to the CreditCard column. For varchar/nvarchar, default() shows 'XXXX'. For int columns it shows 0. For date columns it shows 1900-01-01."},
                                {"line": "FUNCTION = 'email()'", "meaning": "Email mask shows the first character, then 'XXX@XXXX.com'. So 'jane.smith@contoso.com' becomes 'jXXX@XXXX.com'."},
                                {"line": "FUNCTION = 'partial(3, \"XXX-XXX-\", 2)'", "meaning": "Partial mask shows first 3 and last 2 characters of the real value, with the middle string 'XXX-XXX-' inserted. '555-867-5309' becomes '555XXX-XXX-09'."},
                                {"line": "FUNCTION = 'random(10000, 99999)'", "meaning": "For numeric columns, shows a random number in the specified range instead of the real value. Different each time the query runs."},
                                {"line": "CREATE USER SupportUser WITHOUT LOGIN", "meaning": "Creates a database user with no login — useful for testing permissions. In production, users have real logins."},
                                {"line": "EXECUTE AS USER = 'SupportUser'", "meaning": "Temporarily switches execution context to SupportUser. Lets you test what a restricted user would see. REVERT switches back."},
                                {"line": "GRANT UNMASK TO SupervisorUser", "meaning": "Grants database-level permission to see through all masks. This user sees real values for all masked columns in all tables."},
                                {"line": "sys.masked_columns", "meaning": "System catalog view that lists all columns with masks applied, including the mask function name. Use this to audit what is masked."}
                            ],
                            "ssms_steps": [
                                "Open SSMS and connect to your SQL Server (2016+) or Azure SQL Database",
                                "Click 'New Query' and select your target database in the dropdown",
                                "Paste and run the CREATE TABLE block (Step 1)",
                                "Paste and run the ALTER TABLE blocks (Steps 2-4) to add masks",
                                "Paste and run the INSERT to add test data (Step 3)",
                                "Paste and run Steps 4-5 (CREATE USER and EXECUTE AS) to test",
                                "In the Results grid, verify CreditCard shows 'XXXX' and Email shows 'jXXX@XXXX.com'",
                                "Then run Step 6 and test as SupervisorUser — you should see real values"
                            ],
                            "exam_tip": "DDM does NOT protect against users with db_owner or CONTROL DATABASE permissions. They always see real data. DDM is about limiting data exposure to application users, not protecting against privileged database accounts."
                        },
                        {
                            "type": "important",
                            "title": "DDM Limitation: Not a Security Boundary",
                            "body": "Dynamic Data Masking is a <strong>convenience feature, not a security boundary</strong>. Any user who can run arbitrary T-SQL can often infer masked values through brute force or inference attacks. For example: WHERE CreditCard = '4111-1111-1111-1234' still returns rows even if the user cannot SELECT the column value.<br><br>For true sensitive data protection use <strong>Always Encrypted</strong>. DDM is best used to limit accidental data exposure in application UI."
                        },
                        {
                            "type": "tip",
                            "title": "Add Masks at Table Creation Time",
                            "body": "You can add a MASKED WITH clause directly in CREATE TABLE instead of using ALTER TABLE later:<br><code>CreditCard NVARCHAR(19) MASKED WITH (FUNCTION = 'default()')</code><br>This is cleaner for new tables. The ALTER TABLE approach is for adding masks to existing tables."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What does the 'default()' mask function show for a NVARCHAR column?",
                            "opts": ["A. The first and last character with asterisks in between", "B. XXXX", "C. NULL", "D. 0"],
                            "correct": "B",
                            "explain": "For string data types (char, varchar, nvarchar), the default() function shows 'XXXX'. For numeric types it shows 0, for date types it shows 1900-01-01 00:00:00, and for binary types it shows a single byte of 0."
                        },
                        {
                            "q": "A user with which permission can always see unmasked data in a DDM-protected column?",
                            "opts": ["A. SELECT permission on the table", "B. INSERT permission on the table", "C. UNMASK permission or db_owner role", "D. VIEW DEFINITION permission"],
                            "correct": "C",
                            "explain": "Users with the UNMASK permission (granted with GRANT UNMASK TO user) or membership in the db_owner role can see through all masks. Regular users with only SELECT permission see masked values."
                        },
                        {
                            "q": "Which mask function would you use to show 'aXXX@XXXX.com' for the value 'alice@company.com'?",
                            "opts": ["A. default()", "B. email()", "C. partial(1, 'XXX@XXXX', 4)", "D. random(0,1)"],
                            "correct": "B",
                            "explain": "The email() function is specifically designed for email addresses. It shows the first character followed by 'XXX@XXXX.com', regardless of the actual domain."
                        },
                        {
                            "q": "Which T-SQL view shows you all masked columns in the current database?",
                            "opts": ["A. sys.columns WHERE is_masked = 1", "B. sys.masked_columns", "C. sys.data_masks", "D. information_schema.masked_columns"],
                            "correct": "B",
                            "explain": "sys.masked_columns is a system catalog view that returns all columns with Dynamic Data Masking applied, including the table name, column name, and the mask function used."
                        },
                        {
                            "q": "You use ALTER TABLE dbo.Orders ALTER COLUMN CardNumber ADD MASKED WITH (FUNCTION = 'partial(0, \"XXXX-XXXX-XXXX-\", 4)'). What does an unauthorized user see for '1234-5678-9012-3456'?",
                            "opts": ["A. XXXX", "B. XXXX-XXXX-XXXX-3456", "C. 1234-XXXX-XXXX-XXXX", "D. 0"],
                            "correct": "B",
                            "explain": "partial(prefix_length, padding, suffix_length) shows the first 'prefix_length' characters, then the padding string, then the last 'suffix_length' characters. With partial(0, 'XXXX-XXXX-XXXX-', 4), no prefix is shown, then the padding, then the last 4 characters '3456'."
                        }
                    ]
                },

                # ── Unit 4: Row-Level Security ──────────────────────────
                {
                    "id": "lp2-m5-u4",
                    "title": "Row-Level Security",
                    "description": "Implement Row-Level Security to filter which rows each user can access in a table.",
                    "estimated_time": 30,
                    "objectives": [
                        "Explain how RLS works with predicate functions and security policies",
                        "Create a filter predicate to restrict SELECT results",
                        "Create a block predicate to restrict writes",
                        "Understand the difference between FILTER and BLOCK predicates"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Row-Level Security (RLS) Explained",
                            "body": "Row-Level Security lets you control which <strong>rows</strong> in a table a user can see or modify, based on the user's identity or role. Without RLS you would have to write WHERE clauses in every query — and if a developer forgets one, data leaks. RLS enforces the filter <strong>at the database engine level</strong>, so it applies to all queries regardless of application logic.<br><br><strong>RLS consists of two parts:</strong><ol><li><strong>Predicate function</strong> — an inline table-valued function that returns 1 (allow) or 0 (deny). The database engine calls this function automatically for every row.</li><li><strong>Security policy</strong> — binds the predicate function to a table, specifying whether it is a FILTER or BLOCK predicate.</li></ol><strong>Two types of predicates:</strong><ul><li><strong>FILTER predicate</strong> — silently removes rows the user cannot see from SELECT results. The user does not know hidden rows exist.</li><li><strong>BLOCK predicate</strong> — prevents INSERT, UPDATE, or DELETE of rows that violate the predicate. Returns an error.</li></ul><strong>Common use case:</strong> A sales table with rows for many salespeople. Each salesperson should only see their own rows. RLS enforces this without changing application queries."
                        },
                        {
                            "type": "sql_block",
                            "title": "Implement Row-Level Security for a Sales Table",
                            "scenario": "You have a Sales table shared by multiple salespeople. Each salesperson should only see their own sales. The sales manager (SalesManager) should see all rows.",
                            "code": """-- Step 1: Create the Sales table
CREATE TABLE dbo.Sales (
    SaleID       INT IDENTITY(1,1) PRIMARY KEY,
    SalesRep     NVARCHAR(100),    -- stores the username of the salesperson
    Product      NVARCHAR(200),
    Amount       DECIMAL(10,2),
    SaleDate     DATE
);
GO

-- Step 2: Insert sample data for two salespeople
INSERT INTO dbo.Sales (SalesRep, Product, Amount, SaleDate) VALUES
('Alice', 'Laptop',    1200.00, '2024-01-10'),
('Alice', 'Monitor',    350.00, '2024-01-15'),
('Bob',   'Keyboard',    89.00, '2024-01-12'),
('Bob',   'Headphones', 199.00, '2024-01-20');
GO

-- Step 3: Create database users for testing
CREATE USER Alice WITHOUT LOGIN;
CREATE USER Bob WITHOUT LOGIN;
CREATE USER SalesManager WITHOUT LOGIN;
GRANT SELECT, INSERT, UPDATE, DELETE ON dbo.Sales TO Alice, Bob, SalesManager;
GO

-- Step 4: Create the RLS predicate function
-- This function lives in a separate schema for security
CREATE SCHEMA Security;
GO

CREATE FUNCTION Security.fn_SalesFilter
    (@SalesRep AS NVARCHAR(100))
RETURNS TABLE
WITH SCHEMABINDING
AS
RETURN
    SELECT 1 AS fn_securitypredicate_result
    WHERE
        @SalesRep = USER_NAME()         -- user sees their own rows
        OR USER_NAME() = 'SalesManager'; -- manager sees all rows
GO

-- Step 5: Create the Security Policy and bind the predicate
CREATE SECURITY POLICY SalesRLSPolicy
ADD FILTER PREDICATE Security.fn_SalesFilter(SalesRep)
    ON dbo.Sales,
ADD BLOCK PREDICATE Security.fn_SalesFilter(SalesRep)
    ON dbo.Sales AFTER INSERT    -- prevent inserting rows for other users
WITH (STATE = ON);               -- activate the policy immediately
GO

-- Step 6: Test — Alice should only see her 2 rows
EXECUTE AS USER = 'Alice';
SELECT * FROM dbo.Sales;         -- returns 2 rows (Alice's only)
REVERT;
GO

-- Step 7: Test — Bob sees only his 2 rows
EXECUTE AS USER = 'Bob';
SELECT * FROM dbo.Sales;         -- returns 2 rows (Bob's only)
REVERT;
GO

-- Step 8: Manager sees all 4 rows
EXECUTE AS USER = 'SalesManager';
SELECT * FROM dbo.Sales;         -- returns all 4 rows
REVERT;
GO""",
                            "explanation": "The predicate function returns rows where the SalesRep column matches the current user's name OR the current user is 'SalesManager'. The security policy applies this filter to every SELECT, INSERT, UPDATE, and DELETE without any app changes needed.",
                            "purpose": "Enforce data isolation at the database level so each salesperson can only access their own records, without relying on application-layer filtering.",
                            "breakdown": [
                                {"line": "CREATE FUNCTION Security.fn_SalesFilter(@SalesRep AS NVARCHAR(100)) RETURNS TABLE", "meaning": "Defines an inline table-valued function. The parameter (@SalesRep) receives the column value from each row being evaluated. If the function returns a row, the row is allowed; if it returns nothing, the row is filtered out."},
                                {"line": "WITH SCHEMABINDING", "meaning": "Required for RLS predicate functions. Prevents the underlying tables referenced in the function from being dropped or altered without dropping the function first."},
                                {"line": "WHERE @SalesRep = USER_NAME()", "meaning": "USER_NAME() returns the database username of the current session. This condition allows a row only if the SalesRep column matches who is logged in."},
                                {"line": "OR USER_NAME() = 'SalesManager'", "meaning": "Additional condition: the SalesManager user always gets all rows. This is the admin bypass pattern."},
                                {"line": "ADD FILTER PREDICATE Security.fn_SalesFilter(SalesRep) ON dbo.Sales", "meaning": "Binds the function to the Sales table as a FILTER predicate. The column 'SalesRep' is passed to the function's @SalesRep parameter for each row evaluated in a SELECT."},
                                {"line": "ADD BLOCK PREDICATE ... ON dbo.Sales AFTER INSERT", "meaning": "Prevents a user from inserting a row where SalesRep is not their own name. AFTER INSERT checks the new row. Other options: AFTER UPDATE, BEFORE UPDATE, BEFORE DELETE."},
                                {"line": "WITH (STATE = ON)", "meaning": "Activates the policy immediately. You can set STATE = OFF to disable the policy temporarily without dropping it."}
                            ],
                            "ssms_steps": [
                                "Open SSMS and connect to your database",
                                "Click New Query",
                                "Run Steps 1-3 to create the table, insert data, and create users",
                                "Run Steps 4-5 to create the predicate function and security policy",
                                "Run Step 6 (EXECUTE AS USER = 'Alice') and check the Results — you should see only Alice's rows",
                                "Run Step 7 as Bob — see only Bob's rows",
                                "Run Step 8 as SalesManager — see all 4 rows",
                                "To remove RLS: DROP SECURITY POLICY SalesRLSPolicy, then DROP FUNCTION Security.fn_SalesFilter"
                            ],
                            "exam_tip": "The exam often tests the CREATE SECURITY POLICY syntax. Remember: you need both the FUNCTION (predicate logic) and the POLICY (binding to table). FILTER PREDICATE affects SELECT. BLOCK PREDICATE affects writes. Users with db_owner or ALTER ANY SECURITY POLICY permission bypass RLS."
                        },
                        {
                            "type": "tip",
                            "title": "RLS and db_owner",
                            "body": "Users in the <strong>db_owner</strong> role automatically bypass all Row-Level Security policies. This is by design so database administrators can always manage data. If you need to test RLS as a non-owner, use EXECUTE AS USER as shown in the example above."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What T-SQL object type is used as the predicate in Row-Level Security?",
                            "opts": ["A. Stored procedure", "B. Scalar function", "C. Inline table-valued function", "D. Trigger"],
                            "correct": "C",
                            "explain": "RLS predicates must be inline table-valued functions (WITH SCHEMABINDING). The database engine calls the function for each row; if the function returns a row, the predicate passes (row is allowed)."
                        },
                        {
                            "q": "What is the difference between a FILTER predicate and a BLOCK predicate in RLS?",
                            "opts": ["A. FILTER encrypts rows; BLOCK deletes them", "B. FILTER silently hides rows from SELECT; BLOCK prevents unauthorized writes", "C. FILTER applies to a single column; BLOCK applies to the whole table", "D. FILTER is for Azure SQL only; BLOCK works on-premises"],
                            "correct": "B",
                            "explain": "FILTER PREDICATE silently removes rows that fail the predicate from SELECT results — the user does not know those rows exist. BLOCK PREDICATE raises an error when a user tries to INSERT, UPDATE, or DELETE rows that fail the predicate."
                        },
                        {
                            "q": "In RLS, which built-in function returns the database username of the currently connected user?",
                            "opts": ["A. SUSER_SNAME()", "B. USER_NAME()", "C. SESSION_USER()", "D. CURRENT_USER()"],
                            "correct": "B",
                            "explain": "USER_NAME() returns the database-level username (e.g., 'Alice'). It is commonly used in RLS predicates to filter rows based on the logged-in user. SUSER_SNAME() returns the server-level login name."
                        },
                        {
                            "q": "A security policy is created with STATE = OFF. What happens to the RLS filter?",
                            "opts": ["A. The policy is permanently deleted", "B. The filter applies only to SELECT, not writes", "C. The policy is disabled — all users see all rows", "D. Only db_owner users can query the table"],
                            "correct": "C",
                            "explain": "STATE = OFF disables the security policy without dropping it. All users can see all rows. This is useful for troubleshooting or maintenance. Set STATE = ON to re-enable it."
                        },
                        {
                            "q": "Which role automatically bypasses all Row-Level Security policies?",
                            "opts": ["A. db_datareader", "B. db_datawriter", "C. db_owner", "D. db_securityadmin"],
                            "correct": "C",
                            "explain": "Members of db_owner always bypass RLS. This ensures DBAs can always manage the database. It is not a bug — it is by design. For testing RLS as a non-owner, use EXECUTE AS USER = 'username'."
                        }
                    ]
                },

                # ── Unit 5: Permissions and secure access ───────────────
                {
                    "id": "lp2-m5-u5",
                    "title": "Permissions and secure access",
                    "description": "Master SQL Server permissions using GRANT, DENY, REVOKE, roles, and contained database users.",
                    "estimated_time": 30,
                    "objectives": [
                        "Use GRANT, DENY, and REVOKE to control access",
                        "Assign users to built-in database roles",
                        "Create contained database users",
                        "Apply the principle of least privilege"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "SQL Server Permissions — The Basics",
                            "body": "SQL Server uses a hierarchical permission model. Before a user can do anything, they need:<ol><li>A <strong>Login</strong> — a server-level identity (Windows account, SQL login, or Azure AD identity)</li><li>A <strong>User</strong> — a database-level identity mapped to a login</li><li><strong>Permissions</strong> — specific rights (SELECT, INSERT, UPDATE, DELETE, EXECUTE, etc.) granted to the user</li></ol><strong>Three permission commands:</strong><ul><li><code>GRANT</code> — gives permission to a user or role</li><li><code>DENY</code> — explicitly denies permission. DENY always overrides GRANT, even through role membership</li><li><code>REVOKE</code> — removes a previously granted or denied permission (back to neutral state)</li></ul><strong>Built-in Database Roles:</strong><ul><li><code>db_datareader</code> — SELECT on all tables</li><li><code>db_datawriter</code> — INSERT, UPDATE, DELETE on all tables</li><li><code>db_ddladmin</code> — CREATE, ALTER, DROP objects</li><li><code>db_owner</code> — full control of the database</li><li><code>db_securityadmin</code> — manage permissions</li></ul>"
                        },
                        {
                            "type": "sql_block",
                            "title": "Create a Login, User, and Grant Permissions",
                            "scenario": "You need to give a new employee 'ReportUser' read access to the Sales table and execute access to a stored procedure, but explicitly deny access to the Payroll table.",
                            "code": """-- Step 1: Create a SQL Server Login (server-level)
-- Run this in the master database or with USE master first
USE master;
GO
CREATE LOGIN ReportUser WITH PASSWORD = 'Rep0rtP@ss!';
GO

-- Step 2: Create a database user mapped to the login
USE SalesDB;
GO
CREATE USER ReportUser FOR LOGIN ReportUser;
GO

-- Step 3: Grant specific table permissions (least privilege)
GRANT SELECT ON dbo.Sales TO ReportUser;
GRANT SELECT ON dbo.Products TO ReportUser;
GO

-- Step 4: Grant execute on a stored procedure
GRANT EXECUTE ON dbo.usp_GetSalesSummary TO ReportUser;
GO

-- Step 5: Explicitly DENY access to sensitive table
-- DENY overrides any GRANT, even through role membership
DENY SELECT ON dbo.Payroll TO ReportUser;
GO

-- Step 6: Add user to a built-in role for convenience
-- db_datareader gives SELECT on ALL tables, but our DENY on Payroll still blocks it
ALTER ROLE db_datareader ADD MEMBER ReportUser;
GO

-- Step 7: Check what permissions a user has
-- Using sys.fn_my_permissions (run as ReportUser)
EXECUTE AS USER = 'ReportUser';
SELECT * FROM sys.fn_my_permissions('dbo.Sales', 'OBJECT');
REVERT;
GO

-- Step 8: Check permissions via catalog views
SELECT
    pr.name AS PrincipalName,
    dp.class_desc,
    dp.permission_name,
    dp.state_desc,
    OBJECT_NAME(dp.major_id) AS ObjectName
FROM sys.database_permissions dp
JOIN sys.database_principals pr ON dp.grantee_principal_id = pr.principal_id
WHERE pr.name = 'ReportUser';
GO

-- Step 9: Revoke a permission (removes it, back to neutral)
REVOKE SELECT ON dbo.Products FROM ReportUser;
GO

-- Step 10: Create a contained database user (no login required)
-- Useful for Azure SQL Database portability
CREATE USER ContainedUser WITH PASSWORD = 'C0nt@inedP@ss!';
GO""",
                            "explanation": "This demonstrates the full permission lifecycle: create login/user, grant specific permissions, use DENY to block sensitive access, add to roles, and check effective permissions. DENY always wins — even if ReportUser is in db_datareader, they cannot access Payroll.",
                            "purpose": "Apply least-privilege access control so users can only access what they need, with explicit denies on sensitive objects.",
                            "breakdown": [
                                {"line": "CREATE LOGIN ReportUser WITH PASSWORD", "meaning": "Creates a server-level identity. This is what connects to the SQL Server instance. SQL logins store credentials in SQL Server itself."},
                                {"line": "CREATE USER ReportUser FOR LOGIN ReportUser", "meaning": "Creates a database-level principal linked to the server login. Users exist inside a specific database. One login can map to one user per database."},
                                {"line": "GRANT SELECT ON dbo.Sales TO ReportUser", "meaning": "Gives ReportUser the ability to run SELECT on the Sales table only. This is least-privilege: only what is needed."},
                                {"line": "DENY SELECT ON dbo.Payroll TO ReportUser", "meaning": "Explicitly blocks SELECT on Payroll. DENY overrides all GRANTs, including those inherited from roles. Even if you later add this user to db_datareader, Payroll remains blocked."},
                                {"line": "ALTER ROLE db_datareader ADD MEMBER ReportUser", "meaning": "Adds the user to the built-in db_datareader role. This gives SELECT on all tables, BUT the explicit DENY on Payroll still prevents access to that table."},
                                {"line": "sys.fn_my_permissions('dbo.Sales', 'OBJECT')", "meaning": "Returns the effective permissions the current user has on the specified object. Useful for debugging 'why can't I access this?'"},
                                {"line": "CREATE USER ContainedUser WITH PASSWORD", "meaning": "A 'contained' user stores credentials in the database itself rather than linking to a server login. The database can be moved to another server without recreating logins. Required for Azure SQL Database geo-replication scenarios."}
                            ],
                            "ssms_steps": [
                                "Open SSMS and connect as a sysadmin (e.g., sa or your Azure admin account)",
                                "Run Step 1 to create the login (make sure you are connected to master or switch with USE master)",
                                "Switch to SalesDB: type 'USE SalesDB;' or select it in the database dropdown",
                                "Run Steps 2-5 to create the user and set permissions",
                                "To verify: right-click the user in Object Explorer → Properties → Securables to see all permissions visually",
                                "Run Step 7 (EXECUTE AS USER) to test effective permissions",
                                "Check the Results grid for the list of permissions ReportUser has on dbo.Sales"
                            ],
                            "exam_tip": "DENY always wins over GRANT. If a user has GRANT SELECT through a role and DENY SELECT directly, the result is DENY. REVOKE removes the GRANT or DENY but does not add a new state — the user returns to 'no permission assigned'."
                        },
                        {
                            "type": "important",
                            "title": "Principle of Least Privilege",
                            "body": "Always grant the <strong>minimum permissions</strong> needed for a user or application to do its job.<ul><li>Application service accounts should have EXECUTE on stored procedures, not direct SELECT/INSERT/UPDATE/DELETE on tables</li><li>Use roles to manage groups of users instead of granting to individuals</li><li>Regularly audit permissions with sys.database_permissions</li><li>Prefer contained database users for Azure SQL Database — they travel with the database on failover</li></ul>"
                        }
                    ],
                    "quiz": [
                        {
                            "q": "A user has GRANT SELECT on a table through role membership, but also has DENY SELECT directly on the same table. What is the effective permission?",
                            "opts": ["A. GRANT — the most permissive wins", "B. DENY — DENY always overrides GRANT", "C. No access — they cancel out", "D. The most recently set permission wins"],
                            "correct": "B",
                            "explain": "In SQL Server, DENY always overrides GRANT regardless of how the GRANT was received (directly or through role membership). This is a key security principle and a common exam question."
                        },
                        {
                            "q": "Which built-in database role gives a user SELECT permission on all tables in a database?",
                            "opts": ["A. db_ddladmin", "B. db_owner", "C. db_datareader", "D. db_securityadmin"],
                            "correct": "C",
                            "explain": "db_datareader grants SELECT on all user tables and views in the database. db_datawriter grants INSERT/UPDATE/DELETE. db_owner has full control. db_ddladmin can create/alter/drop objects."
                        },
                        {
                            "q": "What is a contained database user in SQL Server?",
                            "opts": ["A. A user whose permissions are contained to a single table", "B. A user whose authentication is stored in the database rather than at the server level", "C. A user created by the db_owner role only", "D. A read-only user that cannot modify data"],
                            "correct": "B",
                            "explain": "Contained database users store their authentication information (password or Azure AD identity) within the database itself, rather than mapping to a server-level login. This allows the database to be moved between servers without recreating logins — important in Azure SQL Database."
                        },
                        {
                            "q": "What does REVOKE SELECT ON dbo.Orders FROM SalesUser do?",
                            "opts": ["A. Denies SELECT to SalesUser", "B. Removes the previous GRANT or DENY, returning to no-permission state", "C. Removes SalesUser from all roles", "D. Drops the SalesUser from the database"],
                            "correct": "B",
                            "explain": "REVOKE removes a previously set GRANT or DENY. It does not apply a new permission — it returns the user to a neutral state (no explicit permission). The user might still have access through role membership."
                        },
                        {
                            "q": "Which system function shows the effective permissions of the current user on a specific object?",
                            "opts": ["A. sys.database_permissions", "B. sys.fn_my_permissions()", "C. OBJECTPROPERTY()", "D. HAS_PERMS_BY_NAME()"],
                            "correct": "B",
                            "explain": "sys.fn_my_permissions('object_name', 'OBJECT') returns a table of permissions the current user has on the specified object. It considers all grants through roles and direct permissions. HAS_PERMS_BY_NAME() checks for a specific permission and returns 1 or 0."
                        }
                    ]
                },

                # ── Unit 6: Auditing SQL databases ─────────────────────
                {
                    "id": "lp2-m5-u6",
                    "title": "Auditing SQL databases",
                    "description": "Configure SQL Server and Azure SQL auditing to capture and review database activity for compliance.",
                    "estimated_time": 25,
                    "objectives": [
                        "Explain the difference between Server Audit and Database Audit Specification",
                        "Create an audit that logs to Azure Blob Storage",
                        "Query audit logs to investigate activity"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "SQL Server Auditing — Why and How",
                            "body": "Auditing answers: <em>Who did what to which data, and when?</em> This is required by regulations like HIPAA, PCI-DSS, SOX, and GDPR.<br><br><strong>SQL Server Audit has two parts:</strong><ol><li><strong>Server Audit</strong> — defines WHERE to write audit logs (file, Windows Event Log, Azure Blob Storage) and the filtering threshold</li><li><strong>Audit Specification</strong> — defines WHAT to audit (which actions on which objects)<ul><li><em>Server Audit Specification</em> — server-level events (failed logins, permission changes)</li><li><em>Database Audit Specification</em> — database-level events (SELECT on a table, stored procedure execution)</li></ul></li></ol><strong>Common audit actions to monitor:</strong><ul><li>SCHEMA_OBJECT_ACCESS_GROUP — SELECT, INSERT, UPDATE, DELETE on tables</li><li>DATABASE_PRINCIPAL_CHANGE_GROUP — user/role changes</li><li>FAILED_LOGIN_GROUP — failed login attempts</li><li>BACKUP_RESTORE_GROUP — backups (could indicate data exfiltration)</li></ul>"
                        },
                        {
                            "type": "sql_block",
                            "title": "Create a Database Audit to Azure Blob Storage",
                            "scenario": "You need to audit all SELECT and INSERT operations on the dbo.Customers table and write logs to Azure Blob Storage for compliance review.",
                            "code": """-- Step 1: Create the Server Audit (defines WHERE logs go)
-- Run this in master database
USE master;
GO

CREATE SERVER AUDIT CustomerDataAudit
TO URL (PATH = 'https://mystorageaccount.blob.core.windows.net/sqllogs',
        RETENTION_DAYS = 90)
WITH (
    QUEUE_DELAY = 1000,           -- buffer up to 1 second before writing
    ON_FAILURE = CONTINUE          -- if audit fails, allow SQL Server to continue
);
GO

-- Step 2: Enable the server audit
ALTER SERVER AUDIT CustomerDataAudit WITH (STATE = ON);
GO

-- Step 3: Create a Database Audit Specification (defines WHAT to audit)
USE SalesDB;
GO

CREATE DATABASE AUDIT SPECIFICATION AuditCustomerAccess
FOR SERVER AUDIT CustomerDataAudit
ADD (SELECT, INSERT, UPDATE, DELETE
     ON dbo.Customers
     BY PUBLIC),                   -- audit for all users (PUBLIC = everyone)
ADD (SCHEMA_OBJECT_ACCESS_GROUP);  -- also audit all object access events
GO

-- Step 4: Enable the database audit specification
ALTER DATABASE AUDIT SPECIFICATION AuditCustomerAccess WITH (STATE = ON);
GO

-- Step 5: Verify audit configuration
SELECT
    a.name AS AuditName,
    a.type_desc AS AuditType,
    a.log_file_path,
    a.is_state_enabled
FROM sys.server_audits a;
GO

-- View database audit specifications
SELECT
    das.name AS SpecificationName,
    das.is_state_enabled,
    dasa.audit_action_name,
    dasa.object_name,
    dasa.principal_name
FROM sys.database_audit_specifications das
JOIN sys.database_audit_specification_details dasa
    ON das.database_specification_id = dasa.database_specification_id;
GO

-- Step 6: Read audit logs (for file-based audits)
SELECT
    event_time,
    action_id,
    succeeded,
    session_server_principal_name AS LoginName,
    database_principal_name AS UserName,
    object_name AS TableAccessed,
    statement
FROM sys.fn_get_audit_file(
    'C:\\AuditLogs\\CustomerDataAudit*.sqlaudit',
    DEFAULT, DEFAULT
)
ORDER BY event_time DESC;""",
                            "explanation": "SQL auditing separates the destination (Server Audit) from the events to capture (Audit Specification). This design lets you reuse one audit destination for multiple specifications. In Azure SQL, configure auditing through the Azure Portal or T-SQL with TO URL.",
                            "purpose": "Create a tamper-resistant audit trail of who accessed sensitive customer data, meeting compliance requirements for data access logging.",
                            "breakdown": [
                                {"line": "CREATE SERVER AUDIT CustomerDataAudit TO URL (PATH = ...)", "meaning": "Defines an audit that writes to Azure Blob Storage. The PATH is the container URL. RETENTION_DAYS sets how long logs are kept."},
                                {"line": "QUEUE_DELAY = 1000", "meaning": "Milliseconds before audit records are flushed to storage. Lower = more real-time but more I/O. 0 means synchronous (most reliable but slower)."},
                                {"line": "ON_FAILURE = CONTINUE", "meaning": "If audit logging fails (e.g., storage is unavailable), SQL Server continues running. ON_FAILURE = SHUTDOWN would stop SQL Server if auditing fails — very strict compliance mode."},
                                {"line": "CREATE DATABASE AUDIT SPECIFICATION ... FOR SERVER AUDIT CustomerDataAudit", "meaning": "Creates the specification that says WHAT to log. Links to the server audit that defines WHERE to log."},
                                {"line": "ADD (SELECT, INSERT, UPDATE, DELETE ON dbo.Customers BY PUBLIC)", "meaning": "Audits SELECT, INSERT, UPDATE, DELETE on the Customers table for ALL users (PUBLIC). You can replace PUBLIC with a specific user or role name."},
                                {"line": "ADD (SCHEMA_OBJECT_ACCESS_GROUP)", "meaning": "An audit action GROUP that captures all schema object access events — a broader catch-all for any SELECT/INSERT/UPDATE/DELETE/EXECUTE on any object."},
                                {"line": "sys.fn_get_audit_file(...)", "meaning": "Table-valued function that reads audit log files and returns rows you can query with T-SQL. Very useful for compliance investigations."}
                            ],
                            "ssms_steps": [
                                "Open SSMS and connect with a sysadmin account",
                                "For Azure SQL: go to Azure Portal → SQL Database → Auditing → enable and set destination",
                                "For on-premises: run the CREATE SERVER AUDIT script in master database",
                                "Switch to your user database and run the CREATE DATABASE AUDIT SPECIFICATION script",
                                "Verify with the SELECT from sys.server_audits",
                                "To test: perform a SELECT on dbo.Customers, then wait a moment and read the audit file",
                                "In Azure Portal you can view audit logs under Diagnostics → Log Analytics"
                            ],
                            "exam_tip": "Remember the two-object model: SERVER AUDIT (where) + AUDIT SPECIFICATION (what). Both must be enabled (STATE = ON) for auditing to work. In Azure SQL Database, you can also enable auditing through the Azure Portal which simplifies the setup."
                        },
                        {
                            "type": "tip",
                            "title": "Azure SQL Auditing in the Portal",
                            "body": "For Azure SQL Database, the easiest way to configure auditing is through the <strong>Azure Portal</strong>: go to your SQL Database → Security → Auditing → toggle ON → choose Log Analytics, Event Hub, or Storage Account as the destination. The portal generates the underlying T-SQL automatically. You can also write custom audit policies with T-SQL for more granular control."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "In SQL Server auditing, what does the Server Audit object define?",
                            "opts": ["A. Which tables to audit", "B. Which users to audit", "C. Where audit logs are written (destination)", "D. Which SQL statements trigger an audit event"],
                            "correct": "C",
                            "explain": "The Server Audit defines the destination (file path, Azure Blob URL, Windows Event Log) and settings like queue delay and failure behavior. The Audit Specification defines what events to capture and links to the Server Audit."
                        },
                        {
                            "q": "What does ON_FAILURE = SHUTDOWN do in a Server Audit configuration?",
                            "opts": ["A. Shuts down SQL Server when an audit event is captured", "B. Shuts down SQL Server if audit logging fails — ensuring no unlogged activity", "C. Deletes old audit files when storage is full", "D. Disables the audit after the first failure"],
                            "correct": "B",
                            "explain": "ON_FAILURE = SHUTDOWN means that if the audit cannot write a record (e.g., storage is full or unavailable), SQL Server shuts down to ensure no activity goes unlogged. This is the highest compliance mode but risks service unavailability."
                        },
                        {
                            "q": "Which audit action group captures all SELECT, INSERT, UPDATE, DELETE activity on all database objects?",
                            "opts": ["A. DATABASE_OBJECT_CHANGE_GROUP", "B. SCHEMA_OBJECT_ACCESS_GROUP", "C. DATABASE_PRINCIPAL_CHANGE_GROUP", "D. OBJECT_PERMISSION_CHANGE_GROUP"],
                            "correct": "B",
                            "explain": "SCHEMA_OBJECT_ACCESS_GROUP captures any access to schema objects (tables, views, procedures) including SELECT, INSERT, UPDATE, DELETE, and EXECUTE. DATABASE_PRINCIPAL_CHANGE_GROUP captures user and role changes."
                        },
                        {
                            "q": "How do you read audit log files stored on disk using T-SQL?",
                            "opts": ["A. SELECT * FROM sys.server_audits", "B. OPENROWSET(BULK, ...)", "C. SELECT * FROM sys.fn_get_audit_file(path, DEFAULT, DEFAULT)", "D. BULK INSERT AuditTable FROM 'audit.sqlaudit'"],
                            "correct": "C",
                            "explain": "sys.fn_get_audit_file() is the built-in table-valued function for reading .sqlaudit files. Pass the file path (wildcards supported) and it returns rows with event_time, login, object accessed, and the statement executed."
                        },
                        {
                            "q": "For a DATABASE AUDIT SPECIFICATION to write audit records, what two objects must have STATE = ON?",
                            "opts": ["A. The Server Login and the Database User", "B. The Server Audit and the Database Audit Specification", "C. The Database Audit Specification and the SQL Agent job", "D. The Table and the Stored Procedure being audited"],
                            "correct": "B",
                            "explain": "Both the Server Audit (destination) and the Database Audit Specification (events) must be enabled with STATE = ON. If either is disabled, no audit records are written."
                        }
                    ]
                },

                # ── Unit 7: Secure AI service access ───────────────────
                {
                    "id": "lp2-m5-u7",
                    "title": "Secure AI service access",
                    "description": "Use Managed Identity and Azure AD authentication to securely connect SQL databases to Azure AI services.",
                    "estimated_time": 20,
                    "objectives": [
                        "Explain Managed Identity and why it eliminates stored credentials",
                        "Configure an Azure SQL Database to use Managed Identity for AI service calls",
                        "Understand Azure AD authentication vs SQL authentication"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Why Managed Identity Matters for AI Integration",
                            "body": "When SQL databases call external Azure AI services (like Azure OpenAI, Azure Cognitive Services, or REST APIs), they need credentials. The old way was to hardcode API keys or passwords in stored procedures or application code — this is a security risk because keys can be leaked in source control or logs.<br><br><strong>Managed Identity</strong> solves this. Azure automatically creates and rotates an identity for your SQL server/app. You never see or store credentials — Azure handles authentication automatically.<br><br><strong>Two types of Managed Identity:</strong><ul><li><strong>System-assigned</strong> — tied to the resource (e.g., the SQL Server). Created and deleted with the resource. One resource = one identity.</li><li><strong>User-assigned</strong> — a standalone Azure resource that can be shared across multiple services. More flexible for complex architectures.</li></ul><strong>How it works for SQL to AI service calls:</strong><ol><li>Enable Managed Identity on the Azure SQL Server</li><li>Grant the Managed Identity access to the AI service (e.g., 'Cognitive Services User' role)</li><li>In SQL code, use sp_invoke_external_rest_endpoint with Managed Identity authentication</li><li>No keys stored anywhere — Azure handles token exchange silently</li></ol>"
                        },
                        {
                            "type": "sql_block",
                            "title": "Call Azure OpenAI from SQL Using Managed Identity",
                            "scenario": "You want to call Azure OpenAI's completions API directly from a SQL stored procedure to analyze customer feedback text, using Managed Identity for authentication.",
                            "code": """-- Step 1: Enable system-assigned Managed Identity in Azure Portal
-- (Azure Portal → SQL Server → Identity → System assigned → On → Save)
-- The Identity gets an Object ID like: 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'

-- Step 2: Grant the Managed Identity access to Azure OpenAI
-- (Run in Azure Portal or Azure CLI — not T-SQL)
-- az role assignment create \
--   --assignee "<Object-ID-of-SQL-Server-Identity>" \
--   --role "Cognitive Services OpenAI User" \
--   --scope "/subscriptions/.../resourceGroups/.../providers/Microsoft.CognitiveServices/accounts/myopenai"

-- Step 3: Create a DATABASE SCOPED CREDENTIAL using Managed Identity
-- This tells SQL Server to use Managed Identity for the external endpoint
USE SalesDB;
GO

CREATE DATABASE SCOPED CREDENTIAL [https://myopenai.openai.azure.com/]
WITH IDENTITY = 'Managed Identity';
GO

-- Step 4: Call Azure OpenAI using sp_invoke_external_rest_endpoint
DECLARE @prompt NVARCHAR(MAX) = 'Analyze this customer review: "The product broke after 2 days. Very disappointed."';
DECLARE @requestBody NVARCHAR(MAX);
DECLARE @response NVARCHAR(MAX);

SET @requestBody = JSON_OBJECT(
    'messages': JSON_ARRAY(
        JSON_OBJECT('role': 'user', 'content': @prompt)
    ),
    'max_tokens': 200
);

EXEC sp_invoke_external_rest_endpoint
    @url = 'https://myopenai.openai.azure.com/openai/deployments/gpt-4/chat/completions?api-version=2024-02-01',
    @method = 'POST',
    @credential = [https://myopenai.openai.azure.com/],
    @payload = @requestBody,
    @response = @response OUTPUT;

-- Step 5: Parse the JSON response
SELECT
    JSON_VALUE(@response, '$.result.choices[0].message.content') AS AIAnalysis;
GO""",
                            "explanation": "Managed Identity authentication means no API keys in your code. The DATABASE SCOPED CREDENTIAL with IDENTITY = 'Managed Identity' tells SQL Server to request an Azure AD token for the endpoint automatically. sp_invoke_external_rest_endpoint (available in Azure SQL Database) handles the HTTP call.",
                            "purpose": "Call external Azure AI services from within SQL without storing API keys or passwords anywhere in the database.",
                            "breakdown": [
                                {"line": "CREATE DATABASE SCOPED CREDENTIAL WITH IDENTITY = 'Managed Identity'", "meaning": "Creates a credential that uses the server's Managed Identity to authenticate. The URL in the credential name must match the base URL of the external service."},
                                {"line": "sp_invoke_external_rest_endpoint", "meaning": "A built-in stored procedure in Azure SQL Database that makes HTTP calls to external REST APIs. Not available in on-premises SQL Server."},
                                {"line": "@credential = [https://myopenai.openai.azure.com/]", "meaning": "References the credential created above. SQL Server uses this credential to get an Azure AD bearer token and include it in the HTTP Authorization header."},
                                {"line": "JSON_VALUE(@response, '$.result.choices[0].message.content')", "meaning": "Parses the JSON response from OpenAI to extract the AI-generated text. Azure SQL has built-in JSON functions for this."}
                            ],
                            "ssms_steps": [
                                "Go to Azure Portal → your Azure SQL Server → Identity → enable System assigned Managed Identity",
                                "Copy the Object ID shown under the Identity panel",
                                "In Azure Portal → your Azure OpenAI resource → Access control (IAM) → Add role assignment",
                                "Assign 'Cognitive Services OpenAI User' role to the SQL Server's Managed Identity (paste the Object ID)",
                                "Open SSMS → New Query → run the CREATE DATABASE SCOPED CREDENTIAL statement",
                                "Run the sp_invoke_external_rest_endpoint call",
                                "Check the Results pane for the AIAnalysis value returned from OpenAI"
                            ],
                            "exam_tip": "The key exam concept: Managed Identity eliminates the need to store credentials. IDENTITY = 'Managed Identity' in a DATABASE SCOPED CREDENTIAL is the pattern for Azure SQL Database to call Azure services without API keys."
                        },
                        {
                            "type": "tip",
                            "title": "Azure AD Authentication for SQL Database",
                            "body": "Instead of SQL logins with passwords, use <strong>Azure Active Directory (Azure AD) authentication</strong> for your SQL databases:<ul><li>Supports Multi-Factor Authentication (MFA)</li><li>Centralized identity management</li><li>No password expiry management for SQL logins</li><li>Works with Azure AD groups for role management</li></ul>Enable it in Azure Portal: SQL Server → Azure Active Directory → Set admin → pick an Azure AD user or group."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What is the main security advantage of using Managed Identity over API keys for AI service access?",
                            "opts": ["A. Managed Identity is faster than API key authentication", "B. Credentials are never stored — Azure manages token exchange automatically", "C. Managed Identity works across all cloud providers", "D. Managed Identity gives access to all Azure services by default"],
                            "correct": "B",
                            "explain": "With Managed Identity, you never create, store, or rotate credentials. Azure automatically provides and manages the authentication token. This eliminates the risk of credentials being leaked in code, logs, or source control."
                        },
                        {
                            "q": "In sp_invoke_external_rest_endpoint, what does the IDENTITY = 'Managed Identity' in the credential definition do?",
                            "opts": ["A. Creates a new managed identity for the database", "B. Tells SQL Server to use the server's Azure AD managed identity for authentication", "C. Specifies the username for basic HTTP authentication", "D. Generates an API key for the external service"],
                            "correct": "B",
                            "explain": "When you create a DATABASE SCOPED CREDENTIAL with IDENTITY = 'Managed Identity', SQL Server knows to request an Azure AD OAuth token using the server's system-assigned or user-assigned managed identity. This token is sent in the Authorization header of the HTTP request."
                        },
                        {
                            "q": "What is the difference between system-assigned and user-assigned Managed Identity?",
                            "opts": ["A. System-assigned can access multiple resources; user-assigned is limited to one", "B. System-assigned is tied to one Azure resource and deleted with it; user-assigned is standalone and shareable", "C. System-assigned requires Azure AD Premium; user-assigned is free", "D. They are identical — just different naming conventions"],
                            "correct": "B",
                            "explain": "System-assigned Managed Identity is created and deleted with the Azure resource (e.g., the SQL Server). User-assigned Managed Identity is a standalone resource that can be assigned to multiple Azure services — useful when you want multiple services to share the same identity."
                        },
                        {
                            "q": "Which stored procedure in Azure SQL Database is used to call external REST APIs?",
                            "opts": ["A. sp_execute_external_script", "B. sp_invoke_external_rest_endpoint", "C. sp_call_rest_api", "D. xp_cmdshell"],
                            "correct": "B",
                            "explain": "sp_invoke_external_rest_endpoint is the Azure SQL Database built-in stored procedure for making HTTP/HTTPS calls to external REST APIs. It supports GET and POST methods and can use database scoped credentials for authentication."
                        },
                        {
                            "q": "Where do you enable a system-assigned Managed Identity for an Azure SQL Server?",
                            "opts": ["A. In SSMS under Server Properties → Security", "B. In the SQL database's Transparent Data Encryption settings", "C. In Azure Portal → SQL Server → Identity → System assigned → On", "D. By running CREATE MANAGED IDENTITY in T-SQL"],
                            "correct": "C",
                            "explain": "Managed Identity is an Azure resource-level feature configured in the Azure Portal (or via Azure CLI/PowerShell). Navigate to your Azure SQL Server resource → Identity → toggle System assigned to On → Save."
                        }
                    ]
                },

                # ── Unit 8: Secure data API endpoints ──────────────────
                {
                    "id": "lp2-m5-u8",
                    "title": "Secure data API endpoints",
                    "description": "Secure Data API Builder endpoints with HTTPS, Azure AD authentication, and API keys.",
                    "estimated_time": 20,
                    "objectives": [
                        "Configure authentication in Data API Builder",
                        "Require HTTPS for all API traffic",
                        "Use Azure AD tokens and API keys as authentication options"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Securing Data API Builder Endpoints",
                            "body": "Data API Builder (DAB) automatically generates REST and GraphQL endpoints from your SQL database. Without proper security, anyone with the URL could read or modify your data.<br><br><strong>Security options in DAB:</strong><ul><li><strong>HTTPS only</strong> — always require encrypted connections; never allow HTTP in production</li><li><strong>Azure AD authentication</strong> — require a valid Azure AD bearer token in the Authorization header. Best for enterprise scenarios.</li><li><strong>API Keys</strong> — a shared secret in the request header. Simpler but less secure than Azure AD tokens. Suitable for service-to-service calls in trusted networks.</li><li><strong>Anonymous access</strong> — no authentication (only for public read-only data)</li></ul>Security is configured in the <strong>dab-config.json</strong> file under the <code>runtime.authentication</code> section."
                        },
                        {
                            "type": "sql_block",
                            "title": "Configure Authentication in dab-config.json",
                            "scenario": "You are deploying Data API Builder for a customer-facing API. You need Azure AD authentication so only your company's Azure AD users can access the API.",
                            "code": """{
  "$schema": "https://dataapibuilder.azureedge.net/schemas/v1.3.0/dab.draft.schema.json",
  "data-source": {
    "database-type": "mssql",
    "connection-string": "@env('DATABASE_CONNECTION_STRING')"
  },
  "runtime": {
    "rest": {
      "enabled": true,
      "path": "/api"
    },
    "graphql": {
      "enabled": true,
      "path": "/graphql"
    },
    "host": {
      "mode": "production",
      "cors": {
        "origins": ["https://myapp.contoso.com"],
        "allow-credentials": true
      },
      "authentication": {
        "provider": "AzureAD",
        "jwt": {
          "audience": "api://my-api-client-id",
          "issuer": "https://login.microsoftonline.com/my-tenant-id/v2.0"
        }
      }
    }
  },
  "entities": {
    "Customer": {
      "source": "dbo.Customers",
      "permissions": [
        {
          "role": "authenticated",
          "actions": ["read"]
        },
        {
          "role": "admin",
          "actions": ["create", "read", "update", "delete"]
        }
      ]
    }
  }
}""",
                            "explanation": "The authentication section in dab-config.json configures Azure AD JWT token validation. The audience must match the App Registration's application ID URI, and the issuer must match the tenant's identity provider URL. This ensures only valid Azure AD tokens from your tenant are accepted.",
                            "purpose": "Protect the auto-generated SQL API endpoints so only authenticated users from your Azure AD tenant can access them.",
                            "breakdown": [
                                {"line": "\"connection-string\": \"@env('DATABASE_CONNECTION_STRING')\"", "meaning": "References an environment variable rather than hardcoding the connection string. Never store connection strings or passwords directly in config files."},
                                {"line": "\"mode\": \"production\"", "meaning": "Disables developer features like detailed error messages and the built-in Swagger UI that expose schema information. Always use production mode when deploying publicly."},
                                {"line": "\"provider\": \"AzureAD\"", "meaning": "Tells DAB to require Azure AD JWT bearer tokens for authentication. Every API request must include an Authorization: Bearer <token> header."},
                                {"line": "\"audience\": \"api://my-api-client-id\"", "meaning": "The expected 'aud' claim in the JWT token. Must match the Application ID URI of your App Registration in Azure AD. Prevents tokens from other apps being used."},
                                {"line": "\"issuer\": \"https://login.microsoftonline.com/my-tenant-id/v2.0\"", "meaning": "The expected 'iss' claim in the JWT token. Must match your Azure AD tenant's issuer URL. Prevents tokens from other tenants being used."},
                                {"line": "\"role\": \"authenticated\", \"actions\": [\"read\"]", "meaning": "Grants read-only access to any authenticated user. The 'authenticated' role is a built-in DAB role assigned to any user with a valid token."},
                                {"line": "\"role\": \"admin\", \"actions\": [\"create\", \"read\", \"update\", \"delete\"]", "meaning": "Full CRUD access for users in the 'admin' role. Map this to an Azure AD group or app role in your App Registration."}
                            ],
                            "ssms_steps": [
                                "This is a DAB configuration task, not SSMS. Open your dab-config.json file in VS Code",
                                "In Azure Portal, create an App Registration for your API: Azure AD → App registrations → New registration",
                                "Copy the Application (client) ID — this becomes your audience value",
                                "Copy the Directory (tenant) ID — use this in the issuer URL",
                                "Update the dab-config.json with your audience and issuer values",
                                "Set the DATABASE_CONNECTION_STRING environment variable in your deployment environment",
                                "Run: dab start --config dab-config.json",
                                "Test: call the API without a token — you should get 401 Unauthorized",
                                "Get an Azure AD token for your user and call again with Authorization: Bearer <token> — you should get 200 OK"
                            ],
                            "exam_tip": "Key config pattern for the exam: connection strings go in environment variables (@env()), not in the config file. authentication.provider = 'AzureAD' requires JWT validation. Never use StaticWebApps authentication provider in production without proper configuration."
                        },
                        {
                            "type": "important",
                            "title": "HTTPS Is Non-Negotiable",
                            "body": "Always use HTTPS for API endpoints in production. HTTP transmits tokens and data in plaintext — anyone on the network can intercept them. In Azure services (App Service, Container Apps), HTTPS is enforced by default. For local development with DAB, use the --no-https flag only, never in production.<br><br>Also configure CORS (Cross-Origin Resource Sharing) to only allow requests from your known frontend domains. Never set CORS origins to '*' in production."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "In Data API Builder's dab-config.json, where is authentication configured?",
                            "opts": ["A. Under the entities section per table", "B. Under runtime.host.authentication", "C. Under data-source.security", "D. In a separate auth-config.json file"],
                            "correct": "B",
                            "explain": "Authentication in DAB is configured under runtime.host.authentication in dab-config.json. This sets the authentication provider (AzureAD, StaticWebApps, etc.) and JWT validation settings (audience, issuer)."
                        },
                        {
                            "q": "What does setting host.mode to 'production' do in Data API Builder?",
                            "opts": ["A. Enables detailed error messages for debugging", "B. Disables developer features and hides schema information from error responses", "C. Switches to a production database connection", "D. Enables automatic TDE encryption"],
                            "correct": "B",
                            "explain": "Production mode disables developer conveniences that could expose sensitive information: detailed error messages that reveal schema, and the built-in Swagger UI. Always use production mode for deployed APIs."
                        },
                        {
                            "q": "Why should you use @env('DATABASE_CONNECTION_STRING') instead of a literal connection string in dab-config.json?",
                            "opts": ["A. Environment variables are faster to read than config file values", "B. It avoids storing passwords in the config file which might be committed to source control", "C. DAB requires environment variables for all string values", "D. Literal connection strings do not work in Azure"],
                            "correct": "B",
                            "explain": "Storing connection strings or passwords in config files risks accidental exposure — especially if the file is committed to a git repository. Environment variables are injected at runtime and kept in secure configuration systems (Azure App Service settings, Key Vault references, etc.)."
                        },
                        {
                            "q": "In a DAB entity permissions block, what does the 'authenticated' role represent?",
                            "opts": ["A. Only users in the Azure AD 'authenticated' security group", "B. Any user who has presented a valid authentication token", "C. The database owner account", "D. Users who have passed through multi-factor authentication"],
                            "correct": "B",
                            "explain": "In Data API Builder, 'authenticated' is a built-in role that applies to any request with a valid authentication token (regardless of what Azure AD roles or groups the user belongs to). It is the baseline role for all logged-in users."
                        },
                        {
                            "q": "What does the 'audience' value in the JWT authentication configuration validate?",
                            "opts": ["A. That the token was issued for the correct API (application ID)", "B. The name of the Azure AD tenant", "C. The expiry time of the token", "D. The username of the authenticated user"],
                            "correct": "A",
                            "explain": "The 'audience' (aud) claim in a JWT identifies the intended recipient of the token. DAB validates that the token's audience matches the configured value (your API's Application ID URI). This prevents tokens issued for other applications from being used to access your API."
                        }
                    ]
                },

                # ── Unit 9: Exercise ────────────────────────────────────
                {
                    "id": "lp2-m5-u9",
                    "title": "Exercise",
                    "description": "Hands-on exercise: implement a complete security solution for a healthcare SQL database.",
                    "estimated_time": 45,
                    "objectives": [
                        "Apply TDE, Dynamic Data Masking, Row-Level Security, and Auditing together",
                        "Test each security layer by querying as different users"
                    ],
                    "content": [
                        {
                            "type": "sql_block",
                            "title": "Exercise: Secure a Patient Records Database",
                            "scenario": "A healthcare company has a PatientRecords database. You must implement: (1) TDE for at-rest encryption, (2) DDM on the SSN column, (3) RLS so doctors only see their own patients, and (4) Auditing all SELECT on the PatientRecords table.",
                            "code": """-- ============================================================
-- EXERCISE: Complete Healthcare Database Security Setup
-- ============================================================

-- SETUP: Create the database and table
USE master;
GO
-- (Assume TDE is already enabled in Azure SQL Database by default)

USE PatientRecords;
GO

CREATE TABLE dbo.Patients (
    PatientID    INT IDENTITY(1,1) PRIMARY KEY,
    FirstName    NVARCHAR(100),
    LastName     NVARCHAR(100),
    SSN          CHAR(11),
    Diagnosis    NVARCHAR(500),
    DoctorName   NVARCHAR(100)    -- stores the doctor's username
);
GO

-- PART 1: Dynamic Data Masking on SSN
ALTER TABLE dbo.Patients
    ALTER COLUMN SSN
    ADD MASKED WITH (FUNCTION = 'partial(0, "XXX-XX-", 4)');
GO

-- PART 2: Row-Level Security so doctors see only their patients
CREATE SCHEMA Security;
GO

CREATE FUNCTION Security.fn_PatientFilter(@DoctorName NVARCHAR(100))
RETURNS TABLE
WITH SCHEMABINDING
AS
RETURN
    SELECT 1 AS result
    WHERE @DoctorName = USER_NAME()
       OR IS_MEMBER('db_owner') = 1;  -- admins see all
GO

CREATE SECURITY POLICY PatientRLSPolicy
ADD FILTER PREDICATE Security.fn_PatientFilter(DoctorName)
    ON dbo.Patients
WITH (STATE = ON);
GO

-- PART 3: Auditing SELECT on the Patients table
-- (In Azure SQL Database, configure via Portal or T-SQL to Log Analytics)
CREATE SERVER AUDIT PatientAudit
TO URL (PATH = 'https://healthstorage.blob.core.windows.net/auditlogs',
        RETENTION_DAYS = 365)
WITH (ON_FAILURE = CONTINUE);
GO
ALTER SERVER AUDIT PatientAudit WITH (STATE = ON);
GO

CREATE DATABASE AUDIT SPECIFICATION AuditPatientAccess
FOR SERVER AUDIT PatientAudit
ADD (SELECT ON dbo.Patients BY PUBLIC);
GO
ALTER DATABASE AUDIT SPECIFICATION AuditPatientAccess WITH (STATE = ON);
GO

-- PART 4: Create test users and grant access
CREATE USER DrSmith WITHOUT LOGIN;
CREATE USER DrJones WITHOUT LOGIN;
GRANT SELECT ON dbo.Patients TO DrSmith, DrJones;
GO

-- PART 5: Insert test data
INSERT INTO dbo.Patients (FirstName, LastName, SSN, Diagnosis, DoctorName)
VALUES
('Alice', 'Cooper',  '123-45-6789', 'Hypertension',    'DrSmith'),
('Bob',   'Dylan',   '987-65-4321', 'Type 2 Diabetes', 'DrSmith'),
('Carol', 'King',    '456-78-9012', 'Asthma',          'DrJones');
GO

-- TEST 1: DrSmith sees only Alice and Bob (his patients), SSN masked
EXECUTE AS USER = 'DrSmith';
SELECT PatientID, FirstName, LastName, SSN, Diagnosis FROM dbo.Patients;
-- Expected: 2 rows, SSN = 'XXX-XX-6789' and 'XXX-XX-4321'
REVERT;
GO

-- TEST 2: DrJones sees only Carol, SSN masked
EXECUTE AS USER = 'DrJones';
SELECT PatientID, FirstName, LastName, SSN, Diagnosis FROM dbo.Patients;
-- Expected: 1 row, SSN = 'XXX-XX-9012'
REVERT;
GO

-- TEST 3: Admin (db_owner) sees all 3 patients with real SSN
-- (db_owner bypasses RLS and DDM)
SELECT PatientID, FirstName, LastName, SSN, Diagnosis, DoctorName
FROM dbo.Patients;
-- Expected: 3 rows with real SSN values
GO""",
                            "explanation": "This exercise stacks three security layers: DDM hides SSN values, RLS filters rows to each doctor's patients, and auditing logs every SELECT for compliance. Each layer is independent — all three work together simultaneously.",
                            "purpose": "Practice implementing defense-in-depth security for sensitive healthcare data combining multiple SQL security features.",
                            "breakdown": [
                                {"line": "partial(0, 'XXX-XX-', 4)", "meaning": "Shows no prefix characters, then 'XXX-XX-', then the last 4 digits. So '123-45-6789' shows as 'XXX-XX-6789'."},
                                {"line": "IS_MEMBER('db_owner') = 1", "meaning": "Returns 1 if the current user is a member of the db_owner role. This is the admin bypass condition in the RLS predicate."},
                                {"line": "RETENTION_DAYS = 365", "meaning": "Keeps audit logs for 1 year in blob storage. Healthcare regulations often require multi-year audit retention."}
                            ],
                            "ssms_steps": [
                                "Open SSMS and connect to Azure SQL Database (or a local SQL Server 2016+)",
                                "Create a new database called PatientRecords or use an existing test database",
                                "Run the SETUP block to create the Patients table",
                                "Run PART 1 to add the DDM mask on SSN",
                                "Run PART 2 to create the Security schema, predicate function, and security policy",
                                "For PART 3: if using Azure SQL, configure auditing in the Azure Portal instead (Diagnostics → Log Analytics is easier)",
                                "Run PART 4 to create test users and grant permissions",
                                "Run PART 5 to insert test data",
                                "Run each TEST block and verify the results match the expected output in the comments"
                            ],
                            "exam_tip": "This exercise shows the defense-in-depth approach the exam expects you to understand. Each layer independently protects data: TDE (files), DDM (column values), RLS (row visibility), Auditing (activity logging). They complement each other."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "In the exercise, DrSmith queries the Patients table. Which security layers affect what he sees?",
                            "opts": ["A. Only TDE", "B. RLS filters rows; DDM masks SSN values", "C. DDM only — RLS requires Admin setup", "D. TDE, DDM, and RLS all apply simultaneously"],
                            "correct": "B",
                            "explain": "TDE is transparent to queries — it protects files on disk. When DrSmith runs SELECT, RLS filters out rows for other doctors, and DDM masks the SSN column values in the rows he can see."
                        },
                        {
                            "q": "In the RLS predicate function, what does IS_MEMBER('db_owner') = 1 accomplish?",
                            "opts": ["A. It creates a new member in the db_owner role", "B. It provides an admin bypass so db_owners can see all rows", "C. It checks if the current user is named 'db_owner'", "D. It grants the db_owner role to the current user"],
                            "correct": "B",
                            "explain": "IS_MEMBER('db_owner') = 1 returns true if the current user is in the db_owner role. Including this in the RLS predicate ensures administrators can see all rows without the row filter being applied to them."
                        },
                        {
                            "q": "You add a new doctor, DrBrown, with GRANT SELECT on dbo.Patients. DrBrown has no patients yet. What happens when she runs SELECT * FROM dbo.Patients?",
                            "opts": ["A. She sees all patients because she has SELECT permission", "B. She gets an error because RLS denies access", "C. She gets 0 rows returned — RLS filters all rows because none match her username", "D. She sees only rows where DoctorName IS NULL"],
                            "correct": "C",
                            "explain": "RLS FILTER PREDICATE silently removes rows that fail the predicate. DrBrown (USER_NAME() = 'DrBrown') has no rows where DoctorName = 'DrBrown', so the predicate returns nothing for her and she gets an empty result set — not an error."
                        },
                        {
                            "q": "RETENTION_DAYS = 365 in the Server Audit configuration means what?",
                            "opts": ["A. Audit logs are deleted after 1 year", "B. Audit logs are kept in blob storage for up to 1 year", "C. Audit runs for 365 days then auto-disables", "D. Only the last 365 audit records are kept"],
                            "correct": "B",
                            "explain": "RETENTION_DAYS controls how long Azure Blob Storage keeps the audit log files before automatically deleting them. 365 days = 1 year of audit history, which satisfies many regulatory requirements."
                        },
                        {
                            "q": "Which of the four security layers in this exercise protects against a stolen backup file being attached to another SQL Server?",
                            "opts": ["A. Dynamic Data Masking", "B. Row-Level Security", "C. Auditing", "D. Transparent Data Encryption (TDE)"],
                            "correct": "D",
                            "explain": "TDE encrypts the physical database files (.mdf, .ldf) and backup files. If someone steals a backup and tries to attach it to another SQL Server, the backup is unreadable without the TDE certificate. DDM, RLS, and Auditing are query-level protections that require a running SQL Server session."
                        }
                    ]
                },

                # ── Unit 10: Module Assessment ──────────────────────────
                {
                    "id": "lp2-m5-u10",
                    "title": "Module assessment",
                    "description": "Test your understanding of all SQL security and compliance topics from this module.",
                    "estimated_time": 20,
                    "objectives": [
                        "Demonstrate understanding of encryption, masking, RLS, permissions, and auditing",
                        "Apply security concepts to realistic scenarios"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Module 5 Security Concepts Review",
                            "body": "Before taking the assessment, review these key security concepts:<br><br><strong>Encryption:</strong><ul><li>TDE — encrypts database files and backups. ON by default in Azure SQL. Requires backing up the TDE certificate.</li><li>Always Encrypted — column-level, client-side encryption. Deterministic = searchable. Randomized = more secure. Keys never in SQL Server.</li></ul><strong>Access Control:</strong><ul><li>DDM — masks column values at query time. UNMASK permission to see real data. Not a security boundary against privileged users.</li><li>RLS — filters rows using a TVF predicate + security policy. FILTER for SELECT. BLOCK for writes. db_owner bypasses RLS.</li><li>GRANT/DENY/REVOKE — DENY always wins. db_datareader = SELECT all. db_datawriter = write all.</li></ul><strong>Auditing:</strong><ul><li>SERVER AUDIT (where) + AUDIT SPECIFICATION (what) = both must be ON.</li><li>SCHEMA_OBJECT_ACCESS_GROUP audits all table access.</li><li>sys.fn_get_audit_file() to read log files.</li></ul><strong>Modern Auth:</strong><ul><li>Managed Identity = no stored credentials for Azure service-to-service calls.</li><li>IDENTITY = 'Managed Identity' in DATABASE SCOPED CREDENTIAL.</li><li>DAB config: runtime.host.authentication for Azure AD JWT validation.</li></ul>"
                        }
                    ],
                    "quiz": [
                        {
                            "q": "A compliance requirement states that database backup files must be encrypted. Which feature addresses this?",
                            "opts": ["A. Dynamic Data Masking", "B. Always Encrypted", "C. Transparent Data Encryption (TDE)", "D. Row-Level Security"],
                            "correct": "C",
                            "explain": "TDE encrypts database files and all backup files at rest. If a backup is stolen, it is unreadable without the TDE certificate. TDE does this automatically — the backup process does not need to change."
                        },
                        {
                            "q": "A healthcare app must ensure that even the database administrator cannot read patient SSN values. Which feature should you use?",
                            "opts": ["A. TDE with AES-256", "B. Dynamic Data Masking with default() function", "C. Always Encrypted with randomized encryption", "D. Row-Level Security with BLOCK predicate"],
                            "correct": "C",
                            "explain": "Always Encrypted is the only feature that prevents DBAs from reading plaintext column values. Encryption happens client-side and the SQL Server engine only sees ciphertext. TDE and DDM can be bypassed by privileged users."
                        },
                        {
                            "q": "You want to prevent a salesperson from seeing other salespeople's commission data without modifying any application queries. Which feature is best?",
                            "opts": ["A. GRANT/DENY at table level", "B. Dynamic Data Masking", "C. Always Encrypted", "D. Row-Level Security with FILTER PREDICATE"],
                            "correct": "D",
                            "explain": "RLS FILTER PREDICATE automatically filters rows at the database engine level based on the current user's identity. No application query changes are needed — the filter is applied transparently. DDM would not hide rows, just mask column values."
                        },
                        {
                            "q": "An audit log shows SELECT events on the Customers table. Which two objects had to have STATE = ON for these records to be captured?",
                            "opts": ["A. The table and the stored procedure", "B. The Server Audit and the Database Audit Specification", "C. The login and the database user", "D. The TDE certificate and the master key"],
                            "correct": "B",
                            "explain": "SQL Server Auditing requires both: (1) Server Audit (defines destination, must be ON) and (2) Database/Server Audit Specification (defines events, must be ON). If either is disabled, no audit records are written."
                        },
                        {
                            "q": "Which T-SQL statement explicitly removes a previously granted permission and returns it to a neutral state?",
                            "opts": ["A. DENY SELECT ON table TO user", "B. DROP GRANT SELECT ON table FROM user", "C. REVOKE SELECT ON table FROM user", "D. REMOVE GRANT SELECT ON table FROM user"],
                            "correct": "C",
                            "explain": "REVOKE removes a previously granted or denied permission, returning it to a neutral 'no explicit permission' state. The user may still have access through role membership. DENY would actively block access."
                        }
                    ]
                },

                # ── Unit 11: Summary ────────────────────────────────────
                {
                    "id": "lp2-m5-u11",
                    "title": "Summary",
                    "description": "Review key security concepts and techniques covered in this module.",
                    "estimated_time": 5,
                    "objectives": [
                        "Recall the main SQL security features and their purposes"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Module 5 Summary — SQL Security and Compliance",
                            "body": "In this module you learned the following SQL security techniques:<br><br><ul><li><strong>Transparent Data Encryption (TDE)</strong> — Encrypts database files and backups at rest. Default ON in Azure SQL. Requires certificate backup. <code>ALTER DATABASE ... SET ENCRYPTION ON</code></li><li><strong>Always Encrypted</strong> — Client-side column encryption. Deterministic (searchable) vs Randomized (more secure). Column Master Key lives in Azure Key Vault, never in SQL Server.</li><li><strong>Dynamic Data Masking (DDM)</strong> — Masks column values at query time. Four functions: default(), email(), random(), partial(). GRANT UNMASK to show real data. Configured with <code>ALTER TABLE ... ALTER COLUMN ... ADD MASKED WITH</code></li><li><strong>Row-Level Security (RLS)</strong> — Filters rows per user. Requires a TVF predicate function + security policy. FILTER PREDICATE (SELECT) and BLOCK PREDICATE (writes). db_owner bypasses RLS.</li><li><strong>GRANT/DENY/REVOKE</strong> — Permission management. DENY always overrides GRANT. Built-in roles: db_datareader, db_datawriter, db_owner. Contained users for portable Azure SQL databases.</li><li><strong>SQL Auditing</strong> — Server Audit (where) + Audit Specification (what). Both must be ON. Use sys.fn_get_audit_file() to read logs. SCHEMA_OBJECT_ACCESS_GROUP captures all table access.</li><li><strong>Managed Identity</strong> — Credential-free authentication for SQL to Azure service calls. IDENTITY = 'Managed Identity' in DATABASE SCOPED CREDENTIAL. Used with sp_invoke_external_rest_endpoint.</li><li><strong>Secure API Endpoints</strong> — Data API Builder config: runtime.host.authentication for Azure AD JWT. Use @env() for connection strings. production mode disables schema exposure.</li></ul>"
                        }
                    ],
                    "quiz": [
                        {
                            "q": "Which security feature prevents data from being read even if the database backup file is stolen?",
                            "opts": ["A. Row-Level Security", "B. Dynamic Data Masking", "C. Transparent Data Encryption", "D. Always Encrypted"],
                            "correct": "C",
                            "explain": "TDE encrypts the physical database and backup files. A stolen backup file cannot be read without the TDE certificate from the original server."
                        },
                        {
                            "q": "Which command adds a mask to an existing column in a table?",
                            "opts": ["A. UPDATE TABLE ... SET COLUMN ... MASKED", "B. ALTER TABLE ... ALTER COLUMN ... ADD MASKED WITH (FUNCTION = ...)", "C. CREATE MASK ON TABLE.COLUMN", "D. MODIFY COLUMN ... SET MASK = 'default()'"],
                            "correct": "B",
                            "explain": "The correct syntax is: ALTER TABLE <table> ALTER COLUMN <column> ADD MASKED WITH (FUNCTION = '<mask_function>'). This adds DDM to an existing column without changing the stored data."
                        },
                        {
                            "q": "What must you create along with a predicate function to activate Row-Level Security?",
                            "opts": ["A. A trigger", "B. A security policy", "C. A database role", "D. A server audit"],
                            "correct": "B",
                            "explain": "RLS requires two objects: (1) an inline table-valued function (the predicate logic) and (2) a SECURITY POLICY that binds the predicate function to a table. Without the policy, the function has no effect."
                        },
                        {
                            "q": "What is the purpose of DATABASE SCOPED CREDENTIAL with IDENTITY = 'Managed Identity'?",
                            "opts": ["A. Creates a new Azure AD managed identity", "B. Stores the SQL Server login password in the database", "C. Enables SQL Server to authenticate to external services using the server's Azure AD identity", "D. Grants managed identity access to all database tables"],
                            "correct": "C",
                            "explain": "DATABASE SCOPED CREDENTIAL with IDENTITY = 'Managed Identity' tells SQL Server (specifically Azure SQL) to use the server's system-assigned or user-assigned Managed Identity to get an Azure AD bearer token when calling external REST APIs."
                        },
                        {
                            "q": "In Always Encrypted, which encryption type should you choose for a column you need to search with WHERE clauses?",
                            "opts": ["A. Randomized", "B. AES-256", "C. Deterministic", "D. RSA-2048"],
                            "correct": "C",
                            "explain": "Deterministic encryption always produces the same ciphertext for the same plaintext, so SQL Server can compare ciphertext values to evaluate equality predicates in WHERE clauses. Randomized encryption produces different ciphertext each time and cannot be searched."
                        }
                    ]
                }
            ]
        },

        # ══════════════════════════════════════════════════════════════
        # MODULE lp2-m6: Optimize database performance
        # ══════════════════════════════════════════════════════════════
        {
            "id": "lp2-m6",
            "title": "Optimize database performance",
            "description": "Learn to tune SQL database performance through configuration, isolation levels, execution plans, Query Store, and deadlock resolution.",
            "units": [

                # ── Unit 1: Introduction ────────────────────────────────
                {
                    "id": "lp2-m6-u1",
                    "title": "Introduction",
                    "description": "Overview of SQL Server performance optimization topics in this module.",
                    "estimated_time": 5,
                    "objectives": [
                        "Understand what database performance optimization involves",
                        "Preview the topics: configuration, isolation levels, execution plans, Query Store, blocking"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Why Database Performance Matters",
                            "body": "A slow database is one of the most common causes of application performance problems. Users complain, reports time out, and business decisions are delayed. Understanding SQL Server performance optimization is critical for the DP-800 exam and for real-world database work.<br><br>In this module you will learn:<ul><li><strong>Database configuration</strong> — compatibility level, MAXDOP, memory settings that affect how SQL Server uses hardware</li><li><strong>Transaction isolation levels</strong> — controlling how queries handle concurrent access and balancing consistency vs performance</li><li><strong>Execution plans and DMVs</strong> — reading SQL Server's query plan to understand why a query is slow</li><li><strong>Query Store</strong> — capturing query performance history and forcing good execution plans</li><li><strong>Blocking and deadlocks</strong> — detecting and resolving queries that wait for each other</li></ul>By the end, you will be able to diagnose common performance problems and apply targeted fixes."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What is the primary purpose of reviewing execution plans for performance tuning?",
                            "opts": ["A. To see which users ran a query", "B. To understand how SQL Server physically retrieves data and identify inefficiencies", "C. To encrypt slow queries", "D. To see the query's audit log"],
                            "correct": "B",
                            "explain": "Execution plans show the physical operations SQL Server uses to retrieve data (index scans, key lookups, hash joins, etc.) and their estimated costs. This helps identify why a query is slow — e.g., a missing index causing a full table scan."
                        },
                        {
                            "q": "What does MAXDOP stand for in SQL Server configuration?",
                            "opts": ["A. Maximum Database Operations Per second", "B. Maximum Degree of Parallelism", "C. Maximum Disk Operations Per query", "D. Maximum Data Output Parameter"],
                            "correct": "B",
                            "explain": "MAXDOP (Maximum Degree of Parallelism) controls how many CPU cores SQL Server can use to execute a single query in parallel. Setting it appropriately prevents one large query from consuming all CPUs."
                        },
                        {
                            "q": "What is a 'deadlock' in SQL Server?",
                            "opts": ["A. A query that runs for too long", "B. Two sessions each waiting for the other to release a lock", "C. A database that has run out of disk space", "D. A query blocked by an index rebuild"],
                            "correct": "B",
                            "explain": "A deadlock occurs when Session A holds lock X and wants lock Y, while Session B holds lock Y and wants lock X. Neither can proceed. SQL Server detects this and terminates one session as the 'deadlock victim'."
                        },
                        {
                            "q": "Which SQL Server feature captures a history of query execution statistics to help identify plan regressions?",
                            "opts": ["A. SQL Agent", "B. Dynamic Management Views (DMVs)", "C. Query Store", "D. Extended Events"],
                            "correct": "C",
                            "explain": "Query Store automatically captures query text, execution plans, and runtime statistics (CPU, duration, reads) over time. It allows you to see if a query's performance changed (plan regression) and force the previous better plan."
                        },
                        {
                            "q": "Which isolation level allows a query to read data that another transaction has modified but not yet committed?",
                            "opts": ["A. READ COMMITTED", "B. SERIALIZABLE", "C. READ UNCOMMITTED", "D. REPEATABLE READ"],
                            "correct": "C",
                            "explain": "READ UNCOMMITTED (also achievable with the NOLOCK hint) allows dirty reads — reading data from uncommitted transactions. This maximizes concurrency but risks reading data that may be rolled back."
                        }
                    ]
                },

                # ── Unit 2: Database configurations for performance ─────
                {
                    "id": "lp2-m6-u2",
                    "title": "Database configurations for performance",
                    "description": "Configure SQL Server settings that impact query performance: compatibility level, MAXDOP, memory, and cost threshold.",
                    "estimated_time": 25,
                    "objectives": [
                        "Change database compatibility level",
                        "Configure MAXDOP and cost threshold for parallelism",
                        "Understand memory configuration options"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Key SQL Server Performance Settings",
                            "body": "SQL Server has several configuration settings that affect how it executes queries. Getting these right is foundational for performance.<br><br><strong>Compatibility Level</strong> — controls which version of the SQL Server query optimizer features are used. Higher = newer optimizer, better estimates, new features. Changing this can improve performance but may change query behavior. Set with ALTER DATABASE.<br><br><strong>MAXDOP (Maximum Degree of Parallelism)</strong> — controls how many CPU cores a single query can use. Default of 0 = use all CPUs, which can starve other sessions. Recommended: set to half the number of CPUs, max 8 on OLTP systems.<br><br><strong>Cost Threshold for Parallelism</strong> — queries must have an estimated cost above this value to use parallel execution. Default is 5 (very low — almost all queries go parallel). Raise to 50 to prevent short queries from going parallel unnecessarily.<br><br><strong>Max Server Memory</strong> — SQL Server takes as much memory as available by default, leaving none for the OS. Always set max server memory to leave 10-20% for the OS."
                        },
                        {
                            "type": "sql_block",
                            "title": "Configure Performance Settings",
                            "scenario": "You have an 8-core SQL Server with 32GB RAM running OLTP workloads. Configure it for optimal performance.",
                            "code": """-- Step 1: Check current compatibility level
SELECT name, compatibility_level
FROM sys.databases
WHERE name = 'SalesDB';
GO

-- Step 2: Upgrade compatibility level to SQL Server 2022 (160)
-- This unlocks newer optimizer features
ALTER DATABASE SalesDB
SET COMPATIBILITY_LEVEL = 160;
GO
-- Common levels: 130=2016, 140=2017, 150=2019, 160=2022

-- Step 3: Configure server-level settings using sp_configure
-- First, enable advanced options
EXEC sp_configure 'show advanced options', 1;
RECONFIGURE;
GO

-- Step 4: Set MAXDOP to 4 (half of 8 cores, good for OLTP)
EXEC sp_configure 'max degree of parallelism', 4;
RECONFIGURE;
GO

-- Step 5: Raise cost threshold for parallelism
-- Default is 5 (too low). Set to 50 to reduce unnecessary parallelism
EXEC sp_configure 'cost threshold for parallelism', 50;
RECONFIGURE;
GO

-- Step 6: Set max server memory (32GB server, leave 4GB for OS)
-- 28GB in MB = 28672 MB
EXEC sp_configure 'max server memory (MB)', 28672;
RECONFIGURE;
GO

-- Step 7: Set MAXDOP at DATABASE level (overrides server setting for this DB)
-- Available in SQL Server 2019+ and Azure SQL Database
ALTER DATABASE SCOPED CONFIGURATION
    SET MAXDOP = 2;    -- this DB uses max 2 CPUs per query
GO

-- Step 8: Check current sp_configure settings
SELECT name, value, value_in_use, description
FROM sys.configurations
WHERE name IN (
    'max degree of parallelism',
    'cost threshold for parallelism',
    'max server memory (MB)'
);
GO

-- Step 9: Enable READ_COMMITTED_SNAPSHOT for better concurrency
-- This eliminates most blocking without changing application code
ALTER DATABASE SalesDB
    SET READ_COMMITTED_SNAPSHOT ON;
GO""",
                            "explanation": "These settings are configured at server level with sp_configure (affects all databases) or at database level with ALTER DATABASE / ALTER DATABASE SCOPED CONFIGURATION (affects one database). READ_COMMITTED_SNAPSHOT is particularly impactful for OLTP performance.",
                            "purpose": "Set foundational SQL Server configuration parameters that prevent common performance bottlenecks like excessive parallelism, memory pressure, and lock contention.",
                            "breakdown": [
                                {"line": "ALTER DATABASE SalesDB SET COMPATIBILITY_LEVEL = 160", "meaning": "Updates the database to use SQL Server 2022 query optimizer features. Can improve cardinality estimation and query plans. Test thoroughly before changing in production."},
                                {"line": "sp_configure 'max degree of parallelism', 4", "meaning": "Sets MAXDOP server-wide to 4. A single query can use at most 4 CPU cores in parallel. Prevents a heavy analytics query from starving all other OLTP queries."},
                                {"line": "sp_configure 'cost threshold for parallelism', 50", "meaning": "A query must have estimated cost >= 50 to be eligible for parallel execution. The default value of 5 causes almost all queries to go parallel. Setting to 50 reserves parallelism for expensive queries only."},
                                {"line": "sp_configure 'max server memory (MB)', 28672", "meaning": "Limits SQL Server buffer pool to 28GB, leaving 4GB for the OS and other processes. Without this, SQL Server may consume all RAM and cause OS memory pressure."},
                                {"line": "ALTER DATABASE SCOPED CONFIGURATION SET MAXDOP = 2", "meaning": "Sets MAXDOP for a specific database, overriding the server-wide setting. Useful when different databases have different workload types on the same server."},
                                {"line": "SET READ_COMMITTED_SNAPSHOT ON", "meaning": "Changes how READ COMMITTED isolation works: instead of using shared locks (which cause blocking), readers use row versions stored in tempdb. Readers no longer block writers and vice versa. A major concurrency improvement."}
                            ],
                            "ssms_steps": [
                                "Open SSMS and connect with sysadmin rights",
                                "Run Step 1 to check the current compatibility level",
                                "Run Steps 3-6 to configure server-level settings (run each GO block separately)",
                                "Run Step 7 to set database-scoped MAXDOP",
                                "Run Step 8 to verify the new settings are applied (check value_in_use column)",
                                "For READ_COMMITTED_SNAPSHOT (Step 9): this requires no other connections to the database. Run during a maintenance window.",
                                "To check if RCSI is on: SELECT name, is_read_committed_snapshot_on FROM sys.databases WHERE name = 'SalesDB'"
                            ],
                            "exam_tip": "RECONFIGURE applies the sp_configure change immediately. RECONFIGURE WITH OVERRIDE bypasses validation checks — only use if you know what you are doing. READ_COMMITTED_SNAPSHOT is a database-level option that dramatically reduces blocking for OLTP workloads without any application changes."
                        },
                        {
                            "type": "important",
                            "title": "ALTER DATABASE SCOPED CONFIGURATION",
                            "body": "SQL Server 2016+ and Azure SQL Database support database-level configuration options via ALTER DATABASE SCOPED CONFIGURATION. Key settings:<br><ul><li><code>MAXDOP = N</code> — MAXDOP for this database only</li><li><code>LEGACY_CARDINALITY_ESTIMATION = ON</code> — use old optimizer statistics model (sometimes fixes plan regressions after compatibility level upgrade)</li><li><code>PARAMETER_SNIFFING = ON/OFF</code> — controls if SQL Server adapts plans to first parameter value seen</li><li><code>QUERY_OPTIMIZER_HOTFIXES = ON</code> — enables optimizer fixes in service packs</li></ul>These are per-database and do not affect other databases on the same server."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What does SET READ_COMMITTED_SNAPSHOT ON do for a database?",
                            "opts": ["A. Encrypts all read-committed transactions", "B. Makes readers use row versioning instead of shared locks, reducing blocking", "C. Forces all queries to use READ UNCOMMITTED isolation", "D. Enables snapshot replication for the database"],
                            "correct": "B",
                            "explain": "READ_COMMITTED_SNAPSHOT (RCSI) changes how READ COMMITTED isolation is implemented. Instead of acquiring shared locks (which block writers), readers read from a row-version snapshot stored in tempdb. Readers no longer block writers, significantly reducing contention in OLTP workloads."
                        },
                        {
                            "q": "You have a 16-core SQL Server running OLTP workloads. What is a recommended MAXDOP setting?",
                            "opts": ["A. 0 (unlimited)", "B. 1 (no parallelism)", "C. 8 (half the cores, capped at 8)", "D. 16 (all cores)"],
                            "correct": "C",
                            "explain": "Microsoft's general MAXDOP guidance for OLTP is: half the number of physical cores, with a maximum of 8. For 16 cores, MAXDOP = 8. This allows parallel query execution while ensuring other sessions also get CPU resources."
                        },
                        {
                            "q": "What is the default value of 'cost threshold for parallelism' and why is it often considered too low?",
                            "opts": ["A. 50 — too high for most queries", "B. 5 — causes most queries to use parallel execution unnecessarily", "C. 100 — prevents any parallel queries", "D. 0 — disables parallelism completely"],
                            "correct": "B",
                            "explain": "The default cost threshold is 5, which is so low that almost all queries qualify for parallel execution. This causes overhead (parallel plan setup, thread coordination) for queries too short to benefit. Raising to 50-100 reserves parallelism for genuinely expensive queries."
                        },
                        {
                            "q": "Which T-SQL command applies changes made with sp_configure?",
                            "opts": ["A. COMMIT CONFIGURATION", "B. APPLY SETTINGS", "C. RECONFIGURE", "D. RESTART SERVICE"],
                            "correct": "C",
                            "explain": "After running sp_configure to change a setting, you must run RECONFIGURE to apply the change. Some settings (like max server memory) take effect immediately. Others (like max worker threads) require a SQL Server restart."
                        },
                        {
                            "q": "What is the purpose of the SQL Server compatibility level setting?",
                            "opts": ["A. Controls which users can connect to the database", "B. Determines which SQL Server version created the database", "C. Controls which query optimizer features and behaviors are available for the database", "D. Sets the maximum number of concurrent connections"],
                            "correct": "C",
                            "explain": "Compatibility level controls which optimizer features, cardinality estimator version, and SQL syntax features are available. Upgrading the level gives access to newer, better optimizer features but may change query plans. Test thoroughly before upgrading."
                        }
                    ]
                },

                # ── Unit 3: Transaction isolation levels ────────────────
                {
                    "id": "lp2-m6-u3",
                    "title": "Transaction isolation levels",
                    "description": "Understand and apply SQL Server transaction isolation levels to balance data consistency and concurrency.",
                    "estimated_time": 30,
                    "objectives": [
                        "Explain all five isolation levels and their trade-offs",
                        "Set isolation level with SET TRANSACTION ISOLATION LEVEL",
                        "Choose the right isolation level for OLTP vs reporting workloads"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Transaction Isolation Levels",
                            "body": "When multiple users access the database at the same time, concurrency problems can occur. Isolation levels define how much one transaction is isolated from the effects of other concurrent transactions — balancing <strong>data consistency</strong> vs <strong>concurrency/performance</strong>.<br><br><strong>The five standard isolation levels (from lowest to highest isolation):</strong><ul><li><strong>READ UNCOMMITTED</strong> — reads uncommitted (dirty) data from other transactions. Highest concurrency, lowest safety. Can read data that gets rolled back.</li><li><strong>READ COMMITTED</strong> (SQL Server default) — only reads committed data. Releases shared locks after each row is read. Still allows non-repeatable reads.</li><li><strong>REPEATABLE READ</strong> — holds shared locks for the entire transaction duration. Prevents non-repeatable reads but allows phantom rows (new rows inserted by other transactions).</li><li><strong>SERIALIZABLE</strong> — highest standard isolation. Prevents dirty reads, non-repeatable reads, AND phantoms. Uses range locks. Lowest concurrency.</li><li><strong>SNAPSHOT</strong> — readers see a consistent point-in-time view using row versioning (like RCSI). No blocking between readers and writers. Data may be slightly behind current state.</li></ul><strong>Concurrency problems by isolation level:</strong><table border='1'><tr><th>Level</th><th>Dirty Read</th><th>Non-repeatable</th><th>Phantom</th></tr><tr><td>READ UNCOMMITTED</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>READ COMMITTED</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td>REPEATABLE READ</td><td>No</td><td>No</td><td>Yes</td></tr><tr><td>SERIALIZABLE</td><td>No</td><td>No</td><td>No</td></tr><tr><td>SNAPSHOT</td><td>No</td><td>No</td><td>No</td></tr></table>"
                        },
                        {
                            "type": "sql_block",
                            "title": "Demonstrate Isolation Levels",
                            "scenario": "You are building a financial reporting query and a real-time inventory check. Choose and apply the right isolation level for each.",
                            "code": """-- ============================================================
-- EXAMPLE 1: READ UNCOMMITTED (dirty read - use with caution)
-- Use for non-critical approximate counts where speed matters more than accuracy
-- ============================================================
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
GO

-- This query can read uncommitted data from other transactions
-- May return approximate results, but never blocks
SELECT COUNT(*) AS ApproximateOrderCount
FROM dbo.Orders;
GO

-- Equivalent shorthand using table hint:
SELECT COUNT(*) AS ApproximateOrderCount
FROM dbo.Orders WITH (NOLOCK);  -- NOLOCK = READ UNCOMMITTED hint
GO

-- ============================================================
-- EXAMPLE 2: READ COMMITTED (SQL Server default)
-- Safe for most OLTP operations
-- ============================================================
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;  -- This is the default
GO

SELECT OrderID, CustomerID, TotalAmount
FROM dbo.Orders
WHERE OrderDate >= '2024-01-01';
GO

-- ============================================================
-- EXAMPLE 3: REPEATABLE READ
-- Use when you need to re-read the same rows multiple times
-- and they must not change between reads
-- ============================================================
BEGIN TRANSACTION;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;

-- First read: get customer balance
SELECT Balance FROM dbo.Accounts WHERE AccountID = 1001;
-- ... application logic here ...

-- Second read: same row, guaranteed same value
-- No other transaction can UPDATE this row while our transaction is open
SELECT Balance FROM dbo.Accounts WHERE AccountID = 1001;

COMMIT TRANSACTION;
GO

-- ============================================================
-- EXAMPLE 4: SNAPSHOT isolation
-- Best for reporting queries - reads consistent data, never blocks
-- Requires: ALTER DATABASE ... SET ALLOW_SNAPSHOT_ISOLATION ON
-- ============================================================
ALTER DATABASE SalesDB SET ALLOW_SNAPSHOT_ISOLATION ON;
GO

SET TRANSACTION ISOLATION LEVEL SNAPSHOT;
BEGIN TRANSACTION;

-- Reads a consistent snapshot of data as of transaction start
-- Will NOT block even if writers are modifying these rows
SELECT
    ProductID,
    ProductName,
    StockQuantity
FROM dbo.Products;

COMMIT TRANSACTION;
GO

-- ============================================================
-- EXAMPLE 5: SERIALIZABLE (highest isolation)
-- Use when you need complete isolation - ranges are locked
-- ============================================================
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN TRANSACTION;

-- No other transaction can insert a row matching this range
-- while our transaction is open
SELECT OrderID, Amount
FROM dbo.Orders
WHERE OrderDate BETWEEN '2024-01-01' AND '2024-01-31';

COMMIT TRANSACTION;
GO""",
                            "explanation": "Each isolation level makes a different trade-off between consistency and concurrency. READ UNCOMMITTED never blocks but can read wrong data. SNAPSHOT never blocks and gives consistent data (requires versioning infrastructure). SERIALIZABLE is fully consistent but severely limits concurrency.",
                            "purpose": "Choose the appropriate isolation level to balance data accuracy requirements against the need for concurrent access in multi-user applications.",
                            "breakdown": [
                                {"line": "SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED", "meaning": "Sets the isolation level for the current session. This affects all subsequent queries until you change it again or the session ends."},
                                {"line": "WITH (NOLOCK)", "meaning": "A table hint that applies READ UNCOMMITTED to just that one table in the query. Equivalent to setting READ UNCOMMITTED for the session but scoped to one table."},
                                {"line": "SET ALLOW_SNAPSHOT_ISOLATION ON", "meaning": "Enables SNAPSHOT isolation for the database. Must be enabled at database level before a session can use SET TRANSACTION ISOLATION LEVEL SNAPSHOT."},
                                {"line": "REPEATABLE READ — BEGIN TRANSACTION", "meaning": "The isolation level matters most inside a transaction. With REPEATABLE READ, shared locks on read rows are held until COMMIT or ROLLBACK, preventing updates by other transactions."}
                            ],
                            "ssms_steps": [
                                "Open SSMS with two query windows to simulate concurrent sessions",
                                "In Window 1: BEGIN TRANSACTION; UPDATE dbo.Orders SET TotalAmount = 999 WHERE OrderID = 1; (do NOT commit yet)",
                                "In Window 2: SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED; SELECT TotalAmount FROM dbo.Orders WHERE OrderID = 1;",
                                "Window 2 sees the uncommitted value 999 (dirty read!)",
                                "Switch Window 2 to READ COMMITTED and try again — it will wait (block) until Window 1 commits or rolls back",
                                "In Window 1: ROLLBACK TRANSACTION; — now Window 2 will return the original value"
                            ],
                            "exam_tip": "The exam frequently tests which isolation levels prevent which concurrency problems. Memorize: READ UNCOMMITTED = all problems possible. SERIALIZABLE = no problems. SNAPSHOT = no problems, uses versioning instead of locks. Only SNAPSHOT and SERIALIZABLE prevent phantom reads."
                        },
                        {
                            "type": "tip",
                            "title": "NOLOCK Hint — Use with Caution",
                            "body": "The WITH (NOLOCK) hint is very popular for 'performance improvement' but is dangerous:<ul><li>Can read rows twice or skip rows if pages are split during reading</li><li>Can read data from rolled-back transactions (dirty reads)</li><li>Can read logically inconsistent data from partial updates</li></ul>Use SNAPSHOT isolation instead — it gives consistent reads without blocking and without these risks. Only use NOLOCK when approximate non-critical counts are acceptable."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "Which isolation level reads data that has been modified by another transaction but not yet committed?",
                            "opts": ["A. READ COMMITTED", "B. REPEATABLE READ", "C. READ UNCOMMITTED", "D. SNAPSHOT"],
                            "correct": "C",
                            "explain": "READ UNCOMMITTED (and the equivalent NOLOCK hint) can read dirty data — rows modified by an open transaction that hasn't committed. This risks reading data that gets rolled back, but it never blocks on locks."
                        },
                        {
                            "q": "What is a 'phantom read' in database transactions?",
                            "opts": ["A. Reading a row that was deleted by another transaction", "B. Reading an uncommitted row", "C. A transaction re-executes a range query and finds new rows inserted by another committed transaction", "D. A transaction reads the same row and gets different values"],
                            "correct": "C",
                            "explain": "A phantom read occurs when a transaction executes the same range query twice and gets different result sets because another transaction committed new rows that match the range. Only SERIALIZABLE and SNAPSHOT isolation levels prevent phantoms."
                        },
                        {
                            "q": "Which isolation level uses row versioning stored in tempdb to provide consistent reads without blocking?",
                            "opts": ["A. SERIALIZABLE", "B. READ COMMITTED with locks", "C. READ UNCOMMITTED", "D. SNAPSHOT"],
                            "correct": "D",
                            "explain": "SNAPSHOT isolation uses row versions stored in tempdb. When a transaction starts, it gets a consistent snapshot of committed data as it existed at that point in time. Readers never block writers and writers never block readers."
                        },
                        {
                            "q": "You have a reporting query that should not block OLTP writes and must see a consistent view of data. Which isolation level is most appropriate?",
                            "opts": ["A. READ UNCOMMITTED", "B. SERIALIZABLE", "C. SNAPSHOT", "D. REPEATABLE READ"],
                            "correct": "C",
                            "explain": "SNAPSHOT isolation is ideal for reporting: it provides a consistent, point-in-time view without acquiring shared locks that block writers. READ UNCOMMITTED gives no consistency guarantees. SERIALIZABLE provides consistency but severely blocks other transactions."
                        },
                        {
                            "q": "Which database-level option must you enable before sessions can use SET TRANSACTION ISOLATION LEVEL SNAPSHOT?",
                            "opts": ["A. SET SNAPSHOT_ENABLED ON", "B. ALTER DATABASE ... SET ALLOW_SNAPSHOT_ISOLATION ON", "C. SET READ_COMMITTED_SNAPSHOT ON", "D. EXEC sp_configure 'snapshot isolation', 1"],
                            "correct": "B",
                            "explain": "SNAPSHOT isolation requires ALTER DATABASE <db> SET ALLOW_SNAPSHOT_ISOLATION ON. This is a separate setting from READ_COMMITTED_SNAPSHOT (which changes the behavior of READ COMMITTED, not SNAPSHOT). Both use row versioning but are configured separately."
                        }
                    ]
                },

                # ── Unit 4: Execution plans and DMVs ───────────────────
                {
                    "id": "lp2-m6-u4",
                    "title": "Execution plans and DMVs",
                    "description": "Read and interpret SQL Server execution plans and use Dynamic Management Views to diagnose performance.",
                    "estimated_time": 35,
                    "objectives": [
                        "Display and read estimated and actual execution plans",
                        "Identify costly operators: table scans, key lookups, sort operations",
                        "Use DMVs to find top resource-consuming queries"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Understanding Execution Plans",
                            "body": "When you run a SQL query, SQL Server's <strong>Query Optimizer</strong> creates an execution plan — a step-by-step blueprint for how to retrieve the data. Understanding execution plans is the most direct way to diagnose why a query is slow.<br><br><strong>Two types of execution plans:</strong><ul><li><strong>Estimated Plan</strong> (Ctrl+L in SSMS) — produced without running the query. Uses statistics to estimate row counts and costs. Fast to get but may differ from actual.</li><li><strong>Actual Plan</strong> (Ctrl+M in SSMS, then run query) — produced after running the query. Shows real row counts, loop iterations, and wait times.</li></ul><strong>Key operators to recognize:</strong><ul><li><strong>Index Seek</strong> — fast, directly jumps to relevant rows using a B-tree index. Look for this in WHERE clauses on indexed columns.</li><li><strong>Index Scan</strong> — slower, reads all rows in the index. Often indicates a non-selective query or missing covering index.</li><li><strong>Table Scan / Clustered Index Scan</strong> — reads every row in the table. Usually bad for large tables. Means no suitable index exists.</li><li><strong>Key Lookup</strong> — after an index seek on a non-clustered index, SQL Server goes back to the clustered index to get other columns. Expensive if done for many rows. Fix: add a covering index with INCLUDE columns.</li><li><strong>Hash Match</strong> — join algorithm used when tables are large and unsorted. Can spill to disk if memory is insufficient.</li></ul><strong>Missing Index Hints:</strong> SQL Server may display a green 'Missing Index' hint in the execution plan. These are suggestions, not commands — evaluate carefully before creating."
                        },
                        {
                            "type": "sql_block",
                            "title": "Enable Statistics and Read Execution Plan Information",
                            "scenario": "A customer search query is running slowly. Use SQL Server diagnostic tools to understand why.",
                            "code": """-- Step 1: Enable I/O and time statistics to see actual resource usage
SET STATISTICS IO ON;
SET STATISTICS TIME ON;
GO

-- Step 2: Run the slow query
SELECT
    c.CustomerID,
    c.LastName,
    c.Email,
    o.OrderID,
    o.TotalAmount
FROM dbo.Customers c
INNER JOIN dbo.Orders o ON c.CustomerID = o.CustomerID
WHERE c.LastName = 'Smith'
  AND o.TotalAmount > 100.00;
GO

-- Statistics IO Output Example:
-- Table 'Customers': Scan count 1, logical reads 1500, physical reads 0
-- Table 'Orders': Scan count 1, logical reads 45000, physical reads 12
-- High logical reads = many data pages read = slow = needs index

-- Step 3: Get estimated plan as XML (for analysis)
SET SHOWPLAN_XML ON;
GO
SELECT CustomerID, LastName FROM dbo.Customers WHERE LastName = 'Smith';
SET SHOWPLAN_XML OFF;
GO

-- Step 4: Find top 10 most expensive queries using DMVs
-- sys.dm_exec_query_stats captures cumulative statistics since last compile
SELECT TOP 10
    qs.total_logical_reads / qs.execution_count AS avg_logical_reads,
    qs.total_worker_time / qs.execution_count AS avg_cpu_microsec,
    qs.total_elapsed_time / qs.execution_count AS avg_duration_microsec,
    qs.execution_count,
    SUBSTRING(qt.text, 1, 500) AS query_text,
    qp.query_plan
FROM sys.dm_exec_query_stats qs
CROSS APPLY sys.dm_exec_sql_text(qs.sql_handle) qt
CROSS APPLY sys.dm_exec_query_plan(qs.plan_handle) qp
ORDER BY qs.total_logical_reads DESC;
GO

-- Step 5: Find currently running queries and their resource usage
SELECT
    r.session_id,
    r.status,
    r.blocking_session_id,
    r.wait_type,
    r.wait_time,
    r.cpu_time,
    r.logical_reads,
    SUBSTRING(st.text, 1, 300) AS current_sql
FROM sys.dm_exec_requests r
CROSS APPLY sys.dm_exec_sql_text(r.sql_handle) st
WHERE r.session_id > 50;    -- skip system sessions
GO

-- Step 6: Check index usage statistics
SELECT
    OBJECT_NAME(i.object_id) AS TableName,
    i.name AS IndexName,
    u.user_seeks,
    u.user_scans,
    u.user_lookups,
    u.user_updates
FROM sys.indexes i
LEFT JOIN sys.dm_db_index_usage_stats u
    ON i.object_id = u.object_id
    AND i.index_id = u.index_id
    AND u.database_id = DB_ID()
WHERE OBJECT_NAME(i.object_id) = 'Customers'
ORDER BY u.user_seeks DESC;
GO""",
                            "explanation": "STATISTICS IO shows how many data pages SQL Server read for each table (logical reads = from cache, physical reads = from disk). More reads = slower query. DMVs give you query statistics across all sessions without running each query manually.",
                            "purpose": "Diagnose slow queries by measuring I/O, viewing execution plans, and using DMVs to identify the top resource-consuming operations in the database.",
                            "breakdown": [
                                {"line": "SET STATISTICS IO ON", "meaning": "After this, every query shows a message like 'Table X: Scan count 1, logical reads 500'. Logical reads count data pages read from buffer cache. Lower is better."},
                                {"line": "SET STATISTICS TIME ON", "meaning": "Shows CPU time and elapsed time for each query execution. Helps identify whether a query is CPU-bound or waiting."},
                                {"line": "sys.dm_exec_query_stats", "meaning": "DMV that aggregates execution statistics for all cached query plans. Shows total and per-execution averages for CPU, reads, writes, duration. Reset when plan is evicted from cache."},
                                {"line": "CROSS APPLY sys.dm_exec_sql_text(qs.sql_handle)", "meaning": "Table function that takes a sql_handle and returns the full query text. Use CROSS APPLY to run it for each row in the outer query."},
                                {"line": "CROSS APPLY sys.dm_exec_query_plan(qs.plan_handle)", "meaning": "Returns the XML execution plan for the query. The query_plan column can be clicked in SSMS Results to open a graphical plan viewer."},
                                {"line": "sys.dm_exec_requests", "meaning": "DMV showing currently executing requests. blocking_session_id shows if a query is waiting for another session to release locks. wait_type shows what the query is waiting for."},
                                {"line": "sys.dm_db_index_usage_stats", "meaning": "Shows how many times each index has been used (seeks, scans, lookups) since the last SQL Server restart. user_seeks = index used efficiently. user_scans = full index scan. High lookups = consider adding INCLUDE columns."}
                            ],
                            "ssms_steps": [
                                "Open SSMS and connect to your database",
                                "Click New Query and type SET STATISTICS IO ON; SET STATISTICS TIME ON; GO",
                                "Then type your slow query and run it (F5)",
                                "Look at the Messages tab (next to Results) — you will see 'Table X: Scan count Y, logical reads Z'",
                                "High logical reads (thousands+) on a small table = missing index",
                                "To view the graphical execution plan: press Ctrl+M to enable actual plan, then press F5",
                                "The plan appears in a new 'Execution plan' tab",
                                "Hover over any operator node to see the tooltip with estimated vs actual row counts",
                                "Look for thick arrows (many rows flowing) and operators with high % cost"
                            ],
                            "exam_tip": "The exam may show an execution plan and ask what is wrong. Key indicators of problems: Table Scan on a large table (missing index), Key Lookup with many rows (add INCLUDE columns to non-clustered index), estimated rows wildly different from actual rows (stale statistics — run UPDATE STATISTICS)."
                        },
                        {
                            "type": "tip",
                            "title": "Update Statistics to Fix Bad Estimates",
                            "body": "If SQL Server's estimated row counts are far from actual row counts, the statistics may be stale. Fix with:<br><code>UPDATE STATISTICS dbo.Customers;</code><br>Or update all statistics in the database:<br><code>EXEC sp_updatestats;</code><br>Stale statistics cause the query optimizer to make bad decisions, like choosing a table scan when a seek would be faster."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "In an execution plan, what does a 'Key Lookup' operator indicate?",
                            "opts": ["A. A foreign key constraint is being verified", "B. SQL Server is returning to the clustered index to fetch columns not in the non-clustered index", "C. An index is being rebuilt", "D. SQL Server found no matching rows"],
                            "correct": "B",
                            "explain": "A Key Lookup occurs when a non-clustered index seek finds matching rows, but the SELECT includes columns not in that index. SQL Server must go back to the clustered index (bookmark lookup) to retrieve the missing columns. Fix: add the needed columns to the index with INCLUDE."
                        },
                        {
                            "q": "What does 'logical reads' in SET STATISTICS IO ON output measure?",
                            "opts": ["A. Number of rows returned by the query", "B. Number of 8KB data pages read from the buffer cache", "C. Number of disk seeks performed", "D. Number of index pages created during query execution"],
                            "correct": "B",
                            "explain": "Logical reads count the number of 8KB data pages SQL Server read from the buffer pool (memory cache). Physical reads count pages that had to be read from disk (cache miss). Fewer logical reads = better query performance."
                        },
                        {
                            "q": "Which DMV shows statistics for queries that are currently executing?",
                            "opts": ["A. sys.dm_exec_query_stats", "B. sys.dm_exec_requests", "C. sys.dm_db_index_usage_stats", "D. sys.dm_exec_sessions"],
                            "correct": "B",
                            "explain": "sys.dm_exec_requests shows currently executing requests (one row per active query). It includes blocking_session_id, wait_type, cpu_time, logical_reads, and the sql_handle you can use with CROSS APPLY to get the query text."
                        },
                        {
                            "q": "Which execution plan operator indicates that SQL Server is reading every row in a table?",
                            "opts": ["A. Index Seek", "B. Nested Loop Join", "C. Table Scan or Clustered Index Scan", "D. Hash Match Aggregate"],
                            "correct": "C",
                            "explain": "A Table Scan (on a heap) or Clustered Index Scan reads every row in the table. This is inefficient for large tables with selective WHERE clauses. It usually means no suitable index exists for the filter columns."
                        },
                        {
                            "q": "How do you view the actual execution plan for a query in SSMS?",
                            "opts": ["A. Press Ctrl+L before running the query", "B. Press Ctrl+M to enable Include Actual Execution Plan, then run the query", "C. Right-click the query and select 'Show Plan'", "D. Run SET SHOWPLAN_TEXT ON before the query"],
                            "correct": "B",
                            "explain": "In SSMS, press Ctrl+M (or click the 'Include Actual Execution Plan' toolbar button) to enable actual plan capture. Then run your query normally (F5). The execution plan appears in a new 'Execution plan' tab showing real row counts and timing data."
                        }
                    ]
                },

                # ── Unit 5: Query Store ─────────────────────────────────
                {
                    "id": "lp2-m6-u5",
                    "title": "Query Store",
                    "description": "Enable and use Query Store to capture query performance history and fix plan regressions.",
                    "estimated_time": 25,
                    "objectives": [
                        "Enable and configure Query Store",
                        "Use Query Store views in SSMS to identify regressed queries",
                        "Force a query execution plan using Query Store"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "What is Query Store?",
                            "body": "Query Store is like a <strong>flight data recorder for your SQL queries</strong>. It automatically captures every query's text, every execution plan variant, and runtime statistics (CPU, duration, reads) over time — stored persistently in the database itself.<br><br><strong>Why Query Store matters:</strong><ul><li><strong>Plan regression detection</strong> — if an upgrade or statistics change causes a query to suddenly use a worse plan, Query Store shows you the before/after plans and lets you force the old one back</li><li><strong>Persistent history</strong> — unlike DMVs which reset on SQL Server restart, Query Store keeps history until you clear it</li><li><strong>Plan forcing</strong> — pin a specific execution plan to a query, so SQL Server always uses it regardless of statistics or parameter changes</li></ul><strong>Query Store is ON by default in Azure SQL Database and SQL Server 2022.</strong><br><br><strong>Key Query Store catalog views:</strong><ul><li><code>sys.query_store_query</code> — every distinct query</li><li><code>sys.query_store_query_text</code> — the SQL text of each query</li><li><code>sys.query_store_plan</code> — every distinct execution plan per query</li><li><code>sys.query_store_runtime_stats</code> — aggregated runtime metrics per plan</li></ul>"
                        },
                        {
                            "type": "sql_block",
                            "title": "Enable and Use Query Store",
                            "scenario": "A critical stored procedure that was running in 50ms is now taking 5 seconds after a SQL Server upgrade. Use Query Store to diagnose and fix the plan regression.",
                            "code": """-- Step 1: Enable Query Store on the database
ALTER DATABASE SalesDB
SET QUERY_STORE = ON (
    OPERATION_MODE = READ_WRITE,       -- captures query data
    CLEANUP_POLICY = (STALE_QUERY_THRESHOLD_DAYS = 30),  -- keep 30 days
    DATA_FLUSH_INTERVAL_SECONDS = 900, -- flush to disk every 15 minutes
    INTERVAL_LENGTH_MINUTES = 60,      -- aggregate stats per hour
    MAX_STORAGE_SIZE_MB = 1000,        -- 1GB max storage
    QUERY_CAPTURE_MODE = AUTO,         -- capture queries above a threshold
    SIZE_BASED_CLEANUP_MODE = AUTO     -- auto-purge oldest data when full
);
GO

-- Step 2: Verify Query Store is enabled
SELECT
    name,
    is_query_store_on,
    query_store_size_mb,
    actual_state_desc
FROM sys.databases
WHERE name = 'SalesDB';
GO

-- Step 3: Find the regressed query (suddenly slower after upgrade)
-- Look for queries where avg_duration increased significantly
SELECT
    qt.query_sql_text,
    q.query_id,
    p.plan_id,
    rs.avg_duration / 1000.0 AS avg_duration_ms,
    rs.avg_logical_io_reads,
    rs.count_executions,
    p.last_compile_start_time
FROM sys.query_store_query q
JOIN sys.query_store_query_text qt ON q.query_text_id = qt.query_text_id
JOIN sys.query_store_plan p ON q.query_id = p.query_id
JOIN sys.query_store_runtime_stats rs ON p.plan_id = rs.plan_id
ORDER BY rs.avg_duration DESC;
GO

-- Step 4: Compare old plan vs new plan for a specific query
-- Suppose query_id = 42 has two plans: plan_id 10 (old, fast) and plan_id 20 (new, slow)
SELECT
    plan_id,
    last_compile_start_time,
    query_plan                -- click this in SSMS to see graphical plan
FROM sys.query_store_plan
WHERE query_id = 42
ORDER BY last_compile_start_time;
GO

-- Step 5: Force the old fast plan (plan_id = 10) to fix the regression
-- SQL Server will always use plan 10 for query 42, ignoring new statistics
EXEC sys.sp_query_store_force_plan
    @query_id = 42,
    @plan_id = 10;
GO

-- Step 6: Verify the plan is forced
SELECT
    q.query_id,
    p.plan_id,
    p.is_forced_plan,
    p.last_compile_start_time
FROM sys.query_store_plan p
JOIN sys.query_store_query q ON p.query_id = q.query_id
WHERE q.query_id = 42;
GO

-- Step 7: To unforce a plan (let SQL Server choose again)
EXEC sys.sp_query_store_unforce_plan
    @query_id = 42,
    @plan_id = 10;
GO

-- Step 8: Flush Query Store data to disk immediately
EXEC sys.sp_query_store_flush_db;
GO""",
                            "explanation": "Query Store persists multiple execution plans per query. When a plan regression occurs (old plan was faster), you can identify the plan IDs from history and force the better plan. SQL Server then always uses the forced plan for that query.",
                            "purpose": "Capture query performance history to detect regressions and stabilize performance by forcing known-good execution plans.",
                            "breakdown": [
                                {"line": "SET QUERY_STORE = ON (OPERATION_MODE = READ_WRITE)", "meaning": "Enables Query Store in read-write mode so it captures both incoming query data and can be queried. READ_ONLY mode lets you query existing data but capture no new data."},
                                {"line": "QUERY_CAPTURE_MODE = AUTO", "meaning": "Automatically decides which queries to capture based on execution count and resource consumption. Avoids capturing every single ad-hoc query. ALL captures everything; NONE captures nothing."},
                                {"line": "sys.query_store_runtime_stats", "meaning": "Contains per-plan execution statistics: avg_duration (microseconds), avg_logical_io_reads, count_executions, etc. Join to query_store_plan via plan_id."},
                                {"line": "sys.sp_query_store_force_plan @query_id, @plan_id", "meaning": "Forces SQL Server to always use the specified plan for the specified query. The plan is pinned regardless of statistics changes, parameter values, or optimizer updates."},
                                {"line": "is_forced_plan", "meaning": "Column in sys.query_store_plan that shows 1 if this plan is currently forced. Helps you audit which plans are pinned."}
                            ],
                            "ssms_steps": [
                                "In SSMS Object Explorer, right-click your database → Properties → Query Store",
                                "Set Operation Mode to Read Write and configure settings, then click OK",
                                "Or run the ALTER DATABASE SET QUERY_STORE = ON T-SQL script",
                                "After running some queries, expand the database in Object Explorer → Query Store folder",
                                "Double-click 'Regressed Queries' to see a graphical view of queries with plan changes",
                                "Click a query to see plan comparison side by side",
                                "Right-click the better (older) plan → Force Plan",
                                "SSMS runs sp_query_store_force_plan for you automatically"
                            ],
                            "exam_tip": "Query Store is the answer to 'how do you fix a plan regression after a SQL Server upgrade?' The steps are: enable Query Store BEFORE upgrade, identify the regressed query by comparing avg_duration before/after, find the old plan_id, call sp_query_store_force_plan."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What is a 'plan regression' in SQL Server context?",
                            "opts": ["A. A query plan that uses deprecated T-SQL syntax", "B. When SQL Server chooses a worse execution plan than before, causing a query to run slower", "C. An execution plan that was created before the current compatibility level", "D. A query that has been forced to use a specific plan"],
                            "correct": "B",
                            "explain": "A plan regression occurs when SQL Server changes an execution plan (due to statistics update, parameter change, upgrade, etc.) and the new plan is significantly worse than the old one. Query Store helps identify and fix regressions by showing plan history."
                        },
                        {
                            "q": "What does EXEC sys.sp_query_store_force_plan @query_id = 5, @plan_id = 12 do?",
                            "opts": ["A. Deletes plan 12 from Query Store", "B. Forces SQL Server to always use plan 12 when executing query 5", "C. Copies plan 12 from another database", "D. Runs query 5 using plan 12 once and then reverts"],
                            "correct": "B",
                            "explain": "sp_query_store_force_plan pins a specific execution plan to a query. SQL Server will always use plan 12 for query 5, ignoring any statistics changes or recompilation triggers. This is how you fix a plan regression with Query Store."
                        },
                        {
                            "q": "Which Query Store catalog view contains the actual runtime statistics like average duration and CPU time?",
                            "opts": ["A. sys.query_store_query", "B. sys.query_store_plan", "C. sys.query_store_runtime_stats", "D. sys.query_store_query_text"],
                            "correct": "C",
                            "explain": "sys.query_store_runtime_stats stores aggregated execution metrics: avg_duration, avg_cpu_time, avg_logical_io_reads, count_executions, etc. It is joined to sys.query_store_plan via plan_id to see which plan produced those metrics."
                        },
                        {
                            "q": "In Query Store, what does QUERY_CAPTURE_MODE = AUTO mean?",
                            "opts": ["A. Query Store automatically enables itself after an upgrade", "B. Only queries exceeding a resource threshold are captured, filtering out trivial queries", "C. All queries are captured regardless of resource usage", "D. Query Store captures queries only when CPU exceeds 80%"],
                            "correct": "B",
                            "explain": "AUTO mode uses an internal threshold to decide which queries are worth capturing. Very cheap, rarely-run queries are filtered out. This prevents Query Store from filling up with millions of trivial ad-hoc queries. ALL captures every query."
                        },
                        {
                            "q": "How is Query Store different from sys.dm_exec_query_stats DMV?",
                            "opts": ["A. Query Store captures estimated plans; DMV captures actual plans", "B. Query Store persists data to disk across SQL Server restarts; DMV data is lost on restart", "C. DMV requires Enterprise Edition; Query Store is available in all editions", "D. They are identical — Query Store is just a GUI over the DMV"],
                            "correct": "B",
                            "explain": "sys.dm_exec_query_stats is an in-memory structure that is cleared when SQL Server restarts or when plans are evicted from cache. Query Store persists data to the database itself, maintaining history across restarts and for the configured retention period."
                        }
                    ]
                },

                # ── Unit 6: Blocking and deadlocks ─────────────────────
                {
                    "id": "lp2-m6-u6",
                    "title": "Blocking and deadlocks",
                    "description": "Detect and resolve blocking chains and deadlocks in SQL Server.",
                    "estimated_time": 30,
                    "objectives": [
                        "Identify blocking using sys.dm_exec_requests",
                        "Explain what causes deadlocks and how SQL Server resolves them",
                        "Use deadlock trace flags and system health session to capture deadlock information"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Blocking vs Deadlocks",
                            "body": "<strong>Blocking</strong> is normal in SQL Server. Session B waits for Session A to release a lock before proceeding. Blocking is temporary — once Session A commits or rolls back, Session B continues. The problem is when blocking lasts too long (minutes).<br><br><strong>Deadlock</strong> is a special case where two sessions block each other in a cycle:<ul><li>Session A holds Lock 1, wants Lock 2</li><li>Session B holds Lock 2, wants Lock 1</li><li>Neither can proceed — SQL Server detects this and kills one session (the 'deadlock victim') with error 1205</li></ul><strong>Common causes of blocking:</strong><ul><li>Long-running transactions holding locks</li><li>Missing indexes causing table scans that hold more locks</li><li>Implicit transactions (JDBC/ODBC drivers sometimes start transactions automatically)</li></ul><strong>Common causes of deadlocks:</strong><ul><li>Transactions accessing tables in different order</li><li>Hot tables with many concurrent writes</li><li>Long-running transactions</li></ul>"
                        },
                        {
                            "type": "sql_block",
                            "title": "Detect and Resolve Blocking",
                            "scenario": "Users are complaining that the application is hanging. Diagnose and resolve active blocking.",
                            "code": """-- Step 1: Find active blocking chains
-- blocking_session_id > 0 means the session is being blocked
SELECT
    r.session_id,
    r.blocking_session_id,
    r.wait_type,
    r.wait_time / 1000.0 AS wait_seconds,
    r.status,
    r.command,
    r.cpu_time,
    r.logical_reads,
    SUBSTRING(st.text, 1, 400) AS current_query,
    s.login_name,
    s.host_name,
    s.program_name
FROM sys.dm_exec_requests r
JOIN sys.dm_exec_sessions s ON r.session_id = s.session_id
CROSS APPLY sys.dm_exec_sql_text(r.sql_handle) st
WHERE r.session_id > 50   -- exclude system sessions
ORDER BY r.blocking_session_id, r.wait_time DESC;
GO

-- Step 2: Find the HEAD BLOCKER (the root cause)
-- The head blocker is the session with blocking_session_id = 0
-- but other sessions have blocking_session_id = that session's ID
SELECT
    s.session_id,
    s.login_name,
    s.host_name,
    s.program_name,
    s.last_request_start_time,
    t.text AS last_query_run
FROM sys.dm_exec_sessions s
LEFT JOIN sys.dm_exec_requests r ON s.session_id = r.session_id
OUTER APPLY sys.dm_exec_sql_text(
    COALESCE(r.sql_handle, s.prev_error)
) t
WHERE s.session_id IN (
    SELECT blocking_session_id
    FROM sys.dm_exec_requests
    WHERE blocking_session_id > 0
);
GO

-- Step 3: Kill the head blocker (as a last resort — will roll back their transaction!)
-- KILL 55;  -- Replace 55 with the actual session_id

-- Step 4: See all open locks on an object
SELECT
    resource_type,
    resource_associated_entity_id,
    request_mode,
    request_status,
    request_session_id
FROM sys.dm_tran_locks
WHERE resource_database_id = DB_ID()
  AND resource_type = 'OBJECT';
GO

-- Step 5: Enable deadlock trace flags for debugging
DBCC TRACEON(1222, -1);   -- detailed deadlock information in error log
DBCC TRACEON(1204, -1);   -- basic deadlock information (older format)
GO
-- After reproducing the deadlock, check SQL Server Error Log in SSMS:
-- Management → SQL Server Logs → Current

-- Step 6: Query the system_health Extended Events session for deadlock XML
-- (Available automatically since SQL Server 2008)
SELECT
    CAST(xdr.value('@timestamp', 'datetime') AT TIME ZONE 'UTC' AS DATETIME) AS deadlock_time,
    xdr.query('.') AS deadlock_graph
FROM (
    SELECT CAST(target_data AS XML) AS target_data
    FROM sys.dm_xe_session_targets t
    JOIN sys.dm_xe_sessions s ON t.event_session_address = s.address
    WHERE s.name = 'system_health'
      AND t.target_name = 'ring_buffer'
) AS data
CROSS APPLY target_data.nodes('//RingBufferTarget/event[@name="xml_deadlock_report"]') AS xdt(xdr)
ORDER BY deadlock_time DESC;
GO

-- Step 7: Prevent deadlocks with SET DEADLOCK_PRIORITY
-- Lower priority = SQL Server kills this session first if deadlock occurs
-- Use in reporting/background processes that can safely retry
SET DEADLOCK_PRIORITY LOW;
GO

-- Step 8: Prevent blocking with shorter transactions
-- BAD: Long-running transaction
BEGIN TRANSACTION;
UPDATE dbo.Orders SET Status = 'Processing' WHERE CustomerID = 100;
-- ... 30 seconds of application logic here ...
UPDATE dbo.Orders SET Status = 'Complete' WHERE CustomerID = 100;
COMMIT TRANSACTION;

-- BETTER: Minimize lock hold time
UPDATE dbo.Orders SET Status = 'Processing' WHERE CustomerID = 100;
-- ... application logic ...
UPDATE dbo.Orders SET Status = 'Complete' WHERE CustomerID = 100;
-- Two separate quick transactions instead of one long one""",
                            "explanation": "Detecting blocking uses DMVs. The head blocker is the root cause — all others are waiting on it. Deadlocks are captured automatically in the system_health XEvent session. Prevention is better than cure: keep transactions short and access tables in consistent order.",
                            "purpose": "Identify and eliminate blocking and deadlocks that cause application timeouts and poor user experience.",
                            "breakdown": [
                                {"line": "r.blocking_session_id", "meaning": "If this is > 0, this session is blocked, waiting for the specified session to release a lock. 0 means not blocked. The session with the most other sessions waiting on it is the head blocker."},
                                {"line": "sys.dm_tran_locks", "meaning": "Shows all currently held locks in the database. resource_type shows OBJECT, PAGE, KEY, etc. request_mode shows what type of lock (S=shared, X=exclusive, U=update)."},
                                {"line": "DBCC TRACEON(1222, -1)", "meaning": "Enables trace flag 1222 globally (-1). This causes SQL Server to write detailed deadlock information to the error log whenever a deadlock is detected. Useful for diagnosing recurring deadlocks."},
                                {"line": "system_health Extended Events", "meaning": "A built-in XEvent session that automatically captures deadlock graphs (xml_deadlock_report). Always running since SQL Server 2008 — you never need to set it up."},
                                {"line": "SET DEADLOCK_PRIORITY LOW", "meaning": "When SQL Server detects a deadlock, it picks one session as the 'victim' to kill. LOW priority makes this session more likely to be chosen as the victim — useful for background jobs that can safely retry."}
                            ],
                            "ssms_steps": [
                                "Open SSMS → New Query",
                                "Run the Step 1 query — look at the Results for sessions with blocking_session_id > 0",
                                "The head blocker is the session_id that appears in blocking_session_id column of other rows",
                                "To see what the head blocker is doing: find its row and look at current_query",
                                "For deadlocks: go to SSMS → Object Explorer → Management → SQL Server Logs → right-click Current → View SQL Server Log",
                                "Search for 'deadlock' in the filter",
                                "Or expand Management → Extended Events → Sessions → system_health → right-click Package0.ring_buffer → View Target Data",
                                "Look for xml_deadlock_report events"
                            ],
                            "exam_tip": "For the exam: WITH (NOLOCK) reduces blocking but causes dirty reads. SNAPSHOT isolation eliminates most blocking with consistent reads. sys.dm_exec_requests shows blocking_session_id. Deadlock victim selection can be influenced with SET DEADLOCK_PRIORITY. Trace flag 1222 adds deadlock details to the error log."
                        },
                        {
                            "type": "important",
                            "title": "Best Practices to Prevent Blocking and Deadlocks",
                            "body": "<strong>Prevent blocking:</strong><ul><li>Keep transactions as short as possible — commit quickly</li><li>Access tables in the same order in all transactions</li><li>Use appropriate indexes to avoid full table scans (which lock more rows)</li><li>Consider READ_COMMITTED_SNAPSHOT to eliminate shared lock blocking</li></ul><strong>Prevent deadlocks:</strong><ul><li>Always access tables in the same order (Application A: Orders then OrderItems; Application B: same order)</li><li>Avoid user interaction inside transactions</li><li>Add retry logic in application code to handle deadlock error 1205</li><li>Use SNAPSHOT isolation for read-heavy workloads</li></ul>"
                        }
                    ],
                    "quiz": [
                        {
                            "q": "In sys.dm_exec_requests, what does blocking_session_id = 67 mean for session 82?",
                            "opts": ["A. Session 82 is blocking session 67", "B. Session 82 is waiting for session 67 to release a lock", "C. Sessions 82 and 67 are in a deadlock", "D. Session 67 killed session 82"],
                            "correct": "B",
                            "explain": "blocking_session_id shows which session is holding a lock that the current session needs. If session 82 shows blocking_session_id = 67, it means session 82 is blocked and waiting for session 67 to release its lock."
                        },
                        {
                            "q": "SQL Server automatically resolves a deadlock by doing what?",
                            "opts": ["A. Pausing both sessions and waiting for a timeout", "B. Asking the user to choose which transaction to abort", "C. Choosing one session as the deadlock victim and rolling back its transaction", "D. Merging both transactions into one"],
                            "correct": "C",
                            "explain": "SQL Server's deadlock monitor detects cycles and picks one session as the 'deadlock victim' to roll back (sending error 1205). The selection is based on DEADLOCK_PRIORITY setting, transaction cost, and other factors. The other session then proceeds normally."
                        },
                        {
                            "q": "Which trace flag writes detailed deadlock information to the SQL Server error log?",
                            "opts": ["A. 1024", "B. 3604", "C. 1222", "D. 4199"],
                            "correct": "C",
                            "explain": "Trace flag 1222 causes SQL Server to write detailed deadlock information (including the resource-wait graph and involved queries) to the error log. Trace flag 1204 writes a simpler format. Both are useful for diagnosing deadlock patterns."
                        },
                        {
                            "q": "How does SET DEADLOCK_PRIORITY LOW affect a session?",
                            "opts": ["A. The session will never be involved in a deadlock", "B. The session's queries run at lower CPU priority", "C. The session is more likely to be chosen as the deadlock victim", "D. The session avoids acquiring locks"],
                            "correct": "C",
                            "explain": "SET DEADLOCK_PRIORITY LOW makes this session's transaction more likely to be chosen as the deadlock victim when SQL Server detects a deadlock. Useful for background processes or reporting queries that can safely retry after being killed."
                        },
                        {
                            "q": "What is the most effective way to prevent reader-writer blocking in an OLTP database without changing application code?",
                            "opts": ["A. Add WITH (NOLOCK) hints to all SELECT queries", "B. Enable READ_COMMITTED_SNAPSHOT database option", "C. Set MAXDOP to 1 for all queries", "D. Use SERIALIZABLE isolation level"],
                            "correct": "B",
                            "explain": "Enabling READ_COMMITTED_SNAPSHOT makes the default READ COMMITTED isolation use row versioning (like SNAPSHOT) instead of shared locks. Readers never block writers and writers never block readers. No application code changes are needed."
                        }
                    ]
                },

                # ── Unit 7: Exercise ────────────────────────────────────
                {
                    "id": "lp2-m6-u7",
                    "title": "Exercise",
                    "description": "Hands-on exercise: diagnose and resolve performance problems in a sample database.",
                    "estimated_time": 40,
                    "objectives": [
                        "Use execution plans and DMVs to find slow queries",
                        "Enable Query Store and identify regressed queries",
                        "Resolve a simulated blocking scenario"
                    ],
                    "content": [
                        {
                            "type": "sql_block",
                            "title": "Exercise: Performance Tuning a Slow Order Query",
                            "scenario": "The Orders report that used to run in 200ms now takes 8 seconds. Users are also reporting hangs when placing orders. Use the techniques from this module to diagnose and fix both issues.",
                            "code": """-- ============================================================
-- EXERCISE PART 1: Diagnose the slow report query
-- ============================================================

-- Setup: Ensure Query Store is enabled
ALTER DATABASE SalesDB SET QUERY_STORE = ON
    (OPERATION_MODE = READ_WRITE, QUERY_CAPTURE_MODE = AUTO);
GO

-- Enable statistics
SET STATISTICS IO ON;
SET STATISTICS TIME ON;
GO

-- Run the slow report query
SELECT
    c.CustomerID,
    c.FirstName + ' ' + c.LastName AS CustomerName,
    COUNT(o.OrderID) AS TotalOrders,
    SUM(o.TotalAmount) AS TotalRevenue
FROM dbo.Customers c
LEFT JOIN dbo.Orders o ON c.CustomerID = o.CustomerID
WHERE o.OrderDate >= '2024-01-01'
  AND o.TotalAmount > 50
GROUP BY c.CustomerID, c.FirstName, c.LastName
ORDER BY TotalRevenue DESC;
GO
-- CHECK: Messages tab shows logical reads for each table
-- PROBLEM: Orders table shows 50,000+ logical reads = table scan

-- ============================================================
-- EXERCISE PART 2: Press Ctrl+M and re-run to see Actual Plan
-- Look for: Table Scan on Orders, Key Lookup, thick arrow
-- ============================================================

-- Suspected missing index: Orders.OrderDate + TotalAmount
-- Create a covering index
CREATE INDEX IX_Orders_Date_Amount
    ON dbo.Orders (OrderDate, TotalAmount)
    INCLUDE (CustomerID);  -- INCLUDE avoids Key Lookup
GO

-- Re-run query — now should use Index Seek, much fewer reads
-- ============================================================

-- ============================================================
-- EXERCISE PART 3: Simulate and detect blocking
-- Open two SSMS query windows simultaneously
-- ============================================================

-- WINDOW 1: Start a long transaction (do NOT commit)
BEGIN TRANSACTION;
UPDATE dbo.Orders
    SET Status = 'Processing'
    WHERE CustomerID = 1;
-- Do not run COMMIT yet!

-- WINDOW 2: Try to read the same rows (will be blocked)
SELECT OrderID, Status FROM dbo.Orders WHERE CustomerID = 1;

-- WINDOW 3: Run blocking diagnosis
SELECT
    r.session_id,
    r.blocking_session_id,
    r.wait_type,
    r.wait_time / 1000.0 AS wait_sec,
    SUBSTRING(st.text, 1, 200) AS sql_text
FROM sys.dm_exec_requests r
CROSS APPLY sys.dm_exec_sql_text(r.sql_handle) st
WHERE r.blocking_session_id > 0;
GO

-- WINDOW 1: Commit to release the lock
COMMIT TRANSACTION;
-- Window 2's query will now complete

-- ============================================================
-- EXERCISE PART 4: Find the regressed plan in Query Store
-- ============================================================

-- Find queries with multiple plans (indicates plan change)
SELECT
    qt.query_sql_text,
    q.query_id,
    COUNT(DISTINCT p.plan_id) AS plan_count,
    MAX(rs.avg_duration) / 1000.0 AS max_avg_ms
FROM sys.query_store_query q
JOIN sys.query_store_query_text qt ON q.query_text_id = qt.query_text_id
JOIN sys.query_store_plan p ON q.query_id = p.query_id
JOIN sys.query_store_runtime_stats rs ON p.plan_id = rs.plan_id
GROUP BY qt.query_sql_text, q.query_id
HAVING COUNT(DISTINCT p.plan_id) > 1      -- multiple plans = possible regression
ORDER BY max_avg_ms DESC;
GO

-- If you find a query with plan_id = 5 (old, fast) and plan_id = 8 (new, slow):
-- EXEC sys.sp_query_store_force_plan @query_id = <id>, @plan_id = 5;""",
                            "explanation": "This exercise combines multiple performance techniques: statistics to find high-read queries, execution plans to identify missing indexes, DMVs to detect blocking, and Query Store to diagnose plan regressions. In real production work these are used together.",
                            "purpose": "Practice the complete performance tuning workflow: measure → diagnose → fix → verify.",
                            "breakdown": [
                                {"line": "CREATE INDEX IX_Orders_Date_Amount ON dbo.Orders (OrderDate, TotalAmount) INCLUDE (CustomerID)", "meaning": "Creates a non-clustered index on the filter columns (OrderDate, TotalAmount). INCLUDE adds CustomerID without it being a key column, allowing the index seek to satisfy the join without a Key Lookup."},
                                {"line": "HAVING COUNT(DISTINCT p.plan_id) > 1", "meaning": "Filters to only queries that have more than one plan in Query Store — these are candidates for plan regression analysis."}
                            ],
                            "ssms_steps": [
                                "Open SSMS with at least two query windows connected to SalesDB",
                                "Run Part 1: enable statistics and run the slow query",
                                "Check the Messages tab for logical reads",
                                "Press Ctrl+M then run the query again to see the Actual Execution Plan",
                                "Look for Table Scan or Index Scan on Orders table",
                                "Run the CREATE INDEX statement",
                                "Re-run the query and compare logical reads and plan — should be much lower",
                                "For Part 3: run the BEGIN TRANSACTION in Window 1 (do NOT commit)",
                                "Switch to Window 2 and run the SELECT — notice it hangs",
                                "Open Window 3 and run the blocking diagnosis query",
                                "Go back to Window 1 and run COMMIT TRANSACTION",
                                "Watch Window 2 complete immediately"
                            ],
                            "exam_tip": "The DP-800 exam may show a scenario where you must choose the right tool: slow query = execution plan + STATISTICS IO. Plan regression = Query Store + sp_query_store_force_plan. Hanging users = blocking diagnosis with sys.dm_exec_requests."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "After adding an index on a filter column, what execution plan change do you expect to see?",
                            "opts": ["A. Table Scan changes to Clustered Index Scan", "B. Table Scan changes to Index Seek", "C. Hash Join changes to Nested Loop", "D. Sort operator is added"],
                            "correct": "B",
                            "explain": "Adding an appropriate non-clustered index on a filter column (used in WHERE or JOIN) allows SQL Server to use an Index Seek instead of a Table Scan. Index Seek directly navigates the B-tree to matching rows, reading far fewer pages."
                        },
                        {
                            "q": "What does the INCLUDE clause in a CREATE INDEX statement do?",
                            "opts": ["A. Includes the index in the query optimizer's consideration", "B. Adds non-key columns to the index leaf level to satisfy SELECT queries without a Key Lookup", "C. Includes statistics for the listed columns", "D. Marks the columns as required (NOT NULL) in the index"],
                            "correct": "B",
                            "explain": "INCLUDE columns are stored at the leaf level of a non-clustered index but are not part of the index key. They allow the index to satisfy SELECT columns without requiring a Key Lookup back to the clustered index. This creates a 'covering index'."
                        },
                        {
                            "q": "In the exercise, what caused Window 2's SELECT query to hang?",
                            "opts": ["A. Window 2 had incorrect SQL syntax", "B. Window 1 held an exclusive lock on the rows from its uncommitted UPDATE", "C. The index was being rebuilt in the background", "D. Query Store was capturing the query plan"],
                            "correct": "B",
                            "explain": "Window 1's BEGIN TRANSACTION + UPDATE acquired an exclusive (X) lock on the CustomerID = 1 rows. Window 2's SELECT needed a shared (S) lock on the same rows but could not get it because X locks are incompatible with S locks — so it waited (blocked)."
                        },
                        {
                            "q": "What does HAVING COUNT(DISTINCT p.plan_id) > 1 find in the Query Store query?",
                            "opts": ["A. Queries that have been executed more than once", "B. Queries where SQL Server has generated multiple different execution plans", "C. Plans that have been forced by sp_query_store_force_plan", "D. Queries with more than one join"],
                            "correct": "B",
                            "explain": "Multiple plan_ids for the same query_id means SQL Server generated different execution plans for the same query at different times. This is a strong indicator of a potential plan regression — comparing the plans can reveal which one caused performance degradation."
                        },
                        {
                            "q": "What is the primary benefit of adding CustomerID to the INCLUDE clause of the Orders index?",
                            "opts": ["A. CustomerID becomes the primary sort key of the index", "B. The index can satisfy the JOIN to Customers table without an additional Key Lookup", "C. CustomerID values are encrypted in the index", "D. The index is automatically updated when CustomerID changes"],
                            "correct": "B",
                            "explain": "Since the query joins on CustomerID, including it in the index means SQL Server can get OrderDate, TotalAmount (key columns for the WHERE), and CustomerID (for the JOIN) all from the same index entry — eliminating the expensive Key Lookup back to the clustered index."
                        }
                    ]
                },

                # ── Unit 8: Knowledge check ─────────────────────────────
                {
                    "id": "lp2-m6-u8",
                    "title": "Knowledge check",
                    "description": "Test your understanding of database performance optimization concepts.",
                    "estimated_time": 15,
                    "objectives": [
                        "Validate understanding of isolation levels, execution plans, Query Store, and blocking"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Module 6 Performance Key Concepts Review",
                            "body": "Quick review before the knowledge check:<br><br><strong>Configuration:</strong> ALTER DATABASE SCOPED CONFIGURATION for per-DB settings. sp_configure for server-level. READ_COMMITTED_SNAPSHOT eliminates most shared-lock blocking. MAXDOP = half CPU count, max 8 for OLTP.<br><br><strong>Isolation Levels:</strong> READ UNCOMMITTED = dirty reads (use NOLOCK hint). SNAPSHOT = consistent reads, no locks, uses tempdb versioning. SERIALIZABLE = no concurrency problems but maximum locking. SET TRANSACTION ISOLATION LEVEL + BEGIN/COMMIT TRANSACTION.<br><br><strong>Execution Plans:</strong> Ctrl+L (estimated) vs Ctrl+M then run (actual). Table Scan = bad. Index Seek = good. Key Lookup = add INCLUDE. SET STATISTICS IO ON to see logical reads. sys.dm_exec_query_stats for top queries by resource usage.<br><br><strong>Query Store:</strong> ALTER DATABASE SET QUERY_STORE = ON. Persists plan history. sp_query_store_force_plan to fix regressions. sys.query_store_runtime_stats for execution metrics.<br><br><strong>Blocking/Deadlocks:</strong> sys.dm_exec_requests with blocking_session_id. Deadlocks detected automatically, victim rolled back (error 1205). Trace flag 1222 for error log details. system_health XEvent session auto-captures deadlock graphs. SET DEADLOCK_PRIORITY LOW."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What is the recommended MAXDOP setting for an OLTP SQL Server with 16 physical cores?",
                            "opts": ["A. 0 (unlimited)", "B. 16 (use all cores)", "C. 8 (half the cores, capped at 8)", "D. 1 (no parallelism for OLTP)"],
                            "correct": "C",
                            "explain": "Microsoft's guidance for OLTP workloads: set MAXDOP to half the number of physical cores, up to a maximum of 8. For 16 cores, MAXDOP = 8. This allows parallel queries while ensuring other connections also get CPU."
                        },
                        {
                            "q": "A query uses SNAPSHOT isolation. If another session is updating the same rows, what happens to the SNAPSHOT query?",
                            "opts": ["A. It waits for the update to complete", "B. It reads the pre-update row version from tempdb and continues without blocking", "C. It raises an error and must retry", "D. It reads the uncommitted updated value"],
                            "correct": "B",
                            "explain": "SNAPSHOT isolation uses row versioning. The SNAPSHOT query sees the committed version of the row that existed when the transaction started. It reads from tempdb's version store and does not wait for (or conflict with) the ongoing UPDATE."
                        },
                        {
                            "q": "Which DMV shows the execution statistics (CPU, reads, duration) for all cached query plans?",
                            "opts": ["A. sys.dm_exec_requests", "B. sys.dm_exec_sessions", "C. sys.dm_exec_query_stats", "D. sys.dm_db_index_usage_stats"],
                            "correct": "C",
                            "explain": "sys.dm_exec_query_stats aggregates execution statistics per plan in the procedure cache. Join it with sys.dm_exec_sql_text to get query text and sys.dm_exec_query_plan to get the XML plan. Reset when plans are evicted from cache."
                        },
                        {
                            "q": "After a SQL Server upgrade, a critical query now runs 10x slower. Which tool can you use to view the old (fast) execution plan and force it back?",
                            "opts": ["A. sys.dm_exec_query_stats", "B. Extended Events", "C. Query Store", "D. SQL Server Profiler"],
                            "correct": "C",
                            "explain": "Query Store retains execution plan history across restarts. After an upgrade, if a plan regressed, you can find the old plan_id in sys.query_store_plan and call sp_query_store_force_plan to make SQL Server always use the old (faster) plan."
                        },
                        {
                            "q": "Which error number does SQL Server send to a deadlock victim's session?",
                            "opts": ["A. 547 (constraint violation)", "B. 1205 (deadlock victim)", "C. 2627 (duplicate key)", "D. 8134 (divide by zero)"],
                            "correct": "B",
                            "explain": "Error 1205 is the SQL Server deadlock victim error: 'Transaction (Process ID X) was deadlocked on lock resources with another process and has been chosen as the deadlock victim. Rerun the transaction.' Application code should catch this error and retry."
                        }
                    ]
                },

                # ── Unit 9: Summary ─────────────────────────────────────
                {
                    "id": "lp2-m6-u9",
                    "title": "Summary",
                    "description": "Review the key performance optimization techniques covered in this module.",
                    "estimated_time": 5,
                    "objectives": [
                        "Recall performance optimization techniques and when to apply them"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Module 6 Summary — Database Performance Optimization",
                            "body": "In this module you learned SQL Server performance optimization:<br><br><ul><li><strong>Database Configuration</strong> — <code>ALTER DATABASE SCOPED CONFIGURATION SET MAXDOP = N</code>. Server-level via <code>sp_configure</code> + RECONFIGURE. Enable <code>READ_COMMITTED_SNAPSHOT ON</code> to eliminate reader-writer blocking. Raise cost threshold for parallelism to 50+.</li><li><strong>Isolation Levels</strong> — <code>SET TRANSACTION ISOLATION LEVEL</code>. READ UNCOMMITTED = dirty reads (NOLOCK hint). READ COMMITTED = default, locks released per row. REPEATABLE READ = locks held for transaction. SERIALIZABLE = no phantom reads, range locks. SNAPSHOT = consistent reads via tempdb versioning, no blocking.</li><li><strong>Execution Plans</strong> — Ctrl+M for actual plan in SSMS. SET STATISTICS IO ON for logical reads. Index Seek = good. Table Scan = bad (missing index). Key Lookup = fix with INCLUDE columns. DMVs: sys.dm_exec_query_stats (cached stats), sys.dm_exec_requests (current).</li><li><strong>Query Store</strong> — <code>ALTER DATABASE SET QUERY_STORE = ON</code>. Captures plan history persistently. Use SSMS built-in reports or T-SQL views. <code>sp_query_store_force_plan</code> to fix regressions. <code>sp_query_store_unforce_plan</code> to release.</li><li><strong>Blocking and Deadlocks</strong> — sys.dm_exec_requests.blocking_session_id to find blocked sessions. KILL <session_id> as last resort. Deadlocks auto-resolved — victim gets error 1205. Trace flag 1222 for error log details. SET DEADLOCK_PRIORITY LOW for non-critical sessions. Prevention: short transactions, consistent table access order, proper indexes.</li></ul>"
                        }
                    ],
                    "quiz": [
                        {
                            "q": "Which command enables Query Store on a database?",
                            "opts": ["A. EXEC sp_configure 'query store', 1", "B. ALTER DATABASE db SET QUERY_STORE = ON", "C. CREATE QUERY STORE FOR DATABASE db", "D. ENABLE QUERY_STORE ON db"],
                            "correct": "B",
                            "explain": "ALTER DATABASE <db_name> SET QUERY_STORE = ON enables Query Store. You can include additional options like OPERATION_MODE, CLEANUP_POLICY, and MAX_STORAGE_SIZE_MB in the same statement."
                        },
                        {
                            "q": "SET STATISTICS IO ON shows 'Table Orders: logical reads 45000'. What does this suggest?",
                            "opts": ["A. 45,000 rows were returned", "B. 45,000 data pages (8KB each) were read — likely a missing index causing a table scan", "C. The query ran for 45,000 milliseconds", "D. 45,000 CPU cycles were used"],
                            "correct": "B",
                            "explain": "Logical reads count 8KB data pages read from the buffer pool. 45,000 logical reads on the Orders table means SQL Server read 45,000 x 8KB = ~360MB of data pages — almost certainly a table scan on a large table, indicating a missing index."
                        },
                        {
                            "q": "What is the key difference between REPEATABLE READ and SNAPSHOT isolation?",
                            "opts": ["A. REPEATABLE READ is only for reads; SNAPSHOT supports writes too", "B. REPEATABLE READ uses shared locks held for the transaction; SNAPSHOT uses row versioning with no locking", "C. SNAPSHOT allows dirty reads; REPEATABLE READ does not", "D. REPEATABLE READ is available only in Azure SQL; SNAPSHOT is on-premises only"],
                            "correct": "B",
                            "explain": "Both prevent non-repeatable reads (re-reading the same row gives the same value). But REPEATABLE READ achieves this by holding shared locks (which block writers), while SNAPSHOT uses row versioning in tempdb (no locks needed — writers are not blocked)."
                        },
                        {
                            "q": "What triggers SQL Server's deadlock monitor to act?",
                            "opts": ["A. A query running longer than 30 seconds", "B. SQL Server detects a circular wait where sessions are each waiting for the other's lock", "C. A session's transaction log fills up", "D. A query returns more than 1 million rows"],
                            "correct": "B",
                            "explain": "The deadlock monitor (a background thread) periodically checks for lock wait cycles. When it detects session A waiting for B and B waiting for A (circular dependency), it picks a victim and rolls back that session's transaction, sending error 1205."
                        },
                        {
                            "q": "You need a covering index for a query: SELECT OrderID, CustomerID FROM Orders WHERE OrderDate > '2024-01-01'. Which CREATE INDEX statement is best?",
                            "opts": ["A. CREATE INDEX IX ON Orders (OrderID, CustomerID)", "B. CREATE INDEX IX ON Orders (OrderDate) INCLUDE (OrderID, CustomerID)", "C. CREATE INDEX IX ON Orders (OrderDate, OrderID, CustomerID)", "D. CREATE INDEX IX ON Orders (CustomerID) INCLUDE (OrderDate)"],
                            "correct": "B",
                            "explain": "The WHERE clause filters on OrderDate (put in the key). The SELECT needs OrderID and CustomerID (put in INCLUDE). Key columns control navigation and filtering; INCLUDE columns satisfy SELECT without a Key Lookup. Making OrderDate the key allows the index seek on the range condition."
                        }
                    ]
                }
            ]
        },

        # ══════════════════════════════════════════════════════════════
        # MODULE lp2-m7: Implement CI/CD by using SQL database projects
        # ══════════════════════════════════════════════════════════════
        {
            "id": "lp2-m7",
            "title": "Implement CI/CD by using SQL database projects",
            "description": "Learn to manage SQL database schema in source control, build DACPAC artifacts, and deploy with CI/CD pipelines using GitHub Actions or Azure DevOps.",
            "units": [

                # ── Unit 1: Introduction ────────────────────────────────
                {
                    "id": "lp2-m7-u1",
                    "title": "Introduction",
                    "description": "Overview of SQL database projects and CI/CD for database deployments.",
                    "estimated_time": 5,
                    "objectives": [
                        "Understand what SQL database projects are and why they matter",
                        "Preview the CI/CD pipeline for SQL databases"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "SQL Database Projects and CI/CD",
                            "body": "Traditional database changes are made directly in production — someone runs ALTER TABLE in SSMS and hopes for the best. This approach has no history, no review process, no way to roll back, and no automated testing.<br><br><strong>SQL Database Projects</strong> bring software engineering discipline to database development:<ul><li>Every database object (table, view, procedure) has its own <strong>.sql file</strong> in source control</li><li>A <strong>.sqlproj</strong> file defines the project</li><li>The project builds to a <strong>DACPAC</strong> (Data-tier Application Package) — a deployable artifact</li><li>DACPAC deployment compares source and target schemas and generates the minimum DDL to bring target up to date</li></ul>In this module you will learn:<ul><li>Creating and building SQL database projects in VS Code</li><li>Git source control for SQL schema files</li><li>Branching, pull requests, and conflict resolution for schema changes</li><li>Schema drift detection and remediation</li><li>CI/CD pipelines with GitHub Actions and Azure DevOps</li><li>Testing SQL databases with tSQLt</li></ul>"
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What file extension is used for a SQL Server database project file?",
                            "opts": ["A. .dbproj", "B. .sqlproj", "C. .dacproj", "D. .tsql"],
                            "correct": "B",
                            "explain": "SQL Server database projects use the .sqlproj file extension. This XML file defines the project type, target platform, and references to the .sql files that define database objects."
                        },
                        {
                            "q": "What is a DACPAC file?",
                            "opts": ["A. A compressed backup of a SQL Server database", "B. A deployable artifact containing the schema definition of a SQL database", "C. A PowerShell script for database deployment", "D. An Azure ARM template for SQL Server"],
                            "correct": "B",
                            "explain": "DACPAC (Data-tier Application Package) is a ZIP-formatted file containing the database schema model. When deployed with SqlPackage.exe or SSMS, it compares the DACPAC schema with the target database and generates the SQL needed to synchronize them."
                        },
                        {
                            "q": "What is the main benefit of storing SQL schema in git source control?",
                            "opts": ["A. SQL files are automatically executed against the database on commit", "B. All schema changes have a history, can be reviewed, and can be reverted", "C. Git automatically backs up the database data", "D. SSMS synchronizes automatically with the git repository"],
                            "correct": "B",
                            "explain": "Storing .sql files in git gives you: full change history (who changed what when), code review via pull requests, branch-based development, and the ability to revert changes. This is the foundation of database DevOps."
                        },
                        {
                            "q": "When you publish a DACPAC to a target database, what does SqlPackage.exe do?",
                            "opts": ["A. Drops and recreates the entire database", "B. Compares the DACPAC schema with the target and generates minimum DDL to synchronize them", "C. Copies data from the DACPAC to the database", "D. Runs all .sql files in alphabetical order"],
                            "correct": "B",
                            "explain": "SqlPackage.exe (with the /Action:Publish option) performs a schema comparison between the DACPAC (source) and target database, then generates and runs the minimum DDL needed (CREATE TABLE, ALTER TABLE, etc.) to make the target match the source."
                        },
                        {
                            "q": "Which tool in VS Code allows you to create and build SQL database projects?",
                            "opts": ["A. Azure Data Studio extension", "B. SQL Database Projects extension (part of mssql extension)", "C. Bicep extension", "D. Azure Resource Manager extension"],
                            "correct": "B",
                            "explain": "The SQL Database Projects extension (bundled with or installed alongside the mssql extension) in VS Code provides a graphical interface to create .sqlproj files, add .sql object files, build to DACPAC, and publish to a database."
                        }
                    ]
                },

                # ── Unit 2: Create, build, and validate SQL database projects ──
                {
                    "id": "lp2-m7-u2",
                    "title": "Create, build, and validate SQL database projects",
                    "description": "Create a SQL database project, define objects in .sql files, build to DACPAC, and validate the schema.",
                    "estimated_time": 30,
                    "objectives": [
                        "Create a SQL database project (.sqlproj) in VS Code",
                        "Add table, view, and stored procedure objects as .sql files",
                        "Build the project to produce a DACPAC",
                        "Publish the DACPAC to a target database"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "SQL Database Project Structure",
                            "body": "A SQL database project is a folder structure with SQL files for each database object, organized logically:<br><pre>MyDatabase/\n  MyDatabase.sqlproj       ← project file\n  Tables/\n    dbo.Customers.sql      ← CREATE TABLE statement\n    dbo.Orders.sql\n  Views/\n    dbo.vw_OrderSummary.sql\n  Stored Procedures/\n    dbo.usp_GetOrders.sql\n  Security/\n    dbo.AppUser.sql        ← CREATE USER / GRANT statements</pre><br>Each .sql file contains a single CREATE statement for that object. Do NOT include DROP statements — SqlPackage handles the diff automatically.<br><br><strong>The .sqlproj file</strong> specifies the SQL Server version target:<br><pre>&lt;DSP&gt;Microsoft.Data.Tools.Schema.Sql.Sql160DatabaseSchemaProvider&lt;/DSP&gt;</pre>This tells the build tools which version of T-SQL syntax is valid."
                        },
                        {
                            "type": "sql_block",
                            "title": "SQL Database Project: Object Files and DACPAC Build",
                            "scenario": "You are creating a SQL database project for the SalesDB database. Create the project structure, add table definitions, and build the DACPAC.",
                            "code": """-- ============================================================
-- FILE: Tables/dbo.Customers.sql
-- ============================================================
CREATE TABLE [dbo].[Customers]
(
    [CustomerID]  INT           IDENTITY(1,1)  NOT NULL,
    [FirstName]   NVARCHAR(100)                NOT NULL,
    [LastName]    NVARCHAR(100)                NOT NULL,
    [Email]       NVARCHAR(200)                NOT NULL,
    [CreatedDate] DATETIME2(0)                 NOT NULL DEFAULT (GETUTCDATE()),
    CONSTRAINT [PK_Customers] PRIMARY KEY CLUSTERED ([CustomerID] ASC)
);
GO

-- ============================================================
-- FILE: Tables/dbo.Orders.sql
-- ============================================================
CREATE TABLE [dbo].[Orders]
(
    [OrderID]     INT           IDENTITY(1,1)  NOT NULL,
    [CustomerID]  INT                          NOT NULL,
    [OrderDate]   DATE                         NOT NULL,
    [TotalAmount] DECIMAL(10,2)               NOT NULL,
    [Status]      NVARCHAR(50)                 NOT NULL DEFAULT ('Pending'),
    CONSTRAINT [PK_Orders] PRIMARY KEY CLUSTERED ([OrderID] ASC),
    CONSTRAINT [FK_Orders_Customers] FOREIGN KEY ([CustomerID])
        REFERENCES [dbo].[Customers] ([CustomerID])
);
GO

-- ============================================================
-- FILE: Views/dbo.vw_OrderSummary.sql
-- ============================================================
CREATE VIEW [dbo].[vw_OrderSummary]
AS
SELECT
    c.CustomerID,
    c.FirstName + ' ' + c.LastName AS CustomerName,
    COUNT(o.OrderID)     AS TotalOrders,
    SUM(o.TotalAmount)   AS TotalRevenue,
    MAX(o.OrderDate)     AS LastOrderDate
FROM [dbo].[Customers] c
LEFT JOIN [dbo].[Orders] o ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerID, c.FirstName, c.LastName;
GO

-- ============================================================
-- FILE: Stored Procedures/dbo.usp_GetCustomerOrders.sql
-- ============================================================
CREATE PROCEDURE [dbo].[usp_GetCustomerOrders]
    @CustomerID INT,
    @StartDate  DATE = NULL,
    @EndDate    DATE = NULL
AS
BEGIN
    SET NOCOUNT ON;

    SELECT
        o.OrderID,
        o.OrderDate,
        o.TotalAmount,
        o.Status
    FROM [dbo].[Orders] o
    WHERE o.CustomerID = @CustomerID
      AND (@StartDate IS NULL OR o.OrderDate >= @StartDate)
      AND (@EndDate IS NULL OR o.OrderDate <= @EndDate)
    ORDER BY o.OrderDate DESC;
END;
GO

-- ============================================================
-- CLI COMMANDS (run in terminal, not SSMS)
-- ============================================================

-- Initialize git repository
-- git init
-- git add .
-- git commit -m "Initial database schema"

-- Build the project (produces bin/Debug/MyDatabase.dacpac)
-- dotnet build MyDatabase.sqlproj

-- Publish DACPAC to a local SQL Server
-- SqlPackage.exe /Action:Publish
--   /SourceFile:"bin/Debug/MyDatabase.dacpac"
--   /TargetServerName:"localhost"
--   /TargetDatabaseName:"SalesDB"
--   /TargetTrustServerCertificate:true

-- Generate a deployment script (preview changes, don't apply)
-- SqlPackage.exe /Action:Script
--   /SourceFile:"bin/Debug/MyDatabase.dacpac"
--   /TargetServerName:"localhost"
--   /TargetDatabaseName:"SalesDB"
--   /OutputPath:"deploy-preview.sql" """,
                            "explanation": "Each SQL file contains exactly one CREATE statement. The project build validates all files together (checking foreign keys, references, etc.) and produces a single DACPAC file. SqlPackage.exe then deploys the DACPAC by comparing it to the target database.",
                            "purpose": "Structure SQL schema as source-controlled code files that can be built, reviewed, tested, and deployed through an automated pipeline.",
                            "breakdown": [
                                {"line": "CONSTRAINT [PK_Customers] PRIMARY KEY CLUSTERED", "meaning": "Defines the primary key constraint with an explicit name. Always name constraints in a SQL project so SqlPackage knows what to compare by name, not just definition."},
                                {"line": "CONSTRAINT [FK_Orders_Customers] FOREIGN KEY REFERENCES [dbo].[Customers]", "meaning": "The foreign key references Customers by table name. In SQL projects, all referenced objects must exist in the same project or a reference — otherwise the build fails with 'unresolved reference'."},
                                {"line": "dotnet build MyDatabase.sqlproj", "meaning": "Builds the SQL project using the .NET SDK and SQL Server Data Tools MSBuild targets. Validates all SQL syntax and cross-object references. Produces bin/Debug/MyDatabase.dacpac."},
                                {"line": "SqlPackage.exe /Action:Publish", "meaning": "Deploys the DACPAC to a target database. Compares source (DACPAC) with target (existing database), generates the diff DDL, and applies it. Does not drop tables or data by default."},
                                {"line": "/Action:Script", "meaning": "Generates a deployment script without executing it. Use this to preview what changes would be made before deploying. Great for code review of database migrations."}
                            ],
                            "ssms_steps": [
                                "Install VS Code and the mssql extension (which includes SQL Database Projects)",
                                "In VS Code: Ctrl+Shift+P → 'Database Projects: Create new' → choose SQL Server → name it SalesDB",
                                "A .sqlproj file is created. Right-click the Tables folder → Add Table → name it Customers",
                                "VS Code creates a dbo.Customers.sql file with a template. Replace with your CREATE TABLE code",
                                "Repeat for Orders table, the View, and the Stored Procedure",
                                "Right-click the .sqlproj → Build — look for 'Build succeeded' in the output",
                                "Right-click .sqlproj → Publish → choose your local SQL Server connection",
                                "Click Generate Script to preview, or Publish to deploy directly"
                            ],
                            "exam_tip": "Each .sql file in a SQL project contains a CREATE statement (not ALTER, not DROP). The project build validates all references between objects. If a view references a table that does not exist in the project, the build fails. This is the advantage over running loose SQL scripts."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What command builds a SQL database project and produces a DACPAC file?",
                            "opts": ["A. SqlPackage.exe /Action:Build", "B. dotnet build MyDatabase.sqlproj", "C. msbuild /target:pack MyDatabase.sqlproj", "D. dacpac build --project MyDatabase.sqlproj"],
                            "correct": "B",
                            "explain": "SQL database projects are built with 'dotnet build <project>.sqlproj' (or msbuild directly). This validates the SQL syntax, checks cross-object references, and produces a .dacpac file in the bin/Debug or bin/Release folder."
                        },
                        {
                            "q": "What should each .sql file in a SQL database project contain?",
                            "opts": ["A. DROP and CREATE statements for the object", "B. A single CREATE statement for one database object", "C. All tables, views, and procedures for the database", "D. INSERT statements to seed reference data"],
                            "correct": "B",
                            "explain": "Each .sql file contains exactly one CREATE statement for one database object. Do NOT include DROP statements — SqlPackage handles the diff automatically and generates DROP or ALTER as needed during deployment."
                        },
                        {
                            "q": "What does SqlPackage.exe /Action:Script do?",
                            "opts": ["A. Runs a SQL script against the target database", "B. Generates a preview deployment script without executing changes", "C. Creates a new .sqlproj file from an existing database", "D. Backs up the target database before deployment"],
                            "correct": "B",
                            "explain": "/Action:Script generates a T-SQL deployment script showing exactly what changes would be made, but does NOT execute them. This is invaluable for reviewing database changes before deployment, especially in regulated environments."
                        },
                        {
                            "q": "A SQL database project has a view file referencing a table that is not in the project. What happens when you build?",
                            "opts": ["A. The build succeeds with a warning", "B. The build fails with an unresolved reference error", "C. The build skips the view file", "D. The view is created without the reference being validated"],
                            "correct": "B",
                            "explain": "One of the key benefits of SQL projects is that the build validates all object references. If a view references a table not in the project (or a referenced project), the build fails with an 'unresolved reference' error — catching schema issues before deployment."
                        },
                        {
                            "q": "What file type specifies the SQL Server target version for a database project?",
                            "opts": ["A. .dacpac", "B. .sqlproj", "C. .targets", "D. .config"],
                            "correct": "B",
                            "explain": "The .sqlproj file (XML format) contains the project configuration including DSP (Database Schema Provider) which specifies the target SQL Server version (e.g., Sql160DatabaseSchemaProvider for SQL Server 2022). This controls which T-SQL syntax and features are valid."
                        }
                    ]
                },

                # ── Unit 3: Source control and reference data ───────────
                {
                    "id": "lp2-m7-u3",
                    "title": "Source control and reference data",
                    "description": "Manage SQL project files with git and include reference/seed data in the project.",
                    "estimated_time": 20,
                    "objectives": [
                        "Initialize git for a SQL database project",
                        "Create a .gitignore for SQL project artifacts",
                        "Use post-deployment scripts for reference data"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Git Source Control for SQL Projects",
                            "body": "SQL database projects are just files — perfect for git. The workflow is:<ol><li>Create/clone the repository</li><li>Modify a .sql file (e.g., add a column to a table)</li><li>Run the project build to validate</li><li>Commit and push to the remote repository</li><li>Create a pull request for code review</li><li>Merge triggers the CI pipeline which builds and deploys the DACPAC</li></ol><strong>What to include in git:</strong><ul><li>All .sql files (object definitions)</li><li>The .sqlproj file</li><li>Post-deployment scripts (.sql files that run AFTER schema deployment)</li></ul><strong>What to exclude (.gitignore):</strong><ul><li>bin/ folder (contains the built .dacpac)</li><li>obj/ folder (intermediate build files)</li><li>*.user files (VS Code/SSDT personal settings)</li></ul><strong>Reference Data:</strong> Static lookup data (country codes, status types) belongs in a <strong>post-deployment script</strong> that runs after the schema is deployed. Use MERGE statements to upsert reference data safely."
                        },
                        {
                            "type": "sql_block",
                            "title": "Git Workflow and Post-Deployment Scripts",
                            "scenario": "Set up git for a SQL project and add a post-deployment script to seed lookup tables.",
                            "code": """-- ============================================================
-- Terminal / PowerShell commands for git setup
-- (Run in the SQL project folder)
-- ============================================================

-- git init
-- git add .
-- git commit -m "feat: initial database schema for SalesDB"

-- ============================================================
-- FILE: .gitignore (create in project root)
-- ============================================================
# Build output - don't commit these
bin/
obj/
*.user
*.suo
.vs/

# DACPAC is a build artifact - regenerated by CI
*.dacpac

-- ============================================================
-- FILE: Scripts/PostDeployment/Script.PostDeployment.sql
-- This file is marked as PostDeploymentScript in the .sqlproj
-- It runs AFTER all schema objects are deployed
-- ============================================================

-- Seed the OrderStatus lookup table using MERGE (safe for re-runs)
MERGE INTO [dbo].[OrderStatus] AS target
USING (
    VALUES
        (1, 'Pending',    'Order received, awaiting processing'),
        (2, 'Processing', 'Order is being processed'),
        (3, 'Shipped',    'Order has been shipped'),
        (4, 'Delivered',  'Order delivered to customer'),
        (5, 'Cancelled',  'Order was cancelled')
) AS source (StatusID, StatusName, Description)
ON target.StatusID = source.StatusID
WHEN MATCHED THEN
    UPDATE SET
        target.StatusName   = source.StatusName,
        target.Description  = source.Description
WHEN NOT MATCHED BY TARGET THEN
    INSERT (StatusID, StatusName, Description)
    VALUES (source.StatusID, source.StatusName, source.Description);
GO

-- ============================================================
-- FILE: Scripts/PostDeployment/SeedCountries.sql
-- Include this in Script.PostDeployment.sql with :r
-- ============================================================

-- :r .\\SeedCountries.sql

MERGE INTO [dbo].[Countries] AS target
USING (
    VALUES
        ('US', 'United States'),
        ('CA', 'Canada'),
        ('GB', 'United Kingdom'),
        ('AU', 'Australia')
) AS source (CountryCode, CountryName)
ON target.CountryCode = source.CountryCode
WHEN MATCHED THEN
    UPDATE SET target.CountryName = source.CountryName
WHEN NOT MATCHED BY TARGET THEN
    INSERT (CountryCode, CountryName)
    VALUES (source.CountryCode, source.CountryName);
GO

-- ============================================================
-- Git workflow for adding a new column
-- ============================================================

-- 1. Edit Tables/dbo.Orders.sql to add a column:
--    ADD [ShippingAddress] NVARCHAR(500) NULL

-- 2. In terminal:
-- git add Tables/dbo.Orders.sql
-- git commit -m "feat: add ShippingAddress column to Orders table"
-- git push origin feature/shipping-address""",
                            "explanation": "Post-deployment scripts run AFTER schema deployment, making them safe for data seeding. Using MERGE instead of INSERT ensures the script is idempotent (can be run multiple times without errors or duplicate data). The :r directive includes another SQL file.",
                            "purpose": "Maintain reference data and seed data in source control as idempotent scripts that can be safely re-run during any deployment.",
                            "breakdown": [
                                {"line": "bin/ and obj/ in .gitignore", "meaning": "The bin/ folder contains the built DACPAC, and obj/ contains intermediate build files. These are generated artifacts — never commit them. The CI pipeline rebuilds them from source."},
                                {"line": "Script.PostDeployment.sql marked as PostDeploymentScript", "meaning": "In the .sqlproj XML, a file can be marked as Build, PreDeploymentScript, or PostDeploymentScript. Post-deployment scripts run after all schema objects are created/updated."},
                                {"line": "MERGE INTO ... WHEN MATCHED THEN UPDATE ... WHEN NOT MATCHED BY TARGET THEN INSERT", "meaning": "MERGE is the SQL upsert pattern. If a row already exists (MATCHED), update it. If it does not exist (NOT MATCHED BY TARGET), insert it. This makes the script idempotent — safe to run on every deployment."},
                                {"line": ":r .\\SeedCountries.sql", "meaning": "The :r directive is used in SQL projects to include another .sql file's content inline. This lets you split large post-deployment scripts into multiple focused files."}
                            ],
                            "ssms_steps": [
                                "Open a terminal (PowerShell or Git Bash) in your SQL project folder",
                                "Run: git init to initialize the repository",
                                "Create a .gitignore file with the content shown above",
                                "Run: git add . and git commit -m 'Initial schema'",
                                "In VS Code, right-click the Scripts folder → Add New Item → Post-Deployment Script",
                                "Add the MERGE statement to seed reference data",
                                "Build the project to validate the post-deployment script",
                                "Publish to deploy both schema and reference data"
                            ],
                            "exam_tip": "Post-deployment scripts are the correct place for reference/seed data in SQL projects. Use MERGE (not INSERT) so the script is idempotent. The .gitignore must exclude bin/ and obj/ folders — DACPAC files are generated artifacts, not source files."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "Why should you use MERGE instead of INSERT in a post-deployment seed script?",
                            "opts": ["A. MERGE is faster than INSERT for large datasets", "B. MERGE is idempotent — it can be run multiple times without creating duplicate rows", "C. INSERT is not valid in post-deployment scripts", "D. MERGE automatically creates the target table if it does not exist"],
                            "correct": "B",
                            "explain": "Post-deployment scripts run on every deployment. If you use INSERT, you get duplicate rows on the second deployment. MERGE (upsert) updates existing rows and inserts new ones, making it safe to run multiple times with the same result."
                        },
                        {
                            "q": "Which folders should be added to .gitignore for a SQL database project?",
                            "opts": ["A. Tables/ and Views/", "B. bin/ and obj/", "C. Scripts/ and Security/", "D. .git/ and .vs/"],
                            "correct": "B",
                            "explain": "bin/ contains the built DACPAC (a generated artifact, not source code) and obj/ contains intermediate build files. These should be excluded from git — they are regenerated by the build process. Never commit generated artifacts to source control."
                        },
                        {
                            "q": "What does the :r directive do in a SQL post-deployment script?",
                            "opts": ["A. Runs the script with elevated permissions", "B. Includes the content of another SQL file inline", "C. Repeats the previous statement a specified number of times", "D. Rolls back the script if an error occurs"],
                            "correct": "B",
                            "explain": ":r <filepath> is a SQLCMD mode directive that includes another .sql file's content at that point in the script. It lets you split large post-deployment scripts into multiple smaller, focused files."
                        },
                        {
                            "q": "When you commit a change to a .sql object file in a SQL database project, what is the typical next step in the CI/CD process?",
                            "opts": ["A. SSMS automatically connects to production and runs the change", "B. The CI pipeline detects the commit, builds the project, and produces a DACPAC artifact", "C. SqlPackage.exe immediately deploys to production", "D. The database is backed up and the .sql file is archived"],
                            "correct": "B",
                            "explain": "In a CI/CD pipeline, a git commit triggers the CI pipeline (GitHub Actions, Azure Pipelines). The pipeline runs 'dotnet build' to validate and produce a DACPAC. The CD stage then uses SqlPackage.exe to deploy the DACPAC to the target environment."
                        },
                        {
                            "q": "Where should reference/lookup data (like country codes or status types) be maintained in a SQL project?",
                            "opts": ["A. In each table's .sql file as INSERT statements", "B. In a post-deployment script using MERGE statements", "C. In the .sqlproj file as embedded data", "D. In a separate database that the main database references"],
                            "correct": "B",
                            "explain": "Reference data belongs in a post-deployment script (marked as PostDeploymentScript in the project). Using MERGE makes it idempotent so it can be run on every deployment safely. Schema definition files (.sql) should only contain CREATE statements, not data."
                        }
                    ]
                },

                # ── Unit 4: Branching, pull requests, conflict resolution ─
                {
                    "id": "lp2-m7-u4",
                    "title": "Branching, pull requests, and conflict resolution",
                    "description": "Use feature branches and pull requests to manage concurrent schema changes safely.",
                    "estimated_time": 25,
                    "objectives": [
                        "Create feature branches for schema changes",
                        "Open a pull request for schema review",
                        "Resolve merge conflicts in SQL schema files"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Git Branching Strategy for SQL Projects",
                            "body": "The branching workflow for SQL projects mirrors application code development:<ol><li><strong>main/master</strong> — always reflects the production database schema. Never commit directly.</li><li><strong>feature/&lt;description&gt;</strong> — create a branch for each schema change</li><li><strong>Pull Request</strong> — the schema change is reviewed before merging to main</li><li><strong>CI on PR</strong> — build the project to validate SQL syntax automatically</li><li><strong>CD on merge</strong> — deploy DACPAC to production</li></ol><strong>Schema conflicts</strong> occur when two branches modify the same .sql file (e.g., two developers both add a column to dbo.Orders). Git will flag this as a merge conflict. Resolution is straightforward: manually edit the .sql file to include BOTH changes, then validate with a project build.<br><br><strong>The key rule:</strong> A .sql file contains ONE CREATE statement. If dev A adds column X and dev B adds column Y to the same table, the resolved file needs both columns in the CREATE TABLE."
                        },
                        {
                            "type": "sql_block",
                            "title": "Feature Branch and Conflict Resolution Workflow",
                            "scenario": "Two developers are adding columns to dbo.Orders simultaneously. Dev A adds DeliveryDate, Dev B adds TrackingNumber. They both work on feature branches.",
                            "code": """-- ============================================================
-- DEVELOPER A's work:
-- Terminal:
-- ============================================================
-- git checkout -b feature/add-delivery-date
-- Edit Tables/dbo.Orders.sql — add DeliveryDate column

-- FILE: Tables/dbo.Orders.sql (Developer A's version)
CREATE TABLE [dbo].[Orders]
(
    [OrderID]      INT           IDENTITY(1,1) NOT NULL,
    [CustomerID]   INT                         NOT NULL,
    [OrderDate]    DATE                        NOT NULL,
    [TotalAmount]  DECIMAL(10,2)               NOT NULL,
    [Status]       NVARCHAR(50)                NOT NULL DEFAULT ('Pending'),
    [DeliveryDate] DATE                        NULL,     -- NEW: Added by Dev A
    CONSTRAINT [PK_Orders] PRIMARY KEY CLUSTERED ([OrderID] ASC),
    CONSTRAINT [FK_Orders_Customers] FOREIGN KEY ([CustomerID])
        REFERENCES [dbo].[Customers] ([CustomerID])
);
GO

-- git add Tables/dbo.Orders.sql
-- git commit -m "feat: add DeliveryDate column to Orders"
-- git push origin feature/add-delivery-date
-- (Opens Pull Request in GitHub/Azure DevOps)

-- ============================================================
-- DEVELOPER B's work (simultaneously):
-- ============================================================
-- git checkout main
-- git checkout -b feature/add-tracking-number
-- Edit Tables/dbo.Orders.sql — add TrackingNumber column

-- FILE: Tables/dbo.Orders.sql (Developer B's version)
CREATE TABLE [dbo].[Orders]
(
    [OrderID]       INT           IDENTITY(1,1) NOT NULL,
    [CustomerID]    INT                         NOT NULL,
    [OrderDate]     DATE                        NOT NULL,
    [TotalAmount]   DECIMAL(10,2)               NOT NULL,
    [Status]        NVARCHAR(50)                NOT NULL DEFAULT ('Pending'),
    [TrackingNumber] NVARCHAR(100)              NULL,    -- NEW: Added by Dev B
    CONSTRAINT [PK_Orders] PRIMARY KEY CLUSTERED ([OrderID] ASC),
    CONSTRAINT [FK_Orders_Customers] FOREIGN KEY ([CustomerID])
        REFERENCES [dbo].[Customers] ([CustomerID])
);
GO

-- ============================================================
-- When Dev A's PR merges first, Dev B gets a CONFLICT.
-- Git marks the conflict in dbo.Orders.sql like this:
-- ============================================================

-- <<<<<<< HEAD (main after Dev A's merge)
-- [DeliveryDate] DATE NULL,
-- =======
-- [TrackingNumber] NVARCHAR(100) NULL,
-- >>>>>>> feature/add-tracking-number

-- ============================================================
-- RESOLVED FILE: Include BOTH columns
-- ============================================================
CREATE TABLE [dbo].[Orders]
(
    [OrderID]        INT           IDENTITY(1,1) NOT NULL,
    [CustomerID]     INT                         NOT NULL,
    [OrderDate]      DATE                        NOT NULL,
    [TotalAmount]    DECIMAL(10,2)               NOT NULL,
    [Status]         NVARCHAR(50)                NOT NULL DEFAULT ('Pending'),
    [DeliveryDate]   DATE                        NULL,     -- Dev A's change
    [TrackingNumber] NVARCHAR(100)               NULL,     -- Dev B's change
    CONSTRAINT [PK_Orders] PRIMARY KEY CLUSTERED ([OrderID] ASC),
    CONSTRAINT [FK_Orders_Customers] FOREIGN KEY ([CustomerID])
        REFERENCES [dbo].[Customers] ([CustomerID])
);
GO

-- After resolving:
-- git add Tables/dbo.Orders.sql
-- git commit -m "resolve: merge DeliveryDate and TrackingNumber columns"
-- dotnet build   (verify the resolved schema is valid)
-- git push""",
                            "explanation": "SQL merge conflicts are simpler than code conflicts because the file contains a single CREATE TABLE statement. The resolution is to include all changes from both branches in one valid CREATE TABLE. Always run dotnet build after resolving to verify the SQL is valid.",
                            "purpose": "Use feature branches to allow parallel schema development while ensuring all changes are reviewed and validated before reaching production.",
                            "breakdown": [
                                {"line": "git checkout -b feature/add-delivery-date", "meaning": "Creates a new branch named 'feature/add-delivery-date' and switches to it. All commits on this branch are isolated until you merge or rebase."},
                                {"line": "<<<<<<< HEAD / ======= / >>>>>>>", "meaning": "Git conflict markers. Content between <<<< HEAD and ==== is the version from the base branch. Content between ==== and >>>> is from the incoming branch. Delete the markers and keep/combine both changes."},
                                {"line": "dotnet build after resolving", "meaning": "Critical step: always build the project after resolving a conflict to ensure the merged .sql file is syntactically valid T-SQL. The CI pipeline does this too, but catching it locally is faster."}
                            ],
                            "ssms_steps": [
                                "In VS Code with the GitLens extension (or GitHub Desktop), create a feature branch: Ctrl+Shift+P → 'Git: Create Branch'",
                                "Make your change to the .sql file",
                                "Stage and commit: Source Control panel in VS Code (Ctrl+Shift+G) → + to stage → commit message → commit",
                                "Push to remote: ... menu → Push",
                                "In GitHub.com or Azure DevOps: New Pull Request from your feature branch to main",
                                "When a conflict is detected on PR merge, VS Code will show the conflict markers in the file",
                                "Edit the file to include both changes (remove <<< === >>> markers)",
                                "Build the project (right-click .sqlproj → Build) to validate",
                                "Stage, commit, and push the resolved file"
                            ],
                            "exam_tip": "SQL project conflicts are resolved at the file level — you edit the .sql file to include all changes from both branches. The key is that after resolving, you must always run a project build to validate the merged SQL is syntactically correct. CI pipeline should also run the build automatically."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What is the best branching strategy for SQL database schema changes?",
                            "opts": ["A. All developers commit directly to main branch", "B. Each schema change is made in a feature branch and merged via pull request", "C. Separate repository for each developer", "D. Use only one branch per release cycle"],
                            "correct": "B",
                            "explain": "Feature branches allow parallel development without conflicts. Pull requests enable code review of schema changes before they reach production. The main branch always reflects the production schema."
                        },
                        {
                            "q": "Two developers both modified dbo.Customers.sql on separate branches. What happens when the second branch tries to merge?",
                            "opts": ["A. The second change automatically wins", "B. Git creates a merge conflict that must be manually resolved", "C. The first change is automatically reverted", "D. Git creates two separate Customers tables"],
                            "correct": "B",
                            "explain": "When two branches modify the same file (dbo.Customers.sql), git cannot automatically determine the correct merged result and marks it as a merge conflict. A developer must manually edit the file to combine both changes, then validate and commit."
                        },
                        {
                            "q": "After resolving a merge conflict in a .sql file, what should you do before pushing?",
                            "opts": ["A. Run the SQL directly in SSMS to test", "B. Run dotnet build to validate the SQL syntax is correct", "C. Deploy to production immediately", "D. Delete the conflicting branch"],
                            "correct": "B",
                            "explain": "Running dotnet build validates that the conflict resolution produced syntactically valid T-SQL. It also checks cross-object references. Always build after resolving conflicts to catch errors locally before the CI pipeline catches them."
                        },
                        {
                            "q": "Which git command creates a new feature branch and switches to it?",
                            "opts": ["A. git branch feature/my-change", "B. git checkout -b feature/my-change", "C. git switch --new feature/my-change", "D. git create-branch feature/my-change"],
                            "correct": "B",
                            "explain": "git checkout -b <branch-name> creates a new branch from the current position and immediately switches to it. Equivalent: git switch -c <branch-name> in newer git versions. Both are valid."
                        },
                        {
                            "q": "In a pull request workflow for SQL projects, what does the CI pipeline typically validate?",
                            "opts": ["A. That all data in the database is correct", "B. That the SQL project builds successfully (syntax, references valid)", "C. That the DACPAC was already deployed to production", "D. That all unit tests in tSQLt pass against production data"],
                            "correct": "B",
                            "explain": "The CI pipeline on a PR typically runs 'dotnet build' to validate: (1) all .sql files have valid T-SQL syntax, (2) all cross-object references are resolvable (views reference existing tables, etc.), and (3) a valid DACPAC is produced. Data correctness is tested in a separate CD step against a test database."
                        }
                    ]
                },

                # ── Unit 5: Schema drift ────────────────────────────────
                {
                    "id": "lp2-m7-u5",
                    "title": "Schema drift",
                    "description": "Understand schema drift — when a database diverges from its source-controlled project — and how to detect and fix it.",
                    "estimated_time": 20,
                    "objectives": [
                        "Define schema drift and its causes",
                        "Detect drift using SqlPackage /Action:DeployReport",
                        "Fix drift by publishing the authoritative DACPAC"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "What Is Schema Drift?",
                            "body": "Schema drift happens when the <strong>actual database schema</strong> in an environment (dev, test, or production) diverges from the <strong>schema defined in source control</strong>.<br><br><strong>Common causes of drift:</strong><ul><li>A developer ran an ad-hoc ALTER TABLE directly in production to fix an emergency — without updating the SQL project</li><li>Someone created a debugging stored procedure that was never removed</li><li>A manual hotfix was applied but never backported to source control</li><li>A third-party application added columns to shared tables</li></ul><strong>Why drift is dangerous:</strong><ul><li>The next DACPAC deployment might DROP the manually-added column (data loss!)</li><li>The development environment does not match production — bugs happen in prod but cannot be reproduced in dev</li><li>Compliance audits fail because the deployed schema does not match the reviewed schema in source control</li></ul><strong>Drift prevention:</strong> Never modify production databases directly. All changes must go through the SQL project → DACPAC → pipeline process."
                        },
                        {
                            "type": "sql_block",
                            "title": "Detect and Remediate Schema Drift",
                            "scenario": "Someone added a column TaxExempt to the Orders table directly in production. Your SQL project does not have this column. Detect and decide how to handle the drift.",
                            "code": """-- ============================================================
-- STEP 1: Detect drift using SqlPackage DeployReport
-- Run in terminal/PowerShell
-- ============================================================

-- Generate a drift report (what DACPAC would do to target)
-- SqlPackage.exe /Action:DeployReport
--   /SourceFile:"bin/Release/SalesDB.dacpac"
--   /TargetServerName:"prod-sql.database.windows.net"
--   /TargetDatabaseName:"SalesDB"
--   /TargetUser:"sqladmin"
--   /TargetPassword:"$(SQL_PASSWORD)"
--   /OutputPath:"drift-report.xml"

-- The report XML will show:
-- <Operation Name="Drop">
--   <Item Value="[dbo].[Orders].[TaxExempt]" Type="SqlColumn" />
-- </Operation>
-- This means: deploying the DACPAC would DROP the TaxExempt column!

-- ============================================================
-- STEP 2: Option A — Add the drifted column to the SQL project
-- (The correct approach if the column is intentional)
-- ============================================================

-- Edit Tables/dbo.Orders.sql in the SQL project:
CREATE TABLE [dbo].[Orders]
(
    [OrderID]      INT           IDENTITY(1,1) NOT NULL,
    [CustomerID]   INT                         NOT NULL,
    [OrderDate]    DATE                        NOT NULL,
    [TotalAmount]  DECIMAL(10,2)               NOT NULL,
    [Status]       NVARCHAR(50)                NOT NULL DEFAULT ('Pending'),
    [TaxExempt]    BIT                         NOT NULL DEFAULT (0), -- Added: backport drift
    CONSTRAINT [PK_Orders] PRIMARY KEY CLUSTERED ([OrderID] ASC)
);
GO

-- Then:
-- git add Tables/dbo.Orders.sql
-- git commit -m "fix: backport TaxExempt column from production to SQL project"
-- git push origin main (after PR review)

-- ============================================================
-- STEP 3: Option B — Deploy DACPAC with DropObjectsNotInSource = false
-- Protects columns in production that are not in the DACPAC
-- USE WITH CAUTION — this hides drift
-- ============================================================

-- SqlPackage.exe /Action:Publish
--   /SourceFile:"bin/Release/SalesDB.dacpac"
--   /TargetServerName:"prod-sql.database.windows.net"
--   /TargetDatabaseName:"SalesDB"
--   /p:DropObjectsNotInSource=false  ← prevents dropping extra columns/tables

-- ============================================================
-- STEP 4: Check for drift using T-SQL schema comparison
-- Compare sys.columns between environments
-- ============================================================
-- Run this on both databases and compare results:
SELECT
    t.name AS TableName,
    c.name AS ColumnName,
    ty.name AS DataType,
    c.max_length,
    c.is_nullable,
    c.column_id
FROM sys.columns c
JOIN sys.tables t ON c.object_id = t.object_id
JOIN sys.types ty ON c.user_type_id = ty.user_type_id
WHERE t.type = 'U'      -- user tables only
ORDER BY t.name, c.column_id;""",
                            "explanation": "Schema drift is detected by comparing what the DACPAC would do to the target (DeployReport). If the report shows DROP operations you did not expect, you have drift. The correct fix is to backport the drifted change to the SQL project — not to suppress the DROP with flags.",
                            "purpose": "Detect when a database has diverged from the source-controlled schema and decide the best remediation strategy.",
                            "breakdown": [
                                {"line": "/Action:DeployReport", "meaning": "SqlPackage action that generates an XML report of what would happen during a publish. Shows operations like Create, Alter, Drop for each object. Use this to detect drift before actually deploying."},
                                {"line": "DropObjectsNotInSource=false", "meaning": "DACPAC deployment property that prevents SqlPackage from dropping objects in the target database that are not in the DACPAC. Useful as a safety net but masks drift rather than fixing it."},
                                {"line": "sys.columns query", "meaning": "Query against system catalog views to see all columns in all tables. Run the same query on dev and production databases and compare results to manually identify drift."}
                            ],
                            "ssms_steps": [
                                "Open SSMS and connect to both dev and production databases",
                                "Run the sys.columns query on both and copy results to Excel",
                                "Compare columns — any differences are schema drift",
                                "For automated detection: run SqlPackage /Action:DeployReport and inspect the XML output",
                                "To fix drift: add the missing change to the SQL project, create a PR, get it reviewed, merge, and let the pipeline deploy",
                                "NEVER suppress drift with DropObjectsNotInSource=false permanently — fix the root cause instead"
                            ],
                            "exam_tip": "The exam may present a scenario where a DACPAC deployment would drop a column from production. The correct answer is to backport the column to the SQL project (add it to the CREATE TABLE in the project) and redeploy — not to use flags to suppress the DROP."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What is database schema drift?",
                            "opts": ["A. Performance degradation over time in a database", "B. When the actual database schema differs from the schema defined in source control", "C. Data corruption caused by concurrent write transactions", "D. When database statistics become stale over time"],
                            "correct": "B",
                            "explain": "Schema drift occurs when someone makes direct changes to a database (ALTER TABLE in production) without updating the SQL project in source control. The deployed schema no longer matches what is in git."
                        },
                        {
                            "q": "Which SqlPackage action detects what changes a DACPAC deployment would make without actually deploying?",
                            "opts": ["A. /Action:Publish", "B. /Action:Extract", "C. /Action:DeployReport", "D. /Action:DriftScan"],
                            "correct": "C",
                            "explain": "/Action:DeployReport generates an XML report listing all operations (Create, Alter, Drop) that would be performed if you ran /Action:Publish. Use this to review expected changes before deploying."
                        },
                        {
                            "q": "A DeployReport shows DROP COLUMN [TaxExempt] on the production Orders table. The column was added directly in production. What is the correct remediation?",
                            "opts": ["A. Set DropObjectsNotInSource=false to prevent the DROP permanently", "B. Add the TaxExempt column to the SQL project's dbo.Orders.sql and commit it", "C. Delete the column from production before deploying", "D. Exclude the Orders table from DACPAC deployment"],
                            "correct": "B",
                            "explain": "The correct fix for schema drift is to backport the change to source control. Add the TaxExempt column to the CREATE TABLE in dbo.Orders.sql, commit via a PR, and redeploy. The source-controlled project becomes the source of truth."
                        },
                        {
                            "q": "What does the SqlPackage property DropObjectsNotInSource=false do?",
                            "opts": ["A. Prevents the deployment if source objects are missing", "B. Prevents SqlPackage from dropping objects in the target that are not in the DACPAC", "C. Creates source objects that are missing from the target", "D. Disables the deployment report output"],
                            "correct": "B",
                            "explain": "With DropObjectsNotInSource=false, objects in the target database that are not in the DACPAC are left in place (not dropped). This prevents accidental data loss during drift remediation, but it is not a permanent solution — it hides the drift."
                        },
                        {
                            "q": "Which system catalog view can you query to list all columns in all user tables to manually compare schemas between environments?",
                            "opts": ["A. sys.tables", "B. information_schema.tables", "C. sys.columns joined with sys.tables", "D. sys.objects WHERE type = 'C'"],
                            "correct": "C",
                            "explain": "sys.columns contains one row per column per table with column_id, name, data type, nullability, etc. Joined to sys.tables to get table names. Query this on both environments and compare to identify drift."
                        }
                    ]
                },

                # ── Unit 6: CI/CD pipelines for SQL ────────────────────
                {
                    "id": "lp2-m7-u6",
                    "title": "CI/CD pipelines for SQL",
                    "description": "Build and configure GitHub Actions or Azure DevOps pipelines to automate SQL database deployment.",
                    "estimated_time": 30,
                    "objectives": [
                        "Write a GitHub Actions workflow that builds a SQL project and deploys the DACPAC",
                        "Configure Azure DevOps pipeline for SQL deployment",
                        "Understand deployment stages: build, test, deploy to dev/staging/prod"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "CI/CD Pipeline Stages for SQL Databases",
                            "body": "A complete CI/CD pipeline for SQL databases has these stages:<ol><li><strong>CI (Continuous Integration)</strong> — on every PR/commit: build the project, validate SQL syntax, run unit tests against a test database, generate the DACPAC artifact</li><li><strong>CD to Dev</strong> — on merge to main: deploy DACPAC to dev environment, run integration tests</li><li><strong>CD to Staging</strong> — manual approval: deploy to staging (production-like), run smoke tests</li><li><strong>CD to Production</strong> — manual approval + monitoring: deploy to production, verify deployment</li></ol><strong>Tools used:</strong><ul><li><strong>GitHub Actions</strong> — YAML workflow files in .github/workflows/</li><li><strong>Azure DevOps Pipelines</strong> — YAML in azure-pipelines.yml</li><li><strong>SqlPackage.exe</strong> — the tool that does the actual DACPAC deployment</li><li><strong>Azure SQL Action</strong> — GitHub Action wrapper for SqlPackage</li></ul>"
                        },
                        {
                            "type": "sql_block",
                            "title": "GitHub Actions CI/CD Pipeline for SQL Database",
                            "scenario": "Create a complete GitHub Actions workflow that builds a SQL project on PR, then deploys to Azure SQL on merge to main.",
                            "code": """# FILE: .github/workflows/sql-cicd.yml
# ============================================================
# GitHub Actions CI/CD Pipeline for SQL Database Project
# ============================================================

name: SQL Database CI/CD

on:
  push:
    branches: [main]          # Deploy on push to main
  pull_request:
    branches: [main]          # Build & test on PRs

env:
  PROJECT_PATH: 'src/SalesDB/SalesDB.sqlproj'
  DACPAC_NAME: 'SalesDB.dacpac'

jobs:
  # ──────────────────────────────────────────────────────────
  # JOB 1: CI — Build and validate the SQL project
  # ──────────────────────────────────────────────────────────
  build:
    name: Build SQL Project
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup .NET SDK
        uses: actions/setup-dotnet@v4
        with:
          dotnet-version: '8.0.x'

      - name: Install SQL project build tools
        run: dotnet tool install -g microsoft.sqlpackage

      - name: Build SQL project (produces DACPAC)
        run: dotnet build ${{ env.PROJECT_PATH }}
               --configuration Release
               --output ./dacpac-output

      - name: Upload DACPAC artifact
        uses: actions/upload-artifact@v4
        with:
          name: dacpac-artifact
          path: ./dacpac-output/${{ env.DACPAC_NAME }}
          retention-days: 7

  # ──────────────────────────────────────────────────────────
  # JOB 2: CD — Deploy to Azure SQL (only on push to main)
  # ──────────────────────────────────────────────────────────
  deploy-dev:
    name: Deploy to Dev Database
    runs-on: ubuntu-latest
    needs: build                          # Only run after build succeeds
    if: github.ref == 'refs/heads/main'   # Only on push to main (not PRs)
    environment: dev                      # GitHub Environment for approval

    steps:
      - name: Download DACPAC artifact
        uses: actions/download-artifact@v4
        with:
          name: dacpac-artifact
          path: ./dacpac

      - name: Deploy DACPAC to Azure SQL
        uses: azure/sql-action@v2
        with:
          connection-string: ${{ secrets.DEV_SQL_CONNECTION_STRING }}
          path: './dacpac/${{ env.DACPAC_NAME }}'
          action: 'publish'
          arguments: '/p:DropObjectsNotInSource=false'

  # ──────────────────────────────────────────────────────────
  # JOB 3: Deploy to Production (manual approval required)
  # ──────────────────────────────────────────────────────────
  deploy-prod:
    name: Deploy to Production Database
    runs-on: ubuntu-latest
    needs: deploy-dev
    environment: production    # Requires reviewer approval in GitHub

    steps:
      - name: Download DACPAC artifact
        uses: actions/download-artifact@v4
        with:
          name: dacpac-artifact
          path: ./dacpac

      - name: Deploy DACPAC to Production Azure SQL
        uses: azure/sql-action@v2
        with:
          connection-string: ${{ secrets.PROD_SQL_CONNECTION_STRING }}
          path: './dacpac/${{ env.DACPAC_NAME }}'
          action: 'publish'""",
                            "explanation": "The pipeline has three jobs: build (runs on every PR and push), deploy-dev (runs on push to main only), and deploy-prod (requires manual approval). Secrets store connection strings — never hardcode them in YAML files.",
                            "purpose": "Automate the SQL database deployment lifecycle from code commit to production using a structured, approval-gated CI/CD pipeline.",
                            "breakdown": [
                                {"line": "on: push: branches: [main] / pull_request: branches: [main]", "meaning": "The workflow triggers on two events: push to main (full pipeline runs) and PRs targeting main (build job only runs, to validate before merge)."},
                                {"line": "needs: build", "meaning": "Job dependency: deploy-dev only runs if the build job completed successfully. This prevents deployment of a broken DACPAC."},
                                {"line": "if: github.ref == 'refs/heads/main'", "meaning": "Conditional: this job only runs on push to main, not on pull request triggers. Prevents auto-deployment from PRs."},
                                {"line": "environment: production", "meaning": "GitHub Environments can require named reviewers to approve before the job runs. Configure this in GitHub Settings → Environments → production → Required reviewers."},
                                {"line": "${{ secrets.PROD_SQL_CONNECTION_STRING }}", "meaning": "References a GitHub secret — a securely stored value. Never put connection strings or passwords in the YAML file. Store them in GitHub Settings → Secrets."},
                                {"line": "azure/sql-action@v2", "meaning": "An official GitHub Action by Microsoft that wraps SqlPackage.exe. It handles authentication and runs the DACPAC publish against Azure SQL Database."}
                            ],
                            "ssms_steps": [
                                "This is a GitHub Actions task — no SSMS needed",
                                "Create the file at .github/workflows/sql-cicd.yml in your git repository",
                                "In GitHub.com → repository Settings → Secrets and variables → Actions → New repository secret",
                                "Add DEV_SQL_CONNECTION_STRING and PROD_SQL_CONNECTION_STRING as secrets",
                                "For production approval: Settings → Environments → New environment → 'production' → add required reviewers",
                                "Push the workflow file: git add .github/workflows/ && git commit && git push",
                                "Go to GitHub → Actions tab → watch the workflow run",
                                "Check the deploy-prod job — it should wait for approval before proceeding"
                            ],
                            "exam_tip": "Key CI/CD concepts: CI builds and validates on every commit/PR. CD deploys automatically to dev on merge to main. Production deployment requires manual approval (GitHub Environments). Secrets store connection strings — never in YAML. DACPAC is the artifact passed between jobs."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "In a GitHub Actions CI/CD pipeline, where should Azure SQL connection strings be stored?",
                            "opts": ["A. Directly in the YAML workflow file", "B. In a .env file committed to the repository", "C. In GitHub repository Secrets", "D. In the .sqlproj file"],
                            "correct": "C",
                            "explain": "Connection strings contain passwords and should never be in source code or YAML files. Store them in GitHub repository Secrets (Settings → Secrets and variables → Actions). Reference them in YAML as ${{ secrets.SECRET_NAME }}."
                        },
                        {
                            "q": "What does 'needs: build' in a GitHub Actions job definition specify?",
                            "opts": ["A. The job needs the .NET build SDK installed", "B. This job depends on the 'build' job completing successfully", "C. The job needs additional build steps before running", "D. The DACPAC needs to be built before deployment"],
                            "correct": "B",
                            "explain": "'needs: build' creates a job dependency — the current job will not start until the 'build' job completes successfully. This ensures the deploy job only runs with a valid DACPAC artifact."
                        },
                        {
                            "q": "How do you require a human reviewer to approve a production deployment in GitHub Actions?",
                            "opts": ["A. Add an approval step in the YAML workflow with manual approval action", "B. Configure a GitHub Environment with required reviewers and reference it in the job", "C. Add a pause step that waits for an email response", "D. Create a special branch rule for production"],
                            "correct": "B",
                            "explain": "GitHub Environments support protection rules including required reviewers. Set environment: production in the job. Configure the 'production' environment in GitHub Settings → Environments → Required reviewers. The job waits for approval before running."
                        },
                        {
                            "q": "Which GitHub Action is used to deploy a DACPAC to Azure SQL Database?",
                            "opts": ["A. actions/setup-dotnet", "B. azure/sql-action", "C. microsoft/deploy-dacpac", "D. actions/deploy-sql"],
                            "correct": "B",
                            "explain": "azure/sql-action is the official Microsoft GitHub Action for SQL database operations. It wraps SqlPackage.exe and supports publish, script, and drift-check actions against Azure SQL Database."
                        },
                        {
                            "q": "You want the CI pipeline to run on pull requests but NOT deploy the DACPAC. Which condition achieves this?",
                            "opts": ["A. if: github.event_name == 'push'", "B. if: github.ref == 'refs/heads/main'", "C. if: github.event == 'pull_request'", "D. if: github.branch == 'feature/*'"],
                            "correct": "B",
                            "explain": "if: github.ref == 'refs/heads/main' restricts the deploy job to only run when the trigger is a push to the main branch. Pull requests have a different ref (refs/pull/N/merge), so they won't trigger the deployment job."
                        }
                    ]
                },

                # ── Unit 7: Testing strategy for SQL databases ──────────
                {
                    "id": "lp2-m7-u7",
                    "title": "Testing strategy for SQL databases",
                    "description": "Write and run automated tests for SQL databases using the tSQLt framework.",
                    "estimated_time": 25,
                    "objectives": [
                        "Understand why automated SQL testing matters",
                        "Create a tSQLt test class and test procedures",
                        "Mock tables and stored procedures in tSQLt tests"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Testing SQL Databases with tSQLt",
                            "body": "Just like application code needs unit tests, SQL database objects need tests too. Without tests, you cannot be confident that a schema change or stored procedure modification does not break existing functionality.<br><br><strong>tSQLt</strong> is an open-source unit testing framework for SQL Server written entirely in T-SQL:<ul><li>Tests are T-SQL stored procedures with names starting with 'test'</li><li>Test classes are SQL schemas</li><li>Supports table mocking (fake tables for isolation)</li><li>Supports stored procedure mocking (spy on calls)</li><li>Each test runs in a transaction that is rolled back at the end — no permanent data changes</li><li>Works in SQL Server and Azure SQL Database</li></ul><strong>Types of SQL tests:</strong><ul><li><strong>Unit tests</strong> — test one stored procedure in isolation, mocking its dependencies</li><li><strong>Integration tests</strong> — test a workflow end-to-end against a test database copy</li><li><strong>Schema tests</strong> — assert that required columns, indexes, or constraints exist</li></ul>"
                        },
                        {
                            "type": "sql_block",
                            "title": "Write tSQLt Unit Tests for a Stored Procedure",
                            "scenario": "You have a stored procedure usp_ApplyDiscount that applies a 10% discount to orders over $100. Write tSQLt tests to verify it works correctly.",
                            "code": """-- ============================================================
-- SETUP: Install tSQLt (run once per database)
-- Download tSQLt.class.sql from tsqlt.org and run it
-- EXEC tSQLt.NewTestClass 'OrderTests';
-- ============================================================

-- Step 1: Create a tSQLt test class (a schema for this test group)
EXEC tSQLt.NewTestClass 'OrderTests';
GO

-- Step 2: The stored procedure we are testing
CREATE OR ALTER PROCEDURE [dbo].[usp_ApplyDiscount]
    @OrderID INT
AS
BEGIN
    UPDATE dbo.Orders
    SET TotalAmount = TotalAmount * 0.90  -- 10% discount
    WHERE OrderID = @OrderID
      AND TotalAmount > 100.00;           -- Only orders over $100
END;
GO

-- Step 3: Write a test for the happy path (discount should apply)
CREATE OR ALTER PROCEDURE [OrderTests].[test usp_ApplyDiscount applies 10 pct discount]
AS
BEGIN
    -- ARRANGE: Create a fake (isolated) copy of Orders table
    EXEC tSQLt.FakeTable 'dbo.Orders';

    -- Insert test data into the fake table
    INSERT INTO dbo.Orders (OrderID, CustomerID, TotalAmount, OrderDate, Status)
    VALUES (1, 100, 200.00, '2024-01-01', 'Pending');  -- $200 order (> $100)

    -- ACT: Run the stored procedure
    EXEC dbo.usp_ApplyDiscount @OrderID = 1;

    -- ASSERT: Check that discount was applied (200 * 0.9 = 180)
    DECLARE @actual DECIMAL(10,2);
    SELECT @actual = TotalAmount FROM dbo.Orders WHERE OrderID = 1;

    EXEC tSQLt.AssertEquals
        @Expected = 180.00,
        @Actual   = @actual,
        @Message  = 'Expected 10% discount on $200 order = $180';
END;
GO

-- Step 4: Write a test for the negative case (no discount under $100)
CREATE OR ALTER PROCEDURE [OrderTests].[test usp_ApplyDiscount does not discount orders under 100]
AS
BEGIN
    -- ARRANGE: Fake table for isolation
    EXEC tSQLt.FakeTable 'dbo.Orders';

    INSERT INTO dbo.Orders (OrderID, CustomerID, TotalAmount, OrderDate, Status)
    VALUES (2, 101, 50.00, '2024-01-01', 'Pending');   -- $50 order (< $100)

    -- ACT
    EXEC dbo.usp_ApplyDiscount @OrderID = 2;

    -- ASSERT: Amount should be unchanged at $50
    DECLARE @actual DECIMAL(10,2);
    SELECT @actual = TotalAmount FROM dbo.Orders WHERE OrderID = 2;

    EXEC tSQLt.AssertEquals
        @Expected = 50.00,
        @Actual   = @actual,
        @Message  = 'Orders under $100 should not receive discount';
END;
GO

-- Step 5: Run all tests in the OrderTests class
EXEC tSQLt.RunTestClass 'OrderTests';
GO

-- Step 6: Run ALL tests in the database
EXEC tSQLt.RunAll;
GO

-- Results show: [SUCCESS] or [FAILURE] with details
-- All tests run in a rolled-back transaction - no permanent data changes""",
                            "explanation": "tSQLt tests follow the Arrange-Act-Assert (AAA) pattern. FakeTable creates an empty copy of the target table in a transaction so tests are isolated and no real data is affected. Every test is rolled back after execution — safe to run in any environment.",
                            "purpose": "Validate stored procedure logic with automated tests that run in the CI pipeline, catching bugs before they reach production.",
                            "breakdown": [
                                {"line": "EXEC tSQLt.NewTestClass 'OrderTests'", "meaning": "Creates a new SQL schema named 'OrderTests'. All test stored procedures within this schema will be recognized as tests by tSQLt."},
                                {"line": "EXEC tSQLt.FakeTable 'dbo.Orders'", "meaning": "Replaces the real dbo.Orders table with an empty copy for the duration of the test. This isolates the test from real data. The fake table is automatically removed when the test transaction rolls back."},
                                {"line": "EXEC tSQLt.AssertEquals @Expected = 180.00, @Actual = @actual", "meaning": "The core assertion: if @Expected equals @Actual, the test passes. If they differ, the test fails with the @Message text shown in the results."},
                                {"line": "EXEC tSQLt.RunTestClass 'OrderTests'", "meaning": "Runs all stored procedures in the 'OrderTests' schema whose names start with 'test'. Each test runs in its own transaction that is rolled back."},
                                {"line": "CREATE OR ALTER PROCEDURE [OrderTests].[test usp_ApplyDiscount ...]", "meaning": "Test procedure naming convention: schema = test class name (OrderTests), procedure name starts with 'test'. tSQLt discovers tests by this naming pattern."}
                            ],
                            "ssms_steps": [
                                "Download tSQLt from tsqlt.org and follow installation instructions for your SQL Server version",
                                "In SSMS: run the tSQLt.class.sql installation script against your test database",
                                "Run EXEC tSQLt.NewTestClass 'OrderTests' to create the test class",
                                "Create the test procedures (Steps 3-4) in a new query window",
                                "Run EXEC tSQLt.RunTestClass 'OrderTests' to execute the tests",
                                "Check the results — each test shows [SUCCESS] or [FAILURE] with a message",
                                "Add the test execution to your CI pipeline: SqlCmd.exe -S server -d db -Q \"EXEC tSQLt.RunAll\""
                            ],
                            "exam_tip": "For the exam: tSQLt is a T-SQL testing framework. Tests are stored procedures in named schemas (test classes). FakeTable isolates tests from real data. Tests run in rolled-back transactions. AssertEquals validates results. Integrate with CI by running EXEC tSQLt.RunAll in the pipeline."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What does tSQLt.FakeTable do during a test?",
                            "opts": ["A. Creates a permanent copy of the table in a test schema", "B. Replaces the real table with an empty isolated copy for the test duration", "C. Generates fake data in the real table", "D. Creates a snapshot of the table for rollback"],
                            "correct": "B",
                            "explain": "tSQLt.FakeTable replaces the specified table with an empty copy within the test transaction. The test works with this isolated fake table. When the test finishes, the transaction rolls back and the real table is restored."
                        },
                        {
                            "q": "What naming convention must tSQLt test procedures follow?",
                            "opts": ["A. Prefix with 'test_' in the dbo schema", "B. Prefix name with 'test' and place in a named test class schema", "C. End the procedure name with '_Test'", "D. Include 'tSQLt' in the procedure name"],
                            "correct": "B",
                            "explain": "tSQLt discovers tests by looking for stored procedures whose names start with 'test' (case-insensitive) in schemas created by tSQLt.NewTestClass. Example: [OrderTests].[test my_procedure does something]"
                        },
                        {
                            "q": "Which tSQLt procedure runs all tests in the database?",
                            "opts": ["A. EXEC tSQLt.RunTests", "B. EXEC tSQLt.ExecuteAll", "C. EXEC tSQLt.RunAll", "D. EXEC tSQLt.RunClass 'ALL'"],
                            "correct": "C",
                            "explain": "EXEC tSQLt.RunAll runs every test in all test classes (schemas) in the database. EXEC tSQLt.RunTestClass 'ClassName' runs only tests in a specific class."
                        },
                        {
                            "q": "Why does each tSQLt test run inside a transaction that gets rolled back?",
                            "opts": ["A. To improve test performance by avoiding disk writes", "B. To ensure tests are isolated — no test affects real data or other tests", "C. To allow multiple tests to run in parallel", "D. Because SQL Server cannot commit within stored procedures"],
                            "correct": "B",
                            "explain": "Running tests in rolled-back transactions ensures: (1) tests don't corrupt real data, (2) tests don't affect each other (isolation), and (3) the same tests can be run repeatedly with the same results. The database is unchanged after test execution."
                        },
                        {
                            "q": "Where in a CI/CD pipeline should SQL unit tests (tSQLt) run?",
                            "opts": ["A. Only in production to verify the deployment", "B. After deploying the DACPAC to a test database, before promoting to staging or production", "C. Before the SQL project is built", "D. Only in the developer's local environment, not in the pipeline"],
                            "correct": "B",
                            "explain": "In a CI/CD pipeline: (1) build the DACPAC, (2) deploy to a test database, (3) run tSQLt.RunAll against the test database, (4) if tests pass, promote to staging/production. This catches stored procedure bugs before they reach production."
                        }
                    ]
                },

                # ── Unit 8: Exercise ────────────────────────────────────
                {
                    "id": "lp2-m7-u8",
                    "title": "Exercise",
                    "description": "Hands-on exercise: create a complete SQL database project with CI/CD pipeline.",
                    "estimated_time": 45,
                    "objectives": [
                        "Create a SQL project with multiple objects",
                        "Set up git and create a feature branch",
                        "Write a tSQLt test for a stored procedure"
                    ],
                    "content": [
                        {
                            "type": "sql_block",
                            "title": "Exercise: Build a Complete SQL Project with Tests and Pipeline",
                            "scenario": "Create a ProductDB SQL project with tables, a stored procedure, tSQLt tests, and a GitHub Actions pipeline. This simulates a real-world database DevOps setup.",
                            "code": """-- ============================================================
-- PART 1: SQL Project structure (create these files in VS Code)
-- ============================================================

-- FILE: Tables/dbo.Products.sql
CREATE TABLE [dbo].[Products]
(
    [ProductID]   INT           IDENTITY(1,1) NOT NULL,
    [ProductName] NVARCHAR(200)               NOT NULL,
    [Price]       DECIMAL(10,2)               NOT NULL,
    [StockQty]    INT                         NOT NULL DEFAULT(0),
    [IsActive]    BIT                         NOT NULL DEFAULT(1),
    CONSTRAINT [PK_Products] PRIMARY KEY CLUSTERED ([ProductID] ASC)
);
GO

-- FILE: Stored Procedures/dbo.usp_UpdateStock.sql
CREATE PROCEDURE [dbo].[usp_UpdateStock]
    @ProductID INT,
    @Quantity  INT      -- positive = restock, negative = sale
AS
BEGIN
    SET NOCOUNT ON;

    -- Prevent negative stock
    IF EXISTS (
        SELECT 1 FROM dbo.Products
        WHERE ProductID = @ProductID
          AND (StockQty + @Quantity) < 0
    )
    BEGIN
        RAISERROR('Insufficient stock for product %d', 16, 1, @ProductID);
        RETURN;
    END;

    UPDATE dbo.Products
    SET StockQty = StockQty + @Quantity
    WHERE ProductID = @ProductID;
END;
GO

-- ============================================================
-- PART 2: tSQLt Tests
-- FILE: Tests/ProductTests.sql (marked as Build in project)
-- ============================================================

EXEC tSQLt.NewTestClass 'ProductTests';
GO

CREATE OR ALTER PROCEDURE [ProductTests].[test usp_UpdateStock adds stock correctly]
AS
BEGIN
    EXEC tSQLt.FakeTable 'dbo.Products';

    INSERT INTO dbo.Products (ProductID, ProductName, Price, StockQty, IsActive)
    VALUES (1, 'Widget', 9.99, 100, 1);

    EXEC dbo.usp_UpdateStock @ProductID = 1, @Quantity = 50;  -- restock

    DECLARE @result INT;
    SELECT @result = StockQty FROM dbo.Products WHERE ProductID = 1;

    EXEC tSQLt.AssertEquals
        @Expected = 150,
        @Actual   = @result,
        @Message  = 'Stock should be 150 after adding 50 to 100';
END;
GO

CREATE OR ALTER PROCEDURE [ProductTests].[test usp_UpdateStock raises error for negative stock]
AS
BEGIN
    EXEC tSQLt.FakeTable 'dbo.Products';

    INSERT INTO dbo.Products (ProductID, ProductName, Price, StockQty, IsActive)
    VALUES (1, 'Widget', 9.99, 10, 1);

    -- Try to sell 20 when only 10 in stock — should raise error
    EXEC tSQLt.ExpectException @ExpectedMessage = 'Insufficient stock for product 1';
    EXEC dbo.usp_UpdateStock @ProductID = 1, @Quantity = -20;
END;
GO

-- ============================================================
-- PART 3: GitHub Actions workflow (create file manually)
-- FILE: .github/workflows/productdb-cicd.yml
-- ============================================================

# name: ProductDB CI/CD
# on:
#   push:
#     branches: [main]
#   pull_request:
#     branches: [main]
#
# jobs:
#   build-and-test:
#     runs-on: ubuntu-latest
#     services:
#       sqlserver:
#         image: mcr.microsoft.com/mssql/server:2022-latest
#         env:
#           ACCEPT_EULA: Y
#           SA_PASSWORD: TestP@ssw0rd!
#         ports: [1433:1433]
#     steps:
#       - uses: actions/checkout@v4
#       - uses: actions/setup-dotnet@v4
#         with: { dotnet-version: '8.0.x' }
#       - name: Build DACPAC
#         run: dotnet build src/ProductDB/ProductDB.sqlproj -c Release -o ./out
#       - name: Deploy to test SQL Server
#         run: sqlpackage /Action:Publish
#               /SourceFile:./out/ProductDB.dacpac
#               /TargetServerName:localhost /TargetDatabaseName:ProductDB
#               /TargetUser:sa /TargetPassword:TestP@ssw0rd!
#               /TargetTrustServerCertificate:true
#       - name: Install tSQLt and run tests
#         run: sqlcmd -S localhost -U sa -P TestP@ssw0rd!
#               -d ProductDB -Q "EXEC tSQLt.RunAll"

-- ============================================================
-- PART 4: Run and verify tests locally
-- ============================================================
-- In SSMS: connect to your local test database
-- Run: EXEC tSQLt.RunTestClass 'ProductTests'
-- Expected output:
-- [SUCCESS] ProductTests.[test usp_UpdateStock adds stock correctly]
-- [SUCCESS] ProductTests.[test usp_UpdateStock raises error for negative stock]
-- Test Case Summary: 2 test cases executed. 0 failed.""",
                            "explanation": "This exercise walks through the complete database DevOps workflow: schema in .sql files, tests in tSQLt, and automation in GitHub Actions. The key insight is that tests run in a disposable SQL Server container in CI — no persistent test database needed.",
                            "purpose": "Experience the complete SQL database CI/CD workflow from schema definition through automated testing to pipeline deployment.",
                            "breakdown": [
                                {"line": "EXEC tSQLt.ExpectException @ExpectedMessage", "meaning": "Tells tSQLt that the next statement SHOULD raise an error. If the error is not raised, the test FAILS. If the error matches, the test PASSES. Used to test error handling."},
                                {"line": "mcr.microsoft.com/mssql/server:2022-latest (GitHub Actions service)", "meaning": "A Docker container running SQL Server 2022 that starts with the job and is available at localhost:1433. Provides an isolated SQL Server for CI testing without needing a persistent server."}
                            ],
                            "ssms_steps": [
                                "Create the folder structure: Tables/, Stored Procedures/, Tests/",
                                "Create each .sql file with the content shown above",
                                "In VS Code SQL Database Projects: open the .sqlproj → Build to validate",
                                "Install tSQLt in your local test database",
                                "Publish the DACPAC to your local test database",
                                "Run the tSQLt test procedures in SSMS",
                                "Verify both tests show [SUCCESS]",
                                "Create the .github/workflows/productdb-cicd.yml file",
                                "Push to GitHub and check the Actions tab for the pipeline run"
                            ],
                            "exam_tip": "The exercise shows the complete database DevOps loop. For the exam, know: .sqlproj builds to DACPAC. SqlPackage.exe deploys DACPAC. tSQLt tests run after deployment. CI runs in Docker containers. Approval gates protect production."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "In the exercise, what does tSQLt.ExpectException do?",
                            "opts": ["A. Catches any exception and marks the test as skipped", "B. Asserts that the next statement raises a specific error — test fails if no error is raised", "C. Prevents exceptions from crashing the test runner", "D. Logs exception details to an audit table"],
                            "correct": "B",
                            "explain": "tSQLt.ExpectException tells the framework that the immediately following statement should throw an error. If the error is raised with the matching message, the test passes. If no error is raised (or a different error), the test fails."
                        },
                        {
                            "q": "What does using a Docker SQL Server container in GitHub Actions CI provide?",
                            "opts": ["A. A connection to the production SQL Server for testing", "B. An isolated, disposable SQL Server instance for each pipeline run", "C. A backup of the production database", "D. A way to test without deploying the DACPAC"],
                            "correct": "B",
                            "explain": "Docker containers in GitHub Actions provide a clean, isolated SQL Server instance that starts fresh for each pipeline run. Tests cannot affect each other or any persistent environment. The container is destroyed after the job completes."
                        },
                        {
                            "q": "Which SqlPackage action is used in the pipeline to deploy the DACPAC to the test SQL Server?",
                            "opts": ["A. /Action:Deploy", "B. /Action:Publish", "C. /Action:Script", "D. /Action:Import"],
                            "correct": "B",
                            "explain": "/Action:Publish deploys the DACPAC to the target database, creating objects that don't exist and altering objects that differ from the DACPAC schema. This is the primary deployment action for CI/CD pipelines."
                        },
                        {
                            "q": "In the exercise, the CI pipeline runs tests against a SQL Server container, not a production database. Why?",
                            "opts": ["A. Production databases don't support tSQLt", "B. To isolate tests from production data and avoid any risk of corrupting live data", "C. Pipeline jobs cannot connect to external databases", "D. tSQLt only works on SQL Server 2022 containers"],
                            "correct": "B",
                            "explain": "Running tests against a disposable container ensures complete isolation from production. Test data, schema changes, and any test failures have zero impact on real users or data. The container is thrown away after each run."
                        },
                        {
                            "q": "What is the correct order of steps in the CI pipeline for SQL database projects?",
                            "opts": ["A. Deploy → Test → Build", "B. Test → Build → Deploy", "C. Build → Deploy to test DB → Run tSQLt tests → Deploy to prod", "D. Deploy to prod → Run tests → Rollback if failed"],
                            "correct": "C",
                            "explain": "The correct CI/CD order is: (1) Build the SQL project to produce a DACPAC, (2) Deploy the DACPAC to a test database, (3) Run tSQLt tests against the test database, (4) If tests pass, deploy to staging/production. Never test after deploying to production."
                        }
                    ]
                },

                # ── Unit 9: Knowledge check ─────────────────────────────
                {
                    "id": "lp2-m7-u9",
                    "title": "Knowledge check",
                    "description": "Test your understanding of SQL database projects and CI/CD concepts.",
                    "estimated_time": 10,
                    "objectives": [
                        "Validate understanding of SQL projects, DACPAC, branching, schema drift, CI/CD, and tSQLt"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Module 7 CI/CD Key Concepts Review",
                            "body": "Quick review of CI/CD for SQL databases:<br><br><strong>SQL Project:</strong> .sqlproj + .sql files per object → dotnet build → DACPAC. Each file = one CREATE statement. No DROP statements in source files.<br><br><strong>Source Control:</strong> git init, feature branches, PRs, .gitignore excludes bin/ and obj/. Post-deployment scripts for reference data using MERGE (idempotent).<br><br><strong>Schema Drift:</strong> When production DB differs from SQL project. Detect with SqlPackage /Action:DeployReport. Fix by backporting to SQL project.<br><br><strong>CI/CD Pipeline:</strong> GitHub Actions or Azure DevOps YAML. Trigger on push to main and PRs. Build → Deploy to test → Run tSQLt → Deploy to staging → Approve → Deploy to prod. Secrets for connection strings. GitHub Environments for approval gates.<br><br><strong>tSQLt Testing:</strong> T-SQL unit tests. tSQLt.NewTestClass for schema. Procedure names start with 'test'. FakeTable for isolation. AssertEquals to validate. ExpectException for error testing. RunAll for CI."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What T-SQL statement should each .sql file in a SQL database project contain?",
                            "opts": ["A. DROP IF EXISTS then CREATE", "B. A single CREATE statement for one database object", "C. ALTER statements for schema migrations", "D. SELECT statements to query the object"],
                            "correct": "B",
                            "explain": "SQL project files contain CREATE statements only — one object per file. SqlPackage generates the ALTER or DROP statements automatically during deployment based on the diff between DACPAC and target database."
                        },
                        {
                            "q": "You discover that a column was added directly to the production database without going through the SQL project. What is this called?",
                            "opts": ["A. Database migration", "B. Schema drift", "C. Database divergence", "D. Unauthorized deployment"],
                            "correct": "B",
                            "explain": "Schema drift is when the actual deployed database schema differs from the schema in source control (the SQL project). It occurs when changes are made directly to databases outside the CI/CD pipeline."
                        },
                        {
                            "q": "Which command detects what changes a DACPAC deployment would make to a target database without executing them?",
                            "opts": ["A. SqlPackage.exe /Action:Preview", "B. SqlPackage.exe /Action:DeployReport", "C. SqlPackage.exe /Action:Compare", "D. dotnet build --dry-run"],
                            "correct": "B",
                            "explain": "SqlPackage /Action:DeployReport generates an XML report of all changes (CREATE, ALTER, DROP) that would be applied if you ran /Action:Publish. Use this to review changes before deploying."
                        },
                        {
                            "q": "In a tSQLt test, what happens to data inserted during the test after the test completes?",
                            "opts": ["A. It remains in the database for debugging purposes", "B. It is deleted by the tSQLt cleanup procedure", "C. It is automatically rolled back — no permanent data changes", "D. It is moved to a test archive table"],
                            "correct": "C",
                            "explain": "Every tSQLt test runs inside a transaction that is rolled back when the test completes (pass or fail). All data inserted, updated, or deleted during the test is automatically undone. The database is unchanged after test execution."
                        },
                        {
                            "q": "Which GitHub Actions feature allows you to require a named person to approve a production deployment?",
                            "opts": ["A. Branch protection rules", "B. GitHub Environments with required reviewers", "C. Repository rulesets", "D. CODEOWNERS file"],
                            "correct": "B",
                            "explain": "GitHub Environments (configured in repository Settings → Environments) support required reviewers. When a job references environment: production, it waits for an approved reviewer before running. This is the standard way to gate production deployments."
                        }
                    ]
                },

                # ── Unit 10: Summary ────────────────────────────────────
                {
                    "id": "lp2-m7-u10",
                    "title": "Summary",
                    "description": "Review the SQL database CI/CD topics covered in this module.",
                    "estimated_time": 5,
                    "objectives": [
                        "Recall the key concepts of SQL database projects, CI/CD, and testing"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Module 7 Summary — SQL CI/CD",
                            "body": "In this module you learned database DevOps with SQL projects:<br><br><ul><li><strong>SQL Database Projects</strong> — .sqlproj + .sql files per object. dotnet build produces DACPAC. Each file has one CREATE statement. Build validates all references.</li><li><strong>DACPAC Deployment</strong> — SqlPackage.exe /Action:Publish deploys schema changes. /Action:Script previews without executing. /Action:DeployReport shows planned changes.</li><li><strong>Source Control</strong> — git for all .sql and .sqlproj files. .gitignore for bin/ and obj/. Post-deployment scripts with MERGE for idempotent seed data. :r directive to include other SQL files.</li><li><strong>Branching</strong> — feature branches for each change. PRs for code review. Resolve conflicts by combining CREATE TABLE definitions. Build after resolving to validate.</li><li><strong>Schema Drift</strong> — when production differs from SQL project. Detect with DeployReport. Fix by backporting to SQL project — never suppress with flags permanently.</li><li><strong>CI/CD Pipelines</strong> — GitHub Actions (.github/workflows/*.yml) or Azure DevOps. Build → Deploy to test → Test → Staging → Approval → Production. Secrets for connection strings. Environments for approval gates.</li><li><strong>tSQLt Testing</strong> — T-SQL unit tests. NewTestClass creates schema. Procedures start with 'test'. FakeTable isolates. AssertEquals validates. ExpectException tests errors. RunAll for pipeline.</li></ul>"
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What tool builds a .sqlproj file and produces a DACPAC?",
                            "opts": ["A. SqlPackage.exe /Action:Build", "B. dotnet build <project>.sqlproj", "C. mssql-build --project <project>.sqlproj", "D. Visual Studio build menu only"],
                            "correct": "B",
                            "explain": "'dotnet build <project>.sqlproj' builds a SQL database project. It validates SQL syntax, checks cross-object references, and produces a DACPAC in the bin/ output folder. This command works cross-platform in CI/CD pipelines."
                        },
                        {
                            "q": "Why should the bin/ folder be in .gitignore for a SQL project?",
                            "opts": ["A. The bin/ folder contains sensitive connection strings", "B. The DACPAC in bin/ is a generated build artifact, not source code", "C. Git cannot handle binary files in bin/", "D. The .sqlproj file already tracks the bin/ contents"],
                            "correct": "B",
                            "explain": "bin/ contains the DACPAC — a generated artifact produced from the source .sql files. Generated files should never be committed to git. They are regenerated by the build process. Committing them causes noise in git history and potential merge conflicts on binary files."
                        },
                        {
                            "q": "Which tSQLt procedure isolates a test by replacing a table with an empty copy?",
                            "opts": ["A. tSQLt.SpyTable", "B. tSQLt.FakeTable", "C. tSQLt.MockTable", "D. tSQLt.IsolateTable"],
                            "correct": "B",
                            "explain": "tSQLt.FakeTable replaces the specified table with an empty copy within the test transaction, isolating the test from real data. The real table is automatically restored when the test transaction rolls back."
                        },
                        {
                            "q": "What is the purpose of a post-deployment script in a SQL project?",
                            "opts": ["A. To run schema validation checks after deployment", "B. To seed reference data, run after all schema objects are deployed", "C. To create the database if it does not exist", "D. To test stored procedures after deployment"],
                            "correct": "B",
                            "explain": "Post-deployment scripts run AFTER all schema objects (tables, views, procedures) are deployed. They are used for seeding reference/lookup data with idempotent MERGE statements, and any post-schema data migration logic."
                        },
                        {
                            "q": "What is the correct first step when schema drift is detected in production?",
                            "opts": ["A. Immediately re-deploy the DACPAC to overwrite production", "B. Add DropObjectsNotInSource=false to the pipeline permanently", "C. Investigate the drifted change, then backport it to the SQL project via a pull request", "D. Roll back production to the previous DACPAC version"],
                            "correct": "C",
                            "explain": "The correct response to drift is: understand what changed, determine if it was intentional, then add the change to the SQL project via a normal PR + review process. This brings source control back in sync with production. Never suppress drift permanently with deployment flags."
                        }
                    ]
                }
            ]
        },

        # ══════════════════════════════════════════════════════════════
        # MODULE lp2-m8: Integrate SQL solutions with Azure services
        # ══════════════════════════════════════════════════════════════
        {
            "id": "lp2-m8",
            "title": "Integrate SQL solutions with Azure services",
            "description": "Learn to expose SQL databases as REST and GraphQL APIs using Data API Builder, monitor with Azure Monitor, and implement event-driven patterns.",
            "units": [

                # ── Unit 1: Introduction ────────────────────────────────
                {
                    "id": "lp2-m8-u1",
                    "title": "Introduction",
                    "description": "Overview of integrating SQL databases with Azure services.",
                    "estimated_time": 5,
                    "objectives": [
                        "Understand how SQL databases integrate with Azure services",
                        "Preview Data API Builder, Azure Monitor, and event-driven patterns"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Azure Integration for SQL Databases",
                            "body": "Modern applications often need SQL data exposed in multiple ways: as a REST API for mobile apps, as GraphQL for flexible queries, with monitoring for operations, and as event streams for real-time processing.<br><br>In this module you will learn:<ul><li><strong>Data API Builder (DAB)</strong> — Microsoft's open-source tool that automatically generates REST and GraphQL endpoints from SQL tables, views, and stored procedures — zero custom code required</li><li><strong>Entities</strong> — how to map SQL objects to API resources in the DAB configuration</li><li><strong>REST endpoints</strong> — the auto-generated CRUD API with standard HTTP methods</li><li><strong>GraphQL</strong> — the auto-generated flexible query API for SQL objects</li><li><strong>Deployment options</strong> — hosting DAB on Azure Container Apps, App Service, or locally</li><li><strong>Azure Monitor</strong> — collecting SQL database metrics, logs, and setting up alerts</li><li><strong>Event-driven patterns</strong> — using Azure Event Grid, Service Bus, and Change Data Capture (CDC) to react to database changes</li></ul>"
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What is Data API Builder (DAB)?",
                            "opts": ["A. A tool for importing data into Azure SQL", "B. An open-source tool that auto-generates REST and GraphQL APIs from SQL database objects", "C. An Azure service for backing up SQL databases", "D. A performance tuning tool for SQL Server"],
                            "correct": "B",
                            "explain": "Data API Builder (DAB) reads a configuration file (dab-config.json) that maps SQL tables/views/procedures to API entities, then auto-generates REST (CRUD) and GraphQL endpoints. No custom API code needed."
                        },
                        {
                            "q": "What is Change Data Capture (CDC) in SQL Server?",
                            "opts": ["A. A feature that encrypts changes to tables", "B. A feature that captures INSERT, UPDATE, and DELETE changes to tables in a change table", "C. A replication feature for copying databases", "D. An auditing feature that logs all DDL changes"],
                            "correct": "B",
                            "explain": "Change Data Capture (CDC) records row-level changes (INSERT, UPDATE, DELETE) to selected tables in CDC change tables. Applications and services can read these change tables to react to data changes — the foundation of event-driven SQL patterns."
                        },
                        {
                            "q": "What does Azure Monitor provide for SQL databases?",
                            "opts": ["A. Automatic schema optimization", "B. Metrics, logs, alerts, and diagnostic data for SQL database health and performance", "C. Data masking for sensitive columns", "D. Backup management for SQL databases"],
                            "correct": "B",
                            "explain": "Azure Monitor collects SQL database telemetry: DTU/vCore usage, connection counts, query performance, deadlocks, and more. You can set alert rules to notify you when thresholds are exceeded and send logs to Log Analytics for querying."
                        },
                        {
                            "q": "Which HTTP method is used for a REST endpoint to retrieve data in Data API Builder?",
                            "opts": ["A. PUT", "B. POST", "C. GET", "D. PATCH"],
                            "correct": "C",
                            "explain": "In REST conventions, GET retrieves data. Data API Builder maps: GET = SELECT (read), POST = INSERT (create), PUT/PATCH = UPDATE (modify), DELETE = DELETE. GET /api/Customer returns all customers."
                        },
                        {
                            "q": "Which Azure messaging service enables decoupled, asynchronous processing of SQL database change events?",
                            "opts": ["A. Azure SQL Sync", "B. Azure Service Bus", "C. Azure SQL Managed Instance", "D. Azure Data Factory"],
                            "correct": "B",
                            "explain": "Azure Service Bus is a message queue service. SQL change events (captured via CDC or triggers) can be published to Service Bus queues or topics. Consumers (like Azure Functions) read messages asynchronously and process them independently of the database."
                        }
                    ]
                },

                # ── Unit 2: Data API Builder configuration files ─────────
                {
                    "id": "lp2-m8-u2",
                    "title": "Data API Builder configuration files",
                    "description": "Create and configure the dab-config.json file that drives Data API Builder.",
                    "estimated_time": 25,
                    "objectives": [
                        "Understand the dab-config.json structure",
                        "Initialize a DAB configuration using the dab CLI",
                        "Configure the data source connection"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "dab-config.json Structure",
                            "body": "Data API Builder is driven entirely by a JSON configuration file (dab-config.json). There is no code to write — just configure the JSON and run <code>dab start</code>.<br><br><strong>Top-level sections of dab-config.json:</strong><ul><li><strong>$schema</strong> — points to the JSON schema for IntelliSense in VS Code</li><li><strong>data-source</strong> — database type and connection string</li><li><strong>runtime</strong> — REST path, GraphQL path, authentication, CORS, host mode</li><li><strong>entities</strong> — the SQL objects (tables, views, stored procedures) to expose as API endpoints</li></ul><strong>dab CLI commands:</strong><ul><li><code>dab init</code> — creates initial config file</li><li><code>dab add</code> — adds a new entity to the config</li><li><code>dab start</code> — starts the local API server</li><li><code>dab validate</code> — validates the config without starting</li></ul>Install dab CLI: <code>dotnet tool install -g microsoft.dataapibuilder</code>"
                        },
                        {
                            "type": "sql_block",
                            "title": "Create and Configure dab-config.json",
                            "scenario": "You have an Azure SQL Database with Customers and Orders tables. Create a Data API Builder configuration to expose both tables as REST and GraphQL endpoints.",
                            "code": """-- ============================================================
-- TERMINAL COMMANDS (PowerShell / bash)
-- Install and initialize DAB
-- ============================================================

# Install the dab CLI tool
# dotnet tool install -g microsoft.dataapibuilder

# Initialize a new dab-config.json
# dab init --database-type mssql \\
#   --connection-string "Server=myserver.database.windows.net;Database=SalesDB;Authentication=Active Directory Default;" \\
#   --host-mode Development

# Add the Customers entity (maps to dbo.Customers table)
# dab add Customer \\
#   --source "dbo.Customers" \\
#   --permissions "anonymous:read" \\
#   --rest.path "/Customer"

# Add the Orders entity
# dab add Order \\
#   --source "dbo.Orders" \\
#   --permissions "authenticated:*" \\
#   --rest.path "/Order"

# Start the local API server
# dab start

# ============================================================
# RESULT: dab-config.json (created by the commands above)
# ============================================================

{
  "$schema": "https://dataapibuilder.azureedge.net/schemas/v1.3.0/dab.draft.schema.json",
  "data-source": {
    "database-type": "mssql",
    "connection-string": "@env('DATABASE_CONNECTION_STRING')"
  },
  "runtime": {
    "rest": {
      "enabled": true,
      "path": "/api"
    },
    "graphql": {
      "enabled": true,
      "path": "/graphql",
      "allow-introspection": true
    },
    "host": {
      "mode": "development",
      "cors": {
        "origins": ["http://localhost:3000"],
        "allow-credentials": true
      },
      "authentication": {
        "provider": "StaticWebApps"
      }
    }
  },
  "entities": {
    "Customer": {
      "source": {
        "object": "dbo.Customers",
        "type": "table"
      },
      "permissions": [
        {
          "role": "anonymous",
          "actions": ["read"]
        }
      ],
      "rest": {
        "enabled": true,
        "path": "/Customer"
      },
      "graphql": {
        "enabled": true,
        "type": {
          "singular": "Customer",
          "plural": "Customers"
        }
      },
      "mappings": {
        "CustomerID": "id",
        "FirstName": "firstName",
        "LastName": "lastName",
        "Email": "email"
      }
    },
    "Order": {
      "source": {
        "object": "dbo.Orders",
        "type": "table"
      },
      "permissions": [
        {
          "role": "authenticated",
          "actions": ["create", "read", "update", "delete"]
        }
      ],
      "relationships": {
        "customer": {
          "target.entity": "Customer",
          "cardinality": "one"
        }
      }
    }
  }
}""",
                            "explanation": "The dab-config.json maps SQL objects to API entities. The 'mappings' section renames database columns to API-friendly camelCase names. 'relationships' enables automatic JOINs in GraphQL queries. The connection string uses @env() to reference an environment variable.",
                            "purpose": "Configure Data API Builder to expose SQL tables as REST and GraphQL endpoints without writing any custom API code.",
                            "breakdown": [
                                {"line": "\"database-type\": \"mssql\"", "meaning": "Tells DAB to use the SQL Server / Azure SQL driver. Other options: postgresql, mysql, cosmosdb_nosql. DAB supports multiple database types."},
                                {"line": "\"connection-string\": \"@env('DATABASE_CONNECTION_STRING')\"", "meaning": "References an environment variable for the connection string. Never hardcode credentials. Set the env variable in your shell or Azure App Service configuration."},
                                {"line": "\"mode\": \"development\"", "meaning": "Development mode shows detailed error messages and enables Swagger UI at /swagger. Use 'production' mode for deployed APIs."},
                                {"line": "\"source\": { \"object\": \"dbo.Customers\", \"type\": \"table\" }", "meaning": "Maps this entity to the dbo.Customers SQL table. type can be 'table', 'view', or 'stored-procedure'."},
                                {"line": "\"permissions\": [{ \"role\": \"anonymous\", \"actions\": [\"read\"] }]", "meaning": "Controls who can do what. 'anonymous' = unauthenticated users. 'authenticated' = any user with a valid token. Actions: create/read/update/delete. Use specific role names for Azure AD roles."},
                                {"line": "\"mappings\": { \"CustomerID\": \"id\" }", "meaning": "Renames the column in the API response. The database has 'CustomerID' but the API exposes it as 'id'. Makes the API more RESTful and decouples the schema from the API contract."},
                                {"line": "\"relationships\": { \"customer\": { \"target.entity\": \"Customer\", \"cardinality\": \"one\" } }", "meaning": "Defines a relationship between Order and Customer. DAB uses this to enable nested GraphQL queries like: query { orders { id customer { firstName } } } — automatically generating the JOIN."}
                            ],
                            "ssms_steps": [
                                "Install dab CLI: open terminal and run dotnet tool install -g microsoft.dataapibuilder",
                                "Create a folder for your project: mkdir my-api && cd my-api",
                                "Run: dab init --database-type mssql --connection-string '<your connection string>' --host-mode Development",
                                "Run: dab add Customer --source 'dbo.Customers' --permissions 'anonymous:read'",
                                "Open dab-config.json in VS Code to see the generated config",
                                "Add mappings and relationships manually in the JSON",
                                "Set the environment variable: $env:DATABASE_CONNECTION_STRING = '<connection string>'",
                                "Run: dab start — API starts at http://localhost:5000",
                                "Open browser: http://localhost:5000/api/Customer to see your data"
                            ],
                            "exam_tip": "The dab-config.json structure: data-source (database connection) + runtime (API settings + auth) + entities (SQL object mappings). Entity source type can be 'table', 'view', or 'stored-procedure'. Permissions control anonymous vs authenticated access and CRUD actions."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "Which dab CLI command initializes a new dab-config.json file?",
                            "opts": ["A. dab create", "B. dab init", "C. dab configure", "D. dab new"],
                            "correct": "B",
                            "explain": "'dab init' creates the initial dab-config.json file with the data-source section configured. You then use 'dab add' to add entities, and 'dab start' to run the API server."
                        },
                        {
                            "q": "What does the 'mappings' section in a DAB entity configuration do?",
                            "opts": ["A. Maps the entity to an Azure AD role", "B. Renames database column names to API-friendly field names", "C. Defines the JOIN condition between related tables", "D. Maps REST methods to SQL commands"],
                            "correct": "B",
                            "explain": "The mappings section allows you to rename columns in the API response. For example, 'CustomerID' (database column) can be exposed as 'id' in the REST/GraphQL API. This decouples your API contract from your database schema."
                        },
                        {
                            "q": "In dab-config.json, what does source type 'stored-procedure' indicate?",
                            "opts": ["A. The entity is backed by a stored procedure instead of a direct table", "B. The entity uses a stored procedure to validate permissions", "C. A stored procedure creates the entity's table automatically", "D. The entity is read-only because stored procedures cannot be updated"],
                            "correct": "A",
                            "explain": "When source type is 'stored-procedure', DAB calls the stored procedure to handle the API request instead of querying the table directly. The stored procedure's parameters map to API query parameters or request body fields."
                        },
                        {
                            "q": "What is the purpose of the 'relationships' section in a DAB entity?",
                            "opts": ["A. Defines foreign key constraints in the database", "B. Enables nested object queries in GraphQL by describing how entities are related", "C. Controls which users can see relationships between entities", "D. Sets up replication between tables"],
                            "correct": "B",
                            "explain": "The relationships section tells DAB how entities are connected (one-to-many, many-to-one). This enables GraphQL queries that traverse relationships, like querying an order and its customer in one request. DAB generates the appropriate SQL JOIN."
                        },
                        {
                            "q": "Which dab CLI command adds a new entity to an existing dab-config.json?",
                            "opts": ["A. dab update", "B. dab entity add", "C. dab add", "D. dab append"],
                            "correct": "C",
                            "explain": "'dab add <EntityName>' adds a new entity definition to the existing dab-config.json. Specify the source SQL object with --source and permissions with --permissions. DAB updates the JSON file automatically."
                        }
                    ]
                },

                # ── Unit 3: Entities for REST and GraphQL ───────────────
                {
                    "id": "lp2-m8-u3",
                    "title": "Entities for REST and GraphQL",
                    "description": "Configure entities in Data API Builder and understand the auto-generated REST and GraphQL API.",
                    "estimated_time": 25,
                    "objectives": [
                        "Test the auto-generated REST endpoints",
                        "Write GraphQL queries against DAB",
                        "Configure field-level permissions on entities"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "REST and GraphQL in Data API Builder",
                            "body": "Once configured, DAB provides two API styles simultaneously from the same configuration:<br><br><strong>REST API:</strong><ul><li>GET /api/Customer — list all customers</li><li>GET /api/Customer/id/5 — get customer with id=5</li><li>POST /api/Customer — create a new customer (JSON body)</li><li>PUT /api/Customer/id/5 — replace customer 5 (all fields)</li><li>PATCH /api/Customer/id/5 — update customer 5 (partial update)</li><li>DELETE /api/Customer/id/5 — delete customer 5</li></ul><strong>GraphQL API:</strong><ul><li>All queries go to POST /graphql</li><li>Query: <code>{ customers { id firstName lastName } }</code></li><li>Filter: <code>{ customers(filter: { lastName: { eq: 'Smith' } }) { id } }</code></li><li>Pagination: <code>{ customers(first: 10, after: 'cursor') { items { id } hasNextPage } }</code></li><li>Mutation: <code>mutation { createCustomer(item: { firstName: 'Alice' }) { id } }</code></li></ul><strong>Filtering REST with OData:</strong> GET /api/Order?$filter=TotalAmount gt 100&$orderby=OrderDate desc&$top=20"
                        },
                        {
                            "type": "sql_block",
                            "title": "Test REST and GraphQL Endpoints",
                            "scenario": "With DAB running locally, test the Customer and Order endpoints using curl commands and GraphQL queries.",
                            "code": """-- ============================================================
-- REST API EXAMPLES (use curl, Postman, or browser)
-- ============================================================

# GET all customers
# curl http://localhost:5000/api/Customer

# Response:
# {
#   "value": [
#     { "id": 1, "firstName": "Alice", "lastName": "Smith", "email": "alice@example.com" },
#     { "id": 2, "firstName": "Bob", "lastName": "Jones", "email": "bob@example.com" }
#   ]
# }

# GET a specific customer by primary key
# curl http://localhost:5000/api/Customer/id/1

# POST to create a new customer
# curl -X POST http://localhost:5000/api/Customer \\
#   -H "Content-Type: application/json" \\
#   -d '{"firstName": "Carol", "lastName": "Taylor", "email": "carol@example.com"}'

# PATCH to update a field
# curl -X PATCH http://localhost:5000/api/Customer/id/1 \\
#   -H "Content-Type: application/json" \\
#   -d '{"email": "alice.new@example.com"}'

# DELETE a customer
# curl -X DELETE http://localhost:5000/api/Customer/id/3

# OData filtering: get orders over $100 ordered by date
# curl "http://localhost:5000/api/Order?\\$filter=totalAmount gt 100&\\$orderby=orderDate desc&\\$top=5"

-- ============================================================
-- GraphQL EXAMPLES (POST to /graphql)
-- ============================================================

# Query 1: Get all customers with selected fields
# curl -X POST http://localhost:5000/graphql \\
#   -H "Content-Type: application/json" \\
#   -d '{
#     "query": "{ customers { items { id firstName lastName email } } }"
#   }'

# Query 2: Filter customers by last name
# {
#   customers(filter: { lastName: { eq: \"Smith\" } }) {
#     items {
#       id
#       firstName
#       email
#     }
#   }
# }

# Query 3: Get orders with nested customer (uses relationship)
# {
#   orders(filter: { totalAmount: { gt: 100 } }, first: 5) {
#     items {
#       id
#       totalAmount
#       orderDate
#       customer {
#         firstName
#         lastName
#       }
#     }
#     hasNextPage
#     endCursor
#   }
# }

# Mutation: Create a new customer
# mutation {
#   createCustomer(item: {
#     firstName: "Dave"
#     lastName: "Brown"
#     email: "dave@example.com"
#   }) {
#     id
#     firstName
#   }
# }

-- ============================================================
-- Entity with field-level permissions (dab-config.json)
-- ============================================================
-- "Customer": {
--   "permissions": [
--     {
--       "role": "authenticated",
--       "actions": [
--         {
--           "action": "read",
--           "fields": {
--             "include": ["id", "firstName", "lastName"],
--             "exclude": ["email"]    <- authenticated users cannot see email
--           }
--         },
--         {
--           "action": "update",
--           "fields": {
--             "include": ["email"]    <- users can only update their own email
--           }
--         }
--       ]
--     }
--   ]
-- }""",
                            "explanation": "DAB generates REST endpoints following HTTP conventions and GraphQL with full filter, sort, and pagination support. Field-level permissions let you control which columns are exposed or modifiable per role. Relationships in config enable JOINs in GraphQL automatically.",
                            "purpose": "Expose SQL database data as both REST and GraphQL APIs from a single configuration without writing any custom API code.",
                            "breakdown": [
                                {"line": "GET /api/Customer?$filter=...&$orderby=...&$top=...", "meaning": "DAB REST endpoints support OData query parameters: $filter for WHERE conditions, $orderby for ORDER BY, $top for LIMIT, $skip for OFFSET. The syntax is OData standard."},
                                {"line": "customers(filter: { lastName: { eq: 'Smith' } })", "meaning": "GraphQL filter syntax in DAB. Operators: eq, neq, gt, gte, lt, lte, contains, startsWith, endsWith. Multiple conditions can be combined with and/or."},
                                {"line": "hasNextPage / endCursor", "meaning": "DAB implements cursor-based pagination for GraphQL. first: 5 limits results. hasNextPage tells you if more results exist. Pass endCursor as 'after' in the next query to get the next page."},
                                {"line": "\"fields\": { \"include\": [...], \"exclude\": [...] }", "meaning": "Field-level permissions restrict which columns a role can see (include) or which are hidden (exclude) from API responses. A role gets the 'include' set minus the 'exclude' set."}
                            ],
                            "ssms_steps": [
                                "Start DAB: in terminal, run 'dab start' — API runs at http://localhost:5000",
                                "Open a browser and go to http://localhost:5000/swagger for the Swagger UI (development mode only)",
                                "Try GET /api/Customer — you should see your customers in JSON",
                                "For GraphQL: go to http://localhost:5000/graphql to open the GraphQL IDE",
                                "Type a query in the left panel and click the play button",
                                "Try the nested customer query to see relationships in action",
                                "For POST/PATCH/DELETE: use Postman, Insomnia, or the VS Code REST Client extension",
                                "Check the terminal where dab start is running to see SQL queries being generated"
                            ],
                            "exam_tip": "REST in DAB uses OData query parameters ($filter, $orderby, $top, $skip). GraphQL uses typed filter arguments. Both read from the same SQL database via the entity configuration. Relationships in config = automatic JOINs in GraphQL. No custom code needed."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What HTTP method does Data API Builder use to create a new entity record?",
                            "opts": ["A. GET", "B. PUT", "C. POST", "D. PATCH"],
                            "correct": "C",
                            "explain": "POST /api/EntityName creates a new record (INSERT). PUT replaces a complete record. PATCH updates specific fields. DELETE removes a record. GET retrieves records. This follows standard REST HTTP method conventions."
                        },
                        {
                            "q": "Which OData query parameter filters REST results in Data API Builder?",
                            "opts": ["A. $where", "B. $filter", "C. $condition", "D. $search"],
                            "correct": "B",
                            "explain": "DAB REST endpoints support OData query parameters: $filter for WHERE conditions (e.g., $filter=totalAmount gt 100), $orderby for sorting, $top for limiting results, $select for choosing columns."
                        },
                        {
                            "q": "In DAB's GraphQL, what does 'first: 10' accomplish in a query?",
                            "opts": ["A. Returns the first record in alphabetical order", "B. Limits the query results to 10 items (pagination)", "C. Returns only the first 10 columns of each row", "D. Caches the first 10 results for performance"],
                            "correct": "B",
                            "explain": "In DAB's GraphQL, 'first: N' implements cursor-based pagination by limiting results to N items. Combined with 'after: cursor' from the previous page's endCursor, you can paginate through large result sets."
                        },
                        {
                            "q": "What does the 'exclude' field list in entity permissions do?",
                            "opts": ["A. Excludes the entity from GraphQL queries", "B. Hides specific columns from the API response for that role", "C. Prevents the listed fields from being indexed", "D. Excludes the entity from audit logging"],
                            "correct": "B",
                            "explain": "Field-level permissions with 'exclude' hide specific database columns from the API response for users with that role. For example, excluding 'salary' from the 'authenticated' role prevents regular users from seeing salary data through the API."
                        },
                        {
                            "q": "How does a GraphQL relationship query in DAB differ from writing a JOIN in T-SQL?",
                            "opts": ["A. GraphQL relationships are faster because they use indexes automatically", "B. DAB generates the JOIN automatically based on the relationship defined in config — no SQL needed", "C. GraphQL uses OUTER JOINs while T-SQL uses INNER JOINs by default", "D. GraphQL relationships require a stored procedure to execute the JOIN"],
                            "correct": "B",
                            "explain": "When you define a relationship in dab-config.json (e.g., Order.customer → Customer), DAB automatically generates the SQL JOIN when a GraphQL query traverses the relationship. You never write T-SQL JOIN syntax — the config drives it."
                        }
                    ]
                },

                # ── Unit 4: Expose stored procedures and views ──────────
                {
                    "id": "lp2-m8-u4",
                    "title": "Expose database objects, stored procedures, and views",
                    "description": "Configure Data API Builder to expose views and stored procedures as API endpoints.",
                    "estimated_time": 20,
                    "objectives": [
                        "Map a SQL view to a DAB entity",
                        "Map a stored procedure to an API endpoint in DAB",
                        "Understand the difference between table, view, and stored-procedure source types"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Views and Stored Procedures as DAB Entities",
                            "body": "Tables are not the only SQL objects DAB can expose:<br><br><strong>Views:</strong><ul><li>Views can be exposed as read-only entities (unless they are updatable views)</li><li>Useful for exposing JOIN results, calculated columns, or filtered subsets</li><li>Configure with <code>\"type\": \"view\"</code> in the source section</li></ul><strong>Stored Procedures:</strong><ul><li>Expose custom business logic as API endpoints</li><li>Parameters map to request body fields (POST) or query string (GET)</li><li>Configure with <code>\"type\": \"stored-procedure\"</code></li><li>Only support one HTTP method (typically POST)</li><li>Cannot be used in GraphQL mutations (read-only SP support only in GraphQL)</li></ul><strong>When to use each:</strong><ul><li>Simple table CRUD → table entity</li><li>Read-only aggregate/join data → view entity</li><li>Complex business logic → stored procedure entity</li></ul>"
                        },
                        {
                            "type": "sql_block",
                            "title": "Configure Views and Stored Procedures in DAB",
                            "scenario": "Expose the vw_OrderSummary view and the usp_GetCustomerOrders stored procedure as API endpoints.",
                            "code": """-- ============================================================
-- SQL objects to expose (already created in the database)
-- ============================================================

-- VIEW: returns pre-joined summary data
CREATE VIEW [dbo].[vw_OrderSummary] AS
SELECT
    c.CustomerID,
    c.FirstName + ' ' + c.LastName AS CustomerName,
    COUNT(o.OrderID) AS TotalOrders,
    SUM(o.TotalAmount) AS TotalRevenue
FROM dbo.Customers c
LEFT JOIN dbo.Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerID, c.FirstName, c.LastName;
GO

-- STORED PROCEDURE: returns filtered orders for a customer
CREATE PROCEDURE [dbo].[usp_GetCustomerOrders]
    @CustomerID INT,
    @StartDate  DATE = NULL
AS
BEGIN
    SELECT OrderID, OrderDate, TotalAmount, Status
    FROM dbo.Orders
    WHERE CustomerID = @CustomerID
      AND (@StartDate IS NULL OR OrderDate >= @StartDate)
    ORDER BY OrderDate DESC;
END;
GO

-- ============================================================
-- dab-config.json entity configuration for view and SP
-- ============================================================

{
  "entities": {
    "OrderSummary": {
      "source": {
        "object": "dbo.vw_OrderSummary",
        "type": "view",
        "key-fields": ["CustomerID"]
      },
      "permissions": [
        {
          "role": "authenticated",
          "actions": ["read"]
        }
      ],
      "rest": {
        "enabled": true,
        "path": "/OrderSummary",
        "methods": ["GET"]
      },
      "graphql": {
        "enabled": true,
        "type": { "singular": "OrderSummary", "plural": "OrderSummaries" }
      }
    },
    "CustomerOrders": {
      "source": {
        "object": "dbo.usp_GetCustomerOrders",
        "type": "stored-procedure",
        "parameters": {
          "CustomerID": {
            "type": "integer",
            "hasDefault": false
          },
          "StartDate": {
            "type": "string",
            "hasDefault": true
          }
        }
      },
      "permissions": [
        {
          "role": "authenticated",
          "actions": ["execute"]
        }
      ],
      "rest": {
        "enabled": true,
        "path": "/CustomerOrders",
        "methods": ["GET"]
      },
      "graphql": {
        "enabled": false
      }
    }
  }
}

-- ============================================================
-- API USAGE
-- ============================================================

# View: GET all order summaries
# curl http://localhost:5000/api/OrderSummary

# View: GET filtered summary (CustomerID >= 5)
# curl "http://localhost:5000/api/OrderSummary?\\$filter=CustomerID eq 5"

# Stored Procedure: GET customer 3's orders since Jan 2024
# curl "http://localhost:5000/api/CustomerOrders?CustomerID=3&StartDate=2024-01-01"

# The SP parameters become query string parameters for GET requests""",
                            "explanation": "Views are exposed read-only by default. The 'key-fields' property is required for views that don't have a defined primary key. Stored procedures use 'parameters' to define what arguments they accept, which map to query string parameters in REST GET requests.",
                            "purpose": "Expose pre-joined views and business logic stored procedures as clean API endpoints without rewriting the SQL in application code.",
                            "breakdown": [
                                {"line": "\"type\": \"view\", \"key-fields\": [\"CustomerID\"]", "meaning": "Tells DAB this entity is backed by a view. key-fields specifies the column(s) that uniquely identify a row in the view (since views don't have PRIMARY KEY constraints)."},
                                {"line": "\"type\": \"stored-procedure\"", "meaning": "This entity is backed by a stored procedure. When the API endpoint is called, DAB executes the stored procedure with the provided parameters."},
                                {"line": "\"parameters\": { \"CustomerID\": { \"type\": \"integer\", \"hasDefault\": false } }", "meaning": "Defines the stored procedure parameters that are exposed in the API. hasDefault: false means this parameter is required — the API returns an error if it is not provided."},
                                {"line": "\"actions\": [\"execute\"]", "meaning": "For stored procedure entities, the permission action is 'execute' instead of 'read'/'create'/'update'/'delete'. This grants permission to call the stored procedure endpoint."},
                                {"line": "\"methods\": [\"GET\"]", "meaning": "For stored procedures, specifies which HTTP methods are allowed. GET maps parameters to query string. POST maps parameters to request body. Most read-only SPs use GET."}
                            ],
                            "ssms_steps": [
                                "Make sure the view and stored procedure exist in your SQL database (run the CREATE statements in SSMS)",
                                "Edit your dab-config.json to add the OrderSummary and CustomerOrders entities as shown",
                                "Run: dab validate to check the config syntax",
                                "Run: dab start to start the API",
                                "Test the view: open browser at http://localhost:5000/api/OrderSummary",
                                "Test the SP: http://localhost:5000/api/CustomerOrders?CustomerID=1",
                                "Check the DAB console output to see the SQL being executed for each API call"
                            ],
                            "exam_tip": "Key exam facts: Views → type: 'view', need key-fields if no PK. Stored procedures → type: 'stored-procedure', parameters mapped from query string (GET) or body (POST), permission action = 'execute'. SPs are generally not available in GraphQL mutations (read-only GraphQL support varies by version)."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "Why is the 'key-fields' property required when exposing a view in Data API Builder?",
                            "opts": ["A. Views require explicit permission to be accessed", "B. Views don't have primary key constraints, so key-fields identifies the unique row identifier", "C. key-fields specifies which columns to include in the API response", "D. Views require a key-fields property to enable GraphQL support"],
                            "correct": "B",
                            "explain": "SQL views don't have PRIMARY KEY constraints. DAB needs to know which column(s) uniquely identify a row in the view to support single-record lookups (GET /api/EntityName/id/5). key-fields provides this information."
                        },
                        {
                            "q": "For a stored procedure entity in DAB, what permission action value grants the right to call the endpoint?",
                            "opts": ["A. read", "B. call", "C. execute", "D. invoke"],
                            "correct": "C",
                            "explain": "For stored-procedure entities, the permission action is 'execute'. This is different from table/view entities which use 'read', 'create', 'update', 'delete'. Execute grants the right to call the stored procedure through the API."
                        },
                        {
                            "q": "When a stored procedure entity uses 'methods': ['GET'] in DAB, how are parameters passed to the API?",
                            "opts": ["A. In the HTTP request body as JSON", "B. As URL path segments (e.g., /api/CustomerOrders/3)", "C. As query string parameters (e.g., ?CustomerID=3)", "D. In HTTP headers"],
                            "correct": "C",
                            "explain": "For GET method stored procedure endpoints, parameters are passed as query string parameters: /api/CustomerOrders?CustomerID=3&StartDate=2024-01-01. For POST method, parameters come from the request body."
                        },
                        {
                            "q": "Which DAB source type would you use for a SQL query that JOINs multiple tables and has no primary key?",
                            "opts": ["A. table", "B. stored-procedure", "C. view", "D. function"],
                            "correct": "C",
                            "explain": "A SQL view encapsulates JOIN logic and complex queries. Expose it in DAB as type: 'view'. Since views have no primary key, specify key-fields to identify which column uniquely identifies rows in the result set."
                        },
                        {
                            "q": "A stored procedure entity is configured with 'hasDefault: false' for a parameter. What happens if a caller omits that parameter?",
                            "opts": ["A. The parameter defaults to NULL", "B. DAB returns a 400 Bad Request error — the parameter is required", "C. DAB skips executing the stored procedure", "D. The stored procedure uses the database default value"],
                            "correct": "B",
                            "explain": "'hasDefault: false' marks the parameter as required. If a caller does not provide it, DAB returns a 400 Bad Request error before calling the stored procedure. This provides client-side validation at the API layer."
                        }
                    ]
                },

                # ── Unit 5: Deployment options for Data API Builder ─────
                {
                    "id": "lp2-m8-u5",
                    "title": "Deployment options for Data API Builder",
                    "description": "Deploy Data API Builder to Azure Container Apps, Azure App Service, or as a Docker container.",
                    "estimated_time": 20,
                    "objectives": [
                        "Understand DAB deployment options",
                        "Deploy DAB to Azure Container Apps",
                        "Configure environment variables for production deployment"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Where to Deploy Data API Builder",
                            "body": "Data API Builder is a self-hosted process (not a managed Azure service). You choose where to run it:<br><br><table border='1'><tr><th>Option</th><th>Best For</th><th>Pros</th><th>Cons</th></tr><tr><td>Azure Container Apps</td><td>Production APIs</td><td>Auto-scaling, HTTPS, managed, serverless</td><td>More configuration</td></tr><tr><td>Azure App Service</td><td>Simple deployments</td><td>Easy deployment, built-in HTTPS</td><td>Always-on cost even when idle</td></tr><tr><td>Docker locally</td><td>Development/testing</td><td>Fast iteration, no Azure cost</td><td>Not production-ready</td></tr><tr><td>Azure Static Web Apps</td><td>Frontend + API combined</td><td>Integrated with DAB, free tier</td><td>Limited to SWA apps</td></tr></table><br><strong>Key deployment considerations:</strong><ul><li>Always use HTTPS in production</li><li>Store connection strings as environment variables or Azure Key Vault references — never in the config file</li><li>Set <code>\"mode\": \"production\"</code> in the config to disable debug information</li><li>Use Managed Identity for database authentication (no passwords in config)</li></ul>"
                        },
                        {
                            "type": "sql_block",
                            "title": "Deploy DAB to Azure Container Apps",
                            "scenario": "Deploy your SalesDB Data API Builder to Azure Container Apps with HTTPS and Managed Identity authentication to Azure SQL.",
                            "code": """# ============================================================
# Deploy Data API Builder to Azure Container Apps
# Run in Azure CLI / Azure Cloud Shell
# ============================================================

# Step 1: Create resource group
az group create \\
  --name rg-salesapi \\
  --location eastus

# Step 2: Create Azure Container Apps environment
az containerapp env create \\
  --name cae-salesapi \\
  --resource-group rg-salesapi \\
  --location eastus

# Step 3: Deploy DAB as a Container App
# Using the official DAB Docker image from MCR
az containerapp create \\
  --name ca-salesapi \\
  --resource-group rg-salesapi \\
  --environment cae-salesapi \\
  --image mcr.microsoft.com/azure-databases/data-api-builder:latest \\
  --target-port 5000 \\
  --ingress external \\
  --min-replicas 1 \\
  --max-replicas 5 \\
  --env-vars \\
    DATABASE_CONNECTION_STRING=secretref:db-connection \\
    ASPNETCORE_ENVIRONMENT=Production \\
  --secrets \\
    db-connection="Server=myserver.database.windows.net;Database=SalesDB;Authentication=Active Directory Managed Identity;" \\
  --cpu 0.5 \\
  --memory 1Gi

# Step 4: Enable system-assigned Managed Identity on the Container App
az containerapp identity assign \\
  --name ca-salesapi \\
  --resource-group rg-salesapi \\
  --system-assigned

# Step 5: Grant the Container App's identity access to Azure SQL
# (Copy the principalId from step 4 output)
# In Azure SQL: CREATE USER [ca-salesapi] FROM EXTERNAL PROVIDER;
#               ALTER ROLE db_datareader ADD MEMBER [ca-salesapi];
#               ALTER ROLE db_datawriter ADD MEMBER [ca-salesapi];

# Step 6: Mount the dab-config.json as a volume or include in the image
# Option A: Build a custom Docker image with your config:
# dockerfile:
# FROM mcr.microsoft.com/azure-databases/data-api-builder:latest
# COPY dab-config.json /App/

# docker build -t myregistry.azurecr.io/salesapi:v1 .
# docker push myregistry.azurecr.io/salesapi:v1

# Step 7: Get the public HTTPS URL
az containerapp show \\
  --name ca-salesapi \\
  --resource-group rg-salesapi \\
  --query properties.configuration.ingress.fqdn \\
  --output tsv
# Output: ca-salesapi.gentleocean-xyz.eastus.azurecontainerapps.io

# Your API is now at:
# https://ca-salesapi.gentleocean-xyz.eastus.azurecontainerapps.io/api/Customer""",
                            "explanation": "Azure Container Apps provides automatic HTTPS, scaling, and managed identity integration. The connection string uses 'Authentication=Active Directory Managed Identity' which uses the Container App's Managed Identity to authenticate — no password needed.",
                            "purpose": "Deploy Data API Builder to a scalable, managed Azure service with HTTPS and secure authentication to Azure SQL Database.",
                            "breakdown": [
                                {"line": "mcr.microsoft.com/azure-databases/data-api-builder:latest", "meaning": "The official Microsoft Container Registry (MCR) image for Data API Builder. Use a specific version tag (e.g., :1.3.0) instead of :latest for production to ensure reproducibility."},
                                {"line": "--ingress external", "meaning": "Makes the Container App accessible from the internet with an auto-generated HTTPS URL. 'internal' would make it only accessible within the Container Apps environment."},
                                {"line": "--min-replicas 1 --max-replicas 5", "meaning": "Auto-scaling configuration. The app scales from 1 to 5 replicas based on HTTP request load. At 0 replicas, it would scale to zero when idle (cold start)."},
                                {"line": "Authentication=Active Directory Managed Identity", "meaning": "Tells the SQL connection driver to use the Container App's Managed Identity to get an Azure AD token for SQL authentication. No username or password in the connection string."},
                                {"line": "secretref:db-connection", "meaning": "References a Container Apps secret (db-connection) as the value of the environment variable. Secrets are stored encrypted and not visible in config or logs."}
                            ],
                            "ssms_steps": [
                                "This is Azure CLI work — open Azure Cloud Shell (shell.azure.com) or install Azure CLI locally",
                                "Run: az login to authenticate with Azure",
                                "Run the az group create and az containerapp env create commands",
                                "Build your custom Docker image with the dab-config.json included",
                                "Push to Azure Container Registry: az acr login --name myregistry && docker push",
                                "Run az containerapp create with the custom image",
                                "Enable Managed Identity with az containerapp identity assign",
                                "In SSMS: connect to Azure SQL and run CREATE USER ... FROM EXTERNAL PROVIDER for the Container App identity",
                                "Test the deployed API at the FQDN returned by az containerapp show"
                            ],
                            "exam_tip": "For the exam: Azure Container Apps is the preferred deployment target for DAB (scalable, HTTPS, Managed Identity). Key config for production: mode = 'production', connection string uses Managed Identity (no passwords), environment variables via secrets. DAB image: mcr.microsoft.com/azure-databases/data-api-builder."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "Which Azure service is most suitable for deploying Data API Builder in production with auto-scaling and built-in HTTPS?",
                            "opts": ["A. Azure Virtual Machines", "B. Azure Container Apps", "C. Azure SQL Managed Instance", "D. Azure Functions"],
                            "correct": "B",
                            "explain": "Azure Container Apps provides a managed container hosting environment with auto-scaling, built-in HTTPS, Managed Identity support, and usage-based pricing. It is the recommended deployment target for Data API Builder in production."
                        },
                        {
                            "q": "In the connection string for Azure SQL with Managed Identity, what replaces the username and password?",
                            "opts": ["A. API key in the Authorization header", "B. Authentication=Active Directory Managed Identity", "C. Integrated Security=True", "D. Trust Server Certificate=True"],
                            "correct": "B",
                            "explain": "'Authentication=Active Directory Managed Identity' tells the SQL client library to obtain an Azure AD token using the host resource's Managed Identity. No username or password is needed — Azure handles token acquisition."
                        },
                        {
                            "q": "What does --ingress external do when creating an Azure Container App?",
                            "opts": ["A. Creates an internal load balancer only accessible within the VNET", "B. Exposes the Container App to the internet with a public HTTPS URL", "C. Sets up an API Gateway in front of the container", "D. Enables external logging to Azure Monitor"],
                            "correct": "B",
                            "explain": "--ingress external makes the Container App accessible from the public internet. Azure Container Apps automatically provisions an HTTPS endpoint with a unique FQDN. HTTPS is enforced by default."
                        },
                        {
                            "q": "Why should you use a specific version tag (e.g., :1.3.0) instead of :latest for the DAB Docker image in production?",
                            "opts": ["A. :latest is not available for the DAB image", "B. Specific versions ensure reproducible deployments — :latest can pull a breaking change unexpectedly", "C. :latest uses more CPU and memory than specific versions", "D. Azure Container Apps requires specific version tags"],
                            "correct": "B",
                            "explain": "Using :latest means every new container instance might pull a different image version, potentially including breaking changes. Pinning to a specific version ensures all replicas run the same code and deployments are reproducible."
                        },
                        {
                            "q": "What is the purpose of creating a SQL user with CREATE USER [container-app-name] FROM EXTERNAL PROVIDER in Azure SQL?",
                            "opts": ["A. Creates a SQL login for the container app to use with a username and password", "B. Creates a database user backed by the container app's Azure AD Managed Identity", "C. Grants the container app permission to create databases", "D. Registers the container app as an OAuth provider for the database"],
                            "correct": "B",
                            "explain": "CREATE USER ... FROM EXTERNAL PROVIDER creates a database user backed by an Azure AD identity (the Container App's Managed Identity). You then GRANT this user the required permissions. No password is set — authentication uses Azure AD tokens."
                        }
                    ]
                },

                # ── Unit 6: Azure Monitor configurations ────────────────
                {
                    "id": "lp2-m8-u6",
                    "title": "Azure Monitor configurations",
                    "description": "Configure Azure Monitor diagnostic settings, Log Analytics, and alert rules for Azure SQL databases.",
                    "estimated_time": 25,
                    "objectives": [
                        "Enable diagnostic settings to send SQL logs to Log Analytics",
                        "Write KQL queries against SQL diagnostic data",
                        "Configure alert rules for database performance thresholds"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Azure Monitor for SQL Databases",
                            "body": "Azure Monitor is the central observability platform for all Azure services. For Azure SQL Database, it provides:<br><br><strong>Metrics (built-in, always collected):</strong><ul><li>DTU/vCore percentage — compute utilization</li><li>Data I/O percentage — storage I/O utilization</li><li>CPU percentage — CPU usage</li><li>Connection count — active connections</li><li>Deadlock count — deadlocks per minute</li><li>Storage percentage — disk usage</li></ul><strong>Diagnostic Logs (must be enabled):</strong><ul><li>SQLInsights — query performance data</li><li>QueryStoreRuntimeStatistics — Query Store data</li><li>Errors — SQL error log</li><li>Deadlocks — deadlock graphs</li><li>Audit — SQL audit log</li></ul><strong>Destinations for diagnostic logs:</strong><ul><li>Log Analytics Workspace (query with KQL)</li><li>Azure Blob Storage (archive)</li><li>Azure Event Hubs (stream to SIEM/third-party)</li></ul>"
                        },
                        {
                            "type": "sql_block",
                            "title": "Configure Diagnostics and KQL Queries",
                            "scenario": "Enable Azure Monitor for an Azure SQL Database and write KQL queries to investigate slow queries and deadlocks.",
                            "code": """# ============================================================
# STEP 1: Enable Diagnostic Settings via Azure CLI
# ============================================================

# Create a Log Analytics Workspace first
az monitor log-analytics workspace create \\
  --resource-group rg-salesdb \\
  --workspace-name law-salesdb \\
  --location eastus

# Enable diagnostic settings for the SQL Database
az monitor diagnostic-settings create \\
  --resource "/subscriptions/<sub-id>/resourceGroups/rg-salesdb/providers/Microsoft.Sql/servers/myserver/databases/SalesDB" \\
  --name "SalesDB-Diagnostics" \\
  --workspace "/subscriptions/<sub-id>/resourceGroups/rg-salesdb/providers/Microsoft.OperationalInsights/workspaces/law-salesdb" \\
  --logs '[
    {"category": "SQLInsights", "enabled": true, "retentionPolicy": {"days": 90, "enabled": true}},
    {"category": "QueryStoreRuntimeStatistics", "enabled": true},
    {"category": "Errors", "enabled": true},
    {"category": "Deadlocks", "enabled": true}
  ]' \\
  --metrics '[
    {"category": "Basic", "enabled": true}
  ]'

# ============================================================
# STEP 2: KQL Queries in Log Analytics
# Run these in Azure Portal → Log Analytics Workspace → Logs
# ============================================================

-- Find slow queries (top 10 by duration)
AzureDiagnostics
| where ResourceProvider == "MICROSOFT.SQL"
| where Category == "QueryStoreRuntimeStatistics"
| where TimeGenerated > ago(24h)
| project
    TimeGenerated,
    query_hash_s,
    avg_duration_d,
    count_executions_d,
    avg_logical_io_reads_d
| sort by avg_duration_d desc
| take 10

-- Count deadlocks over the last 7 days
AzureDiagnostics
| where ResourceProvider == "MICROSOFT.SQL"
| where Category == "Deadlocks"
| where TimeGenerated > ago(7d)
| summarize DeadlockCount = count() by bin(TimeGenerated, 1h)
| sort by TimeGenerated asc
| render timechart

-- Monitor DTU usage over the last hour
AzureMetrics
| where ResourceProvider == "MICROSOFT.SQL"
| where MetricName == "dtu_consumption_percent"
| where TimeGenerated > ago(1h)
| summarize AvgDTU = avg(Average), MaxDTU = max(Maximum) by bin(TimeGenerated, 5m)
| sort by TimeGenerated asc
| render timechart

-- Find connection failures
AzureDiagnostics
| where ResourceProvider == "MICROSOFT.SQL"
| where Category == "Errors"
| where TimeGenerated > ago(24h)
| where error_number_d in (18456, 4060, 40613)  -- login failures, DB unavailable
| project TimeGenerated, error_number_d, error_message_s, client_ip_s
| sort by TimeGenerated desc

# ============================================================
# STEP 3: Create an Alert Rule for high DTU usage
# ============================================================

az monitor metrics alert create \\
  --name "High-DTU-Alert" \\
  --resource-group rg-salesdb \\
  --scopes "/subscriptions/<sub-id>/resourceGroups/rg-salesdb/providers/Microsoft.Sql/servers/myserver/databases/SalesDB" \\
  --condition "avg dtu_consumption_percent > 80" \\
  --window-size 5m \\
  --evaluation-frequency 1m \\
  --action "/subscriptions/<sub-id>/resourceGroups/rg-salesdb/providers/Microsoft.Insights/actionGroups/dba-alerts" \\
  --description "Alert when DTU exceeds 80% for 5 minutes"

# ============================================================
# STEP 4: SQL Insights (query performance monitoring)
# Azure Portal → SQL Database → Monitoring → Query Performance Insight
# Shows top queries by CPU, duration, and I/O automatically
# ============================================================""",
                            "explanation": "Diagnostic settings route SQL telemetry to Log Analytics where KQL queries let you investigate performance, errors, and deadlocks. Alert rules automatically notify your team when thresholds are breached. Query Performance Insight provides a built-in graphical view in the Azure Portal.",
                            "purpose": "Gain visibility into SQL database health and performance through centralized monitoring, enabling proactive issue detection and investigation.",
                            "breakdown": [
                                {"line": "az monitor diagnostic-settings create ... --logs '[{\"category\": \"SQLInsights\"...}]'", "meaning": "Enables specific log categories for the SQL database. Each category sends different data to Log Analytics. SQLInsights = query stats. Deadlocks = deadlock graphs. Errors = SQL error log."},
                                {"line": "AzureDiagnostics | where ResourceProvider == 'MICROSOFT.SQL'", "meaning": "KQL query start. AzureDiagnostics is the Log Analytics table that receives diagnostic logs from all Azure resources. Filter by ResourceProvider to get SQL-specific logs."},
                                {"line": "| where Category == 'QueryStoreRuntimeStatistics'", "meaning": "Filters to Query Store data sent from the SQL database. Contains avg_duration_d, count_executions_d, avg_logical_io_reads_d per query hash."},
                                {"line": "| summarize DeadlockCount = count() by bin(TimeGenerated, 1h)", "meaning": "KQL aggregation: count events per 1-hour time bucket. bin() rounds TimeGenerated to 1-hour intervals. render timechart creates a line chart."},
                                {"line": "az monitor metrics alert create ... --condition 'avg dtu_consumption_percent > 80'", "meaning": "Creates an Azure Monitor alert that fires when the average DTU percentage exceeds 80% over a 5-minute window. Sends notification to the specified action group (email, SMS, webhook)."}
                            ],
                            "ssms_steps": [
                                "In Azure Portal: go to your SQL Database → Diagnostic settings (under Monitoring section)",
                                "Click + Add diagnostic setting",
                                "Check the log categories: SQLInsights, QueryStoreRuntimeStatistics, Errors, Deadlocks",
                                "Choose destination: Send to Log Analytics workspace → select or create a workspace",
                                "Click Save",
                                "Wait 5-10 minutes for data to appear in Log Analytics",
                                "Go to Log Analytics workspace → Logs",
                                "Run the KQL queries from Step 2 above",
                                "To create alerts: Portal → SQL Database → Alerts → New alert rule"
                            ],
                            "exam_tip": "Azure Monitor for SQL: Metrics are auto-collected (DTU%, CPU%, connections). Diagnostic settings must be explicitly enabled and send to Log Analytics, Blob Storage, or Event Hubs. KQL queries AzureDiagnostics and AzureMetrics tables. Alert rules use metric conditions or log query results."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "Which Azure Monitor feature must be explicitly enabled to send SQL database logs to Log Analytics?",
                            "opts": ["A. Azure Monitor Insights", "B. Diagnostic Settings", "C. Activity Logs", "D. Application Insights"],
                            "correct": "B",
                            "explain": "Diagnostic Settings must be configured to route SQL database logs (SQLInsights, QueryStore, Errors, Deadlocks, Audit) to a destination. Basic metrics are collected automatically, but diagnostic logs require explicit configuration."
                        },
                        {
                            "q": "Which KQL table contains Azure SQL diagnostic log data in Log Analytics?",
                            "opts": ["A. SQLDiagnostics", "B. AzureLogs", "C. AzureDiagnostics", "D. SQLInsightsData"],
                            "correct": "C",
                            "explain": "AzureDiagnostics is the primary Log Analytics table that receives diagnostic logs from Azure resources including SQL Database. Filter with: where ResourceProvider == 'MICROSOFT.SQL' to get SQL-specific records."
                        },
                        {
                            "q": "What does the KQL operator 'bin(TimeGenerated, 1h)' do?",
                            "opts": ["A. Filters events older than 1 hour", "B. Rounds timestamps to 1-hour intervals for time-series aggregation", "C. Limits results to 1 hour of data", "D. Creates 1-hour data retention bins"],
                            "correct": "B",
                            "explain": "bin(column, interval) rounds a datetime value down to the nearest interval bucket. bin(TimeGenerated, 1h) groups all events within the same hour into one bucket. Used with summarize to create time-series aggregations."
                        },
                        {
                            "q": "Which Azure Portal feature provides a built-in graphical view of top SQL queries by CPU and duration without writing KQL?",
                            "opts": ["A. Azure Monitor Metrics explorer", "B. Log Analytics Insights", "C. Query Performance Insight", "D. SQL Intelligent Insights"],
                            "correct": "C",
                            "explain": "Query Performance Insight (Azure Portal → SQL Database → Monitoring → Query Performance Insight) provides automatic charts of top queries by CPU, duration, and data I/O. It reads from Query Store data and requires Query Store to be enabled."
                        },
                        {
                            "q": "Which log category in Azure SQL diagnostic settings captures deadlock information?",
                            "opts": ["A. SQLInsights", "B. Errors", "C. Deadlocks", "D. QueryStoreRuntimeStatistics"],
                            "correct": "C",
                            "explain": "The Deadlocks category captures SQL Server deadlock events and their associated deadlock graphs. These are sent to Log Analytics (AzureDiagnostics table with Category = 'Deadlocks') where you can query and analyze deadlock patterns."
                        }
                    ]
                },

                # ── Unit 7: Event-driven patterns with SQL ───────────────
                {
                    "id": "lp2-m8-u7",
                    "title": "Event-driven patterns with SQL",
                    "description": "Implement Change Data Capture (CDC) and event-driven architectures to react to SQL database changes.",
                    "estimated_time": 30,
                    "objectives": [
                        "Enable and query Change Data Capture (CDC) tables",
                        "Understand Azure Event Grid and Service Bus integration patterns",
                        "Design an event-driven architecture for SQL data changes"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Event-Driven Patterns with SQL Databases",
                            "body": "Traditional applications poll the database: 'has anything changed since last check?' This wastes resources and adds latency. Event-driven patterns instead <strong>publish events when data changes</strong>, allowing subscribers to react immediately.<br><br><strong>SQL Server Change Data Capture (CDC):</strong><ul><li>Automatically captures INSERT, UPDATE, DELETE changes to configured tables</li><li>Changes stored in CDC change tables (cdc.dbo_TableName_CT)</li><li>Each change row has: LSN (Log Sequence Number), operation type (__$operation: 1=Delete, 2=Insert, 3=Before Update, 4=After Update)</li><li>Applications poll CDC tables instead of the original table — low impact</li></ul><strong>Event-driven integration options:</strong><ul><li><strong>Azure Logic Apps + SQL connector</strong> — trigger workflow when row is inserted/updated</li><li><strong>Azure Function with SQL trigger</strong> — serverless function triggered by CDC changes</li><li><strong>Azure Event Grid</strong> — SQL Database emits events (available in Azure SQL)</li><li><strong>Change feed to Service Bus</strong> — read CDC changes and publish to Service Bus for async processing</li></ul>"
                        },
                        {
                            "type": "sql_block",
                            "title": "Enable and Use Change Data Capture",
                            "scenario": "You need to detect all changes to the Orders table and publish them to Azure Service Bus so an order fulfillment service can react to new orders without polling the database.",
                            "code": """-- ============================================================
-- STEP 1: Enable CDC on the database
-- ============================================================
USE SalesDB;
GO

-- Enable CDC at the database level
EXEC sys.sp_cdc_enable_db;
GO

-- Verify CDC is enabled
SELECT name, is_cdc_enabled FROM sys.databases WHERE name = 'SalesDB';
GO

-- ============================================================
-- STEP 2: Enable CDC on the Orders table
-- ============================================================
EXEC sys.sp_cdc_enable_table
    @source_schema    = 'dbo',
    @source_name      = 'Orders',
    @role_name        = NULL,              -- NULL = no special role required to read CDC
    @supports_net_changes = 1,             -- enables net changes function
    @capture_instance = 'dbo_Orders';      -- name for the CDC capture instance
GO

-- Verify table is CDC-enabled
SELECT
    object_name(source_object_id) AS TableName,
    capture_instance,
    is_tracked_by_cdc,
    start_lsn
FROM cdc.change_tables;
GO

-- ============================================================
-- STEP 3: Make some changes to generate CDC records
-- ============================================================
INSERT INTO dbo.Orders (CustomerID, OrderDate, TotalAmount, Status)
VALUES (1, GETDATE(), 250.00, 'Pending');

UPDATE dbo.Orders SET Status = 'Processing' WHERE OrderID = 1;

DELETE FROM dbo.Orders WHERE OrderID = 2;
GO

-- ============================================================
-- STEP 4: Query the CDC change table
-- ============================================================
-- The change table is automatically created: cdc.dbo_Orders_CT
SELECT
    __$start_lsn       AS LSN,
    __$operation       AS OperationType,
    -- 1=Delete, 2=Insert, 3=Before Update, 4=After Update
    CASE __$operation
        WHEN 1 THEN 'DELETE'
        WHEN 2 THEN 'INSERT'
        WHEN 3 THEN 'BEFORE_UPDATE'
        WHEN 4 THEN 'AFTER_UPDATE'
    END AS OperationName,
    __$update_mask     AS UpdatedColumns,
    OrderID,
    CustomerID,
    TotalAmount,
    Status
FROM cdc.dbo_Orders_CT
ORDER BY __$start_lsn;
GO

-- ============================================================
-- STEP 5: Use CDC functions to get changes in a time range
-- ============================================================
DECLARE @from_lsn BINARY(10), @to_lsn BINARY(10);

-- Get LSN for 1 hour ago
SET @from_lsn = sys.fn_cdc_map_time_to_lsn('smallest greater than or equal',
    DATEADD(HOUR, -1, GETUTCDATE()));

-- Get LSN for now
SET @to_lsn = sys.fn_cdc_get_max_lsn();

-- Get all changes in the last hour
SELECT * FROM cdc.fn_cdc_get_all_changes_dbo_Orders(
    @from_lsn,
    @to_lsn,
    'all'           -- 'all' returns all change rows; 'all update old' includes before-image
);
GO

-- ============================================================
-- STEP 6: Azure Function pseudo-code (C# / Python) to process changes
-- In Azure Portal: Function App → Add function → SQL trigger
-- ============================================================

-- The Azure Function SQL trigger monitors a table/view for changes:
-- [FunctionName("ProcessOrderChanges")]
-- public static async Task Run(
--   [SqlTrigger("[dbo].[Orders]", "Connection")]
--   IReadOnlyList<SqlChange<Order>> changes,
--   [ServiceBus("orders-queue", Connection = "ServiceBusConnection")]
--   IAsyncCollector<ServiceBusMessage> messageSender)
-- {
--   foreach (var change in changes) {
--     await messageSender.AddAsync(new ServiceBusMessage(
--       JsonSerializer.Serialize(change.Item)));
--   }
-- }

-- This Azure Function automatically fires when rows change in dbo.Orders
-- and publishes the change to Azure Service Bus""",
                            "explanation": "CDC captures changes to the transaction log without impacting the source table's performance. The Azure Function SQL trigger (preview feature) uses CDC under the hood to fire on table changes and can route events to Service Bus, Event Grid, or other Azure services.",
                            "purpose": "Implement event-driven data processing so downstream services react to database changes in real time without polling the database.",
                            "breakdown": [
                                {"line": "sys.sp_cdc_enable_db", "meaning": "Enables CDC at the database level. Creates the CDC schema and supporting tables. Must be done before enabling CDC on individual tables."},
                                {"line": "sys.sp_cdc_enable_table @source_schema, @source_name, @role_name", "meaning": "Enables CDC for a specific table. Creates cdc.dbo_TableName_CT change table. @role_name controls who can read CDC data. NULL means any db_owner/cdc_admin can read."},
                                {"line": "__$operation values 1,2,3,4", "meaning": "CDC operation type: 1=Delete (row being deleted), 2=Insert (new row), 3=Before Update (row before change), 4=After Update (row after change). Updates produce TWO rows: before (3) and after (4)."},
                                {"line": "cdc.fn_cdc_get_all_changes_dbo_Orders(@from_lsn, @to_lsn, 'all')", "meaning": "CDC function that returns all changes to the Orders table between two LSN (Log Sequence Number) points. More structured than querying the change table directly."},
                                {"line": "sys.fn_cdc_map_time_to_lsn('smallest greater than or equal', datetime)", "meaning": "Converts a datetime to the corresponding LSN in the transaction log. Lets you query CDC changes by time range rather than LSN range."}
                            ],
                            "ssms_steps": [
                                "Open SSMS and connect to your SQL Server (2008+) or Azure SQL Database",
                                "Run Step 1: EXEC sys.sp_cdc_enable_db in your database",
                                "Run Step 2: EXEC sys.sp_cdc_enable_table for the Orders table",
                                "Run Step 3: INSERT, UPDATE, DELETE some rows",
                                "Run Step 4: SELECT from cdc.dbo_Orders_CT — you should see the change records",
                                "Observe the __$operation column: 2 for your INSERT, 3 and 4 for your UPDATE, 1 for your DELETE",
                                "Run Step 5: use the CDC functions with time-based LSN mapping"
                            ],
                            "exam_tip": "CDC is the foundation of event-driven SQL patterns. Know: sp_cdc_enable_db (database level) then sp_cdc_enable_table (table level). Change table: cdc.dbo_TableName_CT. Operations: 1=Delete, 2=Insert, 3=Before Update, 4=After Update. Azure Function SQL trigger uses CDC under the hood."
                        },
                        {
                            "type": "tip",
                            "title": "Azure Function SQL Trigger",
                            "body": "The Azure Function SQL trigger (available in preview) is the simplest way to react to table changes. It uses CDC internally and fires your function code whenever rows in a specified table are inserted, updated, or deleted. You just write the handler code — no CDC polling logic needed. The trigger is available for C#, Java, Python, and Node.js Azure Functions."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What is the correct order to enable CDC on a specific table?",
                            "opts": ["A. sp_cdc_enable_table, then sp_cdc_enable_db", "B. sp_cdc_enable_db (database), then sp_cdc_enable_table (table)", "C. ALTER TABLE ... SET CDC ON, then EXEC sp_cdc_enable_db", "D. sp_cdc_enable_table only — no database-level step needed"],
                            "correct": "B",
                            "explain": "CDC setup is a two-step process: (1) Enable at database level with sp_cdc_enable_db — creates CDC infrastructure. (2) Enable on specific tables with sp_cdc_enable_table — creates the change table. The database step must come first."
                        },
                        {
                            "q": "In a CDC change table, what does __$operation = 4 mean?",
                            "opts": ["A. Row was deleted", "B. Row was inserted", "C. The state of the row before an UPDATE", "D. The state of the row after an UPDATE"],
                            "correct": "D",
                            "explain": "CDC operation values: 1=Delete, 2=Insert, 3=Before Update (pre-image), 4=After Update (post-image). An UPDATE generates two rows: operation 3 (what the row looked like before) and operation 4 (what the row looks like after)."
                        },
                        {
                            "q": "Which system function converts a datetime to a CDC Log Sequence Number (LSN)?",
                            "opts": ["A. sys.fn_cdc_datetime_to_lsn()", "B. sys.fn_cdc_map_time_to_lsn()", "C. cdc.fn_convert_datetime_lsn()", "D. sys.fn_cdc_get_lsn_for_time()"],
                            "correct": "B",
                            "explain": "sys.fn_cdc_map_time_to_lsn(relation, datetime) converts a datetime to an LSN. The 'relation' parameter ('smallest greater than or equal', 'largest less than or equal', etc.) determines how the boundary is handled when the datetime falls between log entries."
                        },
                        {
                            "q": "What Azure service can receive CDC-captured changes for asynchronous processing by multiple consumers?",
                            "opts": ["A. Azure SQL Sync", "B. Azure Service Bus (queues or topics)", "C. Azure Monitor Logs", "D. Azure Data Factory"],
                            "correct": "B",
                            "explain": "Azure Service Bus queues (for single consumer) or topics (for multiple consumers/subscriptions) are ideal for publishing SQL change events. Consumers (Azure Functions, Logic Apps, custom services) process messages independently and at their own pace."
                        },
                        {
                            "q": "The Azure Function SQL trigger simplifies event-driven SQL patterns by doing what automatically?",
                            "opts": ["A. Writing change records directly to Azure Cosmos DB", "B. Handling CDC polling and firing the function when table rows change", "C. Creating new CDC-enabled tables for monitored objects", "D. Encrypting changed rows before publishing them"],
                            "correct": "B",
                            "explain": "The Azure Function SQL trigger internally uses CDC to monitor the specified table. When rows are inserted, updated, or deleted, the trigger automatically fires the function with the changed records. Developers don't need to implement CDC polling logic."
                        }
                    ]
                },

                # ── Unit 8: Exercise ────────────────────────────────────
                {
                    "id": "lp2-m8-u8",
                    "title": "Exercise",
                    "description": "Hands-on exercise: expose a SQL database with DAB and set up CDC for event-driven processing.",
                    "estimated_time": 40,
                    "objectives": [
                        "Configure a DAB config for a products database",
                        "Enable CDC on a products table",
                        "Query CDC changes to simulate event-driven processing"
                    ],
                    "content": [
                        {
                            "type": "sql_block",
                            "title": "Exercise: Build an API and Event Pipeline for a Product Catalog",
                            "scenario": "Build a REST/GraphQL API for a product catalog using DAB, and set up CDC to detect inventory changes for a real-time stock alert system.",
                            "code": """-- ============================================================
-- PART 1: Set up the database
-- ============================================================
CREATE TABLE dbo.Products (
    ProductID   INT           IDENTITY(1,1) PRIMARY KEY,
    ProductName NVARCHAR(200) NOT NULL,
    Category    NVARCHAR(100) NOT NULL,
    Price       DECIMAL(10,2) NOT NULL,
    StockQty    INT           NOT NULL DEFAULT(0),
    IsActive    BIT           NOT NULL DEFAULT(1)
);
GO

INSERT INTO dbo.Products (ProductName, Category, Price, StockQty) VALUES
('Laptop Pro 15',  'Electronics', 1299.99, 50),
('Wireless Mouse', 'Electronics',   29.99, 200),
('Office Chair',   'Furniture',    349.99, 15);
GO

-- ============================================================
-- PART 2: Create DAB config (dab-config.json)
-- ============================================================
-- Run from terminal:
-- dab init --database-type mssql \
--     --connection-string "Server=localhost;Database=ProductDB;Trusted_Connection=true;" \
--     --host-mode Development
--
-- dab add Product \
--     --source "dbo.Products" \
--     --permissions "anonymous:read" \
--     --rest.path "/Product"
--
-- Then manually add to dab-config.json:
-- "mappings": { "ProductID": "id", "ProductName": "name",
--               "StockQty": "stock", "IsActive": "active" }
--
-- dab start

-- TEST the API:
-- GET http://localhost:5000/api/Product
-- GET http://localhost:5000/api/Product?$filter=stock lt 20  (low stock)
-- GET http://localhost:5000/api/Product?$filter=Category eq 'Electronics'

-- ============================================================
-- PART 3: Enable CDC to track inventory changes
-- ============================================================
EXEC sys.sp_cdc_enable_db;
GO

EXEC sys.sp_cdc_enable_table
    @source_schema = 'dbo',
    @source_name   = 'Products',
    @role_name     = NULL,
    @capture_instance = 'dbo_Products';
GO

-- PART 4: Simulate inventory changes
UPDATE dbo.Products SET StockQty = 2 WHERE ProductName = 'Office Chair'; -- low stock!
UPDATE dbo.Products SET StockQty = 0 WHERE ProductName = 'Laptop Pro 15'; -- out of stock!
INSERT INTO dbo.Products (ProductName, Category, Price, StockQty)
VALUES ('USB-C Hub', 'Electronics', 49.99, 100);                          -- new product
GO

-- PART 5: Query CDC to get inventory changes
SELECT
    CASE __$operation
        WHEN 1 THEN 'DELETED'
        WHEN 2 THEN 'INSERTED'
        WHEN 4 THEN 'UPDATED'
    END AS EventType,
    ProductID,
    ProductName,
    StockQty,
    CASE
        WHEN StockQty = 0 THEN 'OUT OF STOCK - URGENT'
        WHEN StockQty < 10 THEN 'LOW STOCK - ORDER SOON'
        ELSE 'NORMAL'
    END AS StockAlert
FROM cdc.dbo_Products_CT
WHERE __$operation IN (2, 4)  -- only inserts and after-updates
ORDER BY __$start_lsn;
GO

-- PART 6: Simulate the event processing query
-- (In production this runs in an Azure Function or polling service)
DECLARE @last_lsn BINARY(10) = 0x00000000000000000000;  -- track last processed LSN
DECLARE @current_lsn BINARY(10) = sys.fn_cdc_get_max_lsn();

SELECT
    __$start_lsn AS EventLSN,
    __$operation AS OperationType,
    ProductID,
    ProductName,
    StockQty
FROM cdc.fn_cdc_get_all_changes_dbo_Products(
    @last_lsn,
    @current_lsn,
    'all with merge'   -- collapses before/after update into one row
)
WHERE StockQty <= 10;  -- only low-stock events
GO""",
                            "explanation": "This exercise combines DAB (for API access) and CDC (for change detection). The DAB API lets front-end apps query the catalog. The CDC events drive stock alerts without the alert system needing to poll the Products table directly.",
                            "purpose": "Experience the pattern of exposing SQL data as an API (DAB) while simultaneously using CDC to power real-time event-driven processing.",
                            "breakdown": [
                                {"line": "$filter=stock lt 20", "meaning": "OData filter using the mapped field name 'stock' (mapped from StockQty in dab-config.json). Returns products where StockQty < 20. The mapping means the API uses clean names, not database column names."},
                                {"line": "cdc.fn_cdc_get_all_changes_dbo_Products(@from, @to, 'all with merge')", "meaning": "The 'all with merge' parameter collapses the before-update (op 3) and after-update (op 4) rows into a single result row. Simpler than handling pairs, but you lose the before-image."}
                            ],
                            "ssms_steps": [
                                "Run Part 1 to create the Products table and insert data",
                                "Run dab init and dab add from terminal to create the DAB config",
                                "Edit dab-config.json to add the mappings section",
                                "Run: dab start and test: http://localhost:5000/api/Product",
                                "Try the OData filter: /api/Product?$filter=StockQty lt 20",
                                "In SSMS: run Part 3 to enable CDC",
                                "Run Part 4 to make inventory changes",
                                "Run Part 5 to see the CDC change records with stock alerts",
                                "Examine the EventType and StockAlert columns — you should see 'OUT OF STOCK' for Laptop Pro 15"
                            ],
                            "exam_tip": "This exercise demonstrates the two main integration patterns: DAB (push-based API) and CDC (pull-based change detection). In production, CDC is typically read by an Azure Function that then pushes events to Service Bus or Event Grid."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "In the exercise, the DAB config uses 'stock' as a mapping for the 'StockQty' column. How do you filter on this in a REST query?",
                            "opts": ["A. ?$filter=StockQty lt 20", "B. ?$filter=stock lt 20", "C. ?where=stock<20", "D. ?stock_filter=lt:20"],
                            "correct": "B",
                            "explain": "When column mappings are defined in dab-config.json, API consumers use the mapped names (not database column names). 'StockQty' is mapped to 'stock', so OData filters use 'stock': $filter=stock lt 20."
                        },
                        {
                            "q": "What does 'all with merge' do in cdc.fn_cdc_get_all_changes?",
                            "opts": ["A. Merges CDC data from multiple tables into one result", "B. Combines the before-update and after-update rows into a single row per UPDATE", "C. Merges CDC results with the source table data", "D. Removes duplicate INSERT events from the result"],
                            "correct": "B",
                            "explain": "'all with merge' collapses the two CDC rows for an UPDATE (operation 3=before, operation 4=after) into a single row showing the final state (operation 4). Simpler to process but you lose the before-image comparison."
                        },
                        {
                            "q": "In the exercise's event processing query, why filter on WHERE StockQty <= 10?",
                            "opts": ["A. CDC only captures changes where StockQty changes", "B. To only trigger stock alerts for low-stock changes — not all inventory updates", "C. CDC change tables only store rows where StockQty is less than 10", "D. The Azure Function trigger has a StockQty limit of 10"],
                            "correct": "B",
                            "explain": "The WHERE StockQty <= 10 filter on the CDC query ensures only low-stock changes generate events. CDC captures ALL changes to the Products table, but the business logic only needs alerts for critical stock levels."
                        },
                        {
                            "q": "What is the advantage of using DAB's REST API over direct SQL queries for a front-end application?",
                            "opts": ["A. DAB REST API is faster than SQL queries", "B. The front-end gets a standard HTTP API without needing database credentials or SQL knowledge", "C. DAB automatically caches all database queries", "D. REST API queries run in parallel threads automatically"],
                            "correct": "B",
                            "explain": "DAB provides a standard REST API that front-end applications can call with HTTP — no SQL knowledge, no database driver, no direct database credentials needed. The API enforces permissions and provides a stable interface even if the schema changes."
                        },
                        {
                            "q": "In the exercise, which component detects the stock level dropping to 0 for the Laptop Pro?",
                            "opts": ["A. The DAB REST API query with $filter", "B. An Azure Monitor alert rule", "C. The CDC change table query with CASE WHEN StockQty = 0 THEN 'OUT OF STOCK'", "D. An Azure Function SQL trigger"],
                            "correct": "C",
                            "explain": "The Part 5 CDC query reads from cdc.dbo_Products_CT and applies a CASE expression to categorize stock levels. The UPDATE to StockQty = 0 generated a CDC record with operation 4 (after update), and the CASE detects it as 'OUT OF STOCK - URGENT'."
                        }
                    ]
                },

                # ── Unit 9: Module Assessment ───────────────────────────
                {
                    "id": "lp2-m8-u9",
                    "title": "Module assessment",
                    "description": "Test your understanding of SQL integration with Azure services.",
                    "estimated_time": 20,
                    "objectives": [
                        "Demonstrate knowledge of DAB, Azure Monitor, and event-driven patterns"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Module 8 Key Concepts Review",
                            "body": "Review before the assessment:<br><br><strong>Data API Builder:</strong> dab-config.json drives REST and GraphQL. data-source (connection) + runtime (API config + auth) + entities (SQL object mappings). Source types: table, view, stored-procedure. View needs key-fields. SP permission = execute. REST uses OData ($filter, $orderby, $top). GraphQL uses typed filters. Mappings rename columns. Relationships enable JOINs in GraphQL. Deploy to Azure Container Apps with Managed Identity.<br><br><strong>Azure Monitor:</strong> Metrics auto-collected (DTU%, CPU%). Diagnostic Settings must be enabled (SQLInsights, Deadlocks, Errors). Destinations: Log Analytics, Blob, Event Hubs. KQL queries AzureDiagnostics table. Alert rules on metrics or log queries.<br><br><strong>Event-Driven / CDC:</strong> sp_cdc_enable_db then sp_cdc_enable_table. Change table: cdc.schema_Table_CT. Operations: 1=Delete, 2=Insert, 3=Before Update, 4=After Update. fn_cdc_get_all_changes for LSN-based querying. fn_cdc_map_time_to_lsn to convert datetime to LSN. Azure Function SQL trigger automates CDC polling. Service Bus for async fan-out."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "A developer wants to expose dbo.vw_SalesSummary (a view with no primary key, with SaleID as unique identifier) via DAB. What config is needed?",
                            "opts": ["A. source type: 'table', no additional config", "B. source type: 'view', key-fields: ['SaleID']", "C. source type: 'stored-procedure', parameters: { SaleID: ... }", "D. source type: 'view', primary-key: 'SaleID'"],
                            "correct": "B",
                            "explain": "Views use source type 'view'. Since views have no primary key constraint, key-fields specifies which column(s) uniquely identify rows. This enables single-record lookups like GET /api/SalesSummary/id/5."
                        },
                        {
                            "q": "You need Azure SQL Database logs to be queryable with KQL. What must you configure?",
                            "opts": ["A. Enable Query Store on the database", "B. Create a Diagnostic Setting and route logs to a Log Analytics Workspace", "C. Install Log Analytics agent on the SQL Server VM", "D. Enable Azure Defender for SQL"],
                            "correct": "B",
                            "explain": "To query SQL logs with KQL, you must create a Diagnostic Setting that routes selected log categories (SQLInsights, Errors, Deadlocks, etc.) to a Log Analytics Workspace. Then query the AzureDiagnostics table in that workspace."
                        },
                        {
                            "q": "A CDC change table shows two rows for the same OrderID: one with __$operation = 3 and one with __$operation = 4. What happened?",
                            "opts": ["A. The row was inserted twice", "B. The row was updated — operation 3 is the before-image, operation 4 is the after-image", "C. The row was deleted and then re-inserted", "D. The CDC capture ran twice for the same change"],
                            "correct": "B",
                            "explain": "A single UPDATE produces two CDC records: operation 3 (before update — the old values) and operation 4 (after update — the new values). This lets you see exactly what changed."
                        },
                        {
                            "q": "Which dab-config.json section defines the SQL Server connection?",
                            "opts": ["A. runtime.host", "B. entities", "C. data-source", "D. runtime.rest"],
                            "correct": "C",
                            "explain": "The data-source section in dab-config.json contains the database-type ('mssql', 'postgresql', etc.) and connection-string (preferably via @env()). This is separate from the runtime section (API settings) and entities section (SQL object mappings)."
                        },
                        {
                            "q": "What enables an Azure Function to automatically fire when rows are inserted or updated in a SQL table?",
                            "opts": ["A. A SQL Server trigger that calls the Azure Function URL", "B. The Azure Function SQL trigger binding which uses CDC internally", "C. Azure Monitor alert that triggers the function", "D. A Logic App that polls the table and calls the function"],
                            "correct": "B",
                            "explain": "The Azure Function SQL trigger binding monitors a SQL table (using CDC under the hood) and automatically fires the function when rows are inserted, updated, or deleted. No polling code needed — the Function runtime handles CDC tracking."
                        }
                    ]
                },

                # ── Unit 10: Summary ────────────────────────────────────
                {
                    "id": "lp2-m8-u10",
                    "title": "Summary",
                    "description": "Review all Azure SQL integration topics covered in this module.",
                    "estimated_time": 5,
                    "objectives": [
                        "Recall key DAB, Azure Monitor, and event-driven pattern concepts"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Module 8 Summary — Azure SQL Integration",
                            "body": "In this module you learned to integrate SQL databases with Azure services:<br><br><ul><li><strong>Data API Builder</strong> — dab CLI: init → add entities → start. dab-config.json: data-source + runtime + entities. Source types: table/view/stored-procedure. Views need key-fields. SP permission = execute. Mappings rename columns. REST uses OData. GraphQL with typed filters and cursor pagination. Relationships enable auto-JOINs. Deploy to Azure Container Apps with Managed Identity auth.</li><li><strong>Deployment</strong> — Azure Container Apps preferred: auto-scale, HTTPS, Managed Identity. Official image: mcr.microsoft.com/azure-databases/data-api-builder. Connection string uses 'Authentication=Active Directory Managed Identity'. Secrets for environment variables. production host mode disables debug info.</li><li><strong>Azure Monitor</strong> — Metrics auto-collected. Diagnostic Settings to enable logs → Log Analytics / Blob / Event Hubs. KQL queries AzureDiagnostics: filter by ResourceProvider, Category. Alert rules on metrics (dtu_consumption_percent) or log queries. Query Performance Insight for built-in graphical query analysis.</li><li><strong>Event-Driven / CDC</strong> — sp_cdc_enable_db → sp_cdc_enable_table. Change table: cdc.dbo_TableName_CT. Operations: 1=Del, 2=Ins, 3=BeforeUpd, 4=AfterUpd. fn_cdc_get_all_changes for batch reads. fn_cdc_map_time_to_lsn for time-based queries. Azure Function SQL trigger for serverless event handling. Service Bus for async multi-consumer fan-out.</li></ul>"
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What command starts the Data API Builder local development server?",
                            "opts": ["A. dab run", "B. dab start", "C. dotnet run --project dab", "D. dab serve"],
                            "correct": "B",
                            "explain": "'dab start' starts the local DAB server (by default at http://localhost:5000). It reads dab-config.json from the current directory. Use --config to specify a different config file path."
                        },
                        {
                            "q": "Which section of dab-config.json defines entity-to-SQL-object mappings?",
                            "opts": ["A. data-source", "B. runtime", "C. entities", "D. schema"],
                            "correct": "C",
                            "explain": "The entities section maps API entity names to SQL objects. Each entity specifies source (SQL object name and type), permissions, REST/GraphQL settings, field mappings, and relationships."
                        },
                        {
                            "q": "What does the AzureDiagnostics KQL table contain?",
                            "opts": ["A. Only SQL Server logs", "B. Only Azure Monitor metric values", "C. Diagnostic logs from all Azure resources that have diagnostic settings configured", "D. Only security audit logs from Azure SQL"],
                            "correct": "C",
                            "explain": "AzureDiagnostics receives diagnostic logs from ALL Azure resources with diagnostic settings pointing to that Log Analytics workspace. Filter by ResourceProvider == 'MICROSOFT.SQL' to get SQL-specific records."
                        },
                        {
                            "q": "Which CDC stored procedure enables CDC at the database level?",
                            "opts": ["A. sys.sp_cdc_enable_table", "B. sys.sp_cdc_enable_db", "C. sys.sp_cdc_start", "D. ALTER DATABASE ... SET CDC ON"],
                            "correct": "B",
                            "explain": "sys.sp_cdc_enable_db enables CDC at the database level — creates CDC schema, change tables, and supporting objects. This must be run first. Then sys.sp_cdc_enable_table enables CDC for individual tables."
                        },
                        {
                            "q": "What is the benefit of using Azure Service Bus for processing SQL CDC events?",
                            "opts": ["A. Service Bus automatically writes to CDC tables", "B. Multiple independent consumers can process the same change events asynchronously", "C. Service Bus eliminates the need for CDC entirely", "D. Service Bus automatically replays failed SQL transactions"],
                            "correct": "B",
                            "explain": "Azure Service Bus topics allow multiple subscribers (consumers) to independently receive and process the same messages. CDC events published to a topic can be consumed by an order fulfillment service, an analytics system, and a notification service — all independently and at their own pace."
                        }
                    ]
                }
            ]
        }
    ]
}
