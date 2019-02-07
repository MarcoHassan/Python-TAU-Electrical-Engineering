''' Homework #2. Python for Engineers.'''
''' Marco Hassan and 981745755.'''

#---Question-1-----------------------------------------------------------------

donor = input("Please, donor, enter your blod type ")
recipient = input("Please, recipient, enter your blod type ")

while donor not in ("A", "B", "AB", "O") or recipient not in ("A","B", "AB", "O") :
    print("Sorry, there was an input-mistake")
    donor = input("Please, donor, enter your blod type ")
    recipient = input("Please, recipient, enter your blod type ")
    donor
    recipient

 
if donor == "AB" and recipient == "AB":
    print("True")

elif donor == "B" and (recipient =="B" or recipient =="AB"):
    print("True")

elif donor == "A" and (recipient == "A" or recipient =="AB"):
    print("True")

elif donor == "O":
    print("True")

else:
    print("False")


##---Question-2-----------------------------------------------------------------

k = int(input("Please enter a digit between 1 and 9 "))
n= int(input("Please enter a positve integer "))

for i in range(1,n+1):
    digit_k = str(k)
    digit_n = str(i)
    
    if i % k == 0 and (digit_k in digit_n):
        print("boom-boom!")

    elif i % k == 0:
        print("boom!")

    else:
        print(i)

#---Question-3-----------------------------------------------------------------

str1 = input("Please enter a string ")

if len(str1) < 6:
    print("No")

elif len(str1) % 2 != 0 and str1[0:4] == str1[-4:] and str1[5] == "R" or str1[5] == "r" and str1[((len(str1)+1)//2)-2:((len(str1)+1)//2)+1] == str1[-1:-4:-1]:
    print("Yes")
    
else:
    print("No")

#---Question-4-----------------------------------------------------------------

text = input("Please enter a string ")

for i in range(0, (len(text)+1)):
    if i == len(text):
        print()
        break
    elif str.isalpha(text[i]):
        if str.islower(text[i]):
            print(str.upper(text[i]), end = "")
        else:
            print(str.lower(text[i]), end = "")
    elif str.isdigit(text[i]):
        if text[i] == "9":
            print(0, end = "")
        else:
            a = int(text[i])+1
            print(a, end = "")
    else:
        print(text[i], end = "")
