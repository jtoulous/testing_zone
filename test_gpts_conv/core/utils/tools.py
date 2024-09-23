def GetBehavior(role):
    with open(f'data/{role}/behavior.txt', 'r') as file:
        behavior = file.read()
    return behavior