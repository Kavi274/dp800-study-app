# DP-800 Exam: "Develop AI-enabled database solutions"
# Learning Path 1: Design and develop database solutions

LP1_DATA = {
    "id": "lp1",
    "title": "Design and develop database solutions",
    "description": "Learn to design and build SQL database solutions using T-SQL, programmability objects, and AI-assisted development tools.",
    "color": "#0078d4",
    "icon": "fas fa-database",
    "modules": [

        # ══════════════════════════════════════════════════════════════
        # MODULE 1: Design and implement database objects with SQL
        # ══════════════════════════════════════════════════════════════
        {
            "id": "lp1-m1",
            "title": "Design and implement database objects with SQL",
            "description": "Learn to create tables, indexes, constraints, and advanced structures including JSON columns and partitioned tables.",
            "units": [

                # ── Unit 1: Introduction ─────────────────────────────
                {
                    "id": "lp1-m1-u1",
                    "title": "Introduction",
                    "description": "Overview of what you will learn in this module about designing database objects.",
                    "estimated_time": 5,
                    "objectives": [
                        "Understand the scope of this module",
                        "Know which database object types will be covered",
                        "Understand why good database design matters for the DP-800 exam"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "What This Module Covers",
                            "body": "This module is your foundation for the DP-800 exam section on <strong>designing and implementing database objects</strong>. A database is only as good as its structure — poorly designed tables lead to slow queries, bad data, and maintenance headaches.\n\n<strong>You will learn to:</strong>\n<ul><li>Choose the right SQL Server platform (on-premises vs Azure)</li><li>Create tables with correct data types and nullability</li><li>Speed up queries with indexes (clustered and nonclustered)</li><li>Use specialized table types like temp tables and memory-optimized tables</li><li>Enforce business rules with constraints</li><li>Store and query JSON data inside SQL columns</li><li>Partition large tables to improve performance</li></ul>\n\n<strong>Why this matters for the exam:</strong> The DP-800 exam tests your ability to <em>build</em> database solutions, not just query them. You need to know the T-SQL syntax to create these objects and the reasons why you would choose one approach over another."
                        },
                        {
                            "type": "important",
                            "title": "Prerequisites",
                            "body": "You should have basic SQL knowledge before starting — knowing what SELECT, FROM, and WHERE do is enough. This module will teach you the <strong>CREATE</strong> side of SQL (building structures), not just the querying side."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What is the main focus of this module?",
                            "opts": ["A. Writing SELECT queries", "B. Designing and implementing database objects", "C. Building Power BI reports", "D. Managing Azure subscriptions"],
                            "correct": "B",
                            "explain": "This module focuses on designing and implementing database objects such as tables, indexes, constraints, and partitions using T-SQL."
                        },
                        {
                            "q": "Which T-SQL command is used to build database structures?",
                            "opts": ["A. SELECT", "B. INSERT", "C. CREATE", "D. UPDATE"],
                            "correct": "C",
                            "explain": "CREATE is the DDL (Data Definition Language) command used to build database objects like tables, indexes, views, and procedures."
                        },
                        {
                            "q": "What does DDL stand for in SQL?",
                            "opts": ["A. Data Display Language", "B. Data Definition Language", "C. Database Design Logic", "D. Dynamic Data Layer"],
                            "correct": "B",
                            "explain": "DDL stands for Data Definition Language — the subset of SQL commands (CREATE, ALTER, DROP) used to define and modify database structures."
                        },
                        {
                            "q": "Which of the following is NOT a topic covered in this module?",
                            "opts": ["A. Creating indexes", "B. Enforcing constraints", "C. Writing stored procedures", "D. Partitioning tables"],
                            "correct": "C",
                            "explain": "Stored procedures are covered in Module 2 (Programmability Objects). This module focuses on database objects: tables, indexes, constraints, JSON, and partitioning."
                        },
                        {
                            "q": "Why does good database design matter?",
                            "opts": ["A. It makes dashboards look better", "B. It prevents the need for backups", "C. It improves query performance, data integrity, and maintainability", "D. It reduces the number of SQL keywords needed"],
                            "correct": "C",
                            "explain": "Good database design directly affects query speed (through proper indexing and table structure), data quality (through constraints), and long-term maintainability."
                        }
                    ]
                },

                # ── Unit 2: Understand SQL server-based platform choices ──
                {
                    "id": "lp1-m1-u2",
                    "title": "Understand SQL server-based platform choices",
                    "description": "Compare SQL Server on-premises, Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure VMs.",
                    "estimated_time": 20,
                    "objectives": [
                        "Distinguish between SQL Server deployment options",
                        "Understand when to choose each platform",
                        "Know key differences relevant to the DP-800 exam"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "The Four SQL Server Platform Options",
                            "body": "Microsoft offers SQL Server in several forms. Choosing the right one is an important design decision:\n\n<strong>1. SQL Server on-premises</strong><br>You install SQL Server on your own hardware or a VM in your data center. You control everything — the OS, SQL version, patching schedule — but you also manage everything.\n<ul><li>Best when: You have compliance requirements that prevent cloud use, or legacy apps that need full control</li><li>Example: A hospital that cannot put patient data in the cloud</li></ul>\n\n<strong>2. SQL Server on Azure Virtual Machines (IaaS)</strong><br>SQL Server runs on a VM in Azure, but you still manage the OS and SQL Server installation. Think of it as renting a server in Microsoft's data center.\n<ul><li>Best when: You need a specific SQL Server version or feature not available in PaaS options, or you are doing a lift-and-shift migration</li><li>Key point: This is <strong>IaaS</strong> — you manage the VM</li></ul>\n\n<strong>3. Azure SQL Managed Instance (PaaS)</strong><br>A fully managed SQL Server instance in Azure. Nearly 100% compatible with on-premises SQL Server. Microsoft patches and backs it up automatically.\n<ul><li>Best when: You want cloud benefits but need features like SQL Agent, cross-database queries, or CLR</li><li>Key point: This is <strong>PaaS</strong> — Microsoft manages the infrastructure</li></ul>\n\n<strong>4. Azure SQL Database (PaaS)</strong><br>A single database as a fully managed cloud service. The most cloud-native option with automatic scaling, built-in high availability, and serverless options.\n<ul><li>Best when: Building new cloud-native applications, or when you need elastic scaling</li><li>Key point: Does NOT support some on-premises features (SQL Agent, cross-database queries without elastic queries)</li></ul>"
                        },
                        {
                            "type": "important",
                            "title": "IaaS vs PaaS — Key Exam Distinction",
                            "body": "<strong>IaaS (Infrastructure as a Service):</strong> You manage the OS and SQL Server. Azure manages the physical hardware.<br><strong>PaaS (Platform as a Service):</strong> Microsoft manages everything except your data and configuration. You just use the service.\n\n<strong>Memory trick:</strong> SQL on VM = IaaS (you see a VM). Managed Instance and SQL Database = PaaS (no VM to manage)."
                        },
                        {
                            "type": "theory",
                            "title": "Feature Comparison",
                            "body": "<strong>Features to know for the exam:</strong>\n<ul><li><strong>SQL Server Agent</strong> (scheduled jobs): Available in on-prem, Azure VM, Managed Instance — <em>NOT</em> in Azure SQL Database</li><li><strong>Cross-database queries</strong>: Available in on-prem, Azure VM, Managed Instance — limited in Azure SQL Database</li><li><strong>CLR (Common Language Runtime)</strong>: Available in on-prem, Azure VM, Managed Instance — NOT in Azure SQL Database</li><li><strong>Automatic backups</strong>: Managed Instance and Azure SQL Database handle this automatically</li><li><strong>Always On Availability Groups</strong>: Built-in high availability in Azure SQL DB and Managed Instance</li></ul>"
                        },
                        {
                            "type": "tip",
                            "title": "Exam Strategy for Platform Questions",
                            "body": "When the exam asks which platform to choose, look for these keywords in the scenario:\n<ul><li>'<strong>lift and shift</strong>' or 'minimal changes' → Azure SQL Managed Instance</li><li>'<strong>new cloud-native app</strong>' or 'elastic scale' → Azure SQL Database</li><li>'<strong>full control</strong>' or 'specific SQL version' → SQL Server on Azure VM</li><li>'<strong>cannot use cloud</strong>' or 'on-premises only' → SQL Server on-premises</li></ul>"
                        },
                        {
                            "type": "sql_block",
                            "title": "Checking Your SQL Server Version and Edition",
                            "scenario": "Once connected to any SQL Server platform, you can run a quick query to confirm what you are connected to. This is useful when starting work on an unfamiliar server.",
                            "code": "SELECT \n    @@SERVERNAME        AS ServerName,\n    @@VERSION           AS FullVersionInfo,\n    SERVERPROPERTY('Edition')       AS Edition,\n    SERVERPROPERTY('EngineEdition') AS EngineEdition,\n    SERVERPROPERTY('ProductVersion') AS ProductVersion;",
                            "explanation": "This query returns information about the SQL Server instance you are connected to, helping you understand which platform and version you are working with.",
                            "purpose": "Verify which SQL Server platform you are connected to",
                            "breakdown": [
                                {"line": "@@SERVERNAME", "meaning": "Returns the name of the server. On Azure SQL Database this returns your logical server name."},
                                {"line": "@@VERSION", "meaning": "Returns a full string with version, edition, and build date — everything in one field."},
                                {"line": "SERVERPROPERTY('Edition')", "meaning": "Returns the edition such as 'Developer Edition', 'Enterprise Edition', or 'SQL Azure' for Azure SQL Database."},
                                {"line": "SERVERPROPERTY('EngineEdition')", "meaning": "Returns a number: 1=Personal, 2=Standard, 3=Enterprise, 5=SQL Database (Azure), 8=Managed Instance."},
                                {"line": "SERVERPROPERTY('ProductVersion')", "meaning": "Returns the version number like '16.0.1000.6' — useful for knowing the SQL Server release year."}
                            ],
                            "ssms_steps": [
                                "Open SSMS (SQL Server Management Studio)",
                                "In the 'Connect to Server' dialog, enter your server name and credentials",
                                "Click Connect",
                                "Click 'New Query' in the toolbar (or press Ctrl+N)",
                                "Paste the SQL code above into the query window",
                                "Press F5 or click 'Execute' to run the query",
                                "Look at the Results tab — check the 'Edition' column to see which platform you are on",
                                "If EngineEdition = 5, you are on Azure SQL Database; if 8, you are on Managed Instance"
                            ],
                            "exam_tip": "EngineEdition = 5 means Azure SQL Database (PaaS, serverless option). EngineEdition = 8 means Azure SQL Managed Instance. Knowing these numbers can help you answer platform identification questions."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "Which SQL Server deployment option is classified as IaaS?",
                            "opts": ["A. Azure SQL Database", "B. Azure SQL Managed Instance", "C. SQL Server on Azure Virtual Machines", "D. SQL Server Serverless"],
                            "correct": "C",
                            "explain": "SQL Server on Azure VMs is IaaS because you manage the operating system and SQL Server installation. Azure only manages the physical hardware."
                        },
                        {
                            "q": "A company wants to migrate an on-premises SQL Server application to Azure with minimal code changes and needs SQL Agent jobs. Which option is best?",
                            "opts": ["A. Azure SQL Database", "B. Azure SQL Managed Instance", "C. Azure Cosmos DB", "D. Azure Table Storage"],
                            "correct": "B",
                            "explain": "Azure SQL Managed Instance is nearly 100% compatible with on-premises SQL Server and supports SQL Agent jobs, making it ideal for lift-and-shift migrations."
                        },
                        {
                            "q": "Which feature is NOT available in Azure SQL Database (single database)?",
                            "opts": ["A. Automatic backups", "B. Built-in high availability", "C. SQL Server Agent jobs", "D. T-SQL queries"],
                            "correct": "C",
                            "explain": "SQL Server Agent (for scheduling jobs) is not available in Azure SQL Database. It is available in SQL Server on-premises, Azure VMs, and Managed Instance."
                        },
                        {
                            "q": "What does SERVERPROPERTY('EngineEdition') return for Azure SQL Database?",
                            "opts": ["A. 1", "B. 3", "C. 5", "D. 8"],
                            "correct": "C",
                            "explain": "EngineEdition = 5 identifies Azure SQL Database. EngineEdition = 8 identifies Azure SQL Managed Instance."
                        },
                        {
                            "q": "A startup is building a new cloud-native web application and needs automatic elastic scaling. Which SQL platform is most appropriate?",
                            "opts": ["A. SQL Server on-premises", "B. SQL Server on Azure VM", "C. Azure SQL Managed Instance", "D. Azure SQL Database"],
                            "correct": "D",
                            "explain": "Azure SQL Database is the most cloud-native option with serverless and elastic pool capabilities, making it ideal for new applications needing elastic scaling."
                        }
                    ]
                },

                # ── Unit 3: Build effective tables ───────────────────
                {
                    "id": "lp1-m1-u3",
                    "title": "Build effective tables",
                    "description": "Learn to design and create SQL Server tables with appropriate data types, nullability, and primary keys.",
                    "estimated_time": 25,
                    "objectives": [
                        "Choose appropriate data types for columns",
                        "Understand NULL vs NOT NULL and when to use each",
                        "Create tables with PRIMARY KEY constraints",
                        "Understand the difference between IDENTITY and sequences"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "SQL Server Data Types",
                            "body": "Every column in a SQL table must have a <strong>data type</strong> — this tells SQL Server what kind of data the column stores and how much space it takes.\n\n<strong>Numeric types:</strong>\n<ul><li><strong>INT</strong> — Whole numbers from -2.1 billion to 2.1 billion. Use for IDs, counts.</li><li><strong>BIGINT</strong> — Larger whole numbers. Use when INT is too small (e.g., row counts in billions).</li><li><strong>SMALLINT</strong> — Smaller whole numbers (-32,768 to 32,767). Saves space when values are small.</li><li><strong>DECIMAL(p,s)</strong> or <strong>NUMERIC(p,s)</strong> — Exact decimal numbers. p=total digits, s=digits after decimal. Use for money calculations. Example: DECIMAL(10,2) stores values like 12345678.99</li><li><strong>FLOAT</strong> — Approximate floating-point. Avoid for money — use DECIMAL instead.</li></ul>\n\n<strong>String types:</strong>\n<ul><li><strong>VARCHAR(n)</strong> — Variable-length text up to n characters. Use for names, descriptions. Example: VARCHAR(100) for a name field.</li><li><strong>NVARCHAR(n)</strong> — Variable-length Unicode text. Use when you need to store international characters (Arabic, Chinese, etc). Takes 2 bytes per character.</li><li><strong>CHAR(n)</strong> — Fixed-length text, always n characters (padded with spaces). Use for codes that are always the same length (e.g., state codes like 'CA', 'NY').</li></ul>\n\n<strong>Date/Time types:</strong>\n<ul><li><strong>DATE</strong> — Date only (no time). Example: '2024-01-15'. Use for birthdays, hire dates.</li><li><strong>DATETIME2</strong> — Date and time with high precision. Better than old DATETIME. Use for timestamps.</li><li><strong>DATETIMEOFFSET</strong> — Date/time with timezone offset. Use for global applications.</li></ul>\n\n<strong>Other types:</strong>\n<ul><li><strong>BIT</strong> — 0 or 1 (true/false). Use for boolean flags like IsActive, IsDeleted.</li><li><strong>UNIQUEIDENTIFIER</strong> — A GUID (globally unique ID). Use when you need IDs that are unique across multiple databases.</li></ul>"
                        },
                        {
                            "type": "theory",
                            "title": "NULL vs NOT NULL",
                            "body": "<strong>NULL</strong> means 'no value / unknown'. It is NOT the same as zero or an empty string.\n\n<strong>NOT NULL</strong> on a column means the column is required — SQL Server will reject any INSERT that does not provide a value for that column.\n\n<strong>When to use NOT NULL:</strong>\n<ul><li>Columns that are always required (CustomerID, OrderDate, Email)</li><li>Primary key columns (always NOT NULL)</li><li>Columns used in joins or calculations (NULLs in calculations return NULL)</li></ul>\n\n<strong>When NULL is acceptable:</strong>\n<ul><li>Optional fields (MiddleName, PhoneNumber, Notes)</li><li>Fields filled in later (ShipDate — not known at order time)</li></ul>\n\n<strong>Exam tip:</strong> If you do not write NULL or NOT NULL, SQL Server defaults to NULL (the column is optional). Always be explicit."
                        },
                        {
                            "type": "sql_block",
                            "title": "Creating a Complete Customers Table",
                            "scenario": "You are building an e-commerce database and need to create a Customers table that stores customer information properly.",
                            "code": "-- First, make sure we are using the right database\nUSE ECommerceDB;\nGO\n\n-- Create the Customers table\nCREATE TABLE dbo.Customers (\n    CustomerID    INT             NOT NULL IDENTITY(1,1),\n    FirstName     NVARCHAR(50)    NOT NULL,\n    LastName      NVARCHAR(50)    NOT NULL,\n    Email         VARCHAR(100)    NOT NULL,\n    PhoneNumber   VARCHAR(20)     NULL,\n    DateOfBirth   DATE            NULL,\n    IsActive      BIT             NOT NULL DEFAULT 1,\n    CreatedDate   DATETIME2       NOT NULL DEFAULT GETDATE(),\n    Balance       DECIMAL(10,2)   NOT NULL DEFAULT 0.00,\n    CONSTRAINT PK_Customers PRIMARY KEY (CustomerID),\n    CONSTRAINT UQ_Customers_Email UNIQUE (Email)\n);",
                            "explanation": "This creates a properly designed Customers table with appropriate data types, nullability rules, an auto-incrementing primary key, and useful default values.",
                            "purpose": "Create a table with real-world design best practices",
                            "breakdown": [
                                {"line": "USE ECommerceDB;", "meaning": "Switch to the ECommerceDB database so we create the table in the right place."},
                                {"line": "GO", "meaning": "GO is a batch separator in SSMS — it tells SSMS to send everything before it as one batch to SQL Server. It is not a T-SQL keyword."},
                                {"line": "CREATE TABLE dbo.Customers (", "meaning": "Start creating a table named Customers in the dbo schema. dbo (database owner) is the default schema — always specify it explicitly."},
                                {"line": "CustomerID INT NOT NULL IDENTITY(1,1),", "meaning": "IDENTITY(1,1) means auto-increment: start at 1, increase by 1 each row. NOT NULL because every customer must have an ID."},
                                {"line": "FirstName NVARCHAR(50) NOT NULL,", "meaning": "NVARCHAR stores Unicode text (supports all languages). 50 characters max. NOT NULL because every customer must have a first name."},
                                {"line": "Email VARCHAR(100) NOT NULL,", "meaning": "Email addresses are ASCII characters only, so VARCHAR is fine (no Unicode needed). 100 chars max."},
                                {"line": "PhoneNumber VARCHAR(20) NULL,", "meaning": "NULL here — phone number is optional. Not every customer provides one."},
                                {"line": "IsActive BIT NOT NULL DEFAULT 1,", "meaning": "BIT stores 0 or 1. DEFAULT 1 means new customers are active by default. NOT NULL ensures it always has a value."},
                                {"line": "CreatedDate DATETIME2 NOT NULL DEFAULT GETDATE(),", "meaning": "GETDATE() returns the current date/time. DEFAULT GETDATE() means this fills in automatically when a row is inserted."},
                                {"line": "Balance DECIMAL(10,2) NOT NULL DEFAULT 0.00,", "meaning": "DECIMAL(10,2) allows up to 10 digits total with 2 after the decimal — perfect for money. New customers start with 0."},
                                {"line": "CONSTRAINT PK_Customers PRIMARY KEY (CustomerID),", "meaning": "Explicitly names the primary key constraint PK_Customers. Good practice — named constraints are easier to manage than unnamed ones."},
                                {"line": "CONSTRAINT UQ_Customers_Email UNIQUE (Email)", "meaning": "Ensures no two customers can have the same email address. The UNIQUE constraint enforces this at the database level."}
                            ],
                            "ssms_steps": [
                                "Open SSMS and connect to your SQL Server",
                                "In Object Explorer (left panel), right-click 'Databases' and select 'New Database...' if ECommerceDB doesn't exist",
                                "Name the database 'ECommerceDB' and click OK",
                                "Click 'New Query' in the toolbar",
                                "Paste the full CREATE TABLE code above",
                                "Press F5 to execute",
                                "You should see 'Commands completed successfully' in the Messages tab",
                                "In Object Explorer, expand ECommerceDB → Tables → dbo.Customers → Columns to verify all columns were created",
                                "Right-click on 'dbo.Customers' and select 'Design' to see the visual table designer"
                            ],
                            "exam_tip": "IDENTITY(seed, increment) — seed is the starting value, increment is how much it increases. IDENTITY(1,1) is the most common. The exam may ask you to identify what IDENTITY(100,5) does: starts at 100, increments by 5."
                        },
                        {
                            "type": "tip",
                            "title": "Naming Conventions",
                            "body": "Always use consistent naming:\n<ul><li>Constraint names: <strong>PK_TableName</strong> for primary keys, <strong>FK_TableName_RefTable</strong> for foreign keys, <strong>UQ_TableName_Column</strong> for unique constraints</li><li>Always specify the schema: <strong>dbo.TableName</strong> not just TableName</li><li>Use PascalCase for table and column names: CustomerID not customerid or customer_id</li></ul>\nNamed constraints make it much easier to ALTER or DROP them later."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "Which data type should you use to store monetary values accurately in SQL Server?",
                            "opts": ["A. FLOAT", "B. REAL", "C. DECIMAL(10,2)", "D. INT"],
                            "correct": "C",
                            "explain": "DECIMAL (or NUMERIC) stores exact decimal values and should be used for money. FLOAT stores approximate values, which can cause rounding errors in financial calculations."
                        },
                        {
                            "q": "What does IDENTITY(1,1) mean on a column definition?",
                            "opts": ["A. The column can only store values 1 or -1", "B. The column auto-increments starting at 1, increasing by 1 each row", "C. The column has a default value of 1 and maximum of 1", "D. The column is the first column and has one index"],
                            "correct": "B",
                            "explain": "IDENTITY(seed, increment) configures auto-numbering. IDENTITY(1,1) starts at 1 and adds 1 for each new row inserted, so rows get IDs 1, 2, 3, 4..."
                        },
                        {
                            "q": "What is the difference between VARCHAR and NVARCHAR?",
                            "opts": ["A. VARCHAR stores numbers, NVARCHAR stores text", "B. VARCHAR is fixed-length, NVARCHAR is variable-length", "C. VARCHAR stores ASCII text, NVARCHAR stores Unicode (international characters)", "D. There is no difference — they are aliases"],
                            "correct": "C",
                            "explain": "VARCHAR stores standard ASCII characters (1 byte each). NVARCHAR stores Unicode characters (2 bytes each), which supports all international character sets including Arabic, Chinese, Japanese, etc."
                        },
                        {
                            "q": "If you create a column without specifying NULL or NOT NULL, what is the SQL Server default?",
                            "opts": ["A. NOT NULL — the column is required", "B. NULL — the column is optional", "C. An error is thrown", "D. It depends on the data type"],
                            "correct": "B",
                            "explain": "SQL Server defaults to NULL (optional) if you do not specify. Best practice is to always explicitly write NULL or NOT NULL to make your intent clear."
                        },
                        {
                            "q": "Which constraint ensures no two rows can have the same value in a column (other than the primary key)?",
                            "opts": ["A. CHECK constraint", "B. DEFAULT constraint", "C. UNIQUE constraint", "D. FOREIGN KEY constraint"],
                            "correct": "C",
                            "explain": "The UNIQUE constraint ensures column values are distinct across all rows. It differs from PRIMARY KEY in that a table can have multiple UNIQUE constraints, and UNIQUE columns can allow one NULL value."
                        }
                    ]
                },

                # ── Unit 4: Optimize with indexes ─────────────────────
                {
                    "id": "lp1-m1-u4",
                    "title": "Optimize with indexes",
                    "description": "Understand clustered and nonclustered indexes, how they speed up queries, and how to create them in T-SQL.",
                    "estimated_time": 25,
                    "objectives": [
                        "Understand what an index does and how it works",
                        "Distinguish between clustered and nonclustered indexes",
                        "Create indexes using T-SQL",
                        "Know when to add indexes and when they hurt performance"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "What is an Index?",
                            "body": "An <strong>index</strong> is a database structure that speeds up data retrieval. Without an index, SQL Server must scan every single row in a table to find what you need — this is called a <strong>table scan</strong> and is very slow on large tables.\n\nThink of a book index: instead of reading every page to find 'primary key', you look up P in the index and jump straight to the right pages. SQL indexes work the same way.\n\n<strong>How SQL indexes work internally:</strong><br>SQL Server stores indexes as a <strong>B-tree (Balanced Tree)</strong> structure. Data is sorted and stored in a tree shape. SQL Server can quickly navigate the tree to find values in just a few steps, even in tables with millions of rows.\n\n<strong>The trade-off:</strong> Indexes speed up reads (SELECT) but slow down writes (INSERT, UPDATE, DELETE) because SQL Server must update the index every time data changes. Do not add indexes to every column — add them to columns you frequently search, join, or sort by."
                        },
                        {
                            "type": "theory",
                            "title": "Clustered vs Nonclustered Indexes",
                            "body": "<strong>Clustered Index:</strong>\n<ul><li>Determines the <em>physical order</em> of data in the table — the table rows are stored sorted by the clustered index key</li><li>A table can have <strong>only ONE</strong> clustered index (because data can only be physically sorted one way)</li><li>When you create a PRIMARY KEY, SQL Server creates a clustered index on it automatically</li><li>Think of it as the main filing system — books sorted alphabetically by title on a shelf</li></ul>\n\n<strong>Nonclustered Index:</strong>\n<ul><li>A <em>separate structure</em> that contains index key values and pointers to the actual data rows</li><li>A table can have <strong>up to 999</strong> nonclustered indexes</li><li>Think of it as a card catalog in a library — the cards are sorted by author, but they just point you to where the actual book is on the shelf</li><li>Use nonclustered indexes on columns you frequently filter by (WHERE clause), join on, or sort by (ORDER BY)</li></ul>\n\n<strong>Memory trick:</strong> Clustered = data IS sorted that way. Nonclustered = a separate sorted lookup that POINTS to data."
                        },
                        {
                            "type": "sql_block",
                            "title": "Creating Clustered and Nonclustered Indexes",
                            "scenario": "You have an Orders table that is getting slow. Queries filter by CustomerID and OrderDate frequently. You need to add appropriate indexes.",
                            "code": "-- 1. Create the Orders table first\nCREATE TABLE dbo.Orders (\n    OrderID      INT          NOT NULL IDENTITY(1,1),\n    CustomerID   INT          NOT NULL,\n    OrderDate    DATE         NOT NULL,\n    TotalAmount  DECIMAL(10,2) NOT NULL,\n    Status       VARCHAR(20)  NOT NULL DEFAULT 'Pending',\n    CONSTRAINT PK_Orders PRIMARY KEY CLUSTERED (OrderID)\n);\nGO\n\n-- 2. Add a nonclustered index on CustomerID\n--    (to speed up: WHERE CustomerID = 123)\nCREATE NONCLUSTERED INDEX IX_Orders_CustomerID\n    ON dbo.Orders (CustomerID);\nGO\n\n-- 3. Add a nonclustered index on OrderDate\n--    (to speed up: WHERE OrderDate BETWEEN '2024-01-01' AND '2024-12-31')\nCREATE NONCLUSTERED INDEX IX_Orders_OrderDate\n    ON dbo.Orders (OrderDate DESC);\nGO\n\n-- 4. Add a composite index on CustomerID + OrderDate\n--    (to speed up: WHERE CustomerID = 123 AND OrderDate > '2024-01-01')\nCREATE NONCLUSTERED INDEX IX_Orders_CustomerID_OrderDate\n    ON dbo.Orders (CustomerID, OrderDate DESC)\n    INCLUDE (TotalAmount, Status);\nGO\n\n-- 5. Check what indexes exist on the table\nSELECT \n    i.name AS IndexName,\n    i.type_desc AS IndexType,\n    STRING_AGG(c.name, ', ') AS Columns\nFROM sys.indexes i\nJOIN sys.index_columns ic ON i.object_id = ic.object_id AND i.index_id = ic.index_id\nJOIN sys.columns c ON ic.object_id = c.object_id AND ic.column_id = c.column_id\nWHERE i.object_id = OBJECT_ID('dbo.Orders')\nGROUP BY i.name, i.type_desc;",
                            "explanation": "This demonstrates creating a clustered primary key index, individual nonclustered indexes, and a composite nonclustered index with INCLUDEd columns.",
                            "purpose": "Optimize an Orders table for common query patterns",
                            "breakdown": [
                                {"line": "CONSTRAINT PK_Orders PRIMARY KEY CLUSTERED (OrderID)", "meaning": "Creates the primary key as a CLUSTERED index on OrderID. Rows in the table will be physically stored sorted by OrderID."},
                                {"line": "CREATE NONCLUSTERED INDEX IX_Orders_CustomerID", "meaning": "Creates a separate lookup structure sorted by CustomerID. Queries filtering WHERE CustomerID = x will use this index instead of scanning the whole table."},
                                {"line": "ON dbo.Orders (CustomerID)", "meaning": "Specifies which table and which column(s) the index is built on."},
                                {"line": "CREATE NONCLUSTERED INDEX IX_Orders_OrderDate ON dbo.Orders (OrderDate DESC)", "meaning": "DESC means the index is sorted newest-to-oldest. Useful for queries that ORDER BY OrderDate DESC to get recent orders first."},
                                {"line": "CREATE NONCLUSTERED INDEX IX_Orders_CustomerID_OrderDate", "meaning": "A composite index on two columns. SQL Server can use this for queries that filter on CustomerID alone, or CustomerID + OrderDate together."},
                                {"line": "INCLUDE (TotalAmount, Status)", "meaning": "INCLUDEd columns are stored in the index leaf pages but are NOT part of the sort key. This allows the query to get all needed data from the index without touching the main table rows — called a 'covering index'."},
                                {"line": "sys.indexes, sys.index_columns, sys.columns", "meaning": "System catalog views that store metadata about indexes. Joining them lets you see which indexes exist and which columns they cover."}
                            ],
                            "ssms_steps": [
                                "Open SSMS and connect to your server",
                                "Click New Query",
                                "Paste the full code above",
                                "Press F5 to execute all statements",
                                "In Object Explorer, navigate to your database → Tables → dbo.Orders → Indexes",
                                "You should see PK_Orders (Clustered), IX_Orders_CustomerID (Nonclustered), IX_Orders_OrderDate (Nonclustered), and IX_Orders_CustomerID_OrderDate (Nonclustered)",
                                "To test the index is being used: write a SELECT query, highlight it, then press Ctrl+M to enable 'Include Actual Execution Plan', then press F5",
                                "Look for 'Index Seek' in the execution plan — this means the index was used. 'Table Scan' or 'Index Scan' means no suitable index was found"
                            ],
                            "exam_tip": "A table can have only ONE clustered index but up to 999 nonclustered indexes. The PRIMARY KEY is clustered by default. INCLUDE columns make a 'covering index' that can satisfy a query entirely from the index without reading the base table."
                        },
                        {
                            "type": "important",
                            "title": "Index Performance Trade-offs",
                            "body": "<strong>Indexes help with:</strong> SELECT queries with WHERE, JOIN, ORDER BY, GROUP BY on indexed columns.\n\n<strong>Indexes hurt:</strong> INSERT, UPDATE, DELETE operations because every index must be updated when data changes.\n\n<strong>Rule of thumb:</strong>\n<ul><li>Always index foreign key columns (used in JOINs)</li><li>Index columns you frequently filter by in WHERE clauses</li><li>Do NOT index columns with very few distinct values (e.g., IsActive BIT column — only 0 or 1). An index on such a column is rarely useful.</li><li>Do NOT over-index write-heavy tables (like logging tables)</li></ul>"
                        }
                    ],
                    "quiz": [
                        {
                            "q": "How many clustered indexes can a SQL Server table have?",
                            "opts": ["A. Unlimited", "B. Up to 999", "C. Exactly one", "D. Up to 32"],
                            "correct": "C",
                            "explain": "A table can have only one clustered index because the clustered index determines the physical storage order of data, and data can only be physically sorted one way."
                        },
                        {
                            "q": "What is an INCLUDE column in a nonclustered index?",
                            "opts": ["A. A column that is part of the index sort key", "B. A column stored in the index leaf pages to avoid lookups to the base table", "C. A column that is excluded from the index", "D. A column that triggers an automatic index rebuild"],
                            "correct": "B",
                            "explain": "INCLUDE columns are stored at the leaf level of the nonclustered index. They allow queries to get all needed data from the index alone (a 'covering index'), avoiding a costly lookup back to the base table."
                        },
                        {
                            "q": "Which execution plan operator indicates a query is efficiently using an index?",
                            "opts": ["A. Table Scan", "B. Hash Match", "C. Index Seek", "D. Key Lookup"],
                            "correct": "C",
                            "explain": "Index Seek means SQL Server navigated the B-tree index directly to find matching rows — very efficient. Table Scan means SQL Server read every row in the table — very slow on large tables."
                        },
                        {
                            "q": "Which scenario is a good candidate for a nonclustered index?",
                            "opts": ["A. A BIT column IsActive with values 0 and 1 only", "B. A CustomerID column used in frequent JOIN operations", "C. A large text Notes column that is never searched", "D. A computed column that is rarely queried"],
                            "correct": "B",
                            "explain": "Columns used in JOIN operations are excellent candidates for nonclustered indexes. A BIT column with only 2 distinct values has poor selectivity and makes a poor index candidate."
                        },
                        {
                            "q": "When you create a PRIMARY KEY constraint without specifying CLUSTERED or NONCLUSTERED, what does SQL Server create?",
                            "opts": ["A. A nonclustered index", "B. No index — PRIMARY KEY is not an index", "C. A clustered index", "D. Both a clustered and nonclustered index"],
                            "correct": "C",
                            "explain": "By default, SQL Server creates a CLUSTERED index for a PRIMARY KEY constraint. You can override this by explicitly writing NONCLUSTERED if you want the clustered index on a different column."
                        }
                    ]
                },

                # ── Unit 5: Use specialized table types ───────────────
                {
                    "id": "lp1-m1-u5",
                    "title": "Use specialized table types",
                    "description": "Learn about temporary tables, table variables, and memory-optimized tables and when to use each.",
                    "estimated_time": 20,
                    "objectives": [
                        "Create and use temporary tables (#temp)",
                        "Create and use table variables (@table)",
                        "Understand memory-optimized tables",
                        "Choose the right specialized table type for your scenario"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Why Specialized Table Types?",
                            "body": "Sometimes you need to store data temporarily during a complex operation — data that should not persist in a permanent table. SQL Server offers three options:\n\n<strong>1. Temporary Tables (#temp)</strong>\n<ul><li>Created in the <strong>tempdb</strong> system database</li><li>Prefixed with a single hash: <strong>#TableName</strong></li><li>Visible to the current session and any child sessions (stored procedures called from the same session)</li><li>Automatically dropped when the session ends</li><li>Support indexes, constraints, statistics</li><li>Best for: large intermediate result sets, complex multi-step operations</li></ul>\n\n<strong>2. Global Temporary Tables (##temp)</strong>\n<ul><li>Prefixed with <strong>two hashes: ##TableName</strong></li><li>Visible to ALL sessions (all users)</li><li>Dropped when the last session using them disconnects</li><li>Rarely used — avoid in production as any user can see/modify them</li></ul>\n\n<strong>3. Table Variables (@table)</strong>\n<ul><li>Declared with the <strong>@</strong> prefix, like a regular variable</li><li>Stored in <strong>memory</strong> (and tempdb if large)</li><li>Scope is limited to the batch/procedure they are declared in</li><li>Automatically cleaned up when the batch ends (no explicit DROP needed)</li><li>Less overhead for small datasets, but statistics are limited (SQL Server assumes 1 row)</li><li>Best for: small result sets (less than a few thousand rows)</li></ul>\n\n<strong>4. Memory-Optimized Tables (In-Memory OLTP)</strong>\n<ul><li>Tables that reside entirely in RAM for maximum speed</li><li>Must use the <strong>WITH (MEMORY_OPTIMIZED = ON)</strong> option</li><li>Require a special filegroup: <strong>MEMORY_OPTIMIZED_DATA</strong></li><li>Best for: very high-throughput scenarios (millions of transactions per second)</li></ul>"
                        },
                        {
                            "type": "sql_block",
                            "title": "Temporary Tables and Table Variables in Action",
                            "scenario": "You need to calculate sales summaries in multiple steps. First, collect raw sales data into a temp table, then summarize it.",
                            "code": "-- ============================================\n-- PART 1: Temporary Table (#temp)\n-- ============================================\n\n-- Create a temp table to hold intermediate results\nCREATE TABLE #SalesSummary (\n    CustomerID   INT          NOT NULL,\n    TotalSales   DECIMAL(10,2) NOT NULL,\n    OrderCount   INT          NOT NULL\n);\n\n-- Insert calculated data into the temp table\nINSERT INTO #SalesSummary (CustomerID, TotalSales, OrderCount)\nSELECT \n    CustomerID,\n    SUM(TotalAmount)  AS TotalSales,\n    COUNT(*)          AS OrderCount\nFROM dbo.Orders\nWHERE OrderDate >= '2024-01-01'\nGROUP BY CustomerID;\n\n-- Now use the temp table in further processing\nSELECT \n    s.CustomerID,\n    s.TotalSales,\n    s.OrderCount,\n    s.TotalSales / s.OrderCount AS AvgOrderValue\nFROM #SalesSummary s\nWHERE s.TotalSales > 1000\nORDER BY s.TotalSales DESC;\n\n-- Clean up (optional - drops automatically when session ends)\nDROP TABLE #SalesSummary;\nGO\n\n-- ============================================\n-- PART 2: Table Variable (@table)\n-- ============================================\n\nDECLARE @TopCustomers TABLE (\n    CustomerID   INT          NOT NULL,\n    CustomerName NVARCHAR(100) NOT NULL,\n    TotalSales   DECIMAL(10,2) NOT NULL\n);\n\n-- Insert a small set of top customers\nINSERT INTO @TopCustomers (CustomerID, CustomerName, TotalSales)\nVALUES\n    (1, 'Alice Johnson', 5200.00),\n    (2, 'Bob Smith',     3800.00),\n    (3, 'Carol White',   4100.00);\n\n-- Query the table variable\nSELECT * FROM @TopCustomers ORDER BY TotalSales DESC;\n-- Note: @TopCustomers is automatically gone after this batch ends",
                            "explanation": "Shows the syntax and usage of both #temp tables and @table variables. Temp tables are more powerful; table variables are simpler for small datasets.",
                            "purpose": "Demonstrate when and how to use temporary storage in SQL Server",
                            "breakdown": [
                                {"line": "CREATE TABLE #SalesSummary (", "meaning": "The # prefix creates a temporary table in tempdb. It looks and acts like a regular table but disappears when your session ends."},
                                {"line": "INSERT INTO #SalesSummary ... SELECT ... FROM dbo.Orders", "meaning": "You can insert into a temp table using a SELECT statement — this is called INSERT...SELECT and is very common for populating temp tables with calculated data."},
                                {"line": "DROP TABLE #SalesSummary;", "meaning": "Explicitly removes the temp table. Optional since it auto-drops when session ends, but good practice to clean up."},
                                {"line": "DECLARE @TopCustomers TABLE (", "meaning": "DECLARE creates a table variable. Note the @ prefix (like any variable in T-SQL). The table definition goes in parentheses right after."},
                                {"line": "INSERT INTO @TopCustomers ... VALUES (...)", "meaning": "You can insert rows directly with VALUES. Table variables support INSERT, UPDATE, DELETE, and SELECT just like real tables."},
                                {"line": "SELECT * FROM @TopCustomers ORDER BY TotalSales DESC;", "meaning": "Query a table variable just like a regular table. After this batch ends, @TopCustomers is automatically gone — no DROP needed."}
                            ],
                            "ssms_steps": [
                                "Open SSMS and connect to your server",
                                "Select your database from the dropdown at the top (or USE YourDatabase; at the start)",
                                "Click New Query",
                                "Paste the code for PART 1 (temp table section)",
                                "Press F5 to run — you should see query results showing customers with TotalSales > 1000",
                                "Press Ctrl+N to open a new query window",
                                "Paste the code for PART 2 (table variable section)",
                                "Press F5 — you should see the three customers listed",
                                "Try querying #SalesSummary from the second window — it will fail because temp tables are session-scoped (each query window is a different session)"
                            ],
                            "exam_tip": "Key differences for the exam: #temp supports statistics and indexes (better for large datasets); @table has limited statistics (SQL Server assumes 1 row, which can cause poor query plans). Use #temp for anything over a few thousand rows."
                        },
                        {
                            "type": "tip",
                            "title": "Choosing Between #temp and @table",
                            "body": "<strong>Use #temp when:</strong>\n<ul><li>Your dataset has more than ~1,000-5,000 rows</li><li>You need to add indexes to the intermediate data</li><li>You need the data accessible in called stored procedures</li><li>You need to check row counts or statistics</li></ul>\n<strong>Use @table when:</strong>\n<ul><li>Your dataset is small (a few hundred rows)</li><li>You want automatic cleanup with no DROP needed</li><li>You are inside a function (functions cannot use #temp tables)</li></ul>"
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What prefix is used to create a local temporary table in SQL Server?",
                            "opts": ["A. @", "B. #", "C. ##", "D. $"],
                            "correct": "B",
                            "explain": "A single # prefix creates a local temporary table (visible only to the current session). ## creates a global temp table visible to all sessions."
                        },
                        {
                            "q": "Where are temporary tables stored in SQL Server?",
                            "opts": ["A. In the current user database", "B. In the master database", "C. In the tempdb system database", "D. In memory only"],
                            "correct": "C",
                            "explain": "Temporary tables are created in the tempdb system database, which SQL Server recreates every time it restarts."
                        },
                        {
                            "q": "Which specialized table type is best for very high-throughput scenarios requiring millions of transactions per second?",
                            "opts": ["A. Global temporary tables (##)", "B. Table variables (@)", "C. Memory-optimized tables (MEMORY_OPTIMIZED = ON)", "D. Local temporary tables (#)"],
                            "correct": "C",
                            "explain": "Memory-optimized tables (In-Memory OLTP) reside entirely in RAM and are designed for extremely high-throughput scenarios. They eliminate locking overhead using optimistic concurrency."
                        },
                        {
                            "q": "What is a key limitation of table variables compared to temporary tables?",
                            "opts": ["A. Table variables cannot store NULL values", "B. Table variables cannot be queried with SELECT", "C. Table variables have limited statistics — SQL Server assumes 1 row by default", "D. Table variables cannot be used in stored procedures"],
                            "correct": "C",
                            "explain": "Table variables have outdated or minimal statistics. SQL Server often assumes only 1 row in a table variable, which can lead to poor query execution plans for larger datasets."
                        },
                        {
                            "q": "Can a function in SQL Server use a temporary table (#temp)?",
                            "opts": ["A. Yes, all function types support temp tables", "B. No, functions cannot use temporary tables — use table variables instead", "C. Yes, but only scalar functions", "D. Only table-valued functions can use temp tables"],
                            "correct": "B",
                            "explain": "SQL Server functions cannot create or use temporary tables. If you need temporary storage inside a function, you must use table variables (@table) instead."
                        }
                    ]
                },

                # ── Unit 6: Enforce data integrity with constraints ───
                {
                    "id": "lp1-m1-u6",
                    "title": "Enforce data integrity with constraints",
                    "description": "Learn to use CHECK, UNIQUE, FOREIGN KEY, and DEFAULT constraints to enforce business rules at the database level.",
                    "estimated_time": 25,
                    "objectives": [
                        "Create and use CHECK constraints",
                        "Implement FOREIGN KEY constraints for referential integrity",
                        "Use DEFAULT constraints to provide fallback values",
                        "Understand cascading actions (ON DELETE CASCADE, etc.)"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Why Constraints?",
                            "body": "Constraints are <strong>rules enforced by SQL Server</strong> to ensure your data stays valid and consistent. Instead of relying on application code to validate data, constraints push those rules down to the database level — where they are always enforced, regardless of which application writes data.\n\n<strong>The five main constraint types:</strong>\n<ul><li><strong>PRIMARY KEY</strong> — Uniquely identifies each row, no NULLs allowed</li><li><strong>UNIQUE</strong> — All values in the column must be distinct (allows one NULL)</li><li><strong>FOREIGN KEY</strong> — Ensures a value in one table exists in another table (referential integrity)</li><li><strong>CHECK</strong> — Validates that column values satisfy a logical condition</li><li><strong>DEFAULT</strong> — Provides a value when none is supplied on INSERT</li></ul>"
                        },
                        {
                            "type": "sql_block",
                            "title": "Building a Fully Constrained Database Schema",
                            "scenario": "You are building an order management system. You need constraints to ensure: products have valid prices, orders reference real customers, and order quantities are positive.",
                            "code": "-- ============================================================\n-- Table 1: Products (with CHECK and DEFAULT constraints)\n-- ============================================================\nCREATE TABLE dbo.Products (\n    ProductID    INT            NOT NULL IDENTITY(1,1),\n    ProductName  NVARCHAR(100)  NOT NULL,\n    Price        DECIMAL(10,2)  NOT NULL,\n    StockQty     INT            NOT NULL DEFAULT 0,\n    Category     VARCHAR(50)    NOT NULL DEFAULT 'General',\n    IsActive     BIT            NOT NULL DEFAULT 1,\n    \n    CONSTRAINT PK_Products \n        PRIMARY KEY (ProductID),\n    \n    CONSTRAINT CHK_Products_Price \n        CHECK (Price > 0),\n    \n    CONSTRAINT CHK_Products_StockQty \n        CHECK (StockQty >= 0),\n    \n    CONSTRAINT CHK_Products_Category \n        CHECK (Category IN ('Electronics', 'Clothing', 'Food', 'General'))\n);\nGO\n\n-- ============================================================\n-- Table 2: Customers (already exists from earlier examples)\n-- ============================================================\n-- Assume dbo.Customers already exists with CustomerID PK\n\n-- ============================================================\n-- Table 3: Orders (with FOREIGN KEY constraints)\n-- ============================================================\nCREATE TABLE dbo.OrderItems (\n    OrderItemID  INT            NOT NULL IDENTITY(1,1),\n    OrderID      INT            NOT NULL,\n    ProductID    INT            NOT NULL,\n    Quantity     INT            NOT NULL,\n    UnitPrice    DECIMAL(10,2)  NOT NULL,\n    \n    CONSTRAINT PK_OrderItems \n        PRIMARY KEY (OrderItemID),\n    \n    CONSTRAINT FK_OrderItems_Orders \n        FOREIGN KEY (OrderID) \n        REFERENCES dbo.Orders(OrderID)\n        ON DELETE CASCADE,\n    \n    CONSTRAINT FK_OrderItems_Products \n        FOREIGN KEY (ProductID) \n        REFERENCES dbo.Products(ProductID)\n        ON DELETE NO ACTION,\n    \n    CONSTRAINT CHK_OrderItems_Quantity \n        CHECK (Quantity > 0),\n    \n    CONSTRAINT CHK_OrderItems_UnitPrice \n        CHECK (UnitPrice > 0)\n);\nGO\n\n-- Test the constraints:\n-- This will FAIL: Price cannot be negative\nINSERT INTO dbo.Products (ProductName, Price) \nVALUES ('Laptop', -500.00);  -- Error: CHECK constraint violated\n\n-- This will SUCCEED: valid data\nINSERT INTO dbo.Products (ProductName, Price, Category) \nVALUES ('Laptop', 999.99, 'Electronics');\n\n-- Add a constraint to an existing table using ALTER TABLE\nALTER TABLE dbo.Products\nADD CONSTRAINT CHK_Products_Name \n    CHECK (LEN(ProductName) >= 2);",
                            "explanation": "Demonstrates all major constraint types: PK, CHECK with various conditions, FOREIGN KEY with cascading actions, and how to add constraints to existing tables.",
                            "purpose": "Enforce business rules at the database level",
                            "breakdown": [
                                {"line": "CONSTRAINT CHK_Products_Price CHECK (Price > 0)", "meaning": "A CHECK constraint with a named constraint. The logical expression (Price > 0) is evaluated for every INSERT and UPDATE. If it is false, SQL Server rejects the row."},
                                {"line": "CONSTRAINT CHK_Products_Category CHECK (Category IN ('Electronics', 'Clothing', 'Food', 'General'))", "meaning": "The IN operator in a CHECK constraint acts like a list of allowed values. Only these four strings can be stored in the Category column."},
                                {"line": "DEFAULT 0", "meaning": "If an INSERT does not provide a value for StockQty, SQL Server uses 0. This saves you from having to specify it every time."},
                                {"line": "CONSTRAINT FK_OrderItems_Orders FOREIGN KEY (OrderID) REFERENCES dbo.Orders(OrderID)", "meaning": "This means: the OrderID in OrderItems MUST exist in the OrderID column of dbo.Orders. You cannot add an order item for an order that does not exist."},
                                {"line": "ON DELETE CASCADE", "meaning": "If an Order row is deleted, all its OrderItems rows are AUTOMATICALLY deleted too. CASCADE propagates the delete."},
                                {"line": "ON DELETE NO ACTION", "meaning": "If you try to delete a Product that has OrderItems referencing it, SQL Server will BLOCK the delete and raise an error. This protects your order history."},
                                {"line": "ALTER TABLE dbo.Products ADD CONSTRAINT ...", "meaning": "You can add constraints to existing tables using ALTER TABLE. You don't have to DROP and recreate the whole table."}
                            ],
                            "ssms_steps": [
                                "Open SSMS and connect to your server",
                                "Open a New Query window",
                                "Run the Products table creation first (highlight just that section and press F5)",
                                "Run the OrderItems table creation next",
                                "Test the CHECK constraint: try inserting a product with Price = -500 — you should get an error message saying the CHECK constraint was violated",
                                "Try inserting a valid product — it should succeed",
                                "In Object Explorer, expand Tables → dbo.Products → Constraints to see all constraints listed",
                                "To view constraint definitions: right-click a constraint and select 'Script Constraint as → CREATE To → New Query Window'"
                            ],
                            "exam_tip": "ON DELETE CASCADE vs ON DELETE NO ACTION: CASCADE automatically deletes child rows; NO ACTION (the default) blocks the parent delete. Know these for the exam — questions often ask which cascading action preserves referential integrity while preventing orphaned records."
                        },
                        {
                            "type": "important",
                            "title": "Referential Integrity",
                            "body": "<strong>Referential integrity</strong> means that foreign key values in a child table must always match a primary key in the parent table. No orphaned records.\n\n<strong>Cascading actions:</strong>\n<ul><li><strong>NO ACTION</strong> (default) — Blocks the parent delete/update if children exist</li><li><strong>CASCADE</strong> — Automatically deletes/updates child rows when parent changes</li><li><strong>SET NULL</strong> — Sets child FK column to NULL when parent is deleted</li><li><strong>SET DEFAULT</strong> — Sets child FK column to its DEFAULT value when parent is deleted</li></ul>"
                        }
                    ],
                    "quiz": [
                        {
                            "q": "Which constraint ensures a column value satisfies a custom logical condition?",
                            "opts": ["A. UNIQUE", "B. FOREIGN KEY", "C. CHECK", "D. DEFAULT"],
                            "correct": "C",
                            "explain": "CHECK constraints validate that column values satisfy a specified Boolean expression. For example, CHECK (Price > 0) ensures prices are always positive."
                        },
                        {
                            "q": "What happens when ON DELETE CASCADE is specified on a FOREIGN KEY and the parent row is deleted?",
                            "opts": ["A. The delete is blocked", "B. The parent row is deleted but child rows remain (orphaned)", "C. Child rows are automatically deleted along with the parent", "D. Child FK columns are set to NULL"],
                            "correct": "C",
                            "explain": "ON DELETE CASCADE means when a parent row is deleted, all child rows referencing it are automatically deleted as well."
                        },
                        {
                            "q": "How do you add a CHECK constraint to an existing table?",
                            "opts": ["A. CREATE CONSTRAINT on the table", "B. ALTER TABLE ... ADD CONSTRAINT ... CHECK (...)", "C. UPDATE TABLE ... SET CONSTRAINT", "D. INSERT CONSTRAINT into the table"],
                            "correct": "B",
                            "explain": "ALTER TABLE is used to modify existing tables. The syntax ALTER TABLE TableName ADD CONSTRAINT ConstraintName CHECK (expression) adds a CHECK constraint without recreating the table."
                        },
                        {
                            "q": "Which cascading action on a FOREIGN KEY blocks deletion of a parent row if child rows exist?",
                            "opts": ["A. CASCADE", "B. SET NULL", "C. SET DEFAULT", "D. NO ACTION"],
                            "correct": "D",
                            "explain": "NO ACTION (the default if not specified) blocks the parent delete when child rows reference it, raising a foreign key violation error."
                        },
                        {
                            "q": "What is the difference between a PRIMARY KEY and a UNIQUE constraint?",
                            "opts": ["A. PRIMARY KEY allows NULLs; UNIQUE does not", "B. A table can have many PRIMARY KEYs but only one UNIQUE constraint", "C. PRIMARY KEY does not allow NULLs and there can be only one per table; UNIQUE allows one NULL and multiple can exist", "D. They are identical in behavior"],
                            "correct": "C",
                            "explain": "PRIMARY KEY: no NULLs, exactly one per table. UNIQUE: allows one NULL value, multiple UNIQUE constraints allowed per table. Both enforce distinctness."
                        }
                    ]
                },

                # ── Unit 7: Manage JSON columns and indexes ───────────
                {
                    "id": "lp1-m1-u7",
                    "title": "Manage JSON columns and indexes",
                    "description": "Learn to store JSON data in SQL Server columns and query it using JSON_VALUE, JSON_QUERY, and OPENJSON.",
                    "estimated_time": 25,
                    "objectives": [
                        "Store JSON data in NVARCHAR columns",
                        "Extract scalar values with JSON_VALUE",
                        "Extract JSON objects/arrays with JSON_QUERY",
                        "Shred JSON into rows using OPENJSON",
                        "Index JSON data with computed columns"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "JSON in SQL Server",
                            "body": "SQL Server does not have a native JSON data type. Instead, JSON is stored as <strong>NVARCHAR</strong> text. SQL Server provides built-in functions to parse and query that JSON text.\n\n<strong>Why store JSON in SQL?</strong>\n<ul><li>APIs and modern applications often send data as JSON</li><li>You might need to store flexible, schema-less attributes alongside structured data</li><li>Integration with NoSQL systems or REST APIs</li></ul>\n\n<strong>The three main JSON functions:</strong>\n<ul><li><strong>JSON_VALUE(json, path)</strong> — Extracts a single scalar value (string, number, boolean) from JSON. Returns NVARCHAR.</li><li><strong>JSON_QUERY(json, path)</strong> — Extracts a JSON object or array (returns JSON text, not a scalar)</li><li><strong>OPENJSON(json, path)</strong> — Shreds (unpacks) a JSON array into multiple rows — like turning JSON into a table</li></ul>\n\n<strong>JSON path syntax:</strong>\n<ul><li>Start with <strong>$</strong> (the root of the JSON document)</li><li>Use <strong>.property</strong> to access an object property: <code>$.name</code></li><li>Use <strong>[index]</strong> to access an array element: <code>$.tags[0]</code></li><li>Chain them: <code>$.address.city</code></li></ul>"
                        },
                        {
                            "type": "sql_block",
                            "title": "Working with JSON Data in SQL Server",
                            "scenario": "Your e-commerce system stores flexible product attributes as JSON (since different product categories have different attributes). You need to query and index this JSON data.",
                            "code": "-- ============================================================\n-- Setup: Products table with a JSON attributes column\n-- ============================================================\nCREATE TABLE dbo.ProductsJSON (\n    ProductID    INT           NOT NULL IDENTITY(1,1),\n    ProductName  NVARCHAR(100) NOT NULL,\n    Attributes   NVARCHAR(MAX) NULL,  -- JSON stored as NVARCHAR\n    CONSTRAINT PK_ProductsJSON PRIMARY KEY (ProductID)\n);\nGO\n\n-- Insert products with JSON attributes\nINSERT INTO dbo.ProductsJSON (ProductName, Attributes) VALUES\n('Laptop Pro 15', '{\n    \"brand\": \"TechCorp\",\n    \"specs\": {\n        \"ram\": 16,\n        \"storage\": 512,\n        \"cpu\": \"Intel i7\"\n    },\n    \"tags\": [\"portable\", \"business\", \"fast\"],\n    \"inStock\": true,\n    \"price\": 1299.99\n}'),\n('Budget Phone', '{\n    \"brand\": \"PhoneCo\",\n    \"specs\": {\n        \"ram\": 4,\n        \"storage\": 64,\n        \"cpu\": \"ARM Cortex\"\n    },\n    \"tags\": [\"mobile\", \"budget\"],\n    \"inStock\": false,\n    \"price\": 199.99\n}');\nGO\n\n-- ============================================================\n-- 1. JSON_VALUE: Extract a single scalar value\n-- ============================================================\nSELECT \n    ProductName,\n    JSON_VALUE(Attributes, '$.brand')          AS Brand,\n    JSON_VALUE(Attributes, '$.specs.ram')      AS RAM_GB,\n    JSON_VALUE(Attributes, '$.price')          AS Price,\n    JSON_VALUE(Attributes, '$.tags[0]')        AS FirstTag\nFROM dbo.ProductsJSON;\nGO\n\n-- ============================================================\n-- 2. JSON_QUERY: Extract a JSON object or array\n-- ============================================================\nSELECT \n    ProductName,\n    JSON_QUERY(Attributes, '$.specs')   AS SpecsObject,  -- Returns JSON\n    JSON_QUERY(Attributes, '$.tags')    AS TagsArray     -- Returns JSON array\nFROM dbo.ProductsJSON;\nGO\n\n-- ============================================================\n-- 3. OPENJSON: Shred JSON array into rows\n-- ============================================================\nSELECT \n    p.ProductName,\n    tag.value AS Tag\nFROM dbo.ProductsJSON p\nCROSS APPLY OPENJSON(p.Attributes, '$.tags') AS tag;\nGO\n\n-- ============================================================\n-- 4. OPENJSON with explicit schema (WITH clause)\n-- ============================================================\nSELECT \n    p.ProductName,\n    j.Brand,\n    j.RAM,\n    j.Price\nFROM dbo.ProductsJSON p\nCROSS APPLY OPENJSON(p.Attributes)\nWITH (\n    Brand   NVARCHAR(50)   '$.brand',\n    RAM     INT            '$.specs.ram',\n    Price   DECIMAL(10,2)  '$.price'\n) AS j;\nGO\n\n-- ============================================================\n-- 5. Index JSON data using a computed column\n-- ============================================================\n-- Add a computed column that extracts the brand\nALTER TABLE dbo.ProductsJSON\nADD Brand AS JSON_VALUE(Attributes, '$.brand');\n\n-- Create an index on the computed column\nCREATE NONCLUSTERED INDEX IX_ProductsJSON_Brand\n    ON dbo.ProductsJSON (Brand);\n\n-- Now this query can use the index:\nSELECT ProductName FROM dbo.ProductsJSON\nWHERE JSON_VALUE(Attributes, '$.brand') = 'TechCorp';",
                            "explanation": "Covers all four JSON techniques: JSON_VALUE for scalar extraction, JSON_QUERY for objects/arrays, OPENJSON for shredding, and indexing JSON via computed columns.",
                            "purpose": "Query and index JSON stored in SQL Server NVARCHAR columns",
                            "breakdown": [
                                {"line": "Attributes NVARCHAR(MAX) NULL", "meaning": "JSON is stored as NVARCHAR text. MAX allows up to 2GB of text — use this for JSON that might be large. NVARCHAR because JSON can contain Unicode characters."},
                                {"line": "JSON_VALUE(Attributes, '$.brand')", "meaning": "$ is the root of the JSON document. .brand accesses the 'brand' property. Returns a scalar value (a single string or number)."},
                                {"line": "JSON_VALUE(Attributes, '$.specs.ram')", "meaning": "Chains into a nested object. $.specs gets the specs object, then .ram gets the ram property within it."},
                                {"line": "JSON_VALUE(Attributes, '$.tags[0]')", "meaning": "[0] accesses the first element of the tags array (arrays are zero-indexed in JSON path)."},
                                {"line": "JSON_QUERY(Attributes, '$.specs')", "meaning": "Returns the entire specs object as a JSON string, not a scalar. Use JSON_QUERY when the result is an object or array."},
                                {"line": "CROSS APPLY OPENJSON(p.Attributes, '$.tags') AS tag", "meaning": "CROSS APPLY calls OPENJSON for each row in ProductsJSON. OPENJSON expands the tags array into multiple rows. Each tag becomes its own row."},
                                {"line": "OPENJSON(p.Attributes) WITH (Brand NVARCHAR(50) '$.brand', ...)", "meaning": "The WITH clause gives OPENJSON an explicit schema — you define column names, types, and JSON paths. This returns a strongly typed result set."},
                                {"line": "ADD Brand AS JSON_VALUE(Attributes, '$.brand')", "meaning": "Creates a computed column that automatically extracts the brand from JSON every time a row is accessed. Computed columns can be indexed."},
                                {"line": "CREATE NONCLUSTERED INDEX IX_ProductsJSON_Brand ON dbo.ProductsJSON (Brand)", "meaning": "Indexes the computed column. Now WHERE JSON_VALUE(Attributes, '$.brand') = 'X' can use this index efficiently."}
                            ],
                            "ssms_steps": [
                                "Open SSMS and connect to your server",
                                "Open a New Query window and select your database",
                                "Run the CREATE TABLE section first (highlight and F5)",
                                "Run the INSERT section to add sample data",
                                "Run each SELECT section one at a time — highlight one block and press F5",
                                "Observe the results: JSON_VALUE returns plain strings/numbers; JSON_QUERY returns JSON text",
                                "For OPENJSON: notice how one product row becomes multiple rows (one per tag)",
                                "Run the ALTER TABLE and CREATE INDEX sections to add the computed column and index",
                                "Run the final SELECT with WHERE clause — press Ctrl+M before running to see the execution plan and verify it uses the index"
                            ],
                            "exam_tip": "JSON_VALUE returns a scalar (string/number). JSON_QUERY returns a JSON fragment (object or array). If you call JSON_VALUE on an object/array path, it returns NULL. If you call JSON_QUERY on a scalar path, it returns NULL. Know which function returns what."
                        },
                        {
                            "type": "important",
                            "title": "ISJSON — Validate JSON Before Querying",
                            "body": "Before running JSON functions on a column, you can validate the JSON is well-formed:\n<br><br><code>SELECT * FROM dbo.ProductsJSON WHERE ISJSON(Attributes) = 1;</code>\n<br><br>ISJSON returns 1 if the string is valid JSON, 0 if not. Use this to find corrupted JSON rows. You can also use it in a CHECK constraint: <code>CONSTRAINT CHK_ValidJSON CHECK (ISJSON(Attributes) = 1)</code>"
                        }
                    ],
                    "quiz": [
                        {
                            "q": "Which function extracts a single scalar value (like a string or number) from a JSON column?",
                            "opts": ["A. JSON_QUERY", "B. OPENJSON", "C. JSON_VALUE", "D. JSON_EXTRACT"],
                            "correct": "C",
                            "explain": "JSON_VALUE extracts a single scalar value from a JSON string. For objects or arrays, use JSON_QUERY instead."
                        },
                        {
                            "q": "What does the $ symbol represent in a JSON path expression?",
                            "opts": ["A. A variable name", "B. The root of the JSON document", "C. An array index", "D. A string delimiter"],
                            "correct": "B",
                            "explain": "In JSON path syntax, $ represents the root of the JSON document. All paths start from $ and navigate down using dots and brackets."
                        },
                        {
                            "q": "What does OPENJSON do when applied to a JSON array?",
                            "opts": ["A. Returns the array as a single string", "B. Counts the elements in the array", "C. Shreds the array into multiple rows, one per element", "D. Converts the array to a comma-separated string"],
                            "correct": "C",
                            "explain": "OPENJSON transforms (shreds) a JSON array into a relational result set — each array element becomes its own row. This is used with CROSS APPLY to expand JSON arrays."
                        },
                        {
                            "q": "How do you efficiently index data stored inside a JSON column?",
                            "opts": ["A. Create an index directly on the NVARCHAR column", "B. Add a computed column using JSON_VALUE, then index the computed column", "C. JSON data cannot be indexed in SQL Server", "D. Use a FULLTEXT index on the JSON column"],
                            "correct": "B",
                            "explain": "Create a computed column using JSON_VALUE to extract the JSON property, then create a nonclustered index on that computed column. Queries using JSON_VALUE on that same path can then use the index."
                        },
                        {
                            "q": "What data type should you use to store JSON in SQL Server?",
                            "opts": ["A. JSON (native type)", "B. XML", "C. VARCHAR(MAX) or NVARCHAR(MAX)", "D. VARBINARY(MAX)"],
                            "correct": "C",
                            "explain": "SQL Server has no native JSON type. JSON is stored as NVARCHAR(MAX) (or VARCHAR(MAX) for ASCII-only JSON). NVARCHAR is preferred as JSON can contain Unicode characters."
                        }
                    ]
                },

                # ── Unit 8: Partition tables for scale ───────────────
                {
                    "id": "lp1-m1-u8",
                    "title": "Partition tables for scale",
                    "description": "Learn to partition large tables using partition functions and schemes to improve query performance and manageability.",
                    "estimated_time": 25,
                    "objectives": [
                        "Understand why and when to partition tables",
                        "Create a partition function to define range boundaries",
                        "Create a partition scheme to map partitions to filegroups",
                        "Create a partitioned table"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "What is Table Partitioning?",
                            "body": "When a table has hundreds of millions of rows, even indexed queries can be slow. <strong>Table partitioning</strong> is a technique to split a large table into smaller, more manageable pieces called <strong>partitions</strong>.\n\nPhysically, the table looks like one table to the application — queries use the same T-SQL. But behind the scenes, SQL Server stores the data in different file groups based on partition boundaries.\n\n<strong>How it works:</strong>\n<ol><li>You define a <strong>Partition Function</strong> — this defines the boundary values (e.g., split by year)</li><li>You define a <strong>Partition Scheme</strong> — this maps each partition to a filegroup (storage location)</li><li>You create the <strong>Table</strong> on the partition scheme</li></ol>\n\n<strong>Benefits of partitioning:</strong>\n<ul><li><strong>Partition elimination</strong> — When you query with a WHERE on the partition column, SQL Server only reads the relevant partitions (e.g., WHERE Year = 2024 only reads the 2024 partition)</li><li><strong>Maintenance</strong> — You can archive old data by switching out a partition in seconds instead of deleting millions of rows</li><li><strong>Parallel processing</strong> — SQL Server can process multiple partitions simultaneously</li></ul>\n\n<strong>Best partition columns:</strong>\n<ul><li>Date columns (year, month) — most common use case</li><li>Columns you frequently filter on in WHERE clauses</li><li>Columns with naturally sequential or range-based values</li></ul>"
                        },
                        {
                            "type": "sql_block",
                            "title": "Creating a Partitioned Sales Table by Year",
                            "scenario": "Your SalesOrders table has grown to 500 million rows. You want to partition it by year so queries for a specific year only scan that year's data.",
                            "code": "-- ============================================================\n-- Step 1: Create a Partition Function\n-- Defines the boundary points (values where partitions split)\n-- ============================================================\nCREATE PARTITION FUNCTION PF_SalesByYear (DATE)\nAS RANGE RIGHT FOR VALUES ('2022-01-01', '2023-01-01', '2024-01-01', '2025-01-01');\nGO\n\n-- This creates 5 partitions:\n-- Partition 1: OrderDate < '2022-01-01'   (before 2022)\n-- Partition 2: '2022-01-01' <= OrderDate < '2023-01-01'  (year 2022)\n-- Partition 3: '2023-01-01' <= OrderDate < '2024-01-01'  (year 2023)\n-- Partition 4: '2024-01-01' <= OrderDate < '2025-01-01'  (year 2024)\n-- Partition 5: OrderDate >= '2025-01-01'  (2025 and beyond)\n\n-- ============================================================\n-- Step 2: Create a Partition Scheme\n-- Maps each partition to a filegroup\n-- ============================================================\nCREATE PARTITION SCHEME PS_SalesByYear\nAS PARTITION PF_SalesByYear\nTO ([PRIMARY], [PRIMARY], [PRIMARY], [PRIMARY], [PRIMARY]);\n-- In production: use different filegroups for each year\n-- TO ([FG_Archive], [FG_2022], [FG_2023], [FG_2024], [FG_Current])\nGO\n\n-- ============================================================\n-- Step 3: Create the Partitioned Table\n-- Use ON PartitionSchemeName(PartitionColumn)\n-- ============================================================\nCREATE TABLE dbo.SalesOrders (\n    OrderID      INT            NOT NULL IDENTITY(1,1),\n    CustomerID   INT            NOT NULL,\n    OrderDate    DATE           NOT NULL,\n    TotalAmount  DECIMAL(10,2)  NOT NULL,\n    Status       VARCHAR(20)    NOT NULL DEFAULT 'Pending',\n    CONSTRAINT PK_SalesOrders \n        PRIMARY KEY NONCLUSTERED (OrderID)\n)\nON PS_SalesByYear(OrderDate);  -- Partition by OrderDate\nGO\n\n-- ============================================================\n-- Step 4: Check partition information\n-- ============================================================\nSELECT \n    partition_number,\n    rows AS RowCount\nFROM sys.partitions\nWHERE object_id = OBJECT_ID('dbo.SalesOrders')\nORDER BY partition_number;\n\n-- See which partition a specific date falls into:\nSELECT $PARTITION.PF_SalesByYear('2023-06-15') AS PartitionNumber;\n-- Returns: 3 (the 2023 partition)",
                            "explanation": "Shows the three-step process to partition a table: create a partition function (boundaries), create a partition scheme (filegroup mapping), then create the table on that scheme.",
                            "purpose": "Partition a large table by date to improve query performance",
                            "breakdown": [
                                {"line": "CREATE PARTITION FUNCTION PF_SalesByYear (DATE)", "meaning": "Creates a partition function that works on DATE values. The function defines where the splits happen."},
                                {"line": "AS RANGE RIGHT FOR VALUES ('2022-01-01', '2023-01-01', ...)", "meaning": "RANGE RIGHT means boundary values belong to the RIGHT (higher) partition. So '2022-01-01' goes into the 2022 partition, not the pre-2022 partition. RANGE LEFT would put boundary values in the LEFT (lower) partition."},
                                {"line": "CREATE PARTITION SCHEME PS_SalesByYear AS PARTITION PF_SalesByYear", "meaning": "Creates a partition scheme that uses our partition function. The scheme maps partitions to physical filegroups."},
                                {"line": "TO ([PRIMARY], [PRIMARY], [PRIMARY], [PRIMARY], [PRIMARY])", "meaning": "Maps all 5 partitions to the PRIMARY filegroup. In production you would use different filegroups — one per year — so you can put archived data on slower, cheaper storage."},
                                {"line": "ON PS_SalesByYear(OrderDate)", "meaning": "This is the key part — it tells SQL Server to use the PS_SalesByYear partition scheme and to partition the data based on the OrderDate column."},
                                {"line": "PRIMARY KEY NONCLUSTERED (OrderID)", "meaning": "When using partitioning, the primary key must be NONCLUSTERED if the partition column (OrderDate) is not part of the key. The partition column drives the clustered organization."},
                                {"line": "$PARTITION.PF_SalesByYear('2023-06-15')", "meaning": "A special function to test which partition a value belongs to. Useful for debugging and verifying your partition function works as expected."}
                            ],
                            "ssms_steps": [
                                "Open SSMS and connect to your server",
                                "Open a New Query window and select your target database",
                                "Run Step 1 (CREATE PARTITION FUNCTION) — check Messages tab for success",
                                "Run Step 2 (CREATE PARTITION SCHEME) — check Messages tab for success",
                                "Run Step 3 (CREATE TABLE ... ON PS_SalesByYear) — this creates the partitioned table",
                                "Run the $PARTITION test: SELECT $PARTITION.PF_SalesByYear('2023-06-15') — should return 3",
                                "Insert some test rows with different OrderDate values",
                                "Run Step 4 (sys.partitions query) to see row counts per partition",
                                "In Object Explorer: Tables → dbo.SalesOrders → Storage → Partitions to see partition info visually"
                            ],
                            "exam_tip": "RANGE RIGHT vs RANGE LEFT: With RANGE RIGHT, boundary values go to the right (higher) partition. With RANGE LEFT, boundary values go to the left (lower) partition. The exam may test this. For date partitioning, RANGE RIGHT is most natural: '2023-01-01' belongs to the 2023 partition."
                        },
                        {
                            "type": "important",
                            "title": "Partition Elimination",
                            "body": "<strong>Partition elimination</strong> is the main performance benefit of partitioning. When you write:\n<br><code>SELECT * FROM dbo.SalesOrders WHERE OrderDate BETWEEN '2024-01-01' AND '2024-12-31'</code>\n<br><br>SQL Server knows to only look at Partition 4 (the 2024 partition) and completely skip the other partitions. This can turn a query that used to scan 500 million rows into one that scans only 100 million rows in the 2024 partition.\n\n<strong>For partition elimination to work:</strong> Your WHERE clause must filter on the <em>partition column</em> (the column used in the partition function)."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What is the correct order of steps to create a partitioned table?",
                            "opts": ["A. Create table → Create partition scheme → Create partition function", "B. Create partition function → Create partition scheme → Create table", "C. Create partition scheme → Create partition function → Create table", "D. Create table → Create partition function → Create partition scheme"],
                            "correct": "B",
                            "explain": "The correct order is: 1) CREATE PARTITION FUNCTION (defines boundaries), 2) CREATE PARTITION SCHEME (maps partitions to filegroups), 3) CREATE TABLE ... ON PartitionScheme(Column)."
                        },
                        {
                            "q": "What does RANGE RIGHT mean in a partition function?",
                            "opts": ["A. Data is partitioned from right to left", "B. Boundary values belong to the right (higher) partition", "C. The rightmost partition is used by default", "D. NULL values go to the rightmost partition"],
                            "correct": "B",
                            "explain": "RANGE RIGHT means boundary values are included in the right (higher-value) partition. So if a boundary is '2023-01-01', that date falls in the 2023 partition, not the 2022 partition."
                        },
                        {
                            "q": "What is 'partition elimination'?",
                            "opts": ["A. Dropping partitions that are no longer needed", "B. SQL Server automatically skipping irrelevant partitions when filtering on the partition column", "C. Merging small partitions together", "D. Removing the partition scheme from a table"],
                            "correct": "B",
                            "explain": "Partition elimination is when SQL Server recognizes that a WHERE clause on the partition column means only certain partitions need to be scanned, skipping all others."
                        },
                        {
                            "q": "How many partitions does a partition function with 4 boundary values create?",
                            "opts": ["A. 4", "B. 3", "C. 5", "D. 6"],
                            "correct": "C",
                            "explain": "N boundary values create N+1 partitions. 4 boundary values create 5 partitions: one below the first boundary, one between each pair of boundaries, and one above the last boundary."
                        },
                        {
                            "q": "What T-SQL function tests which partition a specific value falls into?",
                            "opts": ["A. PARTITION_NUMBER()", "B. GET_PARTITION()", "C. $PARTITION.FunctionName(value)", "D. FIND_PARTITION()"],
                            "correct": "C",
                            "explain": "$PARTITION.PartitionFunctionName(value) returns the partition number for a given value. For example: SELECT $PARTITION.PF_SalesByYear('2023-06-15') returns 3."
                        }
                    ]
                },

                # ── Unit 9: Exercise ──────────────────────────────────
                {
                    "id": "lp1-m1-u9",
                    "title": "Exercise",
                    "description": "Practice creating a complete database schema with tables, indexes, constraints, and JSON columns.",
                    "estimated_time": 30,
                    "objectives": [
                        "Apply all Module 1 concepts in a single comprehensive exercise",
                        "Design a real-world schema from scratch",
                        "Troubleshoot constraint violations and index issues"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Exercise Scenario",
                            "body": "In this exercise, you will build a complete <strong>Library Management System</strong> database schema. A library needs to track:\n<ul><li><strong>Books</strong> — with ISBN, title, author, genre, price</li><li><strong>Members</strong> — with member ID, name, email, membership type</li><li><strong>Loans</strong> — which member borrowed which book and when</li><li><strong>BookExtras</strong> — flexible metadata about books stored as JSON</li></ul>\n\nYou will apply: correct data types, NOT NULL/NULL choices, PRIMARY KEY, FOREIGN KEY, CHECK and DEFAULT constraints, nonclustered indexes, and JSON querying."
                        },
                        {
                            "type": "sql_block",
                            "title": "Library Management System — Complete Schema",
                            "scenario": "Build a library database from scratch applying all Module 1 concepts.",
                            "code": "-- ============================================================\n-- Exercise: Library Management System\n-- ============================================================\n\nCREATE DATABASE LibraryDB;\nGO\nUSE LibraryDB;\nGO\n\n-- Table 1: Books\nCREATE TABLE dbo.Books (\n    BookID       INT            NOT NULL IDENTITY(1,1),\n    ISBN         VARCHAR(13)    NOT NULL,\n    Title        NVARCHAR(200)  NOT NULL,\n    Author       NVARCHAR(100)  NOT NULL,\n    Genre        VARCHAR(50)    NOT NULL DEFAULT 'General',\n    Price        DECIMAL(8,2)   NOT NULL,\n    PublishedYear INT           NULL,\n    IsAvailable  BIT            NOT NULL DEFAULT 1,\n    Metadata     NVARCHAR(MAX)  NULL,   -- JSON column\n    \n    CONSTRAINT PK_Books PRIMARY KEY (BookID),\n    CONSTRAINT UQ_Books_ISBN UNIQUE (ISBN),\n    CONSTRAINT CHK_Books_Price CHECK (Price > 0),\n    CONSTRAINT CHK_Books_Year CHECK (PublishedYear IS NULL OR PublishedYear BETWEEN 1000 AND 2100),\n    CONSTRAINT CHK_Books_Genre CHECK (Genre IN ('Fiction', 'Non-Fiction', 'Science', 'History', 'Technology', 'General')),\n    CONSTRAINT CHK_Books_Metadata CHECK (Metadata IS NULL OR ISJSON(Metadata) = 1)\n);\nGO\n\n-- Table 2: Members\nCREATE TABLE dbo.Members (\n    MemberID         INT           NOT NULL IDENTITY(1,1),\n    FirstName        NVARCHAR(50)  NOT NULL,\n    LastName         NVARCHAR(50)  NOT NULL,\n    Email            VARCHAR(100)  NOT NULL,\n    MembershipType   VARCHAR(20)   NOT NULL DEFAULT 'Standard',\n    JoinDate         DATE          NOT NULL DEFAULT GETDATE(),\n    MaxLoans         INT           NOT NULL DEFAULT 3,\n    \n    CONSTRAINT PK_Members PRIMARY KEY (MemberID),\n    CONSTRAINT UQ_Members_Email UNIQUE (Email),\n    CONSTRAINT CHK_Members_MembershipType CHECK (MembershipType IN ('Standard', 'Premium', 'Student')),\n    CONSTRAINT CHK_Members_MaxLoans CHECK (MaxLoans BETWEEN 1 AND 10)\n);\nGO\n\n-- Table 3: Loans\nCREATE TABLE dbo.Loans (\n    LoanID       INT   NOT NULL IDENTITY(1,1),\n    BookID       INT   NOT NULL,\n    MemberID     INT   NOT NULL,\n    LoanDate     DATE  NOT NULL DEFAULT GETDATE(),\n    DueDate      DATE  NOT NULL,\n    ReturnDate   DATE  NULL,    -- NULL means not returned yet\n    \n    CONSTRAINT PK_Loans PRIMARY KEY (LoanID),\n    CONSTRAINT FK_Loans_Books   FOREIGN KEY (BookID)   REFERENCES dbo.Books(BookID)   ON DELETE NO ACTION,\n    CONSTRAINT FK_Loans_Members FOREIGN KEY (MemberID) REFERENCES dbo.Members(MemberID) ON DELETE NO ACTION,\n    CONSTRAINT CHK_Loans_DueDate CHECK (DueDate > LoanDate),\n    CONSTRAINT CHK_Loans_ReturnDate CHECK (ReturnDate IS NULL OR ReturnDate >= LoanDate)\n);\nGO\n\n-- Indexes for common queries\nCREATE NONCLUSTERED INDEX IX_Loans_BookID   ON dbo.Loans(BookID);\nCREATE NONCLUSTERED INDEX IX_Loans_MemberID ON dbo.Loans(MemberID);\nCREATE NONCLUSTERED INDEX IX_Books_Author   ON dbo.Books(Author);\nCREATE NONCLUSTERED INDEX IX_Books_Genre    ON dbo.Books(Genre);\nGO\n\n-- Insert sample data\nINSERT INTO dbo.Books (ISBN, Title, Author, Genre, Price, PublishedYear, Metadata)\nVALUES\n('9780143127550', 'Sapiens', 'Yuval Noah Harari', 'History', 15.99, 2011,\n '{\"pages\": 443, \"language\": \"English\", \"awards\": [\"National Book Award\"], \"rating\": 4.4}'),\n('9780307474728', 'The Road', 'Cormac McCarthy', 'Fiction', 12.99, 2006,\n '{\"pages\": 287, \"language\": \"English\", \"awards\": [\"Pulitzer Prize\"], \"rating\": 4.1}');\n\nINSERT INTO dbo.Members (FirstName, LastName, Email, MembershipType)\nVALUES\n('Alice', 'Johnson', 'alice@email.com', 'Premium'),\n('Bob',   'Smith',   'bob@email.com',   'Standard');\n\nINSERT INTO dbo.Loans (BookID, MemberID, LoanDate, DueDate)\nVALUES (1, 1, '2024-01-10', '2024-01-24');\nGO\n\n-- Query: Active loans with book and member details\nSELECT \n    l.LoanID,\n    b.Title,\n    b.Author,\n    m.FirstName + ' ' + m.LastName AS MemberName,\n    l.LoanDate,\n    l.DueDate,\n    JSON_VALUE(b.Metadata, '$.rating') AS BookRating\nFROM dbo.Loans l\nJOIN dbo.Books   b ON l.BookID   = b.BookID\nJOIN dbo.Members m ON l.MemberID = m.MemberID\nWHERE l.ReturnDate IS NULL\nORDER BY l.DueDate;",
                            "explanation": "A complete real-world schema applying all Module 1 concepts: data types, nullability, constraints, foreign keys, indexes, and JSON.",
                            "purpose": "Hands-on practice building a complete database schema",
                            "breakdown": [
                                {"line": "CONSTRAINT CHK_Books_Metadata CHECK (Metadata IS NULL OR ISJSON(Metadata) = 1)", "meaning": "A CHECK constraint using ISJSON ensures that if the Metadata column has a value, it must be valid JSON. NULL is allowed (the book has no extra metadata)."},
                                {"line": "CONSTRAINT CHK_Loans_DueDate CHECK (DueDate > LoanDate)", "meaning": "Ensures the due date is always after the loan date — you can't return something before you borrowed it."},
                                {"line": "ReturnDate DATE NULL", "meaning": "NULL means the book hasn't been returned yet. This is a common pattern: a NULL in a date column means 'event hasn't happened yet'."},
                                {"line": "JOIN dbo.Books b ON l.BookID = b.BookID", "meaning": "Uses the foreign key relationship. Because BookID is indexed on both tables, this JOIN is efficient."},
                                {"line": "WHERE l.ReturnDate IS NULL", "meaning": "Filters for active loans only. IS NULL is required for NULL comparisons — you cannot write ReturnDate = NULL."}
                            ],
                            "ssms_steps": [
                                "Open SSMS and connect to your server",
                                "Open a New Query window connected to your server (not a specific database)",
                                "Run CREATE DATABASE and USE LibraryDB first",
                                "Run each CREATE TABLE statement one at a time to catch any errors",
                                "Run the CREATE INDEX statements",
                                "Test constraints: Try inserting a book with Price = -5 (should fail with CHECK constraint error)",
                                "Try inserting a loan with a BookID that doesn't exist in Books (should fail with FOREIGN KEY error)",
                                "Run the final SELECT query to see active loans",
                                "Challenge: Add a new column ExpiryDate to Members using ALTER TABLE"
                            ],
                            "exam_tip": "The CHECK constraint ISJSON(column) = 1 validates JSON at the database level. The pattern 'NULL or valid value' using IS NULL OR condition is very common in CHECK constraints for optional columns."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "In the library exercise, why is ReturnDate defined as NULL?",
                            "opts": ["A. Because dates cannot be NOT NULL", "B. Because NULL indicates the book has not been returned yet", "C. Because ReturnDate is not needed", "D. To save storage space"],
                            "correct": "B",
                            "explain": "NULL in ReturnDate means the loan is still active (book not returned). This is a common design pattern: NULL = event hasn't occurred yet. When the book is returned, ReturnDate is updated to the actual return date."
                        },
                        {
                            "q": "What does CHECK (DueDate > LoanDate) enforce?",
                            "opts": ["A. LoanDate must be greater than DueDate", "B. Both dates must equal each other", "C. DueDate must always be after LoanDate", "D. LoanDate cannot be NULL"],
                            "correct": "C",
                            "explain": "This CHECK constraint ensures data integrity by preventing impossible dates — a due date must logically come after the loan date."
                        },
                        {
                            "q": "Why is an index created on Loans.BookID?",
                            "opts": ["A. Because BookID is the primary key of Loans", "B. Because BookID is a foreign key used in JOINs, and indexes speed up JOIN operations", "C. To enforce the UNIQUE constraint on BookID", "D. SQL Server requires indexes on all columns"],
                            "correct": "B",
                            "explain": "Foreign key columns are excellent candidates for nonclustered indexes because they are used in JOIN operations. Without an index, SQL Server must scan the entire Loans table to find rows matching a given BookID."
                        },
                        {
                            "q": "What SQL keyword is required when comparing a column to NULL?",
                            "opts": ["A. = NULL", "B. EQUALS NULL", "C. IS NULL", "D. LIKE NULL"],
                            "correct": "C",
                            "explain": "You must use IS NULL (or IS NOT NULL) to check for NULL values. The expression column = NULL always evaluates to UNKNOWN (not TRUE or FALSE), so it never returns any rows."
                        },
                        {
                            "q": "In the exercise schema, what would happen if you tried to delete a Book row that has active Loans?",
                            "opts": ["A. The Loan rows would be deleted automatically (CASCADE)", "B. The Loan rows would have BookID set to NULL", "C. SQL Server would block the delete and raise an error", "D. The Book row would be deleted and Loan rows would remain with orphaned BookIDs"],
                            "correct": "C",
                            "explain": "The FK_Loans_Books constraint uses ON DELETE NO ACTION, which blocks any deletion of a Book that has referencing Loan rows. This protects data integrity."
                        }
                    ]
                },

                # ── Unit 10: Module assessment ────────────────────────
                {
                    "id": "lp1-m1-u10",
                    "title": "Module assessment",
                    "description": "Test your knowledge of database object design with a comprehensive assessment.",
                    "estimated_time": 20,
                    "objectives": [
                        "Demonstrate understanding of all Module 1 topics",
                        "Apply knowledge to scenario-based questions"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Module 1 Key Concepts Review",
                            "body": "<strong>Platform Choices:</strong> SQL on Azure VM (IaaS) vs Managed Instance/SQL Database (PaaS). Managed Instance = near-100% SQL Server compatibility. Azure SQL DB = cloud-native, most managed.\n\n<strong>Table Design:</strong> Choose data types carefully (DECIMAL for money, NVARCHAR for Unicode, DATETIME2 for timestamps). Always explicit about NULL/NOT NULL.\n\n<strong>Indexes:</strong> One clustered per table (default = PK). Up to 999 nonclustered. INCLUDE columns create covering indexes. Index Seek = good, Table Scan = bad.\n\n<strong>Specialized Tables:</strong> #temp for large intermediate sets; @table for small batches; memory-optimized for ultra-high throughput.\n\n<strong>Constraints:</strong> PRIMARY KEY (unique, not null, one per table), UNIQUE (distinct, allows 1 NULL), FOREIGN KEY (referential integrity + cascading actions), CHECK (business rules), DEFAULT (fallback values).\n\n<strong>JSON:</strong> Stored as NVARCHAR. JSON_VALUE = scalar, JSON_QUERY = object/array, OPENJSON = shred to rows. Index via computed columns.\n\n<strong>Partitioning:</strong> Partition Function → Partition Scheme → Table ON scheme(column). RANGE RIGHT/LEFT. Partition elimination speeds up range queries."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "You need to store customer review text that may contain emoji and special characters from any language. Which data type is most appropriate?",
                            "opts": ["A. VARCHAR(MAX)", "B. NVARCHAR(MAX)", "C. TEXT", "D. CHAR(MAX)"],
                            "correct": "B",
                            "explain": "NVARCHAR stores Unicode characters, supporting all languages and emoji. VARCHAR is limited to the database collation's character set and cannot store all Unicode characters."
                        },
                        {
                            "q": "A table already has a clustered index on OrderID. You want to add another clustered index on OrderDate. What happens?",
                            "opts": ["A. SQL Server creates a second clustered index successfully", "B. SQL Server converts the existing clustered index to nonclustered automatically", "C. SQL Server raises an error — only one clustered index is allowed per table", "D. The existing clustered index is dropped and replaced"],
                            "correct": "C",
                            "explain": "SQL Server only allows one clustered index per table. Attempting to create a second clustered index raises an error. You can create a nonclustered index on OrderDate instead."
                        },
                        {
                            "q": "Which JSON function would you use to extract the 'city' value from: {\"address\": {\"city\": \"Seattle\", \"zip\": \"98101\"}}?",
                            "opts": ["A. JSON_QUERY(col, '$.address')", "B. JSON_VALUE(col, '$.address.city')", "C. OPENJSON(col, '$.city')", "D. JSON_VALUE(col, '$.city')"],
                            "correct": "B",
                            "explain": "JSON_VALUE with path '$.address.city' navigates into the address object and extracts the city scalar value. JSON_QUERY would return the entire address object, not just the city."
                        },
                        {
                            "q": "A table has 5 boundary values in its partition function. How many partitions does this create?",
                            "opts": ["A. 4", "B. 5", "C. 6", "D. 10"],
                            "correct": "C",
                            "explain": "N boundary values always create N+1 partitions. 5 boundaries create 6 partitions: one below boundary 1, one between each consecutive pair, and one above the last boundary."
                        },
                        {
                            "q": "Which cascading action on a FOREIGN KEY automatically sets child rows' FK column to NULL when the parent is deleted?",
                            "opts": ["A. ON DELETE CASCADE", "B. ON DELETE NO ACTION", "C. ON DELETE SET NULL", "D. ON DELETE SET DEFAULT"],
                            "correct": "C",
                            "explain": "ON DELETE SET NULL automatically sets the foreign key column in child rows to NULL when the referenced parent row is deleted. The child rows remain in the table with a NULL FK value."
                        }
                    ]
                },

                # ── Unit 11: Summary ──────────────────────────────────
                {
                    "id": "lp1-m1-u11",
                    "title": "Summary",
                    "description": "Review of all key concepts covered in Module 1.",
                    "estimated_time": 5,
                    "objectives": [
                        "Recap all Module 1 topics",
                        "Identify key exam points"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Module 1 Summary",
                            "body": "<strong>What you learned in this module:</strong>\n\n<ul><li><strong>Platform choices:</strong> SQL on Azure VM = IaaS (you manage OS). Azure SQL Managed Instance and Azure SQL Database = PaaS (Microsoft manages infrastructure). Choose Managed Instance for lift-and-shift migrations; Azure SQL DB for new cloud-native apps.</li>\n\n<li><strong>Building tables:</strong> Use INT for IDs, DECIMAL(p,s) for money, NVARCHAR for Unicode text, DATETIME2 for timestamps, BIT for booleans. IDENTITY(seed,increment) auto-numbers rows. Always specify NULL/NOT NULL explicitly.</li>\n\n<li><strong>Indexes:</strong> Clustered index determines physical row order — one per table, created automatically by PRIMARY KEY. Nonclustered indexes are separate lookup structures — up to 999 per table. INCLUDE columns create covering indexes. Index Seek is efficient; Table Scan is not.</li>\n\n<li><strong>Specialized tables:</strong> #temp in tempdb, session-scoped, supports indexes. @table variable, batch-scoped, limited statistics. Memory-optimized tables for extreme throughput.</li>\n\n<li><strong>Constraints:</strong> PRIMARY KEY (one, no nulls), UNIQUE (multiple, allows one null), FOREIGN KEY (referential integrity), CHECK (business rules), DEFAULT (fallback values). Cascading actions: CASCADE, NO ACTION, SET NULL, SET DEFAULT.</li>\n\n<li><strong>JSON:</strong> Stored as NVARCHAR(MAX). JSON_VALUE = scalar. JSON_QUERY = object/array. OPENJSON = rows. ISJSON validates. Index via computed column + nonclustered index.</li>\n\n<li><strong>Partitioning:</strong> CREATE PARTITION FUNCTION → CREATE PARTITION SCHEME → CREATE TABLE ON scheme(column). RANGE RIGHT puts boundary values in the right partition. Partition elimination speeds up range queries on the partition column.</li></ul>"
                        },
                        {
                            "type": "tip",
                            "title": "Top Exam Tips for Module 1",
                            "body": "<ul><li>One clustered index per table; the PRIMARY KEY is clustered by default</li><li>IDENTITY(seed, increment) — know what seed and increment do</li><li>JSON_VALUE for scalars; JSON_QUERY for objects/arrays — mixing them up returns NULL</li><li>N boundary values = N+1 partitions</li><li>RANGE RIGHT: boundary value belongs to the RIGHT (higher) partition</li><li>ON DELETE CASCADE deletes children; ON DELETE NO ACTION blocks parent delete</li><li>Functions cannot use #temp tables — use @table variables instead</li></ul>"
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What is the maximum number of nonclustered indexes a SQL Server table can have?",
                            "opts": ["A. 32", "B. 64", "C. 249", "D. 999"],
                            "correct": "D",
                            "explain": "SQL Server allows up to 999 nonclustered indexes per table, compared to exactly 1 clustered index."
                        },
                        {
                            "q": "What happens to a #temp table when the SQL Server session that created it ends?",
                            "opts": ["A. It is moved to a permanent table", "B. It is archived in the master database", "C. It is automatically dropped", "D. It remains in tempdb until manually dropped"],
                            "correct": "C",
                            "explain": "Local temporary tables (#temp) are automatically dropped when the session that created them ends. Global temp tables (##) are dropped when the last session using them closes."
                        },
                        {
                            "q": "Which constraint type uses the ISJSON function to validate data?",
                            "opts": ["A. FOREIGN KEY", "B. UNIQUE", "C. CHECK", "D. DEFAULT"],
                            "correct": "C",
                            "explain": "CHECK constraints can use any boolean function including ISJSON. The pattern CONSTRAINT name CHECK (ISJSON(column) = 1) ensures a column always contains valid JSON."
                        },
                        {
                            "q": "In a partition function with RANGE LEFT, where does the boundary value '2023-01-01' fall?",
                            "opts": ["A. In the partition for dates >= 2023-01-01", "B. In the partition for dates < 2023-01-01 (the left/lower partition)", "C. In both partitions", "D. RANGE LEFT has no boundary values"],
                            "correct": "B",
                            "explain": "With RANGE LEFT, boundary values belong to the LEFT (lower) partition. So '2023-01-01' with RANGE LEFT means that exact date falls in the pre-2023 partition."
                        },
                        {
                            "q": "Which SQL Server platform would you choose for a new application that needs automatic elastic scaling and maximum managed service benefits?",
                            "opts": ["A. SQL Server on-premises", "B. SQL Server on Azure VM", "C. Azure SQL Managed Instance", "D. Azure SQL Database"],
                            "correct": "D",
                            "explain": "Azure SQL Database is the most cloud-native option with serverless compute, elastic pools, automatic scaling, and the highest level of managed service. Managed Instance is better for lift-and-shift migrations."
                        }
                    ]
                }
            ]
        },


        # ================================================================
        # MODULE 2: Implement programmability objects with SQL
        # ================================================================
        {
            'id': 'lp1-m2',
            'title': 'Implement programmability objects with SQL',
            'description': 'Create views, stored procedures, functions, and triggers to encapsulate business logic in SQL Server.',
            'units': [
                {
                    'id': 'lp1-m2-u1',
                    'title': 'Introduction',
                    'type': 'intro',
                    'estimated_time': 5,
                    'objectives': ['Know the four main programmability object types'],
                    'content': [
                        {
                            'type': 'theory',
                            'title': 'Programmability Objects Overview',
                            'body': 'SQL Server provides four main programmability objects:<ul><li><strong>Views</strong> - Saved SELECT queries for read simplification and security</li><li><strong>Stored Procedures</strong> - Named T-SQL blocks for business logic and DML</li><li><strong>Functions</strong> - Scalar (one value) or table-valued (result set) for reusable calculations</li><li><strong>Triggers</strong> - Automatic responses to INSERT, UPDATE, DELETE events</li></ul>'
                        },
                        {
                            'type': 'tip',
                            'body': 'Choose stored procedures for DML operations. Use functions only for computations that return a value and have no side effects.'
                        }
                    ],
                    'quiz': [
                        {
                            'q': 'Which object fires automatically on DML events?',
                            'opts': ['A. View', 'B. Stored Procedure', 'C. Trigger', 'D. Scalar Function'],
                            'correct': 'C',
                            'explain': 'Triggers automatically fire in response to DML events (INSERT, UPDATE, DELETE) on a table.'
                        },
                        {
                            'q': 'What is a view in SQL Server?',
                            'opts': [
                                'A. Permanently stored data',
                                'B. A saved SELECT query stored as a named object',
                                'C. A type of index',
                                'D. A compiled function'
                            ],
                            'correct': 'B',
                            'explain': 'A view is a named SELECT statement stored in the database that you can query like a table.'
                        },
                        {
                            'q': 'Which object type returns a single value?',
                            'opts': ['A. Table-valued function', 'B. View', 'C. Scalar function', 'D. Trigger'],
                            'correct': 'C',
                            'explain': 'A scalar function returns exactly one value of a specified data type.'
                        },
                        {
                            'q': 'Which object is best for multi-step business logic with DML?',
                            'opts': ['A. View', 'B. Scalar function', 'C. Trigger', 'D. Stored procedure'],
                            'correct': 'D',
                            'explain': 'Stored procedures support DML, control flow, output parameters, and error handling.'
                        },
                        {
                            'q': 'Triggers can be defined on which objects?',
                            'opts': ['A. Views only', 'B. Tables and views', 'C. Functions only', 'D. Stored procedures'],
                            'correct': 'B',
                            'explain': 'Triggers can be defined on tables (AFTER or INSTEAD OF) and on views (INSTEAD OF).'
                        }
                    ]
                },
                {
                    'id': 'lp1-m2-u2',
                    'title': 'Create views',
                    'type': 'lesson',
                    'estimated_time': 20,
                    'objectives': ['Create views', 'Use WITH SCHEMABINDING', 'Create indexed views'],
                    'content': [
                        {
                            'type': 'theory',
                            'title': 'What is a View?',
                            'body': 'A <strong>view</strong> is a saved SELECT query stored as a named object. Views do not store data (unless indexed). Benefits: simplify complex JOINs, restrict column access, present consistent column names.'
                        },
                        {
                            'type': 'sql_block',
                            'title': 'Create, Alter, Drop Views',
                            'code': "-- Simple view\nCREATE VIEW dbo.vw_CustomerOrders\nAS\nSELECT c.CustomerID,\n       c.FirstName + ' ' + c.LastName AS CustomerName,\n       COUNT(o.OrderID)   AS TotalOrders,\n       SUM(o.TotalAmount) AS LifetimeValue\nFROM dbo.Customers c\nLEFT JOIN dbo.Orders o ON c.CustomerID = o.CustomerID\nGROUP BY c.CustomerID, c.FirstName, c.LastName;\nGO\n\n-- View with SCHEMABINDING\nCREATE VIEW dbo.vw_ActiveProducts\nWITH SCHEMABINDING\nAS\nSELECT ProductID, ProductName, Price, Category\nFROM dbo.Products\nWHERE IsActive = 1;\nGO\n\n-- Indexed view - requires SCHEMABINDING\nCREATE VIEW dbo.vw_OrderTotals\nWITH SCHEMABINDING\nAS\nSELECT CustomerID,\n       COUNT_BIG(*) AS OrderCount,\n       SUM(TotalAmount) AS TotalAmount\nFROM dbo.Orders\nGROUP BY CustomerID;\nGO\n\n-- UNIQUE CLUSTERED index materializes the view\nCREATE UNIQUE CLUSTERED INDEX UX_vw_OrderTotals\n    ON dbo.vw_OrderTotals (CustomerID);\nGO\n\nSELECT * FROM dbo.vw_CustomerOrders WHERE LifetimeValue > 500;\n\nALTER VIEW dbo.vw_ActiveProducts\nWITH SCHEMABINDING\nAS\nSELECT ProductID, ProductName, Price, Category, StockQty\nFROM dbo.Products WHERE IsActive = 1;\n\nDROP VIEW IF EXISTS dbo.vw_CustomerOrders;"
                        },
                        {
                            'type': 'important',
                            'body': 'Indexed views require WITH SCHEMABINDING, two-part table names, and the first index must be UNIQUE CLUSTERED. Use COUNT_BIG(*) not COUNT(*) in grouped indexed views.'
                        },
                        {
                            'type': 'tip',
                            'body': 'WITH SCHEMABINDING prevents the underlying tables and columns referenced by the view from being altered or dropped.'
                        }
                    ],
                    'quiz': [
                        {
                            'q': 'What option prevents dropping columns used by a view?',
                            'opts': ['A. WITH ENCRYPTION', 'B. WITH SCHEMABINDING', 'C. WITH CHECK OPTION', 'D. WITH NOLOCK'],
                            'correct': 'B',
                            'explain': 'WITH SCHEMABINDING binds the view to the schema of underlying objects.'
                        },
                        {
                            'q': 'What type of index materializes a view?',
                            'opts': ['A. Nonclustered index', 'B. Filtered index', 'C. UNIQUE CLUSTERED index', 'D. Columnstore index'],
                            'correct': 'C',
                            'explain': 'An indexed view requires a UNIQUE CLUSTERED index as the first index.'
                        },
                        {
                            'q': 'Which aggregate replaces COUNT(*) in an indexed view?',
                            'opts': ['A. SUM(*)', 'B. COUNT_BIG(*)', 'C. MAX(*)', 'D. AVG(*)'],
                            'correct': 'B',
                            'explain': 'Indexed views with GROUP BY must use COUNT_BIG(*).'
                        },
                        {
                            'q': 'How do you modify an existing view?',
                            'opts': ['A. DROP and recreate', 'B. UPDATE VIEW', 'C. ALTER VIEW', 'D. MODIFY VIEW'],
                            'correct': 'C',
                            'explain': 'ALTER VIEW rewrites a view definition while preserving its name and permissions.'
                        },
                        {
                            'q': 'When does a view store data?',
                            'opts': ['A. Always', 'B. Never', 'C. Only as an indexed (materialized) view', 'D. Only with SCHEMABINDING'],
                            'correct': 'C',
                            'explain': 'Only indexed views physically store result data.'
                        }
                    ]
                },
                {
                    'id': 'lp1-m2-u3',
                    'title': 'Create stored procedures',
                    'type': 'lesson',
                    'estimated_time': 20,
                    'objectives': ['Create stored procedures', 'Use input and output parameters', 'Handle errors with TRY/CATCH'],
                    'content': [
                        {
                            'type': 'theory',
                            'title': 'Stored Procedures',
                            'body': 'A <strong>stored procedure</strong> is a saved T-SQL batch with a name. Benefits: reuse logic, reduce network traffic, parameterize queries (avoid SQL injection), control permissions. Always add <code>SET NOCOUNT ON</code> to suppress row-count messages.'
                        },
                        {
                            'type': 'sql_block',
                            'title': 'Create and Use Stored Procedures',
                            'code': '-- Basic stored procedure\nCREATE PROCEDURE dbo.usp_GetCustomerOrders\n    @CustomerID INT\nAS\nBEGIN\n    SET NOCOUNT ON;\n    SELECT o.OrderID, o.OrderDate, o.TotalAmount\n    FROM dbo.Orders o\n    WHERE o.CustomerID = @CustomerID\n    ORDER BY o.OrderDate DESC;\nEND;\nGO\n\nEXEC dbo.usp_GetCustomerOrders @CustomerID = 42;\n\n-- OUTPUT parameter\nCREATE PROCEDURE dbo.usp_InsertOrder\n    @CustomerID  INT,\n    @TotalAmount DECIMAL(10,2),\n    @NewOrderID  INT OUTPUT\nAS\nBEGIN\n    SET NOCOUNT ON;\n    INSERT INTO dbo.Orders (CustomerID, TotalAmount, OrderDate)\n    VALUES (@CustomerID, @TotalAmount, GETDATE());\n    SET @NewOrderID = SCOPE_IDENTITY();\nEND;\nGO\n\nDECLARE @OID INT;\nEXEC dbo.usp_InsertOrder\n    @CustomerID  = 42,\n    @TotalAmount = 199.99,\n    @NewOrderID  = @OID OUTPUT;\nSELECT @OID AS NewOrderID;\n\n-- TRY/CATCH error handling\nCREATE PROCEDURE dbo.usp_DeleteCustomer\n    @CustomerID INT\nAS\nBEGIN\n    SET NOCOUNT ON;\n    BEGIN TRY\n        DELETE FROM dbo.Customers WHERE CustomerID = @CustomerID;\n    END TRY\n    BEGIN CATCH\n        THROW;\n    END CATCH;\nEND;\nGO\n\nDROP PROCEDURE IF EXISTS dbo.usp_DeleteCustomer;'
                        },
                        {
                            'type': 'important',
                            'body': 'Always use SCOPE_IDENTITY() to get the last inserted identity value - not @@IDENTITY which can be affected by triggers on other tables.'
                        },
                        {
                            'type': 'tip',
                            'body': 'Never prefix procedures with sp_ - SQL Server searches master database first for sp_ names, causing slowness and conflicts.'
                        }
                    ],
                    'quiz': [
                        {
                            'q': 'What does SET NOCOUNT ON do?',
                            'opts': [
                                'A. Stops SELECT output',
                                'B. Suppresses the rows affected message',
                                'C. Stops row counting in WHERE',
                                'D. Prevents NULLs'
                            ],
                            'correct': 'B',
                            'explain': "SET NOCOUNT ON suppresses the '(N row(s) affected)' message."
                        },
                        {
                            'q': 'Which function returns the identity from the most recent INSERT in the current scope?',
                            'opts': ['A. @@IDENTITY', 'B. IDENT_CURRENT()', 'C. SCOPE_IDENTITY()', 'D. LAST_INSERT_ID()'],
                            'correct': 'C',
                            'explain': 'SCOPE_IDENTITY() is unaffected by triggers on other tables.'
                        },
                        {
                            'q': 'How do you declare a parameter that returns a value to the caller?',
                            'opts': ['A. @Param INT RETURN', 'B. @Param INT OUT', 'C. @Param INT OUTPUT', 'D. RETURN @Param'],
                            'correct': 'C',
                            'explain': 'The OUTPUT keyword after the data type marks an output parameter.'
                        },
                        {
                            'q': 'What does bare THROW inside a CATCH block do?',
                            'opts': ['A. Raises a new error', 'B. Re-raises the original error', 'C. Suppresses the error', 'D. Logs the error'],
                            'correct': 'B',
                            'explain': 'THROW with no arguments re-raises the caught error with original number, severity, and state.'
                        },
                        {
                            'q': 'Why avoid the sp_ prefix on stored procedures?',
                            'opts': [
                                'A. Reserved for functions',
                                'B. SQL Server searches master first, causing slowness',
                                'C. Disables output parameters',
                                'D. Conflicts with views'
                            ],
                            'correct': 'B',
                            'explain': 'sp_ names trigger a master database search first, adding overhead and potential conflicts.'
                        }
                    ]
                },
                {
                    'id': 'lp1-m2-u4',
                    'title': 'Create scalar functions',
                    'type': 'lesson',
                    'estimated_time': 15,
                    'objectives': ['Create scalar user-defined functions', 'Understand when to use them'],
                    'content': [
                        {
                            'type': 'theory',
                            'title': 'Scalar Functions',
                            'body': 'A <strong>scalar function</strong> returns exactly one value of the declared return type. Rules: call with two-part name (<code>dbo.fn_Name</code>); cannot perform DML on permanent tables; executes once per row which can hurt performance on large queries.'
                        },
                        {
                            'type': 'sql_block',
                            'title': 'Create and Call Scalar Functions',
                            'code': "CREATE FUNCTION dbo.fn_FullName\n(\n    @First NVARCHAR(50),\n    @Last  NVARCHAR(50)\n)\nRETURNS NVARCHAR(101)\nAS\nBEGIN\n    RETURN LTRIM(RTRIM(@First)) + ' ' + LTRIM(RTRIM(@Last));\nEND;\nGO\n\n-- Must use schema prefix\nSELECT dbo.fn_FullName(FirstName, LastName) AS FullName\nFROM dbo.Customers;\n\nCREATE FUNCTION dbo.fn_DiscountRate (@TotalAmount DECIMAL(10,2))\nRETURNS DECIMAL(5,4)\nAS\nBEGIN\n    DECLARE @Rate DECIMAL(5,4);\n    IF @TotalAmount >= 1000      SET @Rate = 0.15;\n    ELSE IF @TotalAmount >= 500  SET @Rate = 0.10;\n    ELSE IF @TotalAmount >= 100  SET @Rate = 0.05;\n    ELSE SET @Rate = 0.00;\n    RETURN @Rate;\nEND;\nGO\n\nSELECT OrderID, TotalAmount,\n       dbo.fn_DiscountRate(TotalAmount) AS DiscountRate\nFROM dbo.Orders;\n\nDROP FUNCTION IF EXISTS dbo.fn_DiscountRate;"
                        },
                        {
                            'type': 'important',
                            'body': 'Call scalar functions with the schema prefix: dbo.fn_Name(). Without the prefix, SQL Server raises an error.'
                        },
                        {
                            'type': 'tip',
                            'body': 'Scalar functions execute once per row. For high-volume queries consider an inline TVF instead - the optimizer can flatten iTVFs into the outer query plan.'
                        }
                    ],
                    'quiz': [
                        {
                            'q': 'What wraps the body of a scalar function?',
                            'opts': ['A. START/END', 'B. PROCEDURE/END', 'C. BEGIN/END', 'D. RETURNS/END'],
                            'correct': 'C',
                            'explain': 'A scalar function body is wrapped in BEGIN...END after the RETURNS clause.'
                        },
                        {
                            'q': 'How must you call a scalar UDF in a SELECT?',
                            'opts': ['A. fn_Name()', 'B. EXEC fn_Name', 'C. dbo.fn_Name()', 'D. CALL dbo.fn_Name()'],
                            'correct': 'C',
                            'explain': 'Scalar UDFs require the two-part name with schema prefix.'
                        },
                        {
                            'q': 'Can a scalar function INSERT into a permanent table?',
                            'opts': ['A. Yes', 'B. No', 'C. Only with SCHEMABINDING', 'D. Only with OUTPUT'],
                            'correct': 'B',
                            'explain': 'Functions cannot modify permanent database state.'
                        },
                        {
                            'q': 'What clause declares what type a scalar function returns?',
                            'opts': ['A. OUTPUT type', 'B. RETURNS type', 'C. RETURN type', 'D. GIVES type'],
                            'correct': 'B',
                            'explain': 'The RETURNS clause (before BEGIN) declares the return data type.'
                        },
                        {
                            'q': 'What T-SQL statement sends the value back from a scalar function?',
                            'opts': ['A. OUTPUT', 'B. SEND', 'C. RETURN expression', 'D. YIELD'],
                            'correct': 'C',
                            'explain': 'RETURN provides the actual value returned to the caller.'
                        }
                    ]
                },
                {
                    'id': 'lp1-m2-u5',
                    'title': 'Create table-valued functions',
                    'type': 'lesson',
                    'estimated_time': 20,
                    'objectives': ['Create inline TVFs', 'Create multi-statement TVFs', 'Use CROSS APPLY'],
                    'content': [
                        {
                            'type': 'theory',
                            'title': 'Table-Valued Functions',
                            'body': 'A <strong>TVF</strong> returns a table result set. Two types:<ul><li><strong>Inline TVF (iTVF)</strong> - single RETURN (SELECT) statement; optimizer can inline it; best performance</li><li><strong>Multi-statement TVF (mTVF)</strong> - declares @tableVar; uses INSERT to populate; then RETURN. Flexible but opaque to optimizer.</li></ul>Call in FROM clause or with CROSS APPLY / OUTER APPLY.'
                        },
                        {
                            'type': 'sql_block',
                            'title': 'Inline and Multi-Statement TVFs',
                            'code': "-- Inline TVF\nCREATE FUNCTION dbo.fn_CustomerOrders (@CustomerID INT)\nRETURNS TABLE\nAS\nRETURN\n(\n    SELECT o.OrderID, o.OrderDate, o.TotalAmount\n    FROM dbo.Orders o\n    WHERE o.CustomerID = @CustomerID\n);\nGO\n\nSELECT * FROM dbo.fn_CustomerOrders(42);\n\n-- Multi-statement TVF\nCREATE FUNCTION dbo.fn_TopCustomers (@TopN INT)\nRETURNS @Results TABLE\n(\n    CustomerID   INT,\n    CustomerName NVARCHAR(101),\n    TotalSpend   DECIMAL(12,2)\n)\nAS\nBEGIN\n    INSERT INTO @Results\n    SELECT TOP (@TopN) c.CustomerID,\n           c.FirstName + ' ' + c.LastName,\n           SUM(o.TotalAmount)\n    FROM dbo.Customers c\n    JOIN dbo.Orders o ON c.CustomerID = o.CustomerID\n    GROUP BY c.CustomerID, c.FirstName, c.LastName\n    ORDER BY SUM(o.TotalAmount) DESC;\n    RETURN;\nEND;\nGO\n\n-- CROSS APPLY calls TVF per outer row\nSELECT c.CustomerID, c.FirstName, oh.OrderDate, oh.TotalAmount\nFROM dbo.Customers c\nCROSS APPLY dbo.fn_CustomerOrders(c.CustomerID) oh\nWHERE oh.TotalAmount > 100;"
                        },
                        {
                            'type': 'important',
                            'body': 'Prefer inline TVFs - the optimizer can merge them into the outer query for better plans. Multi-statement TVFs are black boxes.'
                        },
                        {
                            'type': 'tip',
                            'body': 'CROSS APPLY excludes outer rows with no matching TVF rows (like INNER JOIN). Use OUTER APPLY to keep all outer rows (like LEFT JOIN).'
                        }
                    ],
                    'quiz': [
                        {
                            'q': 'How do you declare an inline TVF return type?',
                            'opts': ['A. RETURNS @t TABLE(...)', 'B. RETURNS TABLE', 'C. RETURNS ROWSET', 'D. RETURN TABLE AS'],
                            'correct': 'B',
                            'explain': 'Inline TVF uses RETURNS TABLE AS RETURN (SELECT...) - no column list needed.'
                        },
                        {
                            'q': 'Where do you call a TVF?',
                            'opts': ['A. WHERE clause', 'B. SELECT list', 'C. FROM clause', 'D. INSERT VALUES'],
                            'correct': 'C',
                            'explain': 'TVFs go in the FROM clause because they return a result set.'
                        },
                        {
                            'q': 'What does CROSS APPLY do?',
                            'opts': [
                                'A. Joins on all columns',
                                'B. Calls TVF per outer row, excluding non-matching rows',
                                'C. Cross-products all rows',
                                'D. Applies scalar function per row'
                            ],
                            'correct': 'B',
                            'explain': 'CROSS APPLY calls the TVF for each outer row and excludes rows where TVF returns nothing.'
                        },
                        {
                            'q': 'Which TVF type allows optimizer to look inside?',
                            'opts': ['A. Multi-statement TVF', 'B. Inline TVF', 'C. Both equally', 'D. Scalar TVF'],
                            'correct': 'B',
                            'explain': 'Inline TVFs can be inlined into the outer plan. Multi-statement TVFs are opaque.'
                        },
                        {
                            'q': 'How does OUTER APPLY differ from CROSS APPLY?',
                            'opts': [
                                'A. OUTER APPLY excludes non-matching rows',
                                'B. OUTER APPLY keeps outer rows even if TVF returns nothing',
                                'C. OUTER APPLY is faster',
                                'D. No difference'
                            ],
                            'correct': 'B',
                            'explain': 'OUTER APPLY keeps all outer rows and returns NULL for TVF columns when TVF returns no rows.'
                        }
                    ]
                },
                {
                    'id': 'lp1-m2-u6',
                    'title': 'Create triggers',
                    'type': 'lesson',
                    'estimated_time': 20,
                    'objectives': ['Create AFTER triggers', 'Create INSTEAD OF triggers', 'Use inserted and deleted tables'],
                    'content': [
                        {
                            'type': 'theory',
                            'title': 'Triggers',
                            'body': 'A <strong>trigger</strong> fires automatically on INSERT, UPDATE, or DELETE. Two types:<ul><li><strong>AFTER</strong> - fires after DML succeeds; used for auditing, cascades</li><li><strong>INSTEAD OF</strong> - fires instead of the DML; used on views or to override behavior</li></ul>Virtual tables inside triggers: <code>inserted</code> (new/updated rows) and <code>deleted</code> (old/removed rows).'
                        },
                        {
                            'type': 'sql_block',
                            'title': 'Create Triggers',
                            'code': "-- AFTER INSERT trigger\nCREATE TRIGGER trg_Orders_AfterInsert\nON dbo.Orders\nAFTER INSERT\nAS\nBEGIN\n    SET NOCOUNT ON;\n    INSERT INTO dbo.OrderAudit (OrderID, Action, ActionDate)\n    SELECT OrderID, 'INSERT', GETDATE()\n    FROM inserted;\nEND;\nGO\n\n-- AFTER UPDATE trigger - multi-row safe\nCREATE TRIGGER trg_Products_AfterUpdate\nON dbo.Products\nAFTER UPDATE\nAS\nBEGIN\n    SET NOCOUNT ON;\n    IF UPDATE(Price)\n    BEGIN\n        INSERT INTO dbo.PriceHistory (ProductID, OldPrice, NewPrice, ChangeDate)\n        SELECT d.ProductID, d.Price, i.Price, GETDATE()\n        FROM deleted d\n        JOIN inserted i ON d.ProductID = i.ProductID;\n    END;\nEND;\nGO\n\n-- INSTEAD OF trigger on a view\nCREATE TRIGGER trg_vw_Products_InsteadOfInsert\nON dbo.vw_ActiveProducts\nINSTEAD OF INSERT\nAS\nBEGIN\n    SET NOCOUNT ON;\n    INSERT INTO dbo.Products (ProductName, Price, Category, IsActive)\n    SELECT ProductName, Price, Category, 1\n    FROM inserted;\nEND;\nGO\n\nDISABLE TRIGGER trg_Orders_AfterInsert ON dbo.Orders;\nENABLE  TRIGGER trg_Orders_AfterInsert ON dbo.Orders;\nDROP TRIGGER IF EXISTS trg_Orders_AfterInsert;"
                        },
                        {
                            'type': 'important',
                            'body': 'Triggers fire once per statement, not once per row. Always use set-based operations on inserted/deleted - never assume only one row was affected.'
                        },
                        {
                            'type': 'tip',
                            'body': 'Use IF UPDATE(ColumnName) inside an AFTER UPDATE trigger to check whether a specific column was included in the UPDATE statement.'
                        }
                    ],
                    'quiz': [
                        {
                            'q': 'Which virtual table contains newly inserted rows?',
                            'opts': ['A. new', 'B. inserted', 'C. added', 'D. created'],
                            'correct': 'B',
                            'explain': "The 'inserted' virtual table contains new rows being inserted (or new values for updated rows)."
                        },
                        {
                            'q': 'Which virtual table contains old values during UPDATE?',
                            'opts': ['A. old', 'B. removed', 'C. deleted', 'D. previous'],
                            'correct': 'C',
                            'explain': "The 'deleted' virtual table holds the before-values during UPDATE and removed rows during DELETE."
                        },
                        {
                            'q': 'How many times does a trigger fire when 500 rows are inserted in one statement?',
                            'opts': ['A. 500 times', 'B. Once', 'C. Once per batch', 'D. Twice'],
                            'correct': 'B',
                            'explain': 'DML triggers fire once per DML statement. The inserted/deleted tables contain all affected rows.'
                        },
                        {
                            'q': 'Where can INSTEAD OF triggers be defined?',
                            'opts': ['A. Only on tables', 'B. Only on views', 'C. On tables and views', 'D. Only on procedures'],
                            'correct': 'C',
                            'explain': 'INSTEAD OF triggers can be on both tables and views.'
                        },
                        {
                            'q': 'What does IF UPDATE(Price) check?',
                            'opts': [
                                'A. Whether Price value changed',
                                'B. Whether Price column was in the UPDATE SET clause',
                                'C. Whether Price is NULL',
                                'D. Whether Price increased'
                            ],
                            'correct': 'B',
                            'explain': 'IF UPDATE(col) is TRUE if the column was listed in the UPDATE SET clause, regardless of whether the value actually changed.'
                        }
                    ]
                },
                {
                    'id': 'lp1-m2-u7',
                    'title': 'Choose when to use each option',
                    'type': 'lesson',
                    'estimated_time': 15,
                    'objectives': ['Select the correct programmability object for a scenario'],
                    'content': [
                        {
                            'type': 'theory',
                            'title': 'Choosing the Right Object',
                            'body': 'Decision guide for the exam:<ul><li><strong>View</strong> - simplify SELECTs, restrict columns, no parameters needed</li><li><strong>Stored Procedure</strong> - DML operations, multi-step logic, OUTPUT params, error handling</li><li><strong>Scalar Function</strong> - one value inline in expressions (WHERE, SELECT, DEFAULT)</li><li><strong>Inline TVF</strong> - parameterized view; reusable SELECT with parameters</li><li><strong>mTVF</strong> - complex table logic when iTVF is insufficient</li><li><strong>AFTER Trigger</strong> - auto audit, cascade updates, post-DML validations</li><li><strong>INSTEAD OF Trigger</strong> - override DML on a view or redirect base-table writes</li></ul>'
                        },
                        {
                            'type': 'important',
                            'body': 'Exam key: Functions cannot DML permanent tables. Stored procedures can. Use procedures for INSERT/UPDATE/DELETE business logic. Use scalar functions only for computations with no side effects.'
                        },
                        {
                            'type': 'tip',
                            'body': 'Fires automatically when data changes = trigger. Returns one value in SELECT = scalar function. Returns rows with a parameter = inline TVF.'
                        }
                    ],
                    'quiz': [
                        {
                            'q': 'You need to log every DELETE automatically. Which object?',
                            'opts': ['A. Stored procedure', 'B. Scalar function', 'C. AFTER DELETE trigger', 'D. INSTEAD OF trigger'],
                            'correct': 'C',
                            'explain': 'An AFTER DELETE trigger fires automatically and can insert audit records via the deleted table.'
                        },
                        {
                            'q': 'You need a query that accepts a date range and returns rows. Best choice?',
                            'opts': ['A. View', 'B. Scalar function', 'C. Inline TVF', 'D. Stored procedure'],
                            'correct': 'C',
                            'explain': 'An inline TVF is a parameterized view - accepts parameters and returns a result set.'
                        },
                        {
                            'q': 'You need to INSERT into several tables as one unit. Best choice?',
                            'opts': ['A. View', 'B. Trigger', 'C. Scalar function', 'D. Stored procedure'],
                            'correct': 'D',
                            'explain': 'Stored procedures support multi-step DML, transactions, and error handling.'
                        },
                        {
                            'q': 'Complex join view - users query it by CustomerID. Best parameterization?',
                            'opts': ['A. Inline TVF with @CustomerID', 'B. Scalar function', 'C. Stored procedure', 'D. AFTER trigger'],
                            'correct': 'A',
                            'explain': 'An iTVF encapsulates the joins and accepts a parameter.'
                        },
                        {
                            'q': 'Can a scalar function call a stored procedure?',
                            'opts': ['A. Yes', 'B. No', 'C. Only if procedure has no DML', 'D. Only system procedures'],
                            'correct': 'B',
                            'explain': 'User-defined functions cannot execute stored procedures.'
                        }
                    ]
                },
                {
                    'id': 'lp1-m2-u8',
                    'title': 'Exercise: Create programmability objects',
                    'type': 'exercise',
                    'estimated_time': 30,
                    'objectives': ['Apply views, procedures, functions, and triggers in SSMS'],
                    'content': [
                        {
                            'type': 'theory',
                            'title': 'Exercise Overview',
                            'body': 'Build a complete set of programmability objects in SSMS: (1) Create a view combining customer and order data. (2) Stored procedure to insert an order with OUTPUT param. (3) Scalar function for discount. (4) Inline TVF for orders by date range. (5) Trigger to audit inserts.'
                        },
                        {
                            'type': 'sql_block',
                            'title': 'Exercise Tasks',
                            'code': "-- Setup\nCREATE TABLE dbo.Customers (CustomerID INT IDENTITY PRIMARY KEY, Name NVARCHAR(100));\nCREATE TABLE dbo.Orders (OrderID INT IDENTITY PRIMARY KEY, CustomerID INT, Amount DECIMAL(10,2), OrderDate DATE DEFAULT GETDATE());\nCREATE TABLE dbo.OrderAudit (AuditID INT IDENTITY PRIMARY KEY, OrderID INT, InsertedAt DATETIME DEFAULT GETDATE());\nGO\n\n-- Task 1: View\nCREATE VIEW dbo.vw_CustomerSummary AS\nSELECT c.CustomerID, c.Name,\n       COUNT(o.OrderID) AS OrderCount,\n       ISNULL(SUM(o.Amount), 0) AS TotalSpent\nFROM dbo.Customers c\nLEFT JOIN dbo.Orders o ON c.CustomerID = o.CustomerID\nGROUP BY c.CustomerID, c.Name;\nGO\n\n-- Task 2: Stored procedure\nCREATE PROCEDURE dbo.usp_NewOrder\n    @CustomerID INT, @Amount DECIMAL(10,2), @OrderID INT OUTPUT\nAS\nBEGIN\n    SET NOCOUNT ON;\n    INSERT INTO dbo.Orders (CustomerID, Amount) VALUES (@CustomerID, @Amount);\n    SET @OrderID = SCOPE_IDENTITY();\nEND;\nGO\n\n-- Task 3: Scalar function\nCREATE FUNCTION dbo.fn_Discount(@Amount DECIMAL(10,2))\nRETURNS DECIMAL(5,2) AS\nBEGIN\n    RETURN CASE WHEN @Amount >= 500 THEN 0.10\n               WHEN @Amount >= 100 THEN 0.05\n               ELSE 0.00 END;\nEND;\nGO\n\n-- Task 4: Inline TVF\nCREATE FUNCTION dbo.fn_OrdersByDate(@Start DATE, @End DATE)\nRETURNS TABLE AS RETURN\n(\n    SELECT o.OrderID, c.Name, o.Amount, o.OrderDate\n    FROM dbo.Orders o\n    JOIN dbo.Customers c ON o.CustomerID = c.CustomerID\n    WHERE o.OrderDate BETWEEN @Start AND @End\n);\nGO\n\n-- Task 5: Trigger\nCREATE TRIGGER trg_Orders_Audit ON dbo.Orders AFTER INSERT AS\nBEGIN\n    SET NOCOUNT ON;\n    INSERT INTO dbo.OrderAudit (OrderID) SELECT OrderID FROM inserted;\nEND;\nGO\n\n-- Test\nINSERT INTO dbo.Customers VALUES ('Alice'), ('Bob');\nDECLARE @ID INT;\nEXEC dbo.usp_NewOrder 1, 250.00, @ID OUTPUT;\nSELECT @ID AS NewOrderID;\nSELECT * FROM dbo.vw_CustomerSummary;\nSELECT dbo.fn_Discount(250) AS DiscountRate;\nSELECT * FROM dbo.fn_OrdersByDate('2020-01-01', '2030-12-31');\nSELECT * FROM dbo.OrderAudit;"
                        },
                        {
                            'type': 'tip',
                            'body': 'Run each block separately in SSMS (highlight, F5). Check the Messages tab for success/error.'
                        }
                    ],
                    'quiz': [
                        {
                            'q': 'Which object logs inserts automatically without being called directly?',
                            'opts': ['A. Stored procedure', 'B. Scalar function', 'C. Trigger', 'D. View'],
                            'correct': 'C',
                            'explain': 'The AFTER INSERT trigger fires automatically on every INSERT.'
                        },
                        {
                            'q': 'How do you retrieve the new OrderID after the procedure runs?',
                            'opts': ['A. SELECT @@IDENTITY', 'B. Declare variable and use OUTPUT', 'C. Check Messages pane', 'D. SELECT LAST_VALUE()'],
                            'correct': 'B',
                            'explain': 'DECLARE @ID INT; EXEC usp_NewOrder ..., @ID OUTPUT; SELECT @ID;'
                        },
                        {
                            'q': 'fn_Discount returns 0.10 when Amount >= 500. What for Amount = 300?',
                            'opts': ['A. 0.10', 'B. 0.05', 'C. 0.00', 'D. NULL'],
                            'correct': 'B',
                            'explain': '300 is between 100 and 499, so the CASE returns 0.05.'
                        },
                        {
                            'q': 'Why LEFT JOIN in vw_CustomerSummary?',
                            'opts': [
                                'A. Include orders without customers',
                                'B. Include customers with no orders',
                                'C. INNER JOIN not allowed in views',
                                'D. Speed'
                            ],
                            'correct': 'B',
                            'explain': 'LEFT JOIN keeps customers even if they have zero orders.'
                        },
                        {
                            'q': 'How do you call fn_OrdersByDate?',
                            'opts': [
                                'A. SELECT * FROM dbo.fn_OrdersByDate WHERE ...',
                                "B. EXEC dbo.fn_OrdersByDate '2024-01-01','2024-12-31'",
                                "C. SELECT * FROM dbo.fn_OrdersByDate('2024-01-01','2024-12-31')",
                                'D. CALL dbo.fn_OrdersByDate(...)'
                            ],
                            'correct': 'C',
                            'explain': "TVFs go in the FROM clause with parameters: FROM dbo.fn_OrdersByDate('start','end')."
                        }
                    ]
                },
                {
                    'id': 'lp1-m2-u9',
                    'title': 'Knowledge check',
                    'type': 'knowledge_check',
                    'estimated_time': 10,
                    'objectives': ['Assess understanding of programmability objects'],
                    'content': [
                        {
                            'type': 'theory',
                            'title': 'Knowledge Check',
                            'body': 'Answer the following questions to test your understanding of Module 2.'
                        }
                    ],
                    'quiz': [
                        {
                            'q': 'Correct syntax for an inline TVF?',
                            'opts': [
                                'A. CREATE FUNCTION f(@p INT) RETURNS TABLE AS BEGIN...END',
                                'B. CREATE FUNCTION f(@p INT) RETURNS TABLE AS RETURN (SELECT...)',
                                'C. CREATE FUNCTION f(@p INT) RETURNS @t TABLE(...) BEGIN...RETURN;END',
                                'D. CREATE TVF f(@p INT) RETURNS TABLE'
                            ],
                            'correct': 'B',
                            'explain': 'iTVF: RETURNS TABLE AS RETURN(SELECT ...) - no BEGIN/END, no declared table variable.'
                        },
                        {
                            'q': 'Key difference between AFTER and INSTEAD OF triggers?',
                            'opts': [
                                'A. AFTER fires before DML',
                                'B. AFTER fires after DML; INSTEAD OF fires in place of DML',
                                'C. AFTER works on views only',
                                'D. They are the same'
                            ],
                            'correct': 'B',
                            'explain': 'AFTER runs after DML completes. INSTEAD OF replaces the DML entirely.'
                        },
                        {
                            'q': 'Which object type cannot be used inline in a SELECT expression?',
                            'opts': ['A. Scalar function', 'B. Stored procedure', 'C. Inline TVF', 'D. View'],
                            'correct': 'B',
                            'explain': 'Stored procedures cannot be used inline in expressions - they require EXEC.'
                        },
                        {
                            'q': 'What does an indexed view require?',
                            'opts': ['A. WITH ENCRYPTION', 'B. WITH SCHEMABINDING + UNIQUE CLUSTERED index', 'C. WITH CHECK OPTION', 'D. WITH NOLOCK'],
                            'correct': 'B',
                            'explain': 'Indexed views need WITH SCHEMABINDING and the first index must be UNIQUE CLUSTERED.'
                        },
                        {
                            'q': 'A scalar function called 1 million times in a query - performance impact?',
                            'opts': [
                                'A. None - pre-compiled',
                                'B. Minor - network overhead',
                                'C. Significant - executes per row, limits parallelism',
                                'D. Improves due to caching'
                            ],
                            'correct': 'C',
                            'explain': 'Scalar UDFs execute once per row and historically prevented parallelism, causing serious performance issues on large tables.'
                        }
                    ]
                },
                {
                    'id': 'lp1-m2-u10',
                    'title': 'Summary',
                    'type': 'summary',
                    'estimated_time': 5,
                    'objectives': ['Review Module 2 concepts'],
                    'content': [
                        {
                            'type': 'theory',
                            'title': 'Module 2 Summary',
                            'body': 'Key takeaways from Module 2:<ul><li><strong>Views</strong> - saved SELECT queries; WITH SCHEMABINDING prevents base table changes; UNIQUE CLUSTERED index materializes them; use COUNT_BIG(*) in indexed views with GROUP BY</li><li><strong>Stored Procedures</strong> - SET NOCOUNT ON; SCOPE_IDENTITY() for new IDs; INPUT and OUTPUT params; TRY/CATCH with bare THROW</li><li><strong>Scalar Functions</strong> - RETURNS + RETURN; require dbo. prefix; no DML on permanent tables</li><li><strong>Inline TVFs</strong> - RETURNS TABLE AS RETURN(SELECT...); best performance; CROSS/OUTER APPLY</li><li><strong>Triggers</strong> - inserted/deleted virtual tables; once per statement not per row; AFTER for audit; INSTEAD OF for views</li></ul>'
                        },
                        {
                            'type': 'tip',
                            'body': 'Exam reminders: functions = no DML; indexed view = SCHEMABINDING + UNIQUE CLUSTERED + COUNT_BIG; triggers = per statement; iTVF faster than mTVF.'
                        }
                    ],
                    'quiz': [
                        {
                            'q': 'Primary advantage of inline TVF over multi-statement TVF?',
                            'opts': [
                                'A. Supports DML',
                                'B. Optimizer can inline it for better plans',
                                'C. mTVF always faster',
                                'D. Supports OUTPUT parameters'
                            ],
                            'correct': 'B',
                            'explain': 'Inline TVFs can be expanded into the outer query plan. Multi-statement TVFs are black boxes.'
                        },
                        {
                            'q': 'Two virtual tables available inside every DML trigger?',
                            'opts': ['A. new and old', 'B. before and after', 'C. inserted and deleted', 'D. source and target'],
                            'correct': 'C',
                            'explain': 'inserted = new/updated rows; deleted = old/removed rows.'
                        },
                        {
                            'q': 'Required aggregate in indexed view with GROUP BY?',
                            'opts': ['A. COUNT(*)', 'B. COUNT_BIG(*)', 'C. SUM(*)', 'D. MAX(*)'],
                            'correct': 'B',
                            'explain': 'SQL Server requires COUNT_BIG(*) in indexed views with GROUP BY.'
                        },
                        {
                            'q': 'What does SCOPE_IDENTITY() return?',
                            'opts': [
                                'A. Max identity in table',
                                'B. Last identity in current scope',
                                'C. Identity of last updated row',
                                'D. Identity from any table in session'
                            ],
                            'correct': 'B',
                            'explain': 'SCOPE_IDENTITY() returns the last identity from the current scope, unaffected by triggers.'
                        },
                        {
                            'q': 'Allow INSERT on a multi-table JOIN view. Which trigger type?',
                            'opts': ['A. AFTER INSERT', 'B. BEFORE INSERT', 'C. INSTEAD OF INSERT', 'D. FOR INSERT'],
                            'correct': 'C',
                            'explain': 'INSTEAD OF INSERT triggers replace the INSERT with custom logic, making non-updatable views support inserts.'
                        }
                    ]
                }
            ]
        },


        # ================================================================
        # MODULE 3: Write advanced T-SQL code
        # ================================================================
        {
            'id': 'lp1-m3',
            'title': 'Write advanced T-SQL code',
            'description': 'Master CTEs, window functions, JSON, pattern matching, graph queries, correlated subqueries, and error handling.',
            'units': [
                {
                    'id': 'lp1-m3-u1',
                    'title': 'Introduction',
                    'type': 'intro',
                    'estimated_time': 5,
                    'objectives': ['Preview advanced T-SQL topics in this module'],
                    'content': [
                        {
                            'type': 'theory',
                            'title': 'Advanced T-SQL Overview',
                            'body': 'This module covers advanced T-SQL features tested on DP-800:<ul><li><strong>CTEs</strong> - WITH clause, recursive CTEs</li><li><strong>Window functions</strong> - ROW_NUMBER, RANK, LAG, LEAD, running totals</li><li><strong>JSON in T-SQL</strong> - JSON_VALUE, FOR JSON, OPENJSON</li><li><strong>Pattern matching</strong> - LIKE, CHARINDEX, PATINDEX</li><li><strong>Fuzzy strings</strong> - SOUNDEX, DIFFERENCE, TRANSLATE</li><li><strong>Graph queries</strong> - AS NODE, AS EDGE, MATCH</li><li><strong>Correlated subqueries</strong> - EXISTS, NOT EXISTS</li><li><strong>Error handling</strong> - TRY/CATCH, THROW, ERROR_* functions</li></ul>'
                        },
                        {
                            'type': 'tip',
                            'body': 'Window functions and CTEs are frequently tested. Master the OVER() clause syntax and the difference between RANK and DENSE_RANK.'
                        }
                    ],
                    'quiz': [
                        {
                            'q': 'What keyword starts a CTE?',
                            'opts': ['A. CTE', 'B. WITH', 'C. DEFINE', 'D. AS'],
                            'correct': 'B',
                            'explain': 'A CTE begins with the WITH keyword: WITH cte_name AS (SELECT ...).'
                        },
                        {
                            'q': 'Which function assigns sequential integers with no gaps or ties?',
                            'opts': ['A. RANK()', 'B. DENSE_RANK()', 'C. ROW_NUMBER()', 'D. NTILE()'],
                            'correct': 'C',
                            'explain': 'ROW_NUMBER() assigns unique sequential numbers with no ties or gaps.'
                        },
                        {
                            'q': 'Which T-SQL function reads a scalar value from a JSON string?',
                            'opts': ['A. JSON_QUERY', 'B. OPENJSON', 'C. JSON_VALUE', 'D. FOR JSON'],
                            'correct': 'C',
                            'explain': 'JSON_VALUE extracts a single scalar value from a JSON string using a path expression.'
                        },
                        {
                            'q': 'What does EXISTS() return?',
                            'opts': [
                                'A. A count of rows',
                                'B. TRUE if the subquery returns at least one row',
                                'C. The first row of the subquery',
                                'D. NULL if no rows found'
                            ],
                            'correct': 'B',
                            'explain': 'EXISTS returns TRUE (1) if the subquery produces any rows, FALSE (0) otherwise.'
                        },
                        {
                            'q': 'In a graph query, what does MATCH() do?',
                            'opts': [
                                'A. Fuzzy string match',
                                'B. Matches patterns in node-edge-node relationships',
                                'C. Pattern match like LIKE',
                                'D. Matches JSON paths'
                            ],
                            'correct': 'B',
                            'explain': 'MATCH() is used in graph queries to express traversal patterns between nodes and edges.'
                        }
                    ]
                },
                {
                    'id': 'lp1-m3-u2',
                    'title': 'Common table expressions',
                    'type': 'lesson',
                    'estimated_time': 20,
                    'objectives': ['Write CTEs', 'Chain multiple CTEs', 'Write recursive CTEs'],
                    'content': [
                        {
                            'type': 'theory',
                            'title': 'CTEs',
                            'body': 'A <strong>CTE (Common Table Expression)</strong> is a named temporary result set defined in the same statement using <code>WITH name AS (SELECT...)</code>. CTEs improve readability, allow self-referencing (recursive), and can be chained. Unlike a view or temp table, a CTE exists only for the duration of the single statement that references it.'
                        },
                        {
                            'type': 'sql_block',
                            'title': 'CTE Syntax and Recursive CTEs',
                            'code': "-- Simple CTE\nWITH RecentOrders AS\n(\n    SELECT CustomerID, SUM(TotalAmount) AS Total\n    FROM dbo.Orders\n    WHERE OrderDate >= '2024-01-01'\n    GROUP BY CustomerID\n)\nSELECT c.FirstName, c.LastName, ro.Total\nFROM dbo.Customers c\nJOIN RecentOrders ro ON c.CustomerID = ro.CustomerID;\n\n-- Multiple CTEs (chain with commas)\nWITH\nTopCustomers AS\n(\n    SELECT TOP 10 CustomerID, SUM(TotalAmount) AS Spend\n    FROM dbo.Orders\n    GROUP BY CustomerID\n    ORDER BY Spend DESC\n),\nCustomerInfo AS\n(\n    SELECT CustomerID, FirstName + ' ' + LastName AS FullName\n    FROM dbo.Customers\n)\nSELECT ci.FullName, tc.Spend\nFROM TopCustomers tc\nJOIN CustomerInfo ci ON tc.CustomerID = ci.CustomerID;\n\n-- Recursive CTE: employee hierarchy\nWITH EmpHierarchy AS\n(\n    -- Anchor: top-level employees (no manager)\n    SELECT EmpID, EmpName, ManagerID, 0 AS Level\n    FROM dbo.Employees\n    WHERE ManagerID IS NULL\n\n    UNION ALL\n\n    -- Recursive member\n    SELECT e.EmpID, e.EmpName, e.ManagerID, h.Level + 1\n    FROM dbo.Employees e\n    JOIN EmpHierarchy h ON e.ManagerID = h.EmpID\n)\nSELECT EmpID, EmpName, Level\nFROM EmpHierarchy\nOPTION (MAXRECURSION 50);  -- default is 100, 0 = unlimited"
                        },
                        {
                            'type': 'important',
                            'body': 'A recursive CTE must have: (1) an anchor member, (2) UNION ALL, (3) a recursive member that joins back to the CTE name. Use OPTION (MAXRECURSION n) to control max depth - default is 100.'
                        },
                        {
                            'type': 'tip',
                            'body': 'CTEs do not create temp storage. SQL Server expands the CTE inline. For large result sets referenced multiple times, a temp table (#temp) may be more efficient.'
                        }
                    ],
                    'quiz': [
                        {
                            'q': 'What separates the anchor from the recursive member in a recursive CTE?',
                            'opts': ['A. UNION', 'B. UNION ALL', 'C. EXCEPT', 'D. INTERSECT'],
                            'correct': 'B',
                            'explain': 'Recursive CTEs require UNION ALL between the anchor member and the recursive member.'
                        },
                        {
                            'q': 'How long does a CTE persist?',
                            'opts': [
                                'A. Until the session ends',
                                'B. Until explicitly dropped',
                                'C. For the single statement that references it',
                                'D. Until the batch ends'
                            ],
                            'correct': 'C',
                            'explain': 'A CTE only exists for the duration of the single SELECT/INSERT/UPDATE/DELETE statement that follows it.'
                        },
                        {
                            'q': 'What hint limits recursion depth in a recursive CTE?',
                            'opts': ['A. MAXRECURSION', 'B. OPTION (MAXDEPTH)', 'C. OPTION (RECURSE)', 'D. LIMIT RECURSION'],
                            'correct': 'A',
                            'explain': 'OPTION (MAXRECURSION n) in the outer query limits how deep the recursion can go. Default is 100.'
                        },
                        {
                            'q': 'Can you reference a CTE more than once in the same statement?',
                            'opts': ['A. No - single use only', 'B. Yes', 'C. Only if using DISTINCT', 'D. Only in a SELECT'],
                            'correct': 'B',
                            'explain': 'A CTE can be referenced multiple times within the single statement that follows the WITH clause.'
                        },
                        {
                            'q': 'What is the main advantage of CTEs over subqueries?',
                            'opts': [
                                'A. CTEs are stored permanently',
                                'B. CTEs run faster',
                                'C. CTEs can be named and referenced multiple times, improving readability',
                                'D. CTEs cannot be recursive'
                            ],
                            'correct': 'C',
                            'explain': 'CTEs improve readability and can be referenced multiple times in the same statement.'
                        }
                    ]
                },
                {
                    'id': 'lp1-m3-u3',
                    'title': 'Window functions',
                    'type': 'lesson',
                    'estimated_time': 25,
                    'objectives': ['Use ranking functions', 'Use offset functions', 'Use aggregate window functions'],
                    'content': [
                        {
                            'type': 'theory',
                            'title': 'Window Functions',
                            'body': 'Window functions compute values across a set of rows related to the current row using an OVER() clause - they do not collapse rows like GROUP BY. Syntax: <code>FUNCTION() OVER (PARTITION BY col ORDER BY col ROWS BETWEEN ...)</code>. Categories:<ul><li><strong>Ranking</strong>: ROW_NUMBER, RANK, DENSE_RANK, NTILE</li><li><strong>Offset</strong>: LAG, LEAD, FIRST_VALUE, LAST_VALUE</li><li><strong>Aggregate</strong>: SUM, AVG, COUNT, MIN, MAX with OVER()</li></ul>'
                        },
                        {
                            'type': 'sql_block',
                            'title': 'Window Function Examples',
                            'code': '-- Ranking functions\nSELECT CustomerID, TotalAmount,\n    ROW_NUMBER() OVER (ORDER BY TotalAmount DESC) AS RowNum,\n    RANK()       OVER (ORDER BY TotalAmount DESC) AS Rnk,\n    DENSE_RANK() OVER (ORDER BY TotalAmount DESC) AS DenseRnk,\n    NTILE(4)     OVER (ORDER BY TotalAmount DESC) AS Quartile\nFROM dbo.Orders;\n\n-- PARTITION BY: ranking within groups\nSELECT CustomerID, ProductCategory, TotalAmount,\n    ROW_NUMBER() OVER (\n        PARTITION BY CustomerID\n        ORDER BY TotalAmount DESC) AS RankInCustomer\nFROM dbo.Orders;\n\n-- Offset functions: LAG and LEAD\nSELECT OrderDate, TotalAmount,\n    LAG(TotalAmount, 1, 0)  OVER (ORDER BY OrderDate) AS PrevAmount,\n    LEAD(TotalAmount, 1, 0) OVER (ORDER BY OrderDate) AS NextAmount\nFROM dbo.Orders;\n\n-- FIRST_VALUE and LAST_VALUE\nSELECT CustomerID, OrderDate, TotalAmount,\n    FIRST_VALUE(TotalAmount) OVER (\n        PARTITION BY CustomerID ORDER BY OrderDate\n        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS FirstOrder,\n    LAST_VALUE(TotalAmount)  OVER (\n        PARTITION BY CustomerID ORDER BY OrderDate\n        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS LastOrder\nFROM dbo.Orders;\n\n-- Running total with SUM OVER()\nSELECT OrderDate, TotalAmount,\n    SUM(TotalAmount) OVER (\n        ORDER BY OrderDate\n        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS RunningTotal\nFROM dbo.Orders;'
                        },
                        {
                            'type': 'important',
                            'body': 'RANK() vs DENSE_RANK(): if two rows tie at rank 2, RANK gives both rank 2 and then skips to rank 4. DENSE_RANK gives both rank 2 and next rank is 3 (no gap).'
                        },
                        {
                            'type': 'tip',
                            'body': 'LAST_VALUE requires ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING to see all rows in the partition. Without it, the default window goes only to CURRENT ROW.'
                        }
                    ],
                    'quiz': [
                        {
                            'q': 'Two rows tie for position 2. What ranks does RANK() assign?',
                            'opts': ['A. 2 and 2, next is 3', 'B. 2 and 2, next is 4', 'C. 2 and 3, next is 4', 'D. 1 and 1, next is 3'],
                            'correct': 'B',
                            'explain': 'RANK() gives both tied rows the same rank and skips the next rank. Two rows at rank 2 means next rank is 4.'
                        },
                        {
                            'q': 'What does PARTITION BY do in OVER()?',
                            'opts': [
                                'A. Filters rows',
                                'B. Sorts rows',
                                'C. Divides rows into groups for independent window calculations',
                                'D. Limits results'
                            ],
                            'correct': 'C',
                            'explain': 'PARTITION BY divides rows into independent partitions. Window functions restart for each partition.'
                        },
                        {
                            'q': 'LAG(Amount, 1, 0) - what does the third argument do?',
                            'opts': [
                                'A. Specifies offset rows',
                                'B. Sets the default value when no previous row exists',
                                'C. Sets partition count',
                                'D. Orders results'
                            ],
                            'correct': 'B',
                            'explain': 'The third argument of LAG/LEAD is the default value returned when there is no row at the specified offset.'
                        },
                        {
                            'q': 'What is ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW used for?',
                            'opts': [
                                'A. Full partition window',
                                'B. Calculates running total from first row to current row',
                                'C. Last row only',
                                'D. Current row only'
                            ],
                            'correct': 'B',
                            'explain': 'This frame includes all rows from the start of the partition through the current row - standard running total/sum frame.'
                        },
                        {
                            'q': 'Which function divides rows into N roughly equal groups?',
                            'opts': ['A. RANK()', 'B. ROW_NUMBER()', 'C. DENSE_RANK()', 'D. NTILE(N)'],
                            'correct': 'D',
                            'explain': 'NTILE(N) divides rows into N buckets and assigns each row its bucket number.'
                        }
                    ]
                },
                {
                    'id': 'lp1-m3-u4',
                    'title': 'JSON data in T-SQL',
                    'type': 'lesson',
                    'estimated_time': 20,
                    'objectives': ['Read JSON with JSON_VALUE and JSON_QUERY', 'Parse JSON with OPENJSON', 'Generate JSON with FOR JSON'],
                    'content': [
                        {
                            'type': 'theory',
                            'title': 'JSON in SQL Server',
                            'body': 'SQL Server stores JSON as NVARCHAR. Built-in functions handle reading and generating JSON:<ul><li><code>JSON_VALUE(json, path)</code> - extract scalar value</li><li><code>JSON_QUERY(json, path)</code> - extract object or array (not scalar)</li><li><code>OPENJSON(json)</code> - parse JSON into rows</li><li><code>FOR JSON AUTO/PATH</code> - generate JSON from query results</li><li><code>ISJSON(string)</code> - validate JSON (1 = valid)</li><li>SQL Server 2022: <code>JSON_OBJECT()</code> and <code>JSON_ARRAY()</code></li></ul>JSON paths use dollar notation: <code>$.key</code>, <code>$.array[0].key</code>.'
                        },
                        {
                            'type': 'sql_block',
                            'title': 'JSON Functions',
                            'code': 'DECLARE @json NVARCHAR(MAX) = N\'\n{\n  "CustomerID": 42,\n  "Name": "Alice",\n  "Address": {"City": "Seattle", "Zip": "98101"},\n  "Orders": [{"OrderID": 1, "Amount": 150.00}, {"OrderID": 2, "Amount": 75.50}]\n}\';\n\n-- JSON_VALUE: extract scalar\nSELECT JSON_VALUE(@json, \'$.Name\') AS Name,\n       JSON_VALUE(@json, \'$.Address.City\') AS City,\n       JSON_VALUE(@json, \'$.Orders[0].Amount\') AS FirstOrderAmt;\n\n-- JSON_QUERY: extract object or array\nSELECT JSON_QUERY(@json, \'$.Address\') AS AddressObj,\n       JSON_QUERY(@json, \'$.Orders\') AS OrdersArray;\n\n-- OPENJSON: parse array into rows\nSELECT OrderID, Amount\nFROM OPENJSON(@json, \'$.Orders\')\nWITH\n(\n    OrderID INT   \'$.OrderID\',\n    Amount  FLOAT \'$.Amount\'\n);\n\n-- ISJSON: validate\nSELECT ISJSON(@json) AS IsValid;  -- returns 1\n\n-- FOR JSON AUTO: auto-generate JSON\nSELECT TOP 3 CustomerID, FirstName, LastName\nFROM dbo.Customers\nFOR JSON AUTO;\n\n-- FOR JSON PATH with ROOT\nSELECT CustomerID AS [customer.id],\n       FirstName  AS [customer.firstName]\nFROM dbo.Customers\nFOR JSON PATH, ROOT(\'Customers\');\n\n-- SQL Server 2022: JSON_OBJECT and JSON_ARRAY\nSELECT JSON_OBJECT(\'id\': CustomerID, \'name\': FirstName) AS CustomerJSON\nFROM dbo.Customers;'
                        },
                        {
                            'type': 'important',
                            'body': 'JSON_VALUE returns a scalar (string/number). JSON_QUERY returns an object or array as text. Do not use JSON_VALUE to extract objects - it returns NULL.'
                        },
                        {
                            'type': 'tip',
                            'body': 'OPENJSON with a WITH clause (schema on sidecar) is much easier to work with than the default key/value/type columns. Always use the WITH schema when you know the JSON structure.'
                        }
                    ],
                    'quiz': [
                        {
                            'q': 'Which function extracts a single scalar value from JSON?',
                            'opts': ['A. JSON_QUERY', 'B. OPENJSON', 'C. JSON_VALUE', 'D. FOR JSON'],
                            'correct': 'C',
                            'explain': 'JSON_VALUE extracts a scalar (string, number, boolean) from a JSON path.'
                        },
                        {
                            'q': 'Which function extracts a nested JSON object or array?',
                            'opts': ['A. JSON_VALUE', 'B. JSON_QUERY', 'C. OPENJSON', 'D. ISJSON'],
                            'correct': 'B',
                            'explain': 'JSON_QUERY extracts an object or array from a JSON path (returns the JSON text of the sub-object).'
                        },
                        {
                            'q': 'What does ISJSON() return for valid JSON?',
                            'opts': ['A. TRUE', 'B. 1', "C. 'valid'", 'D. 0'],
                            'correct': 'B',
                            'explain': 'ISJSON returns 1 for valid JSON and 0 for invalid JSON.'
                        },
                        {
                            'q': 'How do you convert query results into JSON?',
                            'opts': ['A. JSON(SELECT...)', 'B. SELECT ... FOR JSON AUTO (or PATH)', 'C. CONVERT(JSON, result)', 'D. JSON_CAST(result)'],
                            'correct': 'B',
                            'explain': 'FOR JSON AUTO or FOR JSON PATH at the end of a SELECT statement converts the result set to JSON.'
                        },
                        {
                            'q': 'What is the difference between FOR JSON AUTO and FOR JSON PATH?',
                            'opts': [
                                'A. AUTO is faster',
                                'B. AUTO shapes JSON from table/alias names; PATH lets you control property names with dot notation',
                                'C. PATH generates arrays; AUTO generates objects',
                                'D. They produce identical output'
                            ],
                            'correct': 'B',
                            'explain': 'FOR JSON AUTO infers nesting from JOIN aliases. FOR JSON PATH gives you full control over property names using column aliases like [obj.property].'
                        }
                    ]
                },
                {
                    'id': 'lp1-m3-u5',
                    'title': 'Pattern matching in T-SQL',
                    'type': 'lesson',
                    'estimated_time': 15,
                    'objectives': ['Use LIKE wildcards', 'Use CHARINDEX and PATINDEX'],
                    'content': [
                        {
                            'type': 'theory',
                            'title': 'Pattern Matching',
                            'body': "T-SQL pattern matching uses LIKE with wildcard characters:<ul><li><code>%</code> - any string of zero or more characters</li><li><code>_</code> - any single character</li><li><code>[set]</code> - any single character in set, e.g. [a-z]</li><li><code>[^set]</code> - any single character NOT in set</li></ul>String search functions:<ul><li><code>CHARINDEX(find, string, start)</code> - position of substring (0 if not found)</li><li><code>PATINDEX('%pattern%', string)</code> - position of LIKE pattern (0 if not found)</li></ul>Use ESCAPE to match literal wildcard characters."
                        },
                        {
                            'type': 'sql_block',
                            'title': 'LIKE and String Search',
                            'code': "-- % wildcard\nSELECT * FROM dbo.Customers WHERE LastName LIKE 'Sm%';\n\n-- _ wildcard (exactly one char)\nSELECT * FROM dbo.Products WHERE ProductCode LIKE 'A_B_C';\n\n-- [set] - one char from set\nSELECT * FROM dbo.Customers WHERE FirstName LIKE '[ABC]%';\n\n-- [^set] - one char NOT in set\nSELECT * FROM dbo.Products WHERE SKU LIKE '[^0-9]%';\n\n-- ESCAPE: match literal % or _\nSELECT * FROM dbo.Notes WHERE Body LIKE '%50!%%' ESCAPE '!';\n\n-- CHARINDEX: find position\nSELECT CHARINDEX('@', Email) AS AtPosition,\n       SUBSTRING(Email, 1, CHARINDEX('@', Email) - 1) AS Username\nFROM dbo.Users;\n\n-- PATINDEX: LIKE pattern match returning position\nSELECT ProductName,\n       PATINDEX('%[0-9]%', ProductName) AS FirstDigitPos\nFROM dbo.Products\nWHERE PATINDEX('%[0-9]%', ProductName) > 0;"
                        },
                        {
                            'type': 'important',
                            'body': 'CHARINDEX returns 0 (not NULL) when the substring is not found. Always check > 0 before using it in SUBSTRING calculations.'
                        },
                        {
                            'type': 'tip',
                            'body': 'PATINDEX accepts LIKE wildcards (%, _, [set]). CHARINDEX does not - it looks for a literal substring. Use PATINDEX when you need pattern-based search with positions.'
                        }
                    ],
                    'quiz': [
                        {
                            'q': 'Which wildcard matches any single character in LIKE?',
                            'opts': ['A. %', 'B. *', 'C. _', 'D. ?'],
                            'correct': 'C',
                            'explain': 'The underscore (_) in LIKE matches exactly one character.'
                        },
                        {
                            'q': 'How do you find rows where Email contains exactly one @?',
                            'opts': [
                                "A. WHERE Email LIKE '%@%' AND Email NOT LIKE '%@%@%'",
                                "B. WHERE CHARINDEX('@',Email) = 1",
                                "C. WHERE PATINDEX('%@%',Email) > 1",
                                "D. WHERE Email LIKE '@'"
                            ],
                            'correct': 'A',
                            'explain': 'Check that at least one @ exists and that two @s do NOT exist.'
                        },
                        {
                            'q': 'What does CHARINDEX return when the substring is not found?',
                            'opts': ['A. NULL', 'B. -1', 'C. 0', 'D. FALSE'],
                            'correct': 'C',
                            'explain': 'CHARINDEX returns 0 (not NULL) when the search string is not found.'
                        },
                        {
                            'q': 'Which pattern matches strings starting with A, B, or C?',
                            'opts': ["A. LIKE '(A|B|C)%'", "B. LIKE '[ABC]%'", "C. LIKE '%[ABC]'", "D. LIKE '{ABC}%'"],
                            'correct': 'B',
                            'explain': '[ABC] in a LIKE pattern matches any single character that is A, B, or C.'
                        },
                        {
                            'q': "What does PATINDEX('%[0-9]%', col) return?",
                            'opts': ['A. The digit found', 'B. The position of the first digit in the string', 'C. TRUE/FALSE', 'D. The count of digits'],
                            'correct': 'B',
                            'explain': 'PATINDEX returns the position (1-based) of the first match of the pattern in the string, or 0 if not found.'
                        }
                    ]
                },
                {
                    'id': 'lp1-m3-u6',
                    'title': 'Fuzzy string matching',
                    'type': 'lesson',
                    'estimated_time': 10,
                    'objectives': ['Use SOUNDEX and DIFFERENCE', 'Use TRANSLATE'],
                    'content': [
                        {
                            'type': 'theory',
                            'title': 'Fuzzy String Functions',
                            'body': 'When exact matching is insufficient, use phonetic or translation functions:<ul><li><code>SOUNDEX(string)</code> - returns a 4-character phonetic code (same code for same-sounding words)</li><li><code>DIFFERENCE(s1, s2)</code> - compares SOUNDEX codes; returns 0-4 (4 = best match)</li><li><code>TRANSLATE(string, from_chars, to_chars)</code> - replaces characters one-to-one (SQL Server 2017+); useful for cleaning strings</li></ul>'
                        },
                        {
                            'type': 'sql_block',
                            'title': 'SOUNDEX, DIFFERENCE, TRANSLATE',
                            'code': "-- SOUNDEX: phonetic code\nSELECT SOUNDEX('Smith'),  -- S530\n       SOUNDEX('Smythe'); -- S530 (same!)\n\n-- DIFFERENCE: 0-4, 4 = sounds most alike\nSELECT DIFFERENCE('Smith', 'Smythe');  -- 4\nSELECT DIFFERENCE('Smith', 'Jones');   -- 1\n\n-- Find customers whose names sound like 'Smith'\nSELECT CustomerID, LastName\nFROM dbo.Customers\nWHERE DIFFERENCE(LastName, 'Smith') >= 3;\n\n-- TRANSLATE: replace chars (like multi-char REPLACE)\n-- Remove parentheses and dashes from phone numbers\nSELECT PhoneNumber,\n       TRANSLATE(PhoneNumber, '()-', '   ') AS CleanPhone\nFROM dbo.Contacts;\n\n-- TRANSLATE to convert brackets to parentheses\nSELECT TRANSLATE('[1,2,3]', '[]', '()');  -- returns (1,2,3)"
                        },
                        {
                            'type': 'important',
                            'body': 'DIFFERENCE returns 4 when strings are phonetically identical and 0 when completely different. A threshold of >= 3 is commonly used for fuzzy name matching.'
                        },
                        {
                            'type': 'tip',
                            'body': 'TRANSLATE replaces characters one-for-one (from_chars[i] replaced by to_chars[i]). Both arguments must have the same length. Use it for bulk character substitution.'
                        }
                    ],
                    'quiz': [
                        {
                            'q': "What does SOUNDEX('Smith') return?",
                            'opts': ["A. 'SMITH'", "B. 'S530'", "C. '5300'", "D. 'SM30'"],
                            'correct': 'B',
                            'explain': 'SOUNDEX returns a 4-character code starting with the first letter followed by 3 digits representing phonetic sounds.'
                        },
                        {
                            'q': 'DIFFERENCE returns 4. What does that mean?',
                            'opts': [
                                'A. Strings are identical',
                                'B. Strings sound very similar (best phonetic match)',
                                'C. Strings are completely different',
                                'D. SOUNDEX codes differ by 4 characters'
                            ],
                            'correct': 'B',
                            'explain': 'DIFFERENCE 4 = maximum phonetic similarity. 0 = completely different.'
                        },
                        {
                            'q': 'Which SQL Server version introduced TRANSLATE?',
                            'opts': ['A. 2014', 'B. 2016', 'C. 2017', 'D. 2019'],
                            'correct': 'C',
                            'explain': 'TRANSLATE was introduced in SQL Server 2017.'
                        },
                        {
                            'q': "What is TRANSLATE('(123)-456', '()-', '   ') equivalent to?",
                            'opts': ['A. Removes all spaces', 'B. Replaces (, ), - with spaces', 'C. Extracts digits only', 'D. Reverses the string'],
                            'correct': 'B',
                            'explain': 'TRANSLATE replaces each from_char with the corresponding to_char: ( becomes space, ) becomes space, - becomes space.'
                        },
                        {
                            'q': 'How is TRANSLATE different from REPLACE?',
                            'opts': [
                                'A. TRANSLATE is faster',
                                'B. TRANSLATE replaces multiple characters in one call; REPLACE handles one substring at a time',
                                'C. REPLACE handles characters; TRANSLATE handles substrings',
                                'D. They are identical'
                            ],
                            'correct': 'B',
                            'explain': 'TRANSLATE replaces each character from a set with a corresponding character. REPLACE replaces occurrences of a specific substring with another substring.'
                        }
                    ]
                },
                {
                    'id': 'lp1-m3-u7',
                    'title': 'Graph queries in SQL Server',
                    'type': 'lesson',
                    'estimated_time': 15,
                    'objectives': ['Create node and edge tables', 'Query relationships with MATCH'],
                    'content': [
                        {
                            'type': 'theory',
                            'title': 'SQL Server Graph',
                            'body': 'SQL Server supports graph databases natively (SQL Server 2017+). Key concepts:<ul><li><strong>Node table</strong> - <code>AS NODE</code>: each row is a graph node; has <code>$node_id</code></li><li><strong>Edge table</strong> - <code>AS EDGE</code>: each row is a relationship with <code>$from_id</code>, <code>$to_id</code>, plus custom columns</li><li><strong>MATCH</strong> clause - expresses relationship patterns like (a)-[edge]->(b)</li></ul>Use for social networks, org hierarchies, recommendation engines, fraud detection.'
                        },
                        {
                            'type': 'sql_block',
                            'title': 'Create Graph Tables and Query',
                            'code': "-- Create node tables\nCREATE TABLE dbo.Person\n(\n    PersonID INT PRIMARY KEY,\n    Name     NVARCHAR(100)\n) AS NODE;\n\nCREATE TABLE dbo.City\n(\n    CityID   INT PRIMARY KEY,\n    CityName NVARCHAR(100)\n) AS NODE;\n\n-- Create edge table\nCREATE TABLE dbo.LivesIn\n(\n    Since DATE\n) AS EDGE;\n\n-- Insert nodes\nINSERT INTO dbo.Person VALUES (1, 'Alice'), (2, 'Bob');\nINSERT INTO dbo.City   VALUES (10, 'Seattle'), (11, 'Portland');\n\n-- Insert edges ($from_id, $to_id use $node_id values)\nINSERT INTO dbo.LivesIn ($from_id, $to_id, Since)\nSELECT p.$node_id, c.$node_id, '2020-01-01'\nFROM dbo.Person p, dbo.City c\nWHERE p.Name = 'Alice' AND c.CityName = 'Seattle';\n\n-- MATCH query: who lives in which city?\nSELECT p.Name, c.CityName, li.Since\nFROM dbo.Person p, dbo.LivesIn li, dbo.City c\nWHERE MATCH(p-(li)->c);\n\n-- Friends of friends (multi-hop)\nSELECT p1.Name AS Person, p3.Name AS FriendOfFriend\nFROM dbo.Person p1, dbo.Knows k1, dbo.Person p2,\n     dbo.Knows k2, dbo.Person p3\nWHERE MATCH(p1-(k1)->p2-(k2)->p3);"
                        },
                        {
                            'type': 'important',
                            'body': 'Node tables have a system-generated $node_id column. Edge tables have $from_id and $to_id. You do not create these columns manually - they are added automatically by AS NODE / AS EDGE.'
                        },
                        {
                            'type': 'tip',
                            'body': 'The MATCH clause syntax is (node1-(edge)->node2). The arrow direction matters. You can chain multiple hops in one MATCH expression.'
                        }
                    ],
                    'quiz': [
                        {
                            'q': 'What keyword creates a graph node table?',
                            'opts': ['A. AS VERTEX', 'B. AS NODE', 'C. AS GRAPH', 'D. AS ENTITY'],
                            'correct': 'B',
                            'explain': 'AS NODE at the end of CREATE TABLE marks it as a graph node table with a system $node_id column.'
                        },
                        {
                            'q': 'Which column in an edge table references the source node?',
                            'opts': ['A. $node_id', 'B. $source_id', 'C. $from_id', 'D. $start_id'],
                            'correct': 'C',
                            'explain': 'Edge tables have $from_id (source node) and $to_id (target node).'
                        },
                        {
                            'q': 'What is the MATCH clause used for?',
                            'opts': [
                                'A. String pattern matching',
                                'B. Expressing node-edge-node traversal patterns in graph queries',
                                'C. Fuzzy string matching',
                                'D. JSON path matching'
                            ],
                            'correct': 'B',
                            'explain': 'MATCH expresses graph traversal patterns: (node1-(edge)->node2).'
                        },
                        {
                            'q': 'What SQL Server version introduced graph tables?',
                            'opts': ['A. 2014', 'B. 2016', 'C. 2017', 'D. 2019'],
                            'correct': 'C',
                            'explain': 'Graph node and edge tables (AS NODE, AS EDGE) were introduced in SQL Server 2017.'
                        },
                        {
                            'q': 'In MATCH(p-(li)->c), what does the arrow indicate?',
                            'opts': [
                                'A. Sort direction',
                                'B. Direction of the edge relationship (from p through li to c)',
                                'C. Foreign key direction',
                                'D. Join direction'
                            ],
                            'correct': 'B',
                            'explain': 'The arrow in MATCH shows traversal direction: p is the source node, li is the edge, c is the target node.'
                        }
                    ]
                },
                {
                    'id': 'lp1-m3-u8',
                    'title': 'Correlated subqueries',
                    'type': 'lesson',
                    'estimated_time': 15,
                    'objectives': ['Write correlated subqueries', 'Use EXISTS and NOT EXISTS'],
                    'content': [
                        {
                            'type': 'theory',
                            'title': 'Correlated Subqueries',
                            'body': 'A <strong>correlated subquery</strong> references columns from the outer query - it re-executes for each row of the outer query. Use cases:<ul><li>EXISTS / NOT EXISTS - check row existence efficiently</li><li>Scalar correlated subquery - compute a value per outer row</li></ul>EXISTS stops as soon as the first matching row is found (short-circuit). NOT EXISTS has a NULL danger with NOT IN: if the subquery returns any NULL, NOT IN returns no rows at all.'
                        },
                        {
                            'type': 'sql_block',
                            'title': 'EXISTS, NOT EXISTS, Correlated Subquery',
                            'code': '-- EXISTS: customers who have at least one order\nSELECT c.CustomerID, c.FirstName\nFROM dbo.Customers c\nWHERE EXISTS\n(\n    SELECT 1\n    FROM dbo.Orders o\n    WHERE o.CustomerID = c.CustomerID  -- correlated: references outer c\n);\n\n-- NOT EXISTS: customers with NO orders\nSELECT c.CustomerID, c.FirstName\nFROM dbo.Customers c\nWHERE NOT EXISTS\n(\n    SELECT 1 FROM dbo.Orders o\n    WHERE o.CustomerID = c.CustomerID\n);\n\n-- NOT IN NULL danger - avoid when subquery may have NULLs\n-- This returns NO rows if Orders.CustomerID has any NULL!\nSELECT CustomerID FROM dbo.Customers\nWHERE CustomerID NOT IN (SELECT CustomerID FROM dbo.Orders);\n\n-- Safe version using NOT EXISTS\nSELECT CustomerID FROM dbo.Customers c\nWHERE NOT EXISTS (\n    SELECT 1 FROM dbo.Orders o WHERE o.CustomerID = c.CustomerID\n);\n\n-- Scalar correlated subquery\nSELECT c.CustomerID, c.FirstName,\n       (SELECT SUM(o.TotalAmount)\n        FROM dbo.Orders o\n        WHERE o.CustomerID = c.CustomerID) AS LifetimeValue\nFROM dbo.Customers c;'
                        },
                        {
                            'type': 'important',
                            'body': 'Avoid NOT IN when the subquery can return NULL values. If any NULL exists in the subquery result, NOT IN returns no rows (because NULL = anything is UNKNOWN). Use NOT EXISTS instead.'
                        },
                        {
                            'type': 'tip',
                            'body': 'EXISTS only cares whether at least one row matches - use SELECT 1 (not SELECT *) inside EXISTS for clarity and to avoid confusion about which columns are returned.'
                        }
                    ],
                    'quiz': [
                        {
                            'q': 'What does EXISTS return when the subquery finds at least one row?',
                            'opts': ['A. The first row', 'B. A count', 'C. TRUE (1)', 'D. NULL'],
                            'correct': 'C',
                            'explain': 'EXISTS returns TRUE if the subquery returns at least one row, regardless of the columns selected.'
                        },
                        {
                            'q': 'Why is NOT IN dangerous when the subquery can return NULL?',
                            'opts': [
                                'A. It causes a syntax error',
                                'B. NULL comparisons are UNKNOWN, so NOT IN returns no rows when any NULL exists',
                                'C. NULL is treated as zero',
                                'D. It returns extra rows'
                            ],
                            'correct': 'B',
                            'explain': 'If the subquery returns any NULL, every comparison in NOT IN becomes UNKNOWN, filtering out all rows.'
                        },
                        {
                            'q': "What makes a subquery 'correlated'?",
                            'opts': [
                                'A. It uses GROUP BY',
                                'B. It references a column from the outer query',
                                'C. It uses a CTE',
                                'D. It has a window function'
                            ],
                            'correct': 'B',
                            'explain': 'A correlated subquery references a column from the outer query, causing it to re-execute for each outer row.'
                        },
                        {
                            'q': 'What does SELECT 1 inside EXISTS mean?',
                            'opts': [
                                'A. Only returns 1 row',
                                'B. Returns the number 1 - EXISTS only checks row existence, not values',
                                'C. Counts rows in the subquery',
                                'D. Returns the first column'
                            ],
                            'correct': 'B',
                            'explain': 'The SELECT list inside EXISTS is irrelevant - only whether any row matches matters. SELECT 1 is a convention to signal intent.'
                        },
                        {
                            'q': 'When would you use a scalar correlated subquery instead of a JOIN?',
                            'opts': [
                                'A. When the subquery returns many columns',
                                'B. When computing one aggregated value per outer row without multiplying rows',
                                'C. When using GROUP BY',
                                'D. When joining on text columns'
                            ],
                            'correct': 'B',
                            'explain': 'A scalar correlated subquery computes one value per outer row without inflating the result set the way an uncorrelated aggregate JOIN might.'
                        }
                    ]
                },
                {
                    'id': 'lp1-m3-u9',
                    'title': 'Error handling with TRY/CATCH',
                    'type': 'lesson',
                    'estimated_time': 15,
                    'objectives': ['Use BEGIN TRY/CATCH', 'Use ERROR_* functions', 'Use THROW and RAISERROR'],
                    'content': [
                        {
                            'type': 'theory',
                            'title': 'T-SQL Error Handling',
                            'body': 'T-SQL error handling uses <code>BEGIN TRY...END TRY / BEGIN CATCH...END CATCH</code> blocks. Inside CATCH, use these functions:<ul><li><code>ERROR_NUMBER()</code> - error number</li><li><code>ERROR_MESSAGE()</code> - error message text</li><li><code>ERROR_SEVERITY()</code> - severity level</li><li><code>ERROR_STATE()</code> - error state</li><li><code>ERROR_LINE()</code> - line where error occurred</li><li><code>ERROR_PROCEDURE()</code> - procedure name where error occurred</li></ul>Raising errors: <code>THROW</code> (preferred, SQL 2012+) or <code>RAISERROR</code> (legacy). Bare <code>THROW</code> in CATCH re-raises the caught error.'
                        },
                        {
                            'type': 'sql_block',
                            'title': 'TRY/CATCH and THROW',
                            'code': "-- Basic TRY/CATCH\nBEGIN TRY\n    INSERT INTO dbo.Orders (CustomerID, TotalAmount)\n    VALUES (999, -50.00);  -- will fail FK or CHECK\nEND TRY\nBEGIN CATCH\n    SELECT\n        ERROR_NUMBER()    AS ErrNum,\n        ERROR_MESSAGE()   AS ErrMsg,\n        ERROR_SEVERITY()  AS ErrSev,\n        ERROR_STATE()     AS ErrState,\n        ERROR_LINE()      AS ErrLine,\n        ERROR_PROCEDURE() AS ErrProc;\nEND CATCH;\n\n-- THROW: raise a custom error\nTHROW 50001, 'CustomerID does not exist', 1;\n\n-- Bare THROW in CATCH: re-raise original error\nBEGIN TRY\n    DELETE FROM dbo.Customers WHERE CustomerID = 1;\nEND TRY\nBEGIN CATCH\n    -- Log to error table\n    INSERT INTO dbo.ErrorLog (ErrorMsg, LogTime)\n    VALUES (ERROR_MESSAGE(), GETDATE());\n    THROW;  -- re-raise with original error number\nEND CATCH;\n\n-- RAISERROR (legacy, but still common)\nRAISERROR('Custom error %s occurred', 16, 1, 'test');\n\n-- TRY/CATCH with transaction rollback\nBEGIN TRY\n    BEGIN TRANSACTION;\n        UPDATE dbo.Accounts SET Balance = Balance - 100 WHERE AccountID = 1;\n        UPDATE dbo.Accounts SET Balance = Balance + 100 WHERE AccountID = 2;\n    COMMIT TRANSACTION;\nEND TRY\nBEGIN CATCH\n    IF @@TRANCOUNT > 0\n        ROLLBACK TRANSACTION;\n    THROW;\nEND CATCH;"
                        },
                        {
                            'type': 'important',
                            'body': 'Always check @@TRANCOUNT > 0 before ROLLBACK in a CATCH block. If no transaction is active, ROLLBACK raises an error. Use bare THROW (no arguments) to re-raise the caught error unchanged.'
                        },
                        {
                            'type': 'tip',
                            'body': 'THROW (SQL 2012+) is preferred over RAISERROR for new code. THROW always raises with severity 16. RAISERROR allows custom severity but uses printf-style formatting.'
                        }
                    ],
                    'quiz': [
                        {
                            'q': 'Which function returns the error message text inside a CATCH block?',
                            'opts': ['A. ERROR_TEXT()', 'B. ERROR_MSG()', 'C. ERROR_MESSAGE()', 'D. CATCH_MESSAGE()'],
                            'correct': 'C',
                            'explain': 'ERROR_MESSAGE() returns the complete text of the error message caught in the CATCH block.'
                        },
                        {
                            'q': 'What does bare THROW (no arguments) do inside CATCH?',
                            'opts': [
                                'A. Raises a new generic error',
                                'B. Re-raises the original caught error unchanged',
                                'C. Suppresses the error',
                                'D. Commits the transaction'
                            ],
                            'correct': 'B',
                            'explain': 'THROW with no arguments re-raises the caught error with its original number, severity, and state.'
                        },
                        {
                            'q': 'Why check @@TRANCOUNT > 0 before ROLLBACK?',
                            'opts': [
                                'A. To count committed transactions',
                                'B. To avoid an error if no transaction is open',
                                'C. To enable nested transactions',
                                'D. To log the transaction count'
                            ],
                            'correct': 'B',
                            'explain': 'ROLLBACK raises an error if no transaction is active. Checking @@TRANCOUNT > 0 ensures a transaction exists before rolling back.'
                        },
                        {
                            'q': "What is THROW 50001, 'message', 1 used for?",
                            'opts': [
                                'A. Re-raise a caught error',
                                'B. Raise a new custom error with number 50001',
                                'C. Log an error to the error table',
                                'D. Catch error number 50001'
                            ],
                            'correct': 'B',
                            'explain': 'THROW errorNumber, message, state raises a new error with a custom number (must be >= 50000), message, and state.'
                        },
                        {
                            'q': 'What error numbers are valid for custom THROW or RAISERROR?',
                            'opts': ['A. 1-50000', 'B. >= 50001', 'C. Any positive integer', 'D. >= 50000'],
                            'correct': 'B',
                            'explain': 'User-defined error numbers must be >= 50001 (50000 is reserved). RAISERROR accepts >= 50000.'
                        }
                    ]
                },
                {
                    'id': 'lp1-m3-u10',
                    'title': 'Exercise: Write advanced T-SQL',
                    'type': 'exercise',
                    'estimated_time': 30,
                    'objectives': ['Apply CTEs, window functions, JSON, pattern matching, and error handling'],
                    'content': [
                        {
                            'type': 'theory',
                            'title': 'Exercise Overview',
                            'body': 'Practice advanced T-SQL in SSMS: (1) Write a CTE to find top customers per region. (2) Use window functions to rank orders. (3) Read JSON data from a column. (4) Use LIKE and CHARINDEX to parse email domains. (5) Add TRY/CATCH with transaction rollback to a stored procedure.'
                        },
                        {
                            'type': 'sql_block',
                            'title': 'Exercise Tasks',
                            'code': "-- Task 1: CTE - rank customers by spend\nWITH CustomerSpend AS\n(\n    SELECT CustomerID, SUM(TotalAmount) AS TotalSpend\n    FROM dbo.Orders\n    GROUP BY CustomerID\n)\nSELECT c.FirstName, c.LastName, cs.TotalSpend,\n       RANK() OVER (ORDER BY cs.TotalSpend DESC) AS SpendRank\nFROM CustomerSpend cs\nJOIN dbo.Customers c ON cs.CustomerID = c.CustomerID;\n\n-- Task 2: Window functions - running total + percentile\nSELECT OrderID, CustomerID, TotalAmount,\n    SUM(TotalAmount) OVER (ORDER BY OrderID\n        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS RunningTotal,\n    NTILE(4) OVER (ORDER BY TotalAmount DESC) AS Quartile\nFROM dbo.Orders;\n\n-- Task 3: JSON - read metadata column\nSELECT OrderID,\n    JSON_VALUE(Metadata, '$.ShipMethod')  AS ShipMethod,\n    JSON_VALUE(Metadata, '$.Priority')    AS Priority\nFROM dbo.Orders\nWHERE ISJSON(Metadata) = 1;\n\n-- Task 4: Pattern matching - extract email domain\nSELECT Email,\n    SUBSTRING(Email, CHARINDEX('@', Email) + 1, LEN(Email)) AS Domain\nFROM dbo.Customers\nWHERE Email LIKE '%@%.%';\n\n-- Task 5: TRY/CATCH with transaction\nCREATE PROCEDURE dbo.usp_TransferFunds\n    @FromAccount INT, @ToAccount INT, @Amount DECIMAL(10,2)\nAS\nBEGIN\n    SET NOCOUNT ON;\n    BEGIN TRY\n        BEGIN TRANSACTION;\n            UPDATE dbo.Accounts SET Balance = Balance - @Amount WHERE AccountID = @FromAccount;\n            UPDATE dbo.Accounts SET Balance = Balance + @Amount WHERE AccountID = @ToAccount;\n        COMMIT TRANSACTION;\n    END TRY\n    BEGIN CATCH\n        IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;\n        THROW;\n    END CATCH;\nEND;\nGO"
                        },
                        {
                            'type': 'tip',
                            'body': "Test the TRY/CATCH by passing a negative amount or an AccountID that doesn't exist - the CATCH block should roll back and re-raise the error."
                        }
                    ],
                    'quiz': [
                        {
                            'q': 'In the exercise, which window function creates a running total?',
                            'opts': [
                                'A. RANK()',
                                'B. ROW_NUMBER()',
                                'C. SUM() OVER(ORDER BY ... ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)',
                                'D. NTILE(4)'
                            ],
                            'correct': 'C',
                            'explain': 'SUM() with OVER and ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW creates a cumulative (running) total.'
                        },
                        {
                            'q': "How do you extract the domain from 'user@example.com'?",
                            'opts': [
                                'A. RIGHT(Email, 10)',
                                "B. SUBSTRING(Email, CHARINDEX('@', Email) + 1, LEN(Email))",
                                "C. PATINDEX('%@%', Email)",
                                "D. REPLACE(Email, 'user', '')"
                            ],
                            'correct': 'B',
                            'explain': 'Find the @ position with CHARINDEX, then SUBSTRING from position+1 to end of string.'
                        },
                        {
                            'q': 'What validates that a column contains valid JSON before reading it?',
                            'opts': ['A. JSON_VALID(col)', 'B. TRY_JSON(col)', 'C. ISJSON(col) = 1', 'D. JSON_CHECK(col) > 0'],
                            'correct': 'C',
                            'explain': 'ISJSON(col) returns 1 for valid JSON and 0 for invalid. Filter with WHERE ISJSON(col) = 1.'
                        },
                        {
                            'q': 'In the TRY/CATCH procedure, what happens if the first UPDATE succeeds but the second fails?',
                            'opts': [
                                'A. First UPDATE stays; second is skipped',
                                'B. Both changes are committed',
                                'C. CATCH block rolls back both changes',
                                'D. First UPDATE is also rolled back only if XACT_ABORT is ON'
                            ],
                            'correct': 'C',
                            'explain': 'The CATCH block checks @@TRANCOUNT > 0 and calls ROLLBACK TRANSACTION, which undoes both UPDATEs.'
                        },
                        {
                            'q': 'NTILE(4) divides how many orders into 4 quartiles?',
                            'opts': [
                                'A. Exactly 4 orders',
                                'B. Any number of orders into 4 roughly equal groups',
                                'C. Only orders divisible by 4',
                                'D. Orders in 4 partitions'
                            ],
                            'correct': 'B',
                            'explain': 'NTILE(4) divides all rows in the window into 4 roughly equal buckets regardless of total row count.'
                        }
                    ]
                },
                {
                    'id': 'lp1-m3-u11',
                    'title': 'Module assessment',
                    'type': 'knowledge_check',
                    'estimated_time': 15,
                    'objectives': ['Assess advanced T-SQL knowledge'],
                    'content': [
                        {
                            'type': 'theory',
                            'title': 'Module Assessment',
                            'body': 'This assessment covers all topics from Module 3. Select the best answer for each question.'
                        }
                    ],
                    'quiz': [
                        {
                            'q': 'What is required to terminate a recursive CTE?',
                            'opts': [
                                'A. A MAXRECURSION hint',
                                'B. An anchor member with no recursive reference',
                                'C. OPTION(STOP)',
                                'D. A WHERE Level = 0 clause'
                            ],
                            'correct': 'B',
                            'explain': 'The anchor member (with no self-reference) terminates the recursion by providing base rows. The recursive member joins back to the CTE name.'
                        },
                        {
                            'q': 'You want customer rows plus their order count WITHOUT removing customers with 0 orders. Best approach?',
                            'opts': [
                                'A. INNER JOIN with COUNT()',
                                'B. CTe with HAVING count > 0',
                                'C. LEFT JOIN with COUNT(o.OrderID)',
                                'D. Subquery with EXISTS'
                            ],
                            'correct': 'C',
                            'explain': 'LEFT JOIN keeps all customers. COUNT(o.OrderID) counts only matched rows (returns 0 for customers with no orders).'
                        },
                        {
                            'q': 'RANK() vs DENSE_RANK(): rows ranked 2,2,? When is next rank 3 vs 4?',
                            'opts': ['A. RANK gives 3; DENSE_RANK gives 4', 'B. DENSE_RANK gives 3; RANK gives 4', 'C. Both give 3', 'D. Both give 4'],
                            'correct': 'B',
                            'explain': 'DENSE_RANK gives 3 (no gap). RANK skips to 4 (gap for the tied position).'
                        },
                        {
                            'q': 'JSON_VALUE vs JSON_QUERY: use JSON_QUERY when extracting...?',
                            'opts': ['A. A number', 'B. A string', 'C. A nested JSON object or array', 'D. A boolean'],
                            'correct': 'C',
                            'explain': 'JSON_QUERY extracts objects or arrays. JSON_VALUE extracts scalars (strings, numbers).'
                        },
                        {
                            'q': 'Safest way to find customers with no orders (possible NULL CustomerID in Orders)?',
                            'opts': [
                                'A. NOT IN (SELECT CustomerID FROM Orders)',
                                'B. LEFT JOIN WHERE o.CustomerID IS NULL',
                                'C. NOT EXISTS (SELECT 1 FROM Orders WHERE CustomerID = c.CustomerID)',
                                'D. A and C both work safely'
                            ],
                            'correct': 'C',
                            'explain': 'NOT EXISTS is NULL-safe. NOT IN returns no rows if any NULL exists in the subquery. LEFT JOIN IS NULL works but NOT EXISTS is semantically clearest.'
                        }
                    ]
                },
                {
                    'id': 'lp1-m3-u12',
                    'title': 'Summary',
                    'type': 'summary',
                    'estimated_time': 5,
                    'objectives': ['Review Module 3 key concepts'],
                    'content': [
                        {
                            'type': 'theory',
                            'title': 'Module 3 Summary',
                            'body': 'Advanced T-SQL features covered in this module:<ul><li><strong>CTEs</strong> - WITH name AS (SELECT...); chain with commas; recursive needs anchor + UNION ALL + recursive member + MAXRECURSION</li><li><strong>Window functions</strong> - OVER(PARTITION BY ... ORDER BY ... ROWS BETWEEN ...); RANK/DENSE_RANK/ROW_NUMBER/NTILE; LAG/LEAD; SUM OVER for running totals</li><li><strong>JSON</strong> - JSON_VALUE (scalar), JSON_QUERY (object/array), OPENJSON WITH (schema), FOR JSON PATH/AUTO, ISJSON</li><li><strong>Pattern matching</strong> - LIKE (%_[set][^set] ESCAPE); CHARINDEX returns 0 if not found; PATINDEX accepts LIKE wildcards</li><li><strong>Fuzzy strings</strong> - SOUNDEX (phonetic code), DIFFERENCE (0-4 scale), TRANSLATE (char-to-char replacement)</li><li><strong>Graph</strong> - AS NODE, AS EDGE, MATCH(n1-(e)->n2)</li><li><strong>Correlated subqueries</strong> - EXISTS/NOT EXISTS; avoid NOT IN with NULLs</li><li><strong>Error handling</strong> - TRY/CATCH; ERROR_NUMBER/MESSAGE/SEVERITY; bare THROW; @@TRANCOUNT check before ROLLBACK</li></ul>'
                        },
                        {
                            'type': 'tip',
                            'body': "Exam reminders: DENSE_RANK has no gaps; NOT IN is NULL-unsafe; JSON_VALUE = scalar, JSON_QUERY = object/array; THROW re-raises, THROW n,'msg',s raises new; MAXRECURSION default is 100."
                        }
                    ],
                    'quiz': [
                        {
                            'q': 'Which window function has no rank gaps after ties?',
                            'opts': ['A. RANK()', 'B. ROW_NUMBER()', 'C. DENSE_RANK()', 'D. NTILE()'],
                            'correct': 'C',
                            'explain': 'DENSE_RANK assigns consecutive ranks with no gaps even after ties.'
                        },
                        {
                            'q': "What does OPENJSON WITH (col type 'path') do?",
                            'opts': [
                                'A. Generates JSON',
                                'B. Validates JSON',
                                'C. Parses JSON into a typed relational result set',
                                'D. Extracts a scalar value'
                            ],
                            'correct': 'C',
                            'explain': 'OPENJSON with a WITH clause parses JSON into rows and columns with specified data types.'
                        },
                        {
                            'q': 'A recursive CTE with no MAXRECURSION hint - what is the default limit?',
                            'opts': ['A. 10', 'B. 50', 'C. 100', 'D. 1000'],
                            'correct': 'C',
                            'explain': 'The default MAXRECURSION is 100. Use OPTION(MAXRECURSION 0) for unlimited.'
                        },
                        {
                            'q': "CHARINDEX('@', 'user@example.com') returns what?",
                            'opts': ['A. 5', 'B. 4', "C. '@'", 'D. 0'],
                            'correct': 'A',
                            'explain': "CHARINDEX is 1-based. 'u'=1, 's'=2, 'e'=3, 'r'=4, '@'=5. Returns 5."
                        },
                        {
                            'q': 'You have a CATCH block that logs the error and must re-raise it. Correct code?',
                            'opts': [
                                'A. THROW ERROR_NUMBER(), ERROR_MESSAGE(), 1;',
                                'B. RAISERROR(ERROR_MESSAGE(), 16, 1);',
                                'C. THROW;',
                                'D. RETURN ERROR_NUMBER();'
                            ],
                            'correct': 'C',
                            'explain': 'Bare THROW with no arguments re-raises the caught error with its original number, message, severity, and state.'
                        }
                    ]
                }
            ]
        },


        # ================================================================
        # MODULE 4: Implement SQL solutions by using AI-assisted tools
        # ================================================================
        {
            'id': 'lp1-m4',
            'title': 'Implement SQL solutions by using AI-assisted tools',
            'description': 'Use GitHub Copilot, Fabric Copilot, MCP, and instruction files to build AI-assisted SQL solutions securely.',
            'units': [
                {
                    'id': 'lp1-m4-u1',
                    'title': 'Introduction',
                    'type': 'intro',
                    'estimated_time': 5,
                    'objectives': ['Preview AI-assisted SQL development tools'],
                    'content': [
                        {
                            'type': 'theory',
                            'title': 'AI Tools for SQL Development',
                            'body': 'Module 4 covers AI-assisted tools for SQL development tested on DP-800:<ul><li><strong>GitHub Copilot</strong> - AI code completion in VS Code; generates T-SQL from natural language comments</li><li><strong>Microsoft Fabric Copilot</strong> - AI assistant inside Microsoft Fabric; requires F64+ capacity</li><li><strong>Security considerations</strong> - SQL injection via AI, prompt injection, least-privilege connections</li><li><strong>MCP (Model Context Protocol)</strong> - connects AI assistants to data sources</li><li><strong>Copilot instruction files</strong> - .github/copilot-instructions.md for customizing AI behavior</li></ul>'
                        },
                        {
                            'type': 'tip',
                            'body': 'Always review AI-generated SQL before running it. AI tools can generate syntactically correct but logically incorrect or insecure code.'
                        }
                    ],
                    'quiz': [
                        {
                            'q': 'What is GitHub Copilot?',
                            'opts': ['A. A SQL database', 'B. An AI code completion tool', 'C. A Microsoft Fabric feature', 'D. A T-SQL function'],
                            'correct': 'B',
                            'explain': 'GitHub Copilot is an AI pair programmer that suggests code completions, including T-SQL, based on context and comments.'
                        },
                        {
                            'q': 'What capacity is required to use Microsoft Fabric Copilot?',
                            'opts': ['A. F4', 'B. F16', 'C. F64', 'D. F128'],
                            'correct': 'C',
                            'explain': 'Fabric Copilot requires at least F64 capacity to be enabled.'
                        },
                        {
                            'q': 'What security risk exists when using AI to generate SQL?',
                            'opts': [
                                'A. Code runs too slowly',
                                'B. AI-generated SQL may contain SQL injection vulnerabilities',
                                'C. AI only works with NoSQL',
                                'D. Fabric Copilot requires admin rights always'
                            ],
                            'correct': 'B',
                            'explain': 'AI can generate code that is vulnerable to SQL injection if not reviewed carefully.'
                        },
                        {
                            'q': 'What does MCP stand for in the context of AI tools?',
                            'opts': [
                                'A. Microsoft Copilot Protocol',
                                'B. Model Context Protocol',
                                'C. Multi-Cloud Processing',
                                'D. Managed Connection Provider'
                            ],
                            'correct': 'B',
                            'explain': 'MCP (Model Context Protocol) is an open standard that lets AI assistants connect to external data sources and tools.'
                        },
                        {
                            'q': 'Where do you install GitHub Copilot for SQL development?',
                            'opts': ['A. SSMS extension gallery', 'B. Azure Portal', 'C. VS Code extensions', 'D. SQL Server Management Studio only'],
                            'correct': 'C',
                            'explain': 'GitHub Copilot is installed as an extension in Visual Studio Code.'
                        }
                    ]
                },
                {
                    'id': 'lp1-m4-u2',
                    'title': 'AI development tools for SQL',
                    'type': 'lesson',
                    'estimated_time': 20,
                    'objectives': ['Use GitHub Copilot for T-SQL', 'Use Fabric Copilot in Microsoft Fabric'],
                    'content': [
                        {
                            'type': 'theory',
                            'title': 'GitHub Copilot and Fabric Copilot',
                            'body': "<strong>GitHub Copilot in VS Code</strong>:<ul><li>Install 'GitHub Copilot' extension from VS Code marketplace</li><li>Requires GitHub account with Copilot subscription (Individual, Business, or Enterprise)</li><li>Write a comment describing what you need - Copilot suggests the SQL</li><li>Accept with Tab, reject with Esc, see alternatives with Alt+[ / Alt+]</li><li>Open Copilot Chat with Ctrl+Shift+I for conversational prompts</li></ul><strong>Microsoft Fabric Copilot</strong>:<ul><li>Available in Fabric notebooks, SQL analytics endpoint, and Dataflow Gen2</li><li>Requires F64+ capacity AND admin must enable in Tenant settings</li><li>Can generate DAX, PySpark, SQL from natural language in the Fabric UI</li></ul>"
                        },
                        {
                            'type': 'sql_block',
                            'title': 'Using GitHub Copilot for T-SQL (VS Code workflow)',
                            'code': "-- Step 1: Open a .sql file in VS Code with Copilot extension installed\n\n-- Step 2: Write a descriptive comment and press Enter\n-- Create a stored procedure that returns the top N customers\n-- by total order amount for a given year\n\n-- Copilot will suggest something like:\nCREATE PROCEDURE dbo.usp_TopCustomers\n    @Year INT,\n    @TopN INT = 10\nAS\nBEGIN\n    SET NOCOUNT ON;\n    SELECT TOP (@TopN)\n           c.CustomerID,\n           c.FirstName + ' ' + c.LastName AS CustomerName,\n           SUM(o.TotalAmount) AS YearlySpend\n    FROM dbo.Customers c\n    JOIN dbo.Orders o ON c.CustomerID = o.CustomerID\n    WHERE YEAR(o.OrderDate) = @Year\n    GROUP BY c.CustomerID, c.FirstName, c.LastName\n    ORDER BY YearlySpend DESC;\nEND;\n\n-- Step 3: Review, test, and accept if correct\n-- Always validate: correct table names, no injection, right logic\n\n-- Copilot Chat (Ctrl+Shift+I): conversational prompts\n-- Example prompt: 'Explain what this query does'\n-- Example prompt: 'Optimize this query for performance'\n-- Example prompt: 'Add error handling to this procedure'"
                        },
                        {
                            'type': 'important',
                            'body': 'Always review AI-generated SQL for correctness before executing. Copilot may use wrong table names, generate non-sargable WHERE clauses, or miss NULL handling.'
                        },
                        {
                            'type': 'tip',
                            'body': 'Copilot works best with rich context. Open related files, have table creation scripts visible, and write detailed comments that include table names and column names.'
                        }
                    ],
                    'quiz': [
                        {
                            'q': 'How do you accept a GitHub Copilot suggestion in VS Code?',
                            'opts': ['A. Enter', 'B. Tab', 'C. Ctrl+Space', 'D. F5'],
                            'correct': 'B',
                            'explain': 'Press Tab to accept the current Copilot suggestion. Press Esc to reject it.'
                        },
                        {
                            'q': 'What keyboard shortcut opens GitHub Copilot Chat in VS Code?',
                            'opts': ['A. Ctrl+K', 'B. Ctrl+Shift+P', 'C. Ctrl+Shift+I', 'D. Alt+C'],
                            'correct': 'C',
                            'explain': 'Ctrl+Shift+I opens the GitHub Copilot Chat panel for conversational AI assistance.'
                        },
                        {
                            'q': 'What must an admin enable for Fabric Copilot to work?',
                            'opts': [
                                'A. Premium capacity P1',
                                'B. F64+ capacity AND Tenant settings toggle',
                                'C. Azure OpenAI service deployment',
                                'D. SQL Server 2022 license'
                            ],
                            'correct': 'B',
                            'explain': 'Fabric Copilot requires both F64+ capacity and the admin to enable it in Tenant settings.'
                        },
                        {
                            'q': 'What is the best first step after Copilot generates a stored procedure?',
                            'opts': [
                                'A. Deploy to production immediately',
                                'B. Review for correct table names, logic, and security before running',
                                'C. Run it 10 times to test speed',
                                'D. Add it to version control without testing'
                            ],
                            'correct': 'B',
                            'explain': 'AI-generated code must be reviewed for correctness, appropriate column names, NULL handling, and security before use.'
                        },
                        {
                            'q': 'In which tool does Fabric Copilot assist with SQL analytics?',
                            'opts': ['A. Azure Data Studio', 'B. SSMS', 'C. Microsoft Fabric SQL analytics endpoint', 'D. Power BI Desktop'],
                            'correct': 'C',
                            'explain': 'Fabric Copilot is available in Microsoft Fabric workloads including notebooks, SQL analytics endpoints, and Dataflow Gen2.'
                        }
                    ]
                },
                {
                    'id': 'lp1-m4-u3',
                    'title': 'Security impact of AI tools',
                    'type': 'lesson',
                    'estimated_time': 15,
                    'objectives': ['Identify SQL injection risks from AI tools', 'Understand prompt injection', 'Apply least privilege'],
                    'content': [
                        {
                            'type': 'theory',
                            'title': 'AI Security Risks',
                            'body': "AI tools introduce specific security concerns for SQL development:<ul><li><strong>SQL injection via AI</strong> - AI may generate code that concatenates user input directly into SQL strings instead of using parameterized queries</li><li><strong>Prompt injection</strong> - malicious instructions embedded in data can hijack an AI assistant's behavior (e.g., data in a table cell that says 'ignore previous instructions')</li><li><strong>Least privilege for AI connections</strong> - MCP servers and AI tools connecting to databases should use accounts with minimal permissions (read-only when possible)</li><li><strong>Data leakage</strong> - prompts sent to AI may include sensitive schema or data; use enterprise/on-premises deployments for sensitive environments</li></ul>"
                        },
                        {
                            'type': 'sql_block',
                            'title': 'SQL Injection Risk Example',
                            'code': "-- DANGEROUS: AI might generate concatenated SQL (NEVER do this)\nDECLARE @SQL NVARCHAR(MAX);\nSET @SQL = 'SELECT * FROM Orders WHERE CustomerName = ''' + @UserInput + '''';\nEXEC sp_executesql @SQL;\n-- If @UserInput = 'Alice'' OR 1=1--' -> returns ALL rows!\n\n-- SAFE: Use parameterized queries (sp_executesql with params)\nDECLARE @SafeSQL NVARCHAR(MAX) = N'SELECT * FROM Orders WHERE CustomerName = @Name';\nEXEC sp_executesql @SafeSQL,\n     N'@Name NVARCHAR(100)',\n     @Name = @UserInput;\n\n-- SAFE: Stored procedure with parameters (no dynamic SQL needed)\nCREATE PROCEDURE dbo.usp_GetByName @CustomerName NVARCHAR(100)\nAS\nBEGIN\n    SELECT * FROM dbo.Orders WHERE CustomerName = @CustomerName;\nEND;\n\n-- Least privilege: create read-only SQL login for AI tools\nCREATE LOGIN AICopilotLogin WITH PASSWORD = 'StrongP@ss1!';\nCREATE USER AICopilotUser FOR LOGIN AICopilotLogin;\nGRANT SELECT ON SCHEMA::dbo TO AICopilotUser;\n-- Do NOT grant INSERT, UPDATE, DELETE, EXEC to AI service accounts"
                        },
                        {
                            'type': 'important',
                            'body': 'Never use AI-generated code that builds SQL by concatenating user input. Always ensure parameterized queries or stored procedures are used. Review AI output for injection vulnerabilities before execution.'
                        },
                        {
                            'type': 'tip',
                            'body': 'When connecting AI tools (MCP, Copilot) to production databases, create a dedicated service account with read-only SELECT permissions on only the schemas the AI needs to access.'
                        }
                    ],
                    'quiz': [
                        {
                            'q': 'What is SQL injection via AI?',
                            'opts': [
                                'A. AI database attacks',
                                'B. AI generates unsafe SQL that concatenates user input without parameterization',
                                'C. Injecting AI into SQL queries',
                                'D. Using AI to bypass database logins'
                            ],
                            'correct': 'B',
                            'explain': 'AI tools may generate string concatenation SQL patterns that are vulnerable to SQL injection if not reviewed.'
                        },
                        {
                            'q': 'What is prompt injection?',
                            'opts': [
                                'A. Injecting SQL into prompts',
                                "B. Malicious instructions in data that hijack an AI assistant's behavior",
                                'C. A type of SQL attack on the database',
                                'D. Inserting prompts into stored procedures'
                            ],
                            'correct': 'B',
                            'explain': 'Prompt injection occurs when malicious text in data (e.g., table contents) tricks an AI assistant into following unintended instructions.'
                        },
                        {
                            'q': 'What permission level should an AI service account have on a production database?',
                            'opts': [
                                'A. sysadmin',
                                'B. db_owner',
                                'C. Minimum required - often SELECT only on needed schemas',
                                'D. db_datareader and db_datawriter'
                            ],
                            'correct': 'C',
                            'explain': 'AI service accounts should have least privilege - typically SELECT only on schemas the AI tool needs to read.'
                        },
                        {
                            'q': 'Which approach prevents SQL injection in dynamically built queries?',
                            'opts': [
                                'A. String concatenation with RTRIM',
                                'B. sp_executesql with typed parameters',
                                'C. Wrapping in TRY/CATCH',
                                'D. Adding a CHECK constraint'
                            ],
                            'correct': 'B',
                            'explain': 'sp_executesql with typed parameters treats user input as data, not executable SQL, preventing injection.'
                        },
                        {
                            'q': 'What data leakage risk exists when using cloud AI coding tools?',
                            'opts': [
                                'A. Queries run slower in the cloud',
                                'B. Schema and sensitive data in prompts may be sent to external AI services',
                                'C. AI tools delete data',
                                'D. Cloud AI cannot read SQL syntax'
                            ],
                            'correct': 'B',
                            'explain': 'When you prompt cloud AI with schema or sample data, that information is sent to the AI service. For sensitive data, use enterprise or on-premises AI deployments.'
                        }
                    ]
                },
                {
                    'id': 'lp1-m4-u4',
                    'title': 'Enable GitHub Copilot and Fabric Copilot',
                    'type': 'lesson',
                    'estimated_time': 15,
                    'objectives': ['Install GitHub Copilot in VS Code', 'Enable Fabric Copilot in Tenant settings'],
                    'content': [
                        {
                            'type': 'theory',
                            'title': 'Enabling AI Copilot Features',
                            'body': "<strong>GitHub Copilot setup (VS Code):</strong><ol><li>Open VS Code - go to Extensions (Ctrl+Shift+X)</li><li>Search for 'GitHub Copilot' and install</li><li>Sign in with a GitHub account that has Copilot access</li><li>Also install 'GitHub Copilot Chat' extension for conversational AI</li><li>Test: open a .sql file, write a comment, watch suggestions appear</li></ol><strong>Microsoft Fabric Copilot setup:</strong><ol><li>Admin must go to Fabric Admin portal > Tenant settings</li><li>Enable 'Copilot and Azure OpenAI Service' toggle</li><li>The capacity must be F64 or higher (F64, F128, F256, etc.)</li><li>Once enabled, Copilot icons appear in notebooks, SQL editors, and Dataflow Gen2</li></ol>"
                        },
                        {
                            'type': 'important',
                            'body': 'Fabric Copilot has TWO requirements that BOTH must be met: (1) F64+ capacity size AND (2) admin must enable the Copilot toggle in Tenant settings. Either alone is insufficient.'
                        },
                        {
                            'type': 'tip',
                            'body': 'GitHub Copilot Individual plan allows personal use. Copilot Business/Enterprise adds organization-level management, policy controls, and disables training on your code.'
                        }
                    ],
                    'quiz': [
                        {
                            'q': 'Where do you install the GitHub Copilot extension?',
                            'opts': [
                                'A. GitHub website settings',
                                'B. VS Code Extensions panel (Ctrl+Shift+X)',
                                'C. Azure Portal',
                                'D. SQL Server Configuration Manager'
                            ],
                            'correct': 'B',
                            'explain': "GitHub Copilot is installed through the VS Code Extensions panel (Ctrl+Shift+X), searching for 'GitHub Copilot'."
                        },
                        {
                            'q': 'What are the TWO requirements for Fabric Copilot?',
                            'opts': [
                                'A. F64+ capacity AND admin enables in Tenant settings',
                                'B. P1 Premium AND service principal',
                                'C. Azure OpenAI deployment AND F32 capacity',
                                'D. Power BI Premium AND admin consent'
                            ],
                            'correct': 'A',
                            'explain': 'Both conditions are required: F64+ capacity size AND the admin must enable the Copilot toggle in Fabric Tenant settings.'
                        },
                        {
                            'q': 'Where does a Fabric admin enable Copilot?',
                            'opts': [
                                'A. Azure Active Directory',
                                'B. Fabric Admin portal > Tenant settings',
                                'C. Power BI settings',
                                'D. SQL Server Management Studio'
                            ],
                            'correct': 'B',
                            'explain': 'The Fabric admin enables Copilot in the Fabric Admin portal under Tenant settings > Copilot and Azure OpenAI Service.'
                        },
                        {
                            'q': 'What account is needed to use GitHub Copilot?',
                            'opts': [
                                'A. Microsoft account',
                                'B. Azure account',
                                'C. GitHub account with Copilot subscription',
                                'D. Admin account on the local machine'
                            ],
                            'correct': 'C',
                            'explain': 'GitHub Copilot requires a GitHub account with an active Copilot subscription (Individual, Business, or Enterprise).'
                        },
                        {
                            'q': 'In which Fabric experiences does Copilot appear once enabled?',
                            'opts': [
                                'A. Only in Power BI dashboards',
                                'B. Notebooks, SQL analytics endpoint, and Dataflow Gen2',
                                'C. Only in Fabric pipelines',
                                'D. Only in Lakehouse explorer'
                            ],
                            'correct': 'B',
                            'explain': 'Once enabled, Fabric Copilot is available in notebooks, the SQL analytics endpoint editor, and Dataflow Gen2.'
                        }
                    ]
                },
                {
                    'id': 'lp1-m4-u5',
                    'title': 'Configure MCP options',
                    'type': 'lesson',
                    'estimated_time': 20,
                    'objectives': ['Understand MCP architecture', 'Create mcp.json configuration', 'Choose transport type'],
                    'content': [
                        {
                            'type': 'theory',
                            'title': 'Model Context Protocol (MCP)',
                            'body': '<strong>MCP (Model Context Protocol)</strong> is an open standard that lets AI assistants connect to external tools and data sources. Key concepts:<ul><li><strong>MCP Server</strong> - exposes tools, resources, or prompts to the AI client</li><li><strong>MCP Client</strong> - the AI assistant (e.g., GitHub Copilot Chat, Claude) that calls the server</li><li><strong>Transport types</strong>: <ul><li><code>stdio</code> - spawns a local process; communicates via stdin/stdout; good for local tools</li><li><code>http/SSE</code> - connects to a remote HTTP endpoint; good for cloud services</li></ul></li><li><strong>mcp.json</strong> - configuration file that lists MCP servers and their settings</li></ul>'
                        },
                        {
                            'type': 'sql_block',
                            'title': 'mcp.json Configuration Examples',
                            'code': '// mcp.json (place in .vscode/ or user-level settings)\n{\n  "servers": {\n    "mssql": {\n      "type": "stdio",\n      "command": "npx",\n      "args": ["-y", "@modelcontextprotocol/server-mssql"],\n      "env": {\n        "MSSQL_CONNECTION_STRING": "${env:MSSQL_CONN}"\n      }\n    },\n    "fabric-sql": {\n      "type": "http",\n      "url": "https://api.fabric.microsoft.com/v1/mcp",\n      "headers": {\n        "Authorization": "Bearer ${env:FABRIC_TOKEN}"\n      }\n    }\n  }\n}\n\n// Reference an MCP server in Copilot Chat:\n// @mssql What tables are in the Sales schema?\n// @fabric-sql Show me the top 10 rows from dbo.Orders'
                        },
                        {
                            'type': 'important',
                            'body': 'Use ${env:VARIABLE_NAME} in mcp.json to reference environment variables instead of hardcoding credentials. Never commit connection strings or tokens to source control.'
                        },
                        {
                            'type': 'tip',
                            'body': "The 'stdio' transport spawns a local process - good for local SQL Server connections. 'http/SSE' connects to a remote server - appropriate for cloud services like Microsoft Fabric."
                        }
                    ],
                    'quiz': [
                        {
                            'q': 'What does MCP stand for?',
                            'opts': [
                                'A. Microsoft Copilot Protocol',
                                'B. Model Context Protocol',
                                'C. Multi-Cloud Processing',
                                'D. Managed Connection Provider'
                            ],
                            'correct': 'B',
                            'explain': 'MCP stands for Model Context Protocol - an open standard for connecting AI assistants to external tools and data.'
                        },
                        {
                            'q': 'What transport type spawns a local process communicating via stdin/stdout?',
                            'opts': ['A. http', 'B. SSE', 'C. websocket', 'D. stdio'],
                            'correct': 'D',
                            'explain': 'stdio transport spawns a local command-line process and communicates with it through standard input and output.'
                        },
                        {
                            'q': 'How should you store credentials in mcp.json?',
                            'opts': [
                                'A. Hardcode them directly',
                                'B. Use ${env:VAR_NAME} to reference environment variables',
                                'C. Store in a comments section',
                                'D. Encode in base64'
                            ],
                            'correct': 'B',
                            'explain': 'Use ${env:VARIABLE_NAME} syntax in mcp.json to reference environment variables and avoid hardcoding secrets.'
                        },
                        {
                            'q': 'How do you reference an MCP server in GitHub Copilot Chat?',
                            'opts': ['A. /server-name command', 'B. @servername in the chat prompt', 'C. EXEC mcp.servername', 'D. --mcp flag'],
                            'correct': 'B',
                            'explain': 'In Copilot Chat, use @servername (the key from mcp.json servers object) to route the prompt to that MCP server.'
                        },
                        {
                            'q': 'Which transport is more appropriate for a remote Fabric SQL endpoint?',
                            'opts': ['A. stdio', 'B. websocket', 'C. http/SSE', 'D. named pipe'],
                            'correct': 'C',
                            'explain': 'http/SSE transport connects to a remote HTTP endpoint, suitable for cloud services like Microsoft Fabric APIs.'
                        }
                    ]
                },
                {
                    'id': 'lp1-m4-u6',
                    'title': 'Create Copilot instruction files',
                    'type': 'lesson',
                    'estimated_time': 15,
                    'objectives': ['Create .github/copilot-instructions.md', 'Use applyTo glob patterns'],
                    'content': [
                        {
                            'type': 'theory',
                            'title': 'Copilot Instruction Files',
                            'body': "You can customize GitHub Copilot's behavior using instruction files:<ul><li><strong>Location</strong>: <code>.github/copilot-instructions.md</code> in the repository root</li><li><strong>Purpose</strong>: provide persistent context to Copilot - coding standards, naming conventions, schema notes, SQL style guides</li><li><strong>Format</strong>: Markdown; Copilot reads this file automatically when active in that repo</li><li><strong>applyTo patterns</strong>: use glob patterns to apply instructions only to specific file types (e.g., <code>**/*.sql</code> for SQL files only)</li></ul>Instructions help Copilot generate code that follows your team's conventions without repeating them in every prompt."
                        },
                        {
                            'type': 'sql_block',
                            'title': '.github/copilot-instructions.md Example',
                            'code': '# Copilot Instructions for SQL Development\n\n## SQL Conventions\n- Always use two-part names: dbo.TableName\n- Prefix stored procedures with usp_, functions with fn_\n- Always include SET NOCOUNT ON in stored procedures\n- Use SCOPE_IDENTITY() not @@IDENTITY\n- Wrap DML in TRY/CATCH with THROW for error re-raising\n- Use parameterized queries - never concatenate user input\n\n## Naming\n- Tables: PascalCase singular (dbo.Customer, dbo.Order)\n- Columns: PascalCase (CustomerID, TotalAmount)\n- Indexes: IX_Table_Column, UX_Table_Column for unique\n\n## applyTo configuration (in settings.json):\n{\n  "github.copilot.chat.codeGeneration.instructions": [\n    {\n      "file": ".github/copilot-instructions.md",\n      "applyTo": "**/*.sql"\n    }\n  ]\n}'
                        },
                        {
                            'type': 'important',
                            'body': "The .github/copilot-instructions.md file must be committed to the repository root's .github folder. Copilot reads it automatically - no per-session setup needed."
                        },
                        {
                            'type': 'tip',
                            'body': 'Keep instruction files concise and specific. Copilot has a context window limit. Focus on the most important conventions: naming, error handling, and security rules.'
                        }
                    ],
                    'quiz': [
                        {
                            'q': 'Where does the Copilot instruction file live in a repository?',
                            'opts': [
                                'A. Root directory as copilot.md',
                                'B. .github/copilot-instructions.md',
                                'C. .vscode/copilot.json',
                                'D. docs/copilot-instructions.md'
                            ],
                            'correct': 'B',
                            'explain': 'The Copilot instruction file must be placed at .github/copilot-instructions.md in the repository root.'
                        },
                        {
                            'q': 'What format is the copilot-instructions.md file?',
                            'opts': ['A. JSON', 'B. YAML', 'C. Markdown', 'D. XML'],
                            'correct': 'C',
                            'explain': 'The Copilot instruction file is a Markdown (.md) file containing natural language instructions.'
                        },
                        {
                            'q': "What does an applyTo glob pattern like '**/*.sql' do?",
                            'opts': [
                                'A. Runs SQL files automatically',
                                'B. Applies the instructions only when working with .sql files',
                                'C. Uploads .sql files to GitHub',
                                'D. Prevents Copilot from editing .sql files'
                            ],
                            'correct': 'B',
                            'explain': 'applyTo limits which file types the instruction set applies to. **/*.sql means all .sql files in any subdirectory.'
                        },
                        {
                            'q': 'Why put SQL conventions in copilot-instructions.md?',
                            'opts': [
                                'A. It makes SQL run faster',
                                'B. Copilot reads it automatically and applies conventions without per-prompt repetition',
                                'C. It creates the database schema',
                                'D. It backs up SQL scripts'
                            ],
                            'correct': 'B',
                            'explain': "The instruction file provides persistent context to Copilot so you don't have to repeat conventions in every chat prompt."
                        },
                        {
                            'q': 'What kinds of content belong in a SQL copilot-instructions.md?',
                            'opts': [
                                'A. Actual data to query',
                                'B. Connection strings',
                                'C. Naming conventions, error handling patterns, and SQL style rules',
                                'D. Table row counts'
                            ],
                            'correct': 'C',
                            'explain': 'Good Copilot instructions contain coding conventions, naming patterns, security rules, and tool preferences - not data.'
                        }
                    ]
                },
                {
                    'id': 'lp1-m4-u7',
                    'title': 'Connect to MCP server endpoints',
                    'type': 'lesson',
                    'estimated_time': 15,
                    'objectives': ['Configure an MCP server for SQL Server', 'Query a database via Copilot Chat and MCP'],
                    'content': [
                        {
                            'type': 'theory',
                            'title': 'Connecting AI to SQL via MCP',
                            'body': 'MCP servers act as bridges between AI assistants and databases. A SQL Server MCP server can expose: schema information, query execution, stored procedure documentation. Setup steps:<ol><li>Install the MCP server package (e.g., via npm or pip)</li><li>Add the server entry to mcp.json with connection details from environment variables</li><li>Open GitHub Copilot Chat and use @servername to direct queries to it</li><li>The AI can now inspect schema, generate queries aware of your actual tables, and execute allowed operations</li></ol>The AI can then generate SQL that references real table and column names from your database instead of hallucinating schema.'
                        },
                        {
                            'type': 'sql_block',
                            'title': 'MCP Workflow Example',
                            'code': '// 1. Set environment variable (PowerShell)\n$env:MSSQL_CONN = "Server=.;Database=SalesDB;Trusted_Connection=True;"\n\n// 2. mcp.json entry\n{\n  "servers": {\n    "salesdb": {\n      "type": "stdio",\n      "command": "npx",\n      "args": ["-y", "@modelcontextprotocol/server-mssql"],\n      "env": {"MSSQL_CONNECTION_STRING": "${env:MSSQL_CONN}"}\n    }\n  }\n}\n\n// 3. In Copilot Chat:\n// @salesdb What tables exist in the Sales schema?\n// -> AI responds with actual table list from the database\n\n// @salesdb Write a query to find top 5 customers by revenue in 2024\n// -> AI generates a query using the actual column names it discovered\n\n// @salesdb Explain what the usp_GetCustomerOrders procedure does\n// -> AI reads the procedure definition and explains it'
                        },
                        {
                            'type': 'important',
                            'body': 'The AI account used by the MCP server must have only the permissions it needs. For a read-only assistant, grant SELECT only. Never use sa or a high-privilege account for AI tool connections.'
                        },
                        {
                            'type': 'tip',
                            'body': 'Test MCP connectivity with a simple schema question first: @servername list the tables in dbo schema. If it returns real tables, MCP is connected and working.'
                        }
                    ],
                    'quiz': [
                        {
                            'q': 'What is the main benefit of connecting Copilot to a database via MCP?',
                            'opts': [
                                'A. Faster query execution',
                                'B. AI can use real schema instead of guessing table/column names',
                                'C. Automatic query caching',
                                'D. Bypasses authentication'
                            ],
                            'correct': 'B',
                            'explain': 'MCP gives the AI access to real schema information, so generated queries reference actual tables and columns rather than hallucinated names.'
                        },
                        {
                            'q': 'How do you direct a Copilot Chat message to a specific MCP server?',
                            'opts': ['A. /connect servername', 'B. @servername in the message', 'C. MCP:servername prefix', 'D. #servername tag'],
                            'correct': 'B',
                            'explain': 'In Copilot Chat, prefix your message with @servername (matching the key in mcp.json) to route it to that MCP server.'
                        },
                        {
                            'q': 'What should you use for MCP connection credentials in mcp.json?',
                            'opts': [
                                'A. Hardcoded username and password',
                                'B. Environment variables via ${env:VAR}',
                                'C. Windows Registry values',
                                'D. Azure Key Vault SDK calls'
                            ],
                            'correct': 'B',
                            'explain': 'Use ${env:VAR_NAME} to pull credentials from environment variables, keeping secrets out of the configuration file.'
                        },
                        {
                            'q': 'Which permission should the MCP SQL Server account have for read-only AI assistance?',
                            'opts': ['A. db_owner', 'B. sysadmin', 'C. SELECT on required schemas only', 'D. db_datareader and db_datawriter'],
                            'correct': 'C',
                            'explain': 'Least privilege: grant SELECT on only the schemas the AI assistant needs to read. Avoid write permissions for read-only scenarios.'
                        },
                        {
                            'q': 'What type of MCP transport is appropriate for a local SQL Server on the same machine?',
                            'opts': ['A. http/SSE', 'B. websocket', 'C. stdio', 'D. TCP/IP named pipe'],
                            'correct': 'C',
                            'explain': 'stdio transport spawns a local process - perfect for a local MCP server connecting to an on-premises SQL Server.'
                        }
                    ]
                },
                {
                    'id': 'lp1-m4-u8',
                    'title': 'Exercise: AI-assisted SQL development',
                    'type': 'exercise',
                    'estimated_time': 25,
                    'objectives': ['Use GitHub Copilot to generate T-SQL', 'Configure a basic MCP connection', 'Create a copilot-instructions.md'],
                    'content': [
                        {
                            'type': 'theory',
                            'title': 'Exercise Overview',
                            'body': 'In this exercise: (1) Install GitHub Copilot in VS Code and generate a stored procedure using comment-to-code. (2) Create a .github/copilot-instructions.md with SQL conventions. (3) Configure a local MCP server entry in mcp.json. (4) Use Copilot Chat to query your database schema via MCP. (5) Review AI-generated code for security issues.'
                        },
                        {
                            'type': 'sql_block',
                            'title': 'Exercise Steps',
                            'code': '-- STEP 1: In VS Code with Copilot installed, create a new .sql file\n-- Write this comment and press Enter - Copilot will suggest the rest:\n\n-- Stored procedure: get all orders for a customer in a date range\n-- Parameters: @CustomerID INT, @StartDate DATE, @EndDate DATE\n-- Returns: OrderID, OrderDate, TotalAmount, ordered by date desc\n\n-- Accept Copilot suggestion with Tab, then review:\n-- 1. Does it use parameterized input? (no concatenation)\n-- 2. Does it have SET NOCOUNT ON?\n-- 3. Are table/column names correct for your database?\n-- 4. Is there appropriate error handling?\n\n-- STEP 2: Create .github/copilot-instructions.md\n-- Content to add:\n--   # SQL Standards\n--   - Use dbo. schema prefix on all objects\n--   - Prefix procs with usp_, functions with fn_\n--   - Always SET NOCOUNT ON in procedures\n--   - Use SCOPE_IDENTITY() not @@IDENTITY\n--   - Parameterize all queries\n\n-- STEP 3: Add mcp.json to .vscode/ folder\n-- { "servers": { "localdb": { "type": "stdio",\n--    "command": "npx", "args": ["-y", "@modelcontextprotocol/server-mssql"],\n--    "env": {"MSSQL_CONNECTION_STRING": "${env:MSSQL_CONN}"} } } }\n\n-- STEP 4: In Copilot Chat, test MCP:\n-- @localdb What tables exist in my database?\n-- @localdb Write a query to find orders over 500 in 2024\n\n-- STEP 5: Security review checklist for AI-generated code:\n-- [ ] No string concatenation with user input\n-- [ ] Parameters declared with correct data types\n-- [ ] TRY/CATCH present for DML operations\n-- [ ] No SELECT * in production procedures\n-- [ ] Schema prefix on all object references'
                        },
                        {
                            'type': 'tip',
                            'body': 'Save the security review checklist as a code snippet or add it to your copilot-instructions.md so Copilot generates code that already passes the checklist.'
                        }
                    ],
                    'quiz': [
                        {
                            'q': 'What is the first thing you should do after Copilot generates a stored procedure?',
                            'opts': [
                                'A. Run it in production',
                                'B. Check it for SQL injection, correct object names, and error handling',
                                'C. Commit to main branch',
                                'D. Share with the team'
                            ],
                            'correct': 'B',
                            'explain': 'Always review AI-generated code for security (no concatenation), correctness (right tables/columns), and completeness (error handling, SET NOCOUNT ON).'
                        },
                        {
                            'q': 'Where does the copilot-instructions.md file go?',
                            'opts': ['A. Root of the repo', 'B. .vscode/ folder', 'C. .github/ folder', 'D. src/ folder'],
                            'correct': 'C',
                            'explain': 'The file goes in the .github/ folder of the repository: .github/copilot-instructions.md.'
                        },
                        {
                            'q': 'After adding mcp.json, how do you test if MCP is working in Copilot Chat?',
                            'opts': [
                                'A. EXEC mcp.test',
                                'B. Type @servername list tables and check for real table names',
                                'C. Restart SQL Server',
                                'D. Run npm test'
                            ],
                            'correct': 'B',
                            'explain': 'Ask @servername to list tables - if it returns actual table names from your database, MCP is connected correctly.'
                        },
                        {
                            'q': 'Which is a dangerous pattern in AI-generated SQL?',
                            'opts': [
                                'A. SET NOCOUNT ON',
                                'B. SCOPE_IDENTITY()',
                                "C. 'SELECT * FROM Orders WHERE Name = ''' + @Input + ''''",
                                'D. BEGIN TRY/CATCH'
                            ],
                            'correct': 'C',
                            'explain': 'Concatenating user input into SQL strings creates SQL injection vulnerability. Always use parameterized queries.'
                        },
                        {
                            'q': 'What environment variable syntax in mcp.json keeps credentials safe?',
                            'opts': ['A. %VAR_NAME%', 'B. $VAR_NAME', 'C. ${env:VAR_NAME}', 'D. @{VAR_NAME}'],
                            'correct': 'C',
                            'explain': '${env:VAR_NAME} reads the value from the system environment variable, avoiding hardcoded credentials in mcp.json.'
                        }
                    ]
                },
                {
                    'id': 'lp1-m4-u9',
                    'title': 'Module assessment',
                    'type': 'knowledge_check',
                    'estimated_time': 10,
                    'objectives': ['Assess AI tool knowledge for DP-800'],
                    'content': [
                        {
                            'type': 'theory',
                            'title': 'Module 4 Assessment',
                            'body': 'Test your understanding of AI-assisted SQL development tools and security practices.'
                        }
                    ],
                    'quiz': [
                        {
                            'q': 'Fabric Copilot is available but generating no responses. Admin verified F64 capacity. What else must be checked?',
                            'opts': [
                                'A. Install npm packages',
                                'B. Enable Copilot in Fabric Tenant settings',
                                'C. Add mcp.json to the workspace',
                                'D. Install GitHub Copilot extension'
                            ],
                            'correct': 'B',
                            'explain': 'Both F64+ capacity AND the Tenant settings toggle must be enabled. If capacity is confirmed, check the Tenant settings.'
                        },
                        {
                            'q': "A developer's AI tool generates: SET @SQL = 'SELECT * FROM ' + @TableName; EXEC (@SQL). What is the risk?",
                            'opts': ['A. Performance issue', 'B. SQL injection - @TableName could contain malicious SQL', 'C. Syntax error', 'D. No risk'],
                            'correct': 'B',
                            'explain': 'Concatenating table names into dynamic SQL allows injection attacks. Use a whitelist of valid table names or schema validation instead.'
                        },
                        {
                            'q': 'Best practice for naming the MCP connection account for a reporting tool?',
                            'opts': [
                                'A. Use sa account for simplicity',
                                'B. Use db_owner role',
                                'C. Dedicated read-only login with SELECT on reporting schemas only',
                                'D. Windows admin account'
                            ],
                            'correct': 'C',
                            'explain': 'Least privilege: create a dedicated login with only SELECT on the schemas the reporting AI needs. No sysadmin, no write permissions.'
                        },
                        {
                            'q': "What does applyTo: '**/*.sql' in VS Code settings control?",
                            'opts': [
                                'A. Runs all .sql files automatically',
                                'B. Copilot instruction file applies only when editing .sql files',
                                'C. Uploads .sql to GitHub',
                                'D. Excludes .sql from Copilot'
                            ],
                            'correct': 'B',
                            'explain': 'applyTo glob pattern limits when the instruction set is active - **/*.sql means only when the active file is a .sql file.'
                        },
                        {
                            'q': 'In mcp.json, which transport connects to a remote REST API endpoint?',
                            'opts': ['A. stdio', 'B. named-pipe', 'C. local', 'D. http (or SSE)'],
                            'correct': 'D',
                            'explain': 'http (or Server-Sent Events/SSE) transport connects to a remote HTTP endpoint, appropriate for cloud REST APIs.'
                        }
                    ]
                },
                {
                    'id': 'lp1-m4-u10',
                    'title': 'Summary',
                    'type': 'summary',
                    'estimated_time': 5,
                    'objectives': ['Review AI-assisted SQL development concepts'],
                    'content': [
                        {
                            'type': 'theory',
                            'title': 'Module 4 Summary',
                            'body': 'Key concepts from Module 4 on AI-assisted SQL tools:<ul><li><strong>GitHub Copilot</strong> - VS Code extension; comment-to-code; Tab to accept; Ctrl+Shift+I for Chat; requires GitHub Copilot subscription</li><li><strong>Fabric Copilot</strong> - requires F64+ capacity AND Tenant settings toggle; available in notebooks, SQL analytics endpoint, Dataflow Gen2</li><li><strong>Security</strong> - review AI code for SQL injection; use parameterized queries; least privilege for AI accounts; prompt injection risk from data</li><li><strong>MCP</strong> - Model Context Protocol; mcp.json config; stdio for local processes; http/SSE for remote; ${env:VAR} for credentials; @servername in Copilot Chat</li><li><strong>Instruction files</strong> - .github/copilot-instructions.md; Markdown format; applyTo glob patterns; naming conventions, error handling, security rules</li></ul>'
                        },
                        {
                            'type': 'tip',
                            'body': 'Exam reminders: Fabric Copilot = F64 capacity + Tenant settings; mcp.json transport options = stdio (local) vs http/SSE (remote); instruction file = .github/copilot-instructions.md; always parameterize AI-generated SQL.'
                        }
                    ],
                    'quiz': [
                        {
                            'q': 'Minimum Fabric capacity for Copilot?',
                            'opts': ['A. F4', 'B. F16', 'C. F32', 'D. F64'],
                            'correct': 'D',
                            'explain': 'Fabric Copilot requires F64 or higher capacity.'
                        },
                        {
                            'q': "How do you customize Copilot's behavior for your SQL project?",
                            'opts': [
                                'A. Edit VS Code keybindings.json',
                                'B. Create .github/copilot-instructions.md',
                                'C. Add comments to every .sql file',
                                'D. Configure SQL Server Agent'
                            ],
                            'correct': 'B',
                            'explain': '.github/copilot-instructions.md is automatically read by Copilot and applies conventions to all code generation in that repo.'
                        },
                        {
                            'q': 'What MCP config key references an environment variable?',
                            'opts': ['A. $VAR', 'B. %VAR%', 'C. ${env:VAR}', 'D. @{VAR}'],
                            'correct': 'C',
                            'explain': '${env:VARIABLE_NAME} in mcp.json reads the value from the system environment variable.'
                        },
                        {
                            'q': 'What is prompt injection in the context of AI SQL tools?',
                            'opts': [
                                'A. SQL injection via AI-generated code',
                                'B. Malicious data content that hijacks AI assistant behavior',
                                'C. Inserting prompts into SQL comments',
                                'D. A type of database attack'
                            ],
                            'correct': 'B',
                            'explain': 'Prompt injection is when data in a database or document contains instructions that cause the AI to deviate from its intended behavior.'
                        },
                        {
                            'q': 'Which Copilot Chat syntax routes a question to a specific MCP server?',
                            'opts': ['A. /servername', 'B. @servername', 'C. #servername', 'D. !servername'],
                            'correct': 'B',
                            'explain': 'In Copilot Chat, @servername (matching the key in mcp.json) routes the message to that MCP server.'
                        }
                    ]
                }
            ]
        }

    ]  # end modules list for LP1

}  # end LP1_DATA
