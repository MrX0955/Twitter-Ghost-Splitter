import os
import platform
import requests as mrx
from pystyle import Colors, Colorate


def clear(): os.system('cls' if platform.system() == 'Windows' else 'clear')


class main:
    def __init__(self):
        clear()
        print(Colorate.Horizontal(Colors.purple_to_blue, "Enter Username: ", 1))
        self.query = input().strip()
        clear()
        self.url = "https://api.twitter.com/1.1/guest/activate.json"
        self.headers = {
            "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs"
                             "%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"
        }

    def get_gt(self):
        req = mrx.post(self.url, headers=self.headers)
        return req.json()["guest_token"]

    def split(self):
        url = f"https://api.twitter.com/graphql/NimuplG1OB7Fd2btCLdBOw/UserByScreenName?variables={{\"screen_name\":\"{self.query}\",\"withSafetyModeUserFields\":true}}&features={{\"hidden_profile_likes_enabled\":true,\"hidden_profile_subscriptions_enabled\":true,\"responsive_web_graphql_exclude_directive_enabled\":true,\"verified_phone_label_enabled\":false,\"subscriptions_verification_info_is_identity_verified_enabled\":true,\"subscriptions_verification_info_verified_since_enabled\":true,\"highlights_tweets_tab_ui_enabled\":true,\"responsive_web_twitter_article_notes_tab_enabled\":false,\"creator_subscriptions_tweet_preview_api_enabled\":true,\"responsive_web_graphql_skip_user_profile_image_extensions_enabled\":false,\"responsive_web_graphql_timeline_navigation_enabled\":true}}&fieldToggles={{\"withAuxiliaryUserLabels\":false}}"
        splitter = mrx.get(
            url,
            headers={
                "Authorization": f"Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs"
                                 f"%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
                "x-guest-token": self.get_gt()})
        print(splitter.json())
        try:
            if splitter.json()["data"]["user"]["result"]["__typename"] == "User":
                print(Colorate.Horizontal(Colors.white_to_green, "\n<-- Non Ghost Account Informations -->", 3))
                print(" >> Username: ", splitter.json()["data"]["user"]["result"]["legacy"]["screen_name"], "\n",
                      ">> Nickname: ", splitter.json()["data"]["user"]["result"]["legacy"]["name"], "\n",
                      ">> Blue Tick: ", splitter.json()["data"]["user"]["result"]["is_blue_verified"], "\n", )

            elif splitter.json()["data"]["user"]["result"]["__typename"] == "UserUnavailable":
                print(Colorate.Horizontal(Colors.yellow_to_red, f"Ghost Account >> {self.query}", 2))
        except  Exception:
            print(Colorate.Horizontal(Colors.red_to_purple,
                                      f"Not Available This Account In Twitter Database >> {self.query}", 2))


main().split()
