# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#vardecl.
    def visitVardecl(self, ctx:BKOOLParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr.
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr1.
    def visitExpr1(self, ctx:BKOOLParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr2.
    def visitExpr2(self, ctx:BKOOLParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr3.
    def visitExpr3(self, ctx:BKOOLParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr4.
    def visitExpr4(self, ctx:BKOOLParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr5.
    def visitExpr5(self, ctx:BKOOLParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#subexpr.
    def visitSubexpr(self, ctx:BKOOLParser.SubexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arrdecl.
    def visitArrdecl(self, ctx:BKOOLParser.ArrdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#idxarr.
    def visitIdxarr(self, ctx:BKOOLParser.IdxarrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exprlist.
    def visitExprlist(self, ctx:BKOOLParser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#assarr.
    def visitAssarr(self, ctx:BKOOLParser.AssarrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#asspairdecl.
    def visitAsspairdecl(self, ctx:BKOOLParser.AsspairdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#asspair.
    def visitAsspair(self, ctx:BKOOLParser.AsspairContext):
        return self.visitChildren(ctx)



del BKOOLParser