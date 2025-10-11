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
        inhour = input('What hour would you like to edit? (e.g. the first time, 0000 for midnight, 1300 for 1pm)')
        for i in range(23):
            if plan[i][0] == inhour:
                newtask = input('What would you like to change the task to?')
                plan[i][1] = newtask
                print('Task updated!')
                user()
    elif indata == 'view':
        indata = input('Which hour would you like to view? (e.g. the first time, 0000 for midnight, 1300 for 1pm)')
        for i in range(23):
            if plan[i][0] == indata:
                print('At', plan[i][0], 'you have the following task:', plan[i][1])
                user()
    elif indata == 'quit':
        print('Thanks for using the daily planner! Goodbye!')
        quit()
user()