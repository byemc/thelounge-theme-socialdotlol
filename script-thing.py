import random

good_colors = ["red", "pink", "grape", "violet", "indigo", "blue", "cyan", "teal", "green"]

available_colors = list()

for i in range(1,33):
    available_colors.append(i)

all_colors = []

for color in good_colors:
    for i in range(1,7):
        all_colors.append(f"--{color}-{i}")

for i in range (1,33):
    # get a random color
    color = random.choice(all_colors)
    all_colors.remove(color)
    print(f'#chat.colored-nicks .user.color-{i} {{ color: var({color}) }}')
