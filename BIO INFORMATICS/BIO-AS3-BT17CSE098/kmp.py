
import time 
import matplotlib.pyplot as plt 




with open('DNA.txt', 'r') as file:
    data = file.read().replace('\n', '')                                     # readind DNA string data from file 

file.close()

string = ['TGATCA','TGA','TGGCT','TCAATTG','AGCATGATCAAGGTGCT','GACCGT','TAGGT','AT','GCGAC']            # pattern to count  




def LpsArray(pattern,len2,lps):                                         # LPS array function for KMP Search 
	i = 0                                                               # initailising Index of pattern
	j = 1
	while j < len2:                                                     # loop check if suffix is same as preffix                                                    
		if pattern[i] != pattern[j]:
			j += 1                                                      # if not match increment suffix pointer and preffix point to fist item
			i = 0 
		else:
			lps[j] = lps[j - 1] + 1                                     # if match increment lps array element by 1 w.r.t previous item
			i += 1
			j += 1
	return lps






def KMP(str1,str2):                     					   #KMP search function 
	len1 = len(str1)              
	len2 = len(str2)
	lps = [0]*len2                                             # Initializing LPS array with  length of pattern             
	count = 0
	lps = LpsArray(str2,len2,lps)                              # LPS Array Function 
	i = j = 0

	while i < len1:                                            # traverse complete text data 
		if str1[i] == str2[j]:                                 # if item match increment index i and j by 1
			i += 1
			j += 1
		else :                                                 # if pattern not match increment i by one and j by looking at LPS aarray
			if j == 0:
				i += 1
			else:
				j = lps[j-1]

		if j == len2:                                          # if pattern match increment count by 1
			count += 1
			# i = i - j + 1
			j = 0
	return count 





print("pattern match by Knuth Morris Pratt Algorithm : ",KMP(data,'TGATCA'))


def Bad_match(str2,len2):                               # Bad Match array function for Search in Boyre Moore Algorithms  
	# str2 = str2 + '*'                                   
	temp_str = list(set(str2))                          # making list of item in pattern which not repeat
	bmatch = {}.fromkeys(temp_str,0)                    # making dictonary where temp_str element use as keys 
	for i in range(len2):
		bmatch[str2[i]] = max(1,len2-i-1)               # inserting value at keys 
	# bmatch['*'] = len2
	return bmatch                                       # return Bad match Dictonary





def Boyre_Moore_Algorithm(str1,str2):                            # Boyer Moorer Algorithm 
	len1 = len(str1)
	len2 = len(str2)

	B_match = Bad_match(str2,len2)                               # BAD match Function
	i = 0                                                        # initializing index and counter 
	count = 0 
	j = len2 - 1
	while i <= len1 - len2 :                                     # loop to traverse to text data 
		if str2[j] == str1[i+j]:                                 # matching from R.H.S if match decrement j by 1 
			j -= 1
		else:
			if str2[j] in B_match.keys():                        # if not match increment i by looking at Bad Match Table
				i += B_match[str2[j]]
				j = len2 - 1
			else:                                               
				i += len2 
				j = len2 - 1
		if j < 0 :                                               # pattern match then increment count by 1 
			count += 1
			j = len2 - 1
			i += len2
	return count 




print("Pattern Match By Boyre Moore Algorithm :",Boyre_Moore_Algorithm(data,'TGATCA'))










#  Data Visualization 



arr1 = [ ]
for i in string:
    start = time.time()
    print("pattern match by Knuth Morris Pratt Algorithm : ",KMP(data,i))
    end = time.time()
    arr1.append((end - start)*1000)


arr2 = [ ]
for i in string:
    start = time.time()
    print("Pattern Match By Boyre Moore Algorithm :",Boyre_Moore_Algorithm(data,i))
    end = time.time()
    arr2.append((end - start)*1000)

fig, axes = plt.subplots(figsize=(12, 6))


axes.plot(arr1, '-.b', label="KMP Algoriths")
axes.plot(arr2, '-.r', label="Boyre Moore")
axes.set_xlabel('Example')
axes.set_ylabel('Time in Milisecond')
axes.set_title("KMP VS Boyre Moore Algorithm")

axes.legend()


fig.savefig('KMP_VS_BMORRIS.png')


