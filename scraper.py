from bs4 import BeautifulSoup
from player import Player
import requests


class Scraper:
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def get_list(self, position):
        if position == "rb":
            link = "https://www.thefantasyfootballers.com/2017-running-back-rankings/"
        elif position == "qb":
            link = "https://www.thefantasyfootballers.com/2017-quarterback-rankings/"
        elif position == "wr":
            link = "https://www.thefantasyfootballers.com/2017-wide-receiver-rankings/"

        r = requests.get(link)

        soup = BeautifulSoup(r.text, "html.parser")
        results = soup.find("table", {"id": "table_1"})
        table = results.find("tbody")

        entries = table.findAll("tr")

        for item in entries:
            item_text = {"name": " ".join(item.find("td").text.split(" ")[:2]),
                         "team": "".join(item.find("td").text.split(" ")[2:3]),
                         "ranking": ""}
            ranks = item.findAll("td")

            for rank in ranks:
                try:
                    rank_num = int(rank.text)
                    for player in self.content:
                        if player.rank == rank_num:
                            rank_num += 1
                    item_text["ranking"] = rank_num
                    break
                except ValueError:
                    continue

            new_player = Player(item_text["name"], item_text["team"], position, item_text["ranking"], [])
            if item_text:
                self.content.append(new_player)

        for player in sorted(self.content, key=lambda content: content.rank):
            print(player.name, player.team, player.rank)

        print("\n")





