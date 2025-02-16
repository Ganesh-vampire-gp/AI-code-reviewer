import logging 
# Set logging level to ERROR for streamlit to avoid unnecessary logs
logging.getLogger('streamlit').setLevel(logging.ERROR)
import streamlit as st
import google.generativeai as ai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
API_KEY = os.getenv("API_KEY")

# Check if API_KEY is available
if not API_KEY:
    raise ValueError("API_KEY not found. Please set it in the .env file.")

# Configure the Google Generative AI with the provided API key
ai.configure(api_key=API_KEY)

# Define the system prompt for the AI model
system_prompt = """
You are a helpful AI code reviewer for Python programming.

Users will provide Python code, and your task is to analyze it for errors, potential bugs, and areas for improvement.
You should check for:
Syntax errors (invalid syntax, missing colons, indentation issues, etc.)
Logical errors (incorrect calculations, incorrect condition checks, infinite loops)
Performance optimizations (reducing time complexity, avoiding unnecessary computations)
Code readability (following PEP 8 standards, proper variable naming, comments)
Security vulnerabilities (unsafe eval usage, hardcoded secrets, SQL injections)
If errors are found, explain each issue clearly and provide a corrected code snippet.
If there are areas for improvement (e.g., more efficient algorithms, better structuring), suggest optimizations with explanations.
Handling Student Questions:
If the user asks about Python for data science (e.g., pandas, NumPy, scikit-learn), answer normally.
If the question is outside Python programming (e.g., general data science, statistics, AI theory), politely decline and guide them to ask Python-related programming questions instead.
"""

# Initialize the AI model with the system prompt
model = ai.GenerativeModel(model_name="models/gemini-1.5-pro-latest", system_instruction=system_prompt)

# Display the title of the Streamlit app
st.markdown("## 💬 **An AI Code Reviewer**")
# st.title("AN AI Code Reviewer")

# Create a text area for the user to input their Python code
user_prompt = st.text_area("Enter your Python code here:", placeholder="Type Your code here..")

# Create a button for generating the AI response
btn_click = st.button("Generate")

# If the button is clicked, generate the AI response and display it
if btn_click == True:
    response = model.generate_content(user_prompt)
    st.markdown(response.text)
