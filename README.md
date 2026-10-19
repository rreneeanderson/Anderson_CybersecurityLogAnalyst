# Cybersecurity Log Analyst

This project is a Streamlit web application that uses a Large Language Model to analyze cybersecurity logs.

## Features

- Accepts server or security logs from the user
- Detects suspicious activity
- Assigns a risk level
- Explains why the activity may be suspicious
- Recommends investigation steps

## Technologies Used

- Python
- Streamlit
- LangChain
- Google Gemini / Gemma
- python-dotenv

## How It Works

1. The user pastes security logs into the Streamlit interface.
2. The logs are sent to the LLM.
3. The LLM analyzes the logs for suspicious patterns.
4. The application displays a risk report with recommendations.

## Run the Project

Install the required packages:

```bash
pip install -r requirements.txt