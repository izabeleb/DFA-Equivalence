from Converter import Converter
from DFA import DFA

def main():
    #test1()
    #test2()
    
    DFA1 = Converter.get_DFA_from_file("D1.txt")
    DFA2 = Converter.get_DFA_from_file("D2.txt")
    
    newDFA = DFA.get_symmetric_diff(DFA1, DFA2)
    
    

def test3():
    pass

def test1():
    DFA1 = Converter.get_DFA_from_file("D1.txt")
    DFA2 = Converter.get_DFA_from_file("D2.txt")
    
    #DFA1_complement = DFA1.get_complement()
    DFA_intersect = DFA.get_intersect(DFA1, DFA2)
    print(DFA1.accepted_path_exists())
    print(DFA2.accepted_path_exists())
    
    DFA2.accept_states = ["y"]
    print(DFA2.accepted_path_exists())
    
    DFA2.accept_states = []
    print(DFA2.accepted_path_exists())
    
    dfa3 = DFA(['1', '2', '3', '4', '5', '6'], ['a', 'b'], 
               [['3', '2'], ['4', '2'], ['5', '4'], ['5', '4'], ['6', '6'], ['6', '6']],
               '1', ['5'])
    
    dfa4 = DFA(['1', '2', '3', '4'], ['a', 'b'],
               [['2', '1'], ['3', '2'], ['4', '4'], ['4', '4']],
               '1', ['3'])
    
    print(DFA.are_equivalent(DFA1, DFA2))
    print(DFA.are_equivalent(dfa3, dfa4))

def test2():
    dfa1 = Converter.get_DFA_from_file("D1.txt")
    dfa2 = Converter.get_DFA_from_file("D2.txt")
    dfa3 = DFA(['1', '2', '3', '4', '5', '6'], ['a', 'b'], 
               [['3', '2'], ['4', '2'], ['5', '4'], ['5', '4'], ['6', '6'], ['6', '6']],
               '1', ['5'])
    
    dfa4 = DFA(['1', '2', '3', '4'], ['a', 'b'],
               [['2', '1'], ['3', '2'], ['4', '4'], ['4', '4']],
               '1', ['3'])
    
    #Converter.get_file_from_DFA(dfa1, "test1.txt")
    #Converter.get_file_from_DFA(dfa2, "test2.txt")
    #Converter.get_file_from_DFA(dfa3, "test3.txt")
    #Converter.get_file_from_DFA(dfa4, "test4.txt")
    
    Converter.get_file_from_DFA(dfa4, "sys")
    
    
main()