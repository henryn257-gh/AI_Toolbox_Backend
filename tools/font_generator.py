import json


def create_font(
    font_id,
    name,
    characters,
    output
):

    font = {

        "id": font_id,

        "name": name,

        "version": 1,

        "coverage": {

            "latin": True,

            "numbers": True,

            "symbols": True,

            "greek": "partial",

            "emoji": False

        },

        "characters": characters

    }


    with open(
        output,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            font,
            file,
            ensure_ascii=False,
            indent=4
        )


if __name__ == "__main__":

    create_font(

        "example",

        "Example Font",

        {
            "A":"𝐀",
            "B":"𝐁"
        },

        "example.json"
    )
