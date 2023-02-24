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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3F")
        buf.write("\u019c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\3")
        buf.write("\2\3\2\3\2\7\2`\n\2\f\2\16\2c\13\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\7\4r\n\4\f\4\16\4u\13")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5")
        buf.write("\u0083\n\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\5\7\u008c\n\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u0095\n\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\16\3\16\5\16\u00b9\n\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\7\20\u00c3\n\20\f\20\16\20\u00c6")
        buf.write("\13\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\5\21\u00d7\n\21\3\22\3\22")
        buf.write("\3\22\7\22\u00dc\n\22\f\22\16\22\u00df\13\22\3\23\3\23")
        buf.write("\5\23\u00e3\n\23\3\24\3\24\3\24\7\24\u00e8\n\24\f\24\16")
        buf.write("\24\u00eb\13\24\3\25\5\25\u00ee\n\25\3\25\5\25\u00f1\n")
        buf.write("\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u0103\n\27\3\30\3")
        buf.write("\30\3\30\5\30\u0108\n\30\3\31\3\31\3\31\7\31\u010d\n\31")
        buf.write("\f\31\16\31\u0110\13\31\3\31\3\31\3\32\3\32\3\32\7\32")
        buf.write("\u0117\n\32\f\32\16\32\u011a\13\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\7\33\u0121\n\33\f\33\16\33\u0124\13\33\3\34\3\34")
        buf.write("\3\34\5\34\u0129\n\34\3\35\3\35\3\35\3\35\5\35\u012f\n")
        buf.write("\35\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\7\37")
        buf.write("\u013a\n\37\f\37\16\37\u013d\13\37\3 \3 \3!\3!\3!\3!\3")
        buf.write("!\3!\3!\7!\u0148\n!\f!\16!\u014b\13!\3\"\3\"\3#\3#\3#")
        buf.write("\3#\3#\3#\3#\7#\u0156\n#\f#\16#\u0159\13#\3$\3$\3%\3%")
        buf.write("\3%\5%\u0160\n%\3%\5%\u0163\n%\3&\3&\3\'\3\'\3\'\5\'\u016a")
        buf.write("\n\'\3\'\5\'\u016d\n\'\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write(")\3)\3)\3)\5)\u017d\n)\3*\3*\3*\3*\3+\3+\3+\7+\u0186\n")
        buf.write("+\f+\16+\u0189\13+\3,\3,\3,\3,\3,\3,\3,\3-\3-\3-\7-\u0195")
        buf.write("\n-\f-\16-\u0198\13-\3.\3.\3.\2\5<@D/\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJL")
        buf.write("NPRTVXZ\2\7\3\2!&\3\2\37 \3\2\31\32\3\2\33\35\3\2\3\6")
        buf.write("\2\u01a0\2a\3\2\2\2\4f\3\2\2\2\6n\3\2\2\2\b\u0082\3\2")
        buf.write("\2\2\n\u0084\3\2\2\2\f\u008b\3\2\2\2\16\u008d\3\2\2\2")
        buf.write("\20\u0096\3\2\2\2\22\u00a2\3\2\2\2\24\u00a8\3\2\2\2\26")
        buf.write("\u00b0\3\2\2\2\30\u00b3\3\2\2\2\32\u00b6\3\2\2\2\34\u00bc")
        buf.write("\3\2\2\2\36\u00bf\3\2\2\2 \u00d6\3\2\2\2\"\u00d8\3\2\2")
        buf.write("\2$\u00e2\3\2\2\2&\u00e4\3\2\2\2(\u00ed\3\2\2\2*\u00f6")
        buf.write("\3\2\2\2,\u00f9\3\2\2\2.\u0107\3\2\2\2\60\u0109\3\2\2")
        buf.write("\2\62\u0113\3\2\2\2\64\u011d\3\2\2\2\66\u0125\3\2\2\2")
        buf.write("8\u012a\3\2\2\2:\u0130\3\2\2\2<\u0132\3\2\2\2>\u013e\3")
        buf.write("\2\2\2@\u0140\3\2\2\2B\u014c\3\2\2\2D\u014e\3\2\2\2F\u015a")
        buf.write("\3\2\2\2H\u0162\3\2\2\2J\u0164\3\2\2\2L\u016c\3\2\2\2")
        buf.write("N\u016e\3\2\2\2P\u017c\3\2\2\2R\u017e\3\2\2\2T\u0182\3")
        buf.write("\2\2\2V\u018a\3\2\2\2X\u0191\3\2\2\2Z\u0199\3\2\2\2\\")
        buf.write("`\5 \21\2]`\5*\26\2^`\5\4\3\2_\\\3\2\2\2_]\3\2\2\2_^\3")
        buf.write("\2\2\2`c\3\2\2\2a_\3\2\2\2ab\3\2\2\2bd\3\2\2\2ca\3\2\2")
        buf.write("\2de\7\2\2\3e\3\3\2\2\2fg\7(\2\2gh\7\25\2\2hi\7\61\2\2")
        buf.write("ij\7\b\2\2jk\7\16\2\2kl\7\17\2\2lm\5\6\4\2m\5\3\2\2\2")
        buf.write("ns\7\26\2\2or\5\b\5\2pr\5 \21\2qo\3\2\2\2qp\3\2\2\2ru")
        buf.write("\3\2\2\2sq\3\2\2\2st\3\2\2\2tv\3\2\2\2us\3\2\2\2vw\7\27")
        buf.write("\2\2w\7\3\2\2\2x\u0083\5\n\6\2y\u0083\5\16\b\2z\u0083")
        buf.write("\5\20\t\2{\u0083\5\22\n\2|\u0083\5\24\13\2}\u0083\5\26")
        buf.write("\f\2~\u0083\5\30\r\2\177\u0083\5\32\16\2\u0080\u0083\5")
        buf.write("\34\17\2\u0081\u0083\5\36\20\2\u0082x\3\2\2\2\u0082y\3")
        buf.write("\2\2\2\u0082z\3\2\2\2\u0082{\3\2\2\2\u0082|\3\2\2\2\u0082")
        buf.write("}\3\2\2\2\u0082~\3\2\2\2\u0082\177\3\2\2\2\u0082\u0080")
        buf.write("\3\2\2\2\u0082\u0081\3\2\2\2\u0083\t\3\2\2\2\u0084\u0085")
        buf.write("\5\f\7\2\u0085\u0086\7\30\2\2\u0086\u0087\5\66\34\2\u0087")
        buf.write("\u0088\7\24\2\2\u0088\13\3\2\2\2\u0089\u008c\7@\2\2\u008a")
        buf.write("\u008c\5P)\2\u008b\u0089\3\2\2\2\u008b\u008a\3\2\2\2\u008c")
        buf.write("\r\3\2\2\2\u008d\u008e\7\62\2\2\u008e\u008f\7\16\2\2\u008f")
        buf.write("\u0090\5\66\34\2\u0090\u0091\7\17\2\2\u0091\u0094\5\b")
        buf.write("\5\2\u0092\u0093\7-\2\2\u0093\u0095\5\b\5\2\u0094\u0092")
        buf.write("\3\2\2\2\u0094\u0095\3\2\2\2\u0095\17\3\2\2\2\u0096\u0097")
        buf.write("\7\60\2\2\u0097\u0098\7\16\2\2\u0098\u0099\7@\2\2\u0099")
        buf.write("\u009a\7\30\2\2\u009a\u009b\5\66\34\2\u009b\u009c\7\23")
        buf.write("\2\2\u009c\u009d\5\66\34\2\u009d\u009e\7\23\2\2\u009e")
        buf.write("\u009f\5\66\34\2\u009f\u00a0\7\17\2\2\u00a0\u00a1\5\b")
        buf.write("\5\2\u00a1\21\3\2\2\2\u00a2\u00a3\78\2\2\u00a3\u00a4\7")
        buf.write("\16\2\2\u00a4\u00a5\5\66\34\2\u00a5\u00a6\7\17\2\2\u00a6")
        buf.write("\u00a7\5\b\5\2\u00a7\23\3\2\2\2\u00a8\u00a9\7,\2\2\u00a9")
        buf.write("\u00aa\5\36\20\2\u00aa\u00ab\78\2\2\u00ab\u00ac\7\16\2")
        buf.write("\2\u00ac\u00ad\5\66\34\2\u00ad\u00ae\7\17\2\2\u00ae\u00af")
        buf.write("\7\24\2\2\u00af\25\3\2\2\2\u00b0\u00b1\7*\2\2\u00b1\u00b2")
        buf.write("\7\24\2\2\u00b2\27\3\2\2\2\u00b3\u00b4\7<\2\2\u00b4\u00b5")
        buf.write("\7\24\2\2\u00b5\31\3\2\2\2\u00b6\u00b8\7\65\2\2\u00b7")
        buf.write("\u00b9\5\66\34\2\u00b8\u00b7\3\2\2\2\u00b8\u00b9\3\2\2")
        buf.write("\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb\7\24\2\2\u00bb\33\3")
        buf.write("\2\2\2\u00bc\u00bd\5\62\32\2\u00bd\u00be\7\24\2\2\u00be")
        buf.write("\35\3\2\2\2\u00bf\u00c4\7\26\2\2\u00c0\u00c3\5\b\5\2\u00c1")
        buf.write("\u00c3\5 \21\2\u00c2\u00c0\3\2\2\2\u00c2\u00c1\3\2\2\2")
        buf.write("\u00c3\u00c6\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c4\u00c5\3")
        buf.write("\2\2\2\u00c5\u00c7\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c7\u00c8")
        buf.write("\7\27\2\2\u00c8\37\3\2\2\2\u00c9\u00ca\5\"\22\2\u00ca")
        buf.write("\u00cb\7\25\2\2\u00cb\u00cc\5$\23\2\u00cc\u00cd\7\30\2")
        buf.write("\2\u00cd\u00ce\5T+\2\u00ce\u00cf\7\24\2\2\u00cf\u00d0")
        buf.write("\b\21\1\2\u00d0\u00d7\3\2\2\2\u00d1\u00d2\5\"\22\2\u00d2")
        buf.write("\u00d3\7\25\2\2\u00d3\u00d4\5Z.\2\u00d4\u00d5\7\24\2\2")
        buf.write("\u00d5\u00d7\3\2\2\2\u00d6\u00c9\3\2\2\2\u00d6\u00d1\3")
        buf.write("\2\2\2\u00d7!\3\2\2\2\u00d8\u00dd\7@\2\2\u00d9\u00da\7")
        buf.write("\23\2\2\u00da\u00dc\7@\2\2\u00db\u00d9\3\2\2\2\u00dc\u00df")
        buf.write("\3\2\2\2\u00dd\u00db\3\2\2\2\u00dd\u00de\3\2\2\2\u00de")
        buf.write("#\3\2\2\2\u00df\u00dd\3\2\2\2\u00e0\u00e3\5Z.\2\u00e1")
        buf.write("\u00e3\7\t\2\2\u00e2\u00e0\3\2\2\2\u00e2\u00e1\3\2\2\2")
        buf.write("\u00e3%\3\2\2\2\u00e4\u00e9\5(\25\2\u00e5\u00e6\7\23\2")
        buf.write("\2\u00e6\u00e8\5(\25\2\u00e7\u00e5\3\2\2\2\u00e8\u00eb")
        buf.write("\3\2\2\2\u00e9\u00e7\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea")
        buf.write("\'\3\2\2\2\u00eb\u00e9\3\2\2\2\u00ec\u00ee\7>\2\2\u00ed")
        buf.write("\u00ec\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\u00f0\3\2\2\2")
        buf.write("\u00ef\u00f1\7;\2\2\u00f0\u00ef\3\2\2\2\u00f0\u00f1\3")
        buf.write("\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f3\7@\2\2\u00f3\u00f4")
        buf.write("\7\25\2\2\u00f4\u00f5\5Z.\2\u00f5)\3\2\2\2\u00f6\u00f7")
        buf.write("\5,\27\2\u00f7\u00f8\5\60\31\2\u00f8+\3\2\2\2\u00f9\u00fa")
        buf.write("\7@\2\2\u00fa\u00fb\7\25\2\2\u00fb\u00fc\7\61\2\2\u00fc")
        buf.write("\u00fd\5.\30\2\u00fd\u00fe\7\16\2\2\u00fe\u00ff\5&\24")
        buf.write("\2\u00ff\u0102\7\17\2\2\u0100\u0101\7>\2\2\u0101\u0103")
        buf.write("\7@\2\2\u0102\u0100\3\2\2\2\u0102\u0103\3\2\2\2\u0103")
        buf.write("-\3\2\2\2\u0104\u0108\5Z.\2\u0105\u0108\7\b\2\2\u0106")
        buf.write("\u0108\7\t\2\2\u0107\u0104\3\2\2\2\u0107\u0105\3\2\2\2")
        buf.write("\u0107\u0106\3\2\2\2\u0108/\3\2\2\2\u0109\u010e\7\26\2")
        buf.write("\2\u010a\u010d\5\b\5\2\u010b\u010d\5 \21\2\u010c\u010a")
        buf.write("\3\2\2\2\u010c\u010b\3\2\2\2\u010d\u0110\3\2\2\2\u010e")
        buf.write("\u010c\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u0111\3\2\2\2")
        buf.write("\u0110\u010e\3\2\2\2\u0111\u0112\7\27\2\2\u0112\61\3\2")
        buf.write("\2\2\u0113\u0114\7@\2\2\u0114\u0118\7\16\2\2\u0115\u0117")
        buf.write("\5\64\33\2\u0116\u0115\3\2\2\2\u0117\u011a\3\2\2\2\u0118")
        buf.write("\u0116\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u011b\3\2\2\2")
        buf.write("\u011a\u0118\3\2\2\2\u011b\u011c\7\17\2\2\u011c\63\3\2")
        buf.write("\2\2\u011d\u0122\5\66\34\2\u011e\u011f\7\23\2\2\u011f")
        buf.write("\u0121\5\66\34\2\u0120\u011e\3\2\2\2\u0121\u0124\3\2\2")
        buf.write("\2\u0122\u0120\3\2\2\2\u0122\u0123\3\2\2\2\u0123\65\3")
        buf.write("\2\2\2\u0124\u0122\3\2\2\2\u0125\u0128\58\35\2\u0126\u0127")
        buf.write("\7\'\2\2\u0127\u0129\58\35\2\u0128\u0126\3\2\2\2\u0128")
        buf.write("\u0129\3\2\2\2\u0129\67\3\2\2\2\u012a\u012e\5<\37\2\u012b")
        buf.write("\u012c\5:\36\2\u012c\u012d\5<\37\2\u012d\u012f\3\2\2\2")
        buf.write("\u012e\u012b\3\2\2\2\u012e\u012f\3\2\2\2\u012f9\3\2\2")
        buf.write("\2\u0130\u0131\t\2\2\2\u0131;\3\2\2\2\u0132\u0133\b\37")
        buf.write("\1\2\u0133\u0134\5@!\2\u0134\u013b\3\2\2\2\u0135\u0136")
        buf.write("\f\4\2\2\u0136\u0137\5> \2\u0137\u0138\5@!\2\u0138\u013a")
        buf.write("\3\2\2\2\u0139\u0135\3\2\2\2\u013a\u013d\3\2\2\2\u013b")
        buf.write("\u0139\3\2\2\2\u013b\u013c\3\2\2\2\u013c=\3\2\2\2\u013d")
        buf.write("\u013b\3\2\2\2\u013e\u013f\t\3\2\2\u013f?\3\2\2\2\u0140")
        buf.write("\u0141\b!\1\2\u0141\u0142\5D#\2\u0142\u0149\3\2\2\2\u0143")
        buf.write("\u0144\f\4\2\2\u0144\u0145\5B\"\2\u0145\u0146\5D#\2\u0146")
        buf.write("\u0148\3\2\2\2\u0147\u0143\3\2\2\2\u0148\u014b\3\2\2\2")
        buf.write("\u0149\u0147\3\2\2\2\u0149\u014a\3\2\2\2\u014aA\3\2\2")
        buf.write("\2\u014b\u0149\3\2\2\2\u014c\u014d\t\4\2\2\u014dC\3\2")
        buf.write("\2\2\u014e\u014f\b#\1\2\u014f\u0150\5H%\2\u0150\u0157")
        buf.write("\3\2\2\2\u0151\u0152\f\4\2\2\u0152\u0153\5F$\2\u0153\u0154")
        buf.write("\5H%\2\u0154\u0156\3\2\2\2\u0155\u0151\3\2\2\2\u0156\u0159")
        buf.write("\3\2\2\2\u0157\u0155\3\2\2\2\u0157\u0158\3\2\2\2\u0158")
        buf.write("E\3\2\2\2\u0159\u0157\3\2\2\2\u015a\u015b\t\5\2\2\u015b")
        buf.write("G\3\2\2\2\u015c\u015f\5J&\2\u015d\u0160\5H%\2\u015e\u0160")
        buf.write("\5L\'\2\u015f\u015d\3\2\2\2\u015f\u015e\3\2\2\2\u0160")
        buf.write("\u0163\3\2\2\2\u0161\u0163\5L\'\2\u0162\u015c\3\2\2\2")
        buf.write("\u0162\u0161\3\2\2\2\u0163I\3\2\2\2\u0164\u0165\7\36\2")
        buf.write("\2\u0165K\3\2\2\2\u0166\u0169\5N(\2\u0167\u016a\5P)\2")
        buf.write("\u0168\u016a\5L\'\2\u0169\u0167\3\2\2\2\u0169\u0168\3")
        buf.write("\2\2\2\u016a\u016d\3\2\2\2\u016b\u016d\5P)\2\u016c\u0166")
        buf.write("\3\2\2\2\u016c\u016b\3\2\2\2\u016dM\3\2\2\2\u016e\u016f")
        buf.write("\7\32\2\2\u016fO\3\2\2\2\u0170\u0171\7@\2\2\u0171\u0172")
        buf.write("\7\20\2\2\u0172\u0173\5T+\2\u0173\u0174\7\21\2\2\u0174")
        buf.write("\u017d\3\2\2\2\u0175\u017d\7@\2\2\u0176\u017d\7\f\2\2")
        buf.write("\u0177\u017d\7\n\2\2\u0178\u017d\7\13\2\2\u0179\u017d")
        buf.write("\7\r\2\2\u017a\u017d\5R*\2\u017b\u017d\5\62\32\2\u017c")
        buf.write("\u0170\3\2\2\2\u017c\u0175\3\2\2\2\u017c\u0176\3\2\2\2")
        buf.write("\u017c\u0177\3\2\2\2\u017c\u0178\3\2\2\2\u017c\u0179\3")
        buf.write("\2\2\2\u017c\u017a\3\2\2\2\u017c\u017b\3\2\2\2\u017dQ")
        buf.write("\3\2\2\2\u017e\u017f\7\26\2\2\u017f\u0180\5T+\2\u0180")
        buf.write("\u0181\7\27\2\2\u0181S\3\2\2\2\u0182\u0187\5\66\34\2\u0183")
        buf.write("\u0184\7\23\2\2\u0184\u0186\5\66\34\2\u0185\u0183\3\2")
        buf.write("\2\2\u0186\u0189\3\2\2\2\u0187\u0185\3\2\2\2\u0187\u0188")
        buf.write("\3\2\2\2\u0188U\3\2\2\2\u0189\u0187\3\2\2\2\u018a\u018b")
        buf.write("\7\7\2\2\u018b\u018c\7\20\2\2\u018c\u018d\5X-\2\u018d")
        buf.write("\u018e\7\21\2\2\u018e\u018f\7=\2\2\u018f\u0190\5Z.\2\u0190")
        buf.write("W\3\2\2\2\u0191\u0196\7\n\2\2\u0192\u0193\7\23\2\2\u0193")
        buf.write("\u0195\7\n\2\2\u0194\u0192\3\2\2\2\u0195\u0198\3\2\2\2")
        buf.write("\u0196\u0194\3\2\2\2\u0196\u0197\3\2\2\2\u0197Y\3\2\2")
        buf.write("\2\u0198\u0196\3\2\2\2\u0199\u019a\t\6\2\2\u019a[\3\2")
        buf.write("\2\2$_aqs\u0082\u008b\u0094\u00b8\u00c2\u00c4\u00d6\u00dd")
        buf.write("\u00e2\u00e9\u00ed\u00f0\u0102\u0107\u010c\u010e\u0118")
        buf.write("\u0122\u0128\u012e\u013b\u0149\u0157\u015f\u0162\u0169")
        buf.write("\u016c\u017c\u0187\u0196")
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
                     "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", 
                     "'<='", "'>='", "'::'", "'main'", "'auto'", "'break'", 
                     "'boolean'", "'do'", "'else'", "'false'", "'float'", 
                     "'for'", "'function'", "'if'", "'integer'", "'int'", 
                     "'return'", "'string'", "'true'", "'while'", "'void'", 
                     "'in'", "'out'", "'continue'", "'of'", "'inherit'", 
                     "'array'" ]

    symbolicNames = [ "<INVALID>", "StringType", "IntegerType", "FloatType", 
                      "BooleanType", "ArrayType", "VoidType", "AutoType", 
                      "INTLIT", "FLOATLIT", "BOOLLIT", "STRINGLIT", "LP", 
                      "RP", "LSB", "RSB", "DOT", "CM", "SM", "COLON", "LCB", 
                      "RCB", "ASSIGN", "ADD", "SUB", "MUL", "DIV", "MOD", 
                      "NOT", "ANDAND", "OROR", "EQ", "INEQ", "LT", "GT", 
                      "LE", "GE", "SRO", "MAIN", "AUTO", "BREAK", "BOOLEAN", 
                      "DO", "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", 
                      "IF", "INTEGER", "INT", "RETURN", "STRING", "TRUE", 
                      "WHILE", "VOID", "IN", "OUT", "CONTINUE", "OF", "INHERIT", 
                      "ARRAY", "ID", "BlockComment", "LineComment", "WS", 
                      "UNCLOSE_STRING", "ERROR_CHAR", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_func_main = 1
    RULE_main_return = 2
    RULE_stmt = 3
    RULE_assign_stmt = 4
    RULE_lhs = 5
    RULE_if_stmt = 6
    RULE_for_stmt = 7
    RULE_while_stmt = 8
    RULE_do_while_stmt = 9
    RULE_break_stmt = 10
    RULE_continue_stmt = 11
    RULE_return_stmt = 12
    RULE_call_stmt = 13
    RULE_block_stmt = 14
    RULE_variable_decl = 15
    RULE_identifier_lst = 16
    RULE_valid_type = 17
    RULE_para_lst_decl = 18
    RULE_para_decl = 19
    RULE_func_decl = 20
    RULE_func_prototype = 21
    RULE_func_return_type = 22
    RULE_func_body = 23
    RULE_func_call = 24
    RULE_arg_lst = 25
    RULE_expression = 26
    RULE_relation_expr = 27
    RULE_relation_op = 28
    RULE_logical_expr = 29
    RULE_logical_op = 30
    RULE_adding_expr = 31
    RULE_adding_op = 32
    RULE_multiplying_expr = 33
    RULE_multiplying_op = 34
    RULE_unary_logical_expr = 35
    RULE_unary_logical_op = 36
    RULE_sign_expr = 37
    RULE_sign_op = 38
    RULE_index_expr = 39
    RULE_arrayL = 40
    RULE_expr_lst = 41
    RULE_array_decl = 42
    RULE_integer_lst = 43
    RULE_atomic_type = 44

    ruleNames =  [ "program", "func_main", "main_return", "stmt", "assign_stmt", 
                   "lhs", "if_stmt", "for_stmt", "while_stmt", "do_while_stmt", 
                   "break_stmt", "continue_stmt", "return_stmt", "call_stmt", 
                   "block_stmt", "variable_decl", "identifier_lst", "valid_type", 
                   "para_lst_decl", "para_decl", "func_decl", "func_prototype", 
                   "func_return_type", "func_body", "func_call", "arg_lst", 
                   "expression", "relation_expr", "relation_op", "logical_expr", 
                   "logical_op", "adding_expr", "adding_op", "multiplying_expr", 
                   "multiplying_op", "unary_logical_expr", "unary_logical_op", 
                   "sign_expr", "sign_op", "index_expr", "arrayL", "expr_lst", 
                   "array_decl", "integer_lst", "atomic_type" ]

    EOF = Token.EOF
    StringType=1
    IntegerType=2
    FloatType=3
    BooleanType=4
    ArrayType=5
    VoidType=6
    AutoType=7
    INTLIT=8
    FLOATLIT=9
    BOOLLIT=10
    STRINGLIT=11
    LP=12
    RP=13
    LSB=14
    RSB=15
    DOT=16
    CM=17
    SM=18
    COLON=19
    LCB=20
    RCB=21
    ASSIGN=22
    ADD=23
    SUB=24
    MUL=25
    DIV=26
    MOD=27
    NOT=28
    ANDAND=29
    OROR=30
    EQ=31
    INEQ=32
    LT=33
    GT=34
    LE=35
    GE=36
    SRO=37
    MAIN=38
    AUTO=39
    BREAK=40
    BOOLEAN=41
    DO=42
    ELSE=43
    FALSE=44
    FLOAT=45
    FOR=46
    FUNCTION=47
    IF=48
    INTEGER=49
    INT=50
    RETURN=51
    STRING=52
    TRUE=53
    WHILE=54
    VOID=55
    IN=56
    OUT=57
    CONTINUE=58
    OF=59
    INHERIT=60
    ARRAY=61
    ID=62
    BlockComment=63
    LineComment=64
    WS=65
    UNCLOSE_STRING=66
    ERROR_CHAR=67
    ILLEGAL_ESCAPE=68

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
            while _la==MT22Parser.MAIN or _la==MT22Parser.ID:
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

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

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
            self.match(MT22Parser.LP)
            self.state = 105
            self.match(MT22Parser.RP)
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

        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

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
            self.match(MT22Parser.LCB)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.INTLIT) | (1 << MT22Parser.FLOATLIT) | (1 << MT22Parser.BOOLLIT) | (1 << MT22Parser.STRINGLIT) | (1 << MT22Parser.LCB) | (1 << MT22Parser.BREAK) | (1 << MT22Parser.DO) | (1 << MT22Parser.FOR) | (1 << MT22Parser.IF) | (1 << MT22Parser.RETURN) | (1 << MT22Parser.WHILE) | (1 << MT22Parser.CONTINUE) | (1 << MT22Parser.ID))) != 0):
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
            self.match(MT22Parser.RCB)
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
        self.enterRule(localctx, 6, self.RULE_stmt)
        try:
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 120
                self.for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 121
                self.while_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 122
                self.do_while_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 123
                self.break_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 124
                self.continue_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 125
                self.return_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 126
                self.call_stmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 127
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


        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def SM(self):
            return self.getToken(MT22Parser.SM, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = MT22Parser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.lhs()
            self.state = 131
            self.match(MT22Parser.ASSIGN)
            self.state = 132
            self.expression()
            self.state = 133
            self.match(MT22Parser.SM)
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

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

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
        self.enterRule(localctx, 10, self.RULE_lhs)
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.match(MT22Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
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

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

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
        self.enterRule(localctx, 12, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(MT22Parser.IF)
            self.state = 140
            self.match(MT22Parser.LP)
            self.state = 141
            self.expression()
            self.state = 142
            self.match(MT22Parser.RP)
            self.state = 143
            self.stmt()
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 144
                self.match(MT22Parser.ELSE)
                self.state = 145
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

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExpressionContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.CM)
            else:
                return self.getToken(MT22Parser.CM, i)

        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

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
        self.enterRule(localctx, 14, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(MT22Parser.FOR)
            self.state = 149
            self.match(MT22Parser.LP)
            self.state = 150
            self.match(MT22Parser.ID)
            self.state = 151
            self.match(MT22Parser.ASSIGN)
            self.state = 152
            self.expression()
            self.state = 153
            self.match(MT22Parser.CM)
            self.state = 154
            self.expression()
            self.state = 155
            self.match(MT22Parser.CM)
            self.state = 156
            self.expression()
            self.state = 157
            self.match(MT22Parser.RP)
            self.state = 158
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

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

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
        self.enterRule(localctx, 16, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(MT22Parser.WHILE)
            self.state = 161
            self.match(MT22Parser.LP)
            self.state = 162
            self.expression()
            self.state = 163
            self.match(MT22Parser.RP)
            self.state = 164
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

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def SM(self):
            return self.getToken(MT22Parser.SM, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_do_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_while_stmt" ):
                return visitor.visitDo_while_stmt(self)
            else:
                return visitor.visitChildren(self)




    def do_while_stmt(self):

        localctx = MT22Parser.Do_while_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_do_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(MT22Parser.DO)
            self.state = 167
            self.block_stmt()
            self.state = 168
            self.match(MT22Parser.WHILE)
            self.state = 169
            self.match(MT22Parser.LP)
            self.state = 170
            self.expression()
            self.state = 171
            self.match(MT22Parser.RP)
            self.state = 172
            self.match(MT22Parser.SM)
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

        def SM(self):
            return self.getToken(MT22Parser.SM, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = MT22Parser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(MT22Parser.BREAK)
            self.state = 175
            self.match(MT22Parser.SM)
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

        def SM(self):
            return self.getToken(MT22Parser.SM, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = MT22Parser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(MT22Parser.CONTINUE)
            self.state = 178
            self.match(MT22Parser.SM)
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

        def SM(self):
            return self.getToken(MT22Parser.SM, 0)

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
        self.enterRule(localctx, 24, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(MT22Parser.RETURN)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.INTLIT) | (1 << MT22Parser.FLOATLIT) | (1 << MT22Parser.BOOLLIT) | (1 << MT22Parser.STRINGLIT) | (1 << MT22Parser.LCB) | (1 << MT22Parser.SUB) | (1 << MT22Parser.NOT) | (1 << MT22Parser.ID))) != 0):
                self.state = 181
                self.expression()


            self.state = 184
            self.match(MT22Parser.SM)
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


        def SM(self):
            return self.getToken(MT22Parser.SM, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = MT22Parser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.func_call()
            self.state = 187
            self.match(MT22Parser.SM)
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

        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

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
        self.enterRule(localctx, 28, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(MT22Parser.LCB)
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.INTLIT) | (1 << MT22Parser.FLOATLIT) | (1 << MT22Parser.BOOLLIT) | (1 << MT22Parser.STRINGLIT) | (1 << MT22Parser.LCB) | (1 << MT22Parser.BREAK) | (1 << MT22Parser.DO) | (1 << MT22Parser.FOR) | (1 << MT22Parser.IF) | (1 << MT22Parser.RETURN) | (1 << MT22Parser.WHILE) | (1 << MT22Parser.CONTINUE) | (1 << MT22Parser.ID))) != 0):
                self.state = 192
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 190
                    self.stmt()
                    pass

                elif la_ == 2:
                    self.state = 191
                    self.variable_decl()
                    pass


                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 197
            self.match(MT22Parser.RCB)
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
            self.l = None # Identifier_lstContext
            self.r = None # Expr_lstContext
            self.e = None # Token

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def valid_type(self):
            return self.getTypedRuleContext(MT22Parser.Valid_typeContext,0)


        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def identifier_lst(self):
            return self.getTypedRuleContext(MT22Parser.Identifier_lstContext,0)


        def expr_lst(self):
            return self.getTypedRuleContext(MT22Parser.Expr_lstContext,0)


        def SM(self):
            return self.getToken(MT22Parser.SM, 0)

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
        self.enterRule(localctx, 30, self.RULE_variable_decl)
        try:
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                localctx.l = self.identifier_lst()
                self.state = 200
                self.match(MT22Parser.COLON)
                self.state = 201
                self.valid_type()
                self.state = 202
                self.match(MT22Parser.ASSIGN)
                self.state = 203
                localctx.r = self.expr_lst()
                self.state = 204
                localctx.e = self.match(MT22Parser.SM)
                if len((None if localctx.l is None else self._input.getText(localctx.l.start,localctx.l.stop)).split(',')) != len((None if localctx.r is None else self._input.getText(localctx.r.start,localctx.r.stop)).split(',')):
                        raise Exception('Error on line {} col {}: ;'.format((0 if localctx.e is None else localctx.e.line), (0 if localctx.e is None else localctx.e.column)))
                    
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self.identifier_lst()
                self.state = 208
                self.match(MT22Parser.COLON)
                self.state = 209
                self.atomic_type()
                self.state = 210
                self.match(MT22Parser.SM)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Identifier_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.ID)
            else:
                return self.getToken(MT22Parser.ID, i)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.CM)
            else:
                return self.getToken(MT22Parser.CM, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_identifier_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier_lst" ):
                return visitor.visitIdentifier_lst(self)
            else:
                return visitor.visitChildren(self)




    def identifier_lst(self):

        localctx = MT22Parser.Identifier_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_identifier_lst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(MT22Parser.ID)
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.CM:
                self.state = 215
                self.match(MT22Parser.CM)
                self.state = 216
                self.match(MT22Parser.ID)
                self.state = 221
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
        self.enterRule(localctx, 34, self.RULE_valid_type)
        try:
            self.state = 224
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.StringType, MT22Parser.IntegerType, MT22Parser.FloatType, MT22Parser.BooleanType]:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.atomic_type()
                pass
            elif token in [MT22Parser.AutoType]:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
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


    class Para_lst_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Para_declContext)
            else:
                return self.getTypedRuleContext(MT22Parser.Para_declContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.CM)
            else:
                return self.getToken(MT22Parser.CM, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_para_lst_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_lst_decl" ):
                return visitor.visitPara_lst_decl(self)
            else:
                return visitor.visitChildren(self)




    def para_lst_decl(self):

        localctx = MT22Parser.Para_lst_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_para_lst_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.para_decl()
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.CM:
                self.state = 227
                self.match(MT22Parser.CM)
                self.state = 228
                self.para_decl()
                self.state = 233
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

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

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
        self.enterRule(localctx, 38, self.RULE_para_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 234
                self.match(MT22Parser.INHERIT)


            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.OUT:
                self.state = 237
                self.match(MT22Parser.OUT)


            self.state = 240
            self.match(MT22Parser.ID)
            self.state = 241
            self.match(MT22Parser.COLON)
            self.state = 242
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
        self.enterRule(localctx, 40, self.RULE_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.func_prototype()
            self.state = 245
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.ID)
            else:
                return self.getToken(MT22Parser.ID, i)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def FUNCTION(self):
            return self.getToken(MT22Parser.FUNCTION, 0)

        def func_return_type(self):
            return self.getTypedRuleContext(MT22Parser.Func_return_typeContext,0)


        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def para_lst_decl(self):
            return self.getTypedRuleContext(MT22Parser.Para_lst_declContext,0)


        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

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
        self.enterRule(localctx, 42, self.RULE_func_prototype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(MT22Parser.ID)
            self.state = 248
            self.match(MT22Parser.COLON)
            self.state = 249
            self.match(MT22Parser.FUNCTION)
            self.state = 250
            self.func_return_type()
            self.state = 251
            self.match(MT22Parser.LP)
            self.state = 252
            self.para_lst_decl()
            self.state = 253
            self.match(MT22Parser.RP)
            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 254
                self.match(MT22Parser.INHERIT)
                self.state = 255
                self.match(MT22Parser.ID)


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
        self.enterRule(localctx, 44, self.RULE_func_return_type)
        try:
            self.state = 261
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.StringType, MT22Parser.IntegerType, MT22Parser.FloatType, MT22Parser.BooleanType]:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.atomic_type()
                pass
            elif token in [MT22Parser.VoidType]:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.match(MT22Parser.VoidType)
                pass
            elif token in [MT22Parser.AutoType]:
                self.enterOuterAlt(localctx, 3)
                self.state = 260
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

        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

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
        self.enterRule(localctx, 46, self.RULE_func_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(MT22Parser.LCB)
            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.INTLIT) | (1 << MT22Parser.FLOATLIT) | (1 << MT22Parser.BOOLLIT) | (1 << MT22Parser.STRINGLIT) | (1 << MT22Parser.LCB) | (1 << MT22Parser.BREAK) | (1 << MT22Parser.DO) | (1 << MT22Parser.FOR) | (1 << MT22Parser.IF) | (1 << MT22Parser.RETURN) | (1 << MT22Parser.WHILE) | (1 << MT22Parser.CONTINUE) | (1 << MT22Parser.ID))) != 0):
                self.state = 266
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 264
                    self.stmt()
                    pass

                elif la_ == 2:
                    self.state = 265
                    self.variable_decl()
                    pass


                self.state = 270
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 271
            self.match(MT22Parser.RCB)
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

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def arg_lst(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Arg_lstContext)
            else:
                return self.getTypedRuleContext(MT22Parser.Arg_lstContext,i)


        def getRuleIndex(self):
            return MT22Parser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = MT22Parser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(MT22Parser.ID)
            self.state = 274
            self.match(MT22Parser.LP)
            self.state = 278
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.INTLIT) | (1 << MT22Parser.FLOATLIT) | (1 << MT22Parser.BOOLLIT) | (1 << MT22Parser.STRINGLIT) | (1 << MT22Parser.LCB) | (1 << MT22Parser.SUB) | (1 << MT22Parser.NOT) | (1 << MT22Parser.ID))) != 0):
                self.state = 275
                self.arg_lst()
                self.state = 280
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 281
            self.match(MT22Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arg_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExpressionContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.CM)
            else:
                return self.getToken(MT22Parser.CM, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_arg_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg_lst" ):
                return visitor.visitArg_lst(self)
            else:
                return visitor.visitChildren(self)




    def arg_lst(self):

        localctx = MT22Parser.Arg_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_arg_lst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.expression()
            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.CM:
                self.state = 284
                self.match(MT22Parser.CM)
                self.state = 285
                self.expression()
                self.state = 290
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


        def SRO(self):
            return self.getToken(MT22Parser.SRO, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = MT22Parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.relation_expr()
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.SRO:
                self.state = 292
                self.match(MT22Parser.SRO)
                self.state = 293
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
        self.enterRule(localctx, 54, self.RULE_relation_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.logical_expr(0)
            self.state = 300
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.EQ) | (1 << MT22Parser.INEQ) | (1 << MT22Parser.LT) | (1 << MT22Parser.GT) | (1 << MT22Parser.LE) | (1 << MT22Parser.GE))) != 0):
                self.state = 297
                self.relation_op()
                self.state = 298
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

        def EQ(self):
            return self.getToken(MT22Parser.EQ, 0)

        def INEQ(self):
            return self.getToken(MT22Parser.INEQ, 0)

        def LT(self):
            return self.getToken(MT22Parser.LT, 0)

        def GT(self):
            return self.getToken(MT22Parser.GT, 0)

        def LE(self):
            return self.getToken(MT22Parser.LE, 0)

        def GE(self):
            return self.getToken(MT22Parser.GE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_relation_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelation_op" ):
                return visitor.visitRelation_op(self)
            else:
                return visitor.visitChildren(self)




    def relation_op(self):

        localctx = MT22Parser.Relation_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_relation_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.EQ) | (1 << MT22Parser.INEQ) | (1 << MT22Parser.LT) | (1 << MT22Parser.GT) | (1 << MT22Parser.LE) | (1 << MT22Parser.GE))) != 0)):
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
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_logical_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.adding_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 313
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Logical_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expr)
                    self.state = 307
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 308
                    self.logical_op()
                    self.state = 309
                    self.adding_expr(0) 
                self.state = 315
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
        self.enterRule(localctx, 60, self.RULE_logical_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
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
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_adding_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.multiplying_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 327
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Adding_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_adding_expr)
                    self.state = 321
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 322
                    self.adding_op()
                    self.state = 323
                    self.multiplying_expr(0) 
                self.state = 329
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

        def ADD(self):
            return self.getToken(MT22Parser.ADD, 0)

        def SUB(self):
            return self.getToken(MT22Parser.SUB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_adding_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdding_op" ):
                return visitor.visitAdding_op(self)
            else:
                return visitor.visitChildren(self)




    def adding_op(self):

        localctx = MT22Parser.Adding_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_adding_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            _la = self._input.LA(1)
            if not(_la==MT22Parser.ADD or _la==MT22Parser.SUB):
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
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_multiplying_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.unary_logical_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 341
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Multiplying_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplying_expr)
                    self.state = 335
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 336
                    self.multiplying_op()
                    self.state = 337
                    self.unary_logical_expr() 
                self.state = 343
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

        def MUL(self):
            return self.getToken(MT22Parser.MUL, 0)

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
        self.enterRule(localctx, 68, self.RULE_multiplying_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.MUL) | (1 << MT22Parser.DIV) | (1 << MT22Parser.MOD))) != 0)):
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
        self.enterRule(localctx, 70, self.RULE_unary_logical_expr)
        try:
            self.state = 352
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.unary_logical_op()
                self.state = 349
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                if la_ == 1:
                    self.state = 347
                    self.unary_logical_expr()
                    pass

                elif la_ == 2:
                    self.state = 348
                    self.sign_expr()
                    pass


                pass
            elif token in [MT22Parser.INTLIT, MT22Parser.FLOATLIT, MT22Parser.BOOLLIT, MT22Parser.STRINGLIT, MT22Parser.LCB, MT22Parser.SUB, MT22Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 351
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
        self.enterRule(localctx, 72, self.RULE_unary_logical_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
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
        self.enterRule(localctx, 74, self.RULE_sign_expr)
        try:
            self.state = 362
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.sign_op()
                self.state = 359
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                if la_ == 1:
                    self.state = 357
                    self.index_expr()
                    pass

                elif la_ == 2:
                    self.state = 358
                    self.sign_expr()
                    pass


                pass
            elif token in [MT22Parser.INTLIT, MT22Parser.FLOATLIT, MT22Parser.BOOLLIT, MT22Parser.STRINGLIT, MT22Parser.LCB, MT22Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 361
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

        def SUB(self):
            return self.getToken(MT22Parser.SUB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_sign_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign_op" ):
                return visitor.visitSign_op(self)
            else:
                return visitor.visitChildren(self)




    def sign_op(self):

        localctx = MT22Parser.Sign_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_sign_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.match(MT22Parser.SUB)
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

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def LSB(self):
            return self.getToken(MT22Parser.LSB, 0)

        def expr_lst(self):
            return self.getTypedRuleContext(MT22Parser.Expr_lstContext,0)


        def RSB(self):
            return self.getToken(MT22Parser.RSB, 0)

        def BOOLLIT(self):
            return self.getToken(MT22Parser.BOOLLIT, 0)

        def INTLIT(self):
            return self.getToken(MT22Parser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MT22Parser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MT22Parser.STRINGLIT, 0)

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
        self.enterRule(localctx, 78, self.RULE_index_expr)
        try:
            self.state = 378
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                self.match(MT22Parser.ID)
                self.state = 367
                self.match(MT22Parser.LSB)
                self.state = 368
                self.expr_lst()
                self.state = 369
                self.match(MT22Parser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 371
                self.match(MT22Parser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 372
                self.match(MT22Parser.BOOLLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 373
                self.match(MT22Parser.INTLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 374
                self.match(MT22Parser.FLOATLIT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 375
                self.match(MT22Parser.STRINGLIT)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 376
                self.arrayL()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 377
                self.func_call()
                pass


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

        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def expr_lst(self):
            return self.getTypedRuleContext(MT22Parser.Expr_lstContext,0)


        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_arrayL

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayL" ):
                return visitor.visitArrayL(self)
            else:
                return visitor.visitChildren(self)




    def arrayL(self):

        localctx = MT22Parser.ArrayLContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_arrayL)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.match(MT22Parser.LCB)
            self.state = 381
            self.expr_lst()
            self.state = 382
            self.match(MT22Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExpressionContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.CM)
            else:
                return self.getToken(MT22Parser.CM, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_lst" ):
                return visitor.visitExpr_lst(self)
            else:
                return visitor.visitChildren(self)




    def expr_lst(self):

        localctx = MT22Parser.Expr_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expr_lst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.expression()
            self.state = 389
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.CM:
                self.state = 385
                self.match(MT22Parser.CM)
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

        def LSB(self):
            return self.getToken(MT22Parser.LSB, 0)

        def integer_lst(self):
            return self.getTypedRuleContext(MT22Parser.Integer_lstContext,0)


        def RSB(self):
            return self.getToken(MT22Parser.RSB, 0)

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
            self.match(MT22Parser.LSB)
            self.state = 394
            self.integer_lst()
            self.state = 395
            self.match(MT22Parser.RSB)
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


    class Integer_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.INTLIT)
            else:
                return self.getToken(MT22Parser.INTLIT, i)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.CM)
            else:
                return self.getToken(MT22Parser.CM, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_integer_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteger_lst" ):
                return visitor.visitInteger_lst(self)
            else:
                return visitor.visitChildren(self)




    def integer_lst(self):

        localctx = MT22Parser.Integer_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_integer_lst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.match(MT22Parser.INTLIT)
            self.state = 404
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.CM:
                self.state = 400
                self.match(MT22Parser.CM)
                self.state = 401
                self.match(MT22Parser.INTLIT)
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
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.StringType) | (1 << MT22Parser.IntegerType) | (1 << MT22Parser.FloatType) | (1 << MT22Parser.BooleanType))) != 0)):
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
        self._predicates[29] = self.logical_expr_sempred
        self._predicates[31] = self.adding_expr_sempred
        self._predicates[33] = self.multiplying_expr_sempred
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
         




