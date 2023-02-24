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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u01dc\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\3\2\3\2\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\7\t\u00a2")
        buf.write("\n\t\f\t\16\t\u00a5\13\t\3\t\3\t\5\t\u00a9\n\t\3\n\3\n")
        buf.write("\3\n\5\n\u00ae\n\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n")
        buf.write("\u00b8\n\n\3\13\3\13\7\13\u00bc\n\13\f\13\16\13\u00bf")
        buf.write("\13\13\3\f\3\f\5\f\u00c3\n\f\3\f\6\f\u00c6\n\f\r\f\16")
        buf.write("\f\u00c7\3\r\3\r\5\r\u00cc\n\r\3\16\3\16\7\16\u00d0\n")
        buf.write("\16\f\16\16\16\u00d3\13\16\3\16\3\16\3\16\3\17\3\17\5")
        buf.write("\17\u00da\n\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00ec\n")
        buf.write("\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3")
        buf.write("!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3\'")
        buf.write("\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3+\3+\3,\3,")
        buf.write("\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\3.\3.\3.\3/\3/\3")
        buf.write("/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3")
        buf.write("\61\3\61\3\61\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67\38\38\38\38\3")
        buf.write("8\39\39\39\39\39\39\3:\3:\3:\3:\3:\3;\3;\3;\3;\3<\3<\3")
        buf.write("<\3<\3<\3<\3<\3<\3<\3=\3=\3=\3>\3>\3>\3>\3>\3>\3>\3>\3")
        buf.write("?\3?\3?\3?\3?\3?\3@\3@\3@\3@\3@\3A\3A\7A\u01ab\nA\fA\16")
        buf.write("A\u01ae\13A\3B\6B\u01b1\nB\rB\16B\u01b2\3B\3B\3C\3C\3")
        buf.write("C\3C\7C\u01bb\nC\fC\16C\u01be\13C\3C\3C\3C\3C\3C\3D\3")
        buf.write("D\3D\3D\7D\u01c9\nD\fD\16D\u01cc\13D\3D\3D\3E\3E\7E\u01d2")
        buf.write("\nE\fE\16E\u01d5\13E\3F\3F\3F\3G\3G\3G\3\u01bc\2H\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\2\27\2\31\f\33")
        buf.write("\r\35\2\37\2!\16#\17%\20\'\21)\22+\23-\24/\25\61\26\63")
        buf.write("\27\65\30\67\319\32;\33=\34?\35A\36C\37E G!I\"K#M$O%Q")
        buf.write("&S\'U(W)Y*[+],_-a.c/e\60g\61i\62k\63m\64o\65q\66s\67u")
        buf.write("8w9y:{;}<\177=\u0081>\u0083?\u0085@\u0087A\u0089\2\u008b")
        buf.write("B\u008dC\3\2\13\3\2\63;\3\2\62;\4\2GGgg\4\2--//\4\2$$")
        buf.write("^^\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\16\17\"\"\4\2\f")
        buf.write("\f\17\17\2\u01ee\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2")
        buf.write("\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2")
        buf.write("\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3")
        buf.write("\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2")
        buf.write("\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\3\u008f\3\2\2")
        buf.write("\2\5\u0091\3\2\2\2\7\u0093\3\2\2\2\t\u0095\3\2\2\2\13")
        buf.write("\u0097\3\2\2\2\r\u0099\3\2\2\2\17\u009b\3\2\2\2\21\u00a8")
        buf.write("\3\2\2\2\23\u00b7\3\2\2\2\25\u00b9\3\2\2\2\27\u00c0\3")
        buf.write("\2\2\2\31\u00cb\3\2\2\2\33\u00cd\3\2\2\2\35\u00d9\3\2")
        buf.write("\2\2\37\u00eb\3\2\2\2!\u00ed\3\2\2\2#\u00ef\3\2\2\2%\u00f1")
        buf.write("\3\2\2\2\'\u00f3\3\2\2\2)\u00f5\3\2\2\2+\u00f7\3\2\2\2")
        buf.write("-\u00f9\3\2\2\2/\u00fb\3\2\2\2\61\u00fd\3\2\2\2\63\u00ff")
        buf.write("\3\2\2\2\65\u0101\3\2\2\2\67\u0103\3\2\2\29\u0105\3\2")
        buf.write("\2\2;\u0107\3\2\2\2=\u0109\3\2\2\2?\u010b\3\2\2\2A\u010d")
        buf.write("\3\2\2\2C\u010f\3\2\2\2E\u0112\3\2\2\2G\u0115\3\2\2\2")
        buf.write("I\u0118\3\2\2\2K\u011b\3\2\2\2M\u011d\3\2\2\2O\u0120\3")
        buf.write("\2\2\2Q\u0122\3\2\2\2S\u0125\3\2\2\2U\u0128\3\2\2\2W\u012d")
        buf.write("\3\2\2\2Y\u0133\3\2\2\2[\u013b\3\2\2\2]\u013e\3\2\2\2")
        buf.write("_\u0143\3\2\2\2a\u0149\3\2\2\2c\u014f\3\2\2\2e\u0153\3")
        buf.write("\2\2\2g\u015c\3\2\2\2i\u015f\3\2\2\2k\u0167\3\2\2\2m\u016e")
        buf.write("\3\2\2\2o\u0175\3\2\2\2q\u017a\3\2\2\2s\u0180\3\2\2\2")
        buf.write("u\u0185\3\2\2\2w\u0189\3\2\2\2y\u0192\3\2\2\2{\u0195\3")
        buf.write("\2\2\2}\u019d\3\2\2\2\177\u01a3\3\2\2\2\u0081\u01a8\3")
        buf.write("\2\2\2\u0083\u01b0\3\2\2\2\u0085\u01b6\3\2\2\2\u0087\u01c4")
        buf.write("\3\2\2\2\u0089\u01cf\3\2\2\2\u008b\u01d6\3\2\2\2\u008d")
        buf.write("\u01d9\3\2\2\2\u008f\u0090\5Y-\2\u0090\4\3\2\2\2\u0091")
        buf.write("\u0092\5i\65\2\u0092\6\3\2\2\2\u0093\u0094\5a\61\2\u0094")
        buf.write("\b\3\2\2\2\u0095\u0096\5m\67\2\u0096\n\3\2\2\2\u0097\u0098")
        buf.write("\5}?\2\u0098\f\3\2\2\2\u0099\u009a\5s:\2\u009a\16\3\2")
        buf.write("\2\2\u009b\u009c\5U+\2\u009c\20\3\2\2\2\u009d\u00a3\t")
        buf.write("\2\2\2\u009e\u009f\7a\2\2\u009f\u00a2\t\3\2\2\u00a0\u00a2")
        buf.write("\t\3\2\2\u00a1\u009e\3\2\2\2\u00a1\u00a0\3\2\2\2\u00a2")
        buf.write("\u00a5\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2")
        buf.write("\u00a4\u00a6\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a6\u00a9\b")
        buf.write("\t\2\2\u00a7\u00a9\7\62\2\2\u00a8\u009d\3\2\2\2\u00a8")
        buf.write("\u00a7\3\2\2\2\u00a9\22\3\2\2\2\u00aa\u00ab\5\21\t\2\u00ab")
        buf.write("\u00ad\5\25\13\2\u00ac\u00ae\5\27\f\2\u00ad\u00ac\3\2")
        buf.write("\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b0")
        buf.write("\b\n\3\2\u00b0\u00b8\3\2\2\2\u00b1\u00b2\5\21\t\2\u00b2")
        buf.write("\u00b3\5\27\f\2\u00b3\u00b8\3\2\2\2\u00b4\u00b5\5\25\13")
        buf.write("\2\u00b5\u00b6\5\27\f\2\u00b6\u00b8\3\2\2\2\u00b7\u00aa")
        buf.write("\3\2\2\2\u00b7\u00b1\3\2\2\2\u00b7\u00b4\3\2\2\2\u00b8")
        buf.write("\24\3\2\2\2\u00b9\u00bd\7\60\2\2\u00ba\u00bc\t\3\2\2\u00bb")
        buf.write("\u00ba\3\2\2\2\u00bc\u00bf\3\2\2\2\u00bd\u00bb\3\2\2\2")
        buf.write("\u00bd\u00be\3\2\2\2\u00be\26\3\2\2\2\u00bf\u00bd\3\2")
        buf.write("\2\2\u00c0\u00c2\t\4\2\2\u00c1\u00c3\t\5\2\2\u00c2\u00c1")
        buf.write("\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c5\3\2\2\2\u00c4")
        buf.write("\u00c6\t\3\2\2\u00c5\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2")
        buf.write("\u00c7\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\30\3\2")
        buf.write("\2\2\u00c9\u00cc\5o8\2\u00ca\u00cc\5_\60\2\u00cb\u00c9")
        buf.write("\3\2\2\2\u00cb\u00ca\3\2\2\2\u00cc\32\3\2\2\2\u00cd\u00d1")
        buf.write("\7$\2\2\u00ce\u00d0\5\35\17\2\u00cf\u00ce\3\2\2\2\u00d0")
        buf.write("\u00d3\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2")
        buf.write("\u00d2\u00d4\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d4\u00d5\7")
        buf.write("$\2\2\u00d5\u00d6\b\16\4\2\u00d6\34\3\2\2\2\u00d7\u00da")
        buf.write("\n\6\2\2\u00d8\u00da\5\37\20\2\u00d9\u00d7\3\2\2\2\u00d9")
        buf.write("\u00d8\3\2\2\2\u00da\36\3\2\2\2\u00db\u00dc\7^\2\2\u00dc")
        buf.write("\u00ec\7d\2\2\u00dd\u00de\7^\2\2\u00de\u00ec\7h\2\2\u00df")
        buf.write("\u00e0\7^\2\2\u00e0\u00ec\7t\2\2\u00e1\u00e2\7^\2\2\u00e2")
        buf.write("\u00ec\7p\2\2\u00e3\u00e4\7^\2\2\u00e4\u00ec\7v\2\2\u00e5")
        buf.write("\u00e6\7^\2\2\u00e6\u00ec\7)\2\2\u00e7\u00e8\7^\2\2\u00e8")
        buf.write("\u00ec\7^\2\2\u00e9\u00ea\7^\2\2\u00ea\u00ec\7$\2\2\u00eb")
        buf.write("\u00db\3\2\2\2\u00eb\u00dd\3\2\2\2\u00eb\u00df\3\2\2\2")
        buf.write("\u00eb\u00e1\3\2\2\2\u00eb\u00e3\3\2\2\2\u00eb\u00e5\3")
        buf.write("\2\2\2\u00eb\u00e7\3\2\2\2\u00eb\u00e9\3\2\2\2\u00ec ")
        buf.write("\3\2\2\2\u00ed\u00ee\7*\2\2\u00ee\"\3\2\2\2\u00ef\u00f0")
        buf.write("\7+\2\2\u00f0$\3\2\2\2\u00f1\u00f2\7]\2\2\u00f2&\3\2\2")
        buf.write("\2\u00f3\u00f4\7_\2\2\u00f4(\3\2\2\2\u00f5\u00f6\7\60")
        buf.write("\2\2\u00f6*\3\2\2\2\u00f7\u00f8\7.\2\2\u00f8,\3\2\2\2")
        buf.write("\u00f9\u00fa\7=\2\2\u00fa.\3\2\2\2\u00fb\u00fc\7<\2\2")
        buf.write("\u00fc\60\3\2\2\2\u00fd\u00fe\7}\2\2\u00fe\62\3\2\2\2")
        buf.write("\u00ff\u0100\7\177\2\2\u0100\64\3\2\2\2\u0101\u0102\7")
        buf.write("?\2\2\u0102\66\3\2\2\2\u0103\u0104\7-\2\2\u01048\3\2\2")
        buf.write("\2\u0105\u0106\7/\2\2\u0106:\3\2\2\2\u0107\u0108\7,\2")
        buf.write("\2\u0108<\3\2\2\2\u0109\u010a\7\61\2\2\u010a>\3\2\2\2")
        buf.write("\u010b\u010c\7\'\2\2\u010c@\3\2\2\2\u010d\u010e\7#\2\2")
        buf.write("\u010eB\3\2\2\2\u010f\u0110\7(\2\2\u0110\u0111\7(\2\2")
        buf.write("\u0111D\3\2\2\2\u0112\u0113\7~\2\2\u0113\u0114\7~\2\2")
        buf.write("\u0114F\3\2\2\2\u0115\u0116\7?\2\2\u0116\u0117\7?\2\2")
        buf.write("\u0117H\3\2\2\2\u0118\u0119\7#\2\2\u0119\u011a\7?\2\2")
        buf.write("\u011aJ\3\2\2\2\u011b\u011c\7>\2\2\u011cL\3\2\2\2\u011d")
        buf.write("\u011e\7>\2\2\u011e\u011f\7?\2\2\u011fN\3\2\2\2\u0120")
        buf.write("\u0121\7@\2\2\u0121P\3\2\2\2\u0122\u0123\7@\2\2\u0123")
        buf.write("\u0124\7?\2\2\u0124R\3\2\2\2\u0125\u0126\7<\2\2\u0126")
        buf.write("\u0127\7<\2\2\u0127T\3\2\2\2\u0128\u0129\7c\2\2\u0129")
        buf.write("\u012a\7w\2\2\u012a\u012b\7v\2\2\u012b\u012c\7q\2\2\u012c")
        buf.write("V\3\2\2\2\u012d\u012e\7d\2\2\u012e\u012f\7t\2\2\u012f")
        buf.write("\u0130\7g\2\2\u0130\u0131\7c\2\2\u0131\u0132\7m\2\2\u0132")
        buf.write("X\3\2\2\2\u0133\u0134\7d\2\2\u0134\u0135\7q\2\2\u0135")
        buf.write("\u0136\7q\2\2\u0136\u0137\7n\2\2\u0137\u0138\7g\2\2\u0138")
        buf.write("\u0139\7c\2\2\u0139\u013a\7p\2\2\u013aZ\3\2\2\2\u013b")
        buf.write("\u013c\7f\2\2\u013c\u013d\7q\2\2\u013d\\\3\2\2\2\u013e")
        buf.write("\u013f\7g\2\2\u013f\u0140\7n\2\2\u0140\u0141\7u\2\2\u0141")
        buf.write("\u0142\7g\2\2\u0142^\3\2\2\2\u0143\u0144\7h\2\2\u0144")
        buf.write("\u0145\7c\2\2\u0145\u0146\7n\2\2\u0146\u0147\7u\2\2\u0147")
        buf.write("\u0148\7g\2\2\u0148`\3\2\2\2\u0149\u014a\7h\2\2\u014a")
        buf.write("\u014b\7n\2\2\u014b\u014c\7q\2\2\u014c\u014d\7c\2\2\u014d")
        buf.write("\u014e\7v\2\2\u014eb\3\2\2\2\u014f\u0150\7h\2\2\u0150")
        buf.write("\u0151\7q\2\2\u0151\u0152\7t\2\2\u0152d\3\2\2\2\u0153")
        buf.write("\u0154\7h\2\2\u0154\u0155\7w\2\2\u0155\u0156\7p\2\2\u0156")
        buf.write("\u0157\7e\2\2\u0157\u0158\7v\2\2\u0158\u0159\7k\2\2\u0159")
        buf.write("\u015a\7q\2\2\u015a\u015b\7p\2\2\u015bf\3\2\2\2\u015c")
        buf.write("\u015d\7k\2\2\u015d\u015e\7h\2\2\u015eh\3\2\2\2\u015f")
        buf.write("\u0160\7k\2\2\u0160\u0161\7p\2\2\u0161\u0162\7v\2\2\u0162")
        buf.write("\u0163\7g\2\2\u0163\u0164\7i\2\2\u0164\u0165\7g\2\2\u0165")
        buf.write("\u0166\7t\2\2\u0166j\3\2\2\2\u0167\u0168\7t\2\2\u0168")
        buf.write("\u0169\7g\2\2\u0169\u016a\7v\2\2\u016a\u016b\7w\2\2\u016b")
        buf.write("\u016c\7t\2\2\u016c\u016d\7p\2\2\u016dl\3\2\2\2\u016e")
        buf.write("\u016f\7u\2\2\u016f\u0170\7v\2\2\u0170\u0171\7t\2\2\u0171")
        buf.write("\u0172\7k\2\2\u0172\u0173\7p\2\2\u0173\u0174\7i\2\2\u0174")
        buf.write("n\3\2\2\2\u0175\u0176\7v\2\2\u0176\u0177\7t\2\2\u0177")
        buf.write("\u0178\7w\2\2\u0178\u0179\7g\2\2\u0179p\3\2\2\2\u017a")
        buf.write("\u017b\7y\2\2\u017b\u017c\7j\2\2\u017c\u017d\7k\2\2\u017d")
        buf.write("\u017e\7n\2\2\u017e\u017f\7g\2\2\u017fr\3\2\2\2\u0180")
        buf.write("\u0181\7x\2\2\u0181\u0182\7q\2\2\u0182\u0183\7k\2\2\u0183")
        buf.write("\u0184\7f\2\2\u0184t\3\2\2\2\u0185\u0186\7q\2\2\u0186")
        buf.write("\u0187\7w\2\2\u0187\u0188\7v\2\2\u0188v\3\2\2\2\u0189")
        buf.write("\u018a\7e\2\2\u018a\u018b\7q\2\2\u018b\u018c\7p\2\2\u018c")
        buf.write("\u018d\7v\2\2\u018d\u018e\7k\2\2\u018e\u018f\7p\2\2\u018f")
        buf.write("\u0190\7w\2\2\u0190\u0191\7g\2\2\u0191x\3\2\2\2\u0192")
        buf.write("\u0193\7q\2\2\u0193\u0194\7h\2\2\u0194z\3\2\2\2\u0195")
        buf.write("\u0196\7k\2\2\u0196\u0197\7p\2\2\u0197\u0198\7j\2\2\u0198")
        buf.write("\u0199\7g\2\2\u0199\u019a\7t\2\2\u019a\u019b\7k\2\2\u019b")
        buf.write("\u019c\7v\2\2\u019c|\3\2\2\2\u019d\u019e\7c\2\2\u019e")
        buf.write("\u019f\7t\2\2\u019f\u01a0\7t\2\2\u01a0\u01a1\7c\2\2\u01a1")
        buf.write("\u01a2\7{\2\2\u01a2~\3\2\2\2\u01a3\u01a4\7o\2\2\u01a4")
        buf.write("\u01a5\7c\2\2\u01a5\u01a6\7k\2\2\u01a6\u01a7\7p\2\2\u01a7")
        buf.write("\u0080\3\2\2\2\u01a8\u01ac\t\7\2\2\u01a9\u01ab\t\b\2\2")
        buf.write("\u01aa\u01a9\3\2\2\2\u01ab\u01ae\3\2\2\2\u01ac\u01aa\3")
        buf.write("\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u0082\3\2\2\2\u01ae\u01ac")
        buf.write("\3\2\2\2\u01af\u01b1\t\t\2\2\u01b0\u01af\3\2\2\2\u01b1")
        buf.write("\u01b2\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b2\u01b3\3\2\2\2")
        buf.write("\u01b3\u01b4\3\2\2\2\u01b4\u01b5\bB\5\2\u01b5\u0084\3")
        buf.write("\2\2\2\u01b6\u01b7\7\61\2\2\u01b7\u01b8\7,\2\2\u01b8\u01bc")
        buf.write("\3\2\2\2\u01b9\u01bb\13\2\2\2\u01ba\u01b9\3\2\2\2\u01bb")
        buf.write("\u01be\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bc\u01ba\3\2\2\2")
        buf.write("\u01bd\u01bf\3\2\2\2\u01be\u01bc\3\2\2\2\u01bf\u01c0\7")
        buf.write(",\2\2\u01c0\u01c1\7\61\2\2\u01c1\u01c2\3\2\2\2\u01c2\u01c3")
        buf.write("\bC\5\2\u01c3\u0086\3\2\2\2\u01c4\u01c5\7\61\2\2\u01c5")
        buf.write("\u01c6\7\61\2\2\u01c6\u01ca\3\2\2\2\u01c7\u01c9\n\n\2")
        buf.write("\2\u01c8\u01c7\3\2\2\2\u01c9\u01cc\3\2\2\2\u01ca\u01c8")
        buf.write("\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01cd\3\2\2\2\u01cc")
        buf.write("\u01ca\3\2\2\2\u01cd\u01ce\bD\5\2\u01ce\u0088\3\2\2\2")
        buf.write("\u01cf\u01d3\7$\2\2\u01d0\u01d2\5\35\17\2\u01d1\u01d0")
        buf.write("\3\2\2\2\u01d2\u01d5\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d3")
        buf.write("\u01d4\3\2\2\2\u01d4\u008a\3\2\2\2\u01d5\u01d3\3\2\2\2")
        buf.write("\u01d6\u01d7\5\u0089E\2\u01d7\u01d8\bF\6\2\u01d8\u008c")
        buf.write("\3\2\2\2\u01d9\u01da\13\2\2\2\u01da\u01db\bG\7\2\u01db")
        buf.write("\u008e\3\2\2\2\24\2\u00a1\u00a3\u00a8\u00ad\u00b7\u00bd")
        buf.write("\u00c2\u00c7\u00cb\u00d1\u00d9\u00eb\u01ac\u01b2\u01bc")
        buf.write("\u01ca\u01d3\b\3\t\2\3\n\3\3\16\4\b\2\2\3F\5\3G\6")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BooleanType = 1
    IntegerType = 2
    FloatType = 3
    StringType = 4
    ArrayType = 5
    VoidType = 6
    AutoType = 7
    IntegerL = 8
    FloatL = 9
    BooleanL = 10
    StringL = 11
    LPAREN = 12
    RPAREN = 13
    LSQUARE = 14
    RSQUARE = 15
    DOT = 16
    COMMA = 17
    SEMICOLON = 18
    COLON = 19
    LBRACKET = 20
    RBRACKET = 21
    ASIGN = 22
    PLUS = 23
    MINUS = 24
    STAR = 25
    DIV = 26
    MOD = 27
    NOT = 28
    ANDAND = 29
    OROR = 30
    EQEQ = 31
    NOTEQ = 32
    LESS = 33
    LESSEQ = 34
    CREATER = 35
    CREATEREQ = 36
    DOUBLECOLON = 37
    AUTO = 38
    BREAK = 39
    BOOLEAN = 40
    DO = 41
    ELSE = 42
    FALSE = 43
    FLOAT = 44
    FOR = 45
    FUNCTION = 46
    IF = 47
    INTEGER = 48
    RETURN = 49
    STRING = 50
    TRUE = 51
    WHILE = 52
    VOID = 53
    OUT = 54
    CONTINUE = 55
    OF = 56
    INHERIT = 57
    ARRAY = 58
    MAIN = 59
    Identifier = 60
    WhiteSpaces = 61
    BlockComment = 62
    LineComment = 63
    UNCLOSE_STRING = 64
    ERROR_CHAR = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'['", "']'", "'.'", "','", "';'", "':'", "'{'", 
            "'}'", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", 
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'false'", 
            "'float'", "'for'", "'function'", "'if'", "'integer'", "'return'", 
            "'string'", "'true'", "'while'", "'void'", "'out'", "'continue'", 
            "'of'", "'inherit'", "'array'", "'main'" ]

    symbolicNames = [ "<INVALID>",
            "BooleanType", "IntegerType", "FloatType", "StringType", "ArrayType", 
            "VoidType", "AutoType", "IntegerL", "FloatL", "BooleanL", "StringL", 
            "LPAREN", "RPAREN", "LSQUARE", "RSQUARE", "DOT", "COMMA", "SEMICOLON", 
            "COLON", "LBRACKET", "RBRACKET", "ASIGN", "PLUS", "MINUS", "STAR", 
            "DIV", "MOD", "NOT", "ANDAND", "OROR", "EQEQ", "NOTEQ", "LESS", 
            "LESSEQ", "CREATER", "CREATEREQ", "DOUBLECOLON", "AUTO", "BREAK", 
            "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", 
            "IF", "INTEGER", "RETURN", "STRING", "TRUE", "WHILE", "VOID", 
            "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "MAIN", "Identifier", 
            "WhiteSpaces", "BlockComment", "LineComment", "UNCLOSE_STRING", 
            "ERROR_CHAR" ]

    ruleNames = [ "BooleanType", "IntegerType", "FloatType", "StringType", 
                  "ArrayType", "VoidType", "AutoType", "IntegerL", "FloatL", 
                  "DecimalP", "ExponentP", "BooleanL", "StringL", "Schar", 
                  "EscapeSequence", "LPAREN", "RPAREN", "LSQUARE", "RSQUARE", 
                  "DOT", "COMMA", "SEMICOLON", "COLON", "LBRACKET", "RBRACKET", 
                  "ASIGN", "PLUS", "MINUS", "STAR", "DIV", "MOD", "NOT", 
                  "ANDAND", "OROR", "EQEQ", "NOTEQ", "LESS", "LESSEQ", "CREATER", 
                  "CREATEREQ", "DOUBLECOLON", "AUTO", "BREAK", "BOOLEAN", 
                  "DO", "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", 
                  "INTEGER", "RETURN", "STRING", "TRUE", "WHILE", "VOID", 
                  "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "MAIN", "Identifier", 
                  "WhiteSpaces", "BlockComment", "LineComment", "UncloseString", 
                  "UNCLOSE_STRING", "ERROR_CHAR" ]

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
            actions[7] = self.IntegerL_action 
            actions[8] = self.FloatL_action 
            actions[12] = self.StringL_action 
            actions[68] = self.UNCLOSE_STRING_action 
            actions[69] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def IntegerL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_', '')
     

    def FloatL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_', '')
     

    def StringL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise UncloseString(self.text[1:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
             raise ErrorToken(self.text) 
     


