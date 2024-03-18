# 📚 Weekly Research Paper Summariser

  

Quickly finds latest research paper of user's chosen domain and generates summary according to user's current level of knowledge in **real-time** from publicly available research paper archives [arXiv | Cornell University](https://arxiv.org/).

  

## Demo

  

See how the tool works:

  

![Weekly Research Paper AI Summariser tool demo](assets/demo.gif)

  

The arXiv API is used to search latest research paper in user's chosen domain. You can see that the LLM App enables AI-powered summary for current and latest research paper pdfs (i.e. unstructured documents) of various subjects like physics, biology, computer science, etc. and indexes input data in real-time just after files are found and stored on local storage.

  

## How to run the tool

  

There are 3 ways to run the app:

  

### Run with Conda with a Linux VM or WSL (for windows users) or simply on linux/macOS terminal (for linux/macOS users)

  

1. Clone the repository on your system.

2. Create a .env file with following variables:

```bash

OPENAI_API_TOKEN={OPENAI_API_KEY}

HOST=0.0.0.0

PORT=8080

EMBEDDER_LOCATOR=text-embedding-ada-002

EMBEDDING_DIMENSION=1536

MODEL_LOCATOR=gpt-3.5-turbo

MAX_TOKENS=200

TEMPERATURE=0.0

RESEARCH_PAPER_FOLDER_PATH={REPLACE_WITH_RESEARCH_PAPER_RELATIVE_PATH}

```
3. From the project root folder, open your terminal and run `WSL` if you will be using it.
 
4. Create a conda environment 

5. Activate the conda environment

6. Install the app dependencies

Install the required packages:
```bash

pip  install  --upgrade  -r  requirements.txt

```

7. Run the Pathway API

You start the application by running `main.py`:
```bash

python  main.py

```
8. Run Streamlit UI

You can run the UI separately by running Streamlit app

`streamlit run ui.py` command. It connects to the Pathway's backend API automatically and you will see the UI frontend is running on your browser.


  

### Run with Docker

  

1. Create `.env` file in the root directory of the project, copy and paste the below config. Replace the `OPENAI_API_TOKEN` configuration value with your key `{OPENAI_API_KEY}` and replace `RESEARCH_PAPER_LOCAL_FOLDER_PATH` with a path where Research Paper folder is located `{REPLACE_WITH_RESEARCH_PAPER_FOLDER_PATH}`.  Other properties are optional to change and be default.

  

```bash

OPENAI_API_TOKEN={OPENAI_API_KEY}

HOST=0.0.0.0

PORT=8080

EMBEDDER_LOCATOR=text-embedding-ada-002

EMBEDDING_DIMENSION=1536

MODEL_LOCATOR=gpt-3.5-turbo

MAX_TOKENS=200

TEMPERATURE=0.0

RESEARCH_PAPER_FOLDER_PATH={REPLACE_WITH_RESEARCH_PAPER_RELATIVE_PATH}

```

  

2. From the project root folder, open your terminal and run `docker compose up`.

3. Navigate to `localhost:8501` on your browser when docker installion is successful.

  

### Run from the source

  

#### Prerequisites

  

1. Make sure that [Python](https://www.python.org/downloads/) 3.10 or above installed on your machine.

2. Download and Install [Pip](https://pip.pypa.io/en/stable/installation/) to manage project packages.

3. Create an [OpenAI](https://openai.com/) account and generate a new API Key: To access the OpenAI API, you will need to create an API Key. You can do this by logging into the [OpenAI website](https://openai.com/product) and navigating to the API Key management page.

  

Then, follow the easy steps to install and get started using the app.

  

#### Step 1: Clone the repository

  



  

Next, navigate to the project folder:

  

```bash

cd  Weekly-Research-Paper-Summariser

```

  

#### Step 2: Set environment variables

  

Create `.env` file in the root directory of the project, copy and paste the below config, and replace the `{OPENAI_API_KEY}` configuration value with your key.

  

```bash

OPENAI_API_TOKEN={OPENAI_API_KEY}

HOST=0.0.0.0

PORT=8080

EMBEDDER_LOCATOR=text-embedding-ada-002

EMBEDDING_DIMENSION=1536

MODEL_LOCATOR=gpt-3.5-turbo

MAX_TOKENS=200

TEMPERATURE=0.0

RESEARCH_PAPER_FOLDER_PATH={REPLACE_WITH_RESEARCH_PAPER_RELATIVE_PATH}

```

  

Replace RESEARCH_PAPER_FOLDER_PATH with your local Research Paper folder path and optionally, you customize other values.

  

#### Step 3 (Optional): Create a new virtual environment

  

Create a new virtual environment in the same folder and activate that environment:

  

```bash

python  -m  venv  pw-env && source  pw-env/bin/activate

```

  

#### Step 4: Install the app dependencies

  

Install the required packages:

  

```bash

pip  install  --upgrade  -r  requirements.txt

```

  

#### Step 5: Run the Pathway API

  

You start the application by running `main.py`:

  

```bash

python  main.py

```

  

#### Step 6: Run Streamlit UI

  

You can run the UI separately by running Streamlit app

`streamlit run ui.py` command. It connects to the Pathway's backend API automatically and you will see the UI frontend is running on your browser.
