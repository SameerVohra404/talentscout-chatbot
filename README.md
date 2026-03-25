# TalentScout Hiring Assistant Chatbot

## Project Overview

This project is a Streamlit-based Hiring Assistant chatbot designed for TalentScout's recruitment process.

The chatbot collects candidate information step-by-step and generates technical interview questions based on the candidate's declared tech stack.

The system simulates an AI-powered interviewer using prompt engineering and supports optional API-based LLM integration.

The chatbot maintains conversation state, validates user input, handles unexpected responses, and provides a clean chat-style UI.

---

## Features

- Chat-style UI using Streamlit chat components
- Stateful conversation flow
- Automatic greeting message
- Restart conversation button
- Input validation for user data
- Fallback responses for unexpected input
- Dynamic technical question generation
- Prompt-based design
- Safe handling of candidate information
- Optional AI API integration support

---

## Installation

Install dependencies

```
pip install -r requirements.txt
```

Run the app

```
streamlit run app.py
```

Open browser

```
http://localhost:8501
```

---

## Usage Guide

1. Launch the chatbot
2. Enter candidate details step-by-step
3. Provide tech stack (example: Python, SQL, React)
4. Chatbot generates technical questions
5. Type `exit` to stop
6. Use Restart button to start again

---

## Prompt Engineering

Prompt templates are stored in `prompts.py`.

Example prompt:

```
You are a technical interviewer.

Candidate skills:
Python, SQL

Generate 3 interview questions for each skill.
```

This allows the chatbot to dynamically generate questions for different technologies.

The design supports multiple tech stacks and ensures relevant interview questions are created.

---

## AI / LLM Integration (Optional)

The chatbot is designed to support AI APIs such as:

- Gemini API
- OpenAI API
- Local LLM

To enable API usage, create a `.env` file in the project folder:

```
GEMINI_API_KEY=your_api_key_here
```

The `.env` file is not included in this repository for security reasons.

If no API key is provided, the chatbot uses a built-in question generator.

---

## Input Validation

The chatbot validates user input to ensure realistic interaction.

Examples:

- Name must contain letters
- Email must contain @
- Phone must contain digits only
- Experience must be numeric
- Tech stack cannot be empty

If invalid input is entered, the chatbot asks again without breaking the flow.

---

## Fallback Mechanism

The chatbot provides safe fallback responses when:

- Unexpected input is entered
- Conversation step is finished
- Invalid data is provided

This ensures the chatbot does not deviate from its purpose.

Example fallback:

```
Technical questions already generated.
Type 'exit' to end or restart the chat.
```

---

## Technical Details

Libraries used:

- streamlit
- python-dotenv (optional)
- standard python

Project structure:

```
app.py        → UI
chatbot.py    → conversation logic
prompts.py    → prompt templates
requirements.txt
README.md
.gitignore
```

Conversation state is stored using:

```
st.session_state
```

This allows step-by-step interaction.

---

## Safety & Privacy

- No database used
- No real data stored
- No API keys included
- `.env` ignored using `.gitignore`
- All data exists only during session

This follows basic data privacy practices.

---

## Challenges & Solutions

Challenge:  
Managing conversation state in Streamlit

Solution:  
Used `st.session_state` to track steps and messages

Challenge:  
Handling invalid user input

Solution:  
Added validation functions for each field

Challenge:  
API quota errors during development

Solution:  
Implemented fallback question generator

Challenge:  
Making UI look like real chatbot

Solution:  
Used `st.chat_message` for chat-style layout

---

## Possible Improvements

- Real AI integration
- Database storage
- Resume upload
- Better UI styling
- Multi-role interview mode
- Scoring system

---

## Author

Sameer Vohra