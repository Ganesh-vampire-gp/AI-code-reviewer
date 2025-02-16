# AI Code Reviewer

## Overview
This application is an AI-powered code reviewer for Python programming. It uses Google's Generative AI to analyze Python code for errors, potential bugs, and areas for improvement. The AI checks for syntax errors, logical errors, performance optimizations, code readability, and security vulnerabilities.

## Features
- Syntax error detection
- Logical error detection
- Performance optimization suggestions
- Code readability improvements
- Security vulnerability checks

## Usage
1. **Install Dependencies**: Ensure you have the required Python packages installed.
    ```bash
    pip install streamlit google-generativeai
    ```

2. **Run the Application**: Execute the Streamlit app.
    ```bash
    streamlit run /c:/Users/GANESH/OneDrive/Desktop/AI-code-reviewer/AI_app.py
    ```

3. **Enter Python Code**: In the web interface, enter your Python code in the provided text area.

4. **Generate Review**: Click the "Generate" button to receive the AI-generated code review.

## Configuration
- **API Key**: The application requires a Google Generative AI API key. Configure it in the `AI_app.py` file.
    ```python
    ai.configure(api_key="YOUR_API_KEY_HERE")
    ```

## Example
```python
# Example Python code to review
def add(a, b):
    return a + b

print(add(2, 3))
```

## License
This project is licensed under the MIT License.

## Acknowledgements
- [Streamlit](https://streamlit.io/)
- [Google Generative AI](https://cloud.google.com/generative-ai)
