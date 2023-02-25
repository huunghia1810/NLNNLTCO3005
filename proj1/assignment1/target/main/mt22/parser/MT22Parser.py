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
        buf.write("\u0199\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\7\17")
        buf.write("\u00bd\n\17\f\17\16\17\u00c0\13\17\3\17\3\17\3\20\3\20")
        buf.write("\5\20\u00c6\n\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00d7\n\21")
        buf.write("\3\22\3\22\3\22\7\22\u00dc\n\22\f\22\16\22\u00df\13\22")
        buf.write("\3\23\3\23\5\23\u00e3\n\23\3\24\3\24\3\24\7\24\u00e8\n")
        buf.write("\24\f\24\16\24\u00eb\13\24\3\25\5\25\u00ee\n\25\3\25\5")
        buf.write("\25\u00f1\n\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u0103\n")
        buf.write("\27\3\30\3\30\3\30\5\30\u0108\n\30\3\31\3\31\3\31\7\31")
        buf.write("\u010d\n\31\f\31\16\31\u0110\13\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\5\32\u0117\n\32\3\32\3\32\3\33\3\33\3\33\7\33\u011e")
        buf.write("\n\33\f\33\16\33\u0121\13\33\3\34\3\34\3\34\5\34\u0126")
        buf.write("\n\34\3\35\3\35\3\35\3\35\5\35\u012c\n\35\3\36\3\36\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\3\37\7\37\u0137\n\37\f\37")
        buf.write("\16\37\u013a\13\37\3 \3 \3!\3!\3!\3!\3!\3!\3!\7!\u0145")
        buf.write("\n!\f!\16!\u0148\13!\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\7#\u0153")
        buf.write("\n#\f#\16#\u0156\13#\3$\3$\3%\3%\3%\5%\u015d\n%\3%\5%")
        buf.write("\u0160\n%\3&\3&\3\'\3\'\3\'\5\'\u0167\n\'\3\'\5\'\u016a")
        buf.write("\n\'\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\5)\u017a")
        buf.write("\n)\3*\3*\3*\7*\u017f\n*\f*\16*\u0182\13*\3+\3+\3+\3+")
        buf.write("\3+\3+\3+\3,\3,\3,\7,\u018e\n,\f,\16,\u0191\13,\3-\3-")
        buf.write("\3.\3.\3.\3.\3.\2\5<@D/\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\2\7\3")
        buf.write("\2!&\3\2\37 \3\2\31\32\3\2\33\35\3\2\3\6\2\u019d\2a\3")
        buf.write("\2\2\2\4f\3\2\2\2\6n\3\2\2\2\b\u0082\3\2\2\2\n\u0084\3")
        buf.write("\2\2\2\f\u008b\3\2\2\2\16\u008d\3\2\2\2\20\u0096\3\2\2")
        buf.write("\2\22\u009c\3\2\2\2\24\u00a4\3\2\2\2\26\u00b0\3\2\2\2")
        buf.write("\30\u00b3\3\2\2\2\32\u00b6\3\2\2\2\34\u00b9\3\2\2\2\36")
        buf.write("\u00c3\3\2\2\2 \u00d6\3\2\2\2\"\u00d8\3\2\2\2$\u00e2\3")
        buf.write("\2\2\2&\u00e4\3\2\2\2(\u00ed\3\2\2\2*\u00f6\3\2\2\2,\u00f9")
        buf.write("\3\2\2\2.\u0107\3\2\2\2\60\u0109\3\2\2\2\62\u0113\3\2")
        buf.write("\2\2\64\u011a\3\2\2\2\66\u0122\3\2\2\28\u0127\3\2\2\2")
        buf.write(":\u012d\3\2\2\2<\u012f\3\2\2\2>\u013b\3\2\2\2@\u013d\3")
        buf.write("\2\2\2B\u0149\3\2\2\2D\u014b\3\2\2\2F\u0157\3\2\2\2H\u015f")
        buf.write("\3\2\2\2J\u0161\3\2\2\2L\u0169\3\2\2\2N\u016b\3\2\2\2")
        buf.write("P\u0179\3\2\2\2R\u017b\3\2\2\2T\u0183\3\2\2\2V\u018a\3")
        buf.write("\2\2\2X\u0192\3\2\2\2Z\u0194\3\2\2\2\\`\5 \21\2]`\5*\26")
        buf.write("\2^`\5\4\3\2_\\\3\2\2\2_]\3\2\2\2_^\3\2\2\2`c\3\2\2\2")
        buf.write("a_\3\2\2\2ab\3\2\2\2bd\3\2\2\2ca\3\2\2\2de\7\2\2\3e\3")
        buf.write("\3\2\2\2fg\7(\2\2gh\7\25\2\2hi\7\61\2\2ij\7\b\2\2jk\7")
        buf.write("\16\2\2kl\7\17\2\2lm\5\6\4\2m\5\3\2\2\2ns\7\26\2\2or\5")
        buf.write("\b\5\2pr\5 \21\2qo\3\2\2\2qp\3\2\2\2ru\3\2\2\2sq\3\2\2")
        buf.write("\2st\3\2\2\2tv\3\2\2\2us\3\2\2\2vw\7\27\2\2w\7\3\2\2\2")
        buf.write("x\u0083\5\n\6\2y\u0083\5\16\b\2z\u0083\5\20\t\2{\u0083")
        buf.write("\5\22\n\2|\u0083\5\24\13\2}\u0083\5\26\f\2~\u0083\5\30")
        buf.write("\r\2\177\u0083\5\32\16\2\u0080\u0083\5\34\17\2\u0081\u0083")
        buf.write("\5\36\20\2\u0082x\3\2\2\2\u0082y\3\2\2\2\u0082z\3\2\2")
        buf.write("\2\u0082{\3\2\2\2\u0082|\3\2\2\2\u0082}\3\2\2\2\u0082")
        buf.write("~\3\2\2\2\u0082\177\3\2\2\2\u0082\u0080\3\2\2\2\u0082")
        buf.write("\u0081\3\2\2\2\u0083\t\3\2\2\2\u0084\u0085\5\f\7\2\u0085")
        buf.write("\u0086\7\30\2\2\u0086\u0087\5\66\34\2\u0087\u0088\7\24")
        buf.write("\2\2\u0088\13\3\2\2\2\u0089\u008c\7@\2\2\u008a\u008c\5")
        buf.write("P)\2\u008b\u0089\3\2\2\2\u008b\u008a\3\2\2\2\u008c\r\3")
        buf.write("\2\2\2\u008d\u008e\7\62\2\2\u008e\u008f\7\16\2\2\u008f")
        buf.write("\u0090\5\66\34\2\u0090\u0091\7\17\2\2\u0091\u0094\5\b")
        buf.write("\5\2\u0092\u0093\7-\2\2\u0093\u0095\5\b\5\2\u0094\u0092")
        buf.write("\3\2\2\2\u0094\u0095\3\2\2\2\u0095\17\3\2\2\2\u0096\u0097")
        buf.write("\78\2\2\u0097\u0098\7\16\2\2\u0098\u0099\5\66\34\2\u0099")
        buf.write("\u009a\7\17\2\2\u009a\u009b\5\b\5\2\u009b\21\3\2\2\2\u009c")
        buf.write("\u009d\7,\2\2\u009d\u009e\5\34\17\2\u009e\u009f\78\2\2")
        buf.write("\u009f\u00a0\7\16\2\2\u00a0\u00a1\5\66\34\2\u00a1\u00a2")
        buf.write("\7\17\2\2\u00a2\u00a3\7\24\2\2\u00a3\23\3\2\2\2\u00a4")
        buf.write("\u00a5\7\60\2\2\u00a5\u00a6\7\16\2\2\u00a6\u00a7\7@\2")
        buf.write("\2\u00a7\u00a8\7\30\2\2\u00a8\u00a9\5\66\34\2\u00a9\u00aa")
        buf.write("\7\23\2\2\u00aa\u00ab\5\66\34\2\u00ab\u00ac\7\23\2\2\u00ac")
        buf.write("\u00ad\5\66\34\2\u00ad\u00ae\7\17\2\2\u00ae\u00af\5\b")
        buf.write("\5\2\u00af\25\3\2\2\2\u00b0\u00b1\7*\2\2\u00b1\u00b2\7")
        buf.write("\24\2\2\u00b2\27\3\2\2\2\u00b3\u00b4\7<\2\2\u00b4\u00b5")
        buf.write("\7\24\2\2\u00b5\31\3\2\2\2\u00b6\u00b7\5\62\32\2\u00b7")
        buf.write("\u00b8\7\24\2\2\u00b8\33\3\2\2\2\u00b9\u00be\7\26\2\2")
        buf.write("\u00ba\u00bd\5\b\5\2\u00bb\u00bd\5 \21\2\u00bc\u00ba\3")
        buf.write("\2\2\2\u00bc\u00bb\3\2\2\2\u00bd\u00c0\3\2\2\2\u00be\u00bc")
        buf.write("\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00c1\3\2\2\2\u00c0")
        buf.write("\u00be\3\2\2\2\u00c1\u00c2\7\27\2\2\u00c2\35\3\2\2\2\u00c3")
        buf.write("\u00c5\7\65\2\2\u00c4\u00c6\5\66\34\2\u00c5\u00c4\3\2")
        buf.write("\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c8")
        buf.write("\7\24\2\2\u00c8\37\3\2\2\2\u00c9\u00ca\5\"\22\2\u00ca")
        buf.write("\u00cb\7\25\2\2\u00cb\u00cc\5$\23\2\u00cc\u00cd\7\30\2")
        buf.write("\2\u00cd\u00ce\5R*\2\u00ce\u00cf\7\24\2\2\u00cf\u00d0")
        buf.write("\b\21\1\2\u00d0\u00d7\3\2\2\2\u00d1\u00d2\5\"\22\2\u00d2")
        buf.write("\u00d3\7\25\2\2\u00d3\u00d4\5X-\2\u00d4\u00d5\7\24\2\2")
        buf.write("\u00d5\u00d7\3\2\2\2\u00d6\u00c9\3\2\2\2\u00d6\u00d1\3")
        buf.write("\2\2\2\u00d7!\3\2\2\2\u00d8\u00dd\7@\2\2\u00d9\u00da\7")
        buf.write("\23\2\2\u00da\u00dc\7@\2\2\u00db\u00d9\3\2\2\2\u00dc\u00df")
        buf.write("\3\2\2\2\u00dd\u00db\3\2\2\2\u00dd\u00de\3\2\2\2\u00de")
        buf.write("#\3\2\2\2\u00df\u00dd\3\2\2\2\u00e0\u00e3\5X-\2\u00e1")
        buf.write("\u00e3\7\t\2\2\u00e2\u00e0\3\2\2\2\u00e2\u00e1\3\2\2\2")
        buf.write("\u00e3%\3\2\2\2\u00e4\u00e9\5(\25\2\u00e5\u00e6\7\23\2")
        buf.write("\2\u00e6\u00e8\5(\25\2\u00e7\u00e5\3\2\2\2\u00e8\u00eb")
        buf.write("\3\2\2\2\u00e9\u00e7\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea")
        buf.write("\'\3\2\2\2\u00eb\u00e9\3\2\2\2\u00ec\u00ee\7>\2\2\u00ed")
        buf.write("\u00ec\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\u00f0\3\2\2\2")
        buf.write("\u00ef\u00f1\7;\2\2\u00f0\u00ef\3\2\2\2\u00f0\u00f1\3")
        buf.write("\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f3\7@\2\2\u00f3\u00f4")
        buf.write("\7\25\2\2\u00f4\u00f5\5X-\2\u00f5)\3\2\2\2\u00f6\u00f7")
        buf.write("\5,\27\2\u00f7\u00f8\5\60\31\2\u00f8+\3\2\2\2\u00f9\u00fa")
        buf.write("\7@\2\2\u00fa\u00fb\7\25\2\2\u00fb\u00fc\7\61\2\2\u00fc")
        buf.write("\u00fd\5.\30\2\u00fd\u00fe\7\16\2\2\u00fe\u00ff\5&\24")
        buf.write("\2\u00ff\u0102\7\17\2\2\u0100\u0101\7>\2\2\u0101\u0103")
        buf.write("\7@\2\2\u0102\u0100\3\2\2\2\u0102\u0103\3\2\2\2\u0103")
        buf.write("-\3\2\2\2\u0104\u0108\5X-\2\u0105\u0108\7\b\2\2\u0106")
        buf.write("\u0108\7\t\2\2\u0107\u0104\3\2\2\2\u0107\u0105\3\2\2\2")
        buf.write("\u0107\u0106\3\2\2\2\u0108/\3\2\2\2\u0109\u010e\7\26\2")
        buf.write("\2\u010a\u010d\5\b\5\2\u010b\u010d\5 \21\2\u010c\u010a")
        buf.write("\3\2\2\2\u010c\u010b\3\2\2\2\u010d\u0110\3\2\2\2\u010e")
        buf.write("\u010c\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u0111\3\2\2\2")
        buf.write("\u0110\u010e\3\2\2\2\u0111\u0112\7\27\2\2\u0112\61\3\2")
        buf.write("\2\2\u0113\u0114\7@\2\2\u0114\u0116\7\16\2\2\u0115\u0117")
        buf.write("\5\64\33\2\u0116\u0115\3\2\2\2\u0116\u0117\3\2\2\2\u0117")
        buf.write("\u0118\3\2\2\2\u0118\u0119\7\17\2\2\u0119\63\3\2\2\2\u011a")
        buf.write("\u011f\5\66\34\2\u011b\u011c\7\23\2\2\u011c\u011e\5\66")
        buf.write("\34\2\u011d\u011b\3\2\2\2\u011e\u0121\3\2\2\2\u011f\u011d")
        buf.write("\3\2\2\2\u011f\u0120\3\2\2\2\u0120\65\3\2\2\2\u0121\u011f")
        buf.write("\3\2\2\2\u0122\u0125\58\35\2\u0123\u0124\7\'\2\2\u0124")
        buf.write("\u0126\58\35\2\u0125\u0123\3\2\2\2\u0125\u0126\3\2\2\2")
        buf.write("\u0126\67\3\2\2\2\u0127\u012b\5<\37\2\u0128\u0129\5:\36")
        buf.write("\2\u0129\u012a\5<\37\2\u012a\u012c\3\2\2\2\u012b\u0128")
        buf.write("\3\2\2\2\u012b\u012c\3\2\2\2\u012c9\3\2\2\2\u012d\u012e")
        buf.write("\t\2\2\2\u012e;\3\2\2\2\u012f\u0130\b\37\1\2\u0130\u0131")
        buf.write("\5@!\2\u0131\u0138\3\2\2\2\u0132\u0133\f\4\2\2\u0133\u0134")
        buf.write("\5> \2\u0134\u0135\5@!\2\u0135\u0137\3\2\2\2\u0136\u0132")
        buf.write("\3\2\2\2\u0137\u013a\3\2\2\2\u0138\u0136\3\2\2\2\u0138")
        buf.write("\u0139\3\2\2\2\u0139=\3\2\2\2\u013a\u0138\3\2\2\2\u013b")
        buf.write("\u013c\t\3\2\2\u013c?\3\2\2\2\u013d\u013e\b!\1\2\u013e")
        buf.write("\u013f\5D#\2\u013f\u0146\3\2\2\2\u0140\u0141\f\4\2\2\u0141")
        buf.write("\u0142\5B\"\2\u0142\u0143\5D#\2\u0143\u0145\3\2\2\2\u0144")
        buf.write("\u0140\3\2\2\2\u0145\u0148\3\2\2\2\u0146\u0144\3\2\2\2")
        buf.write("\u0146\u0147\3\2\2\2\u0147A\3\2\2\2\u0148\u0146\3\2\2")
        buf.write("\2\u0149\u014a\t\4\2\2\u014aC\3\2\2\2\u014b\u014c\b#\1")
        buf.write("\2\u014c\u014d\5H%\2\u014d\u0154\3\2\2\2\u014e\u014f\f")
        buf.write("\4\2\2\u014f\u0150\5F$\2\u0150\u0151\5H%\2\u0151\u0153")
        buf.write("\3\2\2\2\u0152\u014e\3\2\2\2\u0153\u0156\3\2\2\2\u0154")
        buf.write("\u0152\3\2\2\2\u0154\u0155\3\2\2\2\u0155E\3\2\2\2\u0156")
        buf.write("\u0154\3\2\2\2\u0157\u0158\t\5\2\2\u0158G\3\2\2\2\u0159")
        buf.write("\u015c\5J&\2\u015a\u015d\5H%\2\u015b\u015d\5L\'\2\u015c")
        buf.write("\u015a\3\2\2\2\u015c\u015b\3\2\2\2\u015d\u0160\3\2\2\2")
        buf.write("\u015e\u0160\5L\'\2\u015f\u0159\3\2\2\2\u015f\u015e\3")
        buf.write("\2\2\2\u0160I\3\2\2\2\u0161\u0162\7\36\2\2\u0162K\3\2")
        buf.write("\2\2\u0163\u0166\5N(\2\u0164\u0167\5P)\2\u0165\u0167\5")
        buf.write("L\'\2\u0166\u0164\3\2\2\2\u0166\u0165\3\2\2\2\u0167\u016a")
        buf.write("\3\2\2\2\u0168\u016a\5P)\2\u0169\u0163\3\2\2\2\u0169\u0168")
        buf.write("\3\2\2\2\u016aM\3\2\2\2\u016b\u016c\7\32\2\2\u016cO\3")
        buf.write("\2\2\2\u016d\u016e\7@\2\2\u016e\u016f\7\20\2\2\u016f\u0170")
        buf.write("\5R*\2\u0170\u0171\7\21\2\2\u0171\u017a\3\2\2\2\u0172")
        buf.write("\u017a\7@\2\2\u0173\u017a\7\f\2\2\u0174\u017a\7\n\2\2")
        buf.write("\u0175\u017a\7\13\2\2\u0176\u017a\7\r\2\2\u0177\u017a")
        buf.write("\5Z.\2\u0178\u017a\5\62\32\2\u0179\u016d\3\2\2\2\u0179")
        buf.write("\u0172\3\2\2\2\u0179\u0173\3\2\2\2\u0179\u0174\3\2\2\2")
        buf.write("\u0179\u0175\3\2\2\2\u0179\u0176\3\2\2\2\u0179\u0177\3")
        buf.write("\2\2\2\u0179\u0178\3\2\2\2\u017aQ\3\2\2\2\u017b\u0180")
        buf.write("\5\66\34\2\u017c\u017d\7\23\2\2\u017d\u017f\5\66\34\2")
        buf.write("\u017e\u017c\3\2\2\2\u017f\u0182\3\2\2\2\u0180\u017e\3")
        buf.write("\2\2\2\u0180\u0181\3\2\2\2\u0181S\3\2\2\2\u0182\u0180")
        buf.write("\3\2\2\2\u0183\u0184\7\7\2\2\u0184\u0185\7\20\2\2\u0185")
        buf.write("\u0186\5V,\2\u0186\u0187\7\21\2\2\u0187\u0188\7=\2\2\u0188")
        buf.write("\u0189\5X-\2\u0189U\3\2\2\2\u018a\u018f\7\n\2\2\u018b")
        buf.write("\u018c\7\23\2\2\u018c\u018e\7\n\2\2\u018d\u018b\3\2\2")
        buf.write("\2\u018e\u0191\3\2\2\2\u018f\u018d\3\2\2\2\u018f\u0190")
        buf.write("\3\2\2\2\u0190W\3\2\2\2\u0191\u018f\3\2\2\2\u0192\u0193")
        buf.write("\t\6\2\2\u0193Y\3\2\2\2\u0194\u0195\7\26\2\2\u0195\u0196")
        buf.write("\5R*\2\u0196\u0197\7\27\2\2\u0197[\3\2\2\2$_aqs\u0082")
        buf.write("\u008b\u0094\u00bc\u00be\u00c5\u00d6\u00dd\u00e2\u00e9")
        buf.write("\u00ed\u00f0\u0102\u0107\u010c\u010e\u0116\u011f\u0125")
        buf.write("\u012b\u0138\u0146\u0154\u015c\u015f\u0166\u0169\u0179")
        buf.write("\u0180\u018f")
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
                      "NOT", "LG_AND", "LG_OR", "EQ", "INEQ", "LT", "GT", 
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
    RULE_while_stmt = 7
    RULE_do_while_stmt = 8
    RULE_for_stmt = 9
    RULE_break_stmt = 10
    RULE_continue_stmt = 11
    RULE_call_stmt = 12
    RULE_block_stmt = 13
    RULE_return_stmt = 14
    RULE_var_decl = 15
    RULE_id_lst = 16
    RULE_valid_type = 17
    RULE_para_lst_decl = 18
    RULE_para_decl = 19
    RULE_func_decl = 20
    RULE_func_prototype = 21
    RULE_func_return_type = 22
    RULE_func_body = 23
    RULE_func_call = 24
    RULE_arg_lst = 25
    RULE_expr = 26
    RULE_relation_expr = 27
    RULE_relation_op = 28
    RULE_logic_expr = 29
    RULE_logic_op = 30
    RULE_adding_expr = 31
    RULE_adding_op = 32
    RULE_multiplying_expr = 33
    RULE_multiplying_op = 34
    RULE_unary_logic_expr = 35
    RULE_unary_logic_op = 36
    RULE_sign_expr = 37
    RULE_sign_op = 38
    RULE_index_expr = 39
    RULE_expr_lst = 40
    RULE_array_decl = 41
    RULE_integer_lst = 42
    RULE_atomic_type = 43
    RULE_arrayLIT = 44

    ruleNames =  [ "program", "func_main", "main_return", "stmt", "assign_stmt", 
                   "lhs", "if_stmt", "while_stmt", "do_while_stmt", "for_stmt", 
                   "break_stmt", "continue_stmt", "call_stmt", "block_stmt", 
                   "return_stmt", "var_decl", "id_lst", "valid_type", "para_lst_decl", 
                   "para_decl", "func_decl", "func_prototype", "func_return_type", 
                   "func_body", "func_call", "arg_lst", "expr", "relation_expr", 
                   "relation_op", "logic_expr", "logic_op", "adding_expr", 
                   "adding_op", "multiplying_expr", "multiplying_op", "unary_logic_expr", 
                   "unary_logic_op", "sign_expr", "sign_op", "index_expr", 
                   "expr_lst", "array_decl", "integer_lst", "atomic_type", 
                   "arrayLIT" ]

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
    LG_AND=29
    LG_OR=30
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

        def var_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Var_declContext)
            else:
                return self.getTypedRuleContext(MT22Parser.Var_declContext,i)


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
                    self.var_decl()
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


        def var_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Var_declContext)
            else:
                return self.getTypedRuleContext(MT22Parser.Var_declContext,i)


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
                    self.var_decl()
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


        def while_stmt(self):
            return self.getTypedRuleContext(MT22Parser.While_stmtContext,0)


        def do_while_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Do_while_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(MT22Parser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Continue_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Call_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Block_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Return_stmtContext,0)


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
                self.while_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 121
                self.do_while_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 122
                self.for_stmt()
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
                self.call_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 126
                self.block_stmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 127
                self.return_stmt()
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

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


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
            self.expr()
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

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


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
            self.expr()
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


    class While_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


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
        self.enterRule(localctx, 14, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(MT22Parser.WHILE)
            self.state = 149
            self.match(MT22Parser.LP)
            self.state = 150
            self.expr()
            self.state = 151
            self.match(MT22Parser.RP)
            self.state = 152
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

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


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
        self.enterRule(localctx, 16, self.RULE_do_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(MT22Parser.DO)
            self.state = 155
            self.block_stmt()
            self.state = 156
            self.match(MT22Parser.WHILE)
            self.state = 157
            self.match(MT22Parser.LP)
            self.state = 158
            self.expr()
            self.state = 159
            self.match(MT22Parser.RP)
            self.state = 160
            self.match(MT22Parser.SM)
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExprContext,i)


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
        self.enterRule(localctx, 18, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(MT22Parser.FOR)
            self.state = 163
            self.match(MT22Parser.LP)
            self.state = 164
            self.match(MT22Parser.ID)
            self.state = 165
            self.match(MT22Parser.ASSIGN)
            self.state = 166
            self.expr()
            self.state = 167
            self.match(MT22Parser.CM)
            self.state = 168
            self.expr()
            self.state = 169
            self.match(MT22Parser.CM)
            self.state = 170
            self.expr()
            self.state = 171
            self.match(MT22Parser.RP)
            self.state = 172
            self.stmt()
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
        self.enterRule(localctx, 24, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.func_call()
            self.state = 181
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


        def var_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Var_declContext)
            else:
                return self.getTypedRuleContext(MT22Parser.Var_declContext,i)


        def getRuleIndex(self):
            return MT22Parser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = MT22Parser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(MT22Parser.LCB)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.INTLIT) | (1 << MT22Parser.FLOATLIT) | (1 << MT22Parser.BOOLLIT) | (1 << MT22Parser.STRINGLIT) | (1 << MT22Parser.LCB) | (1 << MT22Parser.BREAK) | (1 << MT22Parser.DO) | (1 << MT22Parser.FOR) | (1 << MT22Parser.IF) | (1 << MT22Parser.RETURN) | (1 << MT22Parser.WHILE) | (1 << MT22Parser.CONTINUE) | (1 << MT22Parser.ID))) != 0):
                self.state = 186
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 184
                    self.stmt()
                    pass

                elif la_ == 2:
                    self.state = 185
                    self.var_decl()
                    pass


                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 191
            self.match(MT22Parser.RCB)
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

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = MT22Parser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(MT22Parser.RETURN)
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.INTLIT) | (1 << MT22Parser.FLOATLIT) | (1 << MT22Parser.BOOLLIT) | (1 << MT22Parser.STRINGLIT) | (1 << MT22Parser.LCB) | (1 << MT22Parser.SUB) | (1 << MT22Parser.NOT) | (1 << MT22Parser.ID))) != 0):
                self.state = 194
                self.expr()


            self.state = 197
            self.match(MT22Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.t = None # Id_lstContext
            self.r = None # Expr_lstContext
            self.e = None # Token

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def valid_type(self):
            return self.getTypedRuleContext(MT22Parser.Valid_typeContext,0)


        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def id_lst(self):
            return self.getTypedRuleContext(MT22Parser.Id_lstContext,0)


        def expr_lst(self):
            return self.getTypedRuleContext(MT22Parser.Expr_lstContext,0)


        def SM(self):
            return self.getToken(MT22Parser.SM, 0)

        def atomic_type(self):
            return self.getTypedRuleContext(MT22Parser.Atomic_typeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = MT22Parser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_var_decl)
        try:
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                localctx.t = self.id_lst()
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
                if len((None if localctx.t is None else self._input.getText(localctx.t.start,localctx.t.stop)).split(',')) != len((None if localctx.r is None else self._input.getText(localctx.r.start,localctx.r.stop)).split(',')):
                        raise Exception('Error on line {} col {}: ;'.format((0 if localctx.e is None else localctx.e.line), (0 if localctx.e is None else localctx.e.column)))
                    
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self.id_lst()
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


    class Id_lstContext(ParserRuleContext):
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
            return MT22Parser.RULE_id_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_lst" ):
                return visitor.visitId_lst(self)
            else:
                return visitor.visitChildren(self)




    def id_lst(self):

        localctx = MT22Parser.Id_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_id_lst)
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


        def var_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Var_declContext)
            else:
                return self.getTypedRuleContext(MT22Parser.Var_declContext,i)


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
                    self.var_decl()
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

        def arg_lst(self):
            return self.getTypedRuleContext(MT22Parser.Arg_lstContext,0)


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
            self.state = 276
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.INTLIT) | (1 << MT22Parser.FLOATLIT) | (1 << MT22Parser.BOOLLIT) | (1 << MT22Parser.STRINGLIT) | (1 << MT22Parser.LCB) | (1 << MT22Parser.SUB) | (1 << MT22Parser.NOT) | (1 << MT22Parser.ID))) != 0):
                self.state = 275
                self.arg_lst()


            self.state = 278
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExprContext,i)


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
            self.state = 280
            self.expr()
            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.CM:
                self.state = 281
                self.match(MT22Parser.CM)
                self.state = 282
                self.expr()
                self.state = 287
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
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
            return MT22Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MT22Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.relation_expr()
            self.state = 291
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.SRO:
                self.state = 289
                self.match(MT22Parser.SRO)
                self.state = 290
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

        def logic_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Logic_exprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.Logic_exprContext,i)


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
            self.state = 293
            self.logic_expr(0)
            self.state = 297
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.EQ) | (1 << MT22Parser.INEQ) | (1 << MT22Parser.LT) | (1 << MT22Parser.GT) | (1 << MT22Parser.LE) | (1 << MT22Parser.GE))) != 0):
                self.state = 294
                self.relation_op()
                self.state = 295
                self.logic_expr(0)


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
            self.state = 299
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


    class Logic_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def adding_expr(self):
            return self.getTypedRuleContext(MT22Parser.Adding_exprContext,0)


        def logic_expr(self):
            return self.getTypedRuleContext(MT22Parser.Logic_exprContext,0)


        def logic_op(self):
            return self.getTypedRuleContext(MT22Parser.Logic_opContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_logic_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogic_expr" ):
                return visitor.visitLogic_expr(self)
            else:
                return visitor.visitChildren(self)



    def logic_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Logic_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_logic_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.adding_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 310
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Logic_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logic_expr)
                    self.state = 304
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 305
                    self.logic_op()
                    self.state = 306
                    self.adding_expr(0) 
                self.state = 312
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Logic_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LG_AND(self):
            return self.getToken(MT22Parser.LG_AND, 0)

        def LG_OR(self):
            return self.getToken(MT22Parser.LG_OR, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_logic_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogic_op" ):
                return visitor.visitLogic_op(self)
            else:
                return visitor.visitChildren(self)




    def logic_op(self):

        localctx = MT22Parser.Logic_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_logic_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            _la = self._input.LA(1)
            if not(_la==MT22Parser.LG_AND or _la==MT22Parser.LG_OR):
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
            self.state = 316
            self.multiplying_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 324
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Adding_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_adding_expr)
                    self.state = 318
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 319
                    self.adding_op()
                    self.state = 320
                    self.multiplying_expr(0) 
                self.state = 326
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
            self.state = 327
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

        def unary_logic_expr(self):
            return self.getTypedRuleContext(MT22Parser.Unary_logic_exprContext,0)


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
            self.state = 330
            self.unary_logic_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 338
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Multiplying_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplying_expr)
                    self.state = 332
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 333
                    self.multiplying_op()
                    self.state = 334
                    self.unary_logic_expr() 
                self.state = 340
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
            self.state = 341
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


    class Unary_logic_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary_logic_op(self):
            return self.getTypedRuleContext(MT22Parser.Unary_logic_opContext,0)


        def unary_logic_expr(self):
            return self.getTypedRuleContext(MT22Parser.Unary_logic_exprContext,0)


        def sign_expr(self):
            return self.getTypedRuleContext(MT22Parser.Sign_exprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_unary_logic_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_logic_expr" ):
                return visitor.visitUnary_logic_expr(self)
            else:
                return visitor.visitChildren(self)




    def unary_logic_expr(self):

        localctx = MT22Parser.Unary_logic_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_unary_logic_expr)
        try:
            self.state = 349
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.unary_logic_op()
                self.state = 346
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                if la_ == 1:
                    self.state = 344
                    self.unary_logic_expr()
                    pass

                elif la_ == 2:
                    self.state = 345
                    self.sign_expr()
                    pass


                pass
            elif token in [MT22Parser.INTLIT, MT22Parser.FLOATLIT, MT22Parser.BOOLLIT, MT22Parser.STRINGLIT, MT22Parser.LCB, MT22Parser.SUB, MT22Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
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


    class Unary_logic_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(MT22Parser.NOT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_unary_logic_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_logic_op" ):
                return visitor.visitUnary_logic_op(self)
            else:
                return visitor.visitChildren(self)




    def unary_logic_op(self):

        localctx = MT22Parser.Unary_logic_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_unary_logic_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
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
            self.state = 359
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 353
                self.sign_op()
                self.state = 356
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                if la_ == 1:
                    self.state = 354
                    self.index_expr()
                    pass

                elif la_ == 2:
                    self.state = 355
                    self.sign_expr()
                    pass


                pass
            elif token in [MT22Parser.INTLIT, MT22Parser.FLOATLIT, MT22Parser.BOOLLIT, MT22Parser.STRINGLIT, MT22Parser.LCB, MT22Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 358
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
            self.state = 361
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

        def arrayLIT(self):
            return self.getTypedRuleContext(MT22Parser.ArrayLITContext,0)


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
            self.state = 375
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 363
                self.match(MT22Parser.ID)
                self.state = 364
                self.match(MT22Parser.LSB)
                self.state = 365
                self.expr_lst()
                self.state = 366
                self.match(MT22Parser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 368
                self.match(MT22Parser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 369
                self.match(MT22Parser.BOOLLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 370
                self.match(MT22Parser.INTLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 371
                self.match(MT22Parser.FLOATLIT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 372
                self.match(MT22Parser.STRINGLIT)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 373
                self.arrayLIT()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 374
                self.func_call()
                pass


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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExprContext,i)


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
        self.enterRule(localctx, 80, self.RULE_expr_lst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.expr()
            self.state = 382
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.CM:
                self.state = 378
                self.match(MT22Parser.CM)
                self.state = 379
                self.expr()
                self.state = 384
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
        self.enterRule(localctx, 82, self.RULE_array_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.match(MT22Parser.ArrayType)
            self.state = 386
            self.match(MT22Parser.LSB)
            self.state = 387
            self.integer_lst()
            self.state = 388
            self.match(MT22Parser.RSB)
            self.state = 389
            self.match(MT22Parser.OF)
            self.state = 390
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
        self.enterRule(localctx, 84, self.RULE_integer_lst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.match(MT22Parser.INTLIT)
            self.state = 397
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.CM:
                self.state = 393
                self.match(MT22Parser.CM)
                self.state = 394
                self.match(MT22Parser.INTLIT)
                self.state = 399
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
        self.enterRule(localctx, 86, self.RULE_atomic_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
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


    class ArrayLITContext(ParserRuleContext):
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
            return MT22Parser.RULE_arrayLIT

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLIT" ):
                return visitor.visitArrayLIT(self)
            else:
                return visitor.visitChildren(self)




    def arrayLIT(self):

        localctx = MT22Parser.ArrayLITContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_arrayLIT)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.match(MT22Parser.LCB)
            self.state = 403
            self.expr_lst()
            self.state = 404
            self.match(MT22Parser.RCB)
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
        self._predicates[29] = self.logic_expr_sempred
        self._predicates[31] = self.adding_expr_sempred
        self._predicates[33] = self.multiplying_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def logic_expr_sempred(self, localctx:Logic_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def adding_expr_sempred(self, localctx:Adding_exprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def multiplying_expr_sempred(self, localctx:Multiplying_exprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




