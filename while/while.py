# A program to check for available door at each stairs using while loop

stair_1 = 1
stair_2 = 2
stair_3 = 3
stair_4 = 4
stair_5 = 5
stair_6 = 6

# A house with each stairs
stair_house = [stair_1, stair_2, stair_3, stair_4, stair_5, stair_6]

objective = stair_4     # The possible target
stair_number = 0        # stairs start to count from 0
door_found = False      # setting search at default


while stair_number < len(stair_house):
    # setting a condition on how the search is perform
    if (stair_house[stair_number] == objective):
        print(f'{objective} is found on {stair_number}')
        door_found = True       # search found
        break
    else:
        print(f'{objective} is not found {stair_number}')
    stair_number += 1       # counts each stair by one
if not door_found:
    print(f'{objective} is not available')
