
class Stats:

    @staticmethod
    def create_list():
        created_list = []
        for i in range(17):
            created_list.append({"week": i, "ranking": "", "rushingyards": "", "receivingyards": ""})

        return created_list
