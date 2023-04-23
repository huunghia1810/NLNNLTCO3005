from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *

class ASTGeneration(MT22Visitor):

    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(self.visit(ctx.decllist()))

    def visitIdlist(self, ctx: MT22Parser.IdlistContext):
        if ctx.CM():
            return [ctx.ID().getText()] + self.visit(ctx.idlist())
        return [ctx.ID().getText()]

    def visitDecllist(self, ctx: MT22Parser.DecllistContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.decl())
        return self.visit(ctx.decl()) + self.visit(ctx.decllist())

    def visitDecl(self, ctx: MT22Parser.DeclContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        return self.visit(ctx.funcdecl())

    def visitVarnoinit(self, ctx: MT22Parser.VarnoinitContext):
        idlist = self.visit(ctx.idlist())
        type = self.visit(ctx.vartype())
        return list(map(lambda a: VarDecl(a, type, None), idlist))

    def visitVardecl(self, ctx: MT22Parser.VardeclContext):
        if ctx.varnoinit():
            return self.visit(ctx.varnoinit())
        if ctx.varassign():
            return self.visit(ctx.varassign())
        return self.visit(ctx.array())

    def visitVarassign(self, ctx: MT22Parser.VarassignContext):
        ids = self.visit(ctx.idlist())
        type = self.visit(ctx.vartype())
        exprs = self.visit(ctx.expprime())
        return list(map(lambda a, b: VarDecl(a, type, b), ids, exprs))

    def visitVartype(self, ctx: MT22Parser.VardeclContext):
        if ctx.INTEGER():
            return IntegerType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.BOOLEAN():
            return BooleanType()
        if ctx.STRING():
            return StringType()
        return AutoType()

    # ------------------ array ------------------
    def visitArray(self, ctx: MT22Parser.ArrayContext):
        if ctx.arraydecl():
            return self.visit(ctx.arraydecl())
        return self.visit(ctx.arrayinit())

    def visitArraydecl(self, ctx: MT22Parser.ArraydeclContext):
        listId = self.visit(ctx.idlist())
        arrParam = self.visit(ctx.arrayParam())
        return list(map(lambda Id: VarDecl(Id, arrParam, None), listId))

    def visitArrayinit(self, ctx: MT22Parser.ArrayinitContext):
        listId = self.visit(ctx.idlist())
        arrParam = self.visit(ctx.arrayParam())
        arrLit = self.visit(ctx.arraylit())
        return list(map(lambda Id, lit: VarDecl(Id, arrParam, lit), listId, arrLit))

    def visitArraylit(self, ctx: MT22Parser.ArraylitContext):
        if ctx.expprime():
            return self.visit(ctx.expprime())
        return self.visit(ctx.arrayValList())
    
    def visitArrayValList(self, ctx: MT22Parser.ArrayValListContext):
        if ctx.CM():
            return [ArrayLit(self.visit(ctx.arrayVal()))] + self.visit(ctx.arrayValList())
        return [ArrayLit(self.visit(ctx.arrayVal()))]

    def visitArrayVal(self, ctx: MT22Parser.ArrayValContext):
        return self.visit(ctx.exprlist())

    def visitArrayParam(self, ctx: MT22Parser.ArrayParamContext):
        dimension = self.visit(ctx.dimension())
        atomic_type = self.visit(ctx.atomic_type())
        return ArrayType(dimension, atomic_type)

    def visitFuncdecl(self, ctx: MT22Parser.FuncdeclContext):
        baseEle = self.visit(ctx.base_funcdecl())
        body = self.visit(ctx.blockstmt())
        if ctx.PARAM_KEYWORDS():
            return [FuncDecl(baseEle.name, baseEle.return_type, baseEle.params,ctx.ID().getText(), body)]
        return [FuncDecl(baseEle.name, baseEle.return_type, baseEle.params, None, body)]

    def visitBase_funcdecl(self, ctx: MT22Parser.Base_funcdeclContext):
        name = ctx.ID().getText()
        type = self.visit(ctx.returntype())
        params = self.visit(ctx.paramlist())
        return FuncDecl(name, type, params, None, "")

    def visitDimension(self, ctx: MT22Parser.DimensionContext):
        if ctx.CM():
            return [int(ctx.INTLIT().getText())] + self.visit(ctx.dimension())
        return [int(ctx.INTLIT().getText())]

    def visitReturntype(self, ctx: MT22Parser.ReturntypeContext):
        if ctx.VOID():
            return VoidType()
        if ctx.AUTO():
            return AutoType()
        if ctx.atomic_type():
            return self.visit(ctx.atomic_type())
        return self.visit(ctx.arrayParam())
#
    def visitParamlist(self, ctx: MT22Parser.ParamlistContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.paramprime())
        return []

    def visitParamprime(self, ctx: MT22Parser.ParamprimeContext):
        if ctx.CM():
            return [self.visit(ctx.param())] + self.visit(ctx.paramprime())
        return [self.visit(ctx.param())]

    def visitParam(self, ctx: MT22Parser.ParamContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.parambase())
        data = self.visit(ctx.parambase())
        head = self.visit(ctx.paramHead())
        if (head == "2"): #check head
            return ParamDecl(data.name, data.typ, True, True)
        elif head == "inherit":
            return ParamDecl(data.name, data.typ, False, True)
        return ParamDecl(data.name, data.typ, True, False)

    def visitParamHead(self, ctx: MT22Parser.ParamHeadContext):
        if (ctx.getChildCount() == 2):
            return "2"
        return ctx.PARAM_KEYWORDS(0).getText()

    def visitParambase(self, ctx: MT22Parser.ParambaseContext):
        name = ctx.ID().getText()
        type = self.visit(ctx.paramtype())
        return ParamDecl(name, type, False, False)

    def visitParamtype(self, ctx: MT22Parser.ParamtypeContext):
        if ctx.AUTO():
            return AutoType()
        if ctx.atomic_type():
            return self.visit(ctx.atomic_type())
        return self.visit(ctx.arrayParam())

    def visitAtomic_type(self, ctx: MT22Parser.Atomic_typeContext):
        if ctx.FLOAT():
            return FloatType()
        if ctx.INTEGER():
            return IntegerType()
        if ctx.BOOLEAN():
            return BooleanType()
        return StringType()

    # ------------------ 7 statement: stmt -----------------
    def visitStmt(self, ctx: MT22Parser.StmtContext):
        if ctx.assignstmt():
            return self.visit(ctx.assignstmt())
        elif ctx.returnstmt():
            return self.visit(ctx.returnstmt())
        elif ctx.ifstmt():
            return self.visit(ctx.ifstmt())
        elif ctx.callstmt():
            return self.visit(ctx.callstmt())
        elif ctx.forstmt():
            return self.visit(ctx.forstmt())
        elif ctx.blockstmt():
            return self.visit(ctx.blockstmt())
        elif ctx.breakstmt():
            return self.visit(ctx.breakstmt())
        elif ctx.dowhile_stmt():
            return self.visit(ctx.dowhile_stmt())
        elif ctx.whilestmt():
            return self.visit(ctx.whilestmt())
        return self.visit(ctx.continuestmt())

    def visitAssignstmt(self, ctx: MT22Parser.AssignstmtContext):
        return AssignStmt(self.visit(ctx.scalar_variable()), self.visit(ctx.expr()))

    def visitAllowed_blockstmt(self, ctx: MT22Parser.Allowed_blockstmtContext):
        if ctx.stmt():
            return [self.visit(ctx.stmt())]
        return self.visit(ctx.vardecl())

    def visitDowhile_stmt(self, ctx: MT22Parser.Dowhile_stmtContext):
        return DoWhileStmt(self.visit(ctx.expr()), self.visit(ctx.blockstmt()))

    def visitWhilestmt(self, ctx: MT22Parser.WhilestmtContext):
        return WhileStmt(self.visit(ctx.expr()), self.visit(ctx.loopstmt()))

    def visitBlockstmt(self, ctx: MT22Parser.BlockstmtContext):
        return BlockStmt(self.visit(ctx.blocklist()))

    def visitBlocklist(self, ctx: MT22Parser.BlocklistContext):
        if (ctx.getChildCount() == 2):
            return self.visit(ctx.allowed_blockstmt()) + self.visit(ctx.blocklist())
        return []

    def visitForstmt(self, ctx: MT22Parser.ForstmtContext):
        s_var = self.visit(ctx.scalar_variable())
        init = self.visit(ctx.expr(0))
        cond = self.visit(ctx.expr(1))
        inc = self.visit(ctx.expr(2))
        st = self.visit(ctx.loopstmt())

        assInit = AssignStmt(s_var, init)
        return ForStmt(assInit, cond, inc, st)

    def visitIfstmt(self, ctx: MT22Parser.IfstmtContext):
        if ctx.ELSE():
            cond =  self.visit(ctx.expr())
            tstmt = self.visit(ctx.loopstmt(0))
            fstmt = self.visit(ctx.loopstmt(1))
            return IfStmt(cond,tstmt,fstmt)

        cond =  self.visit(ctx.expr())
        tstmt = self.visit(ctx.loopstmt(0))
        return IfStmt(cond,tstmt,None)

    def visitLoopStmt(self, ctx: MT22Parser.LoopstmtContext):
        if ctx.stmt():
            return self.visit(ctx.stmt())
        return self.visit(ctx.blockstmt())

    def visitScalar_variable(self, ctx: MT22Parser.Scalar_variableContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        return self.visit(ctx.indexop())

    def visitCallstmt(self, ctx: MT22Parser.CallstmtContext):
        return CallStmt(ctx.ID().getText(), self.visit(ctx.exprlist()))

    def visitBreakstmt(self, ctx: MT22Parser.BreakstmtContext):
        return BreakStmt()

    def visitContinuestmt(self, ctx: MT22Parser.ContinuestmtContext):
        return ContinueStmt()

    def visitReturnstmt(self, ctx: MT22Parser.ReturnstmtContext):
        if ctx.getChildCount() == 2:
            return ReturnStmt(None)
        return ReturnStmt(self.visit(ctx.expr()))

    # ------------------ expr -----------------
    def visitExprlist(self, ctx: MT22Parser.ExprlistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.expprime())
    
    def visitExpprime(self, ctx: MT22Parser.ExpprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.expprime())
    
    def visitExpr(self, ctx: MT22Parser.ExprContext):
        if ctx.SRO():
            op = ctx.SRO().getText()
            left = self.visit(ctx.expr1(0))
            right = self.visit(ctx.expr1(1))
            return BinExpr(op, left, right)
        return self.visit(ctx.expr1(0))
    
    def visitExpr1(self, ctx: MT22Parser.Expr1Context):
        if ctx.COMPARE():
            op = ctx.COMPARE().getText()
            left = self.visit(ctx.expr2(0))
            right = self.visit(ctx.expr2(1))
            return BinExpr(op, left, right)
        return self.visit(ctx.expr2(0))

    def visitExpr2(self, ctx: MT22Parser.Expr2Context):
        if ctx.AND_OR():
            op = ctx.AND_OR().getText()
            left = self.visit(ctx.expr2())
            right = self.visit(ctx.expr3())
            return BinExpr(op, left, right)
        return self.visit(ctx.expr3())
    
    def visitExpr3(self, ctx: MT22Parser.Expr3Context):
        if ctx.ADD():
            left = self.visit(ctx.expr3())
            right = self.visit(ctx.expr4())
            op = ctx.ADD().getText()
            return BinExpr(op, left, right)

        if ctx.SUB():
            left = self.visit(ctx.expr3())
            right = self.visit(ctx.expr4())
            op = ctx.SUB().getText()
            return BinExpr(op, left, right)
        return self.visit(ctx.expr4())
    
    def visitExpr4(self, ctx: MT22Parser.Expr4Context):
        if ctx.MOD_MUL_DIV():
            op = ctx.MOD_MUL_DIV().getText()
            left = self.visit(ctx.expr4())
            right = self.visit(ctx.expr5())
            return BinExpr(op, left, right)
        return self.visit(ctx.expr5())
    
    def visitExpr5(self, ctx: MT22Parser.Expr5Context):
        if ctx.NOT():
            op = ctx.NOT().getText()
            value = self.visit(ctx.expr5())
            return UnExpr(op, value)
        return self.visit(ctx.expr6())
    
    def visitExpr6(self, ctx: MT22Parser.Expr6Context):
        if ctx.SUB():
            op = ctx.SUB().getText()
            value = self.visit(ctx.expr6())
            return UnExpr(op, value)
        return self.visit(ctx.expr7())

    def visitExpr7(self, ctx: MT22Parser.Expr7Context):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.FLOATLIT():
            st = ctx.FLOATLIT().getText()
            if st[0] == '.' and st[1] == 'e':
                st = '0.0'
            return FloatLit(float(st))
        elif ctx.INTLIT():
            return IntegerLit(int(ctx.INTLIT().getText()))
        elif ctx.BOOLLIT():
            return BooleanLit(ctx.BOOLLIT().getText() == "true")
        elif ctx.STRINGLIT():
            return StringLit(str(ctx.STRINGLIT().getText()))
        elif ctx.subexpr():
            return self.visit(ctx.subexpr())
        elif ctx.callexpr():
            return self.visit(ctx.callexpr())
        return self.visit(ctx.indexop())

    def visitCallexpr(self, ctx: MT22Parser.CallexprContext):
        if ctx.LP() and ctx.RP():
            name = ctx.ID().getText()
            exprs = self.visit(ctx.exprlist())
            return FuncCall(name, exprs)

    def visitSubexpr(self, ctx: MT22Parser.SubexprContext):
        if ctx.LP() and ctx.RP():
            return self.visit(ctx.expr())

    def visitIndexop(self, ctx: MT22Parser.IndexopContext):
        if ctx.LSB() and ctx.RSB():
            name = ctx.ID().getText()
            exprs = self.visit(ctx.expprime())
            return ArrayCell(name, exprs)