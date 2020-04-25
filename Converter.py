# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 03:49:47 2020

@author: Izabele
"""
from DFA import DFA
import sys

class Converter:
    
    @staticmethod
    def get_DFA_from_file (filename):
        """
        Returns a DFA class object with all ingredients populated from
        the specified file
        """
        f = open(filename, "r")
        
        # states
        num_states = f.readline().rstrip()
        states = f.readline().rstrip()
        states = states.split()
        # alphabet
        alpha_size = f.readline().rstrip()
        alpha = f.readline().rstrip()
        alpha = alpha.split()
        # transition function
        trans_func = []
        for i in range(int(num_states)):
            trans_func.append(f.readline().rstrip())    
        transitions = []
        for trans in trans_func:
            transitions.append(trans.split())  
        # start state
        start_state = f.readline().rstrip()
        # accept states
        num_accept_states = f.readline().rstrip() 
        accept_states = f.readline().rstrip().split()
        return DFA(states, alpha, transitions, start_state, accept_states)  
    
    @staticmethod
    def get_file_from_DFA(dfa, filename):
        # option to print to file or console
        if filename == "sys":
            f = sys.stdout
        else:
            f = open(filename, "w")

        # all elements of the DFA will be printed without the nested
        # list structure that might result from DFA operations
        
        # states
        f.write(str(len(dfa.states)))
        f.write("\n")
        if isinstance(dfa.states[0], list):
            new_states = []
            for state in dfa.states:
                new_states.append("".join(list(Converter.flatten_all(state))))
            f.write(" ".join(new_states))
        else:
            f.write(" ".join(dfa.states))
        
        # alphabet
        f.write("\n")
        f.write(str(len(dfa.alpha)))
        f.write("\n")
        f.write(" ".join(dfa.alpha))
        
        # transitions
        f.write("\n")
        for transition in dfa.transitions:
            if isinstance(transition[0], list):
                f.write("".join(list(Converter.flatten_all(transition[0]))))
                f.write(" ")
                f.write("".join(list(Converter.flatten_all(transition[1]))))
            else:   
                f.write(" ".join(transition))
            f.write("\n")
            
        # start state
        if isinstance(dfa.start_state, list):
            f.write("".join(list(Converter.flatten_all(dfa.start_state))))
        else:    
            f.write(dfa.start_state)
            
        # accept states
        f.write("\n")
        f.write(str(len(dfa.accept_states)))
        f.write("\n")
        if len(dfa.accept_states) > 0:
            if isinstance(dfa.accept_states[0], list):
                for acc_state in dfa.accept_states:
                    f.write("".join(Converter.flatten_all(acc_state)))
                    f.write(" ")
            else:
                f.write(" ".join(dfa.accept_states))
        else:
            f.write(" ".join(dfa.accept_states))
        
    @staticmethod
    def flatten_all(iterable):
        # generator code from https://stackoverflow.com/a/13414835
        # flattening lists 
        for elem in iterable:
            if not isinstance(elem, list):
                yield elem
            else:
                for x in Converter.flatten_all(elem):
                    yield x