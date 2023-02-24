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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\28")
        buf.write("\u016c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$")
        buf.write("\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3*\3+")
        buf.write("\3+\3,\6,\u010f\n,\r,\16,\u0110\3,\3,\3-\6-\u0116\n-\r")
        buf.write("-\16-\u0117\3-\3-\6-\u011c\n-\r-\16-\u011d\3-\3-\3.\3")
        buf.write(".\5.\u0124\n.\3/\3/\3/\3/\7/\u012a\n/\f/\16/\u012d\13")
        buf.write("/\3/\7/\u0130\n/\f/\16/\u0133\13/\3/\3/\3/\3\60\6\60\u0139")
        buf.write("\n\60\r\60\16\60\u013a\3\61\3\61\3\61\3\61\7\61\u0141")
        buf.write("\n\61\f\61\16\61\u0144\13\61\3\61\3\61\3\62\3\62\3\62")
        buf.write("\3\62\7\62\u014c\n\62\f\62\16\62\u014f\13\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\63\3\63\7\63\u0158\n\63\f\63\16\63\u015b")
        buf.write("\13\63\3\64\6\64\u015e\n\64\r\64\16\64\u015f\3\64\3\64")
        buf.write("\3\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67\3\u014d")
        buf.write("\28\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8\3\2")
        buf.write("\b\4\2\62;aa\3\2^^\6\2\62;C\\aac|\4\2\f\f\17\17\4\2\f")
        buf.write("\f\16\17\5\2\13\f\16\17\"\"\2\u0177\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2")
        buf.write("\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2")
        buf.write("\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3")
        buf.write("\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W")
        buf.write("\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2")
        buf.write("a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2")
        buf.write("\2k\3\2\2\2\2m\3\2\2\2\3o\3\2\2\2\5u\3\2\2\2\7~\3\2\2")
        buf.write("\2\t\u0083\3\2\2\2\13\u0087\3\2\2\2\r\u008a\3\2\2\2\17")
        buf.write("\u0091\3\2\2\2\21\u0094\3\2\2\2\23\u009a\3\2\2\2\25\u009f")
        buf.write("\3\2\2\2\27\u00a5\3\2\2\2\31\u00ad\3\2\2\2\33\u00b3\3")
        buf.write("\2\2\2\35\u00ba\3\2\2\2\37\u00c2\3\2\2\2!\u00c7\3\2\2")
        buf.write("\2#\u00d0\3\2\2\2%\u00d3\3\2\2\2\'\u00d7\3\2\2\2)\u00d9")
        buf.write("\3\2\2\2+\u00db\3\2\2\2-\u00dd\3\2\2\2/\u00df\3\2\2\2")
        buf.write("\61\u00e1\3\2\2\2\63\u00e3\3\2\2\2\65\u00e5\3\2\2\2\67")
        buf.write("\u00e7\3\2\2\29\u00e9\3\2\2\2;\u00eb\3\2\2\2=\u00ed\3")
        buf.write("\2\2\2?\u00ef\3\2\2\2A\u00f1\3\2\2\2C\u00f3\3\2\2\2E\u00f5")
        buf.write("\3\2\2\2G\u00f8\3\2\2\2I\u00fb\3\2\2\2K\u00fe\3\2\2\2")
        buf.write("M\u0101\3\2\2\2O\u0103\3\2\2\2Q\u0105\3\2\2\2S\u0108\3")
        buf.write("\2\2\2U\u010b\3\2\2\2W\u010e\3\2\2\2Y\u0115\3\2\2\2[\u0123")
        buf.write("\3\2\2\2]\u0125\3\2\2\2_\u0138\3\2\2\2a\u013c\3\2\2\2")
        buf.write("c\u0147\3\2\2\2e\u0155\3\2\2\2g\u015d\3\2\2\2i\u0163\3")
        buf.write("\2\2\2k\u0166\3\2\2\2m\u0169\3\2\2\2op\7d\2\2pq\7t\2\2")
        buf.write("qr\7g\2\2rs\7c\2\2st\7m\2\2t\4\3\2\2\2uv\7e\2\2vw\7q\2")
        buf.write("\2wx\7p\2\2xy\7v\2\2yz\7k\2\2z{\7p\2\2{|\7w\2\2|}\7g\2")
        buf.write("\2}\6\3\2\2\2~\177\7g\2\2\177\u0080\7n\2\2\u0080\u0081")
        buf.write("\7u\2\2\u0081\u0082\7g\2\2\u0082\b\3\2\2\2\u0083\u0084")
        buf.write("\7h\2\2\u0084\u0085\7q\2\2\u0085\u0086\7t\2\2\u0086\n")
        buf.write("\3\2\2\2\u0087\u0088\7k\2\2\u0088\u0089\7h\2\2\u0089\f")
        buf.write("\3\2\2\2\u008a\u008b\7t\2\2\u008b\u008c\7g\2\2\u008c\u008d")
        buf.write("\7v\2\2\u008d\u008e\7w\2\2\u008e\u008f\7t\2\2\u008f\u0090")
        buf.write("\7p\2\2\u0090\16\3\2\2\2\u0091\u0092\7f\2\2\u0092\u0093")
        buf.write("\7q\2\2\u0093\20\3\2\2\2\u0094\u0095\7y\2\2\u0095\u0096")
        buf.write("\7j\2\2\u0096\u0097\7k\2\2\u0097\u0098\7n\2\2\u0098\u0099")
        buf.write("\7g\2\2\u0099\22\3\2\2\2\u009a\u009b\7v\2\2\u009b\u009c")
        buf.write("\7t\2\2\u009c\u009d\7w\2\2\u009d\u009e\7g\2\2\u009e\24")
        buf.write("\3\2\2\2\u009f\u00a0\7h\2\2\u00a0\u00a1\7c\2\2\u00a1\u00a2")
        buf.write("\7n\2\2\u00a2\u00a3\7u\2\2\u00a3\u00a4\7g\2\2\u00a4\26")
        buf.write("\3\2\2\2\u00a5\u00a6\7k\2\2\u00a6\u00a7\7p\2\2\u00a7\u00a8")
        buf.write("\7v\2\2\u00a8\u00a9\7g\2\2\u00a9\u00aa\7i\2\2\u00aa\u00ab")
        buf.write("\7g\2\2\u00ab\u00ac\7t\2\2\u00ac\30\3\2\2\2\u00ad\u00ae")
        buf.write("\7h\2\2\u00ae\u00af\7n\2\2\u00af\u00b0\7q\2\2\u00b0\u00b1")
        buf.write("\7c\2\2\u00b1\u00b2\7v\2\2\u00b2\32\3\2\2\2\u00b3\u00b4")
        buf.write("\7u\2\2\u00b4\u00b5\7v\2\2\u00b5\u00b6\7t\2\2\u00b6\u00b7")
        buf.write("\7k\2\2\u00b7\u00b8\7p\2\2\u00b8\u00b9\7i\2\2\u00b9\34")
        buf.write("\3\2\2\2\u00ba\u00bb\7d\2\2\u00bb\u00bc\7q\2\2\u00bc\u00bd")
        buf.write("\7q\2\2\u00bd\u00be\7n\2\2\u00be\u00bf\7g\2\2\u00bf\u00c0")
        buf.write("\7c\2\2\u00c0\u00c1\7p\2\2\u00c1\36\3\2\2\2\u00c2\u00c3")
        buf.write("\7x\2\2\u00c3\u00c4\7q\2\2\u00c4\u00c5\7k\2\2\u00c5\u00c6")
        buf.write("\7f\2\2\u00c6 \3\2\2\2\u00c7\u00c8\7h\2\2\u00c8\u00c9")
        buf.write("\7w\2\2\u00c9\u00ca\7p\2\2\u00ca\u00cb\7e\2\2\u00cb\u00cc")
        buf.write("\7v\2\2\u00cc\u00cd\7k\2\2\u00cd\u00ce\7q\2\2\u00ce\u00cf")
        buf.write("\7p\2\2\u00cf\"\3\2\2\2\u00d0\u00d1\7k\2\2\u00d1\u00d2")
        buf.write("\7p\2\2\u00d2$\3\2\2\2\u00d3\u00d4\7q\2\2\u00d4\u00d5")
        buf.write("\7w\2\2\u00d5\u00d6\7v\2\2\u00d6&\3\2\2\2\u00d7\u00d8")
        buf.write("\7*\2\2\u00d8(\3\2\2\2\u00d9\u00da\7+\2\2\u00da*\3\2\2")
        buf.write("\2\u00db\u00dc\7}\2\2\u00dc,\3\2\2\2\u00dd\u00de\7\177")
        buf.write("\2\2\u00de.\3\2\2\2\u00df\u00e0\7]\2\2\u00e0\60\3\2\2")
        buf.write("\2\u00e1\u00e2\7_\2\2\u00e2\62\3\2\2\2\u00e3\u00e4\7.")
        buf.write("\2\2\u00e4\64\3\2\2\2\u00e5\u00e6\7<\2\2\u00e6\66\3\2")
        buf.write("\2\2\u00e7\u00e8\7=\2\2\u00e88\3\2\2\2\u00e9\u00ea\7-")
        buf.write("\2\2\u00ea:\3\2\2\2\u00eb\u00ec\7/\2\2\u00ec<\3\2\2\2")
        buf.write("\u00ed\u00ee\7,\2\2\u00ee>\3\2\2\2\u00ef\u00f0\7\61\2")
        buf.write("\2\u00f0@\3\2\2\2\u00f1\u00f2\7\'\2\2\u00f2B\3\2\2\2\u00f3")
        buf.write("\u00f4\7#\2\2\u00f4D\3\2\2\2\u00f5\u00f6\7~\2\2\u00f6")
        buf.write("\u00f7\7~\2\2\u00f7F\3\2\2\2\u00f8\u00f9\7(\2\2\u00f9")
        buf.write("\u00fa\7(\2\2\u00faH\3\2\2\2\u00fb\u00fc\7#\2\2\u00fc")
        buf.write("\u00fd\7?\2\2\u00fdJ\3\2\2\2\u00fe\u00ff\7?\2\2\u00ff")
        buf.write("\u0100\7?\2\2\u0100L\3\2\2\2\u0101\u0102\7>\2\2\u0102")
        buf.write("N\3\2\2\2\u0103\u0104\7@\2\2\u0104P\3\2\2\2\u0105\u0106")
        buf.write("\7>\2\2\u0106\u0107\7?\2\2\u0107R\3\2\2\2\u0108\u0109")
        buf.write("\7@\2\2\u0109\u010a\7?\2\2\u010aT\3\2\2\2\u010b\u010c")
        buf.write("\7?\2\2\u010cV\3\2\2\2\u010d\u010f\t\2\2\2\u010e\u010d")
        buf.write("\3\2\2\2\u010f\u0110\3\2\2\2\u0110\u010e\3\2\2\2\u0110")
        buf.write("\u0111\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0113\b,\2\2")
        buf.write("\u0113X\3\2\2\2\u0114\u0116\t\2\2\2\u0115\u0114\3\2\2")
        buf.write("\2\u0116\u0117\3\2\2\2\u0117\u0115\3\2\2\2\u0117\u0118")
        buf.write("\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u011b\7\60\2\2\u011a")
        buf.write("\u011c\t\2\2\2\u011b\u011a\3\2\2\2\u011c\u011d\3\2\2\2")
        buf.write("\u011d\u011b\3\2\2\2\u011d\u011e\3\2\2\2\u011e\u011f\3")
        buf.write("\2\2\2\u011f\u0120\b-\3\2\u0120Z\3\2\2\2\u0121\u0124\5")
        buf.write("\23\n\2\u0122\u0124\5\25\13\2\u0123\u0121\3\2\2\2\u0123")
        buf.write("\u0122\3\2\2\2\u0124\\\3\2\2\2\u0125\u0131\7$\2\2\u0126")
        buf.write("\u0130\n\3\2\2\u0127\u012b\7^\2\2\u0128\u012a\n\3\2\2")
        buf.write("\u0129\u0128\3\2\2\2\u012a\u012d\3\2\2\2\u012b\u0129\3")
        buf.write("\2\2\2\u012b\u012c\3\2\2\2\u012c\u012e\3\2\2\2\u012d\u012b")
        buf.write("\3\2\2\2\u012e\u0130\7^\2\2\u012f\u0126\3\2\2\2\u012f")
        buf.write("\u0127\3\2\2\2\u0130\u0133\3\2\2\2\u0131\u012f\3\2\2\2")
        buf.write("\u0131\u0132\3\2\2\2\u0132\u0134\3\2\2\2\u0133\u0131\3")
        buf.write("\2\2\2\u0134\u0135\7$\2\2\u0135\u0136\b/\4\2\u0136^\3")
        buf.write("\2\2\2\u0137\u0139\t\4\2\2\u0138\u0137\3\2\2\2\u0139\u013a")
        buf.write("\3\2\2\2\u013a\u0138\3\2\2\2\u013a\u013b\3\2\2\2\u013b")
        buf.write("`\3\2\2\2\u013c\u013d\7\61\2\2\u013d\u013e\7\61\2\2\u013e")
        buf.write("\u0142\3\2\2\2\u013f\u0141\n\5\2\2\u0140\u013f\3\2\2\2")
        buf.write("\u0141\u0144\3\2\2\2\u0142\u0140\3\2\2\2\u0142\u0143\3")
        buf.write("\2\2\2\u0143\u0145\3\2\2\2\u0144\u0142\3\2\2\2\u0145\u0146")
        buf.write("\b\61\5\2\u0146b\3\2\2\2\u0147\u0148\7\61\2\2\u0148\u0149")
        buf.write("\7,\2\2\u0149\u014d\3\2\2\2\u014a\u014c\13\2\2\2\u014b")
        buf.write("\u014a\3\2\2\2\u014c\u014f\3\2\2\2\u014d\u014e\3\2\2\2")
        buf.write("\u014d\u014b\3\2\2\2\u014e\u0150\3\2\2\2\u014f\u014d\3")
        buf.write("\2\2\2\u0150\u0151\7,\2\2\u0151\u0152\7\61\2\2\u0152\u0153")
        buf.write("\3\2\2\2\u0153\u0154\b\62\5\2\u0154d\3\2\2\2\u0155\u0159")
        buf.write("\7%\2\2\u0156\u0158\n\6\2\2\u0157\u0156\3\2\2\2\u0158")
        buf.write("\u015b\3\2\2\2\u0159\u0157\3\2\2\2\u0159\u015a\3\2\2\2")
        buf.write("\u015af\3\2\2\2\u015b\u0159\3\2\2\2\u015c\u015e\t\7\2")
        buf.write("\2\u015d\u015c\3\2\2\2\u015e\u015f\3\2\2\2\u015f\u015d")
        buf.write("\3\2\2\2\u015f\u0160\3\2\2\2\u0160\u0161\3\2\2\2\u0161")
        buf.write("\u0162\b\64\5\2\u0162h\3\2\2\2\u0163\u0164\13\2\2\2\u0164")
        buf.write("\u0165\b\65\6\2\u0165j\3\2\2\2\u0166\u0167\13\2\2\2\u0167")
        buf.write("\u0168\b\66\7\2\u0168l\3\2\2\2\u0169\u016a\13\2\2\2\u016a")
        buf.write("\u016b\b\67\b\2\u016bn\3\2\2\2\17\2\u0110\u0117\u011d")
        buf.write("\u0123\u012b\u012f\u0131\u013a\u0142\u014d\u0159\u015f")
        buf.write("\t\3,\2\3-\3\3/\4\b\2\2\3\65\5\3\66\6\3\67\7")
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
    LINE_CMT = 48
    BLOCK_CMT = 49
    COMMENT = 50
    WS = 51
    ERROR_CHAR = 52
    UNCLOSE_STRING = 53
    ILLEGAL_ESCAPE = 54

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
            "STRINGLIT", "ID", "LINE_CMT", "BLOCK_CMT", "COMMENT", "WS", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "BREAK", "CONTINUE", "ELSE", "FOR", "IF", "RETURN", "DO", 
                  "WHILE", "TRUE", "FALSE", "INTEGER", "FLOAT", "STRTYPE", 
                  "BOOLTYPE", "VOIDTYPE", "FUNCTION", "INCOMING", "OUTCOMING", 
                  "LP", "RP", "LCB", "RCB", "LSB", "RSB", "CM", "COLON", 
                  "SM", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "OR", 
                  "AND", "NOT_EQUAL", "EQUAL", "LT", "GT", "LE", "GE", "ASSIGN", 
                  "INTLIT", "FLOATLIT", "BOOLLIT", "STRINGLIT", "ID", "LINE_CMT", 
                  "BLOCK_CMT", "COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:
            result = super().emit();
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text);
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[42] = self.INTLIT_action 
            actions[43] = self.FLOATLIT_action 
            actions[45] = self.STRINGLIT_action 
            actions[51] = self.ERROR_CHAR_action 
            actions[52] = self.UNCLOSE_STRING_action 
            actions[53] = self.ILLEGAL_ESCAPE_action 
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
     


