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
        return self
