# A program to check for the total number of people in a house using if/else loop or statement.

# house members and each house
house_1 = ['kingsley', 'gwen', 'yvonne', 'smith']
house_2 = ('godwin', 'claudia')

if (house_2 != house_1):  # checks if house_2 members are in house_1
    house_1.append(house_2)  # adding house_2 members to house_1
    # a message that shows house_2 members are at the same location
    print(f'{house_2} lives at the same location')
else:
    # a message that shows house_2 members are not at the same location
    print(f'{house_2} lives elsewhere')

# combines both house_1 and house_2 members
print(house_1)
