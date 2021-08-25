import random
import csv

class Region:
    def __init__(self, bottombound, topbound, name):
        self.topbound = topbound
        self.bottombound = bottombound
        self.name = name
        self.teamlist = []
        self.matchup = []
        self.hometeam = ''
        self.awayteam = ''


    def get_teams(self):
        with open('teams.txt') as csv_file:
            r = csv.reader(csv_file, delimiter=',')
            line_count = self.bottombound
            desired_rows = [row for idx, row in enumerate(r) if idx in range(self.bottombound, self.topbound + 1)]

            for row in desired_rows:
                if line_count == 0:
                    print()
                    line_count += 1

                else:
                    self.teamlist.append(row)
                    line_count += 1
            ##print(self.teamlist)

    def print_teams(self):
        seed = 1

        for i in self.teamlist:
            i = str(i)[1:-1].replace("'", "")
            print(str(seed) + ":", i, end=" ")
            seed += 1
        print()

    def create_matchups(self):
        print(self.name + ":")
        print("--------------------")
        for i in range(len(self.teamlist) // 2):
            self.hometeam = str(self.teamlist[0 + i])[1:-1].replace("'", "")
            self.awayteam = str(self.teamlist[-1 - i])[1:-1].replace("'", "")
            print(i+1, self.hometeam, "vs", 16 - i, self.awayteam)
            self.matchup.append(self.hometeam + self.awayteam)
        print()

    def predict(self):
        pass

    def first_round(self):
        pass

    def second_round(self):
        pass

    def third_round(self):
        pass


print("MARCH MADNESS 2021 MATCHUPS")
print()

Region1 = Region(1, 16, "WEST REGION")
Region2 = Region(17, 32, "SOUTH REGION")
Region3 = Region(33, 48, "MIDWEST REGION")
Region4 = Region(49, 64, "EAST REGION")

Region1.get_teams()
Region2.get_teams()
Region3.get_teams()
Region4.get_teams()

Region1.create_matchups()
Region2.create_matchups()
Region3.create_matchups()
Region4.create_matchups()