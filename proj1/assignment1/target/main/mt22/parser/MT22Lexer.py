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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u0146\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\25\3\25")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3")
        buf.write("!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3")
        buf.write("\'\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,\6,\u0109\n,\r,\16")
        buf.write(",\u010a\3,\3,\3-\6-\u0110\n-\r-\16-\u0111\3-\3-\6-\u0116")
        buf.write("\n-\r-\16-\u0117\3-\3-\3.\3.\5.\u011e\n.\3/\3/\3/\3/\7")
        buf.write("/\u0124\n/\f/\16/\u0127\13/\3/\7/\u012a\n/\f/\16/\u012d")
        buf.write("\13/\3/\3/\3/\3\60\6\60\u0133\n\60\r\60\16\60\u0134\3")
        buf.write("\61\6\61\u0138\n\61\r\61\16\61\u0139\3\61\3\61\3\62\3")
        buf.write("\62\3\62\3\63\3\63\3\63\3\64\3\64\3\64\2\2\65\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\63e\64g\65\3\2\6\4\2\62;aa\3\2^^\4\2")
        buf.write("C\\c|\5\2\13\f\16\17\"\"\2\u014e\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3")
        buf.write("\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\3i\3\2\2\2\5o")
        buf.write("\3\2\2\2\7x\3\2\2\2\t}\3\2\2\2\13\u0081\3\2\2\2\r\u0084")
        buf.write("\3\2\2\2\17\u008b\3\2\2\2\21\u008e\3\2\2\2\23\u0094\3")
        buf.write("\2\2\2\25\u0099\3\2\2\2\27\u009f\3\2\2\2\31\u00a7\3\2")
        buf.write("\2\2\33\u00ad\3\2\2\2\35\u00b4\3\2\2\2\37\u00bc\3\2\2")
        buf.write("\2!\u00c1\3\2\2\2#\u00ca\3\2\2\2%\u00cd\3\2\2\2\'\u00d1")
        buf.write("\3\2\2\2)\u00d3\3\2\2\2+\u00d5\3\2\2\2-\u00d7\3\2\2\2")
        buf.write("/\u00d9\3\2\2\2\61\u00db\3\2\2\2\63\u00dd\3\2\2\2\65\u00df")
        buf.write("\3\2\2\2\67\u00e1\3\2\2\29\u00e3\3\2\2\2;\u00e5\3\2\2")
        buf.write("\2=\u00e7\3\2\2\2?\u00e9\3\2\2\2A\u00eb\3\2\2\2C\u00ed")
        buf.write("\3\2\2\2E\u00ef\3\2\2\2G\u00f2\3\2\2\2I\u00f5\3\2\2\2")
        buf.write("K\u00f8\3\2\2\2M\u00fb\3\2\2\2O\u00fd\3\2\2\2Q\u00ff\3")
        buf.write("\2\2\2S\u0102\3\2\2\2U\u0105\3\2\2\2W\u0108\3\2\2\2Y\u010f")
        buf.write("\3\2\2\2[\u011d\3\2\2\2]\u011f\3\2\2\2_\u0132\3\2\2\2")
        buf.write("a\u0137\3\2\2\2c\u013d\3\2\2\2e\u0140\3\2\2\2g\u0143\3")
        buf.write("\2\2\2ij\7d\2\2jk\7t\2\2kl\7g\2\2lm\7c\2\2mn\7m\2\2n\4")
        buf.write("\3\2\2\2op\7e\2\2pq\7q\2\2qr\7p\2\2rs\7v\2\2st\7k\2\2")
        buf.write("tu\7p\2\2uv\7w\2\2vw\7g\2\2w\6\3\2\2\2xy\7g\2\2yz\7n\2")
        buf.write("\2z{\7u\2\2{|\7g\2\2|\b\3\2\2\2}~\7h\2\2~\177\7q\2\2\177")
        buf.write("\u0080\7t\2\2\u0080\n\3\2\2\2\u0081\u0082\7k\2\2\u0082")
        buf.write("\u0083\7h\2\2\u0083\f\3\2\2\2\u0084\u0085\7t\2\2\u0085")
        buf.write("\u0086\7g\2\2\u0086\u0087\7v\2\2\u0087\u0088\7w\2\2\u0088")
        buf.write("\u0089\7t\2\2\u0089\u008a\7p\2\2\u008a\16\3\2\2\2\u008b")
        buf.write("\u008c\7f\2\2\u008c\u008d\7q\2\2\u008d\20\3\2\2\2\u008e")
        buf.write("\u008f\7y\2\2\u008f\u0090\7j\2\2\u0090\u0091\7k\2\2\u0091")
        buf.write("\u0092\7n\2\2\u0092\u0093\7g\2\2\u0093\22\3\2\2\2\u0094")
        buf.write("\u0095\7v\2\2\u0095\u0096\7t\2\2\u0096\u0097\7w\2\2\u0097")
        buf.write("\u0098\7g\2\2\u0098\24\3\2\2\2\u0099\u009a\7h\2\2\u009a")
        buf.write("\u009b\7c\2\2\u009b\u009c\7n\2\2\u009c\u009d\7u\2\2\u009d")
        buf.write("\u009e\7g\2\2\u009e\26\3\2\2\2\u009f\u00a0\7k\2\2\u00a0")
        buf.write("\u00a1\7p\2\2\u00a1\u00a2\7v\2\2\u00a2\u00a3\7g\2\2\u00a3")
        buf.write("\u00a4\7i\2\2\u00a4\u00a5\7g\2\2\u00a5\u00a6\7t\2\2\u00a6")
        buf.write("\30\3\2\2\2\u00a7\u00a8\7h\2\2\u00a8\u00a9\7n\2\2\u00a9")
        buf.write("\u00aa\7q\2\2\u00aa\u00ab\7c\2\2\u00ab\u00ac\7v\2\2\u00ac")
        buf.write("\32\3\2\2\2\u00ad\u00ae\7u\2\2\u00ae\u00af\7v\2\2\u00af")
        buf.write("\u00b0\7t\2\2\u00b0\u00b1\7k\2\2\u00b1\u00b2\7p\2\2\u00b2")
        buf.write("\u00b3\7i\2\2\u00b3\34\3\2\2\2\u00b4\u00b5\7d\2\2\u00b5")
        buf.write("\u00b6\7q\2\2\u00b6\u00b7\7q\2\2\u00b7\u00b8\7n\2\2\u00b8")
        buf.write("\u00b9\7g\2\2\u00b9\u00ba\7c\2\2\u00ba\u00bb\7p\2\2\u00bb")
        buf.write("\36\3\2\2\2\u00bc\u00bd\7x\2\2\u00bd\u00be\7q\2\2\u00be")
        buf.write("\u00bf\7k\2\2\u00bf\u00c0\7f\2\2\u00c0 \3\2\2\2\u00c1")
        buf.write("\u00c2\7h\2\2\u00c2\u00c3\7w\2\2\u00c3\u00c4\7p\2\2\u00c4")
        buf.write("\u00c5\7e\2\2\u00c5\u00c6\7v\2\2\u00c6\u00c7\7k\2\2\u00c7")
        buf.write("\u00c8\7q\2\2\u00c8\u00c9\7p\2\2\u00c9\"\3\2\2\2\u00ca")
        buf.write("\u00cb\7k\2\2\u00cb\u00cc\7p\2\2\u00cc$\3\2\2\2\u00cd")
        buf.write("\u00ce\7q\2\2\u00ce\u00cf\7w\2\2\u00cf\u00d0\7v\2\2\u00d0")
        buf.write("&\3\2\2\2\u00d1\u00d2\7*\2\2\u00d2(\3\2\2\2\u00d3\u00d4")
        buf.write("\7+\2\2\u00d4*\3\2\2\2\u00d5\u00d6\7}\2\2\u00d6,\3\2\2")
        buf.write("\2\u00d7\u00d8\7\177\2\2\u00d8.\3\2\2\2\u00d9\u00da\7")
        buf.write("]\2\2\u00da\60\3\2\2\2\u00db\u00dc\7_\2\2\u00dc\62\3\2")
        buf.write("\2\2\u00dd\u00de\7.\2\2\u00de\64\3\2\2\2\u00df\u00e0\7")
        buf.write("<\2\2\u00e0\66\3\2\2\2\u00e1\u00e2\7=\2\2\u00e28\3\2\2")
        buf.write("\2\u00e3\u00e4\7-\2\2\u00e4:\3\2\2\2\u00e5\u00e6\7/\2")
        buf.write("\2\u00e6<\3\2\2\2\u00e7\u00e8\7,\2\2\u00e8>\3\2\2\2\u00e9")
        buf.write("\u00ea\7\61\2\2\u00ea@\3\2\2\2\u00eb\u00ec\7\'\2\2\u00ec")
        buf.write("B\3\2\2\2\u00ed\u00ee\7#\2\2\u00eeD\3\2\2\2\u00ef\u00f0")
        buf.write("\7~\2\2\u00f0\u00f1\7~\2\2\u00f1F\3\2\2\2\u00f2\u00f3")
        buf.write("\7(\2\2\u00f3\u00f4\7(\2\2\u00f4H\3\2\2\2\u00f5\u00f6")
        buf.write("\7#\2\2\u00f6\u00f7\7?\2\2\u00f7J\3\2\2\2\u00f8\u00f9")
        buf.write("\7?\2\2\u00f9\u00fa\7?\2\2\u00faL\3\2\2\2\u00fb\u00fc")
        buf.write("\7>\2\2\u00fcN\3\2\2\2\u00fd\u00fe\7@\2\2\u00feP\3\2\2")
        buf.write("\2\u00ff\u0100\7>\2\2\u0100\u0101\7?\2\2\u0101R\3\2\2")
        buf.write("\2\u0102\u0103\7@\2\2\u0103\u0104\7?\2\2\u0104T\3\2\2")
        buf.write("\2\u0105\u0106\7?\2\2\u0106V\3\2\2\2\u0107\u0109\t\2\2")
        buf.write("\2\u0108\u0107\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u0108")
        buf.write("\3\2\2\2\u010a\u010b\3\2\2\2\u010b\u010c\3\2\2\2\u010c")
        buf.write("\u010d\b,\2\2\u010dX\3\2\2\2\u010e\u0110\t\2\2\2\u010f")
        buf.write("\u010e\3\2\2\2\u0110\u0111\3\2\2\2\u0111\u010f\3\2\2\2")
        buf.write("\u0111\u0112\3\2\2\2\u0112\u0113\3\2\2\2\u0113\u0115\7")
        buf.write("\60\2\2\u0114\u0116\t\2\2\2\u0115\u0114\3\2\2\2\u0116")
        buf.write("\u0117\3\2\2\2\u0117\u0115\3\2\2\2\u0117\u0118\3\2\2\2")
        buf.write("\u0118\u0119\3\2\2\2\u0119\u011a\b-\3\2\u011aZ\3\2\2\2")
        buf.write("\u011b\u011e\5\23\n\2\u011c\u011e\5\25\13\2\u011d\u011b")
        buf.write("\3\2\2\2\u011d\u011c\3\2\2\2\u011e\\\3\2\2\2\u011f\u012b")
        buf.write("\7$\2\2\u0120\u012a\n\3\2\2\u0121\u0125\7^\2\2\u0122\u0124")
        buf.write("\n\3\2\2\u0123\u0122\3\2\2\2\u0124\u0127\3\2\2\2\u0125")
        buf.write("\u0123\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0128\3\2\2\2")
        buf.write("\u0127\u0125\3\2\2\2\u0128\u012a\7^\2\2\u0129\u0120\3")
        buf.write("\2\2\2\u0129\u0121\3\2\2\2\u012a\u012d\3\2\2\2\u012b\u0129")
        buf.write("\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u012e\3\2\2\2\u012d")
        buf.write("\u012b\3\2\2\2\u012e\u012f\7$\2\2\u012f\u0130\b/\4\2\u0130")
        buf.write("^\3\2\2\2\u0131\u0133\t\4\2\2\u0132\u0131\3\2\2\2\u0133")
        buf.write("\u0134\3\2\2\2\u0134\u0132\3\2\2\2\u0134\u0135\3\2\2\2")
        buf.write("\u0135`\3\2\2\2\u0136\u0138\t\5\2\2\u0137\u0136\3\2\2")
        buf.write("\2\u0138\u0139\3\2\2\2\u0139\u0137\3\2\2\2\u0139\u013a")
        buf.write("\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u013c\b\61\5\2\u013c")
        buf.write("b\3\2\2\2\u013d\u013e\13\2\2\2\u013e\u013f\b\62\6\2\u013f")
        buf.write("d\3\2\2\2\u0140\u0141\13\2\2\2\u0141\u0142\b\63\7\2\u0142")
        buf.write("f\3\2\2\2\u0143\u0144\13\2\2\2\u0144\u0145\b\64\b\2\u0145")
        buf.write("h\3\2\2\2\f\2\u010a\u0111\u0117\u011d\u0125\u0129\u012b")
        buf.write("\u0134\u0139\t\3,\2\3-\3\3/\4\b\2\2\3\62\5\3\63\6\3\64")
        buf.write("\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BREAK = 1
    CONTINUE = 2
    ELSE = 3
    FOR = 4
    IF = 5
    RETURN = 6
    DO = 7
    WHILE = 8
    TRUE = 9
    FALSE = 10
    INTEGER = 11
    FLOAT = 12
    STRTYPE = 13
    BOOLTYPE = 14
    VOIDTYPE = 15
    FUNCTION = 16
    INCOMING = 17
    OUTCOMING = 18
    LP = 19
    RP = 20
    LCB = 21
    RCB = 22
    LSB = 23
    RSB = 24
    CM = 25
    COLON = 26
    SM = 27
    ADD = 28
    SUB = 29
    MUL = 30
    DIV = 31
    MOD = 32
    NOT = 33
    OR = 34
    AND = 35
    NOT_EQUAL = 36
    EQUAL = 37
    LT = 38
    GT = 39
    LE = 40
    GE = 41
    ASSIGN = 42
    INTLIT = 43
    FLOATLIT = 44
    BOOLLIT = 45
    STRINGLIT = 46
    ID = 47
    WS = 48
    ERROR_CHAR = 49
    UNCLOSE_STRING = 50
    ILLEGAL_ESCAPE = 51

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'break'", "'continue'", "'else'", "'for'", "'if'", "'return'", 
            "'do'", "'while'", "'true'", "'false'", "'integer'", "'float'", 
            "'string'", "'boolean'", "'void'", "'function'", "'in'", "'out'", 
            "'('", "')'", "'{'", "'}'", "'['", "']'", "','", "':'", "';'", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'||'", "'&&'", "'!='", 
            "'=='", "'<'", "'>'", "'<='", "'>='", "'='" ]

    symbolicNames = [ "<INVALID>",
            "BREAK", "CONTINUE", "ELSE", "FOR", "IF", "RETURN", "DO", "WHILE", 
            "TRUE", "FALSE", "INTEGER", "FLOAT", "STRTYPE", "BOOLTYPE", 
            "VOIDTYPE", "FUNCTION", "INCOMING", "OUTCOMING", "LP", "RP", 
            "LCB", "RCB", "LSB", "RSB", "CM", "COLON", "SM", "ADD", "SUB", 
            "MUL", "DIV", "MOD", "NOT", "OR", "AND", "NOT_EQUAL", "EQUAL", 
            "LT", "GT", "LE", "GE", "ASSIGN", "INTLIT", "FLOATLIT", "BOOLLIT", 
            "STRINGLIT", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "BREAK", "CONTINUE", "ELSE", "FOR", "IF", "RETURN", "DO", 
                  "WHILE", "TRUE", "FALSE", "INTEGER", "FLOAT", "STRTYPE", 
                  "BOOLTYPE", "VOIDTYPE", "FUNCTION", "INCOMING", "OUTCOMING", 
                  "LP", "RP", "LCB", "RCB", "LSB", "RSB", "CM", "COLON", 
                  "SM", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "OR", 
                  "AND", "NOT_EQUAL", "EQUAL", "LT", "GT", "LE", "GE", "ASSIGN", 
                  "INTLIT", "FLOATLIT", "BOOLLIT", "STRINGLIT", "ID", "WS", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[42] = self.INTLIT_action 
            actions[43] = self.FLOATLIT_action 
            actions[45] = self.STRINGLIT_action 
            actions[48] = self.ERROR_CHAR_action 
            actions[49] = self.UNCLOSE_STRING_action 
            actions[50] = self.ILLEGAL_ESCAPE_action 
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
     


