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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\31")
        buf.write("\u00a3\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3")
        buf.write("\17\3\20\3\20\3\21\6\21j\n\21\r\21\16\21k\3\21\3\21\3")
        buf.write("\22\6\22q\n\22\r\22\16\22r\3\22\3\22\6\22w\n\22\r\22\16")
        buf.write("\22x\3\22\3\22\3\23\3\23\3\23\3\23\7\23\u0081\n\23\f\23")
        buf.write("\16\23\u0084\13\23\3\23\7\23\u0087\n\23\f\23\16\23\u008a")
        buf.write("\13\23\3\23\3\23\3\23\3\24\6\24\u0090\n\24\r\24\16\24")
        buf.write("\u0091\3\25\6\25\u0095\n\25\r\25\16\25\u0096\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\2\2\31\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\3")
        buf.write("\2\6\4\2\62;aa\3\2^^\4\2C\\c|\5\2\13\f\16\17\"\"\2\u00aa")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\3\61\3\2\2\2\5:\3\2\2\2\7?\3\2\2\2\tG\3\2")
        buf.write("\2\2\13M\3\2\2\2\rQ\3\2\2\2\17T\3\2\2\2\21X\3\2\2\2\23")
        buf.write("Z\3\2\2\2\25\\\3\2\2\2\27^\3\2\2\2\31`\3\2\2\2\33b\3\2")
        buf.write("\2\2\35d\3\2\2\2\37f\3\2\2\2!i\3\2\2\2#p\3\2\2\2%|\3\2")
        buf.write("\2\2\'\u008f\3\2\2\2)\u0094\3\2\2\2+\u009a\3\2\2\2-\u009d")
        buf.write("\3\2\2\2/\u00a0\3\2\2\2\61\62\7h\2\2\62\63\7w\2\2\63\64")
        buf.write("\7p\2\2\64\65\7e\2\2\65\66\7v\2\2\66\67\7k\2\2\678\7q")
        buf.write("\2\289\7p\2\29\4\3\2\2\2:;\7x\2\2;<\7q\2\2<=\7k\2\2=>")
        buf.write("\7f\2\2>\6\3\2\2\2?@\7k\2\2@A\7p\2\2AB\7v\2\2BC\7g\2\2")
        buf.write("CD\7i\2\2DE\7g\2\2EF\7t\2\2F\b\3\2\2\2GH\7h\2\2HI\7n\2")
        buf.write("\2IJ\7q\2\2JK\7c\2\2KL\7v\2\2L\n\3\2\2\2MN\7c\2\2NO\7")
        buf.write("p\2\2OP\7f\2\2P\f\3\2\2\2QR\7q\2\2RS\7t\2\2S\16\3\2\2")
        buf.write("\2TU\7p\2\2UV\7q\2\2VW\7v\2\2W\20\3\2\2\2XY\7?\2\2Y\22")
        buf.write("\3\2\2\2Z[\7*\2\2[\24\3\2\2\2\\]\7+\2\2]\26\3\2\2\2^_")
        buf.write("\7}\2\2_\30\3\2\2\2`a\7\177\2\2a\32\3\2\2\2bc\7.\2\2c")
        buf.write("\34\3\2\2\2de\7<\2\2e\36\3\2\2\2fg\7=\2\2g \3\2\2\2hj")
        buf.write("\t\2\2\2ih\3\2\2\2jk\3\2\2\2ki\3\2\2\2kl\3\2\2\2lm\3\2")
        buf.write("\2\2mn\b\21\2\2n\"\3\2\2\2oq\t\2\2\2po\3\2\2\2qr\3\2\2")
        buf.write("\2rp\3\2\2\2rs\3\2\2\2st\3\2\2\2tv\7\60\2\2uw\t\2\2\2")
        buf.write("vu\3\2\2\2wx\3\2\2\2xv\3\2\2\2xy\3\2\2\2yz\3\2\2\2z{\b")
        buf.write("\22\3\2{$\3\2\2\2|\u0088\7$\2\2}\u0087\n\3\2\2~\u0082")
        buf.write("\7^\2\2\177\u0081\n\3\2\2\u0080\177\3\2\2\2\u0081\u0084")
        buf.write("\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0083\3\2\2\2\u0083")
        buf.write("\u0085\3\2\2\2\u0084\u0082\3\2\2\2\u0085\u0087\7^\2\2")
        buf.write("\u0086}\3\2\2\2\u0086~\3\2\2\2\u0087\u008a\3\2\2\2\u0088")
        buf.write("\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008b\3\2\2\2")
        buf.write("\u008a\u0088\3\2\2\2\u008b\u008c\7$\2\2\u008c\u008d\b")
        buf.write("\23\4\2\u008d&\3\2\2\2\u008e\u0090\t\4\2\2\u008f\u008e")
        buf.write("\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u008f\3\2\2\2\u0091")
        buf.write("\u0092\3\2\2\2\u0092(\3\2\2\2\u0093\u0095\t\5\2\2\u0094")
        buf.write("\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0094\3\2\2\2")
        buf.write("\u0096\u0097\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u0099\b")
        buf.write("\25\5\2\u0099*\3\2\2\2\u009a\u009b\13\2\2\2\u009b\u009c")
        buf.write("\b\26\6\2\u009c,\3\2\2\2\u009d\u009e\13\2\2\2\u009e\u009f")
        buf.write("\b\27\7\2\u009f.\3\2\2\2\u00a0\u00a1\13\2\2\2\u00a1\u00a2")
        buf.write("\b\30\b\2\u00a2\60\3\2\2\2\13\2krx\u0082\u0086\u0088\u0091")
        buf.write("\u0096\t\3\21\2\3\22\3\3\23\4\b\2\2\3\26\5\3\27\6\3\30")
        buf.write("\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    INTEGER = 3
    FLOAT = 4
    AND = 5
    OR = 6
    NOT = 7
    EQ = 8
    LB = 9
    RB = 10
    LP = 11
    RP = 12
    COMMA = 13
    COLON = 14
    SEMI = 15
    INTLIT = 16
    FLOATLIT = 17
    STRINGLIT = 18
    ID = 19
    WS = 20
    ERROR_CHAR = 21
    UNCLOSE_STRING = 22
    ILLEGAL_ESCAPE = 23

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'function'", "'void'", "'integer'", "'float'", "'and'", "'or'", 
            "'not'", "'='", "'('", "')'", "'{'", "'}'", "','", "':'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "INTEGER", "FLOAT", "AND", "OR", "NOT", "EQ", "LB", "RB", "LP", 
            "RP", "COMMA", "COLON", "SEMI", "INTLIT", "FLOATLIT", "STRINGLIT", 
            "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "INTEGER", "FLOAT", "AND", "OR", "NOT", 
                  "EQ", "LB", "RB", "LP", "RP", "COMMA", "COLON", "SEMI", 
                  "INTLIT", "FLOATLIT", "STRINGLIT", "ID", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[15] = self.INTLIT_action 
            actions[16] = self.FLOATLIT_action 
            actions[17] = self.STRINGLIT_action 
            actions[20] = self.ERROR_CHAR_action 
            actions[21] = self.UNCLOSE_STRING_action 
            actions[22] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_','')
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_", "" )
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                    result = str(self.text)
                    self.text = result[1:-1]
                
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise UncloseString(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise IllegalEscape(self.text)
     


