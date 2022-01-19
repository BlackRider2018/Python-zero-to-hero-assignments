name=input("Enter Your Name : ")
school=input("Enter School Name :")
town=input("Enter Your Town : ")
hs=float(input("Enter H.S. percentage : "))
college=input("Enter name of College name : ")
cgpa=float(input("Enter college CGPA : "))
no_attempt=int(input("In how many years you completed the college : "))

print("***---> Here is BIO, genarated from the information provided by You <---*** \n \n\n" )

print(f''' My name is {name}, basically I am from {town}. I have done my schooling from {school}. I have secured {hs} percentage in HS. I have done my graduation from {college} & secured {cgpa} CGPA. I have completed my college in {no_attempt} years.\n''')

print(''' My name is %s, basically I am from %s. I have done my schooling from %s. I have secured %s percentage in HS. I have done my graduation from %s & secured %s CGPA. I have completed my college in %s years.\n'''%(name,town,school,hs,college,cgpa,no_attempt)) 

print(''' My name is {}, basically I am from {}. I have done my schooling from {}. I have secured {} percentage in HS. I have done my graduation from {} & secured {} CGPA. I have completed my college in {} years.\n '''.format(name,town,school,hs,college,cgpa,no_attempt)) 

print(''' My name is {0}, basically I am from {1}. I have done my schooling from {2}. I have secured {3} percentage in HS. I have done my graduation from {4} & secured {5} CGPA. I have completed my college in {6} years.\n '''.format(name,town,school,hs,college,cgpa,no_attempt))


if (no_attempt==3):
    print("You have NO EXTRA years in college\n")
else:
    print(f"You have EXTRA {no_attempt - 3} years in college\n")