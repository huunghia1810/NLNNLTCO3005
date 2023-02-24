# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\u019c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\3")
        buf.write("\2\3\2\3\2\7\2`\n\2\f\2\16\2c\13\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\7\4r\n\4\f\4\16\4u\13")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\5\6\u0087\n\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\5\b\u0090\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u0099\n")
        buf.write("\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\5\17\u00bd\n")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\7\21\u00c7")
        buf.write("\n\21\f\21\16\21\u00ca\13\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22")
        buf.write("\u00db\n\22\3\23\3\23\3\23\7\23\u00e0\n\23\f\23\16\23")
        buf.write("\u00e3\13\23\3\24\3\24\5\24\u00e7\n\24\3\25\3\25\3\25")
        buf.write("\7\25\u00ec\n\25\f\25\16\25\u00ef\13\25\3\26\5\26\u00f2")
        buf.write("\n\26\3\26\5\26\u00f5\n\26\3\26\3\26\3\26\3\26\3\27\3")
        buf.write("\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\5\30\u0107\n\30\3\31\3\31\3\31\5\31\u010c\n\31\3\32\3")
        buf.write("\32\3\32\7\32\u0111\n\32\f\32\16\32\u0114\13\32\3\32\3")
        buf.write("\32\3\33\3\33\3\33\7\33\u011b\n\33\f\33\16\33\u011e\13")
        buf.write("\33\3\33\3\33\3\34\3\34\3\34\7\34\u0125\n\34\f\34\16\34")
        buf.write("\u0128\13\34\3\35\3\35\3\35\5\35\u012d\n\35\3\36\3\36")
        buf.write("\3\36\3\36\5\36\u0133\n\36\3\37\3\37\3 \3 \3 \3 \3 \3")
        buf.write(" \3 \7 \u013e\n \f \16 \u0141\13 \3!\3!\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\7\"\u014c\n\"\f\"\16\"\u014f\13\"\3#\3")
        buf.write("#\3$\3$\3$\3$\3$\3$\3$\7$\u015a\n$\f$\16$\u015d\13$\3")
        buf.write("%\3%\3&\3&\3&\5&\u0164\n&\3&\5&\u0167\n&\3\'\3\'\3(\3")
        buf.write("(\3(\5(\u016e\n(\3(\5(\u0171\n(\3)\3)\3*\3*\3*\3*\3*\3")
        buf.write("*\3*\3*\3*\3*\3*\3*\5*\u0181\n*\3+\3+\3+\7+\u0186\n+\f")
        buf.write("+\16+\u0189\13+\3,\3,\3,\3,\3,\3,\3,\3-\3-\3-\7-\u0195")
        buf.write("\n-\f-\16-\u0198\13-\3.\3.\3.\2\5>BF/\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJL")
        buf.write("NPRTVXZ\2\7\3\2!&\3\2\37 \3\2\31\32\3\2\33\35\3\2\3\6")
        buf.write("\2\u01a0\2a\3\2\2\2\4f\3\2\2\2\6n\3\2\2\2\bx\3\2\2\2\n")
        buf.write("\u0086\3\2\2\2\f\u0088\3\2\2\2\16\u008f\3\2\2\2\20\u0091")
        buf.write("\3\2\2\2\22\u009a\3\2\2\2\24\u00a6\3\2\2\2\26\u00ac\3")
        buf.write("\2\2\2\30\u00b4\3\2\2\2\32\u00b7\3\2\2\2\34\u00ba\3\2")
        buf.write("\2\2\36\u00c0\3\2\2\2 \u00c3\3\2\2\2\"\u00da\3\2\2\2$")
        buf.write("\u00dc\3\2\2\2&\u00e6\3\2\2\2(\u00e8\3\2\2\2*\u00f1\3")
        buf.write("\2\2\2,\u00fa\3\2\2\2.\u00fd\3\2\2\2\60\u010b\3\2\2\2")
        buf.write("\62\u010d\3\2\2\2\64\u0117\3\2\2\2\66\u0121\3\2\2\28\u0129")
        buf.write("\3\2\2\2:\u012e\3\2\2\2<\u0134\3\2\2\2>\u0136\3\2\2\2")
        buf.write("@\u0142\3\2\2\2B\u0144\3\2\2\2D\u0150\3\2\2\2F\u0152\3")
        buf.write("\2\2\2H\u015e\3\2\2\2J\u0166\3\2\2\2L\u0168\3\2\2\2N\u0170")
        buf.write("\3\2\2\2P\u0172\3\2\2\2R\u0180\3\2\2\2T\u0182\3\2\2\2")
        buf.write("V\u018a\3\2\2\2X\u0191\3\2\2\2Z\u0199\3\2\2\2\\`\5\"\22")
        buf.write("\2]`\5,\27\2^`\5\4\3\2_\\\3\2\2\2_]\3\2\2\2_^\3\2\2\2")
        buf.write("`c\3\2\2\2a_\3\2\2\2ab\3\2\2\2bd\3\2\2\2ca\3\2\2\2de\7")
        buf.write("\2\2\3e\3\3\2\2\2fg\7=\2\2gh\7\25\2\2hi\7\60\2\2ij\7\b")
        buf.write("\2\2jk\7\16\2\2kl\7\17\2\2lm\5\6\4\2m\5\3\2\2\2ns\7\26")
        buf.write("\2\2or\5\n\6\2pr\5\"\22\2qo\3\2\2\2qp\3\2\2\2ru\3\2\2")
        buf.write("\2sq\3\2\2\2st\3\2\2\2tv\3\2\2\2us\3\2\2\2vw\7\27\2\2")
        buf.write("w\7\3\2\2\2xy\7\26\2\2yz\5T+\2z{\7\27\2\2{\t\3\2\2\2|")
        buf.write("\u0087\5\f\7\2}\u0087\5\20\t\2~\u0087\5\22\n\2\177\u0087")
        buf.write("\5\24\13\2\u0080\u0087\5\26\f\2\u0081\u0087\5\30\r\2\u0082")
        buf.write("\u0087\5\32\16\2\u0083\u0087\5\34\17\2\u0084\u0087\5\36")
        buf.write("\20\2\u0085\u0087\5 \21\2\u0086|\3\2\2\2\u0086}\3\2\2")
        buf.write("\2\u0086~\3\2\2\2\u0086\177\3\2\2\2\u0086\u0080\3\2\2")
        buf.write("\2\u0086\u0081\3\2\2\2\u0086\u0082\3\2\2\2\u0086\u0083")
        buf.write("\3\2\2\2\u0086\u0084\3\2\2\2\u0086\u0085\3\2\2\2\u0087")
        buf.write("\13\3\2\2\2\u0088\u0089\5\16\b\2\u0089\u008a\7\30\2\2")
        buf.write("\u008a\u008b\58\35\2\u008b\u008c\7\24\2\2\u008c\r\3\2")
        buf.write("\2\2\u008d\u0090\7>\2\2\u008e\u0090\5R*\2\u008f\u008d")
        buf.write("\3\2\2\2\u008f\u008e\3\2\2\2\u0090\17\3\2\2\2\u0091\u0092")
        buf.write("\7\61\2\2\u0092\u0093\7\16\2\2\u0093\u0094\58\35\2\u0094")
        buf.write("\u0095\7\17\2\2\u0095\u0098\5\n\6\2\u0096\u0097\7,\2\2")
        buf.write("\u0097\u0099\5\n\6\2\u0098\u0096\3\2\2\2\u0098\u0099\3")
        buf.write("\2\2\2\u0099\21\3\2\2\2\u009a\u009b\7/\2\2\u009b\u009c")
        buf.write("\7\16\2\2\u009c\u009d\7>\2\2\u009d\u009e\7\30\2\2\u009e")
        buf.write("\u009f\58\35\2\u009f\u00a0\7\23\2\2\u00a0\u00a1\58\35")
        buf.write("\2\u00a1\u00a2\7\23\2\2\u00a2\u00a3\58\35\2\u00a3\u00a4")
        buf.write("\7\17\2\2\u00a4\u00a5\5\n\6\2\u00a5\23\3\2\2\2\u00a6\u00a7")
        buf.write("\7\66\2\2\u00a7\u00a8\7\16\2\2\u00a8\u00a9\58\35\2\u00a9")
        buf.write("\u00aa\7\17\2\2\u00aa\u00ab\5\n\6\2\u00ab\25\3\2\2\2\u00ac")
        buf.write("\u00ad\7+\2\2\u00ad\u00ae\5 \21\2\u00ae\u00af\7\66\2\2")
        buf.write("\u00af\u00b0\7\16\2\2\u00b0\u00b1\58\35\2\u00b1\u00b2")
        buf.write("\7\17\2\2\u00b2\u00b3\7\24\2\2\u00b3\27\3\2\2\2\u00b4")
        buf.write("\u00b5\7)\2\2\u00b5\u00b6\7\24\2\2\u00b6\31\3\2\2\2\u00b7")
        buf.write("\u00b8\79\2\2\u00b8\u00b9\7\24\2\2\u00b9\33\3\2\2\2\u00ba")
        buf.write("\u00bc\7\63\2\2\u00bb\u00bd\58\35\2\u00bc\u00bb\3\2\2")
        buf.write("\2\u00bc\u00bd\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00bf")
        buf.write("\7\24\2\2\u00bf\35\3\2\2\2\u00c0\u00c1\5\64\33\2\u00c1")
        buf.write("\u00c2\7\24\2\2\u00c2\37\3\2\2\2\u00c3\u00c8\7\26\2\2")
        buf.write("\u00c4\u00c7\5\n\6\2\u00c5\u00c7\5\"\22\2\u00c6\u00c4")
        buf.write("\3\2\2\2\u00c6\u00c5\3\2\2\2\u00c7\u00ca\3\2\2\2\u00c8")
        buf.write("\u00c6\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00cb\3\2\2\2")
        buf.write("\u00ca\u00c8\3\2\2\2\u00cb\u00cc\7\27\2\2\u00cc!\3\2\2")
        buf.write("\2\u00cd\u00ce\5$\23\2\u00ce\u00cf\7\25\2\2\u00cf\u00d0")
        buf.write("\5&\24\2\u00d0\u00d1\7\30\2\2\u00d1\u00d2\5T+\2\u00d2")
        buf.write("\u00d3\7\24\2\2\u00d3\u00d4\b\22\1\2\u00d4\u00db\3\2\2")
        buf.write("\2\u00d5\u00d6\5$\23\2\u00d6\u00d7\7\25\2\2\u00d7\u00d8")
        buf.write("\5Z.\2\u00d8\u00d9\7\24\2\2\u00d9\u00db\3\2\2\2\u00da")
        buf.write("\u00cd\3\2\2\2\u00da\u00d5\3\2\2\2\u00db#\3\2\2\2\u00dc")
        buf.write("\u00e1\7>\2\2\u00dd\u00de\7\23\2\2\u00de\u00e0\7>\2\2")
        buf.write("\u00df\u00dd\3\2\2\2\u00e0\u00e3\3\2\2\2\u00e1\u00df\3")
        buf.write("\2\2\2\u00e1\u00e2\3\2\2\2\u00e2%\3\2\2\2\u00e3\u00e1")
        buf.write("\3\2\2\2\u00e4\u00e7\5Z.\2\u00e5\u00e7\7\t\2\2\u00e6\u00e4")
        buf.write("\3\2\2\2\u00e6\u00e5\3\2\2\2\u00e7\'\3\2\2\2\u00e8\u00ed")
        buf.write("\5*\26\2\u00e9\u00ea\7\23\2\2\u00ea\u00ec\5*\26\2\u00eb")
        buf.write("\u00e9\3\2\2\2\u00ec\u00ef\3\2\2\2\u00ed\u00eb\3\2\2\2")
        buf.write("\u00ed\u00ee\3\2\2\2\u00ee)\3\2\2\2\u00ef\u00ed\3\2\2")
        buf.write("\2\u00f0\u00f2\7;\2\2\u00f1\u00f0\3\2\2\2\u00f1\u00f2")
        buf.write("\3\2\2\2\u00f2\u00f4\3\2\2\2\u00f3\u00f5\78\2\2\u00f4")
        buf.write("\u00f3\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f6\3\2\2\2")
        buf.write("\u00f6\u00f7\7>\2\2\u00f7\u00f8\7\25\2\2\u00f8\u00f9\5")
        buf.write("Z.\2\u00f9+\3\2\2\2\u00fa\u00fb\5.\30\2\u00fb\u00fc\5")
        buf.write("\62\32\2\u00fc-\3\2\2\2\u00fd\u00fe\7>\2\2\u00fe\u00ff")
        buf.write("\7\25\2\2\u00ff\u0100\7\60\2\2\u0100\u0101\5\60\31\2\u0101")
        buf.write("\u0102\7\16\2\2\u0102\u0103\5(\25\2\u0103\u0106\7\17\2")
        buf.write("\2\u0104\u0105\7;\2\2\u0105\u0107\7>\2\2\u0106\u0104\3")
        buf.write("\2\2\2\u0106\u0107\3\2\2\2\u0107/\3\2\2\2\u0108\u010c")
        buf.write("\5Z.\2\u0109\u010c\7\b\2\2\u010a\u010c\7\t\2\2\u010b\u0108")
        buf.write("\3\2\2\2\u010b\u0109\3\2\2\2\u010b\u010a\3\2\2\2\u010c")
        buf.write("\61\3\2\2\2\u010d\u0112\7\26\2\2\u010e\u0111\5\n\6\2\u010f")
        buf.write("\u0111\5\"\22\2\u0110\u010e\3\2\2\2\u0110\u010f\3\2\2")
        buf.write("\2\u0111\u0114\3\2\2\2\u0112\u0110\3\2\2\2\u0112\u0113")
        buf.write("\3\2\2\2\u0113\u0115\3\2\2\2\u0114\u0112\3\2\2\2\u0115")
        buf.write("\u0116\7\27\2\2\u0116\63\3\2\2\2\u0117\u0118\7>\2\2\u0118")
        buf.write("\u011c\7\16\2\2\u0119\u011b\5\66\34\2\u011a\u0119\3\2")
        buf.write("\2\2\u011b\u011e\3\2\2\2\u011c\u011a\3\2\2\2\u011c\u011d")
        buf.write("\3\2\2\2\u011d\u011f\3\2\2\2\u011e\u011c\3\2\2\2\u011f")
        buf.write("\u0120\7\17\2\2\u0120\65\3\2\2\2\u0121\u0126\58\35\2\u0122")
        buf.write("\u0123\7\23\2\2\u0123\u0125\58\35\2\u0124\u0122\3\2\2")
        buf.write("\2\u0125\u0128\3\2\2\2\u0126\u0124\3\2\2\2\u0126\u0127")
        buf.write("\3\2\2\2\u0127\67\3\2\2\2\u0128\u0126\3\2\2\2\u0129\u012c")
        buf.write("\5:\36\2\u012a\u012b\7\'\2\2\u012b\u012d\5:\36\2\u012c")
        buf.write("\u012a\3\2\2\2\u012c\u012d\3\2\2\2\u012d9\3\2\2\2\u012e")
        buf.write("\u0132\5> \2\u012f\u0130\5<\37\2\u0130\u0131\5> \2\u0131")
        buf.write("\u0133\3\2\2\2\u0132\u012f\3\2\2\2\u0132\u0133\3\2\2\2")
        buf.write("\u0133;\3\2\2\2\u0134\u0135\t\2\2\2\u0135=\3\2\2\2\u0136")
        buf.write("\u0137\b \1\2\u0137\u0138\5B\"\2\u0138\u013f\3\2\2\2\u0139")
        buf.write("\u013a\f\4\2\2\u013a\u013b\5@!\2\u013b\u013c\5B\"\2\u013c")
        buf.write("\u013e\3\2\2\2\u013d\u0139\3\2\2\2\u013e\u0141\3\2\2\2")
        buf.write("\u013f\u013d\3\2\2\2\u013f\u0140\3\2\2\2\u0140?\3\2\2")
        buf.write("\2\u0141\u013f\3\2\2\2\u0142\u0143\t\3\2\2\u0143A\3\2")
        buf.write("\2\2\u0144\u0145\b\"\1\2\u0145\u0146\5F$\2\u0146\u014d")
        buf.write("\3\2\2\2\u0147\u0148\f\4\2\2\u0148\u0149\5D#\2\u0149\u014a")
        buf.write("\5F$\2\u014a\u014c\3\2\2\2\u014b\u0147\3\2\2\2\u014c\u014f")
        buf.write("\3\2\2\2\u014d\u014b\3\2\2\2\u014d\u014e\3\2\2\2\u014e")
        buf.write("C\3\2\2\2\u014f\u014d\3\2\2\2\u0150\u0151\t\4\2\2\u0151")
        buf.write("E\3\2\2\2\u0152\u0153\b$\1\2\u0153\u0154\5J&\2\u0154\u015b")
        buf.write("\3\2\2\2\u0155\u0156\f\4\2\2\u0156\u0157\5H%\2\u0157\u0158")
        buf.write("\5J&\2\u0158\u015a\3\2\2\2\u0159\u0155\3\2\2\2\u015a\u015d")
        buf.write("\3\2\2\2\u015b\u0159\3\2\2\2\u015b\u015c\3\2\2\2\u015c")
        buf.write("G\3\2\2\2\u015d\u015b\3\2\2\2\u015e\u015f\t\5\2\2\u015f")
        buf.write("I\3\2\2\2\u0160\u0163\5L\'\2\u0161\u0164\5J&\2\u0162\u0164")
        buf.write("\5N(\2\u0163\u0161\3\2\2\2\u0163\u0162\3\2\2\2\u0164\u0167")
        buf.write("\3\2\2\2\u0165\u0167\5N(\2\u0166\u0160\3\2\2\2\u0166\u0165")
        buf.write("\3\2\2\2\u0167K\3\2\2\2\u0168\u0169\7\36\2\2\u0169M\3")
        buf.write("\2\2\2\u016a\u016d\5P)\2\u016b\u016e\5R*\2\u016c\u016e")
        buf.write("\5N(\2\u016d\u016b\3\2\2\2\u016d\u016c\3\2\2\2\u016e\u0171")
        buf.write("\3\2\2\2\u016f\u0171\5R*\2\u0170\u016a\3\2\2\2\u0170\u016f")
        buf.write("\3\2\2\2\u0171O\3\2\2\2\u0172\u0173\7\32\2\2\u0173Q\3")
        buf.write("\2\2\2\u0174\u0175\7>\2\2\u0175\u0176\7\20\2\2\u0176\u0177")
        buf.write("\5T+\2\u0177\u0178\7\21\2\2\u0178\u0181\3\2\2\2\u0179")
        buf.write("\u0181\7>\2\2\u017a\u0181\7\f\2\2\u017b\u0181\7\n\2\2")
        buf.write("\u017c\u0181\7\13\2\2\u017d\u0181\7\r\2\2\u017e\u0181")
        buf.write("\5\b\5\2\u017f\u0181\5\64\33\2\u0180\u0174\3\2\2\2\u0180")
        buf.write("\u0179\3\2\2\2\u0180\u017a\3\2\2\2\u0180\u017b\3\2\2\2")
        buf.write("\u0180\u017c\3\2\2\2\u0180\u017d\3\2\2\2\u0180\u017e\3")
        buf.write("\2\2\2\u0180\u017f\3\2\2\2\u0181S\3\2\2\2\u0182\u0187")
        buf.write("\58\35\2\u0183\u0184\7\23\2\2\u0184\u0186\58\35\2\u0185")
        buf.write("\u0183\3\2\2\2\u0186\u0189\3\2\2\2\u0187\u0185\3\2\2\2")
        buf.write("\u0187\u0188\3\2\2\2\u0188U\3\2\2\2\u0189\u0187\3\2\2")
        buf.write("\2\u018a\u018b\7\7\2\2\u018b\u018c\7\20\2\2\u018c\u018d")
        buf.write("\5X-\2\u018d\u018e\7\21\2\2\u018e\u018f\7:\2\2\u018f\u0190")
        buf.write("\5Z.\2\u0190W\3\2\2\2\u0191\u0196\7\n\2\2\u0192\u0193")
        buf.write("\7\23\2\2\u0193\u0195\7\n\2\2\u0194\u0192\3\2\2\2\u0195")
        buf.write("\u0198\3\2\2\2\u0196\u0194\3\2\2\2\u0196\u0197\3\2\2\2")
        buf.write("\u0197Y\3\2\2\2\u0198\u0196\3\2\2\2\u0199\u019a\t\6\2")
        buf.write("\2\u019a[\3\2\2\2$_aqs\u0086\u008f\u0098\u00bc\u00c6\u00c8")
        buf.write("\u00da\u00e1\u00e6\u00ed\u00f1\u00f4\u0106\u010b\u0110")
        buf.write("\u0112\u011c\u0126\u012c\u0132\u013f\u014d\u015b\u0163")
        buf.write("\u0166\u016d\u0170\u0180\u0187\u0196")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'['", "']'", "'.'", "','", "';'", "':'", 
                     "'{'", "'}'", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", 
                     "'>'", "'>='", "'::'", "'auto'", "'break'", "'boolean'", 
                     "'do'", "'else'", "'false'", "'float'", "'for'", "'function'", 
                     "'if'", "'integer'", "'return'", "'string'", "'true'", 
                     "'while'", "'void'", "'out'", "'continue'", "'of'", 
                     "'inherit'", "'array'", "'main'" ]

    symbolicNames = [ "<INVALID>", "BooleanType", "IntegerType", "FloatType", 
                      "StringType", "ArrayType", "VoidType", "AutoType", 
                      "IntegerL", "FloatL", "BooleanL", "StringL", "LPAREN", 
                      "RPAREN", "LSQUARE", "RSQUARE", "DOT", "COMMA", "SEMICOLON", 
                      "COLON", "LBRACKET", "RBRACKET", "ASIGN", "PLUS", 
                      "MINUS", "STAR", "DIV", "MOD", "NOT", "ANDAND", "OROR", 
                      "EQEQ", "NOTEQ", "LESS", "LESSEQ", "CREATER", "CREATEREQ", 
                      "DOUBLECOLON", "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", 
                      "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", 
                      "RETURN", "STRING", "TRUE", "WHILE", "VOID", "OUT", 
                      "CONTINUE", "OF", "INHERIT", "ARRAY", "MAIN", "Identifier", 
                      "WhiteSpaces", "BlockComment", "LineComment", "UNCLOSE_STRING", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_func_main = 1
    RULE_main_return = 2
    RULE_arrayL = 3
    RULE_stmt = 4
    RULE_assign_stmt = 5
    RULE_lhs = 6
    RULE_if_stmt = 7
    RULE_for_stmt = 8
    RULE_while_stmt = 9
    RULE_do_while_stmt = 10
    RULE_break_stmt = 11
    RULE_continue_stmt = 12
    RULE_return_stmt = 13
    RULE_call_stmt = 14
    RULE_block_stmt = 15
    RULE_variable_decl = 16
    RULE_identifier_list = 17
    RULE_valid_type = 18
    RULE_para_list_decl = 19
    RULE_para_decl = 20
    RULE_func_decl = 21
    RULE_func_prototype = 22
    RULE_func_return_type = 23
    RULE_func_body = 24
    RULE_func_call = 25
    RULE_arg_list = 26
    RULE_expression = 27
    RULE_relation_expr = 28
    RULE_relation_op = 29
    RULE_logical_expr = 30
    RULE_logical_op = 31
    RULE_adding_expr = 32
    RULE_adding_op = 33
    RULE_multiplying_expr = 34
    RULE_multiplying_op = 35
    RULE_unary_logical_expr = 36
    RULE_unary_logical_op = 37
    RULE_sign_expr = 38
    RULE_sign_op = 39
    RULE_index_expr = 40
    RULE_expr_list = 41
    RULE_array_decl = 42
    RULE_integer_list = 43
    RULE_atomic_type = 44

    ruleNames =  [ "program", "func_main", "main_return", "arrayL", "stmt", 
                   "assign_stmt", "lhs", "if_stmt", "for_stmt", "while_stmt", 
                   "do_while_stmt", "break_stmt", "continue_stmt", "return_stmt", 
                   "call_stmt", "block_stmt", "variable_decl", "identifier_list", 
                   "valid_type", "para_list_decl", "para_decl", "func_decl", 
                   "func_prototype", "func_return_type", "func_body", "func_call", 
                   "arg_list", "expression", "relation_expr", "relation_op", 
                   "logical_expr", "logical_op", "adding_expr", "adding_op", 
                   "multiplying_expr", "multiplying_op", "unary_logical_expr", 
                   "unary_logical_op", "sign_expr", "sign_op", "index_expr", 
                   "expr_list", "array_decl", "integer_list", "atomic_type" ]

    EOF = Token.EOF
    BooleanType=1
    IntegerType=2
    FloatType=3
    StringType=4
    ArrayType=5
    VoidType=6
    AutoType=7
    IntegerL=8
    FloatL=9
    BooleanL=10
    StringL=11
    LPAREN=12
    RPAREN=13
    LSQUARE=14
    RSQUARE=15
    DOT=16
    COMMA=17
    SEMICOLON=18
    COLON=19
    LBRACKET=20
    RBRACKET=21
    ASIGN=22
    PLUS=23
    MINUS=24
    STAR=25
    DIV=26
    MOD=27
    NOT=28
    ANDAND=29
    OROR=30
    EQEQ=31
    NOTEQ=32
    LESS=33
    LESSEQ=34
    CREATER=35
    CREATEREQ=36
    DOUBLECOLON=37
    AUTO=38
    BREAK=39
    BOOLEAN=40
    DO=41
    ELSE=42
    FALSE=43
    FLOAT=44
    FOR=45
    FUNCTION=46
    IF=47
    INTEGER=48
    RETURN=49
    STRING=50
    TRUE=51
    WHILE=52
    VOID=53
    OUT=54
    CONTINUE=55
    OF=56
    INHERIT=57
    ARRAY=58
    MAIN=59
    Identifier=60
    WhiteSpaces=61
    BlockComment=62
    LineComment=63
    UNCLOSE_STRING=64
    ERROR_CHAR=65

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def variable_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Variable_declContext)
            else:
                return self.getTypedRuleContext(MT22Parser.Variable_declContext,i)


        def func_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Func_declContext)
            else:
                return self.getTypedRuleContext(MT22Parser.Func_declContext,i)


        def func_main(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Func_mainContext)
            else:
                return self.getTypedRuleContext(MT22Parser.Func_mainContext,i)


        def getRuleIndex(self):
            return MT22Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.MAIN or _la==MT22Parser.Identifier:
                self.state = 93
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 90
                    self.variable_decl()
                    pass

                elif la_ == 2:
                    self.state = 91
                    self.func_decl()
                    pass

                elif la_ == 3:
                    self.state = 92
                    self.func_main()
                    pass


                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 98
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_mainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAIN(self):
            return self.getToken(MT22Parser.MAIN, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def FUNCTION(self):
            return self.getToken(MT22Parser.FUNCTION, 0)

        def VoidType(self):
            return self.getToken(MT22Parser.VoidType, 0)

        def LPAREN(self):
            return self.getToken(MT22Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MT22Parser.RPAREN, 0)

        def main_return(self):
            return self.getTypedRuleContext(MT22Parser.Main_returnContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_func_main

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_main" ):
                return visitor.visitFunc_main(self)
            else:
                return visitor.visitChildren(self)




    def func_main(self):

        localctx = MT22Parser.Func_mainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_func_main)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(MT22Parser.MAIN)
            self.state = 101
            self.match(MT22Parser.COLON)
            self.state = 102
            self.match(MT22Parser.FUNCTION)
            self.state = 103
            self.match(MT22Parser.VoidType)
            self.state = 104
            self.match(MT22Parser.LPAREN)
            self.state = 105
            self.match(MT22Parser.RPAREN)
            self.state = 106
            self.main_return()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_returnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(MT22Parser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(MT22Parser.RBRACKET, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StmtContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StmtContext,i)


        def variable_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Variable_declContext)
            else:
                return self.getTypedRuleContext(MT22Parser.Variable_declContext,i)


        def getRuleIndex(self):
            return MT22Parser.RULE_main_return

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain_return" ):
                return visitor.visitMain_return(self)
            else:
                return visitor.visitChildren(self)




    def main_return(self):

        localctx = MT22Parser.Main_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_main_return)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(MT22Parser.LBRACKET)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.IntegerL) | (1 << MT22Parser.FloatL) | (1 << MT22Parser.BooleanL) | (1 << MT22Parser.StringL) | (1 << MT22Parser.LBRACKET) | (1 << MT22Parser.BREAK) | (1 << MT22Parser.DO) | (1 << MT22Parser.FOR) | (1 << MT22Parser.IF) | (1 << MT22Parser.RETURN) | (1 << MT22Parser.WHILE) | (1 << MT22Parser.CONTINUE) | (1 << MT22Parser.Identifier))) != 0):
                self.state = 111
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 109
                    self.stmt()
                    pass

                elif la_ == 2:
                    self.state = 110
                    self.variable_decl()
                    pass


                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 116
            self.match(MT22Parser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(MT22Parser.LBRACKET, 0)

        def expr_list(self):
            return self.getTypedRuleContext(MT22Parser.Expr_listContext,0)


        def RBRACKET(self):
            return self.getToken(MT22Parser.RBRACKET, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_arrayL

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayL" ):
                return visitor.visitArrayL(self)
            else:
                return visitor.visitChildren(self)




    def arrayL(self):

        localctx = MT22Parser.ArrayLContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_arrayL)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(MT22Parser.LBRACKET)
            self.state = 119
            self.expr_list()
            self.state = 120
            self.match(MT22Parser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(MT22Parser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(MT22Parser.For_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(MT22Parser.While_stmtContext,0)


        def do_while_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Do_while_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Return_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Call_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MT22Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_stmt)
        try:
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 124
                self.for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 125
                self.while_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 126
                self.do_while_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 127
                self.break_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 128
                self.continue_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 129
                self.return_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 130
                self.call_stmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 131
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MT22Parser.LhsContext,0)


        def ASIGN(self):
            return self.getToken(MT22Parser.ASIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(MT22Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = MT22Parser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.lhs()
            self.state = 135
            self.match(MT22Parser.ASIGN)
            self.state = 136
            self.expression()
            self.state = 137
            self.match(MT22Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MT22Parser.Identifier, 0)

        def index_expr(self):
            return self.getTypedRuleContext(MT22Parser.Index_exprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = MT22Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_lhs)
        try:
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.match(MT22Parser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.index_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MT22Parser.IF, 0)

        def LPAREN(self):
            return self.getToken(MT22Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MT22Parser.RPAREN, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StmtContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StmtContext,i)


        def ELSE(self):
            return self.getToken(MT22Parser.ELSE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = MT22Parser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(MT22Parser.IF)
            self.state = 144
            self.match(MT22Parser.LPAREN)
            self.state = 145
            self.expression()
            self.state = 146
            self.match(MT22Parser.RPAREN)
            self.state = 147
            self.stmt()
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 148
                self.match(MT22Parser.ELSE)
                self.state = 149
                self.stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MT22Parser.FOR, 0)

        def LPAREN(self):
            return self.getToken(MT22Parser.LPAREN, 0)

        def Identifier(self):
            return self.getToken(MT22Parser.Identifier, 0)

        def ASIGN(self):
            return self.getToken(MT22Parser.ASIGN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def RPAREN(self):
            return self.getToken(MT22Parser.RPAREN, 0)

        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = MT22Parser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(MT22Parser.FOR)
            self.state = 153
            self.match(MT22Parser.LPAREN)
            self.state = 154
            self.match(MT22Parser.Identifier)
            self.state = 155
            self.match(MT22Parser.ASIGN)
            self.state = 156
            self.expression()
            self.state = 157
            self.match(MT22Parser.COMMA)
            self.state = 158
            self.expression()
            self.state = 159
            self.match(MT22Parser.COMMA)
            self.state = 160
            self.expression()
            self.state = 161
            self.match(MT22Parser.RPAREN)
            self.state = 162
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(MT22Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MT22Parser.RPAREN, 0)

        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = MT22Parser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(MT22Parser.WHILE)
            self.state = 165
            self.match(MT22Parser.LPAREN)
            self.state = 166
            self.expression()
            self.state = 167
            self.match(MT22Parser.RPAREN)
            self.state = 168
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(MT22Parser.DO, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Block_stmtContext,0)


        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(MT22Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MT22Parser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(MT22Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_do_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_while_stmt" ):
                return visitor.visitDo_while_stmt(self)
            else:
                return visitor.visitChildren(self)




    def do_while_stmt(self):

        localctx = MT22Parser.Do_while_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_do_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(MT22Parser.DO)
            self.state = 171
            self.block_stmt()
            self.state = 172
            self.match(MT22Parser.WHILE)
            self.state = 173
            self.match(MT22Parser.LPAREN)
            self.state = 174
            self.expression()
            self.state = 175
            self.match(MT22Parser.RPAREN)
            self.state = 176
            self.match(MT22Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MT22Parser.BREAK, 0)

        def SEMICOLON(self):
            return self.getToken(MT22Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = MT22Parser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(MT22Parser.BREAK)
            self.state = 179
            self.match(MT22Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MT22Parser.CONTINUE, 0)

        def SEMICOLON(self):
            return self.getToken(MT22Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = MT22Parser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(MT22Parser.CONTINUE)
            self.state = 182
            self.match(MT22Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MT22Parser.RETURN, 0)

        def SEMICOLON(self):
            return self.getToken(MT22Parser.SEMICOLON, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = MT22Parser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(MT22Parser.RETURN)
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.IntegerL) | (1 << MT22Parser.FloatL) | (1 << MT22Parser.BooleanL) | (1 << MT22Parser.StringL) | (1 << MT22Parser.LBRACKET) | (1 << MT22Parser.MINUS) | (1 << MT22Parser.NOT) | (1 << MT22Parser.Identifier))) != 0):
                self.state = 185
                self.expression()


            self.state = 188
            self.match(MT22Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_call(self):
            return self.getTypedRuleContext(MT22Parser.Func_callContext,0)


        def SEMICOLON(self):
            return self.getToken(MT22Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = MT22Parser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.func_call()
            self.state = 191
            self.match(MT22Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(MT22Parser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(MT22Parser.RBRACKET, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StmtContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StmtContext,i)


        def variable_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Variable_declContext)
            else:
                return self.getTypedRuleContext(MT22Parser.Variable_declContext,i)


        def getRuleIndex(self):
            return MT22Parser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = MT22Parser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(MT22Parser.LBRACKET)
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.IntegerL) | (1 << MT22Parser.FloatL) | (1 << MT22Parser.BooleanL) | (1 << MT22Parser.StringL) | (1 << MT22Parser.LBRACKET) | (1 << MT22Parser.BREAK) | (1 << MT22Parser.DO) | (1 << MT22Parser.FOR) | (1 << MT22Parser.IF) | (1 << MT22Parser.RETURN) | (1 << MT22Parser.WHILE) | (1 << MT22Parser.CONTINUE) | (1 << MT22Parser.Identifier))) != 0):
                self.state = 196
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 194
                    self.stmt()
                    pass

                elif la_ == 2:
                    self.state = 195
                    self.variable_decl()
                    pass


                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 201
            self.match(MT22Parser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.l = None # Identifier_listContext
            self.r = None # Expr_listContext
            self.e = None # Token

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def valid_type(self):
            return self.getTypedRuleContext(MT22Parser.Valid_typeContext,0)


        def ASIGN(self):
            return self.getToken(MT22Parser.ASIGN, 0)

        def identifier_list(self):
            return self.getTypedRuleContext(MT22Parser.Identifier_listContext,0)


        def expr_list(self):
            return self.getTypedRuleContext(MT22Parser.Expr_listContext,0)


        def SEMICOLON(self):
            return self.getToken(MT22Parser.SEMICOLON, 0)

        def atomic_type(self):
            return self.getTypedRuleContext(MT22Parser.Atomic_typeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_variable_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_decl" ):
                return visitor.visitVariable_decl(self)
            else:
                return visitor.visitChildren(self)




    def variable_decl(self):

        localctx = MT22Parser.Variable_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_variable_decl)
        try:
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                localctx.l = self.identifier_list()
                self.state = 204
                self.match(MT22Parser.COLON)
                self.state = 205
                self.valid_type()
                self.state = 206
                self.match(MT22Parser.ASIGN)
                self.state = 207
                localctx.r = self.expr_list()
                self.state = 208
                localctx.e = self.match(MT22Parser.SEMICOLON)
                if len((None if localctx.l is None else self._input.getText(localctx.l.start,localctx.l.stop)).split(',')) != len((None if localctx.r is None else self._input.getText(localctx.r.start,localctx.r.stop)).split(',')):
                        raise Exception('Error on line {} col {}: ;'.format((0 if localctx.e is None else localctx.e.line), (0 if localctx.e is None else localctx.e.column)))
                    
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
                self.identifier_list()
                self.state = 212
                self.match(MT22Parser.COLON)
                self.state = 213
                self.atomic_type()
                self.state = 214
                self.match(MT22Parser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Identifier_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.Identifier)
            else:
                return self.getToken(MT22Parser.Identifier, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_identifier_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier_list" ):
                return visitor.visitIdentifier_list(self)
            else:
                return visitor.visitChildren(self)




    def identifier_list(self):

        localctx = MT22Parser.Identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_identifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(MT22Parser.Identifier)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.COMMA:
                self.state = 219
                self.match(MT22Parser.COMMA)
                self.state = 220
                self.match(MT22Parser.Identifier)
                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Valid_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atomic_type(self):
            return self.getTypedRuleContext(MT22Parser.Atomic_typeContext,0)


        def AutoType(self):
            return self.getToken(MT22Parser.AutoType, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_valid_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValid_type" ):
                return visitor.visitValid_type(self)
            else:
                return visitor.visitChildren(self)




    def valid_type(self):

        localctx = MT22Parser.Valid_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_valid_type)
        try:
            self.state = 228
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BooleanType, MT22Parser.IntegerType, MT22Parser.FloatType, MT22Parser.StringType]:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.atomic_type()
                pass
            elif token in [MT22Parser.AutoType]:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                self.match(MT22Parser.AutoType)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_list_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Para_declContext)
            else:
                return self.getTypedRuleContext(MT22Parser.Para_declContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_para_list_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_list_decl" ):
                return visitor.visitPara_list_decl(self)
            else:
                return visitor.visitChildren(self)




    def para_list_decl(self):

        localctx = MT22Parser.Para_list_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_para_list_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.para_decl()
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.COMMA:
                self.state = 231
                self.match(MT22Parser.COMMA)
                self.state = 232
                self.para_decl()
                self.state = 237
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MT22Parser.Identifier, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def atomic_type(self):
            return self.getTypedRuleContext(MT22Parser.Atomic_typeContext,0)


        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def OUT(self):
            return self.getToken(MT22Parser.OUT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_para_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_decl" ):
                return visitor.visitPara_decl(self)
            else:
                return visitor.visitChildren(self)




    def para_decl(self):

        localctx = MT22Parser.Para_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_para_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 238
                self.match(MT22Parser.INHERIT)


            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.OUT:
                self.state = 241
                self.match(MT22Parser.OUT)


            self.state = 244
            self.match(MT22Parser.Identifier)
            self.state = 245
            self.match(MT22Parser.COLON)
            self.state = 246
            self.atomic_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_prototype(self):
            return self.getTypedRuleContext(MT22Parser.Func_prototypeContext,0)


        def func_body(self):
            return self.getTypedRuleContext(MT22Parser.Func_bodyContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = MT22Parser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.func_prototype()
            self.state = 249
            self.func_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_prototypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.Identifier)
            else:
                return self.getToken(MT22Parser.Identifier, i)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def FUNCTION(self):
            return self.getToken(MT22Parser.FUNCTION, 0)

        def func_return_type(self):
            return self.getTypedRuleContext(MT22Parser.Func_return_typeContext,0)


        def LPAREN(self):
            return self.getToken(MT22Parser.LPAREN, 0)

        def para_list_decl(self):
            return self.getTypedRuleContext(MT22Parser.Para_list_declContext,0)


        def RPAREN(self):
            return self.getToken(MT22Parser.RPAREN, 0)

        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_func_prototype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_prototype" ):
                return visitor.visitFunc_prototype(self)
            else:
                return visitor.visitChildren(self)




    def func_prototype(self):

        localctx = MT22Parser.Func_prototypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_func_prototype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(MT22Parser.Identifier)
            self.state = 252
            self.match(MT22Parser.COLON)
            self.state = 253
            self.match(MT22Parser.FUNCTION)
            self.state = 254
            self.func_return_type()
            self.state = 255
            self.match(MT22Parser.LPAREN)
            self.state = 256
            self.para_list_decl()
            self.state = 257
            self.match(MT22Parser.RPAREN)
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 258
                self.match(MT22Parser.INHERIT)
                self.state = 259
                self.match(MT22Parser.Identifier)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_return_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atomic_type(self):
            return self.getTypedRuleContext(MT22Parser.Atomic_typeContext,0)


        def VoidType(self):
            return self.getToken(MT22Parser.VoidType, 0)

        def AutoType(self):
            return self.getToken(MT22Parser.AutoType, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_func_return_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_return_type" ):
                return visitor.visitFunc_return_type(self)
            else:
                return visitor.visitChildren(self)




    def func_return_type(self):

        localctx = MT22Parser.Func_return_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_func_return_type)
        try:
            self.state = 265
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BooleanType, MT22Parser.IntegerType, MT22Parser.FloatType, MT22Parser.StringType]:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.atomic_type()
                pass
            elif token in [MT22Parser.VoidType]:
                self.enterOuterAlt(localctx, 2)
                self.state = 263
                self.match(MT22Parser.VoidType)
                pass
            elif token in [MT22Parser.AutoType]:
                self.enterOuterAlt(localctx, 3)
                self.state = 264
                self.match(MT22Parser.AutoType)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(MT22Parser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(MT22Parser.RBRACKET, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StmtContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StmtContext,i)


        def variable_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Variable_declContext)
            else:
                return self.getTypedRuleContext(MT22Parser.Variable_declContext,i)


        def getRuleIndex(self):
            return MT22Parser.RULE_func_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_body" ):
                return visitor.visitFunc_body(self)
            else:
                return visitor.visitChildren(self)




    def func_body(self):

        localctx = MT22Parser.Func_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_func_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(MT22Parser.LBRACKET)
            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.IntegerL) | (1 << MT22Parser.FloatL) | (1 << MT22Parser.BooleanL) | (1 << MT22Parser.StringL) | (1 << MT22Parser.LBRACKET) | (1 << MT22Parser.BREAK) | (1 << MT22Parser.DO) | (1 << MT22Parser.FOR) | (1 << MT22Parser.IF) | (1 << MT22Parser.RETURN) | (1 << MT22Parser.WHILE) | (1 << MT22Parser.CONTINUE) | (1 << MT22Parser.Identifier))) != 0):
                self.state = 270
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 268
                    self.stmt()
                    pass

                elif la_ == 2:
                    self.state = 269
                    self.variable_decl()
                    pass


                self.state = 274
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 275
            self.match(MT22Parser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MT22Parser.Identifier, 0)

        def LPAREN(self):
            return self.getToken(MT22Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MT22Parser.RPAREN, 0)

        def arg_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Arg_listContext)
            else:
                return self.getTypedRuleContext(MT22Parser.Arg_listContext,i)


        def getRuleIndex(self):
            return MT22Parser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = MT22Parser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(MT22Parser.Identifier)
            self.state = 278
            self.match(MT22Parser.LPAREN)
            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.IntegerL) | (1 << MT22Parser.FloatL) | (1 << MT22Parser.BooleanL) | (1 << MT22Parser.StringL) | (1 << MT22Parser.LBRACKET) | (1 << MT22Parser.MINUS) | (1 << MT22Parser.NOT) | (1 << MT22Parser.Identifier))) != 0):
                self.state = 279
                self.arg_list()
                self.state = 284
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 285
            self.match(MT22Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arg_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_arg_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg_list" ):
                return visitor.visitArg_list(self)
            else:
                return visitor.visitChildren(self)




    def arg_list(self):

        localctx = MT22Parser.Arg_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_arg_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.expression()
            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.COMMA:
                self.state = 288
                self.match(MT22Parser.COMMA)
                self.state = 289
                self.expression()
                self.state = 294
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relation_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Relation_exprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.Relation_exprContext,i)


        def DOUBLECOLON(self):
            return self.getToken(MT22Parser.DOUBLECOLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = MT22Parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.relation_expr()
            self.state = 298
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.DOUBLECOLON:
                self.state = 296
                self.match(MT22Parser.DOUBLECOLON)
                self.state = 297
                self.relation_expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relation_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Logical_exprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.Logical_exprContext,i)


        def relation_op(self):
            return self.getTypedRuleContext(MT22Parser.Relation_opContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_relation_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelation_expr" ):
                return visitor.visitRelation_expr(self)
            else:
                return visitor.visitChildren(self)




    def relation_expr(self):

        localctx = MT22Parser.Relation_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_relation_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.logical_expr(0)
            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.EQEQ) | (1 << MT22Parser.NOTEQ) | (1 << MT22Parser.LESS) | (1 << MT22Parser.LESSEQ) | (1 << MT22Parser.CREATER) | (1 << MT22Parser.CREATEREQ))) != 0):
                self.state = 301
                self.relation_op()
                self.state = 302
                self.logical_expr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relation_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQEQ(self):
            return self.getToken(MT22Parser.EQEQ, 0)

        def NOTEQ(self):
            return self.getToken(MT22Parser.NOTEQ, 0)

        def LESS(self):
            return self.getToken(MT22Parser.LESS, 0)

        def CREATER(self):
            return self.getToken(MT22Parser.CREATER, 0)

        def LESSEQ(self):
            return self.getToken(MT22Parser.LESSEQ, 0)

        def CREATEREQ(self):
            return self.getToken(MT22Parser.CREATEREQ, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_relation_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelation_op" ):
                return visitor.visitRelation_op(self)
            else:
                return visitor.visitChildren(self)




    def relation_op(self):

        localctx = MT22Parser.Relation_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_relation_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.EQEQ) | (1 << MT22Parser.NOTEQ) | (1 << MT22Parser.LESS) | (1 << MT22Parser.LESSEQ) | (1 << MT22Parser.CREATER) | (1 << MT22Parser.CREATEREQ))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def adding_expr(self):
            return self.getTypedRuleContext(MT22Parser.Adding_exprContext,0)


        def logical_expr(self):
            return self.getTypedRuleContext(MT22Parser.Logical_exprContext,0)


        def logical_op(self):
            return self.getTypedRuleContext(MT22Parser.Logical_opContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_logical_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_expr" ):
                return visitor.visitLogical_expr(self)
            else:
                return visitor.visitChildren(self)



    def logical_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Logical_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_logical_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.adding_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 317
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Logical_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expr)
                    self.state = 311
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 312
                    self.logical_op()
                    self.state = 313
                    self.adding_expr(0) 
                self.state = 319
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Logical_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ANDAND(self):
            return self.getToken(MT22Parser.ANDAND, 0)

        def OROR(self):
            return self.getToken(MT22Parser.OROR, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_logical_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_op" ):
                return visitor.visitLogical_op(self)
            else:
                return visitor.visitChildren(self)




    def logical_op(self):

        localctx = MT22Parser.Logical_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_logical_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            _la = self._input.LA(1)
            if not(_la==MT22Parser.ANDAND or _la==MT22Parser.OROR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Adding_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplying_expr(self):
            return self.getTypedRuleContext(MT22Parser.Multiplying_exprContext,0)


        def adding_expr(self):
            return self.getTypedRuleContext(MT22Parser.Adding_exprContext,0)


        def adding_op(self):
            return self.getTypedRuleContext(MT22Parser.Adding_opContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_adding_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdding_expr" ):
                return visitor.visitAdding_expr(self)
            else:
                return visitor.visitChildren(self)



    def adding_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Adding_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_adding_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.multiplying_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 331
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Adding_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_adding_expr)
                    self.state = 325
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 326
                    self.adding_op()
                    self.state = 327
                    self.multiplying_expr(0) 
                self.state = 333
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Adding_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(MT22Parser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MT22Parser.MINUS, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_adding_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdding_op" ):
                return visitor.visitAdding_op(self)
            else:
                return visitor.visitChildren(self)




    def adding_op(self):

        localctx = MT22Parser.Adding_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_adding_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            _la = self._input.LA(1)
            if not(_la==MT22Parser.PLUS or _la==MT22Parser.MINUS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multiplying_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary_logical_expr(self):
            return self.getTypedRuleContext(MT22Parser.Unary_logical_exprContext,0)


        def multiplying_expr(self):
            return self.getTypedRuleContext(MT22Parser.Multiplying_exprContext,0)


        def multiplying_op(self):
            return self.getTypedRuleContext(MT22Parser.Multiplying_opContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_multiplying_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplying_expr" ):
                return visitor.visitMultiplying_expr(self)
            else:
                return visitor.visitChildren(self)



    def multiplying_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Multiplying_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_multiplying_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.unary_logical_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 345
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Multiplying_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplying_expr)
                    self.state = 339
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 340
                    self.multiplying_op()
                    self.state = 341
                    self.unary_logical_expr() 
                self.state = 347
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Multiplying_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(MT22Parser.STAR, 0)

        def DIV(self):
            return self.getToken(MT22Parser.DIV, 0)

        def MOD(self):
            return self.getToken(MT22Parser.MOD, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_multiplying_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplying_op" ):
                return visitor.visitMultiplying_op(self)
            else:
                return visitor.visitChildren(self)




    def multiplying_op(self):

        localctx = MT22Parser.Multiplying_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_multiplying_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.STAR) | (1 << MT22Parser.DIV) | (1 << MT22Parser.MOD))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unary_logical_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary_logical_op(self):
            return self.getTypedRuleContext(MT22Parser.Unary_logical_opContext,0)


        def unary_logical_expr(self):
            return self.getTypedRuleContext(MT22Parser.Unary_logical_exprContext,0)


        def sign_expr(self):
            return self.getTypedRuleContext(MT22Parser.Sign_exprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_unary_logical_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_logical_expr" ):
                return visitor.visitUnary_logical_expr(self)
            else:
                return visitor.visitChildren(self)




    def unary_logical_expr(self):

        localctx = MT22Parser.Unary_logical_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_unary_logical_expr)
        try:
            self.state = 356
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.unary_logical_op()
                self.state = 353
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                if la_ == 1:
                    self.state = 351
                    self.unary_logical_expr()
                    pass

                elif la_ == 2:
                    self.state = 352
                    self.sign_expr()
                    pass


                pass
            elif token in [MT22Parser.IntegerL, MT22Parser.FloatL, MT22Parser.BooleanL, MT22Parser.StringL, MT22Parser.LBRACKET, MT22Parser.MINUS, MT22Parser.Identifier]:
                self.enterOuterAlt(localctx, 2)
                self.state = 355
                self.sign_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unary_logical_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(MT22Parser.NOT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_unary_logical_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_logical_op" ):
                return visitor.visitUnary_logical_op(self)
            else:
                return visitor.visitChildren(self)




    def unary_logical_op(self):

        localctx = MT22Parser.Unary_logical_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_unary_logical_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(MT22Parser.NOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sign_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sign_op(self):
            return self.getTypedRuleContext(MT22Parser.Sign_opContext,0)


        def index_expr(self):
            return self.getTypedRuleContext(MT22Parser.Index_exprContext,0)


        def sign_expr(self):
            return self.getTypedRuleContext(MT22Parser.Sign_exprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_sign_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign_expr" ):
                return visitor.visitSign_expr(self)
            else:
                return visitor.visitChildren(self)




    def sign_expr(self):

        localctx = MT22Parser.Sign_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_sign_expr)
        try:
            self.state = 366
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 360
                self.sign_op()
                self.state = 363
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                if la_ == 1:
                    self.state = 361
                    self.index_expr()
                    pass

                elif la_ == 2:
                    self.state = 362
                    self.sign_expr()
                    pass


                pass
            elif token in [MT22Parser.IntegerL, MT22Parser.FloatL, MT22Parser.BooleanL, MT22Parser.StringL, MT22Parser.LBRACKET, MT22Parser.Identifier]:
                self.enterOuterAlt(localctx, 2)
                self.state = 365
                self.index_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sign_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(MT22Parser.MINUS, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_sign_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign_op" ):
                return visitor.visitSign_op(self)
            else:
                return visitor.visitChildren(self)




    def sign_op(self):

        localctx = MT22Parser.Sign_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_sign_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.match(MT22Parser.MINUS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MT22Parser.Identifier, 0)

        def LSQUARE(self):
            return self.getToken(MT22Parser.LSQUARE, 0)

        def expr_list(self):
            return self.getTypedRuleContext(MT22Parser.Expr_listContext,0)


        def RSQUARE(self):
            return self.getToken(MT22Parser.RSQUARE, 0)

        def BooleanL(self):
            return self.getToken(MT22Parser.BooleanL, 0)

        def IntegerL(self):
            return self.getToken(MT22Parser.IntegerL, 0)

        def FloatL(self):
            return self.getToken(MT22Parser.FloatL, 0)

        def StringL(self):
            return self.getToken(MT22Parser.StringL, 0)

        def arrayL(self):
            return self.getTypedRuleContext(MT22Parser.ArrayLContext,0)


        def func_call(self):
            return self.getTypedRuleContext(MT22Parser.Func_callContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_index_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_expr" ):
                return visitor.visitIndex_expr(self)
            else:
                return visitor.visitChildren(self)




    def index_expr(self):

        localctx = MT22Parser.Index_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_index_expr)
        try:
            self.state = 382
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 370
                self.match(MT22Parser.Identifier)
                self.state = 371
                self.match(MT22Parser.LSQUARE)
                self.state = 372
                self.expr_list()
                self.state = 373
                self.match(MT22Parser.RSQUARE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 375
                self.match(MT22Parser.Identifier)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 376
                self.match(MT22Parser.BooleanL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 377
                self.match(MT22Parser.IntegerL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 378
                self.match(MT22Parser.FloatL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 379
                self.match(MT22Parser.StringL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 380
                self.arrayL()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 381
                self.func_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = MT22Parser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expr_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.expression()
            self.state = 389
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.COMMA:
                self.state = 385
                self.match(MT22Parser.COMMA)
                self.state = 386
                self.expression()
                self.state = 391
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ArrayType(self):
            return self.getToken(MT22Parser.ArrayType, 0)

        def LSQUARE(self):
            return self.getToken(MT22Parser.LSQUARE, 0)

        def integer_list(self):
            return self.getTypedRuleContext(MT22Parser.Integer_listContext,0)


        def RSQUARE(self):
            return self.getToken(MT22Parser.RSQUARE, 0)

        def OF(self):
            return self.getToken(MT22Parser.OF, 0)

        def atomic_type(self):
            return self.getTypedRuleContext(MT22Parser.Atomic_typeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_array_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_decl" ):
                return visitor.visitArray_decl(self)
            else:
                return visitor.visitChildren(self)




    def array_decl(self):

        localctx = MT22Parser.Array_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_array_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.match(MT22Parser.ArrayType)
            self.state = 393
            self.match(MT22Parser.LSQUARE)
            self.state = 394
            self.integer_list()
            self.state = 395
            self.match(MT22Parser.RSQUARE)
            self.state = 396
            self.match(MT22Parser.OF)
            self.state = 397
            self.atomic_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Integer_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IntegerL(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.IntegerL)
            else:
                return self.getToken(MT22Parser.IntegerL, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_integer_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteger_list" ):
                return visitor.visitInteger_list(self)
            else:
                return visitor.visitChildren(self)




    def integer_list(self):

        localctx = MT22Parser.Integer_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_integer_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.match(MT22Parser.IntegerL)
            self.state = 404
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.COMMA:
                self.state = 400
                self.match(MT22Parser.COMMA)
                self.state = 401
                self.match(MT22Parser.IntegerL)
                self.state = 406
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Atomic_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BooleanType(self):
            return self.getToken(MT22Parser.BooleanType, 0)

        def IntegerType(self):
            return self.getToken(MT22Parser.IntegerType, 0)

        def FloatType(self):
            return self.getToken(MT22Parser.FloatType, 0)

        def StringType(self):
            return self.getToken(MT22Parser.StringType, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_atomic_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomic_type" ):
                return visitor.visitAtomic_type(self)
            else:
                return visitor.visitChildren(self)




    def atomic_type(self):

        localctx = MT22Parser.Atomic_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_atomic_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.BooleanType) | (1 << MT22Parser.IntegerType) | (1 << MT22Parser.FloatType) | (1 << MT22Parser.StringType))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[30] = self.logical_expr_sempred
        self._predicates[32] = self.adding_expr_sempred
        self._predicates[34] = self.multiplying_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def logical_expr_sempred(self, localctx:Logical_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def adding_expr_sempred(self, localctx:Adding_exprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def multiplying_expr_sempred(self, localctx:Multiplying_exprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




