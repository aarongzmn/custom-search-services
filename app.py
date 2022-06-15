import platform
import requests
import unicodedata
from flask import Flask, redirect, render_template

app = Flask(__name__)


@app.route("/baseball-savant/<player_name>")
def baseball_savant(player_name):
    root_url = "https://baseballsavant.mlb.com"
    player_name = remove_accents(player_name)
    player_search = root_url + f"/player/search-all?search={player_name}"

    try:
        r = requests.get(player_search)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    search_results = r.json()
    if len(search_results) == 1:
        result_name = search_results[0]["name"]
        result_name = remove_accents(player_name).replace(" ", "-")
        player_id = search_results[0]["id"]
        statcast_url = root_url + f"/savant-player/{result_name}-{player_id}"
        return redirect(statcast_url, code=302)
    else:
        return redirect(root_url, code=302)


@app.route("/yahoo-baseball/")
@app.route("/yahoo-baseball/<player_name>")
def yahoo_baseball(player_name):
    root_url = "https://sports.yahoo.com"
    # player_search = root_url + f"/site/api/resource/sports.league.playerssearch;count=10;league=mlb;name={player_name}"
    return redirect(root_url + "/mlb/players/", code=302)


@app.route("/")
def home():
    return render_template("about.html")


def remove_accents(text):
    nfkd_text = unicodedata.normalize("NFKD", text)
    ascii_text = nfkd_text.encode("ASCII", "ignore").decode()
    return ascii_text


if __name__ == "__main__":
    """Checks operating system.
    If Windows, it runs the app in dev/debug mode.
    If Linux, it runs in production mode.
    """
    os_type = platform.system()
    if os_type == "Windows":
        app.run(debug=True, host="localhost", port=8080)
    elif os_type == "Linux":
        app.run(debug=False, host="0.0.0.0", port=8080)
