import hashlib 

pwd="c4ca4238a0b923820dcc509a6f75849b"

epwd = input(" Enter Your Password : ")
result = hashlib.md5(epwd.encode()) 
final = result.hexdigest()
print (final)
if final == pwd :
	print ( " Password Matched ")
	import main.py
else :
	print (" Incorrect Password Entered ")