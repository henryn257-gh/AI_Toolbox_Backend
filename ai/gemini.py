from google import genai

from config.settings import (
    GEMINI_API_KEY,
    DEFAULT_MODEL
)


client = genai.Client(
    api_key=GEMINI_API_KEY
)


def ask_gemini(
    system_prompt,
    user_prompt
):

    response = client.models.generate_content(
        model=DEFAULT_MODEL,

        contents=user_prompt,

        config={
            "system_instruction": system_prompt
        }
    )


    return response.text
