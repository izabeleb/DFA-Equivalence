# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 04:53:50 2020

@author: Izabele
"""
from Converter import Converter
from DFA import DFA

import sys

""" 
Task 4:
    Non-emptyness
"""

if __name__ == "__main__":
    filename = sys.argv[1]
    dfa1 = Converter.get_DFA_from_file(filename)
    print(DFA.accepted_path_exists(dfa1))
