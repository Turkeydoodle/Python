import random
from turtle import *
terrain_choices = ["grass", "dirt", "stone", "gravel"]
terrain = []


def generate(timestogenerate):
    global terrain
    terrain = [[None for _ in range(timestogenerate)] for _ in range(timestogenerate)]

    terrain[0][0] = random.choice(terrain_choices)

    if timestogenerate <= 5:
        for i in range(timestogenerate):
            gchance = dchance = schance = vchance = 25

            if i >= 2:
                prev = terrain[0][i-2]
                if prev == "grass":
                    gchance += 20; vchance -= 20
                elif prev == "dirt":
                    dchance += 20; schance -= 20
                elif prev == "stone":
                    schance += 20; dchance -= 20
                elif prev == "gravel":
                    vchance += 20; gchance -= 20

            r = random.randint(1, 100)
            if r <= gchance:
                terrain[0][i] = "grass"
            elif r <= gchance + dchance:
                terrain[0][i] = "dirt"
            elif r <= gchance + dchance + schance:
                terrain[0][i] = "stone"
            else:
                terrain[0][i] = "gravel"

    else:
        for i in range(timestogenerate):
            terrain[i][0] = random.choice(terrain_choices)

            for j in range(1, timestogenerate):
                gchance = dchance = schance = vchance = 25

                if j >= 2:
                    prev = terrain[i][j-2]
                    if prev == "grass":
                        gchance += 20; vchance -= 20
                    elif prev == "dirt":
                        dchance += 20; schance -= 20
                    elif prev == "stone":
                        schance += 20; dchance -= 20
                    elif prev == "gravel":
                        vchance += 20; gchance -= 20

                r = random.randint(1, 100)
                if r <= gchance:
                    terrain[i][j] = "grass"
                elif r <= gchance + dchance:
                    terrain[i][j] = "dirt"
                elif r <= gchance + dchance + schance:
                    terrain[i][j] = "stone"
                else:
                    terrain[i][j] = "gravel"


def render_terrain():
    tile = 20
    grid = len(terrain)

    speed(0)
    penup()
    goto(-475, 350)  # Start inside the visible window
    pendown()

    for i in range(grid):
        for j in range(grid):

            t = terrain[i][j]

            if t == "grass":
                color("green")
            elif t == "dirt":
                color("brown")
            elif t == "stone":
                color("gray")
            elif t == "gravel":
                color("light gray")
            else:
                color("white")

            begin_fill()
            for _ in range(4):
                forward(tile)
                right(90)
            end_fill()

            forward(tile)
        penup()
        backward(grid * tile)
        pendown()
        right(90)
        forward(tile)
        left(90)


generate(50)
render_terrain()
done()
