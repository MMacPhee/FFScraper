from stats import Stats
from bs4 import BeautifulSoup
import requests


class Player:
    def __init__(self, name, team, position, stats):
        self.name = name
        self.team = team
        self.position = position
        self.stats = stats

    def create_pfr_url(self):
        name_pair = self.name.split(" ")
        url_id = name_pair[1][0] + "/" + name_pair[1][:4] + name_pair[0][:2] + "00"
        url = "http://www.pro-football-reference.com/players/" + url_id + "/gamelog/2016/"
        print(url)
        return url

    def get_stats(self):
        url = self.create_pfr_url()
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        results = soup.find("table", {"id": "stats"})
        table = results.find("tbody")
        entries = table.findAll("tr")

        i = 0
        for rows in entries:
            self.stats[i]["week"] = rows.find("td", {"data-stat": "opp"})
            self.stats[i]["opponent"] = rows.find("td", {"data-stat": "opp"})
            self.stats[i]["rushingyards"] = rows.find("td", {"id": "rush_yds"})
            self.stats[i]["receivingyards"] = rows.find("td", {"id": "rec_yds"})
            i += 1
            print(self.stats[i]["week"], "a",
                  self.stats[i]["opponent"], "b",
                  self.stats[i]["rushingyards"], "c",
                  self.stats[i]["receivingyards"], "d")
