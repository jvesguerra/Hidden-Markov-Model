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

print(prob_dict)
print()

# For E and F

p_states = data[4]
# initialize
prob_dict[key[0]+p_states[0]] = 0.1   # S to E
prob_dict[key[0]+p_states[1]] = 0.9   # S to F
prob_dict[key[1]+p_states[0]] = 0.6   # T to E
prob_dict[key[1]+p_states[1]] = 0.4   # T to F
# END PART 1.


# 1.5 Get what to solve 
case_count = data[7]
given = []
counter = 8
for i in range(0, int(case_count)):
    temp = data[counter+i].split(' ')
    given_string = temp[0]+temp[2]
    given.append(given_string)

print(given)

# PART 2. PREDICTING PROBABILITY VALUE OF NEXT STATE

# check array of what to get


# loop for the given

#for i in range(0, int(case_count)):
for i in range(0, 1):
    check_num = int(given[i][1])    # if T3E3 = 3

    for i in range(0,check_num):
        index = i + 1
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

            # for solving E
            Sn2 = key[0]+ str(index)
            Tn2 = key[1]+ str(index)

            # solve T
            t_Total_prob = prob_dict.get("TS")*prob_dict.get(Sn)+prob_dict.get("TT")*prob_dict.get(Tn)
            prob_dict[key2] = t_Total_prob

            #solve S
            s_Total_prob = prob_dict.get("SS")*prob_dict.get(Sn) + prob_dict.get("ST")*prob_dict.get(Tn)
            prob_dict[key1] = s_Total_prob

            #solve E
            e_Total_prob = prob_dict.get("SE")*prob_dict.get(Sn2)+prob_dict.get("TE")*prob_dict.get(Tn2) #E1
            prob_dict[p_states[0]+str(index)] = e_Total_prob

            #solve F
            e_Total_prob = prob_dict.get("SE")*prob_dict.get(Sn2)+prob_dict.get("TE")*prob_dict.get(Tn2) #E1
            prob_dict[p_states[0]+str(index)] = e_Total_prob

    print(prob_dict)
    print()

    # END OF PART 2

    # to get E to S

        #temp_e =  prob_dict.get("SE")*prob_dict.get(Sn)/prob_dict.get(En)
        #temp_t =  prob_dict.get("TE")*prob_dict.get(Tn)/prob_dict.get(Fn)


        







    

