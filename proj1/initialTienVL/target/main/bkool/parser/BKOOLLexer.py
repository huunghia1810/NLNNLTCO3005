# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\33")
        buf.write("\u0089\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17")
        buf.write("\3\17\3\20\3\20\3\21\6\21\\\n\21\r\21\16\21]\3\22\6\22")
        buf.write("a\n\22\r\22\16\22b\3\23\6\23f\n\23\r\23\16\23g\3\23\3")
        buf.write("\23\6\23l\n\23\r\23\16\23m\3\24\6\24q\n\24\r\24\16\24")
        buf.write("r\3\25\6\25v\n\25\r\25\16\25w\3\26\6\26{\n\26\r\26\16")
        buf.write("\26|\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\2\2\33\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26")
        buf.write("+\27-\30/\31\61\32\63\33\3\2\7\3\2\62;\4\2C\\c|\3\2c|")
        buf.write("\5\2\62;C\\c|\5\2\13\f\17\17\"\"\2\u008f\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\3\65\3\2\2\2\5;\3\2\2\2\7>\3\2\2")
        buf.write("\2\t@\3\2\2\2\13B\3\2\2\2\rD\3\2\2\2\17F\3\2\2\2\21H\3")
        buf.write("\2\2\2\23J\3\2\2\2\25M\3\2\2\2\27P\3\2\2\2\31R\3\2\2\2")
        buf.write("\33T\3\2\2\2\35V\3\2\2\2\37X\3\2\2\2![\3\2\2\2#`\3\2\2")
        buf.write("\2%e\3\2\2\2\'p\3\2\2\2)u\3\2\2\2+z\3\2\2\2-~\3\2\2\2")
        buf.write("/\u0082\3\2\2\2\61\u0085\3\2\2\2\63\u0087\3\2\2\2\65\66")
        buf.write("\7c\2\2\66\67\7t\2\2\678\7t\2\289\7c\2\29:\7{\2\2:\4\3")
        buf.write("\2\2\2;<\7,\2\2<=\7,\2\2=\6\3\2\2\2>?\7\60\2\2?\b\3\2")
        buf.write("\2\2@A\7-\2\2A\n\3\2\2\2BC\7/\2\2C\f\3\2\2\2DE\7,\2\2")
        buf.write("E\16\3\2\2\2FG\7\61\2\2G\20\3\2\2\2HI\7\'\2\2I\22\3\2")
        buf.write("\2\2JK\7A\2\2KL\7A\2\2L\24\3\2\2\2MN\7?\2\2NO\7@\2\2O")
        buf.write("\26\3\2\2\2PQ\7.\2\2Q\30\3\2\2\2RS\7*\2\2S\32\3\2\2\2")
        buf.write("TU\7+\2\2U\34\3\2\2\2VW\7=\2\2W\36\3\2\2\2XY\7?\2\2Y ")
        buf.write("\3\2\2\2Z\\\t\2\2\2[Z\3\2\2\2\\]\3\2\2\2][\3\2\2\2]^\3")
        buf.write("\2\2\2^\"\3\2\2\2_a\t\3\2\2`_\3\2\2\2ab\3\2\2\2b`\3\2")
        buf.write("\2\2bc\3\2\2\2c$\3\2\2\2df\t\2\2\2ed\3\2\2\2fg\3\2\2\2")
        buf.write("ge\3\2\2\2gh\3\2\2\2hi\3\2\2\2ik\7\60\2\2jl\t\2\2\2kj")
        buf.write("\3\2\2\2lm\3\2\2\2mk\3\2\2\2mn\3\2\2\2n&\3\2\2\2oq\t\3")
        buf.write("\2\2po\3\2\2\2qr\3\2\2\2rp\3\2\2\2rs\3\2\2\2s(\3\2\2\2")
        buf.write("tv\t\4\2\2ut\3\2\2\2vw\3\2\2\2wu\3\2\2\2wx\3\2\2\2x*\3")
        buf.write("\2\2\2y{\t\5\2\2zy\3\2\2\2{|\3\2\2\2|z\3\2\2\2|}\3\2\2")
        buf.write("\2},\3\2\2\2~\177\t\6\2\2\177\u0080\3\2\2\2\u0080\u0081")
        buf.write("\b\27\2\2\u0081.\3\2\2\2\u0082\u0083\13\2\2\2\u0083\u0084")
        buf.write("\b\30\3\2\u0084\60\3\2\2\2\u0085\u0086\13\2\2\2\u0086")
        buf.write("\62\3\2\2\2\u0087\u0088\13\2\2\2\u0088\64\3\2\2\2\n\2")
        buf.write("]bgmrw|\4\b\2\2\3\30\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    DSTAR = 2
    DOT = 3
    ADD = 4
    SUB = 5
    MUL = 6
    DIV = 7
    MOD = 8
    DQUES = 9
    ARROW = 10
    COMMA = 11
    LB = 12
    RB = 13
    SEMI = 14
    EQ = 15
    INTLIT = 16
    STRINGLIT = 17
    FLOATLIT = 18
    ID = 19
    VARNAME = 20
    PAIRNAME = 21
    WS = 22
    ERROR_CHAR = 23
    UNCLOSE_STRING = 24
    ILLEGAL_ESCAPE = 25

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'array'", "'**'", "'.'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'??'", "'=>'", "','", "'('", "')'", "';'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "DSTAR", "DOT", "ADD", "SUB", "MUL", "DIV", "MOD", "DQUES", 
            "ARROW", "COMMA", "LB", "RB", "SEMI", "EQ", "INTLIT", "STRINGLIT", 
            "FLOATLIT", "ID", "VARNAME", "PAIRNAME", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "DSTAR", "DOT", "ADD", "SUB", "MUL", "DIV", "MOD", 
                  "DQUES", "ARROW", "COMMA", "LB", "RB", "SEMI", "EQ", "INTLIT", 
                  "STRINGLIT", "FLOATLIT", "ID", "VARNAME", "PAIRNAME", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[22] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


