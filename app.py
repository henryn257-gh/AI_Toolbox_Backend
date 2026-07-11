from fastapi import FastAPI

from database.database import (
    setup_database
)

from ai.router import (
    ask_ai
)



app = FastAPI(
    title="AI Toolbox Backend",
    version="1.0.0"
)



setup_database()



@app.post("/ai")
async def ai_endpoint(
    data: dict
):


    answer = ask_ai(

        data.get(
            "provider",
            "gemini"
        ),

        data.get(
            "system_prompt",
            ""
        ),

        data.get(
            "user_prompt",
            ""
        )

    )


    return {

        "success": True,

        "answer": answer

    }




@app.get("/download")
async def download_endpoint(
    type: str,
    name: str
):


    return {

        "success": True,

        "message":
        "Download system ready",

        "type": type,

        "name": name

    }
