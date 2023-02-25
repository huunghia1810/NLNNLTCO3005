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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2G")
        buf.write("\u0205\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6")
        buf.write("\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\7\t\u00b0\n\t\f\t\16")
        buf.write("\t\u00b3\13\t\3\t\3\t\3\t\5\t\u00b8\n\t\3\n\3\n\3\n\5")
        buf.write("\n\u00bd\n\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00c7")
        buf.write("\n\n\3\13\3\13\7\13\u00cb\n\13\f\13\16\13\u00ce\13\13")
        buf.write("\3\f\3\f\5\f\u00d2\n\f\3\f\6\f\u00d5\n\f\r\f\16\f\u00d6")
        buf.write("\3\r\3\r\3\16\3\16\3\17\3\17\5\17\u00df\n\17\3\20\3\20")
        buf.write("\7\20\u00e3\n\20\f\20\16\20\u00e6\13\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\5\21\u00ed\n\21\3\22\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\5\22\u00ff\n\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3")
        buf.write("\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3")
        buf.write("\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3")
        buf.write("(\3(\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3-\3-\3")
        buf.write(".\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3")
        buf.write("\60\3\60\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\67\3\67\3\67\38\38\38\38\38\38")
        buf.write("\38\38\39\39\39\39\3:\3:\3:\3:\3:\3:\3:\3;\3;\3;\3;\3")
        buf.write(";\3;\3;\3<\3<\3<\3<\3<\3=\3=\3=\3=\3=\3=\3>\3>\3>\3>\3")
        buf.write(">\3?\3?\3?\3@\3@\3@\3@\3A\3A\3A\3A\3A\3A\3A\3A\3A\3B\3")
        buf.write("B\3B\3C\3C\3C\3C\3C\3C\3C\3C\3D\3D\3D\3D\3D\3D\3E\3E\7")
        buf.write("E\u01c5\nE\fE\16E\u01c8\13E\3F\3F\3F\3F\7F\u01ce\nF\f")
        buf.write("F\16F\u01d1\13F\3F\3F\3F\3F\3F\3G\3G\3G\3G\7G\u01dc\n")
        buf.write("G\fG\16G\u01df\13G\3G\3G\3H\6H\u01e4\nH\rH\16H\u01e5\3")
        buf.write("H\3H\3I\3I\7I\u01ec\nI\fI\16I\u01ef\13I\3J\3J\3J\3J\7")
        buf.write("J\u01f5\nJ\fJ\16J\u01f8\13J\3K\3K\3K\3L\3L\3L\3M\3M\3")
        buf.write("M\3N\3N\3N\3\u01cf\2O\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\2\27\2\31\2\33\2\35\f\37\r!\2#\2%\16\'\17")
        buf.write(")\20+\21-\22/\23\61\24\63\25\65\26\67\279\30;\31=\32?")
        buf.write("\33A\34C\35E\36G\37I K!M\"O#Q$S%U&W\'Y([)]*_+a,c-e.g/")
        buf.write("i\60k\61m\62o\63q\64s\65u\66w\67y8{9}:\177;\u0081<\u0083")
        buf.write("=\u0085>\u0087?\u0089@\u008bA\u008dB\u008fC\u0091\2\u0093")
        buf.write("\2\u0095D\u0097E\u0099F\u009bG\3\2\13\4\2GGgg\4\2--//")
        buf.write("\3\2\62;\3\2\63;\4\2$$^^\5\2C\\aac|\6\2\62;C\\aac|\4\2")
        buf.write("\f\f\17\17\5\2\13\f\16\17\"\"\2\u0215\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
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
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\2\u008f\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099")
        buf.write("\3\2\2\2\2\u009b\3\2\2\2\3\u009d\3\2\2\2\5\u009f\3\2\2")
        buf.write("\2\7\u00a1\3\2\2\2\t\u00a3\3\2\2\2\13\u00a5\3\2\2\2\r")
        buf.write("\u00a7\3\2\2\2\17\u00a9\3\2\2\2\21\u00b7\3\2\2\2\23\u00c6")
        buf.write("\3\2\2\2\25\u00c8\3\2\2\2\27\u00cf\3\2\2\2\31\u00d8\3")
        buf.write("\2\2\2\33\u00da\3\2\2\2\35\u00de\3\2\2\2\37\u00e0\3\2")
        buf.write("\2\2!\u00ec\3\2\2\2#\u00fe\3\2\2\2%\u0100\3\2\2\2\'\u0102")
        buf.write("\3\2\2\2)\u0104\3\2\2\2+\u0106\3\2\2\2-\u0108\3\2\2\2")
        buf.write("/\u010a\3\2\2\2\61\u010c\3\2\2\2\63\u010e\3\2\2\2\65\u0110")
        buf.write("\3\2\2\2\67\u0112\3\2\2\29\u0114\3\2\2\2;\u0116\3\2\2")
        buf.write("\2=\u0118\3\2\2\2?\u011a\3\2\2\2A\u011c\3\2\2\2C\u011e")
        buf.write("\3\2\2\2E\u0120\3\2\2\2G\u0122\3\2\2\2I\u0125\3\2\2\2")
        buf.write("K\u0128\3\2\2\2M\u012b\3\2\2\2O\u012e\3\2\2\2Q\u0130\3")
        buf.write("\2\2\2S\u0132\3\2\2\2U\u0135\3\2\2\2W\u0138\3\2\2\2Y\u013b")
        buf.write("\3\2\2\2[\u0140\3\2\2\2]\u0145\3\2\2\2_\u014b\3\2\2\2")
        buf.write("a\u0153\3\2\2\2c\u0156\3\2\2\2e\u015b\3\2\2\2g\u0161\3")
        buf.write("\2\2\2i\u0167\3\2\2\2k\u016b\3\2\2\2m\u0174\3\2\2\2o\u0177")
        buf.write("\3\2\2\2q\u017f\3\2\2\2s\u0183\3\2\2\2u\u018a\3\2\2\2")
        buf.write("w\u0191\3\2\2\2y\u0196\3\2\2\2{\u019c\3\2\2\2}\u01a1\3")
        buf.write("\2\2\2\177\u01a4\3\2\2\2\u0081\u01a8\3\2\2\2\u0083\u01b1")
        buf.write("\3\2\2\2\u0085\u01b4\3\2\2\2\u0087\u01bc\3\2\2\2\u0089")
        buf.write("\u01c2\3\2\2\2\u008b\u01c9\3\2\2\2\u008d\u01d7\3\2\2\2")
        buf.write("\u008f\u01e3\3\2\2\2\u0091\u01e9\3\2\2\2\u0093\u01f0\3")
        buf.write("\2\2\2\u0095\u01f9\3\2\2\2\u0097\u01fc\3\2\2\2\u0099\u01ff")
        buf.write("\3\2\2\2\u009b\u0202\3\2\2\2\u009d\u009e\5u;\2\u009e\4")
        buf.write("\3\2\2\2\u009f\u00a0\5o8\2\u00a0\6\3\2\2\2\u00a1\u00a2")
        buf.write("\5g\64\2\u00a2\b\3\2\2\2\u00a3\u00a4\5_\60\2\u00a4\n\3")
        buf.write("\2\2\2\u00a5\u00a6\5\u0087D\2\u00a6\f\3\2\2\2\u00a7\u00a8")
        buf.write("\5{>\2\u00a8\16\3\2\2\2\u00a9\u00aa\5[.\2\u00aa\20\3\2")
        buf.write("\2\2\u00ab\u00b1\5\33\16\2\u00ac\u00ad\7a\2\2\u00ad\u00b0")
        buf.write("\5\31\r\2\u00ae\u00b0\5\31\r\2\u00af\u00ac\3\2\2\2\u00af")
        buf.write("\u00ae\3\2\2\2\u00b0\u00b3\3\2\2\2\u00b1\u00af\3\2\2\2")
        buf.write("\u00b1\u00b2\3\2\2\2\u00b2\u00b4\3\2\2\2\u00b3\u00b1\3")
        buf.write("\2\2\2\u00b4\u00b5\b\t\2\2\u00b5\u00b8\3\2\2\2\u00b6\u00b8")
        buf.write("\7\62\2\2\u00b7\u00ab\3\2\2\2\u00b7\u00b6\3\2\2\2\u00b8")
        buf.write("\22\3\2\2\2\u00b9\u00ba\5\21\t\2\u00ba\u00bc\5\25\13\2")
        buf.write("\u00bb\u00bd\5\27\f\2\u00bc\u00bb\3\2\2\2\u00bc\u00bd")
        buf.write("\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00bf\b\n\3\2\u00bf")
        buf.write("\u00c7\3\2\2\2\u00c0\u00c1\5\21\t\2\u00c1\u00c2\5\27\f")
        buf.write("\2\u00c2\u00c7\3\2\2\2\u00c3\u00c4\5\25\13\2\u00c4\u00c5")
        buf.write("\5\27\f\2\u00c5\u00c7\3\2\2\2\u00c6\u00b9\3\2\2\2\u00c6")
        buf.write("\u00c0\3\2\2\2\u00c6\u00c3\3\2\2\2\u00c7\24\3\2\2\2\u00c8")
        buf.write("\u00cc\7\60\2\2\u00c9\u00cb\5\31\r\2\u00ca\u00c9\3\2\2")
        buf.write("\2\u00cb\u00ce\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cc\u00cd")
        buf.write("\3\2\2\2\u00cd\26\3\2\2\2\u00ce\u00cc\3\2\2\2\u00cf\u00d1")
        buf.write("\t\2\2\2\u00d0\u00d2\t\3\2\2\u00d1\u00d0\3\2\2\2\u00d1")
        buf.write("\u00d2\3\2\2\2\u00d2\u00d4\3\2\2\2\u00d3\u00d5\5\31\r")
        buf.write("\2\u00d4\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d4")
        buf.write("\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\30\3\2\2\2\u00d8\u00d9")
        buf.write("\t\4\2\2\u00d9\32\3\2\2\2\u00da\u00db\t\5\2\2\u00db\34")
        buf.write("\3\2\2\2\u00dc\u00df\5w<\2\u00dd\u00df\5e\63\2\u00de\u00dc")
        buf.write("\3\2\2\2\u00de\u00dd\3\2\2\2\u00df\36\3\2\2\2\u00e0\u00e4")
        buf.write("\7$\2\2\u00e1\u00e3\5!\21\2\u00e2\u00e1\3\2\2\2\u00e3")
        buf.write("\u00e6\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2")
        buf.write("\u00e5\u00e7\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e7\u00e8\7")
        buf.write("$\2\2\u00e8\u00e9\b\20\4\2\u00e9 \3\2\2\2\u00ea\u00ed")
        buf.write("\n\6\2\2\u00eb\u00ed\5#\22\2\u00ec\u00ea\3\2\2\2\u00ec")
        buf.write("\u00eb\3\2\2\2\u00ed\"\3\2\2\2\u00ee\u00ef\7^\2\2\u00ef")
        buf.write("\u00ff\7d\2\2\u00f0\u00f1\7^\2\2\u00f1\u00ff\7h\2\2\u00f2")
        buf.write("\u00f3\7^\2\2\u00f3\u00ff\7t\2\2\u00f4\u00f5\7^\2\2\u00f5")
        buf.write("\u00ff\7p\2\2\u00f6\u00f7\7^\2\2\u00f7\u00ff\7v\2\2\u00f8")
        buf.write("\u00f9\7^\2\2\u00f9\u00ff\7)\2\2\u00fa\u00fb\7^\2\2\u00fb")
        buf.write("\u00ff\7^\2\2\u00fc\u00fd\7^\2\2\u00fd\u00ff\7$\2\2\u00fe")
        buf.write("\u00ee\3\2\2\2\u00fe\u00f0\3\2\2\2\u00fe\u00f2\3\2\2\2")
        buf.write("\u00fe\u00f4\3\2\2\2\u00fe\u00f6\3\2\2\2\u00fe\u00f8\3")
        buf.write("\2\2\2\u00fe\u00fa\3\2\2\2\u00fe\u00fc\3\2\2\2\u00ff$")
        buf.write("\3\2\2\2\u0100\u0101\7*\2\2\u0101&\3\2\2\2\u0102\u0103")
        buf.write("\7+\2\2\u0103(\3\2\2\2\u0104\u0105\7]\2\2\u0105*\3\2\2")
        buf.write("\2\u0106\u0107\7_\2\2\u0107,\3\2\2\2\u0108\u0109\7\60")
        buf.write("\2\2\u0109.\3\2\2\2\u010a\u010b\7.\2\2\u010b\60\3\2\2")
        buf.write("\2\u010c\u010d\7=\2\2\u010d\62\3\2\2\2\u010e\u010f\7<")
        buf.write("\2\2\u010f\64\3\2\2\2\u0110\u0111\7}\2\2\u0111\66\3\2")
        buf.write("\2\2\u0112\u0113\7\177\2\2\u01138\3\2\2\2\u0114\u0115")
        buf.write("\7?\2\2\u0115:\3\2\2\2\u0116\u0117\7-\2\2\u0117<\3\2\2")
        buf.write("\2\u0118\u0119\7/\2\2\u0119>\3\2\2\2\u011a\u011b\7,\2")
        buf.write("\2\u011b@\3\2\2\2\u011c\u011d\7\61\2\2\u011dB\3\2\2\2")
        buf.write("\u011e\u011f\7\'\2\2\u011fD\3\2\2\2\u0120\u0121\7#\2\2")
        buf.write("\u0121F\3\2\2\2\u0122\u0123\7(\2\2\u0123\u0124\7(\2\2")
        buf.write("\u0124H\3\2\2\2\u0125\u0126\7~\2\2\u0126\u0127\7~\2\2")
        buf.write("\u0127J\3\2\2\2\u0128\u0129\7?\2\2\u0129\u012a\7?\2\2")
        buf.write("\u012aL\3\2\2\2\u012b\u012c\7#\2\2\u012c\u012d\7?\2\2")
        buf.write("\u012dN\3\2\2\2\u012e\u012f\7>\2\2\u012fP\3\2\2\2\u0130")
        buf.write("\u0131\7@\2\2\u0131R\3\2\2\2\u0132\u0133\7>\2\2\u0133")
        buf.write("\u0134\7?\2\2\u0134T\3\2\2\2\u0135\u0136\7@\2\2\u0136")
        buf.write("\u0137\7?\2\2\u0137V\3\2\2\2\u0138\u0139\7<\2\2\u0139")
        buf.write("\u013a\7<\2\2\u013aX\3\2\2\2\u013b\u013c\7o\2\2\u013c")
        buf.write("\u013d\7c\2\2\u013d\u013e\7k\2\2\u013e\u013f\7p\2\2\u013f")
        buf.write("Z\3\2\2\2\u0140\u0141\7c\2\2\u0141\u0142\7w\2\2\u0142")
        buf.write("\u0143\7v\2\2\u0143\u0144\7q\2\2\u0144\\\3\2\2\2\u0145")
        buf.write("\u0146\7d\2\2\u0146\u0147\7t\2\2\u0147\u0148\7g\2\2\u0148")
        buf.write("\u0149\7c\2\2\u0149\u014a\7m\2\2\u014a^\3\2\2\2\u014b")
        buf.write("\u014c\7d\2\2\u014c\u014d\7q\2\2\u014d\u014e\7q\2\2\u014e")
        buf.write("\u014f\7n\2\2\u014f\u0150\7g\2\2\u0150\u0151\7c\2\2\u0151")
        buf.write("\u0152\7p\2\2\u0152`\3\2\2\2\u0153\u0154\7f\2\2\u0154")
        buf.write("\u0155\7q\2\2\u0155b\3\2\2\2\u0156\u0157\7g\2\2\u0157")
        buf.write("\u0158\7n\2\2\u0158\u0159\7u\2\2\u0159\u015a\7g\2\2\u015a")
        buf.write("d\3\2\2\2\u015b\u015c\7h\2\2\u015c\u015d\7c\2\2\u015d")
        buf.write("\u015e\7n\2\2\u015e\u015f\7u\2\2\u015f\u0160\7g\2\2\u0160")
        buf.write("f\3\2\2\2\u0161\u0162\7h\2\2\u0162\u0163\7n\2\2\u0163")
        buf.write("\u0164\7q\2\2\u0164\u0165\7c\2\2\u0165\u0166\7v\2\2\u0166")
        buf.write("h\3\2\2\2\u0167\u0168\7h\2\2\u0168\u0169\7q\2\2\u0169")
        buf.write("\u016a\7t\2\2\u016aj\3\2\2\2\u016b\u016c\7h\2\2\u016c")
        buf.write("\u016d\7w\2\2\u016d\u016e\7p\2\2\u016e\u016f\7e\2\2\u016f")
        buf.write("\u0170\7v\2\2\u0170\u0171\7k\2\2\u0171\u0172\7q\2\2\u0172")
        buf.write("\u0173\7p\2\2\u0173l\3\2\2\2\u0174\u0175\7k\2\2\u0175")
        buf.write("\u0176\7h\2\2\u0176n\3\2\2\2\u0177\u0178\7k\2\2\u0178")
        buf.write("\u0179\7p\2\2\u0179\u017a\7v\2\2\u017a\u017b\7g\2\2\u017b")
        buf.write("\u017c\7i\2\2\u017c\u017d\7g\2\2\u017d\u017e\7t\2\2\u017e")
        buf.write("p\3\2\2\2\u017f\u0180\7k\2\2\u0180\u0181\7p\2\2\u0181")
        buf.write("\u0182\7v\2\2\u0182r\3\2\2\2\u0183\u0184\7t\2\2\u0184")
        buf.write("\u0185\7g\2\2\u0185\u0186\7v\2\2\u0186\u0187\7w\2\2\u0187")
        buf.write("\u0188\7t\2\2\u0188\u0189\7p\2\2\u0189t\3\2\2\2\u018a")
        buf.write("\u018b\7u\2\2\u018b\u018c\7v\2\2\u018c\u018d\7t\2\2\u018d")
        buf.write("\u018e\7k\2\2\u018e\u018f\7p\2\2\u018f\u0190\7i\2\2\u0190")
        buf.write("v\3\2\2\2\u0191\u0192\7v\2\2\u0192\u0193\7t\2\2\u0193")
        buf.write("\u0194\7w\2\2\u0194\u0195\7g\2\2\u0195x\3\2\2\2\u0196")
        buf.write("\u0197\7y\2\2\u0197\u0198\7j\2\2\u0198\u0199\7k\2\2\u0199")
        buf.write("\u019a\7n\2\2\u019a\u019b\7g\2\2\u019bz\3\2\2\2\u019c")
        buf.write("\u019d\7x\2\2\u019d\u019e\7q\2\2\u019e\u019f\7k\2\2\u019f")
        buf.write("\u01a0\7f\2\2\u01a0|\3\2\2\2\u01a1\u01a2\7k\2\2\u01a2")
        buf.write("\u01a3\7p\2\2\u01a3~\3\2\2\2\u01a4\u01a5\7q\2\2\u01a5")
        buf.write("\u01a6\7w\2\2\u01a6\u01a7\7v\2\2\u01a7\u0080\3\2\2\2\u01a8")
        buf.write("\u01a9\7e\2\2\u01a9\u01aa\7q\2\2\u01aa\u01ab\7p\2\2\u01ab")
        buf.write("\u01ac\7v\2\2\u01ac\u01ad\7k\2\2\u01ad\u01ae\7p\2\2\u01ae")
        buf.write("\u01af\7w\2\2\u01af\u01b0\7g\2\2\u01b0\u0082\3\2\2\2\u01b1")
        buf.write("\u01b2\7q\2\2\u01b2\u01b3\7h\2\2\u01b3\u0084\3\2\2\2\u01b4")
        buf.write("\u01b5\7k\2\2\u01b5\u01b6\7p\2\2\u01b6\u01b7\7j\2\2\u01b7")
        buf.write("\u01b8\7g\2\2\u01b8\u01b9\7t\2\2\u01b9\u01ba\7k\2\2\u01ba")
        buf.write("\u01bb\7v\2\2\u01bb\u0086\3\2\2\2\u01bc\u01bd\7c\2\2\u01bd")
        buf.write("\u01be\7t\2\2\u01be\u01bf\7t\2\2\u01bf\u01c0\7c\2\2\u01c0")
        buf.write("\u01c1\7{\2\2\u01c1\u0088\3\2\2\2\u01c2\u01c6\t\7\2\2")
        buf.write("\u01c3\u01c5\t\b\2\2\u01c4\u01c3\3\2\2\2\u01c5\u01c8\3")
        buf.write("\2\2\2\u01c6\u01c4\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7\u008a")
        buf.write("\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c9\u01ca\7\61\2\2\u01ca")
        buf.write("\u01cb\7,\2\2\u01cb\u01cf\3\2\2\2\u01cc\u01ce\13\2\2\2")
        buf.write("\u01cd\u01cc\3\2\2\2\u01ce\u01d1\3\2\2\2\u01cf\u01d0\3")
        buf.write("\2\2\2\u01cf\u01cd\3\2\2\2\u01d0\u01d2\3\2\2\2\u01d1\u01cf")
        buf.write("\3\2\2\2\u01d2\u01d3\7,\2\2\u01d3\u01d4\7\61\2\2\u01d4")
        buf.write("\u01d5\3\2\2\2\u01d5\u01d6\bF\5\2\u01d6\u008c\3\2\2\2")
        buf.write("\u01d7\u01d8\7\61\2\2\u01d8\u01d9\7\61\2\2\u01d9\u01dd")
        buf.write("\3\2\2\2\u01da\u01dc\n\t\2\2\u01db\u01da\3\2\2\2\u01dc")
        buf.write("\u01df\3\2\2\2\u01dd\u01db\3\2\2\2\u01dd\u01de\3\2\2\2")
        buf.write("\u01de\u01e0\3\2\2\2\u01df\u01dd\3\2\2\2\u01e0\u01e1\b")
        buf.write("G\5\2\u01e1\u008e\3\2\2\2\u01e2\u01e4\t\n\2\2\u01e3\u01e2")
        buf.write("\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e5")
        buf.write("\u01e6\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01e8\bH\5\2")
        buf.write("\u01e8\u0090\3\2\2\2\u01e9\u01ed\7$\2\2\u01ea\u01ec\5")
        buf.write("!\21\2\u01eb\u01ea\3\2\2\2\u01ec\u01ef\3\2\2\2\u01ed\u01eb")
        buf.write("\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u0092\3\2\2\2\u01ef")
        buf.write("\u01ed\3\2\2\2\u01f0\u01f1\7\61\2\2\u01f1\u01f2\7,\2\2")
        buf.write("\u01f2\u01f6\3\2\2\2\u01f3\u01f5\5!\21\2\u01f4\u01f3\3")
        buf.write("\2\2\2\u01f5\u01f8\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f6\u01f7")
        buf.write("\3\2\2\2\u01f7\u0094\3\2\2\2\u01f8\u01f6\3\2\2\2\u01f9")
        buf.write("\u01fa\5\u0091I\2\u01fa\u01fb\bK\6\2\u01fb\u0096\3\2\2")
        buf.write("\2\u01fc\u01fd\13\2\2\2\u01fd\u01fe\bL\7\2\u01fe\u0098")
        buf.write("\3\2\2\2\u01ff\u0200\13\2\2\2\u0200\u0201\bM\b\2\u0201")
        buf.write("\u009a\3\2\2\2\u0202\u0203\5\u0093J\2\u0203\u0204\bN\t")
        buf.write("\2\u0204\u009c\3\2\2\2\25\2\u00af\u00b1\u00b7\u00bc\u00c6")
        buf.write("\u00cc\u00d1\u00d6\u00de\u00e4\u00ec\u00fe\u01c6\u01cf")
        buf.write("\u01dd\u01e5\u01ed\u01f6\n\3\t\2\3\n\3\3\20\4\b\2\2\3")
        buf.write("K\5\3L\6\3M\7\3N\b")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    StringType = 1
    IntegerType = 2
    FloatType = 3
    BooleanType = 4
    ArrayType = 5
    VoidType = 6
    AutoType = 7
    INTLIT = 8
    FLOATLIT = 9
    BOOLLIT = 10
    STRINGLIT = 11
    LP = 12
    RP = 13
    LSB = 14
    RSB = 15
    DOT = 16
    CM = 17
    SM = 18
    COLON = 19
    LCB = 20
    RCB = 21
    ASSIGN = 22
    ADD = 23
    SUB = 24
    MUL = 25
    DIV = 26
    MOD = 27
    NOT = 28
    LG_AND = 29
    LG_OR = 30
    EQ = 31
    INEQ = 32
    LT = 33
    GT = 34
    LE = 35
    GE = 36
    SRO = 37
    MAIN = 38
    AUTO = 39
    BREAK = 40
    BOOLEAN = 41
    DO = 42
    ELSE = 43
    FALSE = 44
    FLOAT = 45
    FOR = 46
    FUNCTION = 47
    IF = 48
    INTEGER = 49
    INT = 50
    RETURN = 51
    STRING = 52
    TRUE = 53
    WHILE = 54
    VOID = 55
    IN = 56
    OUT = 57
    CONTINUE = 58
    OF = 59
    INHERIT = 60
    ARRAY = 61
    ID = 62
    BlockComment = 63
    LineComment = 64
    WS = 65
    UNCLOSE_STRING = 66
    ERROR_CHAR = 67
    ILLEGAL_ESCAPE = 68
    UNTERMINATED_COMMENT = 69

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'['", "']'", "'.'", "','", "';'", "':'", "'{'", 
            "'}'", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'::'", 
            "'main'", "'auto'", "'break'", "'boolean'", "'do'", "'else'", 
            "'false'", "'float'", "'for'", "'function'", "'if'", "'integer'", 
            "'int'", "'return'", "'string'", "'true'", "'while'", "'void'", 
            "'in'", "'out'", "'continue'", "'of'", "'inherit'", "'array'" ]

    symbolicNames = [ "<INVALID>",
            "StringType", "IntegerType", "FloatType", "BooleanType", "ArrayType", 
            "VoidType", "AutoType", "INTLIT", "FLOATLIT", "BOOLLIT", "STRINGLIT", 
            "LP", "RP", "LSB", "RSB", "DOT", "CM", "SM", "COLON", "LCB", 
            "RCB", "ASSIGN", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "LG_AND", 
            "LG_OR", "EQ", "INEQ", "LT", "GT", "LE", "GE", "SRO", "MAIN", 
            "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
            "FOR", "FUNCTION", "IF", "INTEGER", "INT", "RETURN", "STRING", 
            "TRUE", "WHILE", "VOID", "IN", "OUT", "CONTINUE", "OF", "INHERIT", 
            "ARRAY", "ID", "BlockComment", "LineComment", "WS", "UNCLOSE_STRING", 
            "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "StringType", "IntegerType", "FloatType", "BooleanType", 
                  "ArrayType", "VoidType", "AutoType", "INTLIT", "FLOATLIT", 
                  "DecimalPart", "ExponentPart", "Digit", "NonZeroDigit", 
                  "BOOLLIT", "STRINGLIT", "Schar", "EscapeSequence", "LP", 
                  "RP", "LSB", "RSB", "DOT", "CM", "SM", "COLON", "LCB", 
                  "RCB", "ASSIGN", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", 
                  "LG_AND", "LG_OR", "EQ", "INEQ", "LT", "GT", "LE", "GE", 
                  "SRO", "MAIN", "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", 
                  "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", 
                  "INT", "RETURN", "STRING", "TRUE", "WHILE", "VOID", "IN", 
                  "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "ID", "BlockComment", 
                  "LineComment", "WS", "UncloseString", "UnterminatedCommentString", 
                  "UNCLOSE_STRING", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

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
            actions[7] = self.INTLIT_action 
            actions[8] = self.FLOATLIT_action 
            actions[14] = self.STRINGLIT_action 
            actions[73] = self.UNCLOSE_STRING_action 
            actions[74] = self.ERROR_CHAR_action 
            actions[75] = self.ILLEGAL_ESCAPE_action 
            actions[76] = self.UNTERMINATED_COMMENT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_', '')
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_', '')
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise UncloseString(self.text[1:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise IllegalEscape(self.text)
     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            raise UnterminatedComment(self.text)
     


