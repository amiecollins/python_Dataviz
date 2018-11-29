import csv
import matplotlib.pyplot as plt
import numpy as np

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


Medals1924 = []
Medals1928 = []
Medals1932 = []
Medals1936 = []
Medals1948 = []
Medals1952 = []
Medals1956 = []
Medals1960 = []
Medals1964 = []
Medals1968 = []
Medals1972 = []
Medals1976 = []
Medals1980 = []
Medals1984 = []
Medals1988 = []
Medals1992 = []
Medals1994 = []
Medals1998 = []
Medals2002 = []
Medals2006 = []
Medals2010 = []
Medals2014 = []

for medal in canada:
    if medal[0] == 1924:
        Medals1924.append(medal)
    elif medal[0] == 1928:
        Medals1928.append(medal)
    elif medal[0] == 1932:
        Medals1932.append(medal)
    elif medal[0] == 1936:
        Medals1936.append(medal)
    elif medal[0] == 1948:
        Medals1948.append(medal)
    elif medal[0] == 1952:
        Medals1952.append(medal)
    elif medal[0] == 1956:
        Medals1956.append(medal)
    elif medal[0] == 1960:
        Medals1960.append(medal)
    elif medal[0] == 1964:
        Medals1964.append(medal)
    elif medal[0] == 1968:
        Medals1968.append(medal)
    elif medal[0] == 1972:
        Medals1972.append(medal)
    elif medal[0] == 1976:
        Medals1976.append(medal)
    elif medal[0] == 1980:
        Medals1980.append(medal)
    elif medal[0] == 1984:
        Medals1984.append(medal)
    elif medal[0] == 1988:
        Medals1988.append(medal)
    elif medal[0] == 1992:
        Medals1992.append(medal)
    elif medal[0] == 1994:
        Medals1994.append(medal)
    elif medal[0] == 1998:
        Medals1998.append(medal)
    elif medal[0] == 2002:
        Medals2002.append(medal)
    elif medal[0] == 2006:
        Medals2006.append(medal)
    elif medal[0] == 2010:
        Medals2010.append(medal)
    elif medal[0] == 2014:
        Medals2014.append(medal)

totalMedals1924 = len(Medals1924)
totalMedals1928 = len(Medals1928)
totalMedals1932 = len(Medals1932)
totalMedals1936 = len(Medals1936)
totalMedals1948 = len(Medals1948)
totalMedals1952 = len(Medals1952)
totalMedals1956 = len(Medals1956)
totalMedals1960 = len(Medals1960)
totalMedals1964 = len(Medals1964)
totalMedals1968 = len(Medals1968)
totalMedals1972 = len(Medals1972)
totalMedals1976 = len(Medals1976)
totalMedals1980 = len(Medals1980)
totalMedals1984 = len(Medals1984)
totalMedals1988 = len(Medals1988)
totalMedals1992 = len(Medals1992)
totalMedals1994 = len(Medals1994)
totalMedals1998 = len(Medals1998)
totalMedals2002 = len(Medals2002)
totalMedals2006 = len(Medals2006)
totalMedals2010 = len(Medals2010)
totalMedals2014 = len(Medals2014)

print(len(Medals1924))

labels = "1924", "1928", "1932", "1936", "1948", "1952", "1956", "1960", "1964", "1968", "1972", "1976", "1980", "1984", "1988", "1992", "1994", "1998", "2002", "2006", "2010", "2014"
sizes = [totalMedals1924, totalMedals1928, totalMedals1932, totalMedals1936, totalMedals1948, totalMedals1952, totalMedals1956, totalMedals1960, totalMedals1964, totalMedals1968, totalMedals1972, totalMedals1976, totalMedals1980, totalMedals1984, totalMedals1988, totalMedals1992, totalMedals1994, totalMedals1998, totalMedals2002, totalMedals2006, totalMedals2010, totalMedals2014]
# sizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
colors = ["yellowgreen", "lightcoral", "lightskyblue", "darksalmon", "olivedrab", "mediumspringgreen", "mediumpurple", "slategray", "navy", "deepskyblue", "chartreuse", "gold", "cadetblue", "rebeccapurple", "darkmagenta", "crimson", "darkviolet", "darkblue", "dodgerblue", "deeppink", "olive", "maroon"]

index = np.arange(len(labels))

plt.bar(index, sizes)
plt.xticks(index, labels)
plt.title("Medals Won By Canada In Their Respective Year")
plt.show()
