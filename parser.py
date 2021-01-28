"""Create an abstract syntax tree"""
from copy import copy
from lexer import Lexer
from tokens import *


class AstNode:
    def __init__(self, token):
        self.token = token

    def __str__(self):
        return str(self.token)


class BinaryOpNode(AstNode):
    def __init__(self, token, left_node, right_node):
        super().__init__(token)
        self.left_child = left_node
        self.right_child = right_node

    def __str__(self):
        return f'({str(self.left_child)}, {self.token}, {str(self.right_child)})'


class Parser:
    def __init__(self, tkns):
        self.tokens = tkns
        self.pos = -1
        self.current_token = None
        self.advance()

    def advance(self, type_check=None):
        """return the current token and then move to next token"""
        prev_token = copy(self.current_token)
        if type_check:
            assert prev_token.type == type_check
        if self.pos + 1 < len(self.tokens):
            self.pos += 1
            self.current_token = self.tokens[self.pos]
        return prev_token

    def term(self, left_node):
        """
        term --> factor (+- factor)*
        return an Ast or leaf node (Token)
        """
        if self.current_token.type in (PLUS, MINUS):
            this_op = self.advance()
            next_num = self.advance()
            return BinaryOpNode(this_op, left_node, self.term(self.factor(next_num)))
        return left_node

    def factor(self, left_node):
        """
        factor --> Int(*/ Int)*
        return an Ast or leaf node (Token)
        """
        if self.current_token.type in (MULT, DIV):
            this_op = self.advance()
            next_num = self.advance()
            return BinaryOpNode(this_op, left_node, self.factor(next_num))
        return left_node

    def expr(self):
        """
        expr --> term
        """
        this_tkn = self.advance()
        print(self.term(self.factor(this_tkn)))


if __name__ == "__main__":
    while True:
        lexer = Lexer(input("raven>") + '\n')
        TOKENS = list()
        TOKENS.append(lexer.current_token)
        while lexer.current_token.type != EOF:
            lexer.advance()
            TOKENS.append(lexer.current_token)
        print(TOKENS)
        parser = Parser(TOKENS)
        parser.expr()
