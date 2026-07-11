import google.generativeai as genai

from config.settings import (
    GEMINI_API_KEY,
    DEFAULT_MODEL
)


genai.configure(
    api_key=GEMINI_API_KEY
)


def ask_gemini(
    system_prompt,
    user_prompt
):

    model = genai.GenerativeModel(
        DEFAULT_MODEL,
        system_instruction=system_prompt
    )


    response = model.generate_content(
        user_prompt
    )


    return response.text
