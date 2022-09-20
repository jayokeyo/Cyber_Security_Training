'''This password cracker is only effective in machines with larger memory
space. The Comb_List generated is very long and has higher memory demand.
'''

from itertools import combinations_with_replacement as cwr
from plumbum import cli

class Password_Cracker(cli.Application):                
    def Gen_Try_Permutations(self,user_password):
        self.user_password = user_password
        self.string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*'
        i = 0
        x = True
        while x:
            comb = list(cwr(self.string,len(self.user_password)))[i]
            #comb = Comb[i]
            for c in comb:
                Trial = ''.join(comb)
            i += 1
            yield Trial
            #The major difference between a list comprehension and a generator
            # expression is that a list comprehension produces the entire list
            # while the generator expression produces one item at a time.
            Trial = Trial
            if Trial == user_password:
                print('User password is: ',Trial)
                x = False

    def main(self):
        x = self.Gen_Try_Permutations(user_password)
        while True:
            next(x)
            print(next(x))

user_password = input('Password:')
if __name__ == '__main__':
    Password_Cracker.run()