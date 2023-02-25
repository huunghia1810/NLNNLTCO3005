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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2F")
        buf.write("\u01f5\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b")
        buf.write("\3\b\3\t\3\t\3\t\3\t\7\t\u00ac\n\t\f\t\16\t\u00af\13\t")
        buf.write("\3\t\3\t\3\t\5\t\u00b4\n\t\3\n\3\n\3\n\5\n\u00b9\n\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00c3\n\n\3\13\3\13")
        buf.write("\7\13\u00c7\n\13\f\13\16\13\u00ca\13\13\3\f\3\f\5\f\u00ce")
        buf.write("\n\f\3\f\6\f\u00d1\n\f\r\f\16\f\u00d2\3\r\3\r\3\16\3\16")
        buf.write("\3\17\3\17\5\17\u00db\n\17\3\20\3\20\7\20\u00df\n\20\f")
        buf.write("\20\16\20\u00e2\13\20\3\20\3\20\3\20\3\21\3\21\5\21\u00e9")
        buf.write("\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00fb\n\22\3\23\3")
        buf.write("\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3$\3%")
        buf.write("\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3*\3+\3")
        buf.write("+\3+\3,\3,\3,\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3/\3/\3/\3")
        buf.write("/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3")
        buf.write("\61\3\61\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65")
        buf.write("\3\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\67")
        buf.write("\3\67\3\67\38\38\38\38\38\38\38\38\39\39\39\39\3:\3:\3")
        buf.write(":\3:\3:\3:\3:\3;\3;\3;\3;\3;\3;\3;\3<\3<\3<\3<\3<\3=\3")
        buf.write("=\3=\3=\3=\3=\3>\3>\3>\3>\3>\3?\3?\3?\3@\3@\3@\3@\3A\3")
        buf.write("A\3A\3A\3A\3A\3A\3A\3A\3B\3B\3B\3C\3C\3C\3C\3C\3C\3C\3")
        buf.write("C\3D\3D\3D\3D\3D\3D\3E\3E\7E\u01c1\nE\fE\16E\u01c4\13")
        buf.write("E\3F\3F\3F\3F\7F\u01ca\nF\fF\16F\u01cd\13F\3F\3F\3F\3")
        buf.write("F\3F\3G\3G\3G\3G\7G\u01d8\nG\fG\16G\u01db\13G\3G\3G\3")
        buf.write("H\6H\u01e0\nH\rH\16H\u01e1\3H\3H\3I\3I\7I\u01e8\nI\fI")
        buf.write("\16I\u01eb\13I\3J\3J\3J\3K\3K\3K\3L\3L\3L\3\u01cb\2M\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\2\27\2\31\2")
        buf.write("\33\2\35\f\37\r!\2#\2%\16\'\17)\20+\21-\22/\23\61\24\63")
        buf.write("\25\65\26\67\279\30;\31=\32?\33A\34C\35E\36G\37I K!M\"")
        buf.write("O#Q$S%U&W\'Y([)]*_+a,c-e.g/i\60k\61m\62o\63q\64s\65u\66")
        buf.write("w\67y8{9}:\177;\u0081<\u0083=\u0085>\u0087?\u0089@\u008b")
        buf.write("A\u008dB\u008fC\u0091\2\u0093D\u0095E\u0097F\3\2\13\4")
        buf.write("\2GGgg\4\2--//\3\2\62;\3\2\63;\4\2$$^^\5\2C\\aac|\6\2")
        buf.write("\62;C\\aac|\4\2\f\f\17\17\5\2\13\f\16\17\"\"\2\u0205\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write("\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2")
        buf.write("\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3")
        buf.write("\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a")
        buf.write("\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2")
        buf.write("k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2")
        buf.write("\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2")
        buf.write("\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0093\3\2\2\2\2\u0095")
        buf.write("\3\2\2\2\2\u0097\3\2\2\2\3\u0099\3\2\2\2\5\u009b\3\2\2")
        buf.write("\2\7\u009d\3\2\2\2\t\u009f\3\2\2\2\13\u00a1\3\2\2\2\r")
        buf.write("\u00a3\3\2\2\2\17\u00a5\3\2\2\2\21\u00b3\3\2\2\2\23\u00c2")
        buf.write("\3\2\2\2\25\u00c4\3\2\2\2\27\u00cb\3\2\2\2\31\u00d4\3")
        buf.write("\2\2\2\33\u00d6\3\2\2\2\35\u00da\3\2\2\2\37\u00dc\3\2")
        buf.write("\2\2!\u00e8\3\2\2\2#\u00fa\3\2\2\2%\u00fc\3\2\2\2\'\u00fe")
        buf.write("\3\2\2\2)\u0100\3\2\2\2+\u0102\3\2\2\2-\u0104\3\2\2\2")
        buf.write("/\u0106\3\2\2\2\61\u0108\3\2\2\2\63\u010a\3\2\2\2\65\u010c")
        buf.write("\3\2\2\2\67\u010e\3\2\2\29\u0110\3\2\2\2;\u0112\3\2\2")
        buf.write("\2=\u0114\3\2\2\2?\u0116\3\2\2\2A\u0118\3\2\2\2C\u011a")
        buf.write("\3\2\2\2E\u011c\3\2\2\2G\u011e\3\2\2\2I\u0121\3\2\2\2")
        buf.write("K\u0124\3\2\2\2M\u0127\3\2\2\2O\u012a\3\2\2\2Q\u012c\3")
        buf.write("\2\2\2S\u012e\3\2\2\2U\u0131\3\2\2\2W\u0134\3\2\2\2Y\u0137")
        buf.write("\3\2\2\2[\u013c\3\2\2\2]\u0141\3\2\2\2_\u0147\3\2\2\2")
        buf.write("a\u014f\3\2\2\2c\u0152\3\2\2\2e\u0157\3\2\2\2g\u015d\3")
        buf.write("\2\2\2i\u0163\3\2\2\2k\u0167\3\2\2\2m\u0170\3\2\2\2o\u0173")
        buf.write("\3\2\2\2q\u017b\3\2\2\2s\u017f\3\2\2\2u\u0186\3\2\2\2")
        buf.write("w\u018d\3\2\2\2y\u0192\3\2\2\2{\u0198\3\2\2\2}\u019d\3")
        buf.write("\2\2\2\177\u01a0\3\2\2\2\u0081\u01a4\3\2\2\2\u0083\u01ad")
        buf.write("\3\2\2\2\u0085\u01b0\3\2\2\2\u0087\u01b8\3\2\2\2\u0089")
        buf.write("\u01be\3\2\2\2\u008b\u01c5\3\2\2\2\u008d\u01d3\3\2\2\2")
        buf.write("\u008f\u01df\3\2\2\2\u0091\u01e5\3\2\2\2\u0093\u01ec\3")
        buf.write("\2\2\2\u0095\u01ef\3\2\2\2\u0097\u01f2\3\2\2\2\u0099\u009a")
        buf.write("\5u;\2\u009a\4\3\2\2\2\u009b\u009c\5o8\2\u009c\6\3\2\2")
        buf.write("\2\u009d\u009e\5g\64\2\u009e\b\3\2\2\2\u009f\u00a0\5_")
        buf.write("\60\2\u00a0\n\3\2\2\2\u00a1\u00a2\5\u0087D\2\u00a2\f\3")
        buf.write("\2\2\2\u00a3\u00a4\5{>\2\u00a4\16\3\2\2\2\u00a5\u00a6")
        buf.write("\5[.\2\u00a6\20\3\2\2\2\u00a7\u00ad\5\33\16\2\u00a8\u00a9")
        buf.write("\7a\2\2\u00a9\u00ac\5\31\r\2\u00aa\u00ac\5\31\r\2\u00ab")
        buf.write("\u00a8\3\2\2\2\u00ab\u00aa\3\2\2\2\u00ac\u00af\3\2\2\2")
        buf.write("\u00ad\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00b0\3")
        buf.write("\2\2\2\u00af\u00ad\3\2\2\2\u00b0\u00b1\b\t\2\2\u00b1\u00b4")
        buf.write("\3\2\2\2\u00b2\u00b4\7\62\2\2\u00b3\u00a7\3\2\2\2\u00b3")
        buf.write("\u00b2\3\2\2\2\u00b4\22\3\2\2\2\u00b5\u00b6\5\21\t\2\u00b6")
        buf.write("\u00b8\5\25\13\2\u00b7\u00b9\5\27\f\2\u00b8\u00b7\3\2")
        buf.write("\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb")
        buf.write("\b\n\3\2\u00bb\u00c3\3\2\2\2\u00bc\u00bd\5\21\t\2\u00bd")
        buf.write("\u00be\5\27\f\2\u00be\u00c3\3\2\2\2\u00bf\u00c0\5\25\13")
        buf.write("\2\u00c0\u00c1\5\27\f\2\u00c1\u00c3\3\2\2\2\u00c2\u00b5")
        buf.write("\3\2\2\2\u00c2\u00bc\3\2\2\2\u00c2\u00bf\3\2\2\2\u00c3")
        buf.write("\24\3\2\2\2\u00c4\u00c8\7\60\2\2\u00c5\u00c7\5\31\r\2")
        buf.write("\u00c6\u00c5\3\2\2\2\u00c7\u00ca\3\2\2\2\u00c8\u00c6\3")
        buf.write("\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\26\3\2\2\2\u00ca\u00c8")
        buf.write("\3\2\2\2\u00cb\u00cd\t\2\2\2\u00cc\u00ce\t\3\2\2\u00cd")
        buf.write("\u00cc\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00d0\3\2\2\2")
        buf.write("\u00cf\u00d1\5\31\r\2\u00d0\u00cf\3\2\2\2\u00d1\u00d2")
        buf.write("\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3")
        buf.write("\30\3\2\2\2\u00d4\u00d5\t\4\2\2\u00d5\32\3\2\2\2\u00d6")
        buf.write("\u00d7\t\5\2\2\u00d7\34\3\2\2\2\u00d8\u00db\5w<\2\u00d9")
        buf.write("\u00db\5e\63\2\u00da\u00d8\3\2\2\2\u00da\u00d9\3\2\2\2")
        buf.write("\u00db\36\3\2\2\2\u00dc\u00e0\7$\2\2\u00dd\u00df\5!\21")
        buf.write("\2\u00de\u00dd\3\2\2\2\u00df\u00e2\3\2\2\2\u00e0\u00de")
        buf.write("\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00e3\3\2\2\2\u00e2")
        buf.write("\u00e0\3\2\2\2\u00e3\u00e4\7$\2\2\u00e4\u00e5\b\20\4\2")
        buf.write("\u00e5 \3\2\2\2\u00e6\u00e9\n\6\2\2\u00e7\u00e9\5#\22")
        buf.write("\2\u00e8\u00e6\3\2\2\2\u00e8\u00e7\3\2\2\2\u00e9\"\3\2")
        buf.write("\2\2\u00ea\u00eb\7^\2\2\u00eb\u00fb\7d\2\2\u00ec\u00ed")
        buf.write("\7^\2\2\u00ed\u00fb\7h\2\2\u00ee\u00ef\7^\2\2\u00ef\u00fb")
        buf.write("\7t\2\2\u00f0\u00f1\7^\2\2\u00f1\u00fb\7p\2\2\u00f2\u00f3")
        buf.write("\7^\2\2\u00f3\u00fb\7v\2\2\u00f4\u00f5\7^\2\2\u00f5\u00fb")
        buf.write("\7)\2\2\u00f6\u00f7\7^\2\2\u00f7\u00fb\7^\2\2\u00f8\u00f9")
        buf.write("\7^\2\2\u00f9\u00fb\7$\2\2\u00fa\u00ea\3\2\2\2\u00fa\u00ec")
        buf.write("\3\2\2\2\u00fa\u00ee\3\2\2\2\u00fa\u00f0\3\2\2\2\u00fa")
        buf.write("\u00f2\3\2\2\2\u00fa\u00f4\3\2\2\2\u00fa\u00f6\3\2\2\2")
        buf.write("\u00fa\u00f8\3\2\2\2\u00fb$\3\2\2\2\u00fc\u00fd\7*\2\2")
        buf.write("\u00fd&\3\2\2\2\u00fe\u00ff\7+\2\2\u00ff(\3\2\2\2\u0100")
        buf.write("\u0101\7]\2\2\u0101*\3\2\2\2\u0102\u0103\7_\2\2\u0103")
        buf.write(",\3\2\2\2\u0104\u0105\7\60\2\2\u0105.\3\2\2\2\u0106\u0107")
        buf.write("\7.\2\2\u0107\60\3\2\2\2\u0108\u0109\7=\2\2\u0109\62\3")
        buf.write("\2\2\2\u010a\u010b\7<\2\2\u010b\64\3\2\2\2\u010c\u010d")
        buf.write("\7}\2\2\u010d\66\3\2\2\2\u010e\u010f\7\177\2\2\u010f8")
        buf.write("\3\2\2\2\u0110\u0111\7?\2\2\u0111:\3\2\2\2\u0112\u0113")
        buf.write("\7-\2\2\u0113<\3\2\2\2\u0114\u0115\7/\2\2\u0115>\3\2\2")
        buf.write("\2\u0116\u0117\7,\2\2\u0117@\3\2\2\2\u0118\u0119\7\61")
        buf.write("\2\2\u0119B\3\2\2\2\u011a\u011b\7\'\2\2\u011bD\3\2\2\2")
        buf.write("\u011c\u011d\7#\2\2\u011dF\3\2\2\2\u011e\u011f\7(\2\2")
        buf.write("\u011f\u0120\7(\2\2\u0120H\3\2\2\2\u0121\u0122\7~\2\2")
        buf.write("\u0122\u0123\7~\2\2\u0123J\3\2\2\2\u0124\u0125\7?\2\2")
        buf.write("\u0125\u0126\7?\2\2\u0126L\3\2\2\2\u0127\u0128\7#\2\2")
        buf.write("\u0128\u0129\7?\2\2\u0129N\3\2\2\2\u012a\u012b\7>\2\2")
        buf.write("\u012bP\3\2\2\2\u012c\u012d\7@\2\2\u012dR\3\2\2\2\u012e")
        buf.write("\u012f\7>\2\2\u012f\u0130\7?\2\2\u0130T\3\2\2\2\u0131")
        buf.write("\u0132\7@\2\2\u0132\u0133\7?\2\2\u0133V\3\2\2\2\u0134")
        buf.write("\u0135\7<\2\2\u0135\u0136\7<\2\2\u0136X\3\2\2\2\u0137")
        buf.write("\u0138\7o\2\2\u0138\u0139\7c\2\2\u0139\u013a\7k\2\2\u013a")
        buf.write("\u013b\7p\2\2\u013bZ\3\2\2\2\u013c\u013d\7c\2\2\u013d")
        buf.write("\u013e\7w\2\2\u013e\u013f\7v\2\2\u013f\u0140\7q\2\2\u0140")
        buf.write("\\\3\2\2\2\u0141\u0142\7d\2\2\u0142\u0143\7t\2\2\u0143")
        buf.write("\u0144\7g\2\2\u0144\u0145\7c\2\2\u0145\u0146\7m\2\2\u0146")
        buf.write("^\3\2\2\2\u0147\u0148\7d\2\2\u0148\u0149\7q\2\2\u0149")
        buf.write("\u014a\7q\2\2\u014a\u014b\7n\2\2\u014b\u014c\7g\2\2\u014c")
        buf.write("\u014d\7c\2\2\u014d\u014e\7p\2\2\u014e`\3\2\2\2\u014f")
        buf.write("\u0150\7f\2\2\u0150\u0151\7q\2\2\u0151b\3\2\2\2\u0152")
        buf.write("\u0153\7g\2\2\u0153\u0154\7n\2\2\u0154\u0155\7u\2\2\u0155")
        buf.write("\u0156\7g\2\2\u0156d\3\2\2\2\u0157\u0158\7h\2\2\u0158")
        buf.write("\u0159\7c\2\2\u0159\u015a\7n\2\2\u015a\u015b\7u\2\2\u015b")
        buf.write("\u015c\7g\2\2\u015cf\3\2\2\2\u015d\u015e\7h\2\2\u015e")
        buf.write("\u015f\7n\2\2\u015f\u0160\7q\2\2\u0160\u0161\7c\2\2\u0161")
        buf.write("\u0162\7v\2\2\u0162h\3\2\2\2\u0163\u0164\7h\2\2\u0164")
        buf.write("\u0165\7q\2\2\u0165\u0166\7t\2\2\u0166j\3\2\2\2\u0167")
        buf.write("\u0168\7h\2\2\u0168\u0169\7w\2\2\u0169\u016a\7p\2\2\u016a")
        buf.write("\u016b\7e\2\2\u016b\u016c\7v\2\2\u016c\u016d\7k\2\2\u016d")
        buf.write("\u016e\7q\2\2\u016e\u016f\7p\2\2\u016fl\3\2\2\2\u0170")
        buf.write("\u0171\7k\2\2\u0171\u0172\7h\2\2\u0172n\3\2\2\2\u0173")
        buf.write("\u0174\7k\2\2\u0174\u0175\7p\2\2\u0175\u0176\7v\2\2\u0176")
        buf.write("\u0177\7g\2\2\u0177\u0178\7i\2\2\u0178\u0179\7g\2\2\u0179")
        buf.write("\u017a\7t\2\2\u017ap\3\2\2\2\u017b\u017c\7k\2\2\u017c")
        buf.write("\u017d\7p\2\2\u017d\u017e\7v\2\2\u017er\3\2\2\2\u017f")
        buf.write("\u0180\7t\2\2\u0180\u0181\7g\2\2\u0181\u0182\7v\2\2\u0182")
        buf.write("\u0183\7w\2\2\u0183\u0184\7t\2\2\u0184\u0185\7p\2\2\u0185")
        buf.write("t\3\2\2\2\u0186\u0187\7u\2\2\u0187\u0188\7v\2\2\u0188")
        buf.write("\u0189\7t\2\2\u0189\u018a\7k\2\2\u018a\u018b\7p\2\2\u018b")
        buf.write("\u018c\7i\2\2\u018cv\3\2\2\2\u018d\u018e\7v\2\2\u018e")
        buf.write("\u018f\7t\2\2\u018f\u0190\7w\2\2\u0190\u0191\7g\2\2\u0191")
        buf.write("x\3\2\2\2\u0192\u0193\7y\2\2\u0193\u0194\7j\2\2\u0194")
        buf.write("\u0195\7k\2\2\u0195\u0196\7n\2\2\u0196\u0197\7g\2\2\u0197")
        buf.write("z\3\2\2\2\u0198\u0199\7x\2\2\u0199\u019a\7q\2\2\u019a")
        buf.write("\u019b\7k\2\2\u019b\u019c\7f\2\2\u019c|\3\2\2\2\u019d")
        buf.write("\u019e\7k\2\2\u019e\u019f\7p\2\2\u019f~\3\2\2\2\u01a0")
        buf.write("\u01a1\7q\2\2\u01a1\u01a2\7w\2\2\u01a2\u01a3\7v\2\2\u01a3")
        buf.write("\u0080\3\2\2\2\u01a4\u01a5\7e\2\2\u01a5\u01a6\7q\2\2\u01a6")
        buf.write("\u01a7\7p\2\2\u01a7\u01a8\7v\2\2\u01a8\u01a9\7k\2\2\u01a9")
        buf.write("\u01aa\7p\2\2\u01aa\u01ab\7w\2\2\u01ab\u01ac\7g\2\2\u01ac")
        buf.write("\u0082\3\2\2\2\u01ad\u01ae\7q\2\2\u01ae\u01af\7h\2\2\u01af")
        buf.write("\u0084\3\2\2\2\u01b0\u01b1\7k\2\2\u01b1\u01b2\7p\2\2\u01b2")
        buf.write("\u01b3\7j\2\2\u01b3\u01b4\7g\2\2\u01b4\u01b5\7t\2\2\u01b5")
        buf.write("\u01b6\7k\2\2\u01b6\u01b7\7v\2\2\u01b7\u0086\3\2\2\2\u01b8")
        buf.write("\u01b9\7c\2\2\u01b9\u01ba\7t\2\2\u01ba\u01bb\7t\2\2\u01bb")
        buf.write("\u01bc\7c\2\2\u01bc\u01bd\7{\2\2\u01bd\u0088\3\2\2\2\u01be")
        buf.write("\u01c2\t\7\2\2\u01bf\u01c1\t\b\2\2\u01c0\u01bf\3\2\2\2")
        buf.write("\u01c1\u01c4\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c2\u01c3\3")
        buf.write("\2\2\2\u01c3\u008a\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c5\u01c6")
        buf.write("\7\61\2\2\u01c6\u01c7\7,\2\2\u01c7\u01cb\3\2\2\2\u01c8")
        buf.write("\u01ca\13\2\2\2\u01c9\u01c8\3\2\2\2\u01ca\u01cd\3\2\2")
        buf.write("\2\u01cb\u01cc\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cc\u01ce")
        buf.write("\3\2\2\2\u01cd\u01cb\3\2\2\2\u01ce\u01cf\7,\2\2\u01cf")
        buf.write("\u01d0\7\61\2\2\u01d0\u01d1\3\2\2\2\u01d1\u01d2\bF\5\2")
        buf.write("\u01d2\u008c\3\2\2\2\u01d3\u01d4\7\61\2\2\u01d4\u01d5")
        buf.write("\7\61\2\2\u01d5\u01d9\3\2\2\2\u01d6\u01d8\n\t\2\2\u01d7")
        buf.write("\u01d6\3\2\2\2\u01d8\u01db\3\2\2\2\u01d9\u01d7\3\2\2\2")
        buf.write("\u01d9\u01da\3\2\2\2\u01da\u01dc\3\2\2\2\u01db\u01d9\3")
        buf.write("\2\2\2\u01dc\u01dd\bG\5\2\u01dd\u008e\3\2\2\2\u01de\u01e0")
        buf.write("\t\n\2\2\u01df\u01de\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1")
        buf.write("\u01df\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e3\3\2\2\2")
        buf.write("\u01e3\u01e4\bH\5\2\u01e4\u0090\3\2\2\2\u01e5\u01e9\7")
        buf.write("$\2\2\u01e6\u01e8\5!\21\2\u01e7\u01e6\3\2\2\2\u01e8\u01eb")
        buf.write("\3\2\2\2\u01e9\u01e7\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea")
        buf.write("\u0092\3\2\2\2\u01eb\u01e9\3\2\2\2\u01ec\u01ed\5\u0091")
        buf.write("I\2\u01ed\u01ee\bJ\6\2\u01ee\u0094\3\2\2\2\u01ef\u01f0")
        buf.write("\13\2\2\2\u01f0\u01f1\bK\7\2\u01f1\u0096\3\2\2\2\u01f2")
        buf.write("\u01f3\13\2\2\2\u01f3\u01f4\bL\b\2\u01f4\u0098\3\2\2\2")
        buf.write("\24\2\u00ab\u00ad\u00b3\u00b8\u00c2\u00c8\u00cd\u00d2")
        buf.write("\u00da\u00e0\u00e8\u00fa\u01c2\u01cb\u01d9\u01e1\u01e9")
        buf.write("\t\3\t\2\3\n\3\3\20\4\b\2\2\3J\5\3K\6\3L\7")
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
            "ERROR_CHAR", "ILLEGAL_ESCAPE" ]

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
                  "LineComment", "WS", "UncloseString", "UNCLOSE_STRING", 
                  "ERROR_CHAR", "ILLEGAL_ESCAPE" ]

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
            actions[72] = self.UNCLOSE_STRING_action 
            actions[73] = self.ERROR_CHAR_action 
            actions[74] = self.ILLEGAL_ESCAPE_action 
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
     


