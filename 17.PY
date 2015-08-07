n=eval(raw_input("enter the number of subjects:"))
sub1=['maths','physics','chemistry','computer','english']
sub={}
for i in range(0,n):
        print "enter marks of" + sub1[i] + ":"
        sub[sub1[i]]=eval(raw_input())
print sub
	
	
	 
