import json

with open('input.txt') as f:
    lines = f.readlines()

sum_arr = 0
first_dig_found = False
first_dig = None
final_dig = None

for line in lines:
    for i in range(0, len(line)):
        if (line[i].isnumeric() and not first_dig_found):
            first_dig = line[i]
            first_dig_found = True
        elif (line[i].isnumeric() and first_dig_found):
            final_dig = line[i]

    # print(line)
    # print("First: ", first_dig)
    # print("Last: ", final_dig)
    if(final_dig == None):
        final_dig = first_dig
    num = int(str(first_dig) + str(final_dig))
    sum_arr += num

    first_dig_found = False
    first_dig = None
    final_dig = None

print(sum_arr)

    
