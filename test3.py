
colors = ['teal', 'PINK', 'PURPLE', 'ORANGE', 'green', 'BLUE', 'YELLOW', 'red', 'pink', 'TEaL', 'PurPLE', 'greEn', 'YELLOW', 'ORAnGE', 'blue', 'RED', 'teal', 'PINk', 'purPle', 'orange', 'GREEN', 'BluE', 'YelLow', 'ReD']

# 1 - print how many colors there are in the list
print(len(colors))

# 2 - get the list of unique colors (in lowercase), case insensitive
results = []
for color in colors:
    color_lower = color.lower()
    if color_lower not in results:
        results.append(color_lower)

print(results)



# 3 - given a color, count how many times it exist on the list
color = "red"
count = 0
for c in colors:
    if color == c.lower():
        count = count + 1

print(count)