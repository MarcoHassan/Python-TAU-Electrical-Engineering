###############################
# Homework 3 
# Name: Marco Hassan
# Student ID: 981745755
###############################

###########
#Question 1
###########

ans = input("Please enter the number for which you intend to compute the geometric mean separated by a comma ',' ")

if len(ans) > 0:
    A = ans.split(',')

    a=1
    for i in range(0, len(A)):
        a = int(A[i]) * a
    a = a**(1/(len(A)))
    print("The geometrical mean is ", a)

else:
    print("NA")


###########
#Question 2
###########

A = input("Enter a string of words separated by a single space ")

A = A.split(" ")

for i in range(0, len(A)):
    if (i+1) % 3 == 0:
        A[i] = A[i-1]

print(A)

		
###########
#Question 3
###########

A = input("Enter a series of integers separated by a comma ',' ")
B = input("Enter a second series of integers separated by a comma ',' ")

A = A.split(',')
B = B.split(',')

print(A)
print(B)

A.sort(reverse = True)
print(A) ## si ferma al 5 elemento. da capire come mai?!
B.reverse()

print(B+A)


###########
#Question 4
###########

E = input("Enter the a series of numbers separated by a comma ',' ")

E = E.split(',')

bigger = True
b = []

if len(E) > 2:
    for i in range(-1, -len(E), -1):
        a = abs(int(E[i])-int(E[i-1]))
        b.append(a)

    for j in range(1, len(b)):
        if b[0] <= b[j]:
            bigger = False
            break

print(bigger)    

