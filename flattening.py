# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 04:03:50 2020

@author: Izabele
"""
 
def main():
     
    thing = [ ['A' ,' x ' ] ,   [ ' A ' ,   ' y ' ] ,   [ ' A ' ,   ' z ' ] ,
             [ ' B ' ,   ' x ' ] ,   [ ' B ' ,   ' y ' ] ,   [ ' B ' ,   ' z ' ] ]
    
    thing2 = [[['A', 'x'], ['A', 'y']],
              [['A', 'z'], ['B', 'x']],
              [['B', 'y'], ['B', 'z']]]
    
    
    for item in thing2:
        print("".join(list(flatten_all(item))))
    
    #thing3 = list(flatten_all(thing))
    #print(thing2)
    
    #li = [1, [2, [3]]]
    #my_lst = list(flatten_all(li))
    #print(my_lst)

def flatten_all(iterable):
    for elem in iterable:
        if not isinstance(elem, list):
            yield elem
        else:
            for x in flatten_all(elem):
                yield x
            
main()