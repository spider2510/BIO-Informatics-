


from random import randint 

# initializing Array (winning_recipe)
winning_recipe = [['*','-','*','-','*','-','*','-','*','-','*'],
				  ['|','/','|','/','|','/','|','/','|','/','|'],
				  ['*','-','*','-','*','-','*','-','*','-','*'],
				  ['|','/','|','/','|','/','|','/','|','/','|'],
				  ['*','-','*','-','*','-','*','-','*','-','*'],
				  ['|','/','|','/','|','/','|','/','|','/','|'],
				  ['*','-','*','-','*','-','*','-','*','-','*'],
				  ['|','/','|','/','|','/','|','/','|','/','|'],
				  ['*','-','*','-','*','-','*','-','*','-','*'],
				  ['|','/','|','/','|','/','|','/','|','/','|'],
				  ['*','-','*','-','*','-','*','-','*','-','*']
				  ]



# Moves() function takeout elements from piles as per Input and instruction 
def Moves(move_value,Pile_A,Pile_B,len_Pile_A,len_Pile_B):
	# * condition where Bob can chose random move 
	if move_value == '*':
		move_value = str(random.randint(1,4))
		print(move_value)


	#  Up arrow or 1 for picking rock from Pile A
	if move_value == "1" or move_value == "|":
		Pile_A.pop(0)
		print("Pop from Pile_A")
		len_Pile_A = len_Pile_A - 1

	#  Up arrow or 1 for picking rock from Pile B
	elif move_value == "2" or move_value == "-":
		print("Pop from Pile_B")
		Pile_B.pop(0)
		len_Pile_B = len_Pile_B - 1

	#  Up arrow or 1 for picking rock from Pile A and Pile B
	elif move_value == '3'  or move_value == "/" :
		print("Pop from Pile_A and Pile_B")
		Pile_A.pop(0)
		Pile_B.pop(0)
		len_Pile_A = len_Pile_A - 1
		len_Pile_B = len_Pile_B - 1
	print("Pile_A :",Pile_A)
	print("Pile_B :",Pile_B)

	return Pile_A,Pile_B,len_Pile_A,len_Pile_B




def Ten_plus_Ten():
	print("Input Type : int (1,2,3)")          # User Instruction's for Input 
	print("Select :\n1. One Rock from Pile_A \n2.One Rock from Pile_A \n3. One Rock from Both Pile")
	i = 0                         # intializing variable to determine who win atlast 
	Pile_A = [0] * 10             # PILE A which contain 10 Items (Rocks)
	Pile_B = [0] * 10             # PILE B which Contain 10 Items (Rocks)
	len_Pile_A = 10               # Pile A length 
	len_Pile_B = 10               # Pile B length 

	while (len_Pile_A + len_Pile_B) != 0:                    #whlile loop terminate when all rock are pick up 
		Alice = int(input(">>> "))



		if Alice > 0 and Alice < 4 :  # input must be between 1-3
			print("After Alice Turn :")
			if len_Pile_A == 0:                         # condition when Pile A is Empty 
				print("You cant pick Rock from Pile A")
 
			# calling function Moves() where it pick up the items from Pile 
			Pile_A,Pile_B,len_Pile_A,len_Pile_B =  Moves(str(Alice),Pile_A,Pile_B,len_Pile_A,len_Pile_B)
			# i = 0 means Alice Turns
			i = 0


			if len_Pile_B == 0:                          # condition when Pile A is Empty 
				print("You cant pick Rock from Pile B")

			# BOB winning Algorithm 
			Bob = winning_recipe[len_Pile_A][len_Pile_B]


			if (len_Pile_B + len_Pile_A) == 0 :
				break 

			print("After Bob Turn :")
			# calling function Moves() where it pick up the items from Pile 
			Pile_A,Pile_B,len_Pile_A,len_Pile_B =  Moves(Bob,Pile_A,Pile_B,len_Pile_A,len_Pile_B)
			i = 1
			print("-------------------------------------------------------------------")


	if i == 0 : print("Alice Win\r")   # if  Alice play last Turn then She wins 
	else : print("Bob Win\r")          # if Bob play last Turns then Bob wins 



# calling function 
Ten_plus_Ten()


print("\rWhat happens for n+n ?")
print(">> It seems from the examples that if n if EVEN then we just have to follow same move that first player play. \n so second player must win if n is EVEN")
print(">> However if n is odd the first player must pick rock from both pile and then follow another player move to insure WIN.")



print("\rWhat if Piles are 3?")
print(">> it is unpredictable for 3 Piles.")
