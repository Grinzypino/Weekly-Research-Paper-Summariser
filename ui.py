import os
import streamlit as st
import requests
from dotenv import load_dotenv
import arxiv

#Defining find_pdf function which stores the searched pdf from arXiv
def find_pdf(url, filename, folder_path):
  
  # Sends HTTP GET request to the URL
  response = requests.get(url)

  # Joins the folder path with the filename
  filepath = os.path.join(folder_path, filename)
    
  # Checks if the request was successful (status code 200)
  if response.status_code == 200:
      # Opens a file in binary write mode and save the content of the response
      with open(filepath, 'wb') as f:
          f.write(response.content)
      print(f"Searched PDF stored successfully as '{filename}'")
  else:
      print(f"Failed to find and store PDF. Status code: {response.status_code}")



with st.sidebar:
    st.markdown(
        "## How to use\n"
        "1. Choose the topic of latest research paper you want.\n"
        "2. Hit the find button.\n"
        "3. Choose your level of expertise in that topic.\n"
        "4. Hit the summarise button.\n"
    )
    st.markdown("---")
    st.markdown("# About")
    st.markdown(
        "AI app to get the summarised version of latest Research Paper of user's chosen topic from archives of top universities [arXiv | Cornell University](https://arxiv.org/) which is tailored to the user's current knowledge level. \n"
        "It uses Pathway’s [LLM App features](https://github.com/pathwaycom/llm-app) "
        "to build real-time LLM-enabled data pipeline in Python and join data from online APIs\n"

    )
    st.markdown("[View the source code on GitHub](https://github.com/Grinzypino/Weekly-Research-Paper-Summariser)

# Load environment variables
load_dotenv()
api_host = os.environ.get("HOST", "0.0.0.0")
api_port = int(os.environ.get("PORT", 8080))

# Streamlit UI elements
st.title("Weekly Research Paper Summariser📚")

topic = st.selectbox(
    'Choose the topic of latest paper you want:',
    ('Physics','Chemistry','Biology','Mathematics','Computer Science'),
    placeholder="Choose an option"
)

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

finder = st.button(
    "Find Research Papers",
    on_click=click_button,
    disabled=not topic
)

#/////////////////////////Finding Research Papers/////////////////////////////
if finder:

    # Constructing the default arXiv API client.
    client = arxiv.Client()

    # Searching for most recent articles matching the topic chosen by user
    search = arxiv.Search(
        query = topic,
        max_results = 1,
        sort_by = arxiv.SortCriterion.SubmittedDate
    )

    # Starts progress bar
    progress_bar = st.progress(0, "Finding latest research paper. Please wait.")

    for r in client.results(search):
        url = r.pdf_url
        name = r.title
        filename = f'{name}.pdf'
        folder_path = os.environ.get("RESEARCH_PAPER_FOLDER_PATH", "./docs")
        find_pdf(url, filename, folder_path)
    
    # Finishes progress bar when done
    progress_bar.progress(1.0, 'Latest research paper found successfully!')

#/////////////////////////Finding Research Papers/////////////////////////////
    

#Streamlit UI elements:
level = st.selectbox(
    'Choose the level of expertise you currently have:',
    ('Beginner', 'Intermediate', 'Expert'),
    placeholder="Choose an option",
    disabled=not st.session_state.clicked
)

generator = st.button(
    "Summarise Research Papers", 
    type="primary",
    disabled=not level
)



# Handling Summarise API request if level is selected and generator is hit
if level and generator:

    url = f'http://{api_host}:{api_port}/'
    data = {"query": f'Give the title and summary of the given paper to explain someone with {level} level of knowledge in {topic}'}

    response = requests.post(url, json=data)

    if response.status_code == 200:
        st.write("### Answer")
        st.write(response.json())
    else:
        st.error(f"Failed to send data to Summarise API. Status code: {response.status_code}")
