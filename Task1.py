# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 01:09:53 2020

@author: Izabele
"""
from Converter import Converter
from DFA import DFA

import sys

if __name__ == "__main__":
    filename = sys.argv[1]
    dfa1 = Converter.get_DFA_from_file(filename)
    Converter.get_file_from_DFA(dfa1.get_complement(), "sys")
    
    
    