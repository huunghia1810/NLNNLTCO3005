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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
        buf.write("\u01e2\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\3\2\3\2\5\2\u008e\n\2\3\2\6\2\u0091\n\2")
        buf.write("\r\2\16\2\u0092\3\3\3\3\7\3\u0097\n\3\f\3\16\3\u009a\13")
        buf.write("\3\3\4\3\4\5\4\u009e\n\4\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3")
        buf.write("\7\5\7\u00a8\n\7\3\b\3\b\5\b\u00ac\n\b\3\t\3\t\5\t\u00b0")
        buf.write("\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5")
        buf.write("\n\u00be\n\n\5\n\u00c0\n\n\3\n\3\n\3\13\3\13\3\13\5\13")
        buf.write("\u00c7\n\13\3\13\7\13\u00ca\n\13\f\13\16\13\u00cd\13\13")
        buf.write("\3\13\5\13\u00d0\n\13\3\f\3\f\7\f\u00d4\n\f\f\f\16\f\u00d7")
        buf.write("\13\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!")
        buf.write("\3\"\3\"\3\"\3\"\7\"\u015b\n\"\f\"\16\"\u015e\13\"\3\"")
        buf.write("\3\"\3#\3#\3#\3#\7#\u0166\n#\f#\16#\u0169\13#\3#\3#\3")
        buf.write("#\3#\3#\3$\3$\7$\u0172\n$\f$\16$\u0175\13$\3%\3%\3&\3")
        buf.write("&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3")
        buf.write("/\3/\3/\5/\u018e\n/\3\60\3\60\5\60\u0192\n\60\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\5\61\u019a\n\61\3\62\3\62\3\63\3")
        buf.write("\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\38\3")
        buf.write("9\39\39\3:\3:\3:\3;\3;\3;\3<\3<\3=\3=\3>\3>\3>\3?\3?\3")
        buf.write("?\3@\3@\3@\3A\3A\3B\6B\u01c4\nB\rB\16B\u01c5\3B\3B\3C")
        buf.write("\3C\7C\u01cc\nC\fC\16C\u01cf\13C\3C\5C\u01d2\nC\3C\3C")
        buf.write("\3D\3D\7D\u01d8\nD\fD\16D\u01db\13D\3D\3D\3D\3E\3E\3E")
        buf.write("\3\u0167\2F\3\2\5\2\7\2\t\2\13\2\r\2\17\3\21\4\23\5\25")
        buf.write("\6\27\7\31\b\33\t\35\n\37\13!\f#\r%\16\'\17)\20+\21-\22")
        buf.write("/\23\61\24\63\25\65\26\67\279\30;\31=\32?\33A\34C\35E")
        buf.write("\36G\37I K!M\"O#Q$S%U&W\'Y([)]*_+a,c-e.g/i\60k\61m\62")
        buf.write("o\63q\64s\65u\66w\67y8{9}:\177;\u0081<\u0083=\u0085>\u0087")
        buf.write("?\u0089@\3\2\r\4\2GGgg\4\2--//\3\2\62;\6\2\n\f\16\17$")
        buf.write("$^^\t\2$$^^ddhhppttvv\3\2\63;\4\2\f\f\17\17\5\2C\\aac")
        buf.write("|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\6\3\n\f\16\17$$^^")
        buf.write("\2\u01f8\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write("\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write("\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3")
        buf.write("\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s")
        buf.write("\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2")
        buf.write("}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2")
        buf.write("\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\3\u008b")
        buf.write("\3\2\2\2\5\u0094\3\2\2\2\7\u009d\3\2\2\2\t\u009f\3\2\2")
        buf.write("\2\13\u00a2\3\2\2\2\r\u00a7\3\2\2\2\17\u00ab\3\2\2\2\21")
        buf.write("\u00af\3\2\2\2\23\u00bf\3\2\2\2\25\u00cf\3\2\2\2\27\u00d1")
        buf.write("\3\2\2\2\31\u00db\3\2\2\2\33\u00e3\3\2\2\2\35\u00e8\3")
        buf.write("\2\2\2\37\u00ee\3\2\2\2!\u00f6\3\2\2\2#\u00fd\3\2\2\2")
        buf.write("%\u0102\3\2\2\2\'\u0105\3\2\2\2)\u010b\3\2\2\2+\u0113")
        buf.write("\3\2\2\2-\u011c\3\2\2\2/\u011f\3\2\2\2\61\u0124\3\2\2")
        buf.write("\2\63\u012a\3\2\2\2\65\u0131\3\2\2\2\67\u0135\3\2\2\2")
        buf.write("9\u0139\3\2\2\2;\u0142\3\2\2\2=\u0145\3\2\2\2?\u014b\3")
        buf.write("\2\2\2A\u0150\3\2\2\2C\u0156\3\2\2\2E\u0161\3\2\2\2G\u016f")
        buf.write("\3\2\2\2I\u0176\3\2\2\2K\u0178\3\2\2\2M\u017a\3\2\2\2")
        buf.write("O\u017c\3\2\2\2Q\u017e\3\2\2\2S\u0180\3\2\2\2U\u0182\3")
        buf.write("\2\2\2W\u0184\3\2\2\2Y\u0186\3\2\2\2[\u0188\3\2\2\2]\u018d")
        buf.write("\3\2\2\2_\u0191\3\2\2\2a\u0199\3\2\2\2c\u019b\3\2\2\2")
        buf.write("e\u019d\3\2\2\2g\u019f\3\2\2\2i\u01a1\3\2\2\2k\u01a3\3")
        buf.write("\2\2\2m\u01a5\3\2\2\2o\u01a7\3\2\2\2q\u01aa\3\2\2\2s\u01ad")
        buf.write("\3\2\2\2u\u01b0\3\2\2\2w\u01b3\3\2\2\2y\u01b5\3\2\2\2")
        buf.write("{\u01b7\3\2\2\2}\u01ba\3\2\2\2\177\u01bd\3\2\2\2\u0081")
        buf.write("\u01c0\3\2\2\2\u0083\u01c3\3\2\2\2\u0085\u01c9\3\2\2\2")
        buf.write("\u0087\u01d5\3\2\2\2\u0089\u01df\3\2\2\2\u008b\u008d\t")
        buf.write("\2\2\2\u008c\u008e\t\3\2\2\u008d\u008c\3\2\2\2\u008d\u008e")
        buf.write("\3\2\2\2\u008e\u0090\3\2\2\2\u008f\u0091\t\4\2\2\u0090")
        buf.write("\u008f\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0090\3\2\2\2")
        buf.write("\u0092\u0093\3\2\2\2\u0093\4\3\2\2\2\u0094\u0098\7\60")
        buf.write("\2\2\u0095\u0097\t\4\2\2\u0096\u0095\3\2\2\2\u0097\u009a")
        buf.write("\3\2\2\2\u0098\u0096\3\2\2\2\u0098\u0099\3\2\2\2\u0099")
        buf.write("\6\3\2\2\2\u009a\u0098\3\2\2\2\u009b\u009e\n\5\2\2\u009c")
        buf.write("\u009e\5\t\5\2\u009d\u009b\3\2\2\2\u009d\u009c\3\2\2\2")
        buf.write("\u009e\b\3\2\2\2\u009f\u00a0\7^\2\2\u00a0\u00a1\t\6\2")
        buf.write("\2\u00a1\n\3\2\2\2\u00a2\u00a3\7$\2\2\u00a3\f\3\2\2\2")
        buf.write("\u00a4\u00a5\7^\2\2\u00a5\u00a8\n\6\2\2\u00a6\u00a8\7")
        buf.write("^\2\2\u00a7\u00a4\3\2\2\2\u00a7\u00a6\3\2\2\2\u00a8\16")
        buf.write("\3\2\2\2\u00a9\u00ac\5)\25\2\u00aa\u00ac\5\65\33\2\u00ab")
        buf.write("\u00a9\3\2\2\2\u00ab\u00aa\3\2\2\2\u00ac\20\3\2\2\2\u00ad")
        buf.write("\u00b0\5? \2\u00ae\u00b0\5A!\2\u00af\u00ad\3\2\2\2\u00af")
        buf.write("\u00ae\3\2\2\2\u00b0\22\3\2\2\2\u00b1\u00b2\5\25\13\2")
        buf.write("\u00b2\u00b3\5\5\3\2\u00b3\u00c0\3\2\2\2\u00b4\u00b5\5")
        buf.write("\25\13\2\u00b5\u00b6\5\5\3\2\u00b6\u00b7\5\3\2\2\u00b7")
        buf.write("\u00c0\3\2\2\2\u00b8\u00b9\5\25\13\2\u00b9\u00ba\5\3\2")
        buf.write("\2\u00ba\u00c0\3\2\2\2\u00bb\u00bd\5\5\3\2\u00bc\u00be")
        buf.write("\5\3\2\2\u00bd\u00bc\3\2\2\2\u00bd\u00be\3\2\2\2\u00be")
        buf.write("\u00c0\3\2\2\2\u00bf\u00b1\3\2\2\2\u00bf\u00b4\3\2\2\2")
        buf.write("\u00bf\u00b8\3\2\2\2\u00bf\u00bb\3\2\2\2\u00c0\u00c1\3")
        buf.write("\2\2\2\u00c1\u00c2\b\n\2\2\u00c2\24\3\2\2\2\u00c3\u00d0")
        buf.write("\7\62\2\2\u00c4\u00cb\t\7\2\2\u00c5\u00c7\7a\2\2\u00c6")
        buf.write("\u00c5\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c8\3\2\2\2")
        buf.write("\u00c8\u00ca\t\4\2\2\u00c9\u00c6\3\2\2\2\u00ca\u00cd\3")
        buf.write("\2\2\2\u00cb\u00c9\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00ce")
        buf.write("\3\2\2\2\u00cd\u00cb\3\2\2\2\u00ce\u00d0\b\13\3\2\u00cf")
        buf.write("\u00c3\3\2\2\2\u00cf\u00c4\3\2\2\2\u00d0\26\3\2\2\2\u00d1")
        buf.write("\u00d5\5\13\6\2\u00d2\u00d4\5\7\4\2\u00d3\u00d2\3\2\2")
        buf.write("\2\u00d4\u00d7\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d5\u00d6")
        buf.write("\3\2\2\2\u00d6\u00d8\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d8")
        buf.write("\u00d9\5\13\6\2\u00d9\u00da\b\f\4\2\u00da\30\3\2\2\2\u00db")
        buf.write("\u00dc\7k\2\2\u00dc\u00dd\7p\2\2\u00dd\u00de\7v\2\2\u00de")
        buf.write("\u00df\7g\2\2\u00df\u00e0\7i\2\2\u00e0\u00e1\7g\2\2\u00e1")
        buf.write("\u00e2\7t\2\2\u00e2\32\3\2\2\2\u00e3\u00e4\7x\2\2\u00e4")
        buf.write("\u00e5\7q\2\2\u00e5\u00e6\7k\2\2\u00e6\u00e7\7f\2\2\u00e7")
        buf.write("\34\3\2\2\2\u00e8\u00e9\7h\2\2\u00e9\u00ea\7n\2\2\u00ea")
        buf.write("\u00eb\7q\2\2\u00eb\u00ec\7c\2\2\u00ec\u00ed\7v\2\2\u00ed")
        buf.write("\36\3\2\2\2\u00ee\u00ef\7d\2\2\u00ef\u00f0\7q\2\2\u00f0")
        buf.write("\u00f1\7q\2\2\u00f1\u00f2\7n\2\2\u00f2\u00f3\7g\2\2\u00f3")
        buf.write("\u00f4\7c\2\2\u00f4\u00f5\7p\2\2\u00f5 \3\2\2\2\u00f6")
        buf.write("\u00f7\7u\2\2\u00f7\u00f8\7v\2\2\u00f8\u00f9\7t\2\2\u00f9")
        buf.write("\u00fa\7k\2\2\u00fa\u00fb\7p\2\2\u00fb\u00fc\7i\2\2\u00fc")
        buf.write("\"\3\2\2\2\u00fd\u00fe\7c\2\2\u00fe\u00ff\7w\2\2\u00ff")
        buf.write("\u0100\7v\2\2\u0100\u0101\7q\2\2\u0101$\3\2\2\2\u0102")
        buf.write("\u0103\7q\2\2\u0103\u0104\7h\2\2\u0104&\3\2\2\2\u0105")
        buf.write("\u0106\7c\2\2\u0106\u0107\7t\2\2\u0107\u0108\7t\2\2\u0108")
        buf.write("\u0109\7c\2\2\u0109\u010a\7{\2\2\u010a(\3\2\2\2\u010b")
        buf.write("\u010c\7k\2\2\u010c\u010d\7p\2\2\u010d\u010e\7j\2\2\u010e")
        buf.write("\u010f\7g\2\2\u010f\u0110\7t\2\2\u0110\u0111\7k\2\2\u0111")
        buf.write("\u0112\7v\2\2\u0112*\3\2\2\2\u0113\u0114\7h\2\2\u0114")
        buf.write("\u0115\7w\2\2\u0115\u0116\7p\2\2\u0116\u0117\7e\2\2\u0117")
        buf.write("\u0118\7v\2\2\u0118\u0119\7k\2\2\u0119\u011a\7q\2\2\u011a")
        buf.write("\u011b\7p\2\2\u011b,\3\2\2\2\u011c\u011d\7k\2\2\u011d")
        buf.write("\u011e\7h\2\2\u011e.\3\2\2\2\u011f\u0120\7g\2\2\u0120")
        buf.write("\u0121\7n\2\2\u0121\u0122\7u\2\2\u0122\u0123\7g\2\2\u0123")
        buf.write("\60\3\2\2\2\u0124\u0125\7d\2\2\u0125\u0126\7t\2\2\u0126")
        buf.write("\u0127\7g\2\2\u0127\u0128\7c\2\2\u0128\u0129\7m\2\2\u0129")
        buf.write("\62\3\2\2\2\u012a\u012b\7t\2\2\u012b\u012c\7g\2\2\u012c")
        buf.write("\u012d\7v\2\2\u012d\u012e\7w\2\2\u012e\u012f\7t\2\2\u012f")
        buf.write("\u0130\7p\2\2\u0130\64\3\2\2\2\u0131\u0132\7q\2\2\u0132")
        buf.write("\u0133\7w\2\2\u0133\u0134\7v\2\2\u0134\66\3\2\2\2\u0135")
        buf.write("\u0136\7h\2\2\u0136\u0137\7q\2\2\u0137\u0138\7t\2\2\u0138")
        buf.write("8\3\2\2\2\u0139\u013a\7e\2\2\u013a\u013b\7q\2\2\u013b")
        buf.write("\u013c\7p\2\2\u013c\u013d\7v\2\2\u013d\u013e\7k\2\2\u013e")
        buf.write("\u013f\7p\2\2\u013f\u0140\7w\2\2\u0140\u0141\7g\2\2\u0141")
        buf.write(":\3\2\2\2\u0142\u0143\7f\2\2\u0143\u0144\7q\2\2\u0144")
        buf.write("<\3\2\2\2\u0145\u0146\7y\2\2\u0146\u0147\7j\2\2\u0147")
        buf.write("\u0148\7k\2\2\u0148\u0149\7n\2\2\u0149\u014a\7g\2\2\u014a")
        buf.write(">\3\2\2\2\u014b\u014c\7v\2\2\u014c\u014d\7t\2\2\u014d")
        buf.write("\u014e\7w\2\2\u014e\u014f\7g\2\2\u014f@\3\2\2\2\u0150")
        buf.write("\u0151\7h\2\2\u0151\u0152\7c\2\2\u0152\u0153\7n\2\2\u0153")
        buf.write("\u0154\7u\2\2\u0154\u0155\7g\2\2\u0155B\3\2\2\2\u0156")
        buf.write("\u0157\7\61\2\2\u0157\u0158\7\61\2\2\u0158\u015c\3\2\2")
        buf.write("\2\u0159\u015b\n\b\2\2\u015a\u0159\3\2\2\2\u015b\u015e")
        buf.write("\3\2\2\2\u015c\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015d")
        buf.write("\u015f\3\2\2\2\u015e\u015c\3\2\2\2\u015f\u0160\b\"\5\2")
        buf.write("\u0160D\3\2\2\2\u0161\u0162\7\61\2\2\u0162\u0163\7,\2")
        buf.write("\2\u0163\u0167\3\2\2\2\u0164\u0166\13\2\2\2\u0165\u0164")
        buf.write("\3\2\2\2\u0166\u0169\3\2\2\2\u0167\u0168\3\2\2\2\u0167")
        buf.write("\u0165\3\2\2\2\u0168\u016a\3\2\2\2\u0169\u0167\3\2\2\2")
        buf.write("\u016a\u016b\7,\2\2\u016b\u016c\7\61\2\2\u016c\u016d\3")
        buf.write("\2\2\2\u016d\u016e\b#\5\2\u016eF\3\2\2\2\u016f\u0173\t")
        buf.write("\t\2\2\u0170\u0172\t\n\2\2\u0171\u0170\3\2\2\2\u0172\u0175")
        buf.write("\3\2\2\2\u0173\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174")
        buf.write("H\3\2\2\2\u0175\u0173\3\2\2\2\u0176\u0177\7*\2\2\u0177")
        buf.write("J\3\2\2\2\u0178\u0179\7+\2\2\u0179L\3\2\2\2\u017a\u017b")
        buf.write("\7]\2\2\u017bN\3\2\2\2\u017c\u017d\7_\2\2\u017dP\3\2\2")
        buf.write("\2\u017e\u017f\7\60\2\2\u017fR\3\2\2\2\u0180\u0181\7.")
        buf.write("\2\2\u0181T\3\2\2\2\u0182\u0183\7=\2\2\u0183V\3\2\2\2")
        buf.write("\u0184\u0185\7<\2\2\u0185X\3\2\2\2\u0186\u0187\7}\2\2")
        buf.write("\u0187Z\3\2\2\2\u0188\u0189\7\177\2\2\u0189\\\3\2\2\2")
        buf.write("\u018a\u018e\5g\64\2\u018b\u018e\5i\65\2\u018c\u018e\5")
        buf.write("k\66\2\u018d\u018a\3\2\2\2\u018d\u018b\3\2\2\2\u018d\u018c")
        buf.write("\3\2\2\2\u018e^\3\2\2\2\u018f\u0192\5o8\2\u0190\u0192")
        buf.write("\5q9\2\u0191\u018f\3\2\2\2\u0191\u0190\3\2\2\2\u0192`")
        buf.write("\3\2\2\2\u0193\u019a\5s:\2\u0194\u019a\5u;\2\u0195\u019a")
        buf.write("\5y=\2\u0196\u019a\5}?\2\u0197\u019a\5w<\2\u0198\u019a")
        buf.write("\5{>\2\u0199\u0193\3\2\2\2\u0199\u0194\3\2\2\2\u0199\u0195")
        buf.write("\3\2\2\2\u0199\u0196\3\2\2\2\u0199\u0197\3\2\2\2\u0199")
        buf.write("\u0198\3\2\2\2\u019ab\3\2\2\2\u019b\u019c\7-\2\2\u019c")
        buf.write("d\3\2\2\2\u019d\u019e\7/\2\2\u019ef\3\2\2\2\u019f\u01a0")
        buf.write("\7,\2\2\u01a0h\3\2\2\2\u01a1\u01a2\7\61\2\2\u01a2j\3\2")
        buf.write("\2\2\u01a3\u01a4\7\'\2\2\u01a4l\3\2\2\2\u01a5\u01a6\7")
        buf.write("#\2\2\u01a6n\3\2\2\2\u01a7\u01a8\7(\2\2\u01a8\u01a9\7")
        buf.write("(\2\2\u01a9p\3\2\2\2\u01aa\u01ab\7~\2\2\u01ab\u01ac\7")
        buf.write("~\2\2\u01acr\3\2\2\2\u01ad\u01ae\7?\2\2\u01ae\u01af\7")
        buf.write("?\2\2\u01aft\3\2\2\2\u01b0\u01b1\7#\2\2\u01b1\u01b2\7")
        buf.write("?\2\2\u01b2v\3\2\2\2\u01b3\u01b4\7>\2\2\u01b4x\3\2\2\2")
        buf.write("\u01b5\u01b6\7@\2\2\u01b6z\3\2\2\2\u01b7\u01b8\7>\2\2")
        buf.write("\u01b8\u01b9\7?\2\2\u01b9|\3\2\2\2\u01ba\u01bb\7@\2\2")
        buf.write("\u01bb\u01bc\7?\2\2\u01bc~\3\2\2\2\u01bd\u01be\7<\2\2")
        buf.write("\u01be\u01bf\7<\2\2\u01bf\u0080\3\2\2\2\u01c0\u01c1\7")
        buf.write("?\2\2\u01c1\u0082\3\2\2\2\u01c2\u01c4\t\13\2\2\u01c3\u01c2")
        buf.write("\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c5")
        buf.write("\u01c6\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7\u01c8\bB\5\2")
        buf.write("\u01c8\u0084\3\2\2\2\u01c9\u01cd\5\13\6\2\u01ca\u01cc")
        buf.write("\5\7\4\2\u01cb\u01ca\3\2\2\2\u01cc\u01cf\3\2\2\2\u01cd")
        buf.write("\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01d1\3\2\2\2")
        buf.write("\u01cf\u01cd\3\2\2\2\u01d0\u01d2\t\f\2\2\u01d1\u01d0\3")
        buf.write("\2\2\2\u01d2\u01d3\3\2\2\2\u01d3\u01d4\bC\6\2\u01d4\u0086")
        buf.write("\3\2\2\2\u01d5\u01d9\5\13\6\2\u01d6\u01d8\5\7\4\2\u01d7")
        buf.write("\u01d6\3\2\2\2\u01d8\u01db\3\2\2\2\u01d9\u01d7\3\2\2\2")
        buf.write("\u01d9\u01da\3\2\2\2\u01da\u01dc\3\2\2\2\u01db\u01d9\3")
        buf.write("\2\2\2\u01dc\u01dd\5\r\7\2\u01dd\u01de\bD\7\2\u01de\u0088")
        buf.write("\3\2\2\2\u01df\u01e0\13\2\2\2\u01e0\u01e1\bE\b\2\u01e1")
        buf.write("\u008a\3\2\2\2\32\2\u008d\u0092\u0098\u009d\u00a7\u00ab")
        buf.write("\u00af\u00bd\u00bf\u00c6\u00cb\u00cf\u00d5\u015c\u0167")
        buf.write("\u0173\u018d\u0191\u0199\u01c5\u01cd\u01d1\u01d9\t\3\n")
        buf.write("\2\3\13\3\3\f\4\b\2\2\3C\5\3D\6\3E\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PARAM_KEYWORDS = 1
    BOOLLIT = 2
    FLOATLIT = 3
    INTLIT = 4
    STRINGLIT = 5
    INTEGER = 6
    VOID = 7
    FLOAT = 8
    BOOLEAN = 9
    STRING = 10
    AUTO = 11
    OF = 12
    ARR = 13
    INHERIT = 14
    FUNCTION = 15
    IF = 16
    ELSE = 17
    BREAK = 18
    RETURN = 19
    OUT = 20
    FOR = 21
    CONTINUE = 22
    DO = 23
    WHILE = 24
    TRUE = 25
    FALSE = 26
    COMMENT = 27
    C_COMMENT = 28
    ID = 29
    LB = 30
    RB = 31
    SQLB = 32
    SQRB = 33
    DOT = 34
    COMMA = 35
    SEMI = 36
    COLON = 37
    LCB = 38
    RCB = 39
    MULDIVMOD = 40
    ANDOR = 41
    COMPARE = 42
    ADD = 43
    MINUS = 44
    MUL = 45
    DIV = 46
    PCENT = 47
    NOT = 48
    AND = 49
    OR = 50
    SAME = 51
    NOTSAME = 52
    LOWER = 53
    HIGHER = 54
    LOWER_EQ = 55
    HIGHER_EQ = 56
    SCOPE = 57
    EQ = 58
    WS = 59
    UNCLOSE_STRING = 60
    ILLEGAL_ESCAPE = 61
    ERROR_CHAR = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'integer'", "'void'", "'float'", "'boolean'", "'string'", "'auto'", 
            "'of'", "'array'", "'inherit'", "'function'", "'if'", "'else'", 
            "'break'", "'return'", "'out'", "'for'", "'continue'", "'do'", 
            "'while'", "'true'", "'false'", "'('", "')'", "'['", "']'", 
            "'.'", "','", "';'", "':'", "'{'", "'}'", "'+'", "'-'", "'*'", 
            "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", 
            "'>'", "'<='", "'>='", "'::'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "PARAM_KEYWORDS", "BOOLLIT", "FLOATLIT", "INTLIT", "STRINGLIT", 
            "INTEGER", "VOID", "FLOAT", "BOOLEAN", "STRING", "AUTO", "OF", 
            "ARR", "INHERIT", "FUNCTION", "IF", "ELSE", "BREAK", "RETURN", 
            "OUT", "FOR", "CONTINUE", "DO", "WHILE", "TRUE", "FALSE", "COMMENT", 
            "C_COMMENT", "ID", "LB", "RB", "SQLB", "SQRB", "DOT", "COMMA", 
            "SEMI", "COLON", "LCB", "RCB", "MULDIVMOD", "ANDOR", "COMPARE", 
            "ADD", "MINUS", "MUL", "DIV", "PCENT", "NOT", "AND", "OR", "SAME", 
            "NOTSAME", "LOWER", "HIGHER", "LOWER_EQ", "HIGHER_EQ", "SCOPE", 
            "EQ", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "EXPPART", "DECPART", "StringChar", "ESC2", "DOUBLEQ", 
                  "IllegalString", "PARAM_KEYWORDS", "BOOLLIT", "FLOATLIT", 
                  "INTLIT", "STRINGLIT", "INTEGER", "VOID", "FLOAT", "BOOLEAN", 
                  "STRING", "AUTO", "OF", "ARR", "INHERIT", "FUNCTION", 
                  "IF", "ELSE", "BREAK", "RETURN", "OUT", "FOR", "CONTINUE", 
                  "DO", "WHILE", "TRUE", "FALSE", "COMMENT", "C_COMMENT", 
                  "ID", "LB", "RB", "SQLB", "SQRB", "DOT", "COMMA", "SEMI", 
                  "COLON", "LCB", "RCB", "MULDIVMOD", "ANDOR", "COMPARE", 
                  "ADD", "MINUS", "MUL", "DIV", "PCENT", "NOT", "AND", "OR", 
                  "SAME", "NOTSAME", "LOWER", "HIGHER", "LOWER_EQ", "HIGHER_EQ", 
                  "SCOPE", "EQ", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

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
            actions[8] = self.FLOATLIT_action 
            actions[9] = self.INTLIT_action 
            actions[10] = self.STRINGLIT_action 
            actions[65] = self.UNCLOSE_STRING_action 
            actions[66] = self.ILLEGAL_ESCAPE_action 
            actions[67] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_', '')
     

    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_', '')
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                    result = str(self.text)
                    self.text = result[1:-1]
                
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                    unclose_str = str(self.text)
                    possible = ['\b', '\t', '\f', '\n', '\r', '"', '\\']
                    if unclose_str[-1] in possible:
                        raise UncloseString(unclose_str[1:-1])
                    else:
                        raise UncloseString(unclose_str[1:])
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                    illegal_str = str(self.text)
                    raise IllegalEscape(illegal_str[1:])
                
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                    raise ErrorToken(self.text)
                
     


