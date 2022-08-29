'''This password cracker is only effective in machines with larger memory
space. The Comb_List generated is very long and has higher memory demand.
'''

from itertools import combinations_with_replacement as cwr
from plumbum import cli

class Password_Cracker(cli.Application):
    global User_Password
    global string
    global Comb_List
    Comb_List = []
    User_Password = str(input('Please enter the user password: ',))
    string = 'abcdefghi'
    #jklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*'

    def All_Permutations(self):
        global Comb_List
        Comb = list(cwr(string,len(User_Password)))
        for comb in Comb:
            Trial = ''.join(comb)
            Comb_List.append(Trial)
        print(Comb_List)

    def Try_Password(self):
        for comb in Comb_List:
            if comb == User_Password:
                print('User password is: ',comb)
                break

    def main(self):
        self.All_Permutations()
        self.Try_Password()

if __name__ == '__main__':
    Password_Cracker.run()