# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("G\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\6\4(\n\4")
        buf.write("\r\4\16\4)\3\5\6\5-\n\5\r\5\16\5.\3\6\3\6\3\7\3\7\3\b")
        buf.write("\3\b\3\t\3\t\3\n\3\n\3\13\6\13<\n\13\r\13\16\13=\3\13")
        buf.write("\3\13\3\f\3\f\3\r\3\r\3\16\3\16\2\2\17\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\3\2\5")
        buf.write("\4\2C\\c|\4\2\62;aa\5\2\13\f\16\17\"\"\2I\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\3\35\3\2")
        buf.write("\2\2\5!\3\2\2\2\7\'\3\2\2\2\t,\3\2\2\2\13\60\3\2\2\2\r")
        buf.write("\62\3\2\2\2\17\64\3\2\2\2\21\66\3\2\2\2\238\3\2\2\2\25")
        buf.write(";\3\2\2\2\27A\3\2\2\2\31C\3\2\2\2\33E\3\2\2\2\35\36\7")
        buf.write("k\2\2\36\37\7p\2\2\37 \7v\2\2 \4\3\2\2\2!\"\7x\2\2\"#")
        buf.write("\7q\2\2#$\7k\2\2$%\7f\2\2%\6\3\2\2\2&(\t\2\2\2\'&\3\2")
        buf.write("\2\2()\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*\b\3\2\2\2+-\t\3\2")
        buf.write("\2,+\3\2\2\2-.\3\2\2\2.,\3\2\2\2./\3\2\2\2/\n\3\2\2\2")
        buf.write("\60\61\7*\2\2\61\f\3\2\2\2\62\63\7+\2\2\63\16\3\2\2\2")
        buf.write("\64\65\7}\2\2\65\20\3\2\2\2\66\67\7\177\2\2\67\22\3\2")
        buf.write("\2\289\7=\2\29\24\3\2\2\2:<\t\4\2\2;:\3\2\2\2<=\3\2\2")
        buf.write("\2=;\3\2\2\2=>\3\2\2\2>?\3\2\2\2?@\b\13\2\2@\26\3\2\2")
        buf.write("\2AB\13\2\2\2B\30\3\2\2\2CD\13\2\2\2D\32\3\2\2\2EF\13")
        buf.write("\2\2\2F\34\3\2\2\2\6\2).=\3\b\2\2")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTTYPE = 1
    VOIDTYPE = 2
    ID = 3
    INTLIT = 4
    LB = 5
    RB = 6
    LP = 7
    RP = 8
    SEMI = 9
    WS = 10
    ERROR_CHAR = 11
    UNCLOSE_STRING = 12
    ILLEGAL_ESCAPE = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'void'", "'('", "')'", "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "VOIDTYPE", "ID", "INTLIT", "LB", "RB", "LP", "RP", 
            "SEMI", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "INTTYPE", "VOIDTYPE", "ID", "INTLIT", "LB", "RB", "LP", 
                  "RP", "SEMI", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


