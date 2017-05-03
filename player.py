from stats import Stats


class Player:
    def __init__(self, name, team, position, stats=Stats.create_list()):
        self.name = name
        self.team = team
        self.position = position
        self.stats = stats
