'''This password cracker is only effective in machines with larger memory
space. The Comb_List generated is very long and has higher memory demand.
'''

from itertools import combinations_with_replacement as cwr

global User_Password
global string
global Comb_List
Comb_List = []
User_Password = str(input('Please enter the user password: ',))
string = 'abcdefghi'
#jklmnopqrstuvwxyz'
#ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*'

def All_Permutations():
    global Comb_List
    Comb = list(cwr(string,len(User_Password)))
    for comb in Comb:
        Trial = ''.join(comb)
        Comb_List.append(Trial)

def Try_Password():
    for comb in Comb_List:
        if comb == User_Password:
            print('User password is: ',comb)
            break

if __name__ == '__main__':
    All_Permutations()
    Try_Password()
