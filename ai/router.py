from ai.gemini import ask_gemini



def ask_ai(
    provider,
    system_prompt,
    user_prompt
):


    if provider == "gemini":

        return ask_gemini(
            system_prompt,
            user_prompt
        )


    return "Provider not supported"
