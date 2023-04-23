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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u01f2\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\3\2\3\2\5\2\u0092\n\2\3\3\3")
        buf.write("\3\5\3\u0096\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\5\4\u00a4\n\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u00ac")
        buf.write("\n\4\3\4\3\4\3\5\3\5\3\5\5\5\u00b3\n\5\3\5\7\5\u00b6\n")
        buf.write("\5\f\5\16\5\u00b9\13\5\3\5\5\5\u00bc\n\5\3\6\3\6\7\6\u00c0")
        buf.write("\n\6\f\6\16\6\u00c3\13\6\3\6\3\6\3\6\3\7\3\7\5\7\u00ca")
        buf.write("\n\7\3\7\6\7\u00cd\n\7\r\7\16\7\u00ce\3\b\3\b\3\t\3\t")
        buf.write("\6\t\u00d5\n\t\r\t\16\t\u00d6\3\n\3\n\5\n\u00db\n\n\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\r\3\r\3\r\5\r\u00e5\n\r\3\16\3")
        buf.write("\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23")
        buf.write("\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\30")
        buf.write("\5\30\u00fe\n\30\3\31\3\31\5\31\u0102\n\31\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\32\5\32\u010a\n\32\3\33\3\33\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"")
        buf.write("\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3")
        buf.write("(\3)\3)\3)\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3,\3,\3")
        buf.write(",\3,\3,\3,\3,\3-\3-\3-\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\3")
        buf.write("/\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3")
        buf.write("\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65")
        buf.write("\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\38\38\38\38\38\39\39\39\39\3")
        buf.write("9\39\3:\3:\3:\3:\3:\3;\3;\3;\3<\3<\3<\3<\3=\3=\3=\3=\3")
        buf.write("=\3=\3=\3=\3=\3>\3>\3>\3?\3?\3?\3?\3?\3?\3?\3?\3@\3@\3")
        buf.write("@\3@\3@\3@\3A\3A\3A\3A\7A\u01b7\nA\fA\16A\u01ba\13A\3")
        buf.write("A\3A\3B\3B\3B\3B\7B\u01c2\nB\fB\16B\u01c5\13B\3B\3B\3")
        buf.write("B\3B\3B\3C\3C\7C\u01ce\nC\fC\16C\u01d1\13C\3D\6D\u01d4")
        buf.write("\nD\rD\16D\u01d5\3D\3D\3E\3E\7E\u01dc\nE\fE\16E\u01df")
        buf.write("\13E\3E\5E\u01e2\nE\3E\3E\3F\3F\7F\u01e8\nF\fF\16F\u01eb")
        buf.write("\13F\3F\3F\3F\3G\3G\3G\3\u01c3\2H\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\2\17\2\21\2\23\2\25\2\27\2\31\2\33\b\35\t\37\n!\13")
        buf.write("#\f%\r\'\16)\17+\20-\21/\22\61\23\63\24\65\25\67\269\27")
        buf.write(";\30=\31?\32A\33C\34E\35G\36I\37K M!O\"Q#S$U%W&Y\'[(]")
        buf.write(")_*a+c,e-g.i/k\60m\61o\62q\63s\64u\65w\66y\67{8}9\177")
        buf.write(":\u0081;\u0083<\u0085=\u0087>\u0089?\u008b@\u008dA\3\2")
        buf.write("\r\3\2\63;\3\2\62;\4\2GGgg\4\2--//\6\2\n\f\16\17$$^^\t")
        buf.write("\2$$^^ddhhppttvv\4\2\f\f\17\17\5\2C\\aac|\6\2\62;C\\a")
        buf.write("ac|\5\2\13\f\17\17\"\"\6\3\n\f\16\17$$^^\2\u0209\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2")
        buf.write("\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\3\u0091")
        buf.write("\3\2\2\2\5\u0095\3\2\2\2\7\u00ab\3\2\2\2\t\u00bb\3\2\2")
        buf.write("\2\13\u00bd\3\2\2\2\r\u00c7\3\2\2\2\17\u00d0\3\2\2\2\21")
        buf.write("\u00d2\3\2\2\2\23\u00da\3\2\2\2\25\u00dc\3\2\2\2\27\u00df")
        buf.write("\3\2\2\2\31\u00e4\3\2\2\2\33\u00e6\3\2\2\2\35\u00e8\3")
        buf.write("\2\2\2\37\u00ea\3\2\2\2!\u00ec\3\2\2\2#\u00ee\3\2\2\2")
        buf.write("%\u00f0\3\2\2\2\'\u00f2\3\2\2\2)\u00f4\3\2\2\2+\u00f6")
        buf.write("\3\2\2\2-\u00f8\3\2\2\2/\u00fd\3\2\2\2\61\u0101\3\2\2")
        buf.write("\2\63\u0109\3\2\2\2\65\u010b\3\2\2\2\67\u010d\3\2\2\2")
        buf.write("9\u010f\3\2\2\2;\u0111\3\2\2\2=\u0113\3\2\2\2?\u0115\3")
        buf.write("\2\2\2A\u0117\3\2\2\2C\u011a\3\2\2\2E\u011d\3\2\2\2G\u0120")
        buf.write("\3\2\2\2I\u0123\3\2\2\2K\u0125\3\2\2\2M\u0127\3\2\2\2")
        buf.write("O\u012a\3\2\2\2Q\u012d\3\2\2\2S\u0130\3\2\2\2U\u0135\3")
        buf.write("\2\2\2W\u013b\3\2\2\2Y\u0143\3\2\2\2[\u0146\3\2\2\2]\u014b")
        buf.write("\3\2\2\2_\u0151\3\2\2\2a\u0157\3\2\2\2c\u015b\3\2\2\2")
        buf.write("e\u0164\3\2\2\2g\u0167\3\2\2\2i\u016f\3\2\2\2k\u0173\3")
        buf.write("\2\2\2m\u017a\3\2\2\2o\u0181\3\2\2\2q\u0186\3\2\2\2s\u018c")
        buf.write("\3\2\2\2u\u0191\3\2\2\2w\u0194\3\2\2\2y\u0198\3\2\2\2")
        buf.write("{\u01a1\3\2\2\2}\u01a4\3\2\2\2\177\u01ac\3\2\2\2\u0081")
        buf.write("\u01b2\3\2\2\2\u0083\u01bd\3\2\2\2\u0085\u01cb\3\2\2\2")
        buf.write("\u0087\u01d3\3\2\2\2\u0089\u01d9\3\2\2\2\u008b\u01e5\3")
        buf.write("\2\2\2\u008d\u01ef\3\2\2\2\u008f\u0092\5}?\2\u0090\u0092")
        buf.write("\5w<\2\u0091\u008f\3\2\2\2\u0091\u0090\3\2\2\2\u0092\4")
        buf.write("\3\2\2\2\u0093\u0096\5o8\2\u0094\u0096\5]/\2\u0095\u0093")
        buf.write("\3\2\2\2\u0095\u0094\3\2\2\2\u0096\6\3\2\2\2\u0097\u0098")
        buf.write("\5\t\5\2\u0098\u0099\5\21\t\2\u0099\u00ac\3\2\2\2\u009a")
        buf.write("\u009b\5\t\5\2\u009b\u009c\5\21\t\2\u009c\u009d\5\r\7")
        buf.write("\2\u009d\u00ac\3\2\2\2\u009e\u009f\5\t\5\2\u009f\u00a0")
        buf.write("\5\r\7\2\u00a0\u00ac\3\2\2\2\u00a1\u00a3\5\21\t\2\u00a2")
        buf.write("\u00a4\5\r\7\2\u00a3\u00a2\3\2\2\2\u00a3\u00a4\3\2\2\2")
        buf.write("\u00a4\u00ac\3\2\2\2\u00a5\u00a6\5\t\5\2\u00a6\u00a7\5")
        buf.write("\17\b\2\u00a7\u00ac\3\2\2\2\u00a8\u00a9\5\17\b\2\u00a9")
        buf.write("\u00aa\5\r\7\2\u00aa\u00ac\3\2\2\2\u00ab\u0097\3\2\2\2")
        buf.write("\u00ab\u009a\3\2\2\2\u00ab\u009e\3\2\2\2\u00ab\u00a1\3")
        buf.write("\2\2\2\u00ab\u00a5\3\2\2\2\u00ab\u00a8\3\2\2\2\u00ac\u00ad")
        buf.write("\3\2\2\2\u00ad\u00ae\b\4\2\2\u00ae\b\3\2\2\2\u00af\u00bc")
        buf.write("\7\62\2\2\u00b0\u00b7\t\2\2\2\u00b1\u00b3\7a\2\2\u00b2")
        buf.write("\u00b1\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b4\3\2\2\2")
        buf.write("\u00b4\u00b6\t\3\2\2\u00b5\u00b2\3\2\2\2\u00b6\u00b9\3")
        buf.write("\2\2\2\u00b7\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00ba")
        buf.write("\3\2\2\2\u00b9\u00b7\3\2\2\2\u00ba\u00bc\b\5\3\2\u00bb")
        buf.write("\u00af\3\2\2\2\u00bb\u00b0\3\2\2\2\u00bc\n\3\2\2\2\u00bd")
        buf.write("\u00c1\5\27\f\2\u00be\u00c0\5\23\n\2\u00bf\u00be\3\2\2")
        buf.write("\2\u00c0\u00c3\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2")
        buf.write("\3\2\2\2\u00c2\u00c4\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c4")
        buf.write("\u00c5\5\27\f\2\u00c5\u00c6\b\6\4\2\u00c6\f\3\2\2\2\u00c7")
        buf.write("\u00c9\t\4\2\2\u00c8\u00ca\t\5\2\2\u00c9\u00c8\3\2\2\2")
        buf.write("\u00c9\u00ca\3\2\2\2\u00ca\u00cc\3\2\2\2\u00cb\u00cd\t")
        buf.write("\3\2\2\u00cc\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00cc")
        buf.write("\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\16\3\2\2\2\u00d0\u00d1")
        buf.write("\7\60\2\2\u00d1\20\3\2\2\2\u00d2\u00d4\5\17\b\2\u00d3")
        buf.write("\u00d5\t\3\2\2\u00d4\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2")
        buf.write("\u00d6\u00d4\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\22\3\2")
        buf.write("\2\2\u00d8\u00db\n\6\2\2\u00d9\u00db\5\25\13\2\u00da\u00d8")
        buf.write("\3\2\2\2\u00da\u00d9\3\2\2\2\u00db\24\3\2\2\2\u00dc\u00dd")
        buf.write("\7^\2\2\u00dd\u00de\t\7\2\2\u00de\26\3\2\2\2\u00df\u00e0")
        buf.write("\7$\2\2\u00e0\30\3\2\2\2\u00e1\u00e2\7^\2\2\u00e2\u00e5")
        buf.write("\n\7\2\2\u00e3\u00e5\7^\2\2\u00e4\u00e1\3\2\2\2\u00e4")
        buf.write("\u00e3\3\2\2\2\u00e5\32\3\2\2\2\u00e6\u00e7\7*\2\2\u00e7")
        buf.write("\34\3\2\2\2\u00e8\u00e9\7+\2\2\u00e9\36\3\2\2\2\u00ea")
        buf.write("\u00eb\7]\2\2\u00eb \3\2\2\2\u00ec\u00ed\7_\2\2\u00ed")
        buf.write("\"\3\2\2\2\u00ee\u00ef\7.\2\2\u00ef$\3\2\2\2\u00f0\u00f1")
        buf.write("\7=\2\2\u00f1&\3\2\2\2\u00f2\u00f3\7<\2\2\u00f3(\3\2\2")
        buf.write("\2\u00f4\u00f5\7}\2\2\u00f5*\3\2\2\2\u00f6\u00f7\7\177")
        buf.write("\2\2\u00f7,\3\2\2\2\u00f8\u00f9\7?\2\2\u00f9.\3\2\2\2")
        buf.write("\u00fa\u00fe\5=\37\2\u00fb\u00fe\59\35\2\u00fc\u00fe\5")
        buf.write(";\36\2\u00fd\u00fa\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fd\u00fc")
        buf.write("\3\2\2\2\u00fe\60\3\2\2\2\u00ff\u0102\5A!\2\u0100\u0102")
        buf.write("\5C\"\2\u0101\u00ff\3\2\2\2\u0101\u0100\3\2\2\2\u0102")
        buf.write("\62\3\2\2\2\u0103\u010a\5E#\2\u0104\u010a\5G$\2\u0105")
        buf.write("\u010a\5K&\2\u0106\u010a\5O(\2\u0107\u010a\5I%\2\u0108")
        buf.write("\u010a\5M\'\2\u0109\u0103\3\2\2\2\u0109\u0104\3\2\2\2")
        buf.write("\u0109\u0105\3\2\2\2\u0109\u0106\3\2\2\2\u0109\u0107\3")
        buf.write("\2\2\2\u0109\u0108\3\2\2\2\u010a\64\3\2\2\2\u010b\u010c")
        buf.write("\7-\2\2\u010c\66\3\2\2\2\u010d\u010e\7/\2\2\u010e8\3\2")
        buf.write("\2\2\u010f\u0110\7,\2\2\u0110:\3\2\2\2\u0111\u0112\7\61")
        buf.write("\2\2\u0112<\3\2\2\2\u0113\u0114\7\'\2\2\u0114>\3\2\2\2")
        buf.write("\u0115\u0116\7#\2\2\u0116@\3\2\2\2\u0117\u0118\7(\2\2")
        buf.write("\u0118\u0119\7(\2\2\u0119B\3\2\2\2\u011a\u011b\7~\2\2")
        buf.write("\u011b\u011c\7~\2\2\u011cD\3\2\2\2\u011d\u011e\7?\2\2")
        buf.write("\u011e\u011f\7?\2\2\u011fF\3\2\2\2\u0120\u0121\7#\2\2")
        buf.write("\u0121\u0122\7?\2\2\u0122H\3\2\2\2\u0123\u0124\7>\2\2")
        buf.write("\u0124J\3\2\2\2\u0125\u0126\7@\2\2\u0126L\3\2\2\2\u0127")
        buf.write("\u0128\7>\2\2\u0128\u0129\7?\2\2\u0129N\3\2\2\2\u012a")
        buf.write("\u012b\7@\2\2\u012b\u012c\7?\2\2\u012cP\3\2\2\2\u012d")
        buf.write("\u012e\7<\2\2\u012e\u012f\7<\2\2\u012fR\3\2\2\2\u0130")
        buf.write("\u0131\7c\2\2\u0131\u0132\7w\2\2\u0132\u0133\7v\2\2\u0133")
        buf.write("\u0134\7q\2\2\u0134T\3\2\2\2\u0135\u0136\7d\2\2\u0136")
        buf.write("\u0137\7t\2\2\u0137\u0138\7g\2\2\u0138\u0139\7c\2\2\u0139")
        buf.write("\u013a\7m\2\2\u013aV\3\2\2\2\u013b\u013c\7d\2\2\u013c")
        buf.write("\u013d\7q\2\2\u013d\u013e\7q\2\2\u013e\u013f\7n\2\2\u013f")
        buf.write("\u0140\7g\2\2\u0140\u0141\7c\2\2\u0141\u0142\7p\2\2\u0142")
        buf.write("X\3\2\2\2\u0143\u0144\7f\2\2\u0144\u0145\7q\2\2\u0145")
        buf.write("Z\3\2\2\2\u0146\u0147\7g\2\2\u0147\u0148\7n\2\2\u0148")
        buf.write("\u0149\7u\2\2\u0149\u014a\7g\2\2\u014a\\\3\2\2\2\u014b")
        buf.write("\u014c\7h\2\2\u014c\u014d\7c\2\2\u014d\u014e\7n\2\2\u014e")
        buf.write("\u014f\7u\2\2\u014f\u0150\7g\2\2\u0150^\3\2\2\2\u0151")
        buf.write("\u0152\7h\2\2\u0152\u0153\7n\2\2\u0153\u0154\7q\2\2\u0154")
        buf.write("\u0155\7c\2\2\u0155\u0156\7v\2\2\u0156`\3\2\2\2\u0157")
        buf.write("\u0158\7h\2\2\u0158\u0159\7q\2\2\u0159\u015a\7t\2\2\u015a")
        buf.write("b\3\2\2\2\u015b\u015c\7h\2\2\u015c\u015d\7w\2\2\u015d")
        buf.write("\u015e\7p\2\2\u015e\u015f\7e\2\2\u015f\u0160\7v\2\2\u0160")
        buf.write("\u0161\7k\2\2\u0161\u0162\7q\2\2\u0162\u0163\7p\2\2\u0163")
        buf.write("d\3\2\2\2\u0164\u0165\7k\2\2\u0165\u0166\7h\2\2\u0166")
        buf.write("f\3\2\2\2\u0167\u0168\7k\2\2\u0168\u0169\7p\2\2\u0169")
        buf.write("\u016a\7v\2\2\u016a\u016b\7g\2\2\u016b\u016c\7i\2\2\u016c")
        buf.write("\u016d\7g\2\2\u016d\u016e\7t\2\2\u016eh\3\2\2\2\u016f")
        buf.write("\u0170\7k\2\2\u0170\u0171\7p\2\2\u0171\u0172\7v\2\2\u0172")
        buf.write("j\3\2\2\2\u0173\u0174\7t\2\2\u0174\u0175\7g\2\2\u0175")
        buf.write("\u0176\7v\2\2\u0176\u0177\7w\2\2\u0177\u0178\7t\2\2\u0178")
        buf.write("\u0179\7p\2\2\u0179l\3\2\2\2\u017a\u017b\7u\2\2\u017b")
        buf.write("\u017c\7v\2\2\u017c\u017d\7t\2\2\u017d\u017e\7k\2\2\u017e")
        buf.write("\u017f\7p\2\2\u017f\u0180\7i\2\2\u0180n\3\2\2\2\u0181")
        buf.write("\u0182\7v\2\2\u0182\u0183\7t\2\2\u0183\u0184\7w\2\2\u0184")
        buf.write("\u0185\7g\2\2\u0185p\3\2\2\2\u0186\u0187\7y\2\2\u0187")
        buf.write("\u0188\7j\2\2\u0188\u0189\7k\2\2\u0189\u018a\7n\2\2\u018a")
        buf.write("\u018b\7g\2\2\u018br\3\2\2\2\u018c\u018d\7x\2\2\u018d")
        buf.write("\u018e\7q\2\2\u018e\u018f\7k\2\2\u018f\u0190\7f\2\2\u0190")
        buf.write("t\3\2\2\2\u0191\u0192\7k\2\2\u0192\u0193\7p\2\2\u0193")
        buf.write("v\3\2\2\2\u0194\u0195\7q\2\2\u0195\u0196\7w\2\2\u0196")
        buf.write("\u0197\7v\2\2\u0197x\3\2\2\2\u0198\u0199\7e\2\2\u0199")
        buf.write("\u019a\7q\2\2\u019a\u019b\7p\2\2\u019b\u019c\7v\2\2\u019c")
        buf.write("\u019d\7k\2\2\u019d\u019e\7p\2\2\u019e\u019f\7w\2\2\u019f")
        buf.write("\u01a0\7g\2\2\u01a0z\3\2\2\2\u01a1\u01a2\7q\2\2\u01a2")
        buf.write("\u01a3\7h\2\2\u01a3|\3\2\2\2\u01a4\u01a5\7k\2\2\u01a5")
        buf.write("\u01a6\7p\2\2\u01a6\u01a7\7j\2\2\u01a7\u01a8\7g\2\2\u01a8")
        buf.write("\u01a9\7t\2\2\u01a9\u01aa\7k\2\2\u01aa\u01ab\7v\2\2\u01ab")
        buf.write("~\3\2\2\2\u01ac\u01ad\7c\2\2\u01ad\u01ae\7t\2\2\u01ae")
        buf.write("\u01af\7t\2\2\u01af\u01b0\7c\2\2\u01b0\u01b1\7{\2\2\u01b1")
        buf.write("\u0080\3\2\2\2\u01b2\u01b3\7\61\2\2\u01b3\u01b4\7\61\2")
        buf.write("\2\u01b4\u01b8\3\2\2\2\u01b5\u01b7\n\b\2\2\u01b6\u01b5")
        buf.write("\3\2\2\2\u01b7\u01ba\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b8")
        buf.write("\u01b9\3\2\2\2\u01b9\u01bb\3\2\2\2\u01ba\u01b8\3\2\2\2")
        buf.write("\u01bb\u01bc\bA\5\2\u01bc\u0082\3\2\2\2\u01bd\u01be\7")
        buf.write("\61\2\2\u01be\u01bf\7,\2\2\u01bf\u01c3\3\2\2\2\u01c0\u01c2")
        buf.write("\13\2\2\2\u01c1\u01c0\3\2\2\2\u01c2\u01c5\3\2\2\2\u01c3")
        buf.write("\u01c4\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c4\u01c6\3\2\2\2")
        buf.write("\u01c5\u01c3\3\2\2\2\u01c6\u01c7\7,\2\2\u01c7\u01c8\7")
        buf.write("\61\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01ca\bB\5\2\u01ca\u0084")
        buf.write("\3\2\2\2\u01cb\u01cf\t\t\2\2\u01cc\u01ce\t\n\2\2\u01cd")
        buf.write("\u01cc\3\2\2\2\u01ce\u01d1\3\2\2\2\u01cf\u01cd\3\2\2\2")
        buf.write("\u01cf\u01d0\3\2\2\2\u01d0\u0086\3\2\2\2\u01d1\u01cf\3")
        buf.write("\2\2\2\u01d2\u01d4\t\13\2\2\u01d3\u01d2\3\2\2\2\u01d4")
        buf.write("\u01d5\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d5\u01d6\3\2\2\2")
        buf.write("\u01d6\u01d7\3\2\2\2\u01d7\u01d8\bD\5\2\u01d8\u0088\3")
        buf.write("\2\2\2\u01d9\u01dd\5\27\f\2\u01da\u01dc\5\23\n\2\u01db")
        buf.write("\u01da\3\2\2\2\u01dc\u01df\3\2\2\2\u01dd\u01db\3\2\2\2")
        buf.write("\u01dd\u01de\3\2\2\2\u01de\u01e1\3\2\2\2\u01df\u01dd\3")
        buf.write("\2\2\2\u01e0\u01e2\t\f\2\2\u01e1\u01e0\3\2\2\2\u01e2\u01e3")
        buf.write("\3\2\2\2\u01e3\u01e4\bE\6\2\u01e4\u008a\3\2\2\2\u01e5")
        buf.write("\u01e9\5\27\f\2\u01e6\u01e8\5\23\n\2\u01e7\u01e6\3\2\2")
        buf.write("\2\u01e8\u01eb\3\2\2\2\u01e9\u01e7\3\2\2\2\u01e9\u01ea")
        buf.write("\3\2\2\2\u01ea\u01ec\3\2\2\2\u01eb\u01e9\3\2\2\2\u01ec")
        buf.write("\u01ed\5\31\r\2\u01ed\u01ee\bF\7\2\u01ee\u008c\3\2\2\2")
        buf.write("\u01ef\u01f0\13\2\2\2\u01f0\u01f1\bG\b\2\u01f1\u008e\3")
        buf.write("\2\2\2\32\2\u0091\u0095\u00a3\u00ab\u00b2\u00b7\u00bb")
        buf.write("\u00c1\u00c9\u00ce\u00d6\u00da\u00e4\u00fd\u0101\u0109")
        buf.write("\u01b8\u01c3\u01cf\u01d5\u01dd\u01e1\u01e9\t\3\4\2\3\5")
        buf.write("\3\3\6\4\b\2\2\3E\5\3F\6\3G\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PARAM_KEYWORDS = 1
    BOOLLIT = 2
    FLOATLIT = 3
    INTLIT = 4
    STRINGLIT = 5
    LP = 6
    RP = 7
    LSB = 8
    RSB = 9
    CM = 10
    SM = 11
    COLON = 12
    LCB = 13
    RCB = 14
    ASSIGN = 15
    MOD_MUL_DIV = 16
    AND_OR = 17
    COMPARE = 18
    ADD = 19
    SUB = 20
    MUL = 21
    DIV = 22
    MOD = 23
    NOT = 24
    LG_AND = 25
    LG_OR = 26
    EQ = 27
    INEQ = 28
    LT = 29
    GT = 30
    LE = 31
    GE = 32
    SRO = 33
    AUTO = 34
    BREAK = 35
    BOOLEAN = 36
    DO = 37
    ELSE = 38
    FALSE = 39
    FLOAT = 40
    FOR = 41
    FUNCTION = 42
    IF = 43
    INTEGER = 44
    INT = 45
    RETURN = 46
    STRING = 47
    TRUE = 48
    WHILE = 49
    VOID = 50
    IN = 51
    OUT = 52
    CONTINUE = 53
    OF = 54
    INHERIT = 55
    ARRAY = 56
    COMMENT = 57
    C_COMMENT = 58
    ID = 59
    WS = 60
    UNCLOSE_STRING = 61
    ILLEGAL_ESCAPE = 62
    ERROR_CHAR = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'['", "']'", "','", "';'", "':'", "'{'", "'}'", 
            "'='", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
            "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'::'", "'auto'", 
            "'break'", "'boolean'", "'do'", "'else'", "'false'", "'float'", 
            "'for'", "'function'", "'if'", "'integer'", "'int'", "'return'", 
            "'string'", "'true'", "'while'", "'void'", "'in'", "'out'", 
            "'continue'", "'of'", "'inherit'", "'array'" ]

    symbolicNames = [ "<INVALID>",
            "PARAM_KEYWORDS", "BOOLLIT", "FLOATLIT", "INTLIT", "STRINGLIT", 
            "LP", "RP", "LSB", "RSB", "CM", "SM", "COLON", "LCB", "RCB", 
            "ASSIGN", "MOD_MUL_DIV", "AND_OR", "COMPARE", "ADD", "SUB", 
            "MUL", "DIV", "MOD", "NOT", "LG_AND", "LG_OR", "EQ", "INEQ", 
            "LT", "GT", "LE", "GE", "SRO", "AUTO", "BREAK", "BOOLEAN", "DO", 
            "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", 
            "INT", "RETURN", "STRING", "TRUE", "WHILE", "VOID", "IN", "OUT", 
            "CONTINUE", "OF", "INHERIT", "ARRAY", "COMMENT", "C_COMMENT", 
            "ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "PARAM_KEYWORDS", "BOOLLIT", "FLOATLIT", "INTLIT", "STRINGLIT", 
                  "EXPPART", "DOT", "DECPART", "StringChar", "ESC2", "DOUBLEQ", 
                  "IllegalString", "LP", "RP", "LSB", "RSB", "CM", "SM", 
                  "COLON", "LCB", "RCB", "ASSIGN", "MOD_MUL_DIV", "AND_OR", 
                  "COMPARE", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "LG_AND", 
                  "LG_OR", "EQ", "INEQ", "LT", "GT", "LE", "GE", "SRO", 
                  "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
                  "FOR", "FUNCTION", "IF", "INTEGER", "INT", "RETURN", "STRING", 
                  "TRUE", "WHILE", "VOID", "IN", "OUT", "CONTINUE", "OF", 
                  "INHERIT", "ARRAY", "COMMENT", "C_COMMENT", "ID", "WS", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
            actions[2] = self.FLOATLIT_action 
            actions[3] = self.INTLIT_action 
            actions[4] = self.STRINGLIT_action 
            actions[67] = self.UNCLOSE_STRING_action 
            actions[68] = self.ILLEGAL_ESCAPE_action 
            actions[69] = self.ERROR_CHAR_action 
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
                
     


