import simplejson as json
import os
from player import Player


class Database:

    @staticmethod
    def open_db():
        if os.path.isfile("./db.json") and os.stat("./db.json").st_size != 0:
            old_file = open("./db.json", "r+")
            data = json.loads(old_file.read())
            return Database.unmake_jsonable(data)
        else:
            return -1

    @staticmethod
    def close_db(data):
        old_file = open("./db.json", "w+")
        old_file.seek(0)
        old_file.write(json.dumps(Database.make_jsonable(data)))

    @staticmethod
    def make_jsonable(data):
        new_data = []
        for entries in data:
            new_entry = {"name": entries.name,
                         "team": entries.team,
                         "position": entries.position,
                         "rank": entries.rank,
                         "stats": entries.stats}
            new_data.append(new_entry)
        return new_data

    @staticmethod
    def unmake_jsonable(data):
        new_data = []
        for item in data:
            player = Player(item["name"], item["team"], item["position"], item["rank"], item["stats"])
            new_data.append(player)
        return new_data
