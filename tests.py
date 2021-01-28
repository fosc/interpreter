import unittest
from tokens import _Dfa, LexerDfa


def char_to_index(c):
    if c.isspace():
        return 0
    elif c == '+':
        return 1
    elif c == '-':
        return 2
    elif c == '*':
        return 3
    elif c == '/':
        return 4
    elif c.isdigit():
        return 5
    else:
        return 6

dfa_table = [
    # ' ', '+', '-', '*', '/', d, *
    ( 0, 1, 2, 3, 4, 5, 7),
    [None]*7,
    [None]*7,
    [None]*7,
    [None]*7,
    (6, 6, 6, 6, 6, 5, 8),
    [None]*7,
    [None]*7
]

class Test_Dfa(unittest.TestCase):

    def test_dfa(self):
        dfa = _Dfa(dfa_table)
        self.assertEqual(0, dfa.next(0))
        self.assertEqual(1, dfa.next(1))
        self.assertEqual(None, dfa.next(4))
        self.assertEqual(1, dfa._state)

    def test_dfa_2(self):
        dfa = _Dfa(dfa_table)
        self.assertEqual(5, dfa.next(5))
        self.assertEqual(5, dfa.next(5))
        self.assertEqual(6, dfa.next(0))
        self.assertEqual(None, dfa.next(3))
        self.assertEqual(6, dfa._state)

    def test_lexer_dfa(self):
        ldfa = LexerDfa()
        ldfa.next_state(' ')
        self.assertEqual(False, ldfa.finished)
        ldfa.next_state('+')
        self.assertEqual(False, ldfa.finished)
        ldfa.next_state('4')
        self.assertEqual(True, ldfa.finished)
