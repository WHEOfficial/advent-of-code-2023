def read_input(day: int):
    data = []
    with open("input/day" + str(day) + ".txt", 'r') as infile:
        data = infile.read().splitlines()
    return data