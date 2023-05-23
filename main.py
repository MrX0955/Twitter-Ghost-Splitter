import os
import platform
import requests as mrx
from pystyle    import Colors, Colorate


def clear(): os.system('cls' if platform.system() == 'Windows' else 'clear')


class main:
    def __init__(self):
        clear()
        print(Colorate.Horizontal(Colors.purple_to_blue, "Enter Username: ", 1))
        self.query = input().strip()
        clear()
        self.url = "https://api.twitter.com/1.1/guest/activate.json"
        self.headers = {
            "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"
        }

    def get_gt(self):
        req = mrx.post(self.url, headers=self.headers)
        return req.json()["guest_token"]

    def split(self):
        splitter = mrx.get(
            f"https://twitter.com/i/api/1.1/search/typeahead.json?include_ext_is_blue_verified=1&include_ext_verified_type=1&q={self.query}&src=search_box&result_type=events%2Cusers%2Ctopics",
            headers={
                "Authorization": f"Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
                "x-guest-token": self.get_gt()})
        if splitter.json()["num_results"] > 0:
            print(Colorate.Horizontal(Colors.white_to_green, "\n<-- Non Ghost Account Informations -->", 3))
            print(" >> Username: ", splitter.json()["users"][0]["screen_name"], "\n",
                  ">> Verified: ", splitter.json()["users"][0]["verified"], "\n",
                  ">> Blue Tick: ", splitter.json()["users"][0]["ext_is_blue_verified"], "\n",
                  ">> Blocked: ", splitter.json()["users"][0]["is_blocked"], "\n",
                  ">> Badges: ", splitter.json()["users"][0]["badges"], )
        elif splitter.json()["num_results"] == 0:
            print(Colorate.Horizontal(Colors.yellow_to_red, f"Ghost Account >> {self.query}", 2))


main().split()
