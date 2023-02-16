# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\33")
        buf.write("\u008c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\6\2\"\n\2\r\2\16\2#\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\5\4\62\n")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\5\59\n\5\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\7\6A\n\6\f\6\16\6D\13\6\3\7\3\7\3\7\3\7\3\7\3\7\7\7")
        buf.write("L\n\7\f\7\16\7O\13\7\3\b\3\b\3\b\3\b\3\b\5\bV\n\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\5\t^\n\t\3\n\3\n\3\n\3\n\3\13\3\13")
        buf.write("\6\13f\n\13\r\13\16\13g\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3")
        buf.write("\r\7\rr\n\r\f\r\16\ru\13\r\5\rw\n\r\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\7\17\u0081\n\17\f\17\16\17\u0084")
        buf.write("\13\17\5\17\u0086\n\17\3\20\3\20\3\20\3\20\3\20\2\4\n")
        buf.write("\f\21\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36\2\4\3\2\6")
        buf.write("\7\3\2\b\n\2\u008d\2!\3\2\2\2\4\'\3\2\2\2\6\61\3\2\2\2")
        buf.write("\b8\3\2\2\2\n:\3\2\2\2\fE\3\2\2\2\16U\3\2\2\2\20]\3\2")
        buf.write("\2\2\22_\3\2\2\2\24e\3\2\2\2\26i\3\2\2\2\30v\3\2\2\2\32")
        buf.write("x\3\2\2\2\34\u0085\3\2\2\2\36\u0087\3\2\2\2 \"\5\4\3\2")
        buf.write("! \3\2\2\2\"#\3\2\2\2#!\3\2\2\2#$\3\2\2\2$%\3\2\2\2%&")
        buf.write("\7\2\2\3&\3\3\2\2\2\'(\7\26\2\2()\7\21\2\2)*\5\6\4\2*")
        buf.write("+\7\20\2\2+\5\3\2\2\2,-\5\b\5\2-.\7\13\2\2./\5\b\5\2/")
        buf.write("\62\3\2\2\2\60\62\5\b\5\2\61,\3\2\2\2\61\60\3\2\2\2\62")
        buf.write("\7\3\2\2\2\63\64\5\n\6\2\64\65\t\2\2\2\65\66\5\b\5\2\66")
        buf.write("9\3\2\2\2\679\5\n\6\28\63\3\2\2\28\67\3\2\2\29\t\3\2\2")
        buf.write("\2:;\b\6\1\2;<\5\f\7\2<B\3\2\2\2=>\f\4\2\2>?\t\3\2\2?")
        buf.write("A\5\f\7\2@=\3\2\2\2AD\3\2\2\2B@\3\2\2\2BC\3\2\2\2C\13")
        buf.write("\3\2\2\2DB\3\2\2\2EF\b\7\1\2FG\5\16\b\2GM\3\2\2\2HI\f")
        buf.write("\4\2\2IJ\7\5\2\2JL\5\16\b\2KH\3\2\2\2LO\3\2\2\2MK\3\2")
        buf.write("\2\2MN\3\2\2\2N\r\3\2\2\2OM\3\2\2\2PQ\5\20\t\2QR\7\4\2")
        buf.write("\2RS\5\16\b\2SV\3\2\2\2TV\5\20\t\2UP\3\2\2\2UT\3\2\2\2")
        buf.write("V\17\3\2\2\2W^\7\26\2\2X^\7\22\2\2Y^\7\24\2\2Z^\7\23\2")
        buf.write("\2[^\5\24\13\2\\^\5\22\n\2]W\3\2\2\2]X\3\2\2\2]Y\3\2\2")
        buf.write("\2]Z\3\2\2\2][\3\2\2\2]\\\3\2\2\2^\21\3\2\2\2_`\7\16\2")
        buf.write("\2`a\5\6\4\2ab\7\17\2\2b\23\3\2\2\2cf\5\26\f\2df\5\32")
        buf.write("\16\2ec\3\2\2\2ed\3\2\2\2fg\3\2\2\2ge\3\2\2\2gh\3\2\2")
        buf.write("\2h\25\3\2\2\2ij\7\3\2\2jk\7\16\2\2kl\5\30\r\2lm\7\17")
        buf.write("\2\2m\27\3\2\2\2ns\5\6\4\2op\7\r\2\2pr\5\30\r\2qo\3\2")
        buf.write("\2\2ru\3\2\2\2sq\3\2\2\2st\3\2\2\2tw\3\2\2\2us\3\2\2\2")
        buf.write("vn\3\2\2\2vw\3\2\2\2w\31\3\2\2\2xy\7\3\2\2yz\7\16\2\2")
        buf.write("z{\5\34\17\2{|\7\17\2\2|\33\3\2\2\2}\u0082\5\36\20\2~")
        buf.write("\177\7\r\2\2\177\u0081\5\34\17\2\u0080~\3\2\2\2\u0081")
        buf.write("\u0084\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0083\3\2\2\2")
        buf.write("\u0083\u0086\3\2\2\2\u0084\u0082\3\2\2\2\u0085}\3\2\2")
        buf.write("\2\u0085\u0086\3\2\2\2\u0086\35\3\2\2\2\u0087\u0088\7")
        buf.write("\27\2\2\u0088\u0089\7\f\2\2\u0089\u008a\5\6\4\2\u008a")
        buf.write("\37\3\2\2\2\17#\618BMU]egsv\u0082\u0085")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'array'", "'**'", "'.'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'??'", "'=>'", "','", "'('", 
                     "')'", "';'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "DSTAR", "DOT", "ADD", "SUB", 
                      "MUL", "DIV", "MOD", "DQUES", "ARROW", "COMMA", "LB", 
                      "RB", "SEMI", "EQ", "INTLIT", "STRINGLIT", "FLOATLIT", 
                      "ID", "VARNAME", "PAIRNAME", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_vardecl = 1
    RULE_expr = 2
    RULE_expr1 = 3
    RULE_expr2 = 4
    RULE_expr3 = 5
    RULE_expr4 = 6
    RULE_expr5 = 7
    RULE_subexpr = 8
    RULE_arrdecl = 9
    RULE_idxarr = 10
    RULE_exprlist = 11
    RULE_assarr = 12
    RULE_asspairdecl = 13
    RULE_asspair = 14

    ruleNames =  [ "program", "vardecl", "expr", "expr1", "expr2", "expr3", 
                   "expr4", "expr5", "subexpr", "arrdecl", "idxarr", "exprlist", 
                   "assarr", "asspairdecl", "asspair" ]

    EOF = Token.EOF
    T__0=1
    DSTAR=2
    DOT=3
    ADD=4
    SUB=5
    MUL=6
    DIV=7
    MOD=8
    DQUES=9
    ARROW=10
    COMMA=11
    LB=12
    RB=13
    SEMI=14
    EQ=15
    INTLIT=16
    STRINGLIT=17
    FLOATLIT=18
    ID=19
    VARNAME=20
    PAIRNAME=21
    WS=22
    ERROR_CHAR=23
    UNCLOSE_STRING=24
    ILLEGAL_ESCAPE=25

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
            return self.getToken(BKOOLParser.EOF, 0)

        def vardecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.VardeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.VardeclContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 30
                self.vardecl()
                self.state = 33 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.VARNAME):
                    break

            self.state = 35
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARNAME(self):
            return self.getToken(BKOOLParser.VARNAME, 0)

        def EQ(self):
            return self.getToken(BKOOLParser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = BKOOLParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(BKOOLParser.VARNAME)
            self.state = 38
            self.match(BKOOLParser.EQ)
            self.state = 39
            self.expr()
            self.state = 40
            self.match(BKOOLParser.SEMI)
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

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Expr1Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Expr1Context,i)


        def DQUES(self):
            return self.getToken(BKOOLParser.DQUES, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = BKOOLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr)
        try:
            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.expr1()
                self.state = 43
                self.match(BKOOLParser.DQUES)
                self.state = 44
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(BKOOLParser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(BKOOLParser.Expr1Context,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = BKOOLParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 54
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.expr2(0)
                self.state = 50
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 51
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(BKOOLParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(BKOOLParser.Expr2Context,0)


        def MUL(self):
            return self.getToken(BKOOLParser.MUL, 0)

        def DIV(self):
            return self.getToken(BKOOLParser.DIV, 0)

        def MOD(self):
            return self.getToken(BKOOLParser.MOD, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 64
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 59
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 60
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MUL) | (1 << BKOOLParser.DIV) | (1 << BKOOLParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 61
                    self.expr3(0) 
                self.state = 66
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(BKOOLParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(BKOOLParser.Expr3Context,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.expr4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 75
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 70
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 71
                    self.match(BKOOLParser.DOT)
                    self.state = 72
                    self.expr4() 
                self.state = 77
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(BKOOLParser.Expr5Context,0)


        def DSTAR(self):
            return self.getToken(BKOOLParser.DSTAR, 0)

        def expr4(self):
            return self.getTypedRuleContext(BKOOLParser.Expr4Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)




    def expr4(self):

        localctx = BKOOLParser.Expr4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expr4)
        try:
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.expr5()
                self.state = 79
                self.match(BKOOLParser.DSTAR)
                self.state = 80
                self.expr4()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.expr5()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARNAME(self):
            return self.getToken(BKOOLParser.VARNAME, 0)

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(BKOOLParser.STRINGLIT, 0)

        def arrdecl(self):
            return self.getTypedRuleContext(BKOOLParser.ArrdeclContext,0)


        def subexpr(self):
            return self.getTypedRuleContext(BKOOLParser.SubexprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = BKOOLParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expr5)
        try:
            self.state = 91
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.VARNAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.match(BKOOLParser.VARNAME)
                pass
            elif token in [BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.match(BKOOLParser.INTLIT)
                pass
            elif token in [BKOOLParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 87
                self.match(BKOOLParser.FLOATLIT)
                pass
            elif token in [BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 88
                self.match(BKOOLParser.STRINGLIT)
                pass
            elif token in [BKOOLParser.T__0]:
                self.enterOuterAlt(localctx, 5)
                self.state = 89
                self.arrdecl()
                pass
            elif token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 6)
                self.state = 90
                self.subexpr()
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


    class SubexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_subexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubexpr" ):
                return visitor.visitSubexpr(self)
            else:
                return visitor.visitChildren(self)




    def subexpr(self):

        localctx = BKOOLParser.SubexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_subexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(BKOOLParser.LB)
            self.state = 94
            self.expr()
            self.state = 95
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idxarr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.IdxarrContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.IdxarrContext,i)


        def assarr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.AssarrContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.AssarrContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_arrdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrdecl" ):
                return visitor.visitArrdecl(self)
            else:
                return visitor.visitChildren(self)




    def arrdecl(self):

        localctx = BKOOLParser.ArrdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_arrdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 99
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        self.state = 97
                        self.idxarr()
                        pass

                    elif la_ == 2:
                        self.state = 98
                        self.assarr()
                        pass



                else:
                    raise NoViableAltException(self)
                self.state = 101 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdxarrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(BKOOLParser.ExprlistContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_idxarr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdxarr" ):
                return visitor.visitIdxarr(self)
            else:
                return visitor.visitChildren(self)




    def idxarr(self):

        localctx = BKOOLParser.IdxarrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_idxarr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(BKOOLParser.T__0)
            self.state = 104
            self.match(BKOOLParser.LB)
            self.state = 105
            self.exprlist()
            self.state = 106
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def exprlist(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprlistContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprlistContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exprlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlist" ):
                return visitor.visitExprlist(self)
            else:
                return visitor.visitChildren(self)




    def exprlist(self):

        localctx = BKOOLParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_exprlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.T__0) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.VARNAME))) != 0):
                self.state = 108
                self.expr()
                self.state = 113
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 109
                        self.match(BKOOLParser.COMMA)
                        self.state = 110
                        self.exprlist() 
                    self.state = 115
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssarrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def asspairdecl(self):
            return self.getTypedRuleContext(BKOOLParser.AsspairdeclContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_assarr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssarr" ):
                return visitor.visitAssarr(self)
            else:
                return visitor.visitChildren(self)




    def assarr(self):

        localctx = BKOOLParser.AssarrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_assarr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(BKOOLParser.T__0)
            self.state = 119
            self.match(BKOOLParser.LB)
            self.state = 120
            self.asspairdecl()
            self.state = 121
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsspairdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asspair(self):
            return self.getTypedRuleContext(BKOOLParser.AsspairContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def asspairdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.AsspairdeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.AsspairdeclContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_asspairdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsspairdecl" ):
                return visitor.visitAsspairdecl(self)
            else:
                return visitor.visitChildren(self)




    def asspairdecl(self):

        localctx = BKOOLParser.AsspairdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_asspairdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.PAIRNAME:
                self.state = 123
                self.asspair()
                self.state = 128
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 124
                        self.match(BKOOLParser.COMMA)
                        self.state = 125
                        self.asspairdecl() 
                    self.state = 130
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsspairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PAIRNAME(self):
            return self.getToken(BKOOLParser.PAIRNAME, 0)

        def ARROW(self):
            return self.getToken(BKOOLParser.ARROW, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_asspair

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsspair" ):
                return visitor.visitAsspair(self)
            else:
                return visitor.visitChildren(self)




    def asspair(self):

        localctx = BKOOLParser.AsspairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_asspair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(BKOOLParser.PAIRNAME)
            self.state = 134
            self.match(BKOOLParser.ARROW)
            self.state = 135
            self.expr()
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
        self._predicates[4] = self.expr2_sempred
        self._predicates[5] = self.expr3_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




