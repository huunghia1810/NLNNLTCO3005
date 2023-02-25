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


    # Visit a parse tree produced by MT22Parser#func_main.
    def visitFunc_main(self, ctx:MT22Parser.Func_mainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#main_return.
    def visitMain_return(self, ctx:MT22Parser.Main_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assign_stmt.
    def visitAssign_stmt(self, ctx:MT22Parser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#lhs.
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#if_stmt.
    def visitIf_stmt(self, ctx:MT22Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#while_stmt.
    def visitWhile_stmt(self, ctx:MT22Parser.While_stmtContext):
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


    # Visit a parse tree produced by MT22Parser#block_stmt.
    def visitBlock_stmt(self, ctx:MT22Parser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_stmt.
    def visitReturn_stmt(self, ctx:MT22Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_decl.
    def visitVar_decl(self, ctx:MT22Parser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#id_lst.
    def visitId_lst(self, ctx:MT22Parser.Id_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#valid_type.
    def visitValid_type(self, ctx:MT22Parser.Valid_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#para_lst_decl.
    def visitPara_lst_decl(self, ctx:MT22Parser.Para_lst_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#para_decl.
    def visitPara_decl(self, ctx:MT22Parser.Para_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_decl.
    def visitFunc_decl(self, ctx:MT22Parser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_prototype.
    def visitFunc_prototype(self, ctx:MT22Parser.Func_prototypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_return_type.
    def visitFunc_return_type(self, ctx:MT22Parser.Func_return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_body.
    def visitFunc_body(self, ctx:MT22Parser.Func_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_call.
    def visitFunc_call(self, ctx:MT22Parser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arg_lst.
    def visitArg_lst(self, ctx:MT22Parser.Arg_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relation_expr.
    def visitRelation_expr(self, ctx:MT22Parser.Relation_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relation_op.
    def visitRelation_op(self, ctx:MT22Parser.Relation_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logic_expr.
    def visitLogic_expr(self, ctx:MT22Parser.Logic_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logic_op.
    def visitLogic_op(self, ctx:MT22Parser.Logic_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#adding_expr.
    def visitAdding_expr(self, ctx:MT22Parser.Adding_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#adding_op.
    def visitAdding_op(self, ctx:MT22Parser.Adding_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#multiplying_expr.
    def visitMultiplying_expr(self, ctx:MT22Parser.Multiplying_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#multiplying_op.
    def visitMultiplying_op(self, ctx:MT22Parser.Multiplying_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#unary_logic_expr.
    def visitUnary_logic_expr(self, ctx:MT22Parser.Unary_logic_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#unary_logic_op.
    def visitUnary_logic_op(self, ctx:MT22Parser.Unary_logic_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#sign_expr.
    def visitSign_expr(self, ctx:MT22Parser.Sign_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#sign_op.
    def visitSign_op(self, ctx:MT22Parser.Sign_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#index_expr.
    def visitIndex_expr(self, ctx:MT22Parser.Index_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr_lst.
    def visitExpr_lst(self, ctx:MT22Parser.Expr_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_decl.
    def visitArray_decl(self, ctx:MT22Parser.Array_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#integer_lst.
    def visitInteger_lst(self, ctx:MT22Parser.Integer_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atomic_type.
    def visitAtomic_type(self, ctx:MT22Parser.Atomic_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayLIT.
    def visitArrayLIT(self, ctx:MT22Parser.ArrayLITContext):
        return self.visitChildren(ctx)



del MT22Parser