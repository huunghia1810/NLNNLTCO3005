# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decl_list.
    def visitDecl_list(self, ctx:MT22Parser.Decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decl.
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_decl.
    def visitVar_decl(self, ctx:MT22Parser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idlist.
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#varssign.
    def visitVarssign(self, ctx:MT22Parser.VarssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#fun_decl.
    def visitFun_decl(self, ctx:MT22Parser.Fun_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param_decl.
    def visitParam_decl(self, ctx:MT22Parser.Param_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramlist.
    def visitParamlist(self, ctx:MT22Parser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param_prime.
    def visitParam_prime(self, ctx:MT22Parser.Param_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param.
    def visitParam(self, ctx:MT22Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param_preffix.
    def visitParam_preffix(self, ctx:MT22Parser.Param_preffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_stmt.
    def visitBlock_stmt(self, ctx:MT22Parser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#if_stmt.
    def visitIf_stmt(self, ctx:MT22Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#do_while_stmt.
    def visitDo_while_stmt(self, ctx:MT22Parser.Do_while_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#for_stmt.
    def visitFor_stmt(self, ctx:MT22Parser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#break_stmt.
    def visitBreak_stmt(self, ctx:MT22Parser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continue_stmt.
    def visitContinue_stmt(self, ctx:MT22Parser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call_stmt.
    def visitCall_stmt(self, ctx:MT22Parser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param_call_stmt.
    def visitParam_call_stmt(self, ctx:MT22Parser.Param_call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param_call_list.
    def visitParam_call_list(self, ctx:MT22Parser.Param_call_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param_call_prime.
    def visitParam_call_prime(self, ctx:MT22Parser.Param_call_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param_call.
    def visitParam_call(self, ctx:MT22Parser.Param_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_stmt.
    def visitReturn_stmt(self, ctx:MT22Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp.
    def visitExp(self, ctx:MT22Parser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp1.
    def visitExp1(self, ctx:MT22Parser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp2.
    def visitExp2(self, ctx:MT22Parser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp3.
    def visitExp3(self, ctx:MT22Parser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp4.
    def visitExp4(self, ctx:MT22Parser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp5.
    def visitExp5(self, ctx:MT22Parser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp6.
    def visitExp6(self, ctx:MT22Parser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp7.
    def visitExp7(self, ctx:MT22Parser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp8.
    def visitExp8(self, ctx:MT22Parser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp9.
    def visitExp9(self, ctx:MT22Parser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#operand.
    def visitOperand(self, ctx:MT22Parser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call.
    def visitCall(self, ctx:MT22Parser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#valintlist.
    def visitValintlist(self, ctx:MT22Parser.ValintlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#valfloatlist.
    def visitValfloatlist(self, ctx:MT22Parser.ValfloatlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#valstringlist.
    def visitValstringlist(self, ctx:MT22Parser.ValstringlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#valbooleanlist.
    def visitValbooleanlist(self, ctx:MT22Parser.ValbooleanlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#typ.
    def visitTyp(self, ctx:MT22Parser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#typeint.
    def visitTypeint(self, ctx:MT22Parser.TypeintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#typefloat.
    def visitTypefloat(self, ctx:MT22Parser.TypefloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#typestring.
    def visitTypestring(self, ctx:MT22Parser.TypestringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#typeboolean.
    def visitTypeboolean(self, ctx:MT22Parser.TypebooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#fntype.
    def visitFntype(self, ctx:MT22Parser.FntypeContext):
        return self.visitChildren(ctx)



del MT22Parser