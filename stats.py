
class Stats:

    @staticmethod
    def create_list():
        created_list = []
        for i in range(17):
            created_list.append({"week": None,
                                 "ranking": None,
                                 "opponent": None,
                                 "rushingyards": None,
                                 "receivingyards": None})

        return created_list
