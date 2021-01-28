from tokens import LexerDfa, EOF


class Token:
    def __init__(self, tok_type, value):
        self.type = tok_type
        self.value = value

    def __str__(self):
        return f'Token({self.type}, {self.value})'

    def __repr__(self):
        return str(self)


class Lexer:
    def __init__(self, text):
        self.pos = 0
        self.text = text
        self.current_token = None
        self.advance()
        print("done init")

    def advance(self):
        """using a LexerDfa find the next Token and assign it to self.current_token"""
        chars = ''
        tokenizer = LexerDfa()
        while self.pos < len(self.text):
            tokenizer.next_state(self.text[self.pos])
            if not tokenizer.finished:
                chars += self.text[self.pos]
                self.pos += 1
            else:
                self.current_token = Token(tokenizer.get_token_type(), chars.strip())
                return
        self.current_token = Token(EOF, None)


if __name__ == "__main__":
    while True:
        lexer = Lexer(input("raven>") + '\n')
        while lexer.current_token.type != EOF:
            lexer.advance()
