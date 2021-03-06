import json
import requests

from flask import Flask

import modules.webscrapGet as wG


app = Flask(__name__)
default_text = "Despicable Me"


@app.route("/", methods=["GET"])
def root() -> str :
    """Get a random joke about our lord Chuck Norris.

    Returns:
        str: The joke about our lord Chuck Norris
    """

    response = requests.get("https://api.chucknorris.io/jokes/random")
    joke = json.loads(response.text)["value"]

    return joke



@app.route("/get-ascii/<style>", defaults={"character_width": "default", "character_height": "default", "text": default_text})
@app.route("/get-ascii/<style>/<character_width>", defaults={"character_height": "default", "text": default_text})
@app.route("/get-ascii/<style>/<character_width>/<character_height>", defaults={"text": default_text})
@app.route("/get-ascii/<style>/<character_width>/<character_height>/<text>", methods=['GET'])
def get_ascii(style : str, character_width : str, character_height : str, text : str) -> str :
    """Function that permit to get ASCII from website

    Args:
        text_style (str): the text style you want
        character_width (str): the character width
        character_height (str): the character height
        text (str): the text you want to convert to ASCII art

    Returns:
        str: ASCII art got from the website
    """

    return wG.generate_ascii(
        style=style,
        character_width=character_width,
        character_height=character_height,
        text=text
    )


app.run(debug=True)
