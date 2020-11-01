print("")
print("\t \t SCHOOL MANAGEMENT ")
print("")

# Teacher file : teachdet.txt
# Student file : studdet.txt

print(" 1. Admit Teachers ")
print(" 2. Admit Students ")
print(" 3. Show Teachers ")
print(" 4. Show Students " )
print(" 5. About ")
print(" 6. Exit ")
print("")
c = int(input("Enter your Choice : ")) 

#### Teacher Area Start ####

if c == 1 :
	print("")
	print("\t \t Teachers Area  ")
	print("")

# Filename : teachdet.txt

	print(" 1. Add Limited Teachers ")
	print(" 2. Add Unlimited Teachers ")
	print(" 3. Show Teachers ")
	print("")
	c2 = int(input("Enter your Choice : "))

	if c2 == 1 :
#program to add limited teachers

		n2 = int(input("Enter number of Teachers : "))
		teachfile = open(r"teachdet.txt","a+")

		for i in range(n2) :
			print("") 
			print("Enter details of Teacher " ,(i+1), " below : ")
			name = input("Enter Name : ")
			post = input("Enter Post : ")
			sall = input("Enter Sallery : ")
			addr = input("Enter Address : ")

			det = "Name : "+name+"\nPost : "+post+"\nSallery : " +sall+"\nAddress : "+addr+"\n \n"
			teachfile.write(det)
		teachfile.close()
		print("")
		print(" Details Saved ")
		print("")

	elif c2 ==2 :
		print("< program comming soon >")
#program to add unlimited teachers

	elif c2 == 3 :
#program to display details

		teachfile = open(r"teachdet.txt")
		myfile = open(r"teachdet.txt" , "r")
		teachcont = teachfile.read()
		lines= myfile.readlines()
		tcount = len(lines)
		tcount = tcount/5
		#print(tcount)
		print("",tcount,"Teachers Record Founded ")
		print("")
		print(teachcont)
		teachfile.close()

	else :
		print (" Invalid Option Selected ")

#### Teacher Area Ended ####


elif c ==2 :
#### Student Area Start ####

	print("\t \t Students Area  ")
	print("")

# Filename : studdet.txt

	print(" 1. Add Limited Students ")
	print(" 2. Add Unlimited Students ")
	print(" 3. Show Students ")
	print("")
	c3 = int(input("Enter your Choice : ")) 

	if c3 == 1 :
#program to add limited students

		n3 = int(input("Enter number of Students : "))
		studfile = open(r"studdet.txt","a+")

		for i in range(n3) :
			print("")
			print(" Enter details of Student " ,(i+1), " below : ")
			name = input("Enter Name : ")
			clas = input("Enter Class: ")
			roll = input("Enter Roll Number : ")
			addr = input("Enter Address : ")

			det = "Name : "+name+"\nClass : "+clas+"\nRoll Number : " +roll+"\nAddress : "+addr+"\n \n"
			studfile.write(det)
		studfile.close()
		print("")
		print(" Details Saved")
		print("")

	elif c3 ==2 :
#program to add unlimited students
		print("")
		print(" Program Cooming soon ")
		
	elif c3 == 3 :
#program to display details

		studfile = open(r"studdet.txt","r")
		studcont = studfile.read()
		sfile = open(r"studdet.txt","r")
		lines = sfile.readlines()
		scount = len(slines)
		sfcount = teachlinecount/5
		print("", sfcount ," Students Record Founded ")
		print("")
		print(studcont)
		studfile.close()

	else :
		print (" Invalid Option Selected ")

#### Students Area Ended ####

elif c == 3 :
#program to display details
	print("")
	print(" Teacher Details ")
	print("")
	teachfile = open(r"teachdet.txt")
	teachcont = teachfile.read()
	myfile = open(r"teachdet.txt","r")
	s = myfile.readlines()
	count = len(s)
	tcount = count/5
	print("", tcount ," Teachers Record Founded ")
	print("")
	print(teachcont)
	teachfile.close()

elif c == 4 :
#program to display details

	print(" Students Detail ")
	studfile = open(r"studdet.txt")
	studcont = studfile.read()
	s2file = open("studdet.txt","r")
	s2lines = s2file.readlines()
	s2tcount = len(s2lines)
	s2count = s2tcount/5
	print("", s2count ," Students Record Founded ")
	print("")
	print(studcont)
	studfile.close()
	
elif c == 5 :
	print("\t \t \t  ABOUT \n ")
	print('''This Software is developed by DEVESH SINGH on Date Sunday 31 November 2020 With Love in India.

This ( SCHOOL MANAGEMENT SYSTEM ) software helps you to save and track teachers details , sallery and students information in simple fast and relaible way.

FEATURES
1 Add Definef number of teacher and students
2 Add unlimited teachers and students at a time
3 Show Teacher and Students details in mannerised way.
4 Easy to customisable

If you have any more ideas on features or find any bug or problem feel free to contact me at username@domain.extension.
Thank you for choosing my work 

''')

elif c == 6 :
	print(" \t \t THANKS FOR USING ME ")
	
else :
	print(" Invalid Option Selected " )
