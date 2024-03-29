# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 02:16:01 2020

@author: Izabele
"""
from Converter import Converter
from DFA import DFA

import sys

"""
Task 2:
    Intersection
"""

if __name__ == "__main__":
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]
    
    dfa1 = Converter.get_DFA_from_file(filename1)
    dfa2 = Converter.get_DFA_from_file(filename2)
    
    inter = DFA.get_intersect(dfa1, dfa2)
    
    Converter.get_file_from_DFA(inter, "sys")
    
    