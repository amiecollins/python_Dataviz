import csv

canada = []
world = []

categories = []

with open("data/OlympicsWinter.csv") as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:
            categories.append(row)
            line_count += 1

        elif row[4] == "CAN":
            canada.append([int(row[0]), row[5], row[6], row[7]])
        else:
            world.append([int(row[0]), row[5], row[6], row[7]])

print("total medals for canada:", len(canada))
print("rest of the world:", len(world))

print(canada[0])

print("processed", line_count, "rows of data")

gold_1924 = []
gold_1948 = []
gold_1972 = []
gold_2002 = []
gold_2014 = []

for medal in canada:
    if medal[0] == 1924 and medal[3] == "Gold":
        gold_1924.append(medal)
    elif medal[0] == 1948 and medal[3] == "Gold":
        gold_1948.append(medal)
    elif medal[0] == 1972 and medal[3] == "Gold":
        gold_1972.append(medal)
    elif medal[0] == 2002 and medal[3] == "Gold":
        gold_2002.append(medal)
    elif medal[0] == 2014 and medal[3] == "Gold":
        gold_2014.append(medal)

print("canada won", len(gold_1924), "gold medals in 1924")
print("canada won", len(gold_2014), "gold medals in 2014")

2014_mens = []
2015_womans = []

for medal in gold_2014:
    if medal[1] == "Men":
        2014_mens.append(medal)
    elif medal[1] = "Woman":
        2014_womans.append(medal)

print("canadian men won:", len(2014_mens), "in 2014")
print("canadian women won:", len(2014_womens), "in 2014")
