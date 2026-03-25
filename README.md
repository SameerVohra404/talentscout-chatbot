# TalentScout Hiring Assistant Chatbot

## Project Overview

TalentScout Hiring Assistant is a Streamlit-based chatbot that simulates an intelligent hiring assistant.
The chatbot collects candidate details step-by-step and generates technical interview questions based on the candidate’s declared tech stack.

The project demonstrates conversational flow design, prompt engineering, input validation, fallback handling, and optional AI integration.
The chatbot is deployed on Streamlit Cloud and the full source code is available in this repository.

---

## Live Demo

Streamlit Cloud App:

https://talentscout-chatbot-assignment.streamlit.app/

---

## Demo Video

Loom Walkthrough:

https://www.loom.com/share/3aaaaafe32474e97b6680c0ca5b5e1da

---

## Features

* Step-by-step candidate information collection
* Chat-style UI using Streamlit
* Input validation for all fields
* Dynamic technical question generation
* Prompt engineering for multiple tech stacks
* Fallback mechanism for unexpected input
* Stateful conversation using session memory
* Restart conversation option
* Secure API key handling using `.env`
* Clean and interactive UI
* Cloud deployment using Streamlit

---

## Installation Instructions

Clone the repository:

git clone https://github.com/SameerVohra404/talentscout-chatbot.git

Go to project folder:

cd talentscout-chatbot

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

Open in browser:

http://localhost:8501

---

## Usage Guide

1. Start the chatbot
2. Enter your name
3. Enter email address
4. Enter phone number
5. Enter years of experience
6. Enter desired position
7. Enter current location
8. Enter tech stack (example: Python, SQL, React)
9. Chatbot generates technical interview questions

The chatbot validates every input before moving to the next step.

---

## Technical Details

Libraries used:

* streamlit
* python-dotenv
* re (regex validation)
* optional LLM API support

Project Structure:

app.py → UI and session state
chatbot.py → conversation logic
prompts.py → prompt templates
requirements.txt → dependencies
.env → API key storage (not uploaded)
.gitignore → ignores sensitive files

Session state is managed using:

st.session_state

---

## Prompt Design

Prompt engineering is used to generate technical interview questions based on the tech stack.

Rules used in prompt:

* Generate questions only for given technologies
* Do not generate generic interview questions
* Keep questions short and clear
* One question per line
* Support multiple technologies

Example prompt:

Generate 2 technical interview questions for each technology.
Return only questions, each on a new line.
Tech stack: Python, SQL

---

## Fallback Mechanism

The chatbot handles unexpected input using validation and safe responses.

Examples:

Invalid name → ask again
Invalid email → ask again
Invalid phone → ask again
Empty input → ask again
Unknown input → fallback message

The chatbot always stays within the hiring assistant purpose.

---

## Input Validation

Validation rules:

Name → letters only
Email → regex format check
Phone → digits only
Experience → numeric only
Tech stack → must not be empty

This ensures realistic chatbot behavior.

---

## Sensitive Data Handling

API keys are not stored in the code.

To enable AI features, create `.env` file:

API_KEY=your_api_key

The `.env` file is ignored using `.gitignore`.

Users must provide their own API key.

---

## Optional AI Integration

The chatbot can use an LLM to generate questions.

If API key is available → AI used
If not available → fallback questions used

This ensures the chatbot always works.

---

## UI Enhancements

* Chat bubble layout
* Restart button
* Greeting message
* Error messages for invalid input
* Clean spacing
* Scrollable chat history

Streamlit is used for UI.

---

## Performance

* Lightweight app
* No database required
* Fast responses
* Uses session state for efficiency

---

## Version Control

Git was used for version control.

Repository:

https://github.com/SameerVohra404/talentscout-chatbot

---

## Challenges & Solutions

API errors → added fallback generator
Invalid input → added validation
Session reset issues → used session_state
API key security → used .env file
UI readability → improved layout
Deployment → used Streamlit Cloud

---

## Author

Sameer Vohra

GitHub:
https://github.com/SameerVohra404

---

## Conclusion

This project demonstrates:

* Prompt engineering
* Chatbot conversation design
* Input validation
* Fallback handling
* Secure API usage
* Streamlit UI
* Cloud deployment
* Version control
* Live demo + video demo

All assignment requirements have been implemented successfully.
