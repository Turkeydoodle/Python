import random 
terrain_choices = ["grass", "dirt", "stone", "gravel"]
terrain = [['', '', '', '', ''],['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']]
def generate(timestogenerate):
    terrain[0][0] = terrain_choices[random.randint(0,3)]
    if timestogenerate <= 200000:
        for i in range(timestogenerate):
            gchance = 25
            dchance = 25
            schance = 25
            vchance = 25
            if terrain[0][i-2] == "grass":
                gchance += 20
                vchance -= 20
            elif terrain[0][i-2] == "dirt":
                dchance += 20
                schance -= 20
            elif terrain[0][i-2] == "stone":
                schance += 20
                dchance -= 20
            elif terrain[0][i-2] == "gravel":
                vchance += 20
                gchance -= 20
            random_choice = random.randint(1, 100)
            if random_choice <= gchance:
                terrain[0][i-1] = "grass"
            elif random_choice <= gchance+dchance:
                terrain[0][i-1] = 'dirt'
            elif random_choice <= gchance+dchance+schance:
                terrain[0][i-1] = "stone"
            elif random_choice <= gchance+dchance+schance+vchance:
                terrain[0][i-1] = "gravel"
    else:
        pass
def print_terrain():
    for i in range(len(terrain)):
        for j in range(len(terrain[i-1])):
            print(terrain[i-1][j-1])
generate(25)
print_terrain()