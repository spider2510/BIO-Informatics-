

with open('DNA.txt', 'r') as file:
    data = file.read().replace('\n', '')                                     # readind DNA string data from file 

file.close()

string2 = 'TGA'                                                          # pattern to count 
len_data = len(data)                                                        # length of data 
len_string2 = len(string2)                                                  # length of pattern 

total_count = 0                                                             # count variable 



for i in range(len_data - len_string2 + 1):                               # for loop till len_data - len_string2 + 1 so we consider all substring
	counter = len_string2                                                   # counter to calculate pattern match 
	for j in range(len_string2):                                            # Nexted for loop till length of pattern    
	 	if  data[i + j] != string2[j] :break                                # break condition for Nested for loop
	 	counter -= 1                                                        # if pattern element match then subtract 1 from counter 
	if counter == 0:total_count += 1                                        # if pattern matched then increment total count var by 1


print("Total Number of count that string2 appear in Data : ",total_count)   # print result 

""" Time Complexity = O(len_string2*(len_data - len_string2 + 1))   """
""" Space Complexity = O(len_data + len_string2 )   """

