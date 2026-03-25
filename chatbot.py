from prompts import generate_question_prompt


# -----------------------------
# Generate technical questions
# -----------------------------
def generate_questions(tech_stack):

    try:
        techs = tech_stack.split(",")

        questions = []

        for t in techs:

            t = t.strip()

            questions.append(f"What is {t} used for?")
            questions.append(f"Explain one advanced concept in {t}.")
            questions.append(f"How is {t} used in real-world projects?")

        return "\n\n".join(questions)

    except:
        return "Could not generate questions. Please enter valid tech stack."


# -----------------------------
# Validators
# -----------------------------

def is_valid_name(text):
    return text.replace(" ", "").isalpha()


def is_valid_email(text):
    return "@" in text and "." in text


def is_valid_phone(text):
    return text.isdigit()


def is_valid_number(text):
    return text.isdigit()


def is_valid_tech(text):
    return len(text.strip()) > 0


# -----------------------------
# Main chatbot logic
# -----------------------------
def get_response(user_input, state):

    if user_input.lower() in ["exit", "quit", "bye"]:
        state["step"] = 999
        return "Thank you for using TalentScout Hiring Assistant."

    # Step 0
    if state["step"] == 0:

        state["step"] = 1

        return (
            "Hello, I am TalentScout Hiring Assistant.\n\n"
            "What is your full name?"
        )

    # Step 1 — name
    elif state["step"] == 1:

        if not is_valid_name(user_input):
            return "Please enter a valid name."

        state["name"] = user_input
        state["step"] = 2

        return "Please enter your email address."

    # Step 2 — email
    elif state["step"] == 2:

        if not is_valid_email(user_input):
            return "Please enter a valid email address."

        state["email"] = user_input
        state["step"] = 3

        return "Please enter your phone number."

    # Step 3 — phone
    elif state["step"] == 3:

        if not is_valid_phone(user_input):
            return "Phone number should contain only digits."

        state["phone"] = user_input
        state["step"] = 4

        return "How many years of experience do you have?"

    # Step 4 — experience
    elif state["step"] == 4:

        if not is_valid_number(user_input):
            return "Please enter number of years as digits."

        state["experience"] = user_input
        state["step"] = 5

        return "What position are you applying for?"

    # Step 5 — position
    elif state["step"] == 5:

        if len(user_input.strip()) == 0:
            return "Please enter a valid position."

        state["position"] = user_input
        state["step"] = 6

        return "What is your current location?"

    # Step 6 — location
    elif state["step"] == 6:

        if len(user_input.strip()) == 0:
            return "Please enter a valid location."

        state["location"] = user_input
        state["step"] = 7

        return "Enter your tech stack (example: Python, SQL, React)"

        # Step 7 — tech stack
    elif state["step"] == 7:

        if not is_valid_tech(user_input):
            return "Please enter at least one technology."

        state["tech"] = user_input
        state["step"] = 8

        questions = generate_questions(user_input)

        return (
            "Here are your technical questions:\n\n"
            + questions
        )

    # After questions generated
    elif state["step"] >= 8:

        return (
            "Technical questions already generated.\n\n"
            "Type 'exit' to end or press Restart to begin again."
        )

    # fallback
    else:
        return "Please enter a valid response."