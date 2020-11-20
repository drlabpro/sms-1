import os
import hashlib

## login ##
def main() :
	os.system('clear')
	pwd="257bd922a614ae23238271abfc096567"
	print(" \t SCHOOL MANAGEMENT SYSTEM ")
	print()
	print(" Continue using password")
	print()
	epwd = input(" Enter Your Password : ")
	result = hashlib.md5(epwd.encode()) 
	final = result.hexdigest()
	if final == pwd :
		print()
		print ( " Password Matched ")
		os.system('sleep 0.5 && clear')
		menu()
	else :
		print (" Incorrect Password Entered ")
		print(" Exiting ")
		os.system('sleep 1')
		exit()
## Main menu ##
def menu() :
	print("\t \t SCHOOL MANAGEMENT SYSTEM ")
	print()
	print(" 1. Admit Teachers ")
	print(" 2. Admit Students ")
	print(" 3. Show Teachers ")
	print(" 4. Show Students " )
	print(" 5. Setting ")
	print(" 6. About ")
	print(" 7. Exit ")
	print()
	print()
	c1=input("Enter your Choice : ")
	
	if c1 == "1":
		teachmenu()
	elif c1=="2":
		studmenu()
	elif c1=="3":
		showteach()
	elif c1=="4":
		showstud()
	elif c1=="5":
		setting()
	elif c1=="6":
		about()
	elif c1=="7":
		exit()
	else:
		print(" Invalid Input ")

## teach menu ##
def teachmenu():
	os.system('sleep 0.5 && clear')
	print("\t \t Teachers Area  ")
	print()
	print(" 1. Add Limited Teachers ")
	print(" 2. Add Unlimited Teachers ")
	print(" 3. Show Teachers ")
	print() 
	print( " 4. Main Menu ") 
	print()
	c2 = input("Enter your Choice : ")
	
	if c2 =="1":
		addlteach()
	elif c2 =="2":
		addteach()
	elif c2 =="3":
		showteach()
	elif c2 =="4":
		menu()
	else:
		print("Invalid Input")
		teachmenu()

## stud menu ##
def studmenu():
	os.system('sleep 0.5 && clear')
	print("\t \t Students Area  ")
	print()
	print(" 1. Add Limited Students ")
	print(" 2. Add Unlimited Students ")
	print(" 3. Show Students ")
	print()
	print(" 4. Main Menu " ) 
	c3 = int(input("Enter your Choice : ")) 
	
	if c3 =="1":
		addlstud()
	elif c2 =="2":
		addstud()
	elif c2 =="3":
		showstud()
	elif c2 =="4":
		menu()
	else:
		print(" Invalid Input ")
		studmenu()

## show tech ##
def showteach():
	os.system('sleep 0.5 && clear')
	print(" Teacher Details ")
	print()
	teachfile = open(r"teachdet.txt")
	teachcont = teachfile.read()
	myfile = open(r"teachdet.txt","r")
	s = myfile.readlines()
	count = len(s)
	tcount = count/5
	print( tcount ," Teachers Record Founded ")
	print()
	print(teachcont)
	teachfile.close()
	menu()

## show stud ##
def showstud():
	os.system('sleep 0.5 && clear')
	print(" Students Detail ")
	studfile = open(r"studdet.txt")
	studcont = studfile.read()
	s2file = open("studdet.txt","r")
	s2lines = s2file.readlines()
	s2tcount = len(s2lines)
	s2count = s2tcount/5
	print(s2count ," Students Record Founded ")
	print()
	print(studcont)
	studfile.close()
	menu()

## about ##
def about():
	os.system('sleep 0.5 && clear')
	print("\t \t \t  ABOUT \n ")
	print('''This Software is developed by DEVESH SINGH on Date Sunday 31 November 2020 With Love in India.

This ( SCHOOL MANAGEMENT SYSTEM ) software helps you to save and track teachers details , sallery and students information in simple fast and relaible way.

FEATURES
1 Add Definef number of teacher and students
2 Add unlimited teachers and students at a time
3 Show Teacher and Students details in mannerised way.
4 Easy to customisable ( Premium )

If you have any more ideas on features or find any bug or problem feel free to contact me at username@domain.extension.
Thank you for choosing my work 

''')
	menu()

## exit ##
def exit():
	os.system('clear')
	print("[!]   Closing this system..")
	os.system('sleep 1 && clear')
	os.sys.exit()

## add l tech ##
def addlteach():
	n2 = int(input("Enter number of Teachers : "))
	teachfile = open(r"teachdet.txt","a+")
	for i in range(n2) :
		print() 
		print("Enter details of Teacher " ,(i+1), " below : ")
		name = input("Enter Name : ")
		post = input("Enter Post : ")
		sall = input("Enter Sallery : ")
		addr = input("Enter Address : ")

		det = "Name : "+name+"\nPost : "+post+"\nSallery : " +sall+"\nAddress : "+addr+"\n \n"
		teachfile.write(det)
	teachfile.close()
	print()
	print(" Details Saved ")
	print()
	teachmenu()
	
## add tech ##
def addtech():
	print(" Program Coming Soon ")
	
## add l stud ##
def addlstud():
	n3 = int(input("Enter number of Students : "))
	studfile = open(r"studdet.txt","a+")
	for i in range(n3) :
		print()
		print(" Enter details of Student " ,(i+1), " below : ")
		name = input("Enter Name : ")
		clas = input("Enter Class: ")
		roll = input("Enter Roll Number : ")
		addr = input("Enter Address : ")

		det = "Name : "+name+"\nClass : "+clas+"\nRoll Number : " +roll+"\nAddress : "+addr+"\n \n"
		studfile.write(det)
	studfile.close()
	print()
	print(" Details Saved")
	print()
	studmenu()

##add stud ##
def addstud():
	print(" Program coming soon")

## setting ##
def setting():
	os.system('sleep 0.5 && clear')
	print("Work in progress")
	print()
	menu()
	
	
if __name__ == "__main__": 
	main()