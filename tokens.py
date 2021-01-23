EOF = "EOF"
PLUS = "PLUS"
MINUS = "MINUS"
MULT = "MULT"
DIV = "DIV"
INT = "INT"

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
    (None, None, None, None, None, 5, 8),
    [None]*7
]

index_to_token_type = {
    0: None,
    1: PLUS,
    2: MINUS,
    3: MULT,
    4: DIV,
    5: INT,
    6: SyntaxError("Invalid Character"),
    7: SyntaxError("Invalid Integer")
}

class Dfa:
    def __init__(self, state_table):
        self.state_table = state_table
        self.state = 0
        self.finished = False

    def next(self, next_input):
        """moves to the next state and returns it """
        new_state = self.state_table[self.state][next_input]
        if new_state is None:
            self.finished = True
            return None
        self.state = new_state
        return new_state


class LexerDfa(Dfa):
    def __init__(self):
        super().__init__(dfa_table)

    def next_state(self, char):
        char_inx = char_to_index(char)
        self.next(char_inx)

    def get_token_type(self):
        return index_to_token_type[self.state]
