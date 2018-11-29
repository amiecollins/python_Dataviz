import csv
import matplotlib.pyplot as plt

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

print("processed", line_count, "rows of data")
print("total medals for canada:", len(canada))
print("rest of the world:", len(world))

print(canada[0])

Men2010 = []
Women2010 = []

for medal in canada:
    if medal[0] == 2010 and medal[1] == "Men":
        Men2010.append(medal)
    elif medal[0] == 2010 and medal[1] == "Women":
        Women2010.append(medal)

print(len(Women2010), len(Men2010))

labels = ["Women", "Men"]
sizes = [len(Women2010), len(Men2010)]
colors = ["yellowgreen", "lightcoral"]

plt.pie(sizes, colors=colors, autopct="%1.1f%%", shadow=True, startangle=140)
plt.axis("equal")

plt.legend(labels, loc=1)
plt.title("Medals Woman Vs. Men in 2010")
plt.show()
