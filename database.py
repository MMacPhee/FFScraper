import simplejson as json
import os


class Database:

    @staticmethod
    def open_db():
        if os.path.isfile("./db.json") and os.stat("./db.json").st_size != 0:
            old_file = open("./db.json", "r+")
            data = json.loads(old_file.read())
            return data
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
        new_entry = {}
        for entries in data:
            new_entry["name"] = entries.name
            new_entry["team"] = entries.team
            new_entry["position"] = entries.position
            new_entry["rank"] = entries.rank
            new_entry["stats"] = entries.stats
            new_data.append(new_entry)
        return new_data
