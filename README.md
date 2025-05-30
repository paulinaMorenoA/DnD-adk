# DunDra - D&D Campaign Publisher

DunDra is a project designed to assist in generating HTML pages for Dungeons & Dragons mini-campaigns, including the campaign story and detailed character sheets.

## Setup

### 1. Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/paulinaMorenoA//DnD-adk.git
cd DnD-adk 
```

### 2. Create and Activate a Virtual Environment
It is recommended to use a virtual environment to manage project dependencies.

**On macOS and Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies
Install the required Python packages using pip:
```bash
pip install -r requirements.txt
```

### 4. **Configuration**

Set up Google Cloud credentials.

You may set the following environment variables in your shell, or in
   a `.env` file instead.

   ```bash
   export GOOGLE_GENAI_USE_VERTEXAI=true
   export GOOGLE_CLOUD_PROJECT=<your-project-id>
   export GOOGLE_CLOUD_LOCATION=<your-project-location>
   export MODEL_NAME =gemini-2.0-flash-001 # Change as needed 
   export OPENAI_API_KEY=<your-openai-api-key>
   ```

Authenticate your GCloud account.

   ```bash
   gcloud auth application-default login
   gcloud auth application-default set-quota-project $GOOGLE_CLOUD_PROJECT
   ```
### 5. Architecture
![DnD Multi-Agent](dnd_diagram.jpg)

## 6. Running the Agent

You can run the agent using the ADK command in your terminal.
from the working directory:

1.  Run agent in CLI:

    ```bash
    adk run dundra
    ```

2.  Run agent with ADK Web UI:
    ```bash
    adk web
    ```
    Select the dundra from the dropdown

