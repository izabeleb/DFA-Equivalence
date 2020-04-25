# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 03:34:56 2020 
@author: Izabele
"""

class DFA:
    """
    DFA class that contains the states, alphabet, transition function, start
    state, and accept states of a DFA
    """
    
    def __init__(self, states, alpha, transitions, start_state, accept_states):
        """
        example input
        
        states = ['q1', 'q2', 'q3']
        alpha = ['a', 'b']
        transitions = [
                        ['q2', 'q3'],
                        ['q1', 'q1'],
                        ['q3', 'q1']
                        ]
        start_state = 'q1'
        accept_states = ['q2', 'q3']
        
        
        transition function: each row represents a state, and each column
        represents a string in the alphabet
        """
        self.states = states
        self.alpha = alpha
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states
        
    def get_complement(self):
        copy = DFA(self.states, self.alpha, self.transitions, self.start_state, self.accept_states)
        complement_accept_states = []
        for char in copy.states:
            if char not in copy.accept_states:
                complement_accept_states.append(char)
        copy.accept_states = complement_accept_states
        return copy
    
    def get_transition(self, state, char):
        # get next transition state from current state and input string read
        row = self.states.index(state)
        col = self.alpha.index(char)
        return self.transitions[row][col]
    
    def get_possible_transitions(self, state):
        # used in DFS to go through all possible transition states
        # and find if an accepted string exists in the language
        return self.transitions[self.states.index(state)]
    
    def accepted_path_exists(self):
        if len(self.accept_states) == 0:
            return "language empty"        
        elif self.start_state in self.accept_states:
            return "language non-empty - e accepted"
        else:
            accept_string = self.DFS([], self.start_state, "", "")
            if accept_string == None:
                return "language empty"
            else:
                return "language non-empty - " + accept_string + " accepted"
            
    def DFS(self, visited, state, char, path):
        # goes through all possible transitions via the transition functions
        # and determines if an accept string exists
        visited.append(state)
        path += char
        if state in self.accept_states:
            return path
        for possible_state in self.get_possible_transitions(state):
            if possible_state not in visited:
                char_index = self.get_possible_transitions(state).index(possible_state)
                return self.DFS(visited, possible_state, self.alpha[char_index], path)
    
    @staticmethod
    def get_intersect(dfa1, dfa2):
        # alphabet
        if dfa1.alpha != dfa2.alpha:
            raise NonMatchingAlphabetError
        else:
            alpha = dfa1.alpha
        # states
        states = []
        for s1 in dfa1.states:
            for s2 in dfa2.states:
                states.append(str(s1) + str(s2))
        # transitions
        transitions = [] 
        for state in states:
            row = []
            for char in alpha:
                transition1 = dfa1.get_transition(state[0], char)
                transition2 = dfa2.get_transition(state[1], char)
                row.append(str(transition1) + str(transition2))
            transitions.append(row)
        # state state
        start_state = str(dfa1.start_state) + str(dfa2.start_state)
        # accept states
        accept_states = []
        for accept_state1 in dfa1.accept_states:
            for accept_state2 in dfa2.accept_states:
                accept_states.append(str(accept_state1) + str(accept_state2))
        # completed dfa
        return DFA(states, alpha, transitions, start_state, accept_states)
    
    @staticmethod
    def get_symmetric_diff(dfa1, dfa2):
        """
        Using DFA's D1 and D2
        (D1' ∩ D2) u (D1 ∩ D2')
        """
        return DFA.get_union(DFA.get_intersect(dfa1.get_complement(), dfa2),
        DFA.get_intersect(dfa1, dfa2.get_complement()))
    
    @staticmethod
    def get_union(dfa1, dfa2):
        inter_DFA = DFA.get_intersect(dfa1, dfa2)
        accept_states = []
        for s1 in dfa1.states:
            for s2 in dfa2.states:
                if (s1 in dfa1.accept_states) or (s2 in dfa2.accept_states):    
                    accept_states.append(str(s1) + str(s2))
        inter_DFA.accept_states = accept_states
        return inter_DFA
    
    @staticmethod
    def are_equivalent(dfa1, dfa2):
        if (DFA.get_symmetric_diff(dfa1, dfa2).accepted_path_exists() == "language empty"):
            return True
        else:
            return False
    
class NonMatchingAlphabetError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return "alphabets of both DFAs must be matching to get their intersection"