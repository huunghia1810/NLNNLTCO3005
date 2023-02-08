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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\n")
        buf.write("@\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\7\5&\n\5\f\5\16\5)")
        buf.write("\13\5\3\5\7\5,\n\5\f\5\16\5/\13\5\3\5\3\5\3\6\6\6\64\n")
        buf.write("\6\r\6\16\6\65\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\t\3\t\2\2")
        buf.write("\n\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\3\2\4\3\2))\5\2")
        buf.write("\13\f\17\17\"\"\2C\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\3\23\3\2\2\2\5\30\3\2\2\2\7\34\3\2\2\2\t!\3\2")
        buf.write("\2\2\13\63\3\2\2\2\r9\3\2\2\2\17<\3\2\2\2\21>\3\2\2\2")
        buf.write("\23\24\7o\2\2\24\25\7c\2\2\25\26\7k\2\2\26\27\7p\2\2\27")
        buf.write("\4\3\2\2\2\30\31\7k\2\2\31\32\7p\2\2\32\33\7v\2\2\33\6")
        buf.write("\3\2\2\2\34\35\7x\2\2\35\36\7q\2\2\36\37\7k\2\2\37 \7")
        buf.write("f\2\2 \b\3\2\2\2!-\7)\2\2\",\n\2\2\2#\'\7)\2\2$&\n\2\2")
        buf.write("\2%$\3\2\2\2&)\3\2\2\2\'%\3\2\2\2\'(\3\2\2\2(*\3\2\2\2")
        buf.write(")\'\3\2\2\2*,\7)\2\2+\"\3\2\2\2+#\3\2\2\2,/\3\2\2\2-+")
        buf.write("\3\2\2\2-.\3\2\2\2.\60\3\2\2\2/-\3\2\2\2\60\61\7)\2\2")
        buf.write("\61\n\3\2\2\2\62\64\t\3\2\2\63\62\3\2\2\2\64\65\3\2\2")
        buf.write("\2\65\63\3\2\2\2\65\66\3\2\2\2\66\67\3\2\2\2\678\b\6\2")
        buf.write("\28\f\3\2\2\29:\13\2\2\2:;\b\7\3\2;\16\3\2\2\2<=\13\2")
        buf.write("\2\2=\20\3\2\2\2>?\13\2\2\2?\22\3\2\2\2\7\2\'+-\65\4\b")
        buf.write("\2\2\3\7\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    INTTYPE = 2
    VOIDTYPE = 3
    ID = 4
    WS = 5
    ERROR_CHAR = 6
    UNCLOSE_STRING = 7
    ILLEGAL_ESCAPE = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'int'", "'void'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "VOIDTYPE", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "INTTYPE", "VOIDTYPE", "ID", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[5] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


