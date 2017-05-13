from stats import Stats
from bs4 import BeautifulSoup
import requests


class Player:
    def __init__(self, name, team, position, stats):
        self.name = name
        self.team = team
        self.position = position
        self.stats = stats

    def create_player_url(self):
        name_pair = self.name.split(" ")
        url_id = name_pair[1][0] + "/" + name_pair[1][:4] + name_pair[0][:2] + "00"
        url = "http://www.pro-football-reference.com/players/" + url_id + "/gamelog/2016/"
        print(url)
        return url

    def get_stats(self):
        url = self.create_player_url()
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        results = soup.find("table", {"id": "stats"})
        table = results.find("tbody")
        entries = table.findAll("td")

        j = 0
        i = 1
        for rows in entries:
            print(i, j)
            if j == 0:
                i = Stats.check_week(rows.text)
            if j == 5:
                self.stats[i - 1]["opponent"] = rows.text
            if j == 8:
                self.stats[i - 1]["rushingyards"] = rows.text
            if j == 13:
                self.stats[i - 1]["receivingyards"] = rows.text
            if j == 19:
                self.stats[i - 1]["week"] = i
                j = 0
                i += 1
                if i > 17:
                    break
                continue
            j += 1

        for i in range(17):
            print(self.stats[i]["week"],
                  self.stats[i]["opponent"],
                  self.stats[i]["rushingyards"],
                  self.stats[i]["receivingyards"])
