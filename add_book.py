# id (1) save name and surr_name 
# phone number 'int' + address 'str'
# class (list or dict)
# methods  add change delete search save load
#
#
#

from random import randint

class Person:
    def __init__ (self,name,surname,phone,address):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.address = address

class AddressBook:     
    def __init__ (self):
        self.book = []
    def show(self):
        max_space = [0,0,0,0]
        id_p = 0
        for person in self.book:
            id_p += 1
            max_space[0] = max(max_space[0],len(str(id_p)))
            max_space[1] = max(max_space[1],len(person.name + person.surname)+1)
            max_space[2] = max(max_space[2],len(str(person.phone)))
            max_space[3] = max(max_space[3],len(person.address))
        id_p = 0
        for person in self.book:
            id_p += 1
            str_id = str(id_p)
            res = ' '*(max_space[0]-len(str_id))+str_id
            res += ' | '
            res += ' '*(max_space[1] - len(person.name + person.surname) - 1) + person.name + ' ' + person.surname
            res += ' | '
            res += ' '*(max_space[2] - len(str(person.phone))) + str(person.phone)
            res += ' | '
            res += ' '*(max_space[3] - len(person.address)) + person.address

            print(res)

    
    def add(self,person):
        self.book.append(person)

def random_str (min_l,max_l):
    res = chr ( randint (65, 90))
    
    for i in range (randint(min_l,max_l)-1):
        res += chr ( randint (97, 122))
    return res



book1 = AddressBook()

for i in range (10):
    person1 = Person( random_str(4,12), random_str(4,12) , randint(1e+3, 1e+10) , random_str(5,17))
    book1.add(person1)

book1.show()
'''
1000 | s a     |    1 |   none |
  11 | Bob Sur | 1234 | bottom |
   2 | Bob Sur | 1234 | bottom |

n = [4, 7, 4, 6]
b = [1, 1, 1, 1]  ' ' * (n[i]-b[i]) + str(i) 
'''