plan = []
print('Welcome to your personal daily planner! Start organizing your day now!')
for i in range(23):
    if i < 10:
        init = ["0"+str(i)+"00", "Empty. Input something!"]
        plan.append(init)
    else:
        init = [str(i)+"00", "Empty. Input something!"]
        plan.append(init)
def user():
    indata = input('What would you like to do? (e.g. edit, view, or quit)')
    if indata == 'edit':
        inhour = input('What hour would you like to edit? (e.g. the first time, )')
user()