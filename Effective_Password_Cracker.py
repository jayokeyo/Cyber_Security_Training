'''Using python's combination_with_replacement function
from the itertools module we can find all the possible 
ways of arranging the letters of the alphabet 
(both lowercase and uppercase) plus the special characters then
compare the resulting string to input user password in a
nid to guess the password. From these experiment it can be shown
that the longer the user password the harder it is to crack. 
Passwords longer than eight characters are very likely to trigger
a memory error.
Moreover, using a combination of uppercase, lowercase, numerical
values, and special characters makes it almost impossible to
crack the passwords.'''
from itertools import combinations_with_replacement as cwd
user_pass = input("Password: ")

password = ['a','b','c','d','e','f','g','h','i','j','k','l',
            'm','n','o','p','q','r','s','t','u','v','w','x',
            'y','z','A','B','C','D','E','F','G','H','I','J',
            'K','L','M','N','O','P','Q','R','S','T','U','V',
            'W','X','Y','Z','0','1','2','3','4','5','6','7',
            '8','9','~','!','@','#','$','%','^','&','*',]

comb = cwd(password,len(user_pass))
for trial in list(comb):
    guess_string = ""
    for i in trial:
        guess_string += str(i)
    print(guess_string)
    if guess_string == user_pass:
        print("User password is: ",guess_string)
        break
