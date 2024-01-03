"""Giving Multiple Values as Inputs at a time"""
x=input("Enter the values with space as seperating Component : ")
x,y,z=x.split(" ")
print(x,y,z)
print((x<y) or (not(z==y)) and (z<x))
#2
#print("hare rama"*2-5)#Will Give An Error
#3
#When we use relational operators in strings they will gives output by considering ASCII values
print("hare" < "Rama Krishna")
print("bye" >"Bye")
print((7/4<6 and " I am fine")) # When  we do and Operation Between 2 truly values it always returnthr
#SECOND  as Answer
#7
#print(a=6) ==> TYPE_ERROR
#print(a==6) ==> NAME_ERROR
"""
wHEN WE ASSIGN A VALUE WITHOUT DECALRING IN PREVIOUYS IT WILL YIELD TYPE ERROR
AND WHEN WE USE A VARIABLE IN RELATIONAL OPERATORS WHICH ARE NIOT CREATED WILL GET NAME_ERROR"""
#10
print("Give the values by seperating with space in order a,b,c")
x=input()
a,b,c=x.split(" ")
a,b,c=int(a),int(b),int(c)
root1=(-b+((b**2)-4*a*c)**0.5)/(2*a)
root2=(-b-((b**2)-4*a*c)**0.5)/(2*a)
print(root1,root2)