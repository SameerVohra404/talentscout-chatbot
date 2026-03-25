# Prompt template for LLM usage
# (Used if API integration is enabled)

def generate_question_prompt(tech_stack):

    prompt = f"""
You are a technical interviewer.

Candidate skills:
{tech_stack}

Generate 3 interview questions for each skill.
Questions should be relevant and moderately difficult.
"""

    return prompt