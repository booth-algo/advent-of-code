import json

with open('input.txt') as f:
    lines = f.readlines()

# lines = ['two1nine']

info = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'zero': 0
}

sum_arr = 0
first_dig_found = False
first_dig = None
final_dig = None

potential_match = []

for line in lines:
    # Process for each line
    for i in range(0, len(line)):
        print(line[i])
        if line[i].isnumeric():
            potential_match = []
            alpha_active = False

            if not first_dig_found:
                first_dig = line[i]
                first_dig_found = True

            elif first_dig_found:
                final_dig = line[i]

        if line[i].isalpha():
            # append new alphanumeric value to every entry 
            for j in range(0, len(potential_match)):
                potential_match[j] = potential_match[j] + line[i] 

            # create new entry in the potential_match list
            potential_match.append(line[i])

            # Check if there is match
            for entry in potential_match:
                if entry in info:
                    print("entry: ", entry)
                    if first_dig_found:
                        final_dig = info.get(entry)
                    elif not first_dig_found:
                        first_dig = info.get(entry)
                        first_dig_found = True

        print(potential_match)
        
    potential_match = []

    print("first dig: ", first_dig)
    print("final dig: ", final_dig)

    if(final_dig == None):
        final_dig = first_dig
    num = int(str(first_dig) + str(final_dig))
    sum_arr += num

    first_dig_found = False
    first_dig = None
    final_dig = None

print(sum_arr)

    
