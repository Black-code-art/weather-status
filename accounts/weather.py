import requests
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())



def process_weather(query):

    url = f"{os.getenv('URL')}?q={query}&key={os.getenv('WEATHER_KEY')}"

    r = requests.get(url)

    if r.status_code == 200:


        return r.json(), True
    else:

        return {"message": "An error occured"}, False
