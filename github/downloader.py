import requests



def download_from_github(url):

    response = requests.get(
        url
    )


    response.raise_for_status()


    return response.content
