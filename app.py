from fastapi import FastAPI

from database.database import (
    setup_database
)

from ai.router import (
    ask_ai
)

from fastapi.responses import Response

from github.downloader import download

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
    path: str
):

    data = download(
        path
    )

    return Response(
        content=data,
        media_type="application/json; charset=utf-8"
    )
