# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 05:00:04 2020

@author: Izabele
"""
from Converter import Converter
from DFA import DFA

import sys

"""
Task 5:
    Equivalence
"""

if __name__ == "__main__":
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]
    
    dfa1 = Converter.get_DFA_from_file(filename1)
    dfa2 = Converter.get_DFA_from_file(filename2)
    
    print(DFA.are_equivalent(dfa1, dfa2))