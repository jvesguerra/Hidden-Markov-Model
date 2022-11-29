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

# PART 1. SOLVING FOR TRANSITION PROBABILITIES

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

# --- might start loop here

# fill dictionary values

# S = key[0]; T = key[1]
#   STSSTSSSTT
#   TSSSSSTTSS

# S or T
#string = data[1]
string = "STSSTSTSSSTT"
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

# S with next state S
ss_total = 0
for i in range(0,string_len):
    if string[i] == key[0]: # if char == "S"
        if string[i+1] == key[0]: # if next char is also S
            ss_total += 1

prob_dict[key[0]+key[0]] = ss_total/s_total

# S with next state T
ts_total = 0
for i in range(0,string_len-1):
    if string[i] == key[0]: # if char == "S"
        if string[i+1] == key[1]: # if next char is T
            ts_total += 1

prob_dict[key[1]+key[0]] = ts_total/s_total
t_total = ts_total

# T with next state T
tt_total = 0
for i in range(0,string_len-1):
    if string[i] == key[1]: # if char == "T"
        if string[i+1] == key[1]: # if next char is T
            tt_total += 1

prob_dict[key[1]+key[1]] = tt_total/t_total

# T with next state S
st_total = 0
for i in range(0,string_len-1):
    if string[i] == key[1]: # if char == "T"
        if string[i+1] == key[0]: # if next char is S
            st_total += 1

prob_dict[key[0]+key[1]] = st_total/t_total

#print(prob_dict)

# END PART 1.

# PART 2. PREDICTING PROBABILITY VALUE OF NEXT STATE

# formula for total probability

# check array of what to get
test_string = "T3"

char1 = key[0]+"1"
char2 = key[1]+"1"
check_let = test_string[0]
check_num = int(test_string[1])

for i in range(0,check_num):
    if i == 0:
        s_Total_prob = prob_dict.get("SS")*prob_dict.get("S") + prob_dict.get("ST")*prob_dict.get("T")
        prob_dict["S1"] = s_Total_prob
        t_Total_prob = prob_dict.get("TS")*prob_dict.get("S") + prob_dict.get("TT")*prob_dict.get("T")
        prob_dict["T1"] = t_Total_prob
    else:
        key1 = key[0]+ str(i+1)  # for saving in dictionary
        key2 = key[1]+ str(i+1)  # for saving in dictionary

        # values
        Sn = key[0]+ str(i)
        Tn = key[1]+ str(i)
        # print(prob_dict.get(Sn))
        # print(prob_dict.get(Tn))

        # solve T
        t_Total_prob = prob_dict.get(Tn)*prob_dict.get(Sn)+prob_dict.get("TT")*prob_dict.get(Tn)
        prob_dict[key2] = t_Total_prob
        #solve S
        s_Total_prob = prob_dict.get("SS")*prob_dict.get(Sn) + prob_dict.get("ST")*prob_dict.get(Tn)
        prob_dict[key1] = s_Total_prob

print(prob_dict)

# END OF PART 2

        







    

