
class Stats:

    @staticmethod
    def create_list():
        created_list = []
        for i in range(17):
            created_list.append({"week": i + 1,
                                 "ranking": None,
                                 "opponent": None,
                                 "rushingyards": None,
                                 "receivingyards": None})

        return created_list

    @staticmethod
    def check_week(date):
        # hard coded for 2016
        if date == "2016-09-08" or date == "2016-09-09" or date == "2016-09-10" or date == "2016-09-11" or date == "2016-09-12":
            return 1
        elif date == "2016-09-15" or date == "2016-09-16" or date == "2016-09-017" or date == "2016-09-18" or date == "2016-09-19":
            return 2
        elif date == "2016-09-22" or date == "2016-09-23" or date == "2016-09-24" or date == "2016-09-25" or date == "2016-09-26":
            return 3
        elif date == "2016-09-29" or date == "2016-09-30" or date == "2016-10-01" or date == "2016-10-02" or date == "2016-10-03":
            return 4
        elif date == "2016-10-06" or date == "2016-10-07" or date == "2016-10-08" or date == "2016-10-09" or date == "2016-10-10":
            return 5
        elif date == "2016-10-13" or date == "2016-10-14" or date == "2016-10-15" or date == "2016-10-16" or date == "2016-10-16":
            return 6
        elif date == "2016-10-20" or date == "2016-10-21" or date == "2016-10-22" or date == "2016-10-23" or date == "2016-10-24":
            return 7
        elif date == "2016-10-27" or date == "2016-10-28" or date == "2016-10-29" or date == "2016-10-30" or date == "2016-10-31":
            return 8
        elif date == "2016-11-03" or date == "2016-11-04" or date == "2016-11-05" or date == "2016-11-06" or date == "2016-11-07":
            return 9
        elif date == "2016-11-10" or date == "2016-11-11" or date == "2016-11-12" or date == "2016-11-13" or date == "2016-11-14":
            return 10
        elif date == "2016-11-17" or date == "2016-11-18" or date == "2016-11-19" or date == "2016-11-20" or date == "2016-11-21":
            return 11
        elif date == "2016-11-24" or date == "2016-11-25" or date == "2016-11-26" or date == "2016-11-27" or date == "2016-11-28":
            return 12
        elif date == "2016-12-01" or date == "2016-12-02" or date == "2016-12-03" or date == "2016-12-04" or date == "2016-12-05":
            return 13
        elif date == "2016-12-08" or date == "2016-12-09" or date == "2016-12-10" or date == "2016-12-11" or date == "2016-12-12":
            return 14
        elif date == "2016-12-15" or date == "2016-12-16" or date == "2016-12-17" or date == "2016-12-18" or date == "2016-12-19":
            return 15
        elif date == "2016-12-22" or date == "2016-12-23" or date == "2016-12-24" or date == "2016-12-25" or date == "2016-12-26":
            return 16
        elif date == "2016-12-29" or date == "2016-12-30" or date == "2016-12-31" or date == "2017-01-01" or date == "2017-01-02":
            return 17
        else:
            print("Error: Invalid date")
            return -1
