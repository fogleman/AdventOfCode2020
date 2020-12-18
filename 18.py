import fileinput
import ply.lex as lex
import ply.yacc as yacc

tokens = ['LPAREN', 'RPAREN', 'ADD', 'MUL', 'NUMBER']

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ADD = r'\+'
t_MUL = r'\*'
t_ignore = ' \n'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# part 1
precedence = [('left', 'ADD', 'MUL')]

# part 2 (comment out to run part 1)
precedence = [('left', 'MUL'), ('left', 'ADD')]

def p_expression_binary_op(t):
    '''expression : expression ADD expression
                  | expression MUL expression'''
    if t[2] == '+':
        t[0] = t[1] + t[3]
    else:
        t[0] = t[1] * t[3]

def p_expression_paren(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]

def p_expression_number(t):
    'expression : NUMBER'
    t[0] = t[1]

lexer = lex.lex(errorlog=lex.NullLogger())
parser = yacc.yacc(debug=False, write_tables=False, errorlog=yacc.NullLogger())

def parse(text):
    return parser.parse(text, lexer=lexer)

lines = list(fileinput.input())
print(sum(parse(line) for line in lines))
