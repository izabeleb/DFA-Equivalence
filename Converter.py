# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 03:49:47 2020

@author: Izabele
"""
from DFA import DFA
import sys

class Converter:
    
    def get_DFA_from_file (filename):
        f = open(filename, "r")
        num_states = f.readline().rstrip()
        states = f.readline().rstrip()
        states = states.split()
        alpha_size = f.readline().rstrip()
        alpha = f.readline().rstrip()
        alpha = alpha.split()
        trans_func = []
        for i in range(int(num_states)):
            trans_func.append(f.readline().rstrip())    
        transitions = []
        for trans in trans_func:
            transitions.append(trans.split())    
        start_state = f.readline().rstrip()
        num_accept_states = f.readline().rstrip() 
        accept_states = f.readline().rstrip().split()
        return DFA(states, alpha, transitions, start_state, accept_states)  
    
    def get_file_from_DFA(dfa, filename):
        if filename == "sys":
            f = sys.stdout
        else:
            f = open(filename, "w")

        f.write(str(len(dfa.states)))
        f.write("\n")
        f.write(" ".join(dfa.states))
        f.write("\n")
        f.write(str(len(dfa.alpha)))
        f.write("\n")
        f.write(" ".join(dfa.alpha))
        f.write("\n")
        for transition in dfa.transitions:
            f.write(" ".join(transition))
            f.write("\n")
        f.write(dfa.start_state)
        f.write("\n")
        f.write(str(len(dfa.accept_states)))
        f.write("\n")
        f.write(" ".join(dfa.accept_states))