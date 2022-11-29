# insert read files to data array
data = []

# read files
with open("hmm.in",'r') as file:
    for row in file:
        data.append(row.rstrip('\n'))
file.close()

# modify data array
for i in range(3,7):
    temp = data[i].split(' ')   # splits S T to array for easier indexing
    data[i] = temp              # update data array

# notes
# data[0] = number of test cases
# data[1] and data[2] = string sequences

# PART 1. GETTING PROBABILITY VALUES

# make dictionary of probabilities
prob_dict = {}

# data[3] = possible values
#initialize keys
key = data[3]
prob_dict[key[0]] = 0           #S
prob_dict[key[0]+key[0]] = 0    #SS
prob_dict[key[1]+key[0]] = 0    #TS
prob_dict[key[1]+key[1]] = 0    #TT
prob_dict[key[0]+key[1]] = 0    #ST
prob_dict[key[1]] = 0           #T

# fill dictionary values

# S = key[0]; T = key[1]
#   STSSTSSSTT
#   TSSSSSTTSS

# S or T
string = data[1]
if string[0] == key[0]:
    prob_dict[key[0]] = 1
else:
    prob_dict[key[1]] = 1

s_total = 0
t_total = 0
string_len = len(string)

# check total occurenes of S
for i in range(0,string_len):
    if string[i] == key[0]: # if char == "S"
        s_total += 1

prob_dict[key[0]] = s_total

# S with next state S
ss_total = 0
for i in range(0,string_len):
    if string[i] == key[0]: # if char == "S"
        if string[i+1] == key[0]: # if next char is also S
            ss_total += 1

prob_dict[key[0]+key[0]] = ss_total

# S with next state T
ts_total = 0
for i in range(0,string_len-1):
    if string[i] == key[0]: # if char == "S"
        if string[i+1] == key[1]: # if next char is T
            ts_total += 1

prob_dict[key[1]+key[0]] = ts_total
t_total = ts_total

# T with next state T
tt_total = 0
for i in range(0,string_len-1):
    if string[i] == key[1]: # if char == "T"
        if string[i+1] == key[1]: # if next char is T
            tt_total += 1

prob_dict[key[1]+key[1]] = tt_total

# T with next state S
st_total = 0
for i in range(0,string_len-1):
    if string[i] == key[1]: # if char == "T"
        if string[i+1] == key[0]: # if next char is S
            st_total += 1

prob_dict[key[0]+key[1]] = st_total

print(prob_dict)
print(t_total)

# END PART 1.







    

