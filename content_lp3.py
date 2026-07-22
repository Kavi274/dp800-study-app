# DP-800 Learning Path 3 Content
# LP3: Implement AI capabilities in database solutions

LP3_DATA = {
    "id": "lp3",
    "title": "Implement AI capabilities in database solutions",
    "description": "Learn to integrate AI models and embeddings into SQL databases, implement intelligent search with full-text and vector search, and build RAG (Retrieval-Augmented Generation) solutions.",
    "color": "#8764b8",
    "icon": "fas fa-brain",
    "modules": [

        # ══════════════════════════════════════════════════════
        # MODULE 9 — Design and implement models and embeddings
        # ══════════════════════════════════════════════════════
        {
            "id": "lp3-m9",
            "title": "Design and implement models and embeddings with SQL",
            "description": "Learn how to connect SQL databases to external AI models, understand vector embeddings, and store and maintain embeddings inside SQL Server or Azure SQL.",
            "units": [

                # ── Unit 1: Introduction ─────────────────────────────────
                {
                    "id": "lp3-m9-u1",
                    "title": "Introduction",
                    "description": "Overview of AI models and embeddings in the context of SQL databases.",
                    "estimated_time": 5,
                    "objectives": [
                        "Understand why AI capabilities are being added to SQL databases",
                        "Preview what models and embeddings are",
                        "Know what this module covers"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Why AI + SQL?",
                            "body": "Traditionally, SQL databases have stored structured data — rows of numbers, dates, and short text. AI changes this by adding two superpowers:\n\n<strong>1. Calling AI models from SQL</strong> — You can call Azure OpenAI or other AI services directly inside T-SQL code using a stored procedure called <code>sp_invoke_external_rest_endpoint</code>. This means your database can ask an AI to summarize a document, classify text, or translate a sentence — without leaving SQL Server.\n\n<strong>2. Storing embeddings</strong> — An embedding is a list of numbers that represents the <em>meaning</em> of a piece of text. By storing embeddings alongside your data, you can do <strong>semantic search</strong>: find rows that are <em>conceptually similar</em> to a question, even if they share no keywords.\n\nThis module teaches you both skills — connecting to AI models and working with embeddings in SQL."
                        },
                        {
                            "type": "theory",
                            "title": "What You Will Learn in This Module",
                            "body": "<ul><li>How to evaluate which AI model fits your use case</li><li>How to create an external model connection in SQL using <code>CREATE EXTERNAL DATA SOURCE</code></li><li>What embeddings are and why they matter</li><li>How to generate embeddings by calling Azure OpenAI from T-SQL</li><li>How to store embeddings using the <code>VECTOR</code> data type</li><li>How to keep embeddings up to date when your source data changes</li></ul>\n\nThese skills are tested in the DP-800 exam and are foundational for implementing intelligent search and RAG (Retrieval-Augmented Generation) — covered in the next two modules."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What is the primary reason for adding AI capabilities to a SQL database?",
                            "opts": ["A. To replace relational tables with JSON files", "B. To enable semantic search and AI-powered operations directly from T-SQL", "C. To remove the need for indexes", "D. To migrate data to the cloud automatically"],
                            "correct": "B",
                            "explain": "Adding AI capabilities to SQL allows you to call AI models from T-SQL and store embeddings for semantic search — making your database 'intelligent' without changing its relational foundation."
                        },
                        {
                            "q": "What is an embedding in the context of AI and SQL?",
                            "opts": ["A. A foreign key constraint", "B. A compressed backup format", "C. A list of numbers that represents the semantic meaning of text", "D. A type of SQL index"],
                            "correct": "C",
                            "explain": "An embedding is a numerical vector (list of numbers) that captures the meaning of a piece of text. Similar texts produce similar embeddings, enabling semantic similarity comparisons."
                        },
                        {
                            "q": "Which stored procedure lets you call an external REST API (like Azure OpenAI) from inside T-SQL?",
                            "opts": ["A. sp_execute_external_script", "B. sp_invoke_external_rest_endpoint", "C. sp_call_api", "D. xp_cmdshell"],
                            "correct": "B",
                            "explain": "sp_invoke_external_rest_endpoint is the built-in Azure SQL / SQL Server 2025 stored procedure that sends an HTTP request to a REST API endpoint and returns the JSON response."
                        },
                        {
                            "q": "What type of search is enabled by storing embeddings in a SQL database?",
                            "opts": ["A. Keyword search using LIKE", "B. Full-text search using CONTAINS", "C. Semantic search based on meaning", "D. Range search using BETWEEN"],
                            "correct": "C",
                            "explain": "Embeddings enable semantic search — finding data that is conceptually similar to a query even if there are no matching keywords. This is more powerful than LIKE or CONTAINS."
                        },
                        {
                            "q": "Which Azure service provides the AI embedding and chat models most commonly used with Azure SQL?",
                            "opts": ["A. Azure Blob Storage", "B. Azure OpenAI Service", "C. Azure Active Directory", "D. Azure DevOps"],
                            "correct": "B",
                            "explain": "Azure OpenAI Service provides embedding models (like text-embedding-ada-002) and chat models (like gpt-4) that can be called from SQL using sp_invoke_external_rest_endpoint."
                        }
                    ]
                },

                # ── Unit 2: Evaluate AI models for SQL solutions ─────────
                {
                    "id": "lp3-m9-u2",
                    "title": "Evaluate AI models for SQL solutions",
                    "description": "Learn how to choose the right AI model for embedding or chat tasks, and understand the tradeoffs of accuracy, cost, and latency.",
                    "estimated_time": 20,
                    "objectives": [
                        "Distinguish between embedding models and chat/completion models",
                        "Understand key evaluation criteria: accuracy, latency, cost, token limits",
                        "Use Azure AI Foundry to browse the model catalog",
                        "Match model capabilities to specific SQL use cases"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Two Types of AI Models Used with SQL",
                            "body": "When integrating AI with SQL, you will primarily work with two categories of model:\n\n<strong>1. Embedding Models</strong><br>These convert text into a vector of numbers. They do NOT generate text — they only produce a numerical representation.\n<ul><li><strong>text-embedding-ada-002</strong> — The most common Azure OpenAI embedding model. Produces a 1536-dimensional vector. Fast, cheap, and works well for most scenarios.</li><li><strong>text-embedding-3-small</strong> — A newer, improved model. Also 1536 dimensions by default (configurable). Better quality than ada-002 at similar cost.</li><li><strong>text-embedding-3-large</strong> — Produces up to 3072 dimensions. Higher quality but costs more and uses more storage.</li></ul>\n\n<strong>2. Chat / Completion Models</strong><br>These generate text responses to a prompt. Used for summarization, Q&amp;A, and RAG.\n<ul><li><strong>gpt-4o</strong> — Fast, multimodal (text + images), cost-effective GPT-4 class model</li><li><strong>gpt-4</strong> — High quality reasoning, higher cost</li><li><strong>gpt-35-turbo</strong> — Faster and cheaper, lower quality than GPT-4</li></ul>"
                        },
                        {
                            "type": "theory",
                            "title": "Model Evaluation Criteria",
                            "body": "When choosing a model, evaluate these four factors:\n\n<strong>1. Accuracy / Quality</strong><br>How well does the model understand meaning? For embeddings, better models produce vectors where similar documents cluster more tightly. For chat models, better models reason more accurately.\n\n<strong>2. Latency</strong><br>How long does an API call take? Embedding calls are typically 100-500ms. Chat completions can take 1-10 seconds. Latency matters if you need real-time responses.\n\n<strong>3. Cost</strong><br>Azure OpenAI charges per 1,000 tokens (roughly 750 words). Embedding models are much cheaper than chat models. <em>text-embedding-ada-002</em> costs ~$0.0001 per 1K tokens vs. ~$0.03 per 1K tokens for GPT-4.\n\n<strong>4. Token Limits</strong><br>Each model has a maximum input size. <em>text-embedding-ada-002</em> accepts up to 8,191 tokens per call (~6,000 words). If your text is longer, you must chunk it first."
                        },
                        {
                            "type": "important",
                            "title": "Embedding Dimensions Matter for Storage",
                            "body": "The number of dimensions in an embedding vector directly affects storage size. Each dimension is stored as a 4-byte float.\n<ul><li>1536 dimensions = 6,144 bytes per row (~6 KB)</li><li>3072 dimensions = 12,288 bytes per row (~12 KB)</li></ul>\nFor a table with 1 million rows and 1536-dimensional embeddings, that is ~6 GB just for the embedding column. Choose the smallest model that meets your accuracy requirements."
                        },
                        {
                            "type": "theory",
                            "title": "Azure AI Foundry Model Catalog",
                            "body": "Azure AI Foundry (formerly Azure AI Studio) hosts the <strong>Model Catalog</strong> — a searchable directory of AI models you can deploy.\n\n<strong>How to browse:</strong>\n<ol><li>Go to <code>ai.azure.com</code> and sign in</li><li>Click <strong>Model catalog</strong> in the left nav</li><li>Filter by task: <em>Text Embeddings</em> or <em>Chat completion</em></li><li>Click a model to see its benchmark scores, pricing, token limits, and deployment options</li></ol>\n\n<strong>Key fact:</strong> For use with Azure SQL via <code>sp_invoke_external_rest_endpoint</code>, you must deploy the model to an <strong>Azure OpenAI resource</strong> and get an endpoint URL and API key."
                        },
                        {
                            "type": "sql_block",
                            "title": "Testing a Model Choice with sp_invoke_external_rest_endpoint",
                            "scenario": "You want to verify that your chosen embedding model (text-embedding-ada-002) is reachable from SQL Server and understand the response structure before building a full solution.",
                            "code": """DECLARE @url NVARCHAR(4000) =
    'https://YOUR-RESOURCE.openai.azure.com/openai/deployments/text-embedding-ada-002/embeddings?api-version=2023-05-15';

DECLARE @payload NVARCHAR(MAX) = N'{
    "input": "This is a test sentence to check the embedding model."
}';

DECLARE @response NVARCHAR(MAX);
DECLARE @status INT;

EXEC sp_invoke_external_rest_endpoint
    @url        = @url,
    @method     = 'POST',
    @headers    = N'{"Content-Type": "application/json", "api-key": "YOUR-API-KEY"}',
    @payload    = @payload,
    @response   = @response OUTPUT,
    @statuscode = @status OUTPUT;

SELECT
    @status              AS http_status_code,
    @response            AS raw_response,
    JSON_VALUE(@response, '$.result.data[0].embedding[0]')  AS first_dimension,
    JSON_VALUE(@response, '$.result.model')                  AS model_used,
    JSON_VALUE(@response, '$.result.usage.total_tokens')     AS tokens_used;""",
                            "explanation": "This code sends a test sentence to Azure OpenAI's embedding API and prints the HTTP status code, raw JSON response, and some parsed values. It helps you verify connectivity and understand the response format before building production code.",
                            "purpose": "Verify model connectivity and inspect the response structure from Azure OpenAI embeddings API.",
                            "breakdown": [
                                {"line": "DECLARE @url NVARCHAR(4000) = ...", "meaning": "The full URL of your Azure OpenAI deployment. Replace YOUR-RESOURCE with your actual resource name and text-embedding-ada-002 with your deployment name."},
                                {"line": "DECLARE @payload NVARCHAR(MAX) = N'{\"input\": ...}'", "meaning": "The JSON body sent to the API. The 'input' field is the text you want to embed. N prefix makes it Unicode (required for JSON in T-SQL)."},
                                {"line": "EXEC sp_invoke_external_rest_endpoint", "meaning": "Calls the built-in stored procedure that makes HTTP requests from inside SQL Server. Only available in Azure SQL Database and SQL Server 2025."},
                                {"line": "@url = @url, @method = 'POST'", "meaning": "Specifies the endpoint URL and HTTP method. Embedding APIs always use POST."},
                                {"line": "@headers = N'{\"Content-Type\": ...}'", "meaning": "HTTP headers including the API key for authentication. The api-key header is how Azure OpenAI authenticates requests."},
                                {"line": "@response = @response OUTPUT", "meaning": "The OUTPUT keyword means the stored procedure writes the API's JSON response into this variable."},
                                {"line": "@statuscode = @status OUTPUT", "meaning": "Captures the HTTP status code. 200 means success. 401 means wrong API key. 404 means wrong URL."},
                                {"line": "JSON_VALUE(@response, '$.result.data[0].embedding[0]')", "meaning": "Parses the first number from the embedding array in the JSON response. The full embedding has 1536 numbers."},
                                {"line": "JSON_VALUE(@response, '$.result.usage.total_tokens')", "meaning": "Shows how many tokens the input used. Useful for estimating costs before bulk operations."}
                            ],
                            "ssms_steps": [
                                "Open SQL Server Management Studio (SSMS)",
                                "In Object Explorer, connect to your Azure SQL Database server",
                                "Click New Query in the toolbar",
                                "Paste the code above into the query window",
                                "Replace YOUR-RESOURCE with your Azure OpenAI resource name",
                                "Replace YOUR-API-KEY with your actual API key (found in Azure Portal > Azure OpenAI > Keys and Endpoint)",
                                "Replace text-embedding-ada-002 in the URL with your deployment name if different",
                                "Press F5 or click Execute",
                                "In the Results pane, check that http_status_code = 200",
                                "The first_dimension column should show a small decimal number (e.g., 0.0234567)",
                                "tokens_used shows how many tokens your test sentence consumed"
                            ],
                            "exam_tip": "sp_invoke_external_rest_endpoint is only available in Azure SQL Database and SQL Server 2025 — not in older SQL Server versions. The response body is accessed via the @response OUTPUT parameter and then parsed with JSON_VALUE or OPENJSON."
                        },
                        {
                            "type": "tip",
                            "title": "Model Selection Rule of Thumb",
                            "body": "<strong>Start with text-embedding-ada-002 or text-embedding-3-small</strong> for most embedding use cases — they offer a good balance of quality, speed, and cost.\n\nOnly upgrade to text-embedding-3-large if you find that semantic search results are poor quality after testing.\n\nFor chat/RAG: use <strong>gpt-35-turbo</strong> for high-volume, cost-sensitive scenarios; use <strong>gpt-4o</strong> when accuracy and reasoning quality matter more."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What does text-embedding-ada-002 produce as output?",
                            "opts": ["A. A generated text summary of the input", "B. A 1536-dimensional vector of floating-point numbers", "C. A SQL table of keywords", "D. A compressed binary blob"],
                            "correct": "B",
                            "explain": "text-embedding-ada-002 produces a 1536-dimensional vector — a list of 1536 floating-point numbers that represent the semantic meaning of the input text. It does NOT generate text."
                        },
                        {
                            "q": "Which of the following is NOT a factor to consider when evaluating an AI model for SQL integration?",
                            "opts": ["A. Token limit per API call", "B. Cost per 1,000 tokens", "C. The number of SQL Server logins", "D. Model latency"],
                            "correct": "C",
                            "explain": "The number of SQL Server logins is unrelated to AI model evaluation. The key factors are accuracy/quality, latency, cost, and token limits."
                        },
                        {
                            "q": "A table has 2 million rows and you want to store 3072-dimensional embeddings. Approximately how much storage will the embedding column require?",
                            "opts": ["A. About 24 GB", "B. About 2 GB", "C. About 100 MB", "D. About 240 GB"],
                            "correct": "A",
                            "explain": "3072 dimensions × 4 bytes per float = 12,288 bytes per row. 12,288 × 2,000,000 rows = ~24.6 GB. Always factor embedding storage into your capacity planning."
                        },
                        {
                            "q": "What is the maximum token input limit for text-embedding-ada-002?",
                            "opts": ["A. 512 tokens", "B. 2,048 tokens", "C. 8,191 tokens", "D. 32,000 tokens"],
                            "correct": "C",
                            "explain": "text-embedding-ada-002 accepts up to 8,191 tokens per API call (roughly 6,000 words). Text longer than this must be split (chunked) before embedding."
                        },
                        {
                            "q": "Where can you browse and compare available AI models for Azure deployment, including benchmark scores and pricing?",
                            "opts": ["A. Azure Active Directory", "B. Azure AI Foundry Model Catalog at ai.azure.com", "C. SQL Server Configuration Manager", "D. Azure Cost Management"],
                            "correct": "B",
                            "explain": "Azure AI Foundry (ai.azure.com) hosts the Model Catalog where you can search, compare benchmark scores, view pricing, and deploy models including OpenAI embedding and chat models."
                        }
                    ]
                },

                # ── Unit 3: Create external models in SQL ─────────────────
                {
                    "id": "lp3-m9-u3",
                    "title": "Create external models in SQL",
                    "description": "Learn to configure the connection between SQL Server and Azure AI services using external data sources and credentials.",
                    "estimated_time": 25,
                    "objectives": [
                        "Create a DATABASE SCOPED CREDENTIAL to store an API key securely",
                        "Create an EXTERNAL DATA SOURCE pointing to Azure OpenAI",
                        "Understand how sp_invoke_external_rest_endpoint uses these objects",
                        "Call an AI model using T-SQL"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "How SQL Connects to External AI Services",
                            "body": "SQL Server does not store API keys in plain text in your query code. Instead, you set up a two-object pattern:\n\n<strong>Step 1: DATABASE SCOPED CREDENTIAL</strong><br>A secure object that stores your API key inside the database's encryption system. Only users with the right permissions can use it — no one can read the key back out.\n\n<strong>Step 2: EXTERNAL DATA SOURCE</strong><br>An object that records the URL of the external service (e.g., your Azure OpenAI endpoint) and links to the credential for authentication.\n\nThen, when you call <code>sp_invoke_external_rest_endpoint</code>, you can reference the external data source instead of hard-coding your URL and key every time.\n\n<strong>Why this pattern?</strong><br><ul><li>API keys are never visible in query text or logs</li><li>Changing an API key only requires updating one credential object</li><li>Access can be controlled with SQL permissions</li></ul>"
                        },
                        {
                            "type": "sql_block",
                            "title": "Step 1 — Create a Database Master Key",
                            "scenario": "Before you can create a credential, you must create a Database Master Key (DMK). This is the encryption root that protects all credentials in the database.",
                            "code": """-- Run this once per database
-- The password is used to protect the key backup —
-- choose something strong and store it safely
CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'MyStr0ng!MasterKeyPass';""",
                            "explanation": "The Database Master Key (DMK) is required before you can create any DATABASE SCOPED CREDENTIAL. It encrypts all secrets in the database. You only need to run this once per database.",
                            "purpose": "Create the encryption foundation that protects API keys and credentials stored in the database.",
                            "breakdown": [
                                {"line": "CREATE MASTER KEY ENCRYPTION BY PASSWORD = '...'", "meaning": "Creates the Database Master Key, encrypted with the provided password. Store this password safely — you need it to restore backups that contain credentials. This is a one-time setup per database."}
                            ],
                            "ssms_steps": [
                                "Open SSMS and connect to your Azure SQL Database",
                                "Click New Query",
                                "First check if a master key already exists: SELECT * FROM sys.symmetric_keys WHERE name = '##MS_DatabaseMasterKey##'",
                                "If no rows returned, paste the CREATE MASTER KEY statement",
                                "Replace the password with a strong password of your choice",
                                "Press F5 to execute",
                                "You should see 'Commands completed successfully'"
                            ],
                            "exam_tip": "The Database Master Key must exist before creating any DATABASE SCOPED CREDENTIAL. If you skip this step, the CREATE CREDENTIAL statement will fail with an error."
                        },
                        {
                            "type": "sql_block",
                            "title": "Step 2 — Create a Database Scoped Credential",
                            "scenario": "Store your Azure OpenAI API key securely in the database so it never appears in plain text in your queries.",
                            "code": """-- Store the Azure OpenAI API key as a secret
CREATE DATABASE SCOPED CREDENTIAL [AzureOpenAI_Credential]
WITH
    IDENTITY = 'HTTPEndpointHeaders',
    SECRET = '{"api-key": "YOUR-AZURE-OPENAI-API-KEY-HERE"}';""",
                            "explanation": "This creates a named credential that securely stores your Azure OpenAI API key. The IDENTITY value 'HTTPEndpointHeaders' tells SQL Server that the SECRET is a JSON object of HTTP headers to include in API calls.",
                            "purpose": "Securely store the Azure OpenAI API key so it can be referenced by name without exposing the key value in code.",
                            "breakdown": [
                                {"line": "CREATE DATABASE SCOPED CREDENTIAL [AzureOpenAI_Credential]", "meaning": "Creates a new credential object named AzureOpenAI_Credential. The square brackets allow spaces or special characters in the name."},
                                {"line": "IDENTITY = 'HTTPEndpointHeaders'", "meaning": "This specific value tells sp_invoke_external_rest_endpoint that the SECRET contains HTTP headers to send with requests. This is the required value for API key authentication."},
                                {"line": "SECRET = '{\"api-key\": \"YOUR-KEY\"}'", "meaning": "The JSON-formatted secret containing your API key. The api-key header is what Azure OpenAI uses for authentication. Replace YOUR-AZURE-OPENAI-API-KEY-HERE with your actual key from the Azure Portal."}
                            ],
                            "ssms_steps": [
                                "In SSMS, open a New Query window connected to your database",
                                "Go to Azure Portal > Your Azure OpenAI resource > Keys and Endpoint",
                                "Copy KEY 1 value",
                                "Paste the CREATE DATABASE SCOPED CREDENTIAL code above",
                                "Replace YOUR-AZURE-OPENAI-API-KEY-HERE with the key you copied",
                                "Press F5 to execute",
                                "Verify success: SELECT name FROM sys.database_scoped_credentials"
                            ],
                            "exam_tip": "IDENTITY = 'HTTPEndpointHeaders' is the magic value that makes sp_invoke_external_rest_endpoint treat the SECRET as HTTP headers. Using any other IDENTITY value will break the authentication."
                        },
                        {
                            "type": "sql_block",
                            "title": "Step 3 — Create an External Data Source",
                            "scenario": "Create a named external data source that points to your Azure OpenAI endpoint, linking it to the credential you just created.",
                            "code": """-- Create external data source pointing to Azure OpenAI
CREATE EXTERNAL DATA SOURCE [AzureOpenAI]
WITH (
    LOCATION = 'https://YOUR-RESOURCE-NAME.openai.azure.com',
    CREDENTIAL = [AzureOpenAI_Credential]
);""",
                            "explanation": "An EXTERNAL DATA SOURCE registers the URL of the external AI service and links it to a credential. You reference this object by name when calling sp_invoke_external_rest_endpoint instead of repeating the URL and key every time.",
                            "purpose": "Create a reusable, named connection to Azure OpenAI that can be used in all AI-related T-SQL calls.",
                            "breakdown": [
                                {"line": "CREATE EXTERNAL DATA SOURCE [AzureOpenAI]", "meaning": "Creates a named data source object called AzureOpenAI. You will reference this name in your T-SQL calls."},
                                {"line": "LOCATION = 'https://YOUR-RESOURCE-NAME.openai.azure.com'", "meaning": "The base URL of your Azure OpenAI resource. Find this in Azure Portal > Azure OpenAI > Keys and Endpoint. Replace YOUR-RESOURCE-NAME with your actual resource name."},
                                {"line": "CREDENTIAL = [AzureOpenAI_Credential]", "meaning": "Links this data source to the credential created in Step 2. When SQL Server calls this endpoint, it automatically includes the api-key header from the credential's SECRET."}
                            ],
                            "ssms_steps": [
                                "In SSMS, open a New Query window",
                                "Go to Azure Portal > Azure OpenAI resource > Keys and Endpoint",
                                "Copy the Endpoint URL (e.g., https://myresource.openai.azure.com)",
                                "Paste the CREATE EXTERNAL DATA SOURCE code above",
                                "Replace YOUR-RESOURCE-NAME.openai.azure.com with your actual endpoint",
                                "Press F5 to execute",
                                "Verify: SELECT name, location FROM sys.external_data_sources"
                            ],
                            "exam_tip": "The LOCATION in EXTERNAL DATA SOURCE is the base URL only (no path). The specific deployment path (e.g., /openai/deployments/...) is appended in the @url parameter when calling sp_invoke_external_rest_endpoint."
                        },
                        {
                            "type": "tip",
                            "title": "Verify Your External Model Connection",
                            "body": "After creating the credential and data source, test the connection with a simple embedding call:\n<code>EXEC sp_invoke_external_rest_endpoint @url = 'https://YOUR-RESOURCE.openai.azure.com/openai/deployments/text-embedding-ada-002/embeddings?api-version=2023-05-15', @method = 'POST', @payload = N'{\"input\": \"test\"}';</code>\n\nIf you get HTTP 200, your setup is correct. HTTP 401 means wrong API key. HTTP 404 means wrong URL or deployment name."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What is the purpose of a DATABASE SCOPED CREDENTIAL in the context of Azure OpenAI integration?",
                            "opts": ["A. It stores the SQL Server login password", "B. It securely stores the Azure OpenAI API key for use in T-SQL calls", "C. It creates a new Azure subscription", "D. It configures the SQL Server firewall"],
                            "correct": "B",
                            "explain": "DATABASE SCOPED CREDENTIAL securely stores the Azure OpenAI API key inside the database's encryption system. It is then referenced by an EXTERNAL DATA SOURCE, so the key never appears in plain text in queries."
                        },
                        {
                            "q": "What must be created BEFORE a DATABASE SCOPED CREDENTIAL?",
                            "opts": ["A. An EXTERNAL DATA SOURCE", "B. A database master key", "C. A stored procedure", "D. A new database user"],
                            "correct": "B",
                            "explain": "The Database Master Key (created with CREATE MASTER KEY) must exist before any DATABASE SCOPED CREDENTIAL can be created. The master key is the encryption foundation that protects all credentials."
                        },
                        {
                            "q": "What IDENTITY value must be used in a DATABASE SCOPED CREDENTIAL so that sp_invoke_external_rest_endpoint treats the SECRET as HTTP headers?",
                            "opts": ["A. 'APIKey'", "B. 'AzureOpenAI'", "C. 'HTTPEndpointHeaders'", "D. 'Bearer'"],
                            "correct": "C",
                            "explain": "IDENTITY = 'HTTPEndpointHeaders' is the specific value required to tell sp_invoke_external_rest_endpoint that the SECRET field contains a JSON object of HTTP headers (like the api-key header for Azure OpenAI)."
                        },
                        {
                            "q": "In an EXTERNAL DATA SOURCE for Azure OpenAI, what does the LOCATION field contain?",
                            "opts": ["A. The full API URL including the deployment name and API version", "B. The base URL of the Azure OpenAI resource (e.g., https://myresource.openai.azure.com)", "C. The name of the SQL database", "D. The Azure subscription ID"],
                            "correct": "B",
                            "explain": "LOCATION contains only the base URL of the Azure OpenAI resource. The specific deployment path (/openai/deployments/model-name/...) and API version are added in the @url parameter when calling sp_invoke_external_rest_endpoint."
                        },
                        {
                            "q": "Which system catalog view would you query to verify that an EXTERNAL DATA SOURCE was created successfully?",
                            "opts": ["A. sys.tables", "B. sys.credentials", "C. sys.external_data_sources", "D. sys.objects"],
                            "correct": "C",
                            "explain": "sys.external_data_sources is the catalog view that lists all external data sources in the current database. You can query SELECT name, location FROM sys.external_data_sources to verify your external data source exists."
                        }
                    ]
                },

                # ── Unit 4: Design embeddings for SQL data ────────────────
                {
                    "id": "lp3-m9-u4",
                    "title": "Design embeddings for SQL data",
                    "description": "Understand what embeddings are, how they capture meaning, and how to design your SQL schema to store them effectively.",
                    "estimated_time": 25,
                    "objectives": [
                        "Explain what an embedding vector is and how it represents meaning",
                        "Understand cosine similarity and why it is used",
                        "Design a SQL table with a VECTOR column for embeddings",
                        "Choose which text fields to embed and what to embed together"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "What Is an Embedding? A Beginner Explanation",
                            "body": "Imagine you could describe every word or sentence as a point in space — but instead of 3 dimensions (x, y, z), you use 1,536 dimensions. Two sentences that mean similar things end up as points that are <em>close together</em> in that space, even if they use completely different words.\n\n<strong>Example:</strong>\n<ul><li>\"The dog chased the ball\" → some point in 1536D space</li><li>\"A puppy ran after a toy\" → a point very close to the first one (similar meaning)</li><li>\"The quarterly revenue exceeded projections\" → a point very far away (different topic)</li></ul>\n\nAn embedding is simply those 1,536 numbers (called <strong>dimensions</strong>) that describe where a piece of text sits in this meaning-space. The model that generates these numbers (like text-embedding-ada-002) has been trained on billions of texts, so it understands language deeply.\n\n<strong>Why store embeddings in SQL?</strong><br>Once you have embeddings stored as a column, you can find the rows most similar to any query — just by comparing the query's embedding to all stored embeddings. This is semantic search."
                        },
                        {
                            "type": "theory",
                            "title": "Cosine Similarity — How We Measure 'Closeness'",
                            "body": "The standard way to measure similarity between two embeddings is <strong>cosine similarity</strong>.\n\nThink of each embedding as an arrow pointing from the origin (0,0,...,0) in 1536-dimensional space. Cosine similarity measures the angle between two arrows:\n<ul><li>Angle = 0° (arrows point the same direction) → cosine similarity = 1.0 → <strong>identical meaning</strong></li><li>Angle = 90° (arrows are perpendicular) → cosine similarity = 0.0 → <strong>unrelated</strong></li><li>Angle = 180° (arrows point opposite directions) → cosine similarity = -1.0 → <strong>opposite meaning</strong></li></ul>\n\nIn practice, you will see values between 0.7 and 1.0 for semantically similar texts.\n\nSQL Server 2025 and Azure SQL provide the <code>VECTOR_DISTANCE</code> function which can compute cosine distance (1 - cosine similarity) natively. A smaller distance = more similar."
                        },
                        {
                            "type": "important",
                            "title": "The VECTOR Data Type",
                            "body": "Azure SQL Database and SQL Server 2025 introduced the native <strong>VECTOR</strong> data type for storing embedding vectors.\n\n<code>column_name VECTOR(1536)</code>\n\nThe number in parentheses is the number of dimensions. Key facts:\n<ul><li>Stored efficiently as binary, not as a string</li><li>Works with <code>VECTOR_DISTANCE()</code> for similarity calculations</li><li>Cannot be used with standard comparison operators (=, &lt;, &gt;)</li><li>Must match the dimension count of your embedding model</li></ul>\n\nFor older SQL Server versions (pre-2025), you can store embeddings as <code>NVARCHAR(MAX)</code> (JSON string) or <code>VARBINARY(MAX)</code> and write your own cosine similarity function."
                        },
                        {
                            "type": "sql_block",
                            "title": "Design a Table with a VECTOR Column",
                            "scenario": "You have a product catalog table and want to add semantic search. Design a table that stores product descriptions along with their 1536-dimensional embedding vectors.",
                            "code": """-- Create a product catalog table with embedding support
-- Requires Azure SQL Database or SQL Server 2025
CREATE TABLE ProductCatalog (
    ProductID        INT           PRIMARY KEY IDENTITY(1,1),
    ProductName      NVARCHAR(200) NOT NULL,
    Description      NVARCHAR(MAX) NOT NULL,        -- Text we will embed
    Category         NVARCHAR(100),
    Price            DECIMAL(10,2),
    DescriptionEmbedding  VECTOR(1536),             -- Stores the embedding
    EmbeddingModel   NVARCHAR(100)                  -- Track which model was used
        DEFAULT 'text-embedding-ada-002',
    EmbeddingUpdated DATETIME2                      -- Track when embedding was last generated
        DEFAULT GETUTCDATE()
);

-- Index for fast lookup by ProductID (already covered by PK)
-- Note: Vector indexes (ANN) are in preview — check current Azure SQL docs
CREATE INDEX IX_ProductCatalog_Category
    ON ProductCatalog(Category);

-- Verify the table structure
SELECT
    COLUMN_NAME,
    DATA_TYPE,
    CHARACTER_MAXIMUM_LENGTH
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'ProductCatalog'
ORDER BY ORDINAL_POSITION;""",
                            "explanation": "This creates a product table that combines regular relational columns (ProductName, Category, Price) with an embedding column (DescriptionEmbedding). The audit columns (EmbeddingModel, EmbeddingUpdated) help you track embedding quality and freshness.",
                            "purpose": "Define a production-ready schema that supports both traditional SQL queries and AI-powered semantic search.",
                            "breakdown": [
                                {"line": "ProductID INT PRIMARY KEY IDENTITY(1,1)", "meaning": "Standard auto-incrementing primary key. Nothing AI-specific here — every table needs a PK."},
                                {"line": "Description NVARCHAR(MAX) NOT NULL", "meaning": "The source text that will be embedded. We store the original text AND the embedding — we need the text for display, and the embedding for search."},
                                {"line": "DescriptionEmbedding VECTOR(1536)", "meaning": "The key new column. VECTOR(1536) stores a 1536-dimensional float vector — the embedding of the Description text. 1536 matches text-embedding-ada-002's output dimensions."},
                                {"line": "EmbeddingModel NVARCHAR(100) DEFAULT 'text-embedding-ada-002'", "meaning": "Tracks which model generated the embedding. If you change models, you need to regenerate all embeddings — this column helps you identify which rows need updates."},
                                {"line": "EmbeddingUpdated DATETIME2 DEFAULT GETUTCDATE()", "meaning": "Records when the embedding was last generated. Useful for detecting stale embeddings when the Description text has been updated more recently."}
                            ],
                            "ssms_steps": [
                                "Open SSMS and connect to your Azure SQL Database",
                                "In Object Explorer, expand your database",
                                "Click New Query",
                                "Paste the CREATE TABLE statement above",
                                "Press F5 to execute",
                                "In Object Explorer, right-click Tables and click Refresh",
                                "Expand the new ProductCatalog table and click Columns to verify the VECTOR column appears",
                                "Run the SELECT from INFORMATION_SCHEMA.COLUMNS to see the column definitions"
                            ],
                            "exam_tip": "VECTOR(1536) is only available in Azure SQL Database and SQL Server 2025. The number must exactly match the dimensions your embedding model produces — 1536 for text-embedding-ada-002, up to 3072 for text-embedding-3-large."
                        },
                        {
                            "type": "tip",
                            "title": "What Text Should You Embed?",
                            "body": "Design your embeddings to match what users will search for:\n<ul><li><strong>Concatenate related fields</strong>: If users search for products, embed ProductName + ' ' + Description + ' ' + Category together — not just Description alone. This gives the embedding more context.</li><li><strong>Normalize text</strong>: Remove excessive whitespace, HTML tags, and special characters before embedding. Clean input = better embeddings.</li><li><strong>Chunk long text</strong>: If Description is very long (>6000 words), split it into smaller chunks and store one embedding per chunk. This gives more precise search results.</li><li><strong>Don't embed IDs or codes</strong>: Numbers like '12345' or codes like 'SKU-AB-C' carry no semantic meaning — don't include them in the text you embed.</li></ul>"
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What does a 1536-dimensional embedding vector represent?",
                            "opts": ["A. A 1536-row table of keywords", "B. The position of a piece of text in a 1536-dimensional meaning-space", "C. A 1536-character text string", "D. A 1536-byte binary file"],
                            "correct": "B",
                            "explain": "An embedding vector represents the semantic meaning of a piece of text as coordinates in high-dimensional space. 1536 dimensions means there are 1536 floating-point numbers that together describe where the text 'sits' in meaning-space."
                        },
                        {
                            "q": "What does a cosine similarity of 0.95 between two embeddings indicate?",
                            "opts": ["A. The texts are mostly unrelated", "B. The texts have very similar semantic meaning", "C. The texts are exact duplicates", "D. The texts are in different languages"],
                            "correct": "B",
                            "explain": "Cosine similarity ranges from -1 to 1. A value of 0.95 is very close to 1.0, meaning the two texts have very similar semantic meaning (the angle between their embedding vectors is very small)."
                        },
                        {
                            "q": "Which SQL Server data type is used to store embedding vectors natively?",
                            "opts": ["A. VARBINARY(MAX)", "B. NVARCHAR(MAX)", "C. VECTOR(1536)", "D. FLOAT ARRAY"],
                            "correct": "C",
                            "explain": "VECTOR(n) is the native data type for embedding vectors in Azure SQL Database and SQL Server 2025. The number in parentheses specifies the dimension count and must match the embedding model's output dimensions."
                        },
                        {
                            "q": "Why is it good practice to store both the original text AND the embedding vector in the same table?",
                            "opts": ["A. Because SQL Server requires it for VECTOR columns", "B. Because you need the original text for display, while the embedding is used only for similarity search", "C. Because the embedding can be converted back to text if the original is lost", "D. Because it reduces storage requirements"],
                            "correct": "B",
                            "explain": "The original text is needed for display and reading. The embedding is used for semantic similarity computation. Embeddings cannot be converted back to text — they are one-way transformations. Storing both gives you both capabilities."
                        },
                        {
                            "q": "What is the best practice when embedding a product table where users search by product name, description, and category?",
                            "opts": ["A. Embed only the product name", "B. Create separate embeddings for each column", "C. Concatenate the product name, description, and category into one string and embed that", "D. Embed the product ID"],
                            "correct": "C",
                            "explain": "Concatenating related fields before embedding creates a richer, more contextual vector that captures the full product context. Separate embeddings per column would require combining scores later, which is more complex. Product IDs carry no semantic meaning."
                        }
                    ]
                },

                # ── Unit 5: Generate and maintain embeddings ──────────────
                {
                    "id": "lp3-m9-u5",
                    "title": "Generate and maintain embeddings",
                    "description": "Learn to generate embeddings by calling Azure OpenAI from T-SQL and keep them current as your data changes.",
                    "estimated_time": 30,
                    "objectives": [
                        "Write T-SQL to call the Azure OpenAI embedding API and parse the response",
                        "Insert the generated embedding into a VECTOR column",
                        "Create a trigger to auto-regenerate embeddings when source text changes",
                        "Design a batch refresh job for bulk embedding updates"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "The Embedding Generation Workflow",
                            "body": "Generating and storing an embedding involves three steps:\n\n<strong>Step 1: Build the input text</strong><br>Concatenate the fields you want to embed into a single string. Clean the text (trim whitespace, remove HTML if needed).\n\n<strong>Step 2: Call Azure OpenAI embedding API</strong><br>Use <code>sp_invoke_external_rest_endpoint</code> to POST the text to Azure OpenAI. The API returns a JSON object containing the embedding array.\n\n<strong>Step 3: Parse and store the result</strong><br>Use <code>JSON_QUERY</code> to extract the embedding array from the JSON response, then INSERT or UPDATE the row's VECTOR column.\n\nThe tricky part is the JSON parsing — Azure OpenAI returns the embedding as a JSON array like <code>[0.0023, -0.0134, ...]</code> inside a nested JSON structure. You need to extract exactly that array and convert it to the VECTOR type."
                        },
                        {
                            "type": "sql_block",
                            "title": "Generate an Embedding for a Single Row",
                            "scenario": "You just inserted a new product into ProductCatalog and need to generate its embedding by calling Azure OpenAI from T-SQL.",
                            "code": """-- Generate embedding for a single product
-- Step 1: Declare variables
DECLARE @ProductID      INT = 42;
DECLARE @TextToEmbed    NVARCHAR(MAX);
DECLARE @Payload        NVARCHAR(MAX);
DECLARE @Response       NVARCHAR(MAX);
DECLARE @StatusCode     INT;
DECLARE @EmbeddingJSON  NVARCHAR(MAX);

-- Step 2: Build the text to embed (concatenate relevant fields)
SELECT @TextToEmbed = ProductName + ' ' + Description + ' ' + ISNULL(Category, '')
FROM ProductCatalog
WHERE ProductID = @ProductID;

-- Step 3: Build the JSON payload for the API
SET @Payload = N'{"input": ' + (SELECT @TextToEmbed FOR JSON PATH, WITHOUT_ARRAY_WRAPPER) + '}';

-- Step 4: Call Azure OpenAI embedding API
EXEC sp_invoke_external_rest_endpoint
    @url        = 'https://YOUR-RESOURCE.openai.azure.com/openai/deployments/text-embedding-ada-002/embeddings?api-version=2023-05-15',
    @method     = 'POST',
    @headers    = N'{"Content-Type": "application/json", "api-key": "YOUR-API-KEY"}',
    @payload    = @Payload,
    @response   = @Response OUTPUT,
    @statuscode = @StatusCode OUTPUT;

-- Step 5: Check the API call succeeded
IF @StatusCode <> 200
BEGIN
    RAISERROR('Azure OpenAI API call failed. HTTP status: %d. Response: %s', 16, 1, @StatusCode, @Response);
    RETURN;
END

-- Step 6: Extract the embedding array from the JSON response
SET @EmbeddingJSON = JSON_QUERY(@Response, '$.result.data[0].embedding');

-- Step 7: Update the table with the new embedding
UPDATE ProductCatalog
SET
    DescriptionEmbedding = CAST(@EmbeddingJSON AS VECTOR(1536)),
    EmbeddingUpdated     = GETUTCDATE()
WHERE ProductID = @ProductID;

PRINT 'Embedding generated and stored for ProductID: ' + CAST(@ProductID AS VARCHAR);""",
                            "explanation": "This script takes a single product, builds the text to embed, calls Azure OpenAI, checks for errors, extracts the embedding from the JSON response, and stores it in the VECTOR column.",
                            "purpose": "Generate and store a vector embedding for a specific product row by calling the Azure OpenAI API from T-SQL.",
                            "breakdown": [
                                {"line": "DECLARE @TextToEmbed NVARCHAR(MAX)", "meaning": "Variable to hold the concatenated text we will send to Azure OpenAI for embedding."},
                                {"line": "SELECT @TextToEmbed = ProductName + ' ' + Description + ...", "meaning": "Concatenates the product name, description, and category into one string. ISNULL(Category, '') handles NULL category values — sending NULL to an API would cause errors."},
                                {"line": "SET @Payload = N'{\"input\": ' + (SELECT @TextToEmbed FOR JSON PATH, WITHOUT_ARRAY_WRAPPER) + '}'", "meaning": "Builds the JSON payload. FOR JSON PATH, WITHOUT_ARRAY_WRAPPER converts the text to a properly escaped JSON string value, handling special characters like quotes and backslashes automatically."},
                                {"line": "EXEC sp_invoke_external_rest_endpoint ... @response = @Response OUTPUT", "meaning": "Makes the HTTP POST request to Azure OpenAI. The entire JSON response from the API is stored in @Response."},
                                {"line": "IF @StatusCode <> 200 ... RAISERROR(...)", "meaning": "Always check the HTTP status code. 200 = success. Any other code means something went wrong. RAISERROR stops execution and reports the error."},
                                {"line": "SET @EmbeddingJSON = JSON_QUERY(@Response, '$.result.data[0].embedding')", "meaning": "Extracts the embedding array from the nested JSON. The path $.result.data[0].embedding navigates: result object > data array > first element > embedding array. JSON_QUERY returns a JSON fragment (array), not a scalar value."},
                                {"line": "CAST(@EmbeddingJSON AS VECTOR(1536))", "meaning": "Converts the JSON array string into the native VECTOR(1536) data type. SQL Server parses the JSON array and creates the binary vector representation."}
                            ],
                            "ssms_steps": [
                                "Open SSMS and connect to your Azure SQL Database",
                                "Click New Query",
                                "Paste the code above",
                                "Set @ProductID to the ID of a row you want to embed",
                                "Replace YOUR-RESOURCE and YOUR-API-KEY with your actual values",
                                "Press F5 to execute",
                                "Check the Messages tab for 'Embedding generated and stored for ProductID: 42'",
                                "Verify: SELECT ProductID, EmbeddingUpdated FROM ProductCatalog WHERE ProductID = 42",
                                "The DescriptionEmbedding column should now be non-NULL"
                            ],
                            "exam_tip": "JSON_QUERY extracts a JSON fragment (object or array) while JSON_VALUE extracts a scalar value. Use JSON_QUERY to extract the embedding array because it is a JSON array — JSON_VALUE would fail because it only works with scalar values like strings and numbers."
                        },
                        {
                            "type": "sql_block",
                            "title": "Batch Embedding — Process All Rows Without Embeddings",
                            "scenario": "You have 10,000 products in the table with no embeddings yet. Write a loop that processes them in batches to avoid overwhelming the API or hitting timeout limits.",
                            "code": """-- Batch embedding generation with rate limiting
DECLARE @BatchSize  INT = 100;    -- Process 100 rows at a time
DECLARE @ProductID  INT;
DECLARE @TextToEmbed NVARCHAR(MAX);
DECLARE @Payload    NVARCHAR(MAX);
DECLARE @Response   NVARCHAR(MAX);
DECLARE @StatusCode INT;
DECLARE @Count      INT = 0;

-- Cursor over rows that have no embedding yet
DECLARE embedding_cursor CURSOR FOR
    SELECT ProductID, ProductName + ' ' + Description + ' ' + ISNULL(Category, '')
    FROM ProductCatalog
    WHERE DescriptionEmbedding IS NULL   -- Only rows needing embeddings
    ORDER BY ProductID;

OPEN embedding_cursor;
FETCH NEXT FROM embedding_cursor INTO @ProductID, @TextToEmbed;

WHILE @@FETCH_STATUS = 0
BEGIN
    -- Build and send the API request
    SET @Payload = N'{"input": ' + (SELECT @TextToEmbed FOR JSON PATH, WITHOUT_ARRAY_WRAPPER) + '}';

    EXEC sp_invoke_external_rest_endpoint
        @url        = 'https://YOUR-RESOURCE.openai.azure.com/openai/deployments/text-embedding-ada-002/embeddings?api-version=2023-05-15',
        @method     = 'POST',
        @headers    = N'{"Content-Type": "application/json", "api-key": "YOUR-API-KEY"}',
        @payload    = @Payload,
        @response   = @Response OUTPUT,
        @statuscode = @StatusCode OUTPUT;

    -- Only update if API call succeeded
    IF @StatusCode = 200
    BEGIN
        UPDATE ProductCatalog
        SET
            DescriptionEmbedding = CAST(JSON_QUERY(@Response, '$.result.data[0].embedding') AS VECTOR(1536)),
            EmbeddingUpdated     = GETUTCDATE()
        WHERE ProductID = @ProductID;

        SET @Count = @Count + 1;
    END

    FETCH NEXT FROM embedding_cursor INTO @ProductID, @TextToEmbed;
END

CLOSE embedding_cursor;
DEALLOCATE embedding_cursor;

PRINT 'Embeddings generated for ' + CAST(@Count AS VARCHAR) + ' products.';""",
                            "explanation": "This uses a T-SQL cursor to iterate over all rows that are missing embeddings and generates them one by one, updating as it goes. It skips rows where the API call fails so one bad row does not stop the entire batch.",
                            "purpose": "Populate embeddings for all existing rows in bulk, processing only rows that need updates.",
                            "breakdown": [
                                {"line": "WHERE DescriptionEmbedding IS NULL", "meaning": "Filters to only rows without an embedding. This makes the batch job safe to re-run — it will skip rows that already have embeddings and only process new ones."},
                                {"line": "DECLARE embedding_cursor CURSOR FOR ...", "meaning": "A cursor lets you process rows one at a time in a loop. Normally avoid cursors in SQL (they are slow), but here each row requires a separate API call, so row-by-row processing is appropriate."},
                                {"line": "WHILE @@FETCH_STATUS = 0", "meaning": "Continues the loop as long as the cursor has more rows to read. @@FETCH_STATUS = 0 means the last FETCH succeeded."},
                                {"line": "IF @StatusCode = 200", "meaning": "Only update the database if the API call succeeded. This prevents storing NULL or garbage in the embedding column if the API is temporarily unavailable."},
                                {"line": "CLOSE embedding_cursor; DEALLOCATE embedding_cursor", "meaning": "Always close and deallocate cursors when done. Forgetting this leaks server resources."}
                            ],
                            "ssms_steps": [
                                "Open SSMS and connect to your Azure SQL Database",
                                "Click New Query",
                                "Paste the cursor code above",
                                "Replace YOUR-RESOURCE and YOUR-API-KEY with actual values",
                                "Press F5 to run — note this may take several minutes for large tables",
                                "Monitor progress in the Messages tab",
                                "When complete, verify: SELECT COUNT(*) AS WithEmbedding, COUNT(*) - SUM(CASE WHEN DescriptionEmbedding IS NULL THEN 0 ELSE 1 END) AS WithoutEmbedding FROM ProductCatalog"
                            ],
                            "exam_tip": "Cursors are generally slow in SQL, but for embedding generation (where each row needs a separate API call), they are appropriate. For very large tables, consider running this as an Azure SQL Agent job in small batches to avoid long transaction locks."
                        },
                        {
                            "type": "sql_block",
                            "title": "Auto-Maintain Embeddings with a Trigger",
                            "scenario": "A product's description is updated by the application. You want the embedding to automatically regenerate whenever the Description or ProductName changes.",
                            "code": """-- Trigger to regenerate embedding when source text changes
CREATE OR ALTER TRIGGER trg_ProductCatalog_UpdateEmbedding
ON ProductCatalog
AFTER UPDATE
AS
BEGIN
    SET NOCOUNT ON;

    -- Only fire if the Description or ProductName was actually changed
    IF NOT (UPDATE(Description) OR UPDATE(ProductName) OR UPDATE(Category))
        RETURN;

    -- Process each updated row (handles multi-row updates)
    DECLARE @ProductID      INT;
    DECLARE @TextToEmbed    NVARCHAR(MAX);
    DECLARE @Payload        NVARCHAR(MAX);
    DECLARE @Response       NVARCHAR(MAX);
    DECLARE @StatusCode     INT;

    DECLARE update_cursor CURSOR FOR
        SELECT
            i.ProductID,
            i.ProductName + ' ' + i.Description + ' ' + ISNULL(i.Category, '')
        FROM inserted i;   -- 'inserted' is the virtual table of new row values

    OPEN update_cursor;
    FETCH NEXT FROM update_cursor INTO @ProductID, @TextToEmbed;

    WHILE @@FETCH_STATUS = 0
    BEGIN
        SET @Payload = N'{"input": ' + (SELECT @TextToEmbed FOR JSON PATH, WITHOUT_ARRAY_WRAPPER) + '}';

        EXEC sp_invoke_external_rest_endpoint
            @url        = 'https://YOUR-RESOURCE.openai.azure.com/openai/deployments/text-embedding-ada-002/embeddings?api-version=2023-05-15',
            @method     = 'POST',
            @headers    = N'{"Content-Type": "application/json", "api-key": "YOUR-API-KEY"}',
            @payload    = @Payload,
            @response   = @Response OUTPUT,
            @statuscode = @StatusCode OUTPUT;

        IF @StatusCode = 200
            UPDATE ProductCatalog
            SET
                DescriptionEmbedding = CAST(JSON_QUERY(@Response, '$.result.data[0].embedding') AS VECTOR(1536)),
                EmbeddingUpdated     = GETUTCDATE()
            WHERE ProductID = @ProductID;

        FETCH NEXT FROM update_cursor INTO @ProductID, @TextToEmbed;
    END

    CLOSE update_cursor;
    DEALLOCATE update_cursor;
END;""",
                            "explanation": "This AFTER UPDATE trigger fires whenever a product row is updated. It checks whether the text fields (Description, ProductName, Category) actually changed — if only Price changed, it skips the expensive API call. For each changed row, it regenerates the embedding.",
                            "purpose": "Automatically keep embeddings synchronized with source text without requiring application-layer logic.",
                            "breakdown": [
                                {"line": "CREATE OR ALTER TRIGGER trg_ProductCatalog_UpdateEmbedding ON ProductCatalog AFTER UPDATE", "meaning": "Creates (or replaces if it exists) a trigger that runs after any UPDATE on the ProductCatalog table."},
                                {"line": "IF NOT (UPDATE(Description) OR UPDATE(ProductName) OR UPDATE(Category)) RETURN", "meaning": "The UPDATE() function returns TRUE if that column was included in the UPDATE statement. This guard prevents wasting API calls when only irrelevant columns like Price changed."},
                                {"line": "FROM inserted i", "meaning": "The 'inserted' virtual table contains the NEW values of rows that were just updated. (The 'deleted' virtual table contains the old values.) This is how triggers access the changed data."},
                                {"line": "DECLARE update_cursor CURSOR FOR SELECT ... FROM inserted i", "meaning": "Cursors in triggers handle multi-row updates. If someone updates 5 products at once, the trigger must process all 5 rows individually since each needs its own API call."}
                            ],
                            "ssms_steps": [
                                "Open SSMS and connect to your Azure SQL Database",
                                "Click New Query",
                                "Paste the CREATE OR ALTER TRIGGER code above",
                                "Replace YOUR-RESOURCE and YOUR-API-KEY with actual values",
                                "Press F5 to create the trigger",
                                "Test it: UPDATE ProductCatalog SET Description = 'Updated description here' WHERE ProductID = 1",
                                "Wait a few seconds for the API call to complete",
                                "Check: SELECT ProductID, EmbeddingUpdated FROM ProductCatalog WHERE ProductID = 1",
                                "The EmbeddingUpdated timestamp should be the current time"
                            ],
                            "exam_tip": "Triggers that call external APIs add latency to every UPDATE statement. For high-volume tables, consider using the trigger to mark rows as 'dirty' (add a NeedsEmbeddingRefresh BIT column) and then process those rows asynchronously with a background job instead."
                        },
                        {
                            "type": "tip",
                            "title": "Incremental Embedding Updates",
                            "body": "Instead of regenerating all embeddings when you change models, use a version column:\n<code>EmbeddingVersion NVARCHAR(50) DEFAULT 'ada-002-v1'</code>\n\nWhen you switch to a new model, run a batch job: <code>WHERE EmbeddingVersion != 'ada-002-v2'</code>. This way you can track which rows have been updated to the new model and which still need processing."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "Which JSON function extracts the embedding array from the Azure OpenAI API response?",
                            "opts": ["A. JSON_VALUE", "B. JSON_QUERY", "C. OPENJSON", "D. JSON_ARRAY"],
                            "correct": "B",
                            "explain": "JSON_QUERY extracts a JSON fragment (object or array) rather than a scalar value. Since the embedding is a JSON array ([0.023, -0.015, ...]), you must use JSON_QUERY. JSON_VALUE only works for scalar string/number values."
                        },
                        {
                            "q": "In an AFTER UPDATE trigger, which virtual table contains the NEW values of the updated rows?",
                            "opts": ["A. updated", "B. new", "C. inserted", "D. modified"],
                            "correct": "C",
                            "explain": "In SQL Server triggers, 'inserted' contains the new row values (after the change) and 'deleted' contains the old row values (before the change). This applies to both INSERT and UPDATE triggers."
                        },
                        {
                            "q": "Why should a trigger that regenerates embeddings check UPDATE(Description) before calling the API?",
                            "opts": ["A. Because SQL Server requires it for all triggers", "B. To avoid making unnecessary API calls when unrelated columns like Price are updated", "C. Because UPDATE() is required to access the inserted table", "D. To prevent the trigger from running more than once"],
                            "correct": "B",
                            "explain": "The UPDATE(column_name) function returns TRUE if that column was included in the UPDATE statement. Checking this prevents expensive Azure OpenAI API calls when only non-text columns like Price or Category changed, reducing cost and latency."
                        },
                        {
                            "q": "What does WHERE DescriptionEmbedding IS NULL accomplish in a batch embedding job?",
                            "opts": ["A. It deletes rows without embeddings", "B. It limits processing to only rows that have not yet had an embedding generated, making the job safe to re-run", "C. It filters out rows where the description is empty", "D. It selects only the first row in the table"],
                            "correct": "B",
                            "explain": "Filtering for NULL embeddings means the batch job only processes rows that need embeddings. This makes it idempotent (safe to run multiple times) — already-processed rows are skipped, so a re-run only handles new rows."
                        },
                        {
                            "q": "How do you convert a JSON embedding array string into the SQL VECTOR type for storage?",
                            "opts": ["A. CONVERT(VECTOR(1536), @EmbeddingJSON)", "B. CAST(@EmbeddingJSON AS VECTOR(1536))", "C. VECTOR_FROM_JSON(@EmbeddingJSON)", "D. INSERT INTO VECTOR VALUES (@EmbeddingJSON)"],
                            "correct": "B",
                            "explain": "CAST(@EmbeddingJSON AS VECTOR(1536)) converts the JSON array string extracted from the API response into the native VECTOR data type. SQL Server parses the JSON array and creates the efficient binary vector representation."
                        }
                    ]
                },

                # ── Unit 6: Exercise ──────────────────────────────────────
                {
                    "id": "lp3-m9-u6",
                    "title": "Exercise",
                    "description": "Hands-on exercise: build a complete embeddings solution for a knowledge base table.",
                    "estimated_time": 45,
                    "objectives": [
                        "Create a knowledge base table with a VECTOR column",
                        "Set up the external credential and data source for Azure OpenAI",
                        "Populate embeddings for existing rows",
                        "Create a trigger to auto-maintain embeddings"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Exercise: Build a Knowledge Base with Embeddings",
                            "body": "<strong>Scenario:</strong> You work for a company that has a support knowledge base — a table of troubleshooting articles. Your task is to add AI-powered semantic search capability by storing embeddings for each article.\n\n<strong>What you will build:</strong>\n<ol><li>A <code>KnowledgeBase</code> table with a VECTOR column for article embeddings</li><li>The credential and external data source for Azure OpenAI</li><li>A script to generate embeddings for 5 sample articles</li><li>A trigger that auto-regenerates embeddings when article content changes</li><li>A verification query that shows all articles have embeddings</li></ol>\n\n<strong>Prerequisites:</strong>\n<ul><li>Access to an Azure SQL Database (Azure subscription required)</li><li>An Azure OpenAI resource with text-embedding-ada-002 deployed</li><li>SQL Server Management Studio (SSMS) installed</li></ul>"
                        },
                        {
                            "type": "sql_block",
                            "title": "Exercise Step 1 — Set Up the Database and Table",
                            "scenario": "Create the KnowledgeBase table and insert 5 sample articles without embeddings yet.",
                            "code": """-- Exercise Step 1: Create the KnowledgeBase table
CREATE TABLE KnowledgeBase (
    ArticleID   INT           PRIMARY KEY IDENTITY(1,1),
    Title       NVARCHAR(300) NOT NULL,
    Content     NVARCHAR(MAX) NOT NULL,
    Category    NVARCHAR(100),
    ContentEmbedding  VECTOR(1536),           -- Will be populated in Step 3
    EmbeddingUpdated  DATETIME2
);

-- Insert 5 sample support articles (no embeddings yet)
INSERT INTO KnowledgeBase (Title, Content, Category) VALUES
('How to reset your password',
 'To reset your password, click Forgot Password on the login page. Enter your email address and check your inbox for a reset link. The link expires in 24 hours. If you do not receive the email, check your spam folder.',
 'Account Management'),

('Setting up two-factor authentication',
 'Two-factor authentication (2FA) adds an extra layer of security. Go to Account Settings, click Security, then Enable 2FA. Download an authenticator app like Microsoft Authenticator. Scan the QR code shown on screen.',
 'Security'),

('Uploading files to your workspace',
 'To upload files, click the Upload button in the top toolbar. You can drag and drop files or browse for them. Supported formats include PDF, DOCX, XLSX, PNG, and JPG. Maximum file size is 100MB.',
 'File Management'),

('Billing and subscription management',
 'To view your current plan and billing history, go to Settings > Billing. You can upgrade or downgrade your plan at any time. Changes take effect at the start of the next billing cycle. Refunds are not available for partial months.',
 'Billing'),

('Connecting to external data sources',
 'You can connect to external databases, APIs, and cloud storage. Go to Integrations > Add Connection. Select your data source type and provide the required credentials. Connections are encrypted and credentials are stored securely.',
 'Integrations');

-- Verify the table
SELECT ArticleID, Title, Category, ContentEmbedding AS EmbeddingIsNull
FROM KnowledgeBase;""",
                            "explanation": "This creates the KnowledgeBase table and inserts 5 realistic support articles. Note that ContentEmbedding is NULL for all rows — you will populate these in Step 3.",
                            "purpose": "Set up the base table and sample data for the exercise.",
                            "breakdown": [
                                {"line": "ContentEmbedding VECTOR(1536)", "meaning": "The embedding column, using the VECTOR data type with 1536 dimensions to match text-embedding-ada-002."},
                                {"line": "INSERT INTO KnowledgeBase ... VALUES ...", "meaning": "Inserts 5 sample articles with realistic support content. ContentEmbedding is not included so it defaults to NULL."}
                            ],
                            "ssms_steps": [
                                "Open SSMS and connect to your Azure SQL Database",
                                "Click New Query",
                                "Paste Step 1 code and press F5",
                                "You should see 5 rows returned with NULL in the EmbeddingIsNull column",
                                "This confirms the table is set up and data is inserted"
                            ],
                            "exam_tip": "In exercises, always verify each step before moving to the next. Check row counts and NULL values match your expectations."
                        },
                        {
                            "type": "sql_block",
                            "title": "Exercise Step 2 — Set Up Azure OpenAI Connection",
                            "scenario": "Create the master key, credential, and external data source that will allow T-SQL to call Azure OpenAI.",
                            "code": """-- Exercise Step 2: Set up Azure OpenAI connection

-- 2a: Create database master key (if not already exists)
IF NOT EXISTS (SELECT 1 FROM sys.symmetric_keys WHERE name = '##MS_DatabaseMasterKey##')
    CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'Exercise@Str0ngPass1!';

-- 2b: Create credential with your Azure OpenAI API key
CREATE DATABASE SCOPED CREDENTIAL [ExerciseOpenAI_Cred]
WITH
    IDENTITY = 'HTTPEndpointHeaders',
    SECRET   = '{"api-key": "PASTE-YOUR-API-KEY-HERE"}';

-- 2c: Create external data source
CREATE EXTERNAL DATA SOURCE [ExerciseOpenAI]
WITH (
    LOCATION   = 'https://YOUR-RESOURCE-NAME.openai.azure.com',
    CREDENTIAL = [ExerciseOpenAI_Cred]
);

-- 2d: Verify the objects were created
SELECT 'Credential' AS ObjectType, name FROM sys.database_scoped_credentials
UNION ALL
SELECT 'External Data Source', name FROM sys.external_data_sources;""",
                            "explanation": "This sets up the three objects needed before calling Azure OpenAI from T-SQL: the master key (encryption root), a scoped credential (stores the API key), and an external data source (registers the endpoint URL).",
                            "purpose": "Configure the Azure OpenAI connection for the exercise.",
                            "breakdown": [
                                {"line": "IF NOT EXISTS (...) CREATE MASTER KEY", "meaning": "Safe pattern — only creates the master key if one does not already exist. Running this on a database that already has a master key would error without the IF NOT EXISTS guard."}
                            ],
                            "ssms_steps": [
                                "In Azure Portal, navigate to your Azure OpenAI resource",
                                "Click Keys and Endpoint in the left menu",
                                "Copy KEY 1 and the Endpoint URL",
                                "Back in SSMS, paste Step 2 code into a new query",
                                "Replace PASTE-YOUR-API-KEY-HERE with your copied key",
                                "Replace YOUR-RESOURCE-NAME with the name from your endpoint URL",
                                "Press F5 and verify the final SELECT shows both the credential and data source"
                            ],
                            "exam_tip": "In the exam, you may be asked about the order of operations: Master Key FIRST, then Credential, then External Data Source. Skipping any step causes the next one to fail."
                        },
                        {
                            "type": "sql_block",
                            "title": "Exercise Step 3 — Generate Embeddings for All Articles",
                            "scenario": "Call Azure OpenAI for each article and store the embedding vectors in the ContentEmbedding column.",
                            "code": """-- Exercise Step 3: Generate embeddings for all 5 articles
DECLARE @ArticleID   INT;
DECLARE @TextToEmbed NVARCHAR(MAX);
DECLARE @Payload     NVARCHAR(MAX);
DECLARE @Response    NVARCHAR(MAX);
DECLARE @StatusCode  INT;
DECLARE @Count       INT = 0;

DECLARE article_cursor CURSOR FOR
    SELECT ArticleID, Title + '. ' + Content + ' Category: ' + ISNULL(Category, '')
    FROM KnowledgeBase
    WHERE ContentEmbedding IS NULL;

OPEN article_cursor;
FETCH NEXT FROM article_cursor INTO @ArticleID, @TextToEmbed;

WHILE @@FETCH_STATUS = 0
BEGIN
    SET @Payload = N'{"input": ' + (SELECT @TextToEmbed FOR JSON PATH, WITHOUT_ARRAY_WRAPPER) + '}';

    EXEC sp_invoke_external_rest_endpoint
        @url        = 'https://YOUR-RESOURCE-NAME.openai.azure.com/openai/deployments/text-embedding-ada-002/embeddings?api-version=2023-05-15',
        @method     = 'POST',
        @headers    = N'{"Content-Type": "application/json", "api-key": "YOUR-API-KEY"}',
        @payload    = @Payload,
        @response   = @Response OUTPUT,
        @statuscode = @StatusCode OUTPUT;

    IF @StatusCode = 200
    BEGIN
        UPDATE KnowledgeBase
        SET ContentEmbedding = CAST(JSON_QUERY(@Response, '$.result.data[0].embedding') AS VECTOR(1536)),
            EmbeddingUpdated = GETUTCDATE()
        WHERE ArticleID = @ArticleID;

        SET @Count = @Count + 1;
        PRINT 'Embedded article ' + CAST(@ArticleID AS VARCHAR);
    END
    ELSE
        PRINT 'FAILED for article ' + CAST(@ArticleID AS VARCHAR) + ' - HTTP ' + CAST(@StatusCode AS VARCHAR);

    FETCH NEXT FROM article_cursor INTO @ArticleID, @TextToEmbed;
END

CLOSE article_cursor;
DEALLOCATE article_cursor;

-- Verify all embeddings were created
SELECT
    ArticleID,
    Title,
    CASE WHEN ContentEmbedding IS NULL THEN 'MISSING' ELSE 'OK' END AS EmbeddingStatus,
    EmbeddingUpdated
FROM KnowledgeBase;

PRINT 'Total embeddings generated: ' + CAST(@Count AS VARCHAR);""",
                            "explanation": "Iterates through all articles without embeddings, calls Azure OpenAI for each one, and stores the result. The final SELECT confirms all 5 articles have embeddings.",
                            "purpose": "Populate embeddings for all existing knowledge base articles.",
                            "breakdown": [
                                {"line": "Title + '. ' + Content + ' Category: ' + ISNULL(Category, '')", "meaning": "Builds a rich text string combining the title, content, and category. Including the title helps the embedding capture the article's topic more accurately."}
                            ],
                            "ssms_steps": [
                                "Paste Step 3 code into a new query window in SSMS",
                                "Replace YOUR-RESOURCE-NAME and YOUR-API-KEY",
                                "Press F5 — you should see 'Embedded article 1' through 'Embedded article 5' in the Messages tab",
                                "The final SELECT should show EmbeddingStatus = 'OK' for all 5 rows",
                                "If any show 'MISSING', check the error messages and retry"
                            ],
                            "exam_tip": "Always print progress messages during batch operations. If the script fails midway, you can re-run it safely because the WHERE ContentEmbedding IS NULL filter skips already-processed rows."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "In the exercise, why does the INSERT into KnowledgeBase not include a value for ContentEmbedding?",
                            "opts": ["A. Because VECTOR columns cannot be inserted directly", "B. Because the embedding is generated separately after the text data exists", "C. Because ContentEmbedding has a DEFAULT value of 0", "D. Because Azure SQL does not support VECTOR in INSERT statements"],
                            "correct": "B",
                            "explain": "Embeddings are generated by calling an external AI API — they cannot be computed at INSERT time without that API call. The pattern is: INSERT the text data first (embedding = NULL), then run a separate process to generate and UPDATE the embedding."
                        },
                        {
                            "q": "In the exercise, the text embedded for each article combines the Title, Content, and Category. Why include the Title?",
                            "opts": ["A. Because the Azure OpenAI API requires a title field", "B. To make the embedding larger and use more storage", "C. To help the embedding capture the article's topic more accurately, improving search relevance", "D. Because Content is too short to embed alone"],
                            "correct": "C",
                            "explain": "Including the title in the embedded text helps the AI model understand the article's main topic. A search for 'how to change my password' will match better with an embedding that includes 'How to reset your password' in the text than one that only has the body content."
                        },
                        {
                            "q": "In Step 2 of the exercise, why is IF NOT EXISTS used before CREATE MASTER KEY?",
                            "opts": ["A. It is required syntax for CREATE MASTER KEY", "B. To safely skip creation if the master key already exists, preventing an error", "C. To check if Azure OpenAI is available", "D. To verify the database is online"],
                            "correct": "B",
                            "explain": "A database can only have one master key. If one already exists (from a previous setup), CREATE MASTER KEY would fail with an error. The IF NOT EXISTS guard makes the script idempotent — safe to run multiple times."
                        },
                        {
                            "q": "After running the batch embedding script, how do you verify all articles have embeddings?",
                            "opts": ["A. Check sys.external_data_sources", "B. Run SELECT ArticleID, CASE WHEN ContentEmbedding IS NULL THEN 'MISSING' ELSE 'OK' END FROM KnowledgeBase", "C. Check the Azure OpenAI usage dashboard", "D. Run DBCC CHECKDB"],
                            "correct": "B",
                            "explain": "Querying the table with a CASE expression to flag NULL embeddings as 'MISSING' and non-NULL as 'OK' is the most direct way to verify embedding population status."
                        },
                        {
                            "q": "What would happen if you ran the batch embedding script from Step 3 a second time on the same database?",
                            "opts": ["A. It would generate duplicate embeddings for all rows", "B. It would fail with an error because embeddings already exist", "C. It would skip all rows because they already have embeddings (WHERE ContentEmbedding IS NULL filters them out)", "D. It would delete the existing embeddings first"],
                            "correct": "C",
                            "explain": "The WHERE ContentEmbedding IS NULL filter means the cursor selects zero rows on the second run (all rows already have embeddings). The loop runs zero times, and the script completes with 'Total embeddings generated: 0'."
                        }
                    ]
                },

                # ── Unit 7: Knowledge Check ───────────────────────────────
                {
                    "id": "lp3-m9-u7",
                    "title": "Knowledge Check",
                    "description": "Review key concepts from Module 9 and test your understanding.",
                    "estimated_time": 15,
                    "objectives": [
                        "Review the key concepts from Module 9",
                        "Test understanding of models, embeddings, and T-SQL integration"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Module 9 Key Concepts Review",
                            "body": "Before taking the knowledge check, review these core concepts:\n\n<strong>External Model Setup (3 steps):</strong>\n<ol><li>CREATE MASTER KEY — encryption foundation</li><li>CREATE DATABASE SCOPED CREDENTIAL with IDENTITY='HTTPEndpointHeaders' — stores API key</li><li>CREATE EXTERNAL DATA SOURCE — registers the endpoint URL</li></ol>\n\n<strong>Embedding Facts:</strong>\n<ul><li>text-embedding-ada-002 produces 1536-dimensional vectors</li><li>VECTOR(1536) is the native SQL data type for storing embeddings</li><li>JSON_QUERY extracts the embedding array from the API response</li><li>CAST(@json AS VECTOR(1536)) converts to the VECTOR type</li></ul>\n\n<strong>Maintenance Patterns:</strong>\n<ul><li>Batch job with cursor — populate all NULL embeddings</li><li>AFTER UPDATE trigger — auto-regenerate when source text changes</li><li>Check UPDATE(column) in triggers to skip unnecessary API calls</li><li>Version column — track which model version generated each embedding</li></ul>\n\n<strong>Model Selection:</strong>\n<ul><li>Embedding models: text-embedding-ada-002, text-embedding-3-small/large</li><li>Chat models: gpt-4o, gpt-4, gpt-35-turbo</li><li>Key tradeoffs: accuracy vs. cost vs. latency vs. token limits</li></ul>"
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What is the correct order for setting up an Azure OpenAI connection in SQL Server?",
                            "opts": ["A. External Data Source → Credential → Master Key", "B. Master Key → Credential → External Data Source", "C. Credential → Master Key → External Data Source", "D. External Data Source → Master Key → Credential"],
                            "correct": "B",
                            "explain": "The correct order is: (1) Create Master Key — the encryption foundation, (2) Create Database Scoped Credential — uses the master key to encrypt the API key, (3) Create External Data Source — references the credential. Each step depends on the previous one."
                        },
                        {
                            "q": "A company has a product table with 500,000 rows. They want to use text-embedding-ada-002 (1536 dimensions). Approximately how much storage will the embedding column require?",
                            "opts": ["A. About 3 GB", "B. About 300 MB", "C. About 30 GB", "D. About 30 MB"],
                            "correct": "A",
                            "explain": "1536 dimensions × 4 bytes per float = 6,144 bytes per row. 6,144 × 500,000 = ~3.07 GB. Always plan for embedding column storage when designing your schema."
                        },
                        {
                            "q": "Which system view would you query to check the list of database-scoped credentials that exist in a database?",
                            "opts": ["A. sys.server_principals", "B. sys.database_scoped_credentials", "C. sys.objects", "D. sys.external_files"],
                            "correct": "B",
                            "explain": "sys.database_scoped_credentials lists all DATABASE SCOPED CREDENTIAL objects in the current database. Note that querying this view shows the credential names but not the SECRET values — those remain encrypted."
                        },
                        {
                            "q": "An AFTER UPDATE trigger regenerates embeddings. A user updates only the Price column of a product. What should happen?",
                            "opts": ["A. The trigger should regenerate the embedding anyway to be safe", "B. The trigger should skip the API call because UPDATE(Description) and UPDATE(ProductName) return FALSE", "C. The trigger should delete the existing embedding", "D. The trigger should log an error"],
                            "correct": "B",
                            "explain": "Using IF NOT (UPDATE(Description) OR UPDATE(ProductName) OR UPDATE(Category)) RETURN at the start of the trigger checks if any text columns changed. If only Price changed, this evaluates to TRUE and the trigger returns early without making an API call."
                        },
                        {
                            "q": "Which path in the Azure OpenAI JSON response contains the embedding values?",
                            "opts": ["A. $.result.embedding", "B. $.result.data[0].embedding", "C. $.data.embedding[0]", "D. $.choices[0].embedding"],
                            "correct": "B",
                            "explain": "The Azure OpenAI embedding API response structure is: result > data (array) > [0] (first element) > embedding (the vector array). The correct JSON path is $.result.data[0].embedding, accessed with JSON_QUERY()."
                        }
                    ]
                },

                # ── Unit 8: Summary ───────────────────────────────────────
                {
                    "id": "lp3-m9-u8",
                    "title": "Summary",
                    "description": "Review what you learned in Module 9 about AI models and embeddings in SQL.",
                    "estimated_time": 5,
                    "objectives": [
                        "Consolidate knowledge of AI model integration with SQL",
                        "Review the key T-SQL objects and patterns for embeddings"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Module 9 Summary",
                            "body": "In this module you learned:\n\n<strong>AI Models and SQL Integration</strong>\n<ul><li>SQL databases can call external AI APIs using <strong>sp_invoke_external_rest_endpoint</strong></li><li>This enables embedding generation, text analysis, and AI-powered operations from T-SQL</li><li>Two model types: <strong>embedding models</strong> (text → vector) and <strong>chat/completion models</strong> (text → text)</li></ul>\n\n<strong>Setting Up External Model Connections</strong>\n<ul><li>Three objects required: <strong>Master Key → Credential → External Data Source</strong></li><li>Credentials use IDENTITY='HTTPEndpointHeaders' to pass API keys as HTTP headers</li><li>External Data Sources register the base URL and link to the credential</li></ul>\n\n<strong>Vector Embeddings</strong>\n<ul><li>Embeddings are numerical vectors (e.g., 1536 numbers) representing text meaning</li><li>Similar text → similar embeddings; measured by cosine similarity</li><li>The <strong>VECTOR(n)</strong> data type stores embeddings natively in Azure SQL / SQL Server 2025</li></ul>\n\n<strong>Generating and Maintaining Embeddings</strong>\n<ul><li>Call Azure OpenAI API → parse with JSON_QUERY → CAST to VECTOR(1536) → store with UPDATE</li><li>Batch jobs process existing rows (filter with WHERE column IS NULL)</li><li>Triggers auto-regenerate when source text changes (use UPDATE() guard to avoid unnecessary calls)</li><li>Version columns help track when embeddings need to be refreshed due to model changes</li></ul>\n\n<strong>Next:</strong> In Module 10, you will use these stored embeddings to build powerful search capabilities using full-text search, vector search, and hybrid approaches."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What is the primary purpose of storing embeddings in a SQL database?",
                            "opts": ["A. To compress text data and save storage", "B. To enable semantic similarity search — finding data conceptually similar to a query", "C. To encrypt sensitive text columns", "D. To improve T-SQL query compilation speed"],
                            "correct": "B",
                            "explain": "Embeddings enable semantic search — you can find rows that are conceptually similar to a query even without matching keywords. This is the key value proposition of storing embeddings in SQL."
                        },
                        {
                            "q": "Which SQL Server feature requires Azure SQL Database or SQL Server 2025?",
                            "opts": ["A. CREATE TABLE", "B. sp_execute_external_script", "C. The VECTOR data type and sp_invoke_external_rest_endpoint", "D. FULL TEXT CATALOG"],
                            "correct": "C",
                            "explain": "Both the VECTOR data type and sp_invoke_external_rest_endpoint are only available in Azure SQL Database and SQL Server 2025. They are not available in older SQL Server versions (2019 or earlier)."
                        },
                        {
                            "q": "After this module, what would be your next step to build a product search feature using embeddings?",
                            "opts": ["A. Create a new Azure subscription", "B. Use VECTOR_DISTANCE to find products whose embeddings are closest to a user's search query embedding", "C. Convert embeddings back to text and use LIKE", "D. Delete the embedding column and use full-text search instead"],
                            "correct": "B",
                            "explain": "With embeddings stored, the next step is to use VECTOR_DISTANCE to find the rows whose embedding vectors are closest (most similar) to the embedding of the user's search query. This is vector search, covered in Module 10."
                        },
                        {
                            "q": "How many floating-point numbers does a text-embedding-ada-002 embedding contain?",
                            "opts": ["A. 768", "B. 1024", "C. 1536", "D. 3072"],
                            "correct": "C",
                            "explain": "text-embedding-ada-002 produces a 1536-dimensional vector — 1536 floating-point numbers. This is why you use VECTOR(1536) as the column type when storing ada-002 embeddings."
                        },
                        {
                            "q": "What happens to the embedding stored in a row if you update the row's Description text but do NOT have an AFTER UPDATE trigger?",
                            "opts": ["A. SQL Server automatically regenerates the embedding", "B. The embedding becomes stale — it still reflects the old Description text", "C. SQL Server deletes the embedding and sets it to NULL", "D. The UPDATE fails because the embedding no longer matches"],
                            "correct": "B",
                            "explain": "Embeddings are NOT automatically regenerated when source text changes — they are static values stored in a column. Without a trigger or manual refresh process, the embedding stays as it was when last generated, no longer reflecting the updated Description."
                        }
                    ]
                }
            ]
        },

        # ══════════════════════════════════════════════════════
        # MODULE 10 — Design and implement intelligent search
        # ══════════════════════════════════════════════════════
        {
            "id": "lp3-m10",
            "title": "Design and implement intelligent search with SQL",
            "description": "Learn to implement full-text search, vector similarity search, and hybrid search in SQL Server to power intelligent search experiences.",
            "units": [

                # ── Unit 1: Introduction ──────────────────────────────────
                {
                    "id": "lp3-m10-u1",
                    "title": "Introduction",
                    "description": "Overview of intelligent search approaches available in SQL Server.",
                    "estimated_time": 5,
                    "objectives": [
                        "Understand the three main search approaches available in SQL",
                        "Know when each approach is appropriate",
                        "Preview the module content"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Why 'Intelligent Search'?",
                            "body": "Traditional SQL search uses WHERE Name LIKE '%laptop%'. This only finds rows that literally contain the word 'laptop'. Users often search in natural language ('affordable computer for work') and expect to find relevant results even when exact words do not match.\n\nThis module teaches three increasingly powerful search approaches:\n\n<strong>1. Full-Text Search (FTS)</strong> — Better than LIKE. Handles word forms (run/running/ran), stopwords (ignore 'the', 'a'), and phrase searches. Still keyword-based — no understanding of meaning.\n\n<strong>2. Vector Search</strong> — Uses the embeddings from Module 9. Finds results based on semantic meaning, not keywords. A search for 'notebook computer' finds laptop results.\n\n<strong>3. Hybrid Search</strong> — Combines full-text and vector search scores for best-of-both-worlds results.\n\nBy the end of this module, you will be able to implement all three approaches in T-SQL."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What is the key limitation of using LIKE for text search?",
                            "opts": ["A. It is too slow for any query", "B. It only finds exact substring matches and cannot understand synonyms or word variations", "C. It requires a special index to work", "D. It cannot search NVARCHAR columns"],
                            "correct": "B",
                            "explain": "LIKE only matches literal substrings. LIKE '%run%' would not match 'running' or 'ran', and would miss 'jog' even though users might consider jogging and running similar."
                        },
                        {
                            "q": "Which search approach uses stored embedding vectors to find semantically similar results?",
                            "opts": ["A. Full-text search", "B. LIKE-based search", "C. Vector search", "D. Indexed views"],
                            "correct": "C",
                            "explain": "Vector search uses stored embedding vectors and a distance function (like VECTOR_DISTANCE) to find rows whose embeddings are closest to the query's embedding — matching by meaning, not keywords."
                        },
                        {
                            "q": "What does hybrid search combine?",
                            "opts": ["A. SQL and NoSQL databases", "B. Full-text search keyword scores and vector similarity scores", "C. Azure SQL and SQL Server on-premises", "D. T-SQL and Python"],
                            "correct": "B",
                            "explain": "Hybrid search combines scores from both full-text search (keyword relevance) and vector search (semantic similarity) to produce a unified ranking that benefits from both approaches."
                        },
                        {
                            "q": "A user searches for 'affordable computer for work'. Which search approach would find 'budget laptop for office use' even without keyword overlap?",
                            "opts": ["A. LIKE '%affordable computer for work%'", "B. Full-text search CONTAINS(column, 'affordable')", "C. Vector search using VECTOR_DISTANCE on stored embeddings", "D. WHERE Price < 1000"],
                            "correct": "C",
                            "explain": "Vector search compares the semantic meaning of the query embedding with stored product embeddings. 'affordable computer for work' and 'budget laptop for office use' have similar meanings, so their embeddings are close in vector space."
                        },
                        {
                            "q": "When might full-text search be preferred over vector search?",
                            "opts": ["A. When searching for exact product codes, part numbers, or specific terminology where keyword matching is more precise", "B. Always — full-text search is always better", "C. When the database is too small to store embeddings", "D. When the Azure OpenAI service is not available"],
                            "correct": "A",
                            "explain": "For exact terminology, part numbers, or domain-specific codes (like 'SKU-AB-123' or medical codes), full-text keyword matching is more precise than semantic search. Vector search works best for natural language queries."
                        }
                    ]
                },

                # ── Unit 2: Choose a search approach ─────────────────────
                {
                    "id": "lp3-m10-u2",
                    "title": "Choose a search approach",
                    "description": "Learn how to evaluate your requirements and select the right search strategy.",
                    "estimated_time": 20,
                    "objectives": [
                        "Compare full-text, vector, and hybrid search on key dimensions",
                        "Identify scenarios where each approach excels",
                        "Understand the cost and complexity tradeoffs"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Comparing the Three Search Approaches",
                            "body": "<strong>Full-Text Search (FTS)</strong>\n<ul><li><strong>How it works:</strong> Indexes individual words. Searches for word stems (run = running = ran). Ignores stopwords (the, a, is).</li><li><strong>Best for:</strong> Searching for specific terms, codes, names; high-precision keyword matching</li><li><strong>Limitations:</strong> No understanding of synonyms unless you add a thesaurus; no semantic understanding</li><li><strong>Cost:</strong> Low — just a SQL Server feature, no external API calls</li></ul>\n\n<strong>Vector Search</strong>\n<ul><li><strong>How it works:</strong> Converts the user's query to an embedding (API call), then finds stored embeddings that are closest using VECTOR_DISTANCE</li><li><strong>Best for:</strong> Natural language queries, finding similar documents, cross-language semantic matching</li><li><strong>Limitations:</strong> Requires embedding generation (cost + latency); VECTOR type only in Azure SQL / SQL Server 2025</li><li><strong>Cost:</strong> Medium — requires Azure OpenAI API calls for query embedding; ongoing storage cost</li></ul>\n\n<strong>Hybrid Search</strong>\n<ul><li><strong>How it works:</strong> Runs both FTS and vector search, then combines scores using a ranking formula (like RRF)</li><li><strong>Best for:</strong> Production search where both precision (keywords) and recall (meaning) matter</li><li><strong>Limitations:</strong> Most complex to implement and tune; highest latency</li><li><strong>Cost:</strong> Highest — combines both FTS infrastructure and vector API costs</li></ul>"
                        },
                        {
                            "type": "important",
                            "title": "Decision Guide: Which Search to Use",
                            "body": "Use this guide for the exam:\n<ul><li><strong>Use FTS when:</strong> Users search for specific product codes, names, technical terms, or when budget is a constraint</li><li><strong>Use Vector when:</strong> Users ask natural language questions; content has many synonyms; cross-language search needed</li><li><strong>Use Hybrid when:</strong> You need production-quality search that handles both precise terms AND natural language queries</li><li><strong>Don't use LIKE when:</strong> The text column has more than a few thousand rows — FTS is dramatically faster at scale</li></ul>"
                        },
                        {
                            "type": "tip",
                            "title": "Prototype Order",
                            "body": "When building a new search feature, start simple and add complexity only when needed:\n<ol><li>Start with Full-Text Search — quick to set up, no API costs</li><li>Add Vector Search if FTS quality is insufficient</li><li>Implement Hybrid Search if you need the best of both</li></ol>\nMost teams find that FTS alone handles 60-70% of use cases adequately."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "A company wants to add search to their parts catalog. Users search by exact part numbers like 'PN-4471-B'. Which approach is most appropriate?",
                            "opts": ["A. Vector search — it handles all text queries", "B. Full-text search — it excels at exact term matching", "C. Hybrid search — always use hybrid", "D. LIKE '%PN-4471-B%' — simplest approach"],
                            "correct": "B",
                            "explain": "For exact part numbers and codes, full-text search is most appropriate. Part numbers are exact terms with no synonyms or natural language variation. Vector search would add unnecessary cost and complexity for this use case."
                        },
                        {
                            "q": "What is the primary advantage of vector search over full-text search for natural language queries?",
                            "opts": ["A. It is faster to set up", "B. It understands semantic meaning, finding relevant results even when no keywords match", "C. It does not require an index", "D. It works on older SQL Server versions"],
                            "correct": "B",
                            "explain": "Vector search compares the semantic meaning encoded in embedding vectors. A query about 'car repairs' can match documents about 'automobile maintenance' even though none of those words appear in the query."
                        },
                        {
                            "q": "Which search approach has the highest implementation complexity and latency?",
                            "opts": ["A. LIKE-based search", "B. Full-text search", "C. Vector search", "D. Hybrid search"],
                            "correct": "D",
                            "explain": "Hybrid search runs both full-text and vector search and then combines and normalizes their scores. It requires more code, more tuning, and has higher latency because it executes two search pipelines."
                        },
                        {
                            "q": "Why is LIKE a poor choice for searching large text columns with millions of rows?",
                            "opts": ["A. LIKE cannot search NVARCHAR columns", "B. LIKE with a leading wildcard (LIKE '%word%') cannot use indexes and does a full table scan", "C. LIKE only works on VARCHAR, not NVARCHAR", "D. LIKE is limited to 100 rows returned"],
                            "correct": "B",
                            "explain": "LIKE '%word%' with a leading wildcard cannot use a B-tree index — SQL Server must scan every row in the table. On millions of rows, this is extremely slow. Full-text search uses an inverted index that makes these queries fast."
                        },
                        {
                            "q": "A startup has a budget constraint and needs to add basic text search to a job listings table. Which approach should they start with?",
                            "opts": ["A. Hybrid search immediately", "B. Full-text search — it has no external API costs and is a native SQL Server feature", "C. Vector search — it produces better results", "D. LIKE — it is built into SQL and free"],
                            "correct": "B",
                            "explain": "Full-text search is a native SQL Server feature with no additional cost. For a budget-constrained startup, starting with FTS provides substantial improvement over LIKE without requiring Azure OpenAI costs. Vector search can be added later if FTS quality is insufficient."
                        }
                    ]
                },

                # ── Unit 3: Full-text search in SQL ──────────────────────
                {
                    "id": "lp3-m10-u3",
                    "title": "Full-text search in SQL",
                    "description": "Learn to set up and query SQL Server Full-Text Search for efficient keyword-based text search.",
                    "estimated_time": 30,
                    "objectives": [
                        "Create a Full-Text Catalog and Full-Text Index",
                        "Use CONTAINS for precise keyword searches",
                        "Use FREETEXT for natural language searches",
                        "Use CONTAINSTABLE and FREETEXTTABLE for ranked results",
                        "Understand stopwords and their impact"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "How Full-Text Search Works",
                            "body": "Standard SQL indexes store sorted column values and let you find rows by value quickly. Full-Text Indexes work differently — they build an <strong>inverted index</strong>:\n\n<ol><li>SQL Server reads all the text in the indexed column</li><li>It splits the text into individual words (called <strong>tokens</strong>)</li><li>It removes <strong>stopwords</strong> — common words like 'the', 'a', 'is', 'and' that are too common to be useful for filtering</li><li>It applies <strong>word stemming</strong> — reducing words to their root (running → run, ran → run)</li><li>It builds an inverted index: for each unique word root, a list of which rows contain it</li></ol>\n\nWhen you search, SQL Server looks up your search term in the inverted index and returns matching rows instantly — no table scan needed.\n\n<strong>Key components:</strong>\n<ul><li><strong>Full-Text Catalog</strong> — A container that organizes full-text indexes (like a folder)</li><li><strong>Full-Text Index</strong> — The actual inverted index built on a specific table column</li></ul>"
                        },
                        {
                            "type": "sql_block",
                            "title": "Set Up Full-Text Search — Catalog and Index",
                            "scenario": "You have a ProductCatalog table and want to enable fast full-text search on the Description and ProductName columns.",
                            "code": """-- Step 1: Create a Full-Text Catalog (container for FT indexes)
CREATE FULLTEXT CATALOG ProductFTSCatalog AS DEFAULT;

-- Step 2: Create a Full-Text Index on the ProductCatalog table
-- The table must have a unique single-column index (like a primary key)
CREATE FULLTEXT INDEX ON ProductCatalog
(
    ProductName    LANGUAGE 1033,    -- 1033 = English
    Description    LANGUAGE 1033
)
KEY INDEX PK__ProductC__B40CC6ED     -- Name of your PRIMARY KEY index
ON ProductFTSCatalog                 -- The catalog to use
WITH CHANGE_TRACKING AUTO;           -- Auto-update index when data changes

-- Verify the full-text index was created
SELECT
    t.name   AS table_name,
    c.name   AS column_name,
    l.name   AS language
FROM sys.fulltext_index_columns fic
JOIN sys.tables     t ON fic.object_id = t.object_id
JOIN sys.columns    c ON fic.object_id = c.object_id AND fic.column_id = c.column_id
JOIN sys.fulltext_languages l ON fic.language_id = l.lcid;""",
                            "explanation": "Creating a Full-Text Catalog and Index is a two-step process. The catalog is the container; the index does the actual work. Once created, SQL Server automatically indexes all existing data and keeps the index updated as data changes.",
                            "purpose": "Enable fast keyword search on text columns without requiring full table scans.",
                            "breakdown": [
                                {"line": "CREATE FULLTEXT CATALOG ProductFTSCatalog AS DEFAULT", "meaning": "Creates a named catalog (container). AS DEFAULT means this catalog is used when no catalog is specified in CREATE FULLTEXT INDEX. A database can have multiple catalogs, typically one per application or use case."},
                                {"line": "CREATE FULLTEXT INDEX ON ProductCatalog", "meaning": "Starts defining the full-text index on the ProductCatalog table. SQL Server will build an inverted word index for the specified columns."},
                                {"line": "ProductName LANGUAGE 1033", "meaning": "Indexes the ProductName column with English language rules (1033 is the LCID code for English). The language setting determines which stemmer and stopword list to use."},
                                {"line": "KEY INDEX PK__ProductC__B40CC6ED", "meaning": "Full-text indexes require a regular unique index to link back to table rows. Specify the name of your table's primary key index here. Find it with: SELECT name FROM sys.indexes WHERE object_id = OBJECT_ID('ProductCatalog') AND is_primary_key = 1"},
                                {"line": "WITH CHANGE_TRACKING AUTO", "meaning": "Tells SQL Server to automatically update the full-text index when rows are inserted, updated, or deleted. MANUAL means you must rebuild manually; OFF means changes are never tracked."}
                            ],
                            "ssms_steps": [
                                "Open SSMS and connect to your database",
                                "First find your primary key index name: SELECT name FROM sys.indexes WHERE object_id = OBJECT_ID('ProductCatalog') AND is_primary_key = 1",
                                "Copy the index name from the results",
                                "Open a New Query window",
                                "Paste the CREATE FULLTEXT CATALOG statement and press F5",
                                "Paste the CREATE FULLTEXT INDEX statement, replace the KEY INDEX name with yours, and press F5",
                                "Wait a few seconds for SQL Server to build the index",
                                "Run the verification query to confirm the index is set up"
                            ],
                            "exam_tip": "Full-Text Indexes require: (1) The table must have a unique, non-nullable single-column index (primary key works). (2) You must specify a language for stemming and stopwords. CHANGE_TRACKING AUTO is recommended for tables that are frequently updated."
                        },
                        {
                            "type": "sql_block",
                            "title": "Searching with CONTAINS and FREETEXT",
                            "scenario": "Users search your product catalog. Implement both precise keyword search (CONTAINS) and natural language search (FREETEXT).",
                            "code": """-- CONTAINS: Precise keyword matching (supports operators)
-- Search for products where Description contains 'wireless'
SELECT ProductID, ProductName, Description
FROM ProductCatalog
WHERE CONTAINS(Description, 'wireless');

-- CONTAINS with AND: both words must appear
SELECT ProductID, ProductName
FROM ProductCatalog
WHERE CONTAINS(Description, '"wireless" AND "keyboard"');

-- CONTAINS with OR: either word
SELECT ProductID, ProductName
FROM ProductCatalog
WHERE CONTAINS(Description, '"wireless" OR "bluetooth"');

-- CONTAINS with prefix: words starting with 'wire'
SELECT ProductID, ProductName
FROM ProductCatalog
WHERE CONTAINS(Description, '"wire*"');

-- FREETEXT: Natural language mode (no operators, uses stemming)
-- Finds: laptop, laptops, notebook computers, portable computers
SELECT ProductID, ProductName
FROM ProductCatalog
WHERE FREETEXT(Description, 'portable laptop computer for travel');

-- FREETEXT on multiple columns at once
SELECT ProductID, ProductName
FROM ProductCatalog
WHERE FREETEXT((ProductName, Description), 'fast lightweight laptop');""",
                            "explanation": "CONTAINS gives you precise control with Boolean operators. FREETEXT is simpler — it breaks your phrase into words, applies stemming, and finds rows that match any of the stems. Use CONTAINS when precision matters; FREETEXT when natural language queries are expected.",
                            "purpose": "Demonstrate the two main full-text search query functions and their syntax differences.",
                            "breakdown": [
                                {"line": "WHERE CONTAINS(Description, 'wireless')", "meaning": "Finds rows where the Description column's full-text index contains the word 'wireless'. Much faster than LIKE '%wireless%' and supports word stemming."},
                                {"line": "CONTAINS(Description, '\"wireless\" AND \"keyboard\"')", "meaning": "Both words must appear in the Description. Double quotes around each word are required for CONTAINS Boolean expressions."},
                                {"line": "CONTAINS(Description, '\"wire*\"')", "meaning": "Prefix search: finds words starting with 'wire' — wireless, wired, wireframe, etc. The * is a wildcard for word endings, not the same as SQL LIKE."},
                                {"line": "FREETEXT(Description, 'portable laptop computer for travel')", "meaning": "Breaks the phrase into meaningful words (ignoring 'for'), stems each word, and finds rows containing any of those stems. More permissive than CONTAINS — good for search bars where users type natural language."},
                                {"line": "FREETEXT((ProductName, Description), 'fast lightweight laptop')", "meaning": "Searches both ProductName and Description columns simultaneously. The column list in parentheses allows multi-column search with one predicate."}
                            ],
                            "ssms_steps": [
                                "Open SSMS with a New Query connected to your database (with FTS set up)",
                                "Run the CONTAINS example: WHERE CONTAINS(Description, 'wireless')",
                                "Note how it finds all rows with 'wireless' (and 'wirelessly', 'wireless-enabled' due to stemming)",
                                "Try the AND version to narrow results",
                                "Run the FREETEXT example with a natural language phrase",
                                "Compare the result sets — FREETEXT typically returns more rows with lower precision",
                                "If no rows returned, check that your description text actually contains relevant words"
                            ],
                            "exam_tip": "Key difference for the exam: CONTAINS supports Boolean operators (AND, OR, NOT, NEAR) and is precision-focused. FREETEXT automatically breaks phrases into words and applies stemming — it is simpler but less precise. Both are faster than LIKE on large tables."
                        },
                        {
                            "type": "sql_block",
                            "title": "Ranked Results with CONTAINSTABLE and FREETEXTTABLE",
                            "scenario": "You want to show search results ordered by how relevant they are to the search query, not just return all matching rows.",
                            "code": """-- FREETEXTTABLE returns rows with a RANK score (0-1000)
-- Higher RANK = more relevant
SELECT
    p.ProductID,
    p.ProductName,
    p.Description,
    fts.RANK AS relevance_score
FROM ProductCatalog p
INNER JOIN FREETEXTTABLE(ProductCatalog, Description, 'wireless portable keyboard') fts
    ON p.ProductID = fts.[KEY]
ORDER BY fts.RANK DESC;

-- CONTAINSTABLE with ranked results and a minimum rank threshold
SELECT
    p.ProductID,
    p.ProductName,
    fts.RANK AS relevance_score
FROM ProductCatalog p
INNER JOIN CONTAINSTABLE(ProductCatalog, Description, 'wireless AND keyboard', 50) fts
    ON p.ProductID = fts.[KEY]
WHERE fts.RANK >= 50     -- Only return results with rank 50 or higher
ORDER BY fts.RANK DESC
FETCH FIRST 10 ROWS ONLY;""",
                            "explanation": "FREETEXTTABLE and CONTAINSTABLE are the table-valued versions of FREETEXT and CONTAINS. They return a two-column result set: [KEY] (the row identifier) and RANK (relevance score 0-1000). You JOIN them to your main table to get the full row data plus the relevance score.",
                            "purpose": "Retrieve search results with relevance rankings so users see the most relevant results first.",
                            "breakdown": [
                                {"line": "FREETEXTTABLE(ProductCatalog, Description, 'wireless portable keyboard')", "meaning": "A table-valued function that returns {KEY, RANK} pairs for matching rows. ProductCatalog = table, Description = column, the string = search phrase."},
                                {"line": "INNER JOIN ... ON p.ProductID = fts.[KEY]", "meaning": "Joins the full-text results back to the main table using the primary key. [KEY] is always the column defined as KEY INDEX in the full-text index definition."},
                                {"line": "fts.RANK DESC", "meaning": "Orders results by relevance score descending. RANK ranges from 0 to 1000; 1000 means an exact, complete match."},
                                {"line": "CONTAINSTABLE(ProductCatalog, Description, 'wireless AND keyboard', 50)", "meaning": "The last parameter (50) is the minimum rank threshold — only returns rows with RANK >= 50. This filters out weakly matching results."}
                            ],
                            "ssms_steps": [
                                "Open SSMS with a New Query window",
                                "Paste the FREETEXTTABLE query",
                                "Replace the search phrase with something relevant to your data",
                                "Press F5 to run",
                                "In the results, note the RANK column — higher values indicate more relevant results",
                                "Sort the results grid by relevance_score descending",
                                "Try different search phrases and compare the RANK values"
                            ],
                            "exam_tip": "CONTAINSTABLE and FREETEXTTABLE are the table-valued function equivalents of CONTAINS and FREETEXT. The key column is always named [KEY] and the relevance score is always named RANK (0-1000). You must JOIN on [KEY] to get the actual row data."
                        },
                        {
                            "type": "tip",
                            "title": "Stopwords and Their Impact",
                            "body": "Stopwords are common words excluded from full-text indexes (the, a, is, and, of, in, etc.). This means:\n<ul><li>Searching for 'a wireless keyboard' is equivalent to searching for 'wireless keyboard' — 'a' is a stopword and is ignored</li><li>Searching for a phrase that is ALL stopwords (e.g., 'a and the') returns no results</li><li>You can view the default stoplist: <code>SELECT stopword FROM sys.fulltext_system_stopwords WHERE language_id = 1033</code></li><li>You can create a custom stoplist if you want to remove domain-specific words (like 'product', 'item') from your stopword list</li></ul>"
                        }
                    ],
                    "quiz": [
                        {
                            "q": "Which full-text search function returns a RANK score indicating relevance?",
                            "opts": ["A. CONTAINS", "B. FREETEXT", "C. FREETEXTTABLE", "D. FULLTEXTCATALOGPROPERTY"],
                            "correct": "C",
                            "explain": "FREETEXTTABLE (and CONTAINSTABLE) are table-valued functions that return {KEY, RANK} pairs. RANK is a relevance score from 0-1000. CONTAINS and FREETEXT are predicates that return TRUE/FALSE — they do not return a score."
                        },
                        {
                            "q": "What does WITH CHANGE_TRACKING AUTO do in a CREATE FULLTEXT INDEX statement?",
                            "opts": ["A. It rebuilds the full-text index every hour", "B. It automatically updates the full-text index when rows are inserted, updated, or deleted", "C. It tracks which users run full-text queries", "D. It enables automatic language detection"],
                            "correct": "B",
                            "explain": "CHANGE_TRACKING AUTO means SQL Server automatically propagates INSERT, UPDATE, and DELETE changes to the full-text index without manual intervention. This keeps search results current as data changes."
                        },
                        {
                            "q": "What is the correct CONTAINS syntax to find rows where Description contains BOTH 'wireless' AND 'keyboard'?",
                            "opts": ["A. CONTAINS(Description, 'wireless keyboard')", "B. CONTAINS(Description, '\"wireless\" AND \"keyboard\"')", "C. CONTAINS(Description, 'wireless' AND 'keyboard')", "D. CONTAINS(Description, 'wireless', 'keyboard')"],
                            "correct": "B",
                            "explain": "CONTAINS uses a search condition string with Boolean operators. Each term must be in double quotes within the string, and operators are in uppercase. The correct syntax is '\"wireless\" AND \"keyboard\"'."
                        },
                        {
                            "q": "A full-text search for 'running' also returns rows containing 'run' and 'ran'. What feature causes this?",
                            "opts": ["A. Wildcards", "B. Stopword removal", "C. Word stemming (inflectional forms)", "D. Language translation"],
                            "correct": "C",
                            "explain": "Word stemming reduces words to their root form during indexing and searching. 'running', 'run', and 'ran' all stem to 'run', so a search for 'running' finds all inflectional forms. This is a key advantage over LIKE."
                        },
                        {
                            "q": "Why must a table have a unique, non-nullable single-column index before you can create a Full-Text Index on it?",
                            "opts": ["A. For security reasons", "B. Because the full-text index uses this unique key column to link back to specific rows in the base table", "C. Because SQL Server requires indexes on all columns before enabling full-text", "D. To prevent duplicate text from being indexed"],
                            "correct": "B",
                            "explain": "The full-text index stores (word, KEY) pairs in its inverted index structure. KEY is the value from the unique index column (usually the primary key) that identifies which row contains that word. Without a unique key, there is no way to link back to specific rows."
                        }
                    ]
                },

                # ── Unit 4: Prepare for vector search ────────────────────
                {
                    "id": "lp3-m10-u4",
                    "title": "Prepare for vector search",
                    "description": "Learn how to set up your database and data for vector similarity search using embeddings.",
                    "estimated_time": 20,
                    "objectives": [
                        "Understand cosine distance vs cosine similarity",
                        "Learn the VECTOR_DISTANCE function syntax",
                        "Embed a user's search query using T-SQL",
                        "Understand why vector indexes (ANN) matter for performance"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "From Embeddings to Search",
                            "body": "In Module 9, you learned to generate and store embeddings. Now you will use them for search.\n\nThe fundamental idea of vector search is:\n<ol><li>User types a search query: <em>'fast laptop for gaming'</em></li><li>You call the embedding API to convert that query to a vector (the same model used to embed your data)</li><li>You compare the query vector to all stored vectors using a distance function</li><li>You return the rows with the smallest distance (= most similar meaning)</li></ol>\n\n<strong>Important: Use the same model for query and data embeddings!</strong><br>If you embedded your products with text-embedding-ada-002, you must also embed the search query with text-embedding-ada-002. Mixing models produces garbage results because different models use different 'languages' of vectors.\n\n<strong>VECTOR_DISTANCE function:</strong><br><code>VECTOR_DISTANCE('cosine', vector1, vector2)</code><br>Returns a value from 0 to 2 where:\n<ul><li>0 = identical (same direction)</li><li>1 = unrelated (perpendicular)</li><li>2 = opposite meaning</li></ul>\nSmaller distance = more similar. This is the inverse of cosine similarity."
                        },
                        {
                            "type": "sql_block",
                            "title": "Embed a User Search Query in T-SQL",
                            "scenario": "A user searches for 'wireless keyboard for office'. Embed this query using the same model used for your product data.",
                            "code": """-- Step 1: Embed the user's search query
DECLARE @UserQuery   NVARCHAR(MAX) = 'wireless keyboard for office';
DECLARE @Payload     NVARCHAR(MAX);
DECLARE @Response    NVARCHAR(MAX);
DECLARE @StatusCode  INT;
DECLARE @QueryVector VECTOR(1536);   -- Will hold the query embedding

-- Build the API payload
SET @Payload = N'{"input": ' + (SELECT @UserQuery FOR JSON PATH, WITHOUT_ARRAY_WRAPPER) + '}';

-- Call Azure OpenAI to embed the query
EXEC sp_invoke_external_rest_endpoint
    @url        = 'https://YOUR-RESOURCE.openai.azure.com/openai/deployments/text-embedding-ada-002/embeddings?api-version=2023-05-15',
    @method     = 'POST',
    @headers    = N'{"Content-Type": "application/json", "api-key": "YOUR-API-KEY"}',
    @payload    = @Payload,
    @response   = @Response OUTPUT,
    @statuscode = @StatusCode OUTPUT;

-- Convert JSON array to VECTOR type
IF @StatusCode = 200
    SET @QueryVector = CAST(JSON_QUERY(@Response, '$.result.data[0].embedding') AS VECTOR(1536));
ELSE
    RAISERROR('Failed to embed query: HTTP %d', 16, 1, @StatusCode);

-- Step 2: Find the 10 most similar products
SELECT TOP 10
    ProductID,
    ProductName,
    Description,
    VECTOR_DISTANCE('cosine', DescriptionEmbedding, @QueryVector) AS cosine_distance
FROM ProductCatalog
WHERE DescriptionEmbedding IS NOT NULL
ORDER BY cosine_distance ASC;    -- ASC = smallest distance first = most similar""",
                            "explanation": "This two-step query first embeds the user's search query (same model as the stored data), then uses VECTOR_DISTANCE to find the 10 products whose embeddings are closest to the query embedding. ORDER BY cosine_distance ASC means most similar first.",
                            "purpose": "Implement a complete vector search query from user input to ranked results.",
                            "breakdown": [
                                {"line": "DECLARE @QueryVector VECTOR(1536)", "meaning": "Variable to hold the embedding of the user's search query. Must be VECTOR(1536) to match the stored product embeddings."},
                                {"line": "SET @QueryVector = CAST(JSON_QUERY(...) AS VECTOR(1536))", "meaning": "Converts the JSON array from the API response into the VECTOR type. This is the same pattern used when storing product embeddings in Module 9."},
                                {"line": "VECTOR_DISTANCE('cosine', DescriptionEmbedding, @QueryVector)", "meaning": "Computes the cosine distance between each product's stored embedding and the query embedding. 'cosine' is the distance metric. Range is 0 (identical) to 2 (opposite)."},
                                {"line": "WHERE DescriptionEmbedding IS NOT NULL", "meaning": "Skips rows that do not have an embedding yet. Including NULL-embedding rows would cause errors in VECTOR_DISTANCE."},
                                {"line": "ORDER BY cosine_distance ASC", "meaning": "ASC (ascending) order puts the smallest distance first — these are the most similar products. This is the correct sort order for distance-based search."}
                            ],
                            "ssms_steps": [
                                "Open SSMS and connect to your Azure SQL Database",
                                "Open a New Query window",
                                "Paste the complete two-step code above",
                                "Change @UserQuery to match something your product data covers",
                                "Replace YOUR-RESOURCE and YOUR-API-KEY with real values",
                                "Press F5 to run both steps",
                                "Review the results — the top rows should be the most semantically similar products",
                                "Check the cosine_distance column: values below 0.3 are very similar, above 0.7 are barely related"
                            ],
                            "exam_tip": "VECTOR_DISTANCE returns a DISTANCE (0=same, 2=opposite), not a similarity (1=same, -1=opposite). Always use ORDER BY distance ASC to get most-similar results first. This feature requires Azure SQL Database or SQL Server 2025."
                        },
                        {
                            "type": "important",
                            "title": "Approximate Nearest Neighbor (ANN) Search",
                            "body": "The query above performs an <strong>exact nearest neighbor search</strong> — it computes VECTOR_DISTANCE for every row in the table. For small tables (&lt;100K rows), this is fine.\n\nFor large tables (millions of rows), an exact scan becomes slow. <strong>Approximate Nearest Neighbor (ANN) indexes</strong> can speed this up by quickly narrowing down candidates — trading a tiny amount of accuracy for large speed gains.\n\nAzure SQL Database has vector index support in preview (check current Microsoft documentation for the exact CREATE INDEX syntax as it evolves). The key concept for the exam: ANN indexes enable scalable vector search at the cost of approximation."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What does VECTOR_DISTANCE('cosine', v1, v2) return when v1 and v2 are identical vectors?",
                            "opts": ["A. 1.0", "B. 0.0", "C. -1.0", "D. 1000"],
                            "correct": "B",
                            "explain": "VECTOR_DISTANCE returns cosine distance, not cosine similarity. Identical vectors have zero angle between them → cosine = 1.0 → distance = 1 - 1.0 = 0.0. A distance of 0 means perfect similarity."
                        },
                        {
                            "q": "Why must you use the same embedding model to embed search queries as you used to embed your stored data?",
                            "opts": ["A. Because Azure OpenAI only has one model", "B. Because different models produce vectors in different dimensional spaces that are not comparable", "C. Because SQL Server requires model consistency for VECTOR columns", "D. Because using different models violates the Azure terms of service"],
                            "correct": "B",
                            "explain": "Each embedding model maps text to its own unique vector space. Comparing vectors from different models is meaningless — like comparing GPS coordinates from different mapping systems. You must use the same model for both data and queries."
                        },
                        {
                            "q": "In a vector search result sorted by cosine distance ASC, what does the first row represent?",
                            "opts": ["A. The row with the most keywords matching the query", "B. The row with the highest price", "C. The row whose embedding vector is closest (most similar) to the query vector", "D. The most recently inserted row"],
                            "correct": "C",
                            "explain": "Sorting by cosine distance ASC puts the smallest distance first. The smallest distance means the greatest semantic similarity. The first row is the most semantically similar document to the search query."
                        },
                        {
                            "q": "What is the WHERE DescriptionEmbedding IS NOT NULL condition for in a vector search query?",
                            "opts": ["A. To speed up the query with index filtering", "B. To exclude rows that haven't had their embedding generated yet, preventing VECTOR_DISTANCE errors", "C. To filter out products with no description", "D. Because VECTOR_DISTANCE only works on non-NULL values"],
                            "correct": "B",
                            "explain": "Passing NULL to VECTOR_DISTANCE would cause an error. Rows where embeddings have not been generated yet (NULL) must be excluded from vector search. This also reflects a data quality consideration — incomplete rows should not appear in search results."
                        },
                        {
                            "q": "What trade-off does Approximate Nearest Neighbor (ANN) search make compared to exact nearest neighbor search?",
                            "opts": ["A. ANN returns more accurate results but is slower", "B. ANN is faster but may miss some of the true closest results (trades accuracy for speed)", "C. ANN requires no index but uses more CPU", "D. ANN only works with 128-dimensional vectors"],
                            "correct": "B",
                            "explain": "ANN indexes narrow down candidates quickly without comparing every row, dramatically improving speed for large datasets. The trade-off is that it might miss 1-5% of the true closest results. For search use cases, this approximation is usually acceptable."
                        }
                    ]
                },

                # ── Unit 5: Vector search patterns ───────────────────────
                {
                    "id": "lp3-m10-u5",
                    "title": "Vector search patterns",
                    "description": "Learn common patterns for vector search: top-N results, filtered search, and similarity thresholds.",
                    "estimated_time": 25,
                    "objectives": [
                        "Implement top-N nearest neighbor search",
                        "Add metadata filters to vector search",
                        "Apply a similarity threshold to filter weak results",
                        "Cache query embeddings to reduce API costs"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Common Vector Search Patterns",
                            "body": "Real-world vector search scenarios require more than a simple ORDER BY query. Here are the most common patterns you need to know:\n\n<strong>Pattern 1: Top-N Search</strong><br>Return the N most similar results. Use TOP(N) or FETCH FIRST N ROWS ONLY.\n\n<strong>Pattern 2: Filtered Vector Search</strong><br>Combine vector similarity with traditional SQL WHERE filters. Example: find the 5 most similar products in a specific category. Also called 'pre-filtering' (filter then search) or 'post-filtering' (search then filter).\n\n<strong>Pattern 3: Similarity Threshold</strong><br>Only return results above a minimum similarity level. Avoids returning irrelevant results when there are no good matches. Filter with WHERE VECTOR_DISTANCE(...) &lt; 0.5 (only results with distance below 0.5 = high similarity).\n\n<strong>Pattern 4: Diverse Result Sets</strong><br>Sometimes the top 10 nearest neighbors are all very similar to each other (e.g., 10 nearly identical products). Advanced patterns like Maximum Marginal Relevance (MMR) diversify results — beyond exam scope but worth knowing."
                        },
                        {
                            "type": "sql_block",
                            "title": "Pattern 1 and 2 — Top-N with Metadata Filter",
                            "scenario": "Find the 5 most similar laptop products to a user's search query, restricting results to the 'Computers' category.",
                            "code": """-- Pattern: Top-N vector search with metadata pre-filtering
-- This finds the 5 most similar products IN THE 'Computers' CATEGORY

DECLARE @QueryVector VECTOR(1536);   -- Assume already populated (see Unit 4)

-- Pre-filtering: narrow to a category first, then rank by similarity
SELECT TOP 5
    ProductID,
    ProductName,
    Category,
    Price,
    VECTOR_DISTANCE('cosine', DescriptionEmbedding, @QueryVector) AS similarity_distance
FROM ProductCatalog
WHERE
    Category = 'Computers'                   -- Pre-filter: only this category
    AND DescriptionEmbedding IS NOT NULL     -- Only rows with embeddings
ORDER BY similarity_distance ASC;            -- Most similar first

-- Pattern: Top-N with similarity THRESHOLD
-- Only return results where cosine distance < 0.5 (fairly similar)
SELECT TOP 10
    ProductID,
    ProductName,
    VECTOR_DISTANCE('cosine', DescriptionEmbedding, @QueryVector) AS similarity_distance
FROM ProductCatalog
WHERE
    DescriptionEmbedding IS NOT NULL
    AND VECTOR_DISTANCE('cosine', DescriptionEmbedding, @QueryVector) < 0.5
ORDER BY similarity_distance ASC;

-- Pattern: No results above threshold? Return a message
-- Use this to detect 'no good match found'
DECLARE @MinSimilarityDistance FLOAT = 0.5;
DECLARE @ResultCount INT;

SELECT @ResultCount = COUNT(*)
FROM ProductCatalog
WHERE DescriptionEmbedding IS NOT NULL
  AND VECTOR_DISTANCE('cosine', DescriptionEmbedding, @QueryVector) < @MinSimilarityDistance;

IF @ResultCount = 0
    SELECT 'No similar products found. Try broadening your search.' AS message;
ELSE
    SELECT TOP 5
        ProductID,
        ProductName,
        VECTOR_DISTANCE('cosine', DescriptionEmbedding, @QueryVector) AS similarity_distance
    FROM ProductCatalog
    WHERE DescriptionEmbedding IS NOT NULL
      AND VECTOR_DISTANCE('cosine', DescriptionEmbedding, @QueryVector) < @MinSimilarityDistance
    ORDER BY similarity_distance ASC;""",
                            "explanation": "These patterns show how to combine vector search with regular SQL filtering. Pre-filtering with WHERE Category = 'Computers' reduces the number of distance calculations needed. The threshold pattern prevents returning irrelevant results when there are no good matches.",
                            "purpose": "Implement production-ready vector search patterns that combine semantic similarity with business logic filters.",
                            "breakdown": [
                                {"line": "WHERE Category = 'Computers' AND DescriptionEmbedding IS NOT NULL", "meaning": "Pre-filtering: only compute VECTOR_DISTANCE for rows in the 'Computers' category. This reduces computation — you only calculate similarity for the subset of rows that pass the filter."},
                                {"line": "AND VECTOR_DISTANCE('cosine', ...) < 0.5", "meaning": "Applies a similarity threshold: only return rows with cosine distance below 0.5. A distance of 0.5 means moderate similarity; below 0.3 is high similarity. Adjust the threshold based on your testing."},
                                {"line": "DECLARE @MinSimilarityDistance FLOAT = 0.5", "meaning": "Making the threshold a variable makes it easy to adjust for different use cases without changing the SQL logic. You can even store this as a configuration setting."}
                            ],
                            "ssms_steps": [
                                "Open SSMS with a New Query window",
                                "First run the query from Unit 4 to populate @QueryVector",
                                "Then paste the Pattern 1 query and press F5",
                                "Observe that results are limited to the 'Computers' category",
                                "Try changing the category to see different result sets",
                                "Run the threshold query and adjust the 0.5 value up or down to see how it affects results",
                                "Try 0.3 for strict filtering and 0.7 for permissive filtering"
                            ],
                            "exam_tip": "Pre-filtering (WHERE Category = 'Computers') before vector distance calculation is more efficient than post-filtering. However, pre-filtering may miss relevant results in adjacent categories. For the exam, know both approaches and their tradeoffs."
                        },
                        {
                            "type": "tip",
                            "title": "Cache Query Embeddings to Reduce Costs",
                            "body": "Each call to the Azure OpenAI embedding API costs money. If many users search for the same terms, cache the query embeddings:\n\n<code>CREATE TABLE SearchQueryCache (QueryText NVARCHAR(500) PRIMARY KEY, QueryEmbedding VECTOR(1536), CachedAt DATETIME2 DEFAULT GETUTCDATE());</code>\n\nBefore calling the API, check if the query is already cached:\n<code>SELECT @QueryVector = QueryEmbedding FROM SearchQueryCache WHERE QueryText = @UserQuery AND CachedAt > DATEADD(HOUR, -24, GETUTCDATE());</code>\n\nOnly call the API if the cache miss. This can reduce embedding costs by 80-90% for popular search terms."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "A vector search returns 10 results but 8 of them have a cosine distance of 0.85 — far from the query. What should you do?",
                            "opts": ["A. Return all 10 results to the user", "B. Apply a similarity threshold (e.g., WHERE VECTOR_DISTANCE < 0.5) to filter out weakly similar results", "C. Increase the TOP value to return more results", "D. Switch to LIKE search instead"],
                            "correct": "B",
                            "explain": "A cosine distance of 0.85 indicates very low similarity. Showing these results to users as 'similar products' would be misleading. A threshold filter (e.g., WHERE distance < 0.5) ensures only meaningfully similar results are returned."
                        },
                        {
                            "q": "What is 'pre-filtering' in the context of vector search?",
                            "opts": ["A. Filtering results after computing all vector distances", "B. Applying SQL WHERE conditions before computing vector distances to reduce the number of comparisons", "C. Pre-processing the query text before embedding", "D. Filtering out stopwords from the search query"],
                            "correct": "B",
                            "explain": "Pre-filtering applies regular SQL WHERE conditions (like Category = 'Computers') before VECTOR_DISTANCE calculations. This reduces the number of expensive distance computations and can significantly improve performance."
                        },
                        {
                            "q": "What cosine distance value indicates very high similarity between two vectors?",
                            "opts": ["A. Close to 2.0", "B. Close to 1.0", "C. Close to 0.0", "D. Close to -1.0"],
                            "correct": "C",
                            "explain": "VECTOR_DISTANCE with 'cosine' returns cosine distance, where 0 = identical, 1 = unrelated, 2 = opposite. Very high similarity = very small distance = value close to 0.0."
                        },
                        {
                            "q": "Why would you cache query embeddings in a SearchQueryCache table?",
                            "opts": ["A. Because VECTOR columns cannot store query vectors", "B. To avoid repeated expensive Azure OpenAI API calls for the same or similar search queries", "C. Because the VECTOR_DISTANCE function requires pre-cached vectors", "D. To meet GDPR requirements"],
                            "correct": "B",
                            "explain": "Each Azure OpenAI embedding API call has a cost. For popular search queries that many users type, caching the embedding means paying for the API call only once. Subsequent searches using the same query text reuse the cached embedding."
                        },
                        {
                            "q": "You search for 'laptop' and get 0 results with WHERE VECTOR_DISTANCE < 0.3. What is the most likely cause and solution?",
                            "opts": ["A. The API is down — retry later", "B. The threshold (0.3) may be too strict. Try relaxing it to 0.5 or 0.7", "C. The VECTOR column is broken and needs to be rebuilt", "D. Text-embedding-ada-002 does not understand the word 'laptop'"],
                            "correct": "B",
                            "explain": "A threshold of 0.3 is quite strict — it only returns results with very high similarity. If no products match at this level, the threshold may be too restrictive for your data. Try 0.5 (moderate similarity) or 0.7 (any similarity) to return more results."
                        }
                    ]
                },

                # ── Unit 6: Hybrid search and ranking ────────────────────
                {
                    "id": "lp3-m10-u6",
                    "title": "Hybrid search and ranking",
                    "description": "Combine full-text and vector search using Reciprocal Rank Fusion for the best search quality.",
                    "estimated_time": 30,
                    "objectives": [
                        "Understand why hybrid search outperforms either approach alone",
                        "Implement Reciprocal Rank Fusion (RRF) to combine scores",
                        "Build a hybrid search stored procedure",
                        "Tune the balance between FTS and vector results"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Why Hybrid Search?",
                            "body": "<strong>The problem with each approach alone:</strong>\n\n<strong>Full-text search fails when:</strong> The user uses different words than the document. Search for 'laptop' but the product says 'notebook computer' → no FTS match.\n\n<strong>Vector search fails when:</strong> The user searches for a specific code or exact term. Search for 'SKU-AB-4471' → vector search might return any product with a numeric code because they all have similar embeddings.\n\n<strong>Hybrid search combines both:</strong>\n<ul><li>FTS handles exact keyword matches, product codes, and technical terms</li><li>Vector search handles natural language, synonyms, and conceptual queries</li><li>The combined ranking promotes results that score well on BOTH — reducing the chance of bad results</li></ul>\n\n<strong>Reciprocal Rank Fusion (RRF):</strong><br>The most common algorithm for combining rankings from multiple sources. The formula for each document is:\n<br><code>RRF_score = Σ 1 / (k + rank_i)</code>\n<br>Where k is a constant (typically 60) and rank_i is the document's rank in each result list.\n\nThe key insight: a document that ranks #1 in both FTS and vector search gets a very high RRF score. A document that ranks #2 in vector search but appears nowhere in FTS still gets a decent score."
                        },
                        {
                            "type": "sql_block",
                            "title": "Implementing Hybrid Search with RRF",
                            "scenario": "Implement a hybrid search that combines FREETEXTTABLE scores and vector distance ranks, then uses RRF to produce a unified ranking.",
                            "code": """-- Hybrid Search using Reciprocal Rank Fusion (RRF)
-- Assumes @QueryVector is already populated (from embedding the user query)

DECLARE @UserQuery   NVARCHAR(500) = 'wireless keyboard for office work';
DECLARE @QueryVector VECTOR(1536);   -- Populate this from Azure OpenAI (see Unit 4)
DECLARE @K           INT = 60;       -- RRF constant (60 is the standard value)
DECLARE @TopN        INT = 20;       -- Retrieve top 20 from each source before merging

-- Step 1: Get Full-Text Search results with ranks
;WITH FTS_Results AS (
    SELECT
        p.ProductID,
        fts.RANK                                       AS fts_raw_rank,
        ROW_NUMBER() OVER (ORDER BY fts.RANK DESC)    AS fts_position  -- 1 = best FTS result
    FROM ProductCatalog p
    INNER JOIN FREETEXTTABLE(ProductCatalog, Description, @UserQuery) fts
        ON p.ProductID = fts.[KEY]
    WHERE p.DescriptionEmbedding IS NOT NULL
),

-- Step 2: Get Vector Search results with ranks
Vector_Results AS (
    SELECT TOP (@TopN)
        ProductID,
        VECTOR_DISTANCE('cosine', DescriptionEmbedding, @QueryVector) AS vector_distance,
        ROW_NUMBER() OVER (ORDER BY VECTOR_DISTANCE('cosine', DescriptionEmbedding, @QueryVector) ASC) AS vector_position
    FROM ProductCatalog
    WHERE DescriptionEmbedding IS NOT NULL
    ORDER BY vector_distance ASC
),

-- Step 3: Compute RRF score for each document
RRF_Scores AS (
    SELECT
        COALESCE(f.ProductID, v.ProductID) AS ProductID,
        COALESCE(1.0 / (@K + f.fts_position),    0) AS fts_rrf_score,
        COALESCE(1.0 / (@K + v.vector_position), 0) AS vec_rrf_score,
        COALESCE(1.0 / (@K + f.fts_position), 0) +
        COALESCE(1.0 / (@K + v.vector_position), 0) AS total_rrf_score
    FROM FTS_Results f
    FULL OUTER JOIN Vector_Results v ON f.ProductID = v.ProductID
)

-- Step 4: Return final ranked results
SELECT TOP 10
    r.ProductID,
    p.ProductName,
    p.Description,
    p.Category,
    r.fts_rrf_score,
    r.vec_rrf_score,
    r.total_rrf_score
FROM RRF_Scores r
JOIN ProductCatalog p ON r.ProductID = p.ProductID
ORDER BY r.total_rrf_score DESC;""",
                            "explanation": "This query runs both FTS and vector search in parallel (using CTEs), converts each result's rank to an RRF score, and combines them with a FULL OUTER JOIN. Results that score well on both approaches bubble to the top.",
                            "purpose": "Implement production-quality hybrid search that combines keyword and semantic search using the Reciprocal Rank Fusion algorithm.",
                            "breakdown": [
                                {"line": "WITH FTS_Results AS (...)", "meaning": "A CTE (Common Table Expression) that gets full-text search results. ROW_NUMBER() OVER (ORDER BY fts.RANK DESC) assigns position 1 to the best FTS result."},
                                {"line": "Vector_Results AS (...)", "meaning": "A CTE that gets vector search results ordered by cosine distance ASC (most similar first). ROW_NUMBER() assigns position 1 to the closest vector."},
                                {"line": "COALESCE(1.0 / (@K + f.fts_position), 0)", "meaning": "Computes the RRF contribution from FTS. COALESCE handles cases where a product appears in vector results but NOT in FTS results — those get an FTS RRF score of 0."},
                                {"line": "FULL OUTER JOIN Vector_Results v ON f.ProductID = v.ProductID", "meaning": "FULL OUTER JOIN keeps all rows from both FTS and vector results, even if a product only appears in one of them. Products in both get contributions from both sources."},
                                {"line": "ORDER BY r.total_rrf_score DESC", "meaning": "The highest total RRF score is the combined best rank. Products that appear near the top in BOTH FTS and vector search will have the highest total scores."},
                                {"line": "@K INT = 60", "meaning": "The RRF constant k=60 is the industry standard. Increasing k makes ranks matter less (smoother distribution); decreasing k makes the top ranks dominate more strongly."}
                            ],
                            "ssms_steps": [
                                "Ensure you have both a Full-Text Index (from Unit 3) and embeddings (from Module 9) on your ProductCatalog table",
                                "Open SSMS with a New Query window",
                                "First, populate @QueryVector by running the embedding call from Unit 4",
                                "Then paste the hybrid search CTE query above",
                                "Press F5 to run",
                                "Review the fts_rrf_score, vec_rrf_score, and total_rrf_score columns",
                                "Products with non-zero scores in BOTH columns are those that appeared in both search types",
                                "Try changing @UserQuery to different search phrases and observe how rankings change"
                            ],
                            "exam_tip": "Reciprocal Rank Fusion (RRF) is the standard algorithm for combining multiple ranked lists. The formula is: score = Σ 1/(k + rank_i) for each source. k=60 is the conventional default. FULL OUTER JOIN is used so that results appearing in only one source are still included."
                        },
                        {
                            "type": "important",
                            "title": "RRF vs Score Normalization",
                            "body": "You might wonder: why not just add the FTS RANK (0-1000) and vector distance (0-2) together? The problem is they are on completely different scales.\n\n<strong>Score normalization</strong> is another approach: convert each score to a 0-1 range before adding.\n<code>normalized_fts = fts_rank / 1000.0</code>\n<code>normalized_vec = 1 - (vector_distance / 2.0)</code>  ← converts distance to similarity\n\n<strong>RRF advantages over normalization:</strong>\n<ul><li>Not affected by extreme outliers (one score of 999 does not dominate)</li><li>More robust — works even when score distributions change</li><li>Well-established in information retrieval research</li></ul>\n\nFor the DP-800 exam, know that RRF is the recommended approach for hybrid search ranking."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What is the Reciprocal Rank Fusion (RRF) formula for a single result list?",
                            "opts": ["A. rank / max_rank", "B. 1 / (k + position)", "C. similarity_score * fts_rank", "D. 1 - cosine_distance"],
                            "correct": "B",
                            "explain": "The RRF formula for a document's contribution from one result list is 1 / (k + position), where k is a constant (typically 60) and position is the document's rank in that list (1 = best). A document's total RRF score sums this across all result lists."
                        },
                        {
                            "q": "Why is a FULL OUTER JOIN used when combining FTS and vector search results in hybrid search?",
                            "opts": ["A. FULL OUTER JOIN is required for CTE queries", "B. To keep results that appear in only one of the two search methods (FTS or vector)", "C. To avoid duplicate rows in the result", "D. Because INNER JOIN does not work with VECTOR columns"],
                            "correct": "B",
                            "explain": "FULL OUTER JOIN preserves all rows from both result sets, including products that appear only in FTS results or only in vector results. An INNER JOIN would discard these, losing potentially relevant results that scored highly in one method."
                        },
                        {
                            "q": "A product appears at position 1 in FTS results and position 3 in vector results (k=60). What is its total RRF score?",
                            "opts": ["A. 1/61 + 1/63 ≈ 0.0164 + 0.0159 ≈ 0.032", "B. 1 + 3 = 4", "C. (1000 + 1) / 2 = 500.5", "D. 0"],
                            "correct": "A",
                            "explain": "RRF score from FTS: 1/(60+1) = 1/61 ≈ 0.0164. RRF score from vector: 1/(60+3) = 1/63 ≈ 0.0159. Total = 0.0164 + 0.0159 ≈ 0.032. The product scores well because it ranks near the top in both methods."
                        },
                        {
                            "q": "Why is score normalization less robust than RRF for combining FTS and vector search?",
                            "opts": ["A. Normalization is more expensive to compute", "B. One extreme outlier score can dominate the normalized sum, while RRF uses rank position which is not affected by score magnitude", "C. SQL Server does not support mathematical normalization", "D. Normalization requires a machine learning model"],
                            "correct": "B",
                            "explain": "If one FTS result has a score of 999 while all others score around 10, normalizing and adding would let that single result dominate. RRF uses rank position (1st, 2nd, 3rd...) which is not affected by the absolute score value — making it more robust."
                        },
                        {
                            "q": "What is the standard value of the RRF constant k?",
                            "opts": ["A. 10", "B. 60", "C. 100", "D. 1000"],
                            "correct": "B",
                            "explain": "k=60 is the standard, well-established default value for Reciprocal Rank Fusion, originating from information retrieval research. It provides a good balance where top-ranked results matter significantly but the distribution is smooth enough not to overweight position 1."
                        }
                    ]
                },

                # ── Unit 7: Exercise ──────────────────────────────────────
                {
                    "id": "lp3-m10-u7",
                    "title": "Exercise",
                    "description": "Hands-on exercise: implement full-text, vector, and hybrid search on a job listings database.",
                    "estimated_time": 50,
                    "objectives": [
                        "Set up full-text search on a job listings table",
                        "Implement vector search for semantic job matching",
                        "Build a hybrid search query combining both approaches",
                        "Compare the three approaches on the same query"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Exercise: Job Listings Search Engine",
                            "body": "<strong>Scenario:</strong> You are building a job search feature. Job seekers type natural language queries like 'data analyst role with Python skills' and expect to see relevant listings.\n\n<strong>Exercise Structure:</strong>\n<ol><li><strong>Setup</strong> — Create a JobListings table with sample data</li><li><strong>Full-Text Search</strong> — Set up FTS and run keyword searches</li><li><strong>Vector Search</strong> — Embed job descriptions and run semantic search</li><li><strong>Hybrid Search</strong> — Combine both with RRF</li><li><strong>Comparison</strong> — Compare results from all three approaches</li></ol>\n\n<strong>Skills practiced:</strong> CREATE FULLTEXT CATALOG/INDEX, FREETEXTTABLE, sp_invoke_external_rest_endpoint, VECTOR_DISTANCE, CTEs, FULL OUTER JOIN, RRF formula."
                        },
                        {
                            "type": "sql_block",
                            "title": "Exercise Setup — Create Job Listings Table",
                            "scenario": "Create a JobListings table with 8 sample job postings and set up both full-text search and embedding columns.",
                            "code": """-- Exercise: Job Listings Search Engine

-- Step 1: Create the table
CREATE TABLE JobListings (
    JobID       INT           PRIMARY KEY IDENTITY(1,1),
    Title       NVARCHAR(200) NOT NULL,
    Description NVARCHAR(MAX) NOT NULL,
    Company     NVARCHAR(100),
    Location    NVARCHAR(100),
    Salary      INT,
    DescriptionEmbedding VECTOR(1536),
    EmbeddingUpdated     DATETIME2
);

-- Step 2: Insert sample job listings
INSERT INTO JobListings (Title, Description, Company, Location, Salary) VALUES
('Data Analyst',
 'Analyze business data using SQL and Excel. Create dashboards in Power BI. Work with stakeholders to define KPIs. Experience with Python preferred.',
 'Acme Corp', 'New York', 85000),

('Machine Learning Engineer',
 'Build and deploy machine learning models. Experience with Python, TensorFlow, and PyTorch required. Work with large datasets. MLOps experience a plus.',
 'TechStart', 'San Francisco', 140000),

('SQL Database Administrator',
 'Manage SQL Server databases. Performance tuning, backup and recovery, security administration. SSMS expertise required. Azure SQL experience preferred.',
 'Global Finance', 'Chicago', 95000),

('Data Engineer',
 'Build data pipelines using Apache Spark and Azure Data Factory. ETL development, data warehouse design. Python and SQL skills required.',
 'CloudCo', 'Seattle', 120000),

('Business Intelligence Developer',
 'Develop Power BI reports and dashboards. DAX and M query experience. Work with data warehouse team. SQL knowledge required.',
 'RetailPlus', 'Austin', 90000),

('AI Solutions Architect',
 'Design AI and machine learning solutions for enterprise clients. Azure OpenAI, Azure AI services. Vector databases and embeddings experience. Python expertise.',
 'Consulting Group', 'Remote', 160000),

('Data Scientist',
 'Statistical modeling and machine learning. Python, R, and SQL. A/B testing, experimentation design. Communication skills to present findings to executives.',
 'E-Commerce Inc', 'Boston', 130000),

('Azure Cloud Engineer',
 'Design and implement Azure infrastructure. ARM templates, Terraform. Azure SQL, Azure Storage, Azure Functions. DevOps and CI/CD experience.',
 'CloudOps', 'Denver', 110000);

-- Verify
SELECT JobID, Title, Company, Location, Salary FROM JobListings;

-- Step 3: Create Full-Text Search
CREATE FULLTEXT CATALOG JobFTSCatalog AS DEFAULT;
CREATE FULLTEXT INDEX ON JobListings(Title LANGUAGE 1033, Description LANGUAGE 1033)
KEY INDEX PK__JobListi__056690C2       -- Replace with YOUR primary key index name
ON JobFTSCatalog
WITH CHANGE_TRACKING AUTO;

PRINT 'Setup complete. 8 job listings created with FTS index.';""",
                            "explanation": "Creates the JobListings table with both a VECTOR column for semantic search and the setup for full-text search. The 8 sample jobs cover different roles in data and tech.",
                            "purpose": "Establish the base dataset for the search exercise.",
                            "breakdown": [
                                {"line": "DescriptionEmbedding VECTOR(1536)", "meaning": "Column to store the 1536-dimensional embedding for each job description. NULL until populated in Step 4."},
                                {"line": "CREATE FULLTEXT INDEX ON JobListings(Title LANGUAGE 1033, Description LANGUAGE 1033)", "meaning": "Indexes both the Title and Description columns for full-text search. LANGUAGE 1033 = English stemming and stopwords."}
                            ],
                            "ssms_steps": [
                                "Open SSMS and connect to your Azure SQL Database",
                                "New Query → paste the setup code",
                                "Before running, find your PK index name: SELECT name FROM sys.indexes WHERE object_id = OBJECT_ID('JobListings') AND is_primary_key = 1",
                                "Replace PK__JobListi__056690C2 with your actual PK index name",
                                "Press F5 to run the entire setup",
                                "Verify: SELECT COUNT(*) FROM JobListings should return 8"
                            ],
                            "exam_tip": "You must look up the actual primary key index name for your table — it is auto-generated and different in every database. Use sys.indexes to find it."
                        },
                        {
                            "type": "sql_block",
                            "title": "Exercise — Compare All Three Search Approaches",
                            "scenario": "A job seeker searches for 'data analysis with Python'. Run all three search types and compare results.",
                            "code": """-- Exercise: Compare Full-Text, Vector, and Hybrid Search
-- Query: 'data analysis with Python'

-- SEARCH 1: Full-Text Search
PRINT '=== FULL-TEXT SEARCH RESULTS ===';
SELECT TOP 5
    p.JobID,
    p.Title,
    fts.RANK AS fts_rank
FROM JobListings p
INNER JOIN FREETEXTTABLE(JobListings, Description, 'data analysis with Python') fts
    ON p.JobID = fts.[KEY]
ORDER BY fts.RANK DESC;

-- SEARCH 2: Vector Search
-- (Assumes @QueryVector is populated from Azure OpenAI)
-- DECLARE @QueryVector VECTOR(1536); -- populate from API

PRINT '=== VECTOR SEARCH RESULTS ===';
SELECT TOP 5
    JobID,
    Title,
    VECTOR_DISTANCE('cosine', DescriptionEmbedding, @QueryVector) AS vec_distance
FROM JobListings
WHERE DescriptionEmbedding IS NOT NULL
ORDER BY vec_distance ASC;

-- SEARCH 3: Hybrid Search (RRF)
PRINT '=== HYBRID SEARCH RESULTS (RRF) ===';
DECLARE @K INT = 60;

;WITH FTS_Ranked AS (
    SELECT p.JobID, ROW_NUMBER() OVER (ORDER BY fts.RANK DESC) AS pos
    FROM JobListings p
    INNER JOIN FREETEXTTABLE(JobListings, Description, 'data analysis with Python') fts
        ON p.JobID = fts.[KEY]
),
Vec_Ranked AS (
    SELECT JobID, ROW_NUMBER() OVER (ORDER BY VECTOR_DISTANCE('cosine', DescriptionEmbedding, @QueryVector) ASC) AS pos
    FROM JobListings
    WHERE DescriptionEmbedding IS NOT NULL
),
RRF AS (
    SELECT
        COALESCE(f.JobID, v.JobID) AS JobID,
        COALESCE(1.0/(@K + f.pos), 0) + COALESCE(1.0/(@K + v.pos), 0) AS rrf_score
    FROM FTS_Ranked f FULL OUTER JOIN Vec_Ranked v ON f.JobID = v.JobID
)
SELECT TOP 5
    r.JobID,
    j.Title,
    j.Company,
    r.rrf_score
FROM RRF r
JOIN JobListings j ON r.JobID = j.JobID
ORDER BY r.rrf_score DESC;""",
                            "explanation": "This exercise runs all three search types on the same query so you can compare their results. Each approach may return a different set of top results, demonstrating their different strengths.",
                            "purpose": "Understand the practical differences between the three search approaches through direct comparison.",
                            "breakdown": [
                                {"line": "FREETEXTTABLE(JobListings, Description, 'data analysis with Python')", "meaning": "Full-text search finds jobs where the description contains these words (with stemming). Will find 'analyzing' for 'analysis', 'Python' exactly."},
                                {"line": "VECTOR_DISTANCE('cosine', DescriptionEmbedding, @QueryVector)", "meaning": "Vector search finds jobs semantically similar to 'data analysis with Python' — may find 'data scientist' role even if it uses different keywords."},
                                {"line": "FULL OUTER JOIN Vec_Ranked v ON f.JobID = v.JobID", "meaning": "Combines both result lists. Jobs in both lists get contributions from both scores; jobs in only one list still appear with a partial score."}
                            ],
                            "ssms_steps": [
                                "First, generate embeddings for all JobListings using the batch cursor pattern from Module 9",
                                "Then, in a new query, embed the search query 'data analysis with Python' into @QueryVector",
                                "Paste the comparison queries and run each section",
                                "Compare which jobs appear in which search results",
                                "Observe: FTS may miss 'Machine Learning Engineer' (no 'analysis' in description), but vector search might find it because ML uses data analysis",
                                "The hybrid results should be the best overall ranking"
                            ],
                            "exam_tip": "The exam may show you scenarios where one search approach returns better results than another. Know that: FTS excels for exact terms, vector excels for conceptual queries, and hybrid typically outperforms both."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "In the exercise, a job seeker searches 'data analysis with Python'. Which search approach is most likely to find a 'Data Scientist' role that uses 'statistical analysis' instead of 'data analysis'?",
                            "opts": ["A. CONTAINS with exact term matching", "B. FREETEXTTABLE with keyword stemming", "C. Vector search based on semantic similarity", "D. LIKE '%data analysis%'"],
                            "correct": "C",
                            "explain": "Vector search compares meanings. 'Data analysis with Python' and 'statistical analysis' are conceptually similar in the context of data science roles. Their embeddings will be close in vector space, even though no exact keywords match."
                        },
                        {
                            "q": "In the hybrid search CTE, why is COALESCE used around the RRF score calculations?",
                            "opts": ["A. To improve performance", "B. To handle NULL values when a job appears in only one of the two result lists (FTS or vector)", "C. Because FULL OUTER JOIN returns NULLs for all columns", "D. To convert the score to an integer"],
                            "correct": "B",
                            "explain": "FULL OUTER JOIN returns NULL for the other table's columns when a row has no match. COALESCE(1.0/(@K + f.pos), 0) means: use the RRF score if the job appeared in FTS results, otherwise use 0. This prevents NULL arithmetic errors."
                        },
                        {
                            "q": "After setting up the full-text index in the exercise, a search for 'analyzing' returns jobs that contain 'analysis' and 'analyze'. Why?",
                            "opts": ["A. Full-text search uses wildcard pattern matching", "B. Word stemming reduces inflectional forms to the same root, so analyzing/analysis/analyze all match", "C. The LANGUAGE 1033 setting translates words", "D. SQL Server automatically adds synonyms"],
                            "correct": "B",
                            "explain": "Full-text search applies stemming based on the specified language. For English (LANGUAGE 1033), 'analyzing', 'analysis', and 'analyze' all stem to the same root, so searching for any one of them finds rows containing any form."
                        },
                        {
                            "q": "In the exercise comparison, the hybrid RRF search assigns a score to a job that appeared in vector search at position 2 but did NOT appear in FTS results at all. What is that job's RRF score (k=60)?",
                            "opts": ["A. 0 — jobs not in FTS get no score", "B. 1/(60+2) ≈ 0.0161", "C. 1/(60+1) + 1/(60+2) ≈ 0.032", "D. 1000/62 ≈ 16.1"],
                            "correct": "B",
                            "explain": "The job is not in FTS results, so its FTS RRF contribution = COALESCE(null, 0) = 0. Its vector contribution = 1/(60+2) = 1/62 ≈ 0.0161. Total RRF = 0 + 0.0161 ≈ 0.0161."
                        },
                        {
                            "q": "What is the purpose of the EmbeddingUpdated column in the JobListings table?",
                            "opts": ["A. It stores the creation date of the job listing", "B. It tracks when the embedding was last generated, helping identify stale embeddings that need refreshing", "C. It is required by the VECTOR data type", "D. It stores the Azure OpenAI API call timestamp for billing"],
                            "correct": "B",
                            "explain": "EmbeddingUpdated records when each embedding was last generated. You can compare it to the job listing's update date to find rows where the Description changed after the embedding was created — those embeddings are stale and need to be regenerated."
                        }
                    ]
                },

                # ── Unit 8: Knowledge Check ───────────────────────────────
                {
                    "id": "lp3-m10-u8",
                    "title": "Knowledge Check",
                    "description": "Review and test your understanding of intelligent search in SQL.",
                    "estimated_time": 15,
                    "objectives": [
                        "Review key concepts from Module 10",
                        "Test understanding of FTS, vector, and hybrid search"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Module 10 Key Concepts Review",
                            "body": "<strong>Full-Text Search Recap:</strong>\n<ul><li>Requires FULLTEXT CATALOG + FULLTEXT INDEX with KEY INDEX (your PK index)</li><li>CONTAINS(col, '\"term\"') — precise Boolean search</li><li>FREETEXT(col, 'phrase') — natural language search with stemming</li><li>CONTAINSTABLE / FREETEXTTABLE — return {KEY, RANK} for ordered results</li><li>Stopwords excluded; stemming applied based on LANGUAGE setting</li></ul>\n\n<strong>Vector Search Recap:</strong>\n<ul><li>VECTOR(n) column stores embeddings; requires Azure SQL / SQL Server 2025</li><li>VECTOR_DISTANCE('cosine', v1, v2) — returns 0 (same) to 2 (opposite)</li><li>Always ORDER BY distance ASC for most-similar first</li><li>Must embed query with same model used for data</li><li>Filter with WHERE distance &lt; threshold to avoid weak matches</li></ul>\n\n<strong>Hybrid Search Recap:</strong>\n<ul><li>Combines FTS and vector results using RRF algorithm</li><li>RRF score = Σ 1/(k + position) where k=60 by default</li><li>Use FULL OUTER JOIN to include results from either source</li><li>COALESCE handles NULL scores for documents in only one source</li></ul>"
                        }
                    ],
                    "quiz": [
                        {
                            "q": "A FREETEXTTABLE query returns 0 rows for 'affordable laptop'. The table has 1000 products with descriptions. What is the most likely cause?",
                            "opts": ["A. FREETEXTTABLE does not support multi-word phrases", "B. 'affordable' and 'laptop' may be in the stopword list, or the full-text index has not finished building", "C. The VECTOR column blocks full-text search", "D. FREETEXTTABLE requires a minimum of 5000 rows"],
                            "correct": "B",
                            "explain": "If the full-text index is still building (check with SELECT FULLTEXTCATALOGPROPERTY('CatalogName', 'PopulateStatus')), it may return no results. Also verify 'affordable' and 'laptop' are not in the stopword list with SELECT stopword FROM sys.fulltext_system_stopwords WHERE language_id = 1033."
                        },
                        {
                            "q": "What does the [KEY] column represent in a FREETEXTTABLE result set?",
                            "opts": ["A. A unique identifier for the search query", "B. The primary key value of the matching row in the base table", "C. The full-text catalog name", "D. The relevance rank converted to a string"],
                            "correct": "B",
                            "explain": "[KEY] in FREETEXTTABLE (and CONTAINSTABLE) results contains the value from the column specified as KEY INDEX in the full-text index — typically the table's primary key. You JOIN on this to retrieve full row data from the base table."
                        },
                        {
                            "q": "VECTOR_DISTANCE returns 1.8 for a result. What does this indicate?",
                            "opts": ["A. The documents are very similar — 1.8 is close to the maximum similarity of 2", "B. The documents are quite dissimilar — cosine distance of 1.8 is close to the maximum of 2 (opposite meaning)", "C. The API returned an error", "D. The result is outside the valid range for cosine distance"],
                            "correct": "B",
                            "explain": "Cosine distance ranges from 0 (identical) to 2 (opposite meaning). A value of 1.8 is very close to 2, meaning the two vectors point in nearly opposite directions — the documents have very different (or opposite) semantic content."
                        },
                        {
                            "q": "Which T-SQL operator is appropriate for combining full-text and vector search result sets in hybrid search?",
                            "opts": ["A. INNER JOIN — to only include documents that appear in both result sets", "B. FULL OUTER JOIN — to include documents from either result set even if they appear in only one", "C. CROSS JOIN — to combine all results", "D. LEFT JOIN — to prioritize FTS results"],
                            "correct": "B",
                            "explain": "FULL OUTER JOIN includes all rows from both result sets. A document that appears only in FTS (not in vector search) or only in vector search (not FTS) should still be included in hybrid results, just with a lower combined score."
                        },
                        {
                            "q": "You are building search for an e-commerce site. Products have codes like 'HDMI-CABLE-6FT' and users search by code AND by description like 'cable for monitor'. Which approach fits best?",
                            "opts": ["A. Vector search only", "B. Full-text search only", "C. Hybrid search — FTS for exact codes, vector for descriptive queries", "D. LIKE search only — it handles both"],
                            "correct": "C",
                            "explain": "Hybrid search is ideal here: FTS accurately matches exact product codes ('HDMI-CABLE-6FT'), while vector search handles descriptive natural language queries ('cable for monitor'). Neither approach alone handles both well."
                        }
                    ]
                },

                # ── Unit 9: Summary ───────────────────────────────────────
                {
                    "id": "lp3-m10-u9",
                    "title": "Summary",
                    "description": "Review what you learned in Module 10 about intelligent search in SQL.",
                    "estimated_time": 5,
                    "objectives": [
                        "Consolidate knowledge of search approaches",
                        "Review the key T-SQL patterns for each search type"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Module 10 Summary",
                            "body": "In this module you learned three approaches to intelligent search in SQL:\n\n<strong>Full-Text Search (FTS)</strong>\n<ul><li>Built into SQL Server — no external services needed</li><li>Setup: CREATE FULLTEXT CATALOG + CREATE FULLTEXT INDEX</li><li>Query predicates: CONTAINS (precise), FREETEXT (natural language)</li><li>Ranked results: CONTAINSTABLE, FREETEXTTABLE return {KEY, RANK}</li><li>Features: stemming, stopwords, Boolean operators, prefix search (*)</li></ul>\n\n<strong>Vector Search</strong>\n<ul><li>Requires embeddings stored in VECTOR(n) columns</li><li>Query: embed the user's query with the same model, then ORDER BY VECTOR_DISTANCE ASC</li><li>Filter weak results with WHERE VECTOR_DISTANCE &lt; threshold</li><li>Best for natural language queries, synonyms, cross-lingual search</li><li>Requires Azure SQL Database or SQL Server 2025</li></ul>\n\n<strong>Hybrid Search with RRF</strong>\n<ul><li>Runs both FTS and vector search and merges results with RRF</li><li>RRF formula: 1/(k + position), k=60 standard</li><li>FULL OUTER JOIN combines both result lists</li><li>Highest quality search — handles both keywords and semantic queries</li></ul>\n\n<strong>Next:</strong> Module 11 builds on these search techniques to implement RAG (Retrieval-Augmented Generation) — using SQL to retrieve relevant context and feed it to an LLM to generate intelligent answers."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What are the two objects required to enable full-text search on a SQL Server table?",
                            "opts": ["A. Full-Text Catalog and Full-Text Index", "B. Full-Text Index and Full-Text View", "C. B-Tree Index and Full-Text Index", "D. Full-Text Catalog and External Data Source"],
                            "correct": "A",
                            "explain": "Full-Text Search requires: (1) a FULLTEXT CATALOG as the container/storage location for the full-text index, and (2) a FULLTEXT INDEX on the specific table and column(s) you want to search."
                        },
                        {
                            "q": "What is the key difference between CONTAINS and FREETEXT?",
                            "opts": ["A. CONTAINS is faster; FREETEXT is slower", "B. CONTAINS supports Boolean operators and exact control; FREETEXT automatically breaks phrases into words for natural language search", "C. FREETEXT only works on VARCHAR columns", "D. CONTAINS requires an external API call"],
                            "correct": "B",
                            "explain": "CONTAINS gives precise control with Boolean operators (AND, OR, NOT, NEAR, prefix *). FREETEXT is simpler — it automatically tokenizes and stems your phrase for natural language search but does not support operators."
                        },
                        {
                            "q": "In which direction should you sort by VECTOR_DISTANCE to get the most similar results first?",
                            "opts": ["A. DESC — highest distance first", "B. ASC — lowest distance first (0 = identical, so smallest = most similar)", "C. No sorting needed — VECTOR_DISTANCE returns results pre-sorted", "D. Random order — cosine distance has no meaningful sort direction"],
                            "correct": "B",
                            "explain": "VECTOR_DISTANCE returns a distance value where 0 = identical (most similar). Sorting ASC (ascending) puts the smallest distance values first — giving you the most similar results at the top."
                        },
                        {
                            "q": "What happens to a document's RRF score if it appears in vector search at position 5 but does NOT appear in FTS results at all (k=60)?",
                            "opts": ["A. Score = 0 because it is not in both result lists", "B. Score = 1/(60+5) = 1/65 ≈ 0.0154 (contribution from vector only, FTS contribution = 0)", "C. Score = 1/(60+5) + 1/(60+1) ≈ 0.031 (position 1 in FTS by default)", "D. The document is excluded from hybrid results"],
                            "correct": "B",
                            "explain": "RRF uses COALESCE to give a 0 score for missing results rather than excluding them. FTS contribution = COALESCE(null, 0) = 0. Vector contribution = 1/(60+5) = 1/65 ≈ 0.0154. Total = 0.0154. The document appears in hybrid results, just with a lower combined score."
                        },
                        {
                            "q": "After completing Module 10, which module should you study to learn how to use these search results to power AI-generated answers?",
                            "opts": ["A. Module 9 — revisit embeddings", "B. Module 11 — RAG (Retrieval-Augmented Generation) with SQL", "C. Module 1 — start over with basics", "D. A separate Azure OpenAI course"],
                            "correct": "B",
                            "explain": "Module 11 covers RAG (Retrieval-Augmented Generation) — the pattern of using SQL search (including the vector and hybrid search from Module 10) to retrieve context, then feeding that context to an LLM to generate grounded, accurate AI responses."
                        }
                    ]
                }
            ]
        },

        # ══════════════════════════════════════════════════════
        # MODULE 11 — Design and implement RAG with SQL
        # ══════════════════════════════════════════════════════
        {
            "id": "lp3-m11",
            "title": "Design and implement RAG with SQL",
            "description": "Learn to build Retrieval-Augmented Generation (RAG) solutions using SQL as the retrieval layer, feeding relevant database context into Azure OpenAI chat models to generate accurate, grounded AI responses.",
            "units": [

                # ── Unit 1: Introduction ──────────────────────────────────
                {
                    "id": "lp3-m11-u1",
                    "title": "Introduction",
                    "description": "Overview of RAG architecture and why it matters for enterprise AI solutions.",
                    "estimated_time": 5,
                    "objectives": [
                        "Understand what RAG (Retrieval-Augmented Generation) is",
                        "Know why LLMs need RAG for real-world enterprise use",
                        "Preview the module content and what you will build"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "What Is RAG and Why Does It Matter?",
                            "body": "<strong>The Problem with LLMs Alone</strong><br>Large Language Models (LLMs) like GPT-4 are trained on vast amounts of public internet text up to a certain date — their 'training cutoff'. They have no knowledge of:\n<ul><li>Your company's internal documents and data</li><li>Events after their training cutoff (typically 2021-2023)</li><li>Specific product catalogs, policies, or customer data</li></ul>\n\nIf you ask GPT-4 'What are our company's refund policies?', it cannot answer accurately — it doesn't know your policies.\n\n<strong>The RAG Solution</strong><br>RAG (Retrieval-Augmented Generation) solves this by:\n<ol><li><strong>Retrieve</strong> — Use SQL search to find relevant information from your database</li><li><strong>Augment</strong> — Add that information to the prompt as context</li><li><strong>Generate</strong> — Let the LLM answer the question using the provided context</li></ol>\n\nThe result: an LLM that answers questions accurately based on YOUR data, not just its training data.\n\n<strong>Why SQL for RAG?</strong><br>Most enterprise data lives in relational databases. Using SQL as the retrieval layer means RAG works with data you already have — product catalogs, knowledge bases, documents, support tickets — without migrating to a specialized vector database."
                        },
                        {
                            "type": "theory",
                            "title": "What You Will Learn in This Module",
                            "body": "<ul><li>RAG use cases and when to apply it</li><li>How to prepare SQL data for retrieval (chunking long documents)</li><li>How to retrieve relevant context using the search techniques from Module 10</li><li>How to augment LLM prompts with retrieved SQL data</li><li>How to call Azure OpenAI chat completion from T-SQL and parse the response</li><li>How to handle conversation history for multi-turn Q&amp;A</li></ul>\n\nBy the end, you will be able to build a complete RAG pipeline that answers questions using data from a SQL database."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What is the 'training cutoff' problem with LLMs that RAG solves?",
                            "opts": ["A. LLMs run too slowly without RAG", "B. LLMs have no knowledge of your private data or events after their training date", "C. LLMs cannot understand SQL queries", "D. LLMs are too expensive without RAG to reduce costs"],
                            "correct": "B",
                            "explain": "LLMs like GPT-4 are trained on public data up to a specific date. They cannot know your private company data, real-time information, or events after training. RAG addresses this by retrieving current, private data and providing it in the prompt."
                        },
                        {
                            "q": "What does the 'R' in RAG stand for?",
                            "opts": ["A. Reasoning", "B. Retrieval", "C. Ranking", "D. Real-time"],
                            "correct": "B",
                            "explain": "RAG = Retrieval-Augmented Generation. Retrieval refers to searching and fetching relevant information from a data store (like a SQL database). This retrieved context augments (enriches) the prompt sent to the LLM."
                        },
                        {
                            "q": "In a RAG pipeline using SQL, what is the role of vector search or full-text search?",
                            "opts": ["A. To replace the LLM entirely", "B. To retrieve relevant context from the SQL database based on the user's question", "C. To generate the final answer", "D. To train the LLM on new data"],
                            "correct": "B",
                            "explain": "SQL search (vector, full-text, or hybrid) is the Retrieval step in RAG. It finds the most relevant rows/documents from the database given the user's question. These retrieved rows become the context fed into the LLM prompt."
                        },
                        {
                            "q": "Why is SQL particularly well-suited as the retrieval layer for enterprise RAG solutions?",
                            "opts": ["A. SQL is faster than specialized vector databases", "B. Most enterprise data is already stored in SQL databases, avoiding the need to migrate to specialized vector databases", "C. SQL can generate text responses without an LLM", "D. SQL is free and requires no licensing"],
                            "correct": "B",
                            "explain": "Enterprise data (product catalogs, customer records, documents, knowledge bases) already lives in SQL databases. Using SQL for RAG retrieval means you can build AI-powered Q&A on existing data without a full migration to a specialized vector database."
                        },
                        {
                            "q": "What are the three steps of a RAG pipeline in order?",
                            "opts": ["A. Generate → Retrieve → Augment", "B. Augment → Retrieve → Generate", "C. Retrieve → Augment → Generate", "D. Train → Retrieve → Generate"],
                            "correct": "C",
                            "explain": "RAG follows the order: (1) Retrieve — search the database for relevant context, (2) Augment — add the retrieved context to the LLM prompt, (3) Generate — the LLM produces an answer based on the augmented prompt."
                        }
                    ]
                },

                # ── Unit 2: RAG use cases and architecture ────────────────
                {
                    "id": "lp3-m11-u2",
                    "title": "RAG use cases and architecture",
                    "description": "Explore real-world RAG use cases and understand the end-to-end architecture of a SQL-based RAG solution.",
                    "estimated_time": 20,
                    "objectives": [
                        "Identify common enterprise RAG use cases",
                        "Understand the end-to-end RAG architecture with SQL",
                        "Know the components involved: embedding, retrieval, prompt building, LLM call",
                        "Understand the token budget — fitting context into the LLM's context window"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Common RAG Use Cases",
                            "body": "<strong>1. Knowledge Base Q&amp;A</strong><br>Users ask questions like 'How do I reset my password?' The system searches a support knowledge base, retrieves the relevant article, and generates a helpful, conversational answer.\n\n<strong>2. Product Catalog Q&amp;A</strong><br>'What laptops do you have under $800 with more than 16GB RAM?' RAG retrieves matching products and lets the LLM synthesize a natural language recommendation.\n\n<strong>3. Document Q&amp;A</strong><br>Users ask questions about uploaded PDFs or policy documents stored in the database. RAG retrieves relevant sections and answers questions about them.\n\n<strong>4. Customer Support Copilot</strong><br>Support agents type a customer issue; the system retrieves similar past cases and resolution steps, helping agents resolve issues faster.\n\n<strong>5. Internal Data Assistant</strong><br>Business users ask plain English questions about internal data: 'Show me sales trends for Q3 in the Northwest region.' RAG can retrieve the relevant aggregated data and explain it in natural language.\n\n<strong>Common thread:</strong> In every case, the user's question drives a SQL search, the SQL results provide grounding facts, and the LLM converts those facts into a natural language response."
                        },
                        {
                            "type": "theory",
                            "title": "RAG Architecture with SQL — End-to-End Flow",
                            "body": "Here is the complete flow of a SQL-based RAG system:\n\n<ol>\n<li><strong>User sends a question</strong><br>Example: 'What are the symptoms of SQL Server blocking?'</li>\n\n<li><strong>Embed the question</strong><br>Call Azure OpenAI text-embedding-ada-002 via sp_invoke_external_rest_endpoint. Get a VECTOR(1536).</li>\n\n<li><strong>Retrieve relevant chunks</strong><br>Run VECTOR_DISTANCE search (or hybrid FTS+vector) against a SQL table of document chunks. Get the top 3-5 most relevant text chunks.</li>\n\n<li><strong>Build the augmented prompt</strong><br>Concatenate: system instructions + retrieved text chunks + user question. This is the 'augmented prompt' sent to the LLM.</li>\n\n<li><strong>Call the chat completion API</strong><br>POST the augmented prompt to Azure OpenAI gpt-4 or gpt-35-turbo via sp_invoke_external_rest_endpoint.</li>\n\n<li><strong>Parse and return the response</strong><br>Extract choices[0].message.content from the JSON response. Return it to the user.</li>\n\n<li><strong>Optionally store conversation history</strong><br>Save the question and answer to a conversation history table for multi-turn chat support.</li>\n</ol>"
                        },
                        {
                            "type": "important",
                            "title": "The Token Budget — Context Window Limits",
                            "body": "Every LLM has a <strong>context window limit</strong> — the maximum total tokens (input + output) it can process at once.\n<ul><li>gpt-35-turbo: 4,096 tokens (~3,000 words)</li><li>gpt-4: 8,192 or 32,768 tokens depending on version</li><li>gpt-4o: 128,000 tokens</li></ul>\n\nYour augmented prompt must fit within this limit. The prompt includes:\n<ul><li>System instructions (~100-300 tokens)</li><li>Retrieved context chunks (the bulk — typically 1,000-3,000 tokens)</li><li>User question (~50-200 tokens)</li><li>Reserve for the response (~500-1,000 tokens)</li></ul>\n\n<strong>Practical rule:</strong> For gpt-35-turbo, limit retrieved context to ~2,500 tokens. For gpt-4o, you can include much more context.\n\nThis is why chunking (next unit) matters — you need to retrieve the right amount of context, not too much or too little."
                        },
                        {
                            "type": "tip",
                            "title": "Metadata Filtering for Better Retrieval",
                            "body": "Add metadata columns to your chunks table to enable filtered retrieval:\n<code>CREATE TABLE DocumentChunks (ChunkID INT, DocumentID INT, Category NVARCHAR(100), CreatedDate DATE, ChunkText NVARCHAR(MAX), ChunkEmbedding VECTOR(1536));</code>\n\nThen filter before search: WHERE Category = 'Technical' AND CreatedDate > '2024-01-01'. This reduces the search space AND improves relevance by limiting results to the right category or time period."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "A company wants users to ask natural language questions about their internal policy documents stored in SQL. Which pattern describes this use case?",
                            "opts": ["A. Full-text search with CONTAINS", "B. RAG — retrieve relevant policy sections from SQL, augment an LLM prompt, generate a conversational answer", "C. A stored procedure that returns raw policy text", "D. Azure AI Document Intelligence"],
                            "correct": "B",
                            "explain": "This is a classic RAG use case: Document Q&A. The user's question drives a similarity search of policy documents in SQL. Retrieved policy sections become the LLM prompt context, and the LLM generates a natural language answer grounded in the actual policy text."
                        },
                        {
                            "q": "In the RAG architecture, what is the purpose of Step 2 (embedding the user's question)?",
                            "opts": ["A. To translate the question to SQL", "B. To create a vector that can be compared against stored document embeddings for similarity search", "C. To encrypt the user's question for privacy", "D. To count the tokens in the user's question"],
                            "correct": "B",
                            "explain": "Embedding the user's question converts it to a vector using the same model used to embed the stored documents. This enables VECTOR_DISTANCE comparison — finding stored document chunks whose vectors are closest to the query vector."
                        },
                        {
                            "q": "What is the 'context window' of an LLM and why does it matter for RAG?",
                            "opts": ["A. The time window during which the LLM is available for API calls", "B. The maximum total tokens (prompt + response) the LLM can process in one call — limits how much retrieved context you can include", "C. The browser window used to view LLM responses", "D. The number of conversation turns the LLM can remember"],
                            "correct": "B",
                            "explain": "The context window is the LLM's maximum input+output size in tokens. It limits how much retrieved SQL context you can include in the augmented prompt. If you retrieve too many chunks, you may exceed the limit. This is why chunking and selective retrieval are important."
                        },
                        {
                            "q": "Which step in the RAG pipeline is responsible for converting the final response into a user-readable answer?",
                            "opts": ["A. The SQL vector search step", "B. The prompt augmentation step", "C. The LLM chat completion call (Generate step)", "D. The database master key"],
                            "correct": "C",
                            "explain": "The Generate step calls the LLM (e.g., Azure OpenAI gpt-4) with the augmented prompt. The LLM reads the system instructions, retrieved context, and user question, then generates a natural language answer. This is what the user ultimately sees."
                        },
                        {
                            "q": "What is metadata filtering in the context of RAG retrieval, and what is its benefit?",
                            "opts": ["A. Filtering SQL column names before sending to the LLM", "B. Using SQL WHERE conditions on metadata columns (category, date, author) to narrow the retrieval search space and improve relevance", "C. Filtering out stopwords from the LLM response", "D. Removing personal data from retrieved context for privacy"],
                            "correct": "B",
                            "explain": "Metadata filtering uses regular SQL WHERE conditions (e.g., WHERE Category = 'Technical') before or during vector search. This reduces the candidate set and improves relevance — you are not searching all documents, just the ones in the right category or time period."
                        }
                    ]
                },

                # ── Unit 3: Prepare retrieval context ────────────────────
                {
                    "id": "lp3-m11-u3",
                    "title": "Prepare retrieval context",
                    "description": "Learn how to chunk long documents for storage in SQL and prepare them for effective RAG retrieval.",
                    "estimated_time": 25,
                    "objectives": [
                        "Understand why chunking is necessary for RAG",
                        "Implement text chunking in T-SQL",
                        "Create a DocumentChunks table with proper schema",
                        "Choose appropriate chunk size and overlap strategies"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Why Chunk Documents?",
                            "body": "RAG retrieval works best with <strong>chunks</strong> — shorter pieces of text rather than full documents. Here is why:\n\n<strong>Problem with full documents:</strong>\n<ul><li>A 10-page policy document exceeds the 8,191-token limit of text-embedding-ada-002</li><li>Even within limits, a very long embedding is a poor representation of any single topic within the document</li><li>If you store one embedding per document, a search for 'refund policy' might match an HR document that mentions refunds in passing, rather than the actual refund policy section</li></ul>\n\n<strong>The chunking solution:</strong><br>Split each document into smaller pieces (chunks) — typically 200-500 words each. Each chunk gets its own embedding that precisely represents that specific piece of content.\n\n<strong>Chunk size tradeoffs:</strong>\n<table>\n<tr><td><strong>Too small (&lt;100 words)</strong></td><td>Lost context; a chunk might be a single sentence without enough surrounding information</td></tr>\n<tr><td><strong>Too large (&gt;1000 words)</strong></td><td>Embeddings become 'blurry' — the vector averages too many topics; also harder to fit multiple chunks in the LLM context window</td></tr>\n<tr><td><strong>Just right (200-500 words)</strong></td><td>Enough context for meaning, precise enough for targeted search</td></tr>\n</table>\n\n<strong>Chunk overlap:</strong><br>When splitting at chunk boundaries, a sentence might be cut in half. Overlapping chunks (last 50 words of chunk N = first 50 words of chunk N+1) prevents losing meaning at boundaries."
                        },
                        {
                            "type": "sql_block",
                            "title": "Create a DocumentChunks Table",
                            "scenario": "Design and create a table to store document chunks with their embeddings, ready for RAG retrieval.",
                            "code": """-- DocumentChunks table for RAG retrieval
CREATE TABLE DocumentChunks (
    ChunkID         INT           PRIMARY KEY IDENTITY(1,1),
    DocumentID      INT           NOT NULL,        -- FK to a Documents table
    DocumentTitle   NVARCHAR(300) NOT NULL,        -- Included for display
    ChunkIndex      INT           NOT NULL,        -- Which chunk number within the document
    ChunkText       NVARCHAR(MAX) NOT NULL,        -- The actual text of this chunk
    ChunkWordCount  INT,                           -- Approximate word count of this chunk
    Category        NVARCHAR(100),                 -- For metadata filtering
    SourceDate      DATE,                          -- Document creation/update date
    ChunkEmbedding  VECTOR(1536),                  -- Embedding of ChunkText
    EmbeddingModel  NVARCHAR(100) DEFAULT 'text-embedding-ada-002',
    EmbeddingUpdated DATETIME2
);

-- Index to filter by document and category efficiently
CREATE INDEX IX_DocumentChunks_DocumentID ON DocumentChunks(DocumentID);
CREATE INDEX IX_DocumentChunks_Category   ON DocumentChunks(Category);

-- Verify the schema
SELECT COLUMN_NAME, DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'DocumentChunks'
ORDER BY ORDINAL_POSITION;""",
                            "explanation": "This table stores one row per text chunk from each document. Each chunk has its own embedding. The metadata columns (Category, SourceDate) enable pre-filtering before vector search. ChunkIndex tracks the order of chunks within a document for reassembly.",
                            "purpose": "Define the core table for a RAG retrieval system that stores document chunks with their embeddings.",
                            "breakdown": [
                                {"line": "ChunkID INT PRIMARY KEY IDENTITY(1,1)", "meaning": "Unique identifier for each chunk. Required for the FULLTEXT INDEX KEY INDEX if you also add full-text search."},
                                {"line": "DocumentID INT NOT NULL", "meaning": "Links back to the source document. Allows you to retrieve all chunks from a specific document or filter by document category."},
                                {"line": "ChunkIndex INT NOT NULL", "meaning": "The sequential number of this chunk within the document (0, 1, 2, ...). Useful for retrieving neighboring chunks for additional context if needed."},
                                {"line": "ChunkWordCount INT", "meaning": "Approximate word count. Useful for monitoring that chunks are the right size and for debugging why some chunks might not embed well."},
                                {"line": "Category NVARCHAR(100)", "meaning": "Document category for pre-filtering. A user asking about 'refund policy' should only search chunks from the 'Policies' category, not technical documentation."},
                                {"line": "CREATE INDEX IX_DocumentChunks_Category ON DocumentChunks(Category)", "meaning": "A regular B-tree index on the Category column enables fast pre-filtering. Without this, filtering by category before vector search would require a full table scan."}
                            ],
                            "ssms_steps": [
                                "Open SSMS and connect to your Azure SQL Database",
                                "Click New Query",
                                "Paste the CREATE TABLE and CREATE INDEX statements",
                                "Press F5 to execute",
                                "In Object Explorer, expand Tables and refresh to see DocumentChunks",
                                "Expand Columns to verify the VECTOR column appears as expected",
                                "Run the INFORMATION_SCHEMA query to see all column names and types"
                            ],
                            "exam_tip": "The DocumentChunks table design is important for RAG. Key points: (1) one row per chunk, not per document; (2) store both ChunkText AND ChunkEmbedding; (3) include metadata columns for filtering; (4) include ChunkIndex to reconstruct document order if needed."
                        },
                        {
                            "type": "sql_block",
                            "title": "Chunking Text with T-SQL",
                            "scenario": "You have a long support article (2000 words) stored as a single NVARCHAR(MAX). Split it into ~400-word chunks with T-SQL and insert each chunk into DocumentChunks.",
                            "code": """-- T-SQL text chunking using recursive CTE
-- Splits a long document into chunks of approximately @ChunkSize characters
-- (Use character count as proxy for word count — roughly 5 chars/word)

DECLARE @DocumentID    INT          = 1;
DECLARE @DocumentTitle NVARCHAR(300)= 'SQL Server Troubleshooting Guide';
DECLARE @Category      NVARCHAR(100)= 'Technical';
DECLARE @SourceDate    DATE         = '2024-06-01';
DECLARE @FullText      NVARCHAR(MAX);   -- The full document text
DECLARE @ChunkSize     INT          = 2000;  -- Characters per chunk (~400 words)
DECLARE @Overlap       INT          = 200;   -- Overlap characters between chunks

-- Get the source document text
SELECT @FullText = DocumentContent FROM SourceDocuments WHERE DocumentID = @DocumentID;

-- Split into chunks using a recursive CTE
;WITH Chunks AS (
    -- Base case: first chunk
    SELECT
        0                          AS ChunkIndex,
        SUBSTRING(@FullText, 1, @ChunkSize) AS ChunkText,
        @ChunkSize - @Overlap      AS NextStart     -- Next chunk starts with overlap

    UNION ALL

    -- Recursive case: each subsequent chunk
    SELECT
        ChunkIndex + 1,
        SUBSTRING(@FullText, NextStart, @ChunkSize),
        NextStart + @ChunkSize - @Overlap
    FROM Chunks
    WHERE NextStart <= LEN(@FullText)     -- Stop when we've passed the end
)
INSERT INTO DocumentChunks (DocumentID, DocumentTitle, ChunkIndex, ChunkText, ChunkWordCount, Category, SourceDate)
SELECT
    @DocumentID,
    @DocumentTitle,
    ChunkIndex,
    ChunkText,
    LEN(ChunkText) / 5   AS ChunkWordCount,   -- Rough word count estimate
    @Category,
    @SourceDate
FROM Chunks
WHERE LEN(LTRIM(RTRIM(ChunkText))) > 0   -- Skip empty chunks
OPTION (MAXRECURSION 1000);              -- Allow up to 1000 chunks per document

-- Verify the chunks created
SELECT ChunkID, ChunkIndex, ChunkWordCount, LEFT(ChunkText, 100) AS Preview
FROM DocumentChunks
WHERE DocumentID = @DocumentID
ORDER BY ChunkIndex;""",
                            "explanation": "This uses a recursive CTE to split a long document into overlapping chunks. Each iteration of the recursion produces one chunk. The OPTION (MAXRECURSION 1000) allows documents to be split into up to 1000 chunks before stopping.",
                            "purpose": "Split long document text into appropriately sized chunks ready for embedding and RAG retrieval.",
                            "breakdown": [
                                {"line": "@ChunkSize INT = 2000", "meaning": "Chunk size in characters. 2000 chars ≈ 400 words (at ~5 chars/word). Adjust based on your LLM's context window and the granularity of search you need."},
                                {"line": "@Overlap INT = 200", "meaning": "Number of characters to repeat between consecutive chunks. This prevents losing context at chunk boundaries where a sentence might be cut in half."},
                                {"line": "SELECT 0 AS ChunkIndex, SUBSTRING(@FullText, 1, @ChunkSize) AS ChunkText, @ChunkSize - @Overlap AS NextStart", "meaning": "The base case starts the recursion with the first chunk (characters 1 to @ChunkSize). NextStart is where the NEXT chunk begins (shifted back by @Overlap characters)."},
                                {"line": "SUBSTRING(@FullText, NextStart, @ChunkSize)", "meaning": "Each recursive step extracts the next chunk starting from NextStart. SUBSTRING(string, start, length) — start is 1-based in T-SQL."},
                                {"line": "WHERE NextStart <= LEN(@FullText)", "meaning": "The recursion stops when the next start position is beyond the end of the document. This prevents generating empty chunks."},
                                {"line": "OPTION (MAXRECURSION 1000)", "meaning": "SQL Server limits recursive CTEs to 100 levels by default (which would only support documents up to ~40,000 characters). MAXRECURSION 1000 increases this limit to support longer documents."}
                            ],
                            "ssms_steps": [
                                "First create a SourceDocuments table: CREATE TABLE SourceDocuments (DocumentID INT PRIMARY KEY, DocumentTitle NVARCHAR(300), DocumentContent NVARCHAR(MAX))",
                                "Insert a test document: INSERT INTO SourceDocuments VALUES (1, 'Test Doc', REPLICATE('This is a test sentence about SQL Server. ', 100))",
                                "Paste the chunking CTE code above",
                                "Set @DocumentID = 1 to match your test document",
                                "Press F5 to run",
                                "Run the verification SELECT to see the chunks created",
                                "Check that each chunk is approximately 400 words and overlapping content is visible at boundaries"
                            ],
                            "exam_tip": "Recursive CTEs in SQL Server require OPTION (MAXRECURSION N) for documents that would produce more than 100 chunks. The default limit is 100 recursions. For the exam, know that chunking is a prerequisite for effective RAG retrieval."
                        },
                        {
                            "type": "tip",
                            "title": "Sentence Boundary Splitting",
                            "body": "The character-based SUBSTRING chunking above may split sentences in the middle. A better production approach is to split at sentence boundaries — look for '. ' or '\\n\\n' (paragraph breaks) near your target chunk size.\n\nA simple heuristic: find the last '. ' before @ChunkSize characters:\n<code>SET @SplitPos = CHARINDEX('. ', @FullText, @ChunkSize - 200);\nIF @SplitPos = 0 SET @SplitPos = @ChunkSize;</code>\n\nThis produces more natural chunks where each chunk is complete sentences."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "Why is chunking necessary before embedding documents for RAG?",
                            "opts": ["A. Because the VECTOR data type has a maximum size limit", "B. To fit within embedding model token limits and create precise, topic-focused embeddings for better search accuracy", "C. Because SQL Server cannot store documents longer than 1000 characters", "D. To reduce the number of API calls to Azure OpenAI"],
                            "correct": "B",
                            "explain": "Embedding models have token limits (e.g., 8,191 for ada-002). Long documents exceed these limits. Additionally, smaller chunks produce more precise embeddings focused on specific topics, improving search accuracy compared to one blurry embedding for an entire document."
                        },
                        {
                            "q": "What is chunk overlap and why is it used?",
                            "opts": ["A. Storing the same chunk twice for redundancy", "B. Repeating a portion of text at the start of the next chunk to prevent losing context at chunk boundaries", "C. Embedding the same text with two different models", "D. Creating indexes that span multiple chunks"],
                            "correct": "B",
                            "explain": "Chunk overlap means the last N characters of chunk i are also the first N characters of chunk i+1. This prevents important context from being lost when a sentence is split across a chunk boundary."
                        },
                        {
                            "q": "What does OPTION (MAXRECURSION 1000) do in a recursive CTE for chunking?",
                            "opts": ["A. Limits the query to returning 1000 rows", "B. Allows the recursive CTE to recurse up to 1000 times instead of the default 100, supporting longer documents", "C. Sets the maximum chunk size to 1000 characters", "D. Enables parallel processing of 1000 chunks at once"],
                            "correct": "B",
                            "explain": "SQL Server limits recursive CTEs to 100 levels by default to prevent infinite loops. For chunking long documents into 100+ chunks, you need OPTION (MAXRECURSION N) to raise this limit. MAXRECURSION 0 removes the limit entirely (use with care)."
                        },
                        {
                            "q": "A document is 10,000 characters long with @ChunkSize=2000 and @Overlap=200. Approximately how many chunks will be produced?",
                            "opts": ["A. 5 chunks", "B. 6 chunks", "C. 10 chunks", "D. 50 chunks"],
                            "correct": "B",
                            "explain": "Effective step size per chunk = ChunkSize - Overlap = 2000 - 200 = 1800 characters. Number of chunks ≈ ceil(10000 / 1800) ≈ 6 chunks (with the last chunk potentially shorter than full size)."
                        },
                        {
                            "q": "Why should the DocumentChunks table include a Category column with an index on it?",
                            "opts": ["A. Category is required by the VECTOR data type", "B. To enable fast pre-filtering — limiting vector search to relevant document categories before computing similarity distances", "C. To store the embedding model name", "D. To comply with SQL Server licensing requirements"],
                            "correct": "B",
                            "explain": "A regular B-tree index on Category enables fast pre-filtering with WHERE Category = 'Technical'. This narrows the vector search to only relevant chunks before VECTOR_DISTANCE computation, improving both relevance and performance."
                        }
                    ]
                },

                # ── Unit 4: Augment prompts with SQL data ─────────────────
                {
                    "id": "lp3-m11-u4",
                    "title": "Augment prompts with SQL data",
                    "description": "Learn how to retrieve relevant context from SQL and build the augmented prompt for the LLM.",
                    "estimated_time": 25,
                    "objectives": [
                        "Retrieve top-N relevant chunks using vector search",
                        "Concatenate retrieved chunks into a context string",
                        "Build a well-structured augmented prompt",
                        "Understand the system prompt, context, and user question structure"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Prompt Engineering for RAG",
                            "body": "A well-structured RAG prompt has three parts:\n\n<strong>1. System Prompt</strong><br>Instructions that set the context, persona, and rules for the LLM. Example:\n<em>'You are a helpful SQL Server support assistant. Answer questions based ONLY on the provided context. If the context does not contain enough information to answer the question, say \"I don't have information about that.\" Do not make up answers.'</em>\n\n<strong>2. Retrieved Context</strong><br>The relevant chunks retrieved from the SQL database, formatted as text. Label them clearly:\n<em>CONTEXT:\n[Chunk 1]: ...\n[Chunk 2]: ...\n[Chunk 3]: ...</em>\n\n<strong>3. User Question</strong><br>The actual question the user asked.\n<em>QUESTION: What are the symptoms of SQL Server blocking?</em>\n\n<strong>Why structure matters:</strong><br>The LLM reads all three parts and uses them together. A clear structure helps the LLM distinguish between background instructions, factual context, and the specific question to answer.\n\n<strong>Critical instruction: 'Answer based ONLY on the context'</strong><br>This instruction prevents the LLM from using its training knowledge to fill in gaps — which could introduce hallucinations (plausible-sounding but incorrect information). Always include this."
                        },
                        {
                            "type": "sql_block",
                            "title": "Retrieve Context and Build the Augmented Prompt",
                            "scenario": "A user asks 'What are the symptoms of SQL Server blocking?' Retrieve the top 3 most relevant knowledge base chunks and build the augmented prompt as a T-SQL string.",
                            "code": """-- Step 1: Set up the user question and retrieve its embedding
DECLARE @UserQuestion   NVARCHAR(MAX) = 'What are the symptoms of SQL Server blocking?';
DECLARE @Category       NVARCHAR(100) = 'Technical';  -- Optional metadata filter
DECLARE @QueryVector    VECTOR(1536);
DECLARE @EmbedPayload   NVARCHAR(MAX);
DECLARE @EmbedResponse  NVARCHAR(MAX);
DECLARE @EmbedStatus    INT;

-- Embed the user's question
SET @EmbedPayload = N'{"input": ' + (SELECT @UserQuestion FOR JSON PATH, WITHOUT_ARRAY_WRAPPER) + '}';
EXEC sp_invoke_external_rest_endpoint
    @url        = 'https://YOUR-RESOURCE.openai.azure.com/openai/deployments/text-embedding-ada-002/embeddings?api-version=2023-05-15',
    @method     = 'POST',
    @headers    = N'{"Content-Type": "application/json", "api-key": "YOUR-API-KEY"}',
    @payload    = @EmbedPayload,
    @response   = @EmbedResponse OUTPUT,
    @statuscode = @EmbedStatus OUTPUT;

IF @EmbedStatus = 200
    SET @QueryVector = CAST(JSON_QUERY(@EmbedResponse, '$.result.data[0].embedding') AS VECTOR(1536));

-- Step 2: Retrieve top 3 most relevant chunks from DocumentChunks
DECLARE @ContextText NVARCHAR(MAX) = '';

SELECT TOP 3
    @ContextText = @ContextText +
                   '[Context ' + CAST(ROW_NUMBER() OVER (ORDER BY VECTOR_DISTANCE('cosine', ChunkEmbedding, @QueryVector)) AS NVARCHAR(10)) + ']: ' +
                   ChunkText + CHAR(10) + CHAR(10)
FROM DocumentChunks
WHERE
    Category = @Category              -- Pre-filter by category
    AND ChunkEmbedding IS NOT NULL
    AND VECTOR_DISTANCE('cosine', ChunkEmbedding, @QueryVector) < 0.7  -- Relevance threshold
ORDER BY VECTOR_DISTANCE('cosine', ChunkEmbedding, @QueryVector) ASC;

-- Step 3: Build the augmented prompt
DECLARE @SystemPrompt NVARCHAR(MAX) =
    'You are a helpful SQL Server support assistant. ' +
    'Answer the question based ONLY on the provided context. ' +
    'If the context does not contain sufficient information, say "I do not have enough information to answer that question." ' +
    'Be concise and factual.';

DECLARE @AugmentedPrompt NVARCHAR(MAX) =
    'CONTEXT:' + CHAR(10) +
    @ContextText + CHAR(10) +
    'QUESTION: ' + @UserQuestion;

-- Preview what we will send to the LLM
SELECT
    LEN(@SystemPrompt) / 4        AS system_prompt_approx_tokens,
    LEN(@ContextText) / 4         AS context_approx_tokens,
    LEN(@AugmentedPrompt) / 4     AS total_prompt_approx_tokens,
    LEFT(@AugmentedPrompt, 500)   AS prompt_preview;""",
                            "explanation": "This builds the augmented prompt by: (1) embedding the user question, (2) retrieving the top 3 most relevant chunks from the DocumentChunks table, (3) concatenating them into a formatted context string, and (4) building the full prompt with system instructions, context, and question.",
                            "purpose": "Implement the Retrieval and Augment steps of the RAG pipeline to build a grounded LLM prompt.",
                            "breakdown": [
                                {"line": "@ContextText = @ContextText + '[Context ' + ... + ']'", "meaning": "String concatenation builds the context by appending each retrieved chunk to the running context variable. CHAR(10) adds line breaks between chunks for readability."},
                                {"line": "ROW_NUMBER() OVER (ORDER BY VECTOR_DISTANCE(...)) AS chunk_number", "meaning": "Numbers the context chunks in order of relevance (most relevant = [Context 1]). This helps the LLM understand which context is most relevant."},
                                {"line": "AND VECTOR_DISTANCE('cosine', ...) < 0.7", "meaning": "Threshold filter: only include chunks that are at least somewhat relevant (distance < 0.7). If no chunks meet this threshold, @ContextText remains empty, which should trigger the LLM's 'I don't have information' response."},
                                {"line": "LEN(@AugmentedPrompt) / 4 AS total_prompt_approx_tokens", "meaning": "Rough token estimate: 1 token ≈ 4 characters in English. This helps verify the prompt fits within the LLM's context window before sending."}
                            ],
                            "ssms_steps": [
                                "Open SSMS with a New Query window",
                                "Paste the code above",
                                "Replace YOUR-RESOURCE and YOUR-API-KEY",
                                "Press F5 to run",
                                "In the Results pane, check total_prompt_approx_tokens — it should be under 2000 for gpt-35-turbo",
                                "Review the prompt_preview to see how the context and question are formatted",
                                "If @ContextText is empty, either your chunks have no embeddings yet, or the threshold (0.7) is too strict"
                            ],
                            "exam_tip": "The instruction 'Answer based ONLY on the provided context' is critical for preventing hallucinations. Without it, the LLM may mix retrieved context with its training knowledge, potentially producing inaccurate answers. Always include a grounding instruction in the system prompt."
                        },
                        {
                            "type": "important",
                            "title": "Preventing LLM Hallucinations",
                            "body": "Hallucinations occur when an LLM generates plausible-sounding but incorrect information. In RAG, hallucinations usually happen when:\n<ul><li>The LLM fills in gaps not covered by the retrieved context with guessed information</li><li>The retrieved context is too short or irrelevant</li><li>The system prompt does not explicitly restrict the LLM to use only the provided context</li></ul>\n\n<strong>Prevention strategies:</strong>\n<ol><li>Always include 'Answer based ONLY on the provided context' in the system prompt</li><li>Include a fallback instruction: 'If the context does not answer the question, say you don't have that information'</li><li>Verify retrieved chunks are actually relevant (check cosine distance values)</li><li>Use temperature = 0 for factual tasks (temperature controls randomness; 0 = most deterministic)</li></ol>"
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What are the three parts of a well-structured RAG prompt?",
                            "opts": ["A. SQL query, API key, user ID", "B. System prompt, retrieved context, user question", "C. Embedding vector, cosine distance, chunk size", "D. Model name, temperature, max tokens"],
                            "correct": "B",
                            "explain": "A RAG prompt has three parts: (1) System prompt — instructions and persona for the LLM, (2) Retrieved context — relevant chunks from the SQL database, (3) User question — the actual question to answer. This structure helps the LLM understand its role, the facts to use, and what to answer."
                        },
                        {
                            "q": "Why is the instruction 'Answer based ONLY on the provided context' important in a RAG system prompt?",
                            "opts": ["A. It is required syntax for Azure OpenAI", "B. It prevents the LLM from mixing retrieved facts with training knowledge, reducing the risk of hallucinations", "C. It improves the speed of the API response", "D. It limits the response length to match the context size"],
                            "correct": "B",
                            "explain": "Without this instruction, the LLM may supplement retrieved context with its training knowledge, producing answers that seem reasonable but are not grounded in your actual data. Restricting to 'ONLY the provided context' forces the LLM to stick to what you retrieved."
                        },
                        {
                            "q": "Why is LEN(@AugmentedPrompt) / 4 a useful calculation before calling the LLM?",
                            "opts": ["A. It calculates the exact token count for billing", "B. It provides an approximate token count to verify the prompt fits within the LLM's context window", "C. It is required before calling sp_invoke_external_rest_endpoint", "D. It checks if the prompt contains valid JSON"],
                            "correct": "B",
                            "explain": "Tokens ≈ characters/4 for English text. Checking approximate token count before the API call helps you verify the prompt fits within the model's context window (e.g., ~4096 for gpt-35-turbo). Exceeding the window causes an API error."
                        },
                        {
                            "q": "What happens if @ContextText is empty (no chunks retrieved) when the augmented prompt is built?",
                            "opts": ["A. The API call fails with an error", "B. The LLM receives a prompt with no context, and (if the system prompt is correct) should respond 'I don't have enough information to answer'", "C. The query returns NULL", "D. sp_invoke_external_rest_endpoint skips the call automatically"],
                            "correct": "B",
                            "explain": "If no chunks are retrieved (e.g., all chunks have similarity distance > 0.7), the CONTEXT section of the prompt is empty. A well-designed system prompt instructs the LLM to respond with 'I don't have information about that' rather than making up an answer."
                        },
                        {
                            "q": "What does temperature = 0 do when calling an LLM for RAG?",
                            "opts": ["A. Prevents the API from charging for the call", "B. Makes the LLM's responses deterministic and factual by eliminating randomness in token selection", "C. Sets the response language to English", "D. Limits the response to 0 characters"],
                            "correct": "B",
                            "explain": "Temperature controls how randomly the LLM selects each output token. Temperature=0 means always choosing the highest-probability token — producing the most deterministic, factual, and consistent responses. Higher temperature produces more creative/varied but potentially less accurate outputs. For factual RAG, use temperature=0."
                        }
                    ]
                },

                # ── Unit 5: Generate RAG responses ────────────────────────
                {
                    "id": "lp3-m11-u5",
                    "title": "Generate RAG responses",
                    "description": "Learn to call the Azure OpenAI chat completion API from T-SQL and parse the generated response.",
                    "estimated_time": 30,
                    "objectives": [
                        "Call Azure OpenAI chat completion from sp_invoke_external_rest_endpoint",
                        "Build the correct JSON payload for a chat completion request",
                        "Parse the LLM response from the JSON output",
                        "Store conversation history for multi-turn dialogue",
                        "Handle errors and edge cases in RAG responses"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Chat Completion API vs Embedding API",
                            "body": "You have already used the <strong>Embeddings API</strong> to convert text to vectors. The <strong>Chat Completion API</strong> is different:\n\n<strong>Embeddings API</strong>\n<ul><li>Input: text string</li><li>Output: JSON array of numbers (the vector)</li><li>Endpoint: <code>/openai/deployments/MODEL/embeddings</code></li></ul>\n\n<strong>Chat Completion API</strong>\n<ul><li>Input: array of message objects with roles (system, user, assistant)</li><li>Output: JSON with a generated text response</li><li>Endpoint: <code>/openai/deployments/MODEL/chat/completions</code></li></ul>\n\n<strong>Message roles:</strong>\n<ul><li><code>system</code> — background instructions for the LLM (sent once at the start)</li><li><code>user</code> — messages from the human (includes the context + question)</li><li><code>assistant</code> — the LLM's previous responses (for multi-turn conversation history)</li></ul>"
                        },
                        {
                            "type": "sql_block",
                            "title": "Complete RAG Pipeline — Single T-SQL Script",
                            "scenario": "Combine everything: embed the question, retrieve context chunks, build the augmented prompt, call the chat completion API, and parse the AI-generated answer — all in one T-SQL script.",
                            "code": """-- Complete RAG Pipeline in T-SQL
-- Assumes: DocumentChunks table with embeddings, Azure OpenAI deployed

DECLARE @UserQuestion    NVARCHAR(MAX) = 'What are the main causes of slow SQL Server queries?';
DECLARE @Category        NVARCHAR(100) = 'Technical';
DECLARE @QueryVector     VECTOR(1536);
DECLARE @ContextText     NVARCHAR(MAX) = '';
DECLARE @SystemPrompt    NVARCHAR(MAX);
DECLARE @UserMessage     NVARCHAR(MAX);
DECLARE @ChatPayload     NVARCHAR(MAX);
DECLARE @ChatResponse    NVARCHAR(MAX);
DECLARE @ChatStatus      INT;
DECLARE @AIAnswer        NVARCHAR(MAX);

-- ═══ STEP 1: Embed the user's question ═══════════════════════════════════
DECLARE @EmbedPayload  NVARCHAR(MAX);
DECLARE @EmbedResponse NVARCHAR(MAX);
DECLARE @EmbedStatus   INT;

SET @EmbedPayload = N'{"input": ' + (SELECT @UserQuestion FOR JSON PATH, WITHOUT_ARRAY_WRAPPER) + '}';
EXEC sp_invoke_external_rest_endpoint
    @url        = 'https://YOUR-RESOURCE.openai.azure.com/openai/deployments/text-embedding-ada-002/embeddings?api-version=2023-05-15',
    @method     = 'POST',
    @headers    = N'{"Content-Type": "application/json", "api-key": "YOUR-API-KEY"}',
    @payload    = @EmbedPayload,
    @response   = @EmbedResponse OUTPUT,
    @statuscode = @EmbedStatus OUTPUT;

IF @EmbedStatus <> 200 RAISERROR('Embedding API failed: %d', 16, 1, @EmbedStatus);
SET @QueryVector = CAST(JSON_QUERY(@EmbedResponse, '$.result.data[0].embedding') AS VECTOR(1536));

-- ═══ STEP 2: Retrieve top 3 relevant chunks ═══════════════════════════════
SELECT TOP 3
    @ContextText = @ContextText +
        '[Source ' + CAST(ROW_NUMBER() OVER (ORDER BY VECTOR_DISTANCE('cosine', ChunkEmbedding, @QueryVector)) AS NVARCHAR(5)) + ']: ' +
        ChunkText + CHAR(13) + CHAR(10)
FROM DocumentChunks
WHERE
    Category = @Category
    AND ChunkEmbedding IS NOT NULL
    AND VECTOR_DISTANCE('cosine', ChunkEmbedding, @QueryVector) < 0.8
ORDER BY VECTOR_DISTANCE('cosine', ChunkEmbedding, @QueryVector) ASC;

IF LEN(ISNULL(@ContextText, '')) = 0
BEGIN
    SELECT 'No relevant context found in the knowledge base for this question.' AS Answer;
    RETURN;
END

-- ═══ STEP 3: Build the augmented prompt ══════════════════════════════════
SET @SystemPrompt = 'You are a SQL Server expert assistant. Answer the user question based ONLY on the provided context. If the context does not have enough information, say so. Be concise.';
SET @UserMessage  = 'CONTEXT:' + CHAR(13) + CHAR(10) + @ContextText + CHAR(13) + CHAR(10) + 'QUESTION: ' + @UserQuestion;

-- ═══ STEP 4: Build the chat completion JSON payload ═══════════════════════
SET @ChatPayload = N'{
    "messages": [
        {"role": "system", "content": ' + (SELECT @SystemPrompt FOR JSON PATH, WITHOUT_ARRAY_WRAPPER) + '},
        {"role": "user",   "content": ' + (SELECT @UserMessage  FOR JSON PATH, WITHOUT_ARRAY_WRAPPER) + '}
    ],
    "temperature": 0,
    "max_tokens": 500
}';

-- ═══ STEP 5: Call the chat completion API ════════════════════════════════
EXEC sp_invoke_external_rest_endpoint
    @url        = 'https://YOUR-RESOURCE.openai.azure.com/openai/deployments/gpt-4/chat/completions?api-version=2024-02-01',
    @method     = 'POST',
    @headers    = N'{"Content-Type": "application/json", "api-key": "YOUR-API-KEY"}',
    @payload    = @ChatPayload,
    @response   = @ChatResponse OUTPUT,
    @statuscode = @ChatStatus OUTPUT;

IF @ChatStatus <> 200 RAISERROR('Chat API failed: %d. Response: %s', 16, 1, @ChatStatus, @ChatResponse);

-- ═══ STEP 6: Parse and return the AI answer ══════════════════════════════
SET @AIAnswer = JSON_VALUE(@ChatResponse, '$.result.choices[0].message.content');

SELECT
    @UserQuestion AS question,
    @AIAnswer     AS ai_answer,
    JSON_VALUE(@ChatResponse, '$.result.usage.prompt_tokens')     AS prompt_tokens,
    JSON_VALUE(@ChatResponse, '$.result.usage.completion_tokens') AS completion_tokens,
    JSON_VALUE(@ChatResponse, '$.result.usage.total_tokens')      AS total_tokens;""",
                            "explanation": "This single T-SQL script implements the complete 6-step RAG pipeline: embed → retrieve → build prompt → format JSON → call chat API → parse response. The final SELECT shows the AI's answer alongside token usage for cost monitoring.",
                            "purpose": "Implement the full RAG pipeline from user question to AI-generated answer in a single T-SQL script.",
                            "breakdown": [
                                {"line": "\"messages\": [{\"role\": \"system\", ...}, {\"role\": \"user\", ...}]", "meaning": "The chat completion API takes an array of messages. The 'system' role sets LLM behavior; 'user' role contains the augmented prompt (context + question). Additional 'assistant' messages can include conversation history for multi-turn chat."},
                                {"line": "\"temperature\": 0", "meaning": "Sets output determinism. 0 = most deterministic/factual output. For RAG answering factual questions, temperature=0 reduces randomness and hallucinations."},
                                {"line": "\"max_tokens\": 500", "meaning": "Maximum length of the generated response. 500 tokens ≈ 375 words. Adjust based on how long you expect answers to be. This also controls maximum API cost per call."},
                                {"line": "JSON_VALUE(@ChatResponse, '$.result.choices[0].message.content')", "meaning": "Extracts the AI's generated answer. The path: result > choices (array) > [0] (first choice) > message > content. This is the actual text response from the LLM."},
                                {"line": "JSON_VALUE(@ChatResponse, '$.result.usage.total_tokens')", "meaning": "Total tokens consumed by this request (input + output). Use this to monitor costs and ensure you stay within token limits."},
                                {"line": "(SELECT @SystemPrompt FOR JSON PATH, WITHOUT_ARRAY_WRAPPER)", "meaning": "Converts the system prompt string to a properly escaped JSON string value. This handles special characters (quotes, backslashes, newlines) that would break the JSON payload if included as-is."}
                            ],
                            "ssms_steps": [
                                "Ensure DocumentChunks has data with embeddings from previous units",
                                "Open SSMS with a New Query window",
                                "Paste the complete 6-step RAG script",
                                "Replace YOUR-RESOURCE and YOUR-API-KEY in both API calls (embedding and chat)",
                                "Replace gpt-4 in the chat URL with your deployed model name",
                                "Change @UserQuestion to a question your documents can answer",
                                "Press F5 to run all 6 steps",
                                "In Results, you should see: the question, the AI's answer, and token counts",
                                "Verify the answer is grounded in your document content, not made up"
                            ],
                            "exam_tip": "The chat completion response path for the generated text is $.result.choices[0].message.content — not $.result.text or $.result.answer. This is a common exam trick. Also note: chat completions use a different endpoint path than embeddings (/chat/completions vs /embeddings)."
                        },
                        {
                            "type": "sql_block",
                            "title": "Store Conversation History for Multi-Turn RAG",
                            "scenario": "A user wants to have a back-and-forth conversation with the AI assistant. Store each question and answer so subsequent turns can include conversation history.",
                            "code": """-- Table to store RAG conversation history
CREATE TABLE ConversationHistory (
    MessageID     INT          PRIMARY KEY IDENTITY(1,1),
    SessionID     UNIQUEIDENTIFIER NOT NULL DEFAULT NEWID(),  -- Groups messages in a session
    Role          NVARCHAR(20) NOT NULL CHECK (Role IN ('user', 'assistant', 'system')),
    Content       NVARCHAR(MAX) NOT NULL,
    TokenCount    INT,
    CreatedAt     DATETIME2    DEFAULT GETUTCDATE()
);

-- Insert a conversation turn after getting the RAG response
INSERT INTO ConversationHistory (SessionID, Role, Content, TokenCount)
VALUES
    (@SessionID, 'user',      @UserQuestion, NULL),
    (@SessionID, 'assistant', @AIAnswer,     NULL);

-- Build chat payload with conversation history for multi-turn
-- Retrieve the last 5 turns (10 messages: 5 user + 5 assistant)
DECLARE @MessagesJSON NVARCHAR(MAX) = '';

SELECT @MessagesJSON = @MessagesJSON +
    '{"role": "' + Role + '", "content": ' + (SELECT Content FOR JSON PATH, WITHOUT_ARRAY_WRAPPER) + '},'
FROM (
    SELECT TOP 10 Role, Content
    FROM ConversationHistory
    WHERE SessionID = @SessionID
    ORDER BY MessageID DESC     -- Get the most recent
) recent
ORDER BY MessageID ASC;         -- Re-order to chronological for the payload

-- Remove trailing comma from the list
SET @MessagesJSON = LEFT(@MessagesJSON, LEN(@MessagesJSON) - 1);

-- Build the full chat payload including history
SET @ChatPayload = N'{
    "messages": [
        {"role": "system", "content": ' + (SELECT @SystemPrompt FOR JSON PATH, WITHOUT_ARRAY_WRAPPER) + '},' +
        @MessagesJSON + ',' +
        '{"role": "user", "content": ' + (SELECT @UserMessage FOR JSON PATH, WITHOUT_ARRAY_WRAPPER) + '}
    ],
    "temperature": 0,
    "max_tokens": 500
}';""",
                            "explanation": "This extends the RAG pipeline for multi-turn conversation. ConversationHistory stores all messages in a session. When building the next prompt, you include recent history so the LLM understands the conversation context.",
                            "purpose": "Enable multi-turn RAG conversations where the LLM can reference previous questions and answers in the session.",
                            "breakdown": [
                                {"line": "SessionID UNIQUEIDENTIFIER NOT NULL DEFAULT NEWID()", "meaning": "Groups all messages in a conversation. A new GUID is generated for each new conversation session. NEWID() generates a globally unique identifier."},
                                {"line": "Role NVARCHAR(20) CHECK (Role IN ('user', 'assistant', 'system'))", "meaning": "The message role — must be one of the three valid chat roles. The CHECK constraint prevents invalid role values from being stored."},
                                {"line": "ORDER BY MessageID DESC ... ORDER BY MessageID ASC", "meaning": "The inner ORDER BY DESC takes the MOST RECENT messages. The outer ORDER BY ASC re-sorts them chronologically so the LLM reads conversation history in correct time order."}
                            ],
                            "ssms_steps": [
                                "Create the ConversationHistory table with the CREATE TABLE above",
                                "At the end of each RAG pipeline execution, insert the user question and AI answer",
                                "For subsequent turns, use the history-aware chat payload",
                                "Test with two questions in sequence: first ask a broad question, then a follow-up",
                                "Verify the AI's follow-up answer references context from the first turn"
                            ],
                            "exam_tip": "For multi-turn conversation in the chat API, include previous turns as alternating 'user' and 'assistant' messages in the messages array. The LLM uses these to understand context. However, watch token limits — each history turn adds tokens. Limit to the last 5-10 turns for most models."
                        },
                        {
                            "type": "tip",
                            "title": "Monitoring RAG Quality",
                            "body": "After building a RAG system, monitor these signals to detect quality issues:\n<ul><li><strong>Context coverage</strong>: Log when @ContextText is empty — this means the question found no relevant chunks. May indicate poor chunking or missing content.</li><li><strong>Token usage</strong>: Log total_tokens per call. Spikes may indicate bloated context chunks or very long questions.</li><li><strong>Response patterns</strong>: If the AI frequently says 'I don't have enough information', your vector search threshold may be too strict or your knowledge base needs more content.</li><li><strong>Latency</strong>: Log the time for each step. If embedding is slow, consider caching popular query embeddings.</li></ul>"
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What is the JSON path to extract the generated text from an Azure OpenAI chat completion response?",
                            "opts": ["A. $.result.text", "B. $.result.choices[0].message.content", "C. $.result.answer", "D. $.result.output.text"],
                            "correct": "B",
                            "explain": "The Azure OpenAI chat completion response structure is: result > choices (array) > [0] (first choice) > message > content. The JSON path is $.result.choices[0].message.content, accessed with JSON_VALUE()."
                        },
                        {
                            "q": "What does temperature = 0 mean in a chat completion API call?",
                            "opts": ["A. The API call times out in 0 seconds", "B. The LLM produces the most deterministic, consistent output by always choosing the highest probability token", "C. The response is returned at 0 cost", "D. No tokens are consumed"],
                            "correct": "B",
                            "explain": "Temperature controls randomness in LLM output. Temperature=0 means always selecting the most probable next token — producing consistent, deterministic, factual answers. Higher temperatures (0.7-1.0) add more creativity and variability."
                        },
                        {
                            "q": "Why is FOR JSON PATH, WITHOUT_ARRAY_WRAPPER used when building the chat payload?",
                            "opts": ["A. To convert the SQL results to a table", "B. To properly escape special characters (quotes, newlines, backslashes) in strings being embedded in JSON", "C. To reduce the size of the API payload", "D. It is required by sp_invoke_external_rest_endpoint"],
                            "correct": "B",
                            "explain": "FOR JSON PATH, WITHOUT_ARRAY_WRAPPER converts a string value to a properly escaped JSON string — handling special characters like double quotes (\"), backslashes (\\), and newlines (\\n). Without this, a user question containing a quote would break the JSON payload."
                        },
                        {
                            "q": "In a multi-turn RAG conversation, why do you include 'assistant' role messages in the chat payload?",
                            "opts": ["A. Azure OpenAI requires at least one assistant message", "B. To show the LLM the previous responses so it can maintain context and coherence across conversation turns", "C. To reduce the number of API calls needed", "D. Assistant messages are the retrieved context chunks"],
                            "correct": "B",
                            "explain": "Including previous 'assistant' messages in the chat payload gives the LLM memory of what it said before. Without these, each turn is independent — the LLM cannot refer to previous answers or maintain a coherent multi-turn conversation."
                        },
                        {
                            "q": "If the max_tokens parameter is set to 500 in the chat completion call, what happens if the LLM's response would naturally be 800 tokens long?",
                            "opts": ["A. The API raises an error", "B. The response is truncated at approximately 500 tokens, potentially cutting off mid-sentence", "C. The API automatically increases max_tokens to 800", "D. The response is compressed to fit 500 tokens"],
                            "correct": "B",
                            "explain": "max_tokens is a hard limit on the generated response length. If the natural response would be longer, the generation stops at max_tokens, potentially mid-sentence. Always set max_tokens high enough for expected response length but not so high that it wastes money on padding."
                        }
                    ]
                },

                # ── Unit 6: Exercise ──────────────────────────────────────
                {
                    "id": "lp3-m11-u6",
                    "title": "Exercise",
                    "description": "Hands-on exercise: build a complete RAG Q&A system for a company's FAQ knowledge base.",
                    "estimated_time": 60,
                    "objectives": [
                        "Set up a FAQ knowledge base with chunked content and embeddings",
                        "Implement the complete RAG pipeline as a stored procedure",
                        "Test the system with multiple questions",
                        "Add conversation history support"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Exercise: Company FAQ RAG System",
                            "body": "<strong>Scenario:</strong> You are building an internal AI assistant for Contoso Corporation. Employees can ask questions and the assistant answers based on the company's FAQ documents stored in SQL Server.\n\n<strong>What you will build:</strong>\n<ol><li>A <code>FAQ_Chunks</code> table with chunked FAQ content and embeddings</li><li>A stored procedure <code>sp_GetRAGAnswer</code> that takes a question and returns an AI-generated answer</li><li>A <code>FAQ_ConversationLog</code> table to track all Q&amp;A interactions</li><li>Test the system with 3 different questions</li></ol>\n\n<strong>Skills practiced:</strong> DocumentChunks design, batch embedding, prompt building, sp_invoke_external_rest_endpoint for both embedding and chat, JSON parsing, stored procedure creation."
                        },
                        {
                            "type": "sql_block",
                            "title": "Exercise Step 1 — Set Up FAQ Knowledge Base",
                            "scenario": "Create the FAQ_Chunks table and insert sample FAQ content (pre-chunked for simplicity in this exercise).",
                            "code": """-- Exercise Step 1: Create FAQ knowledge base

CREATE TABLE FAQ_Chunks (
    ChunkID         INT PRIMARY KEY IDENTITY(1,1),
    Topic           NVARCHAR(100),
    ChunkText       NVARCHAR(MAX) NOT NULL,
    ChunkEmbedding  VECTOR(1536),
    EmbeddingUpdated DATETIME2
);

-- Insert pre-chunked FAQ content (3 topics, 2 chunks each)
INSERT INTO FAQ_Chunks (Topic, ChunkText) VALUES

('Vacation Policy',
 'Full-time employees accrue 15 vacation days per year in their first 3 years. After 3 years of service, accrual increases to 20 days per year. Vacation days reset annually on January 1st. Unused days up to 5 may be carried over to the following year.'),

('Vacation Policy',
 'To request vacation, submit a request in the HR portal at least 2 weeks in advance. Your manager must approve the request. During blackout periods (fiscal year-end, December 15-31), vacation requests require VP approval.'),

('Remote Work',
 'Employees may work remotely up to 3 days per week with manager approval. All remote workers must be available during core hours of 10am-3pm in their local timezone. A reliable internet connection of at least 25 Mbps is required.'),

('Remote Work',
 'Remote work equipment including a laptop and monitor is provided by IT. Submit an equipment request through the IT portal. Home office stipend of $50/month is available for eligible employees after 6 months of employment.'),

('Expense Reimbursement',
 'Business expenses must be submitted within 30 days of incurrence. All expenses over $75 require a receipt. Meals during business travel are reimbursed up to $60 per day. Hotel stays must be booked through the corporate travel portal.'),

('Expense Reimbursement',
 'Submit expense reports through the Concur system. Include receipt images for all items over $75. Expense reports over $500 require additional VP approval. Reimbursements are processed in the next payroll cycle after approval.');

-- Verify
SELECT ChunkID, Topic, LEFT(ChunkText, 80) AS Preview FROM FAQ_Chunks;

PRINT 'FAQ_Chunks table created with 6 sample chunks.';""",
                            "explanation": "Creates the FAQ knowledge base with 6 pre-chunked FAQ items across 3 topics. In a real scenario, you would load these from source documents and chunk them automatically using the recursive CTE from Unit 3.",
                            "purpose": "Set up the FAQ data store for the RAG exercise.",
                            "breakdown": [
                                {"line": "Topic NVARCHAR(100)", "meaning": "A category column that enables pre-filtering. If a user asks about vacation, you can filter to Topic = 'Vacation Policy' before vector search."}
                            ],
                            "ssms_steps": [
                                "Open SSMS → New Query",
                                "Paste and run the CREATE TABLE and INSERT statements",
                                "Verify with the final SELECT — should show 6 rows with Topic and text preview",
                                "Note that ChunkEmbedding is NULL — you will populate this in Step 2"
                            ],
                            "exam_tip": "In the real DP-800 exam, you may be asked to identify which table design supports RAG retrieval. Look for: one row per chunk, a VECTOR column for embeddings, metadata columns for filtering, and a timestamp column for tracking embedding freshness."
                        },
                        {
                            "type": "sql_block",
                            "title": "Exercise Step 2 — Create the RAG Stored Procedure",
                            "scenario": "Create a stored procedure sp_GetRAGAnswer that takes a user's question and returns the AI-generated answer using the RAG pipeline.",
                            "code": """-- Exercise Step 2: Create the RAG stored procedure

CREATE OR ALTER PROCEDURE sp_GetRAGAnswer
    @Question   NVARCHAR(MAX),
    @TopicFilter NVARCHAR(100) = NULL   -- Optional: filter by topic
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @QueryVector    VECTOR(1536);
    DECLARE @ContextText    NVARCHAR(MAX) = '';
    DECLARE @SystemPrompt   NVARCHAR(MAX);
    DECLARE @UserMessage    NVARCHAR(MAX);
    DECLARE @ChatPayload    NVARCHAR(MAX);
    DECLARE @ChatResponse   NVARCHAR(MAX);
    DECLARE @ChatStatus     INT;
    DECLARE @EmbedResponse  NVARCHAR(MAX);
    DECLARE @EmbedStatus    INT;
    DECLARE @EmbedPayload   NVARCHAR(MAX);

    -- Step A: Embed the question
    SET @EmbedPayload = N'{"input": ' + (SELECT @Question FOR JSON PATH, WITHOUT_ARRAY_WRAPPER) + '}';
    EXEC sp_invoke_external_rest_endpoint
        @url        = 'https://YOUR-RESOURCE.openai.azure.com/openai/deployments/text-embedding-ada-002/embeddings?api-version=2023-05-15',
        @method     = 'POST',
        @headers    = N'{"Content-Type": "application/json", "api-key": "YOUR-API-KEY"}',
        @payload    = @EmbedPayload,
        @response   = @EmbedResponse OUTPUT,
        @statuscode = @EmbedStatus OUTPUT;

    IF @EmbedStatus <> 200
    BEGIN
        SELECT 'Error embedding question. HTTP status: ' + CAST(@EmbedStatus AS VARCHAR) AS Answer;
        RETURN;
    END

    SET @QueryVector = CAST(JSON_QUERY(@EmbedResponse, '$.result.data[0].embedding') AS VECTOR(1536));

    -- Step B: Retrieve top 3 relevant chunks
    SELECT TOP 3
        @ContextText = @ContextText + '[FAQ ' + CAST(ROW_NUMBER() OVER (ORDER BY VECTOR_DISTANCE('cosine', ChunkEmbedding, @QueryVector)) AS NVARCHAR(5)) + ']: ' + ChunkText + CHAR(10) + CHAR(10)
    FROM FAQ_Chunks
    WHERE
        ChunkEmbedding IS NOT NULL
        AND VECTOR_DISTANCE('cosine', ChunkEmbedding, @QueryVector) < 0.8
        AND (@TopicFilter IS NULL OR Topic = @TopicFilter)
    ORDER BY VECTOR_DISTANCE('cosine', ChunkEmbedding, @QueryVector) ASC;

    -- Handle no results found
    IF LEN(ISNULL(@ContextText, '')) = 0
    BEGIN
        SELECT
            @Question AS Question,
            'I could not find relevant information in our FAQ to answer this question. Please contact HR directly.' AS Answer;
        RETURN;
    END

    -- Step C: Build the augmented prompt
    SET @SystemPrompt = 'You are a helpful Contoso Corporation HR assistant. Answer the employee question based ONLY on the provided FAQ content. Be concise and friendly. If the FAQ content does not answer the question, say so.';
    SET @UserMessage  = 'FAQ CONTENT:' + CHAR(10) + @ContextText + 'EMPLOYEE QUESTION: ' + @Question;

    -- Step D: Call chat completion
    SET @ChatPayload = N'{"messages": [{"role": "system", "content": ' + (SELECT @SystemPrompt FOR JSON PATH, WITHOUT_ARRAY_WRAPPER) + '}, {"role": "user", "content": ' + (SELECT @UserMessage FOR JSON PATH, WITHOUT_ARRAY_WRAPPER) + '}], "temperature": 0, "max_tokens": 400}';

    EXEC sp_invoke_external_rest_endpoint
        @url        = 'https://YOUR-RESOURCE.openai.azure.com/openai/deployments/gpt-4/chat/completions?api-version=2024-02-01',
        @method     = 'POST',
        @headers    = N'{"Content-Type": "application/json", "api-key": "YOUR-API-KEY"}',
        @payload    = @ChatPayload,
        @response   = @ChatResponse OUTPUT,
        @statuscode = @ChatStatus OUTPUT;

    IF @ChatStatus <> 200
    BEGIN
        SELECT @Question AS Question, 'Error calling AI service. Please try again.' AS Answer;
        RETURN;
    END

    -- Step E: Return the answer
    SELECT
        @Question AS Question,
        JSON_VALUE(@ChatResponse, '$.result.choices[0].message.content') AS Answer,
        JSON_VALUE(@ChatResponse, '$.result.usage.total_tokens') AS TokensUsed;
END;

-- Test the procedure
EXEC sp_GetRAGAnswer @Question = 'How many vacation days do I get after 5 years?';
EXEC sp_GetRAGAnswer @Question = 'Can I work from home every day?';
EXEC sp_GetRAGAnswer @Question = 'What is the deadline to submit expense reports?';""",
                            "explanation": "This stored procedure encapsulates the complete RAG pipeline. Callers just provide a question (and optional topic filter) and receive the AI-generated answer. The procedure handles all the steps internally: embed → retrieve → build prompt → call LLM → parse response.",
                            "purpose": "Package the RAG pipeline as a reusable stored procedure that can be called by applications.",
                            "breakdown": [
                                {"line": "@TopicFilter NVARCHAR(100) = NULL", "meaning": "An optional parameter that allows callers to limit FAQ search to a specific topic. NULL = search all topics. This implements pre-filtering for targeted RAG."},
                                {"line": "AND (@TopicFilter IS NULL OR Topic = @TopicFilter)", "meaning": "Smart filter: when @TopicFilter is NULL, the condition is always TRUE (search all chunks). When a topic is specified, only chunks matching that topic are searched."}
                            ],
                            "ssms_steps": [
                                "First ensure FAQ_Chunks has embeddings (run the batch embedding from Unit 5 on FAQ_Chunks)",
                                "Paste the CREATE OR ALTER PROCEDURE code",
                                "Replace YOUR-RESOURCE and YOUR-API-KEY in both API calls",
                                "Press F5 to create the procedure",
                                "Test with the three EXEC statements at the bottom",
                                "Verify each returns a relevant, grounded answer based on the FAQ content",
                                "Try EXEC sp_GetRAGAnswer @Question = 'What is the stock price?' — it should say it cannot find relevant information"
                            ],
                            "exam_tip": "Wrapping the RAG pipeline in a stored procedure is a best practice: it encapsulates complexity, enables permission control (GRANT EXECUTE ON sp_GetRAGAnswer TO app_user), and makes it reusable across multiple applications."
                        }
                    ],
                    "quiz": [
                        {
                            "q": "What is the benefit of wrapping the RAG pipeline in a stored procedure?",
                            "opts": ["A. Stored procedures run faster than ad-hoc queries", "B. It encapsulates complexity, enables SQL permission control, and makes the pipeline reusable by multiple applications", "C. Stored procedures automatically cache embeddings", "D. It is required by Azure SQL Database for calling external APIs"],
                            "correct": "B",
                            "explain": "A stored procedure packages the entire RAG pipeline (embed → retrieve → build prompt → call LLM → parse response) behind a simple interface. Applications call sp_GetRAGAnswer(@Question) without knowing the internal complexity. SQL permissions can be granted on the procedure."
                        },
                        {
                            "q": "In sp_GetRAGAnswer, what does the @TopicFilter = NULL default parameter accomplish?",
                            "opts": ["A. It causes the procedure to skip topic filtering", "B. It makes the topic filter optional — when not provided, all FAQ chunks are searched regardless of topic", "C. It filters to only chunks where Topic IS NULL", "D. NULL is required as the default for NVARCHAR parameters"],
                            "correct": "B",
                            "explain": "The condition AND (@TopicFilter IS NULL OR Topic = @TopicFilter) is TRUE for all rows when @TopicFilter is NULL. This makes the parameter optional — callers who don't specify a topic search the entire knowledge base."
                        },
                        {
                            "q": "What should sp_GetRAGAnswer return when @ContextText is empty after the vector search?",
                            "opts": ["A. An empty result set", "B. An error with RAISERROR", "C. A user-friendly message like 'I could not find relevant information' without calling the LLM", "D. NULL"],
                            "correct": "C",
                            "explain": "When no relevant chunks are found, calling the LLM with empty context would waste API tokens and the LLM might hallucinate. The better pattern is to detect empty context early and return a helpful fallback message without making the LLM call."
                        },
                        {
                            "q": "A user asks 'What is the company stock price?' to sp_GetRAGAnswer. The FAQ_Chunks table has nothing about stock prices. What should happen?",
                            "opts": ["A. The procedure returns the current stock price from the internet", "B. The procedure returns the fallback message because no relevant FAQ chunks are found", "C. The LLM generates an answer using its training knowledge about the company", "D. The procedure crashes with an error"],
                            "correct": "B",
                            "explain": "Vector search will find no chunks with cosine distance < 0.8 for 'stock price' (since the FAQ has no such content). @ContextText remains empty, triggering the early return with the fallback message 'I could not find relevant information'."
                        },
                        {
                            "q": "After successfully testing sp_GetRAGAnswer, a developer wants to also log every question and answer to an audit table. Where in the procedure is the best place to add this logging?",
                            "opts": ["A. Before Step A (embedding)", "B. After Step E (after parsing the AI answer)", "C. Between Step B and C (after retrieval)", "D. Outside the stored procedure in the calling application"],
                            "correct": "B",
                            "explain": "The best place to log is after Step E when you have both the question (@Question) and the AI's answer (parsed from @ChatResponse). At that point you can INSERT both values, plus token usage, into an audit/log table."
                        }
                    ]
                },

                # ── Unit 7: Knowledge Check ───────────────────────────────
                {
                    "id": "lp3-m11-u7",
                    "title": "Knowledge Check",
                    "description": "Review and test your understanding of RAG with SQL.",
                    "estimated_time": 15,
                    "objectives": [
                        "Review key concepts from Module 11",
                        "Test understanding of the RAG architecture and T-SQL implementation"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Module 11 Key Concepts Review",
                            "body": "<strong>RAG Architecture (in order):</strong>\n<ol><li>Embed user question → VECTOR(1536)</li><li>Vector search / FTS / Hybrid to retrieve top-N chunks</li><li>Build augmented prompt: System + Context + Question</li><li>Call chat completion API (gpt-4 / gpt-35-turbo)</li><li>Parse $.result.choices[0].message.content</li><li>Return to user (optionally store in ConversationHistory)</li></ol>\n\n<strong>Chunking:</strong>\n<ul><li>Split documents into 200-500 word chunks</li><li>Use overlap (50-200 chars) to avoid boundary issues</li><li>Recursive CTE with OPTION (MAXRECURSION 1000) for long docs</li><li>Store one embedding per chunk in DocumentChunks table</li></ul>\n\n<strong>Prompt Design:</strong>\n<ul><li>System prompt must say: 'Answer based ONLY on the provided context'</li><li>Fallback: 'If context is insufficient, say so'</li><li>Use temperature=0 for factual RAG responses</li><li>Monitor total_tokens per call for cost management</li></ul>\n\n<strong>API Differences:</strong>\n<ul><li>Embedding API: /embeddings endpoint, input field, returns data[0].embedding</li><li>Chat API: /chat/completions endpoint, messages array, returns choices[0].message.content</li></ul>"
                        }
                    ],
                    "quiz": [
                        {
                            "q": "A RAG system returns an answer that sounds plausible but is factually incorrect. What is this called and what is the most likely cause?",
                            "opts": ["A. A compilation error — the SQL is incorrect", "B. A hallucination — the LLM generated information not grounded in the retrieved context, possibly because the system prompt lacked a 'context only' instruction", "C. A timeout — the API response took too long", "D. A chunking error — chunks were too small"],
                            "correct": "B",
                            "explain": "Hallucination is when an LLM generates plausible-sounding but incorrect information. In RAG, this often happens when the system prompt does not explicitly restrict the LLM to use only the provided context, allowing it to supplement with (potentially wrong) training knowledge."
                        },
                        {
                            "q": "What is the correct Azure OpenAI endpoint path for chat completion (vs embeddings)?",
                            "opts": ["A. /openai/deployments/MODEL/completions", "B. /openai/deployments/MODEL/chat/completions", "C. /openai/deployments/MODEL/generate", "D. /openai/deployments/MODEL/embeddings"],
                            "correct": "B",
                            "explain": "Chat completion uses /openai/deployments/MODEL/chat/completions. Embeddings use /openai/deployments/MODEL/embeddings. These are different endpoints with different request and response formats."
                        },
                        {
                            "q": "Which T-SQL function is used to extract a scalar value (like the AI answer text) from a JSON response?",
                            "opts": ["A. JSON_QUERY", "B. JSON_VALUE", "C. OPENJSON", "D. JSON_EXTRACT"],
                            "correct": "B",
                            "explain": "JSON_VALUE extracts a single scalar value (string, number, boolean) from JSON. For extracting the AI answer from $.result.choices[0].message.content (which is a string), use JSON_VALUE. Use JSON_QUERY for JSON objects or arrays."
                        },
                        {
                            "q": "In a multi-turn RAG conversation, what is the purpose of including 'assistant' role messages in the chat payload?",
                            "opts": ["A. Azure OpenAI requires at least one assistant message", "B. To give the LLM memory of its previous responses so it can maintain conversational context across turns", "C. Assistant messages replace the system prompt", "D. To reduce the number of retrieved context chunks needed"],
                            "correct": "B",
                            "explain": "Including previous 'assistant' messages in the messages array gives the LLM conversation memory. Without them, each call is stateless — the LLM does not know what was said in previous turns and cannot refer back to earlier parts of the conversation."
                        },
                        {
                            "q": "A company's RAG system uses gpt-35-turbo (4,096 token context window). The system prompt is 200 tokens, the retrieved context is 3,000 tokens, and the question is 50 tokens. How many tokens remain for the response?",
                            "opts": ["A. 846 tokens", "B. 3,846 tokens", "C. 4,096 tokens", "D. 0 tokens — the prompt already exceeds the context window"],
                            "correct": "A",
                            "explain": "Total input tokens = 200 (system) + 3000 (context) + 50 (question) = 3250 tokens. Remaining for response = 4096 - 3250 = 846 tokens. This is enough for a short answer but may truncate longer responses. Consider using gpt-4o (128K context) for larger context needs."
                        }
                    ]
                },

                # ── Unit 8: Summary ───────────────────────────────────────
                {
                    "id": "lp3-m11-u8",
                    "title": "Summary",
                    "description": "Review what you learned in Module 11 about RAG with SQL, and consolidate your Learning Path 3 knowledge.",
                    "estimated_time": 5,
                    "objectives": [
                        "Consolidate knowledge of the RAG pipeline",
                        "Review LP3 as a whole and how all three modules connect"
                    ],
                    "content": [
                        {
                            "type": "theory",
                            "title": "Module 11 Summary",
                            "body": "In this module you learned to build complete RAG solutions with SQL:\n\n<strong>RAG Fundamentals</strong>\n<ul><li>RAG grounds LLM responses in your private, current data from SQL</li><li>Solves the training cutoff and private data limitations of LLMs</li><li>Three steps: Retrieve → Augment → Generate</li></ul>\n\n<strong>Data Preparation</strong>\n<ul><li>Chunk long documents into 200-500 word pieces</li><li>Store chunks with metadata (Category, Date) for pre-filtering</li><li>Generate embeddings for each chunk using text-embedding-ada-002</li><li>Use recursive CTEs with OPTION (MAXRECURSION 1000) for chunking</li></ul>\n\n<strong>Retrieval</strong>\n<ul><li>Embed the user's question with the same model as stored chunks</li><li>Use VECTOR_DISTANCE with threshold filtering to find relevant chunks</li><li>Pre-filter with metadata WHERE conditions for better precision</li></ul>\n\n<strong>Prompt Building</strong>\n<ul><li>Combine system instructions, retrieved context, and user question</li><li>Always include: 'Answer based ONLY on the provided context'</li><li>Check token count before sending (LEN/4 estimate)</li></ul>\n\n<strong>Response Generation</strong>\n<ul><li>Call /chat/completions endpoint with temperature=0 for factual tasks</li><li>Parse response with JSON_VALUE(response, '$.result.choices[0].message.content')</li><li>Store conversation history for multi-turn chat</li><li>Monitor total_tokens for cost management</li></ul>"
                        },
                        {
                            "type": "theory",
                            "title": "Learning Path 3 Complete — How It All Connects",
                            "body": "Congratulations! You have completed Learning Path 3. Here is how the three modules build on each other:\n\n<strong>Module 9 (Embeddings)</strong> taught you:\n<ul><li>How to connect SQL to Azure OpenAI with credentials and external data sources</li><li>What embeddings are and how to store them in VECTOR columns</li><li>How to generate and maintain embeddings with triggers and batch jobs</li></ul>\n\n<strong>Module 10 (Intelligent Search)</strong> used those embeddings to:\n<ul><li>Find semantically similar documents with VECTOR_DISTANCE</li><li>Combine with full-text search for hybrid approaches</li><li>Rank results using Reciprocal Rank Fusion</li></ul>\n\n<strong>Module 11 (RAG)</strong> used that search capability to:\n<ul><li>Retrieve relevant context for user questions</li><li>Augment LLM prompts with database content</li><li>Generate grounded, accurate AI responses</li><li>Build complete enterprise AI assistant systems</li></ul>\n\n<strong>For the DP-800 exam:</strong>\n<ul><li>Know the setup order: Master Key → Credential → External Data Source</li><li>Know the VECTOR type, VECTOR_DISTANCE, and JSON paths for embedding responses</li><li>Know full-text search objects: FULLTEXT CATALOG, FULLTEXT INDEX, CONTAINS, FREETEXT, FREETEXTTABLE</li><li>Know the RAG prompt structure and the critical 'context only' instruction</li><li>Know that VECTOR and sp_invoke_external_rest_endpoint require Azure SQL / SQL Server 2025</li></ul>"
                        }
                    ],
                    "quiz": [
                        {
                            "q": "Which three modules make up Learning Path 3 of the DP-800 exam?",
                            "opts": ["A. Embeddings, Search, RAG", "B. Data Factory, Power BI, Azure SQL", "C. Spark, Delta Lake, Lakehouse", "D. Security, Governance, Compliance"],
                            "correct": "A",
                            "explain": "LP3 covers: Module 9 (Design and implement models and embeddings with SQL), Module 10 (Design and implement intelligent search with SQL), and Module 11 (Design and implement RAG with SQL). These three modules form the complete AI-enabled database solutions learning path."
                        },
                        {
                            "q": "What is the end-to-end value proposition of combining all LP3 skills (embeddings + search + RAG)?",
                            "opts": ["A. It allows SQL Server to replace Python for machine learning", "B. It enables you to build enterprise AI assistants that answer questions using your private SQL data, grounded by AI-powered semantic search", "C. It eliminates the need for Azure OpenAI entirely", "D. It converts SQL databases into vector databases"],
                            "correct": "B",
                            "explain": "Combining embeddings (Module 9), semantic search (Module 10), and RAG (Module 11) enables enterprise AI assistants that: understand natural language questions, find relevant information from your SQL databases using semantic search, and generate accurate, grounded answers using Azure OpenAI LLMs."
                        },
                        {
                            "q": "A colleague says they can build RAG without chunking — they will embed entire 20-page documents. What is wrong with this approach?",
                            "opts": ["A. Nothing — whole-document embeddings work fine for RAG", "B. 20-page documents exceed embedding model token limits, and the resulting embedding is too general to enable precise retrieval of specific facts within the document", "C. Azure SQL does not support VECTOR columns large enough for 20-page documents", "D. The VECTOR type only supports up to 1536 numbers, which is too few for long documents"],
                            "correct": "B",
                            "explain": "A 20-page document contains approximately 10,000 words = ~13,000 tokens, far exceeding the 8,191-token limit of ada-002. Even if it fit, the embedding would be a 'blurry' average of all topics in the document, making precise fact retrieval unreliable."
                        },
                        {
                            "q": "Which SQL Server feature enables calling Azure OpenAI APIs directly from T-SQL in all three LP3 modules?",
                            "opts": ["A. OPENROWSET", "B. LINKED SERVERS", "C. sp_invoke_external_rest_endpoint", "D. xp_cmdshell"],
                            "correct": "C",
                            "explain": "sp_invoke_external_rest_endpoint is the stored procedure used throughout LP3 to make HTTP calls to Azure OpenAI from T-SQL — for generating embeddings (Module 9), embedding search queries (Module 10), and calling chat completion APIs (Module 11)."
                        },
                        {
                            "q": "What are TWO things you must remember about VECTOR data type and sp_invoke_external_rest_endpoint for the DP-800 exam?",
                            "opts": ["A. They work on SQL Server 2019 and Azure SQL Database", "B. They require Azure SQL Database or SQL Server 2025, and sp_invoke_external_rest_endpoint requires IDENTITY='HTTPEndpointHeaders' in the credential for API key authentication", "C. They require a paid Azure AI Foundry subscription to use", "D. VECTOR columns have a maximum of 768 dimensions"],
                            "correct": "B",
                            "explain": "Two critical exam points: (1) VECTOR data type and sp_invoke_external_rest_endpoint are ONLY available in Azure SQL Database and SQL Server 2025 — not older SQL Server versions. (2) The DATABASE SCOPED CREDENTIAL must use IDENTITY = 'HTTPEndpointHeaders' for the API key to be sent correctly as an HTTP header."
                        }
                    ]
                }
            ]
        }
    ]
}
