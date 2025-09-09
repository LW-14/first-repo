# A program to differentiate each house gate in a community using For loop

# A variable called 'community house' containing all details
community_houses = [{'house': 'gate_1', 'painted': 'black'},
                    {'house': 'gate_2', 'painted': 'blue'},
                    {'house': 'gate_3', 'painted': 'ash'},
                    {'house': 'gate_4', 'painted': 'brown'},
                    {'house': 'gate_5', 'painted': 'blue'},
                    {'house': 'gate_6', 'painted': 'black'},
                    {'house': 'gate_7', 'painted': 'brown'}]

# creating containers to store each information
black_gate = []
brown_gate = []
ash_gate = []
blue_gate = []

# Using the For loop
for houses in community_houses:
    if (houses['painted'] == 'black'):      # if a house is painted black run this command
        # add the house containing that specific house
        black_gate.append(houses['house'])
    elif (houses['painted'] == 'brown'):
        brown_gate.append(houses['house'])
    elif (houses['painted'] == 'ash'):
        ash_gate.append(houses['house'])
    else:
        blue_gate.append(houses['house'])

print('black gate = ', black_gate)      # display this particular variable
print('brown gate = ', brown_gate)      # display this particular variable
print('ash gate = ', ash_gate)          # display this particular variable
print('blue gate = ', blue_gate)        # display this particular variable
