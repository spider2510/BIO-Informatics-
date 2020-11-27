



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
	# count = 0
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

		if j == len2:                                          # if pattern match return True
			return True
	return False


stringA = 'aaccggacgaaaccccgcgcgggaaa'
stringB = 'gcgcgg'
stringC = 'ggga'



def Sub_string(str1,str2,str3):                                    # Substring Search function
	flag1 = False
	flag2 = False                                                  # Flage boolean variable 
	count = 0
	count1 = 0                                                     # count variable 
	if KMP(str2,str3):                                             # if string3 is in string 2 
		if KMP(str1,str2):                                  # if string3 is in string 2 and string 2 is in string 1 return True 
			return True
		return False
	temp1 = temp2 = str3                                   # initializing temp variable 

	for i in range(1,len(str3)):                           # Union Opereation  between string 2 and 3 
		j = - i                                            
		if str2[i] == temp1[j]:                            # front element of string 2 is same as str 1 then set flag1 true   
			count += 1
			flag1 = True
		if str2[j] == temp2[i]:                            #front element of string 3 is same as str 2 then set flag2 true 
			count1 += 1
			flag2 = True
		if i == 0 and count1+count == 0:                 # if cant union then return false
			return False
	if flag1 :                                           
		temp1 = temp1[::(len(str3) - count)]        # if flag1 True then search temp1 in string 1
		temp1 = temp1 + str2
		if KMP(str1,temp1):return True
	if flag2:
		temp2 =  temp2[count1::]                    # # if flag2 True then search temp1 in string 2
		temp2 = str2 + temp2
		if KMP(str1,temp2):return True
	return False

print("Example 1 Sub_string   Found : ",Sub_string(stringA,stringB,stringC))


StringA  = 'aaccggacgaaaccccgcgcgggaaa'
StringB =  'gcgcgg'
StringC =  'aa'
print(Sub_string("Example 2 Sub_string   Found : ",StringA,StringB,StringC))