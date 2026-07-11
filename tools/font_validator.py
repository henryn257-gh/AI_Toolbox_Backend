import json


REQUIRED_FIELDS = [
    "id",
    "name",
    "version",
    "coverage",
    "characters"
]


def validate_font(font):

    errors = []

    # Required fields
    for field in REQUIRED_FIELDS:
        if field not in font:
            errors.append(
                f"Missing field: {field}"
            )

    # Characters
    if "characters" in font:

        if not isinstance(
            font["characters"],
            dict
        ):
            errors.append(
                "characters must be an object"
            )

        else:
            for key, value in font["characters"].items():

                if len(key) != 1:
                    errors.append(
                        f"Invalid character key: {key}"
                    )

                if not isinstance(
                    value,
                    str
                ):
                    errors.append(
                        f"Invalid replacement for {key}"
                    )

    return errors



def validate_file(path):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        font = json.load(file)

    return validate_font(font)



if __name__ == "__main__":

    result = validate_file(
        "font.json"
    )

    if result:
        print("FAILED")

        for error in result:
            print("-", error)

    else:
        print("VALID FONT")
