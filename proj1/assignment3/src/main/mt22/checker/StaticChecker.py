#Nguyen Huu Nghia, MSSV: 2033068
from Visitor import Visitor
from StaticError import *
from AST import *

class Symbol(): 
    def __init__(self, name, typ):
        self.name = name
        self.typ = typ
    def __str__(self):
        return "Symbol({}, {})".format(str(self.name), str(self.typ))

class FuncSymbol(Symbol): 
    def __init__(self, name, return_type, paramSortType, inherit, env, body):
        self.name = name
        self.return_type = return_type
        self.paramSortType = paramSortType
        self.inherit = inherit
        self.env = env
        self.body = body
        
class ParamSymbol(Symbol):
    def __init__(self, name, typ, inherit = False, out = False):
        self.name = name
        self.typ = typ
        self.inherit = inherit
        self.out = out

class Utils():
    def infer(SymbolTable, name, typ):
        global funcDeclSort
        global notDeclaredFunction
        if notDeclaredFunction == True:
            for symbol in funcDeclSort:
                if symbol.name == name:
                    symbol.return_type = typ
                    notDeclaredFunction = False
                    return typ
        for listSymbols in SymbolTable:
            for symbol in listSymbols:
                if symbol.name == name:
                    if type(symbol) is FuncSymbol:
                        symbol.return_type = typ
                        return typ
                    else:
                        symbol.typ = typ
                        return typ

flagMainExisted = False
funcDeclSort = []
parentExisted = False
notDeclaredFunction = False

class StaticChecker(Visitor):
    preDefinedFunction = [
        FuncSymbol("readInteger", IntegerType(), [], None, [], []),
        FuncSymbol("printInteger", IntegerType(), [IntegerType()], None, [], []),
        FuncSymbol("readFloat", FloatType(), [], None, [], []),
        FuncSymbol("writeFloat", FloatType(), [FloatType()], None, [], []),
        FuncSymbol("readString", StringType(), [], None, [], []),
        FuncSymbol("printString", StringType(), [StringType()], None, [], []),
        FuncSymbol("readBoolean", BooleanType(), [], None, [], []),
        FuncSymbol("printBoolean", BooleanType(), [BooleanType()], None, [], []),
        FuncSymbol("super", StringType(), [StringType()], None, [], []),
        FuncSymbol("preventDefault", None, [], None, [], [])
    ]
    def __init__(self, ast):
        self.ast = ast

    def __del__(self):
        global flagMainExisted
        global parentExisted
        global funcDeclSort
        global notDeclaredFunction
        flagMainExisted = False
        funcDeclSort = []
        parentExisted = False
        notDeclaredFunction = False

    def check(self):
        return self.visitProgram(self.ast, StaticChecker.preDefinedFunction)

    def visitProgram(self, ast, o:object):
        global flagMainExisted
        global parentExisted
        global funcDeclSort
        global notDeclaredFunction
        o = []
        round1 = GetEnv(ast, StaticChecker.preDefinedFunction)
        funcDeclSort = round1.visit(ast, o)

        o = [StaticChecker.preDefinedFunction]
        for decl in ast.decls:
            o = self.visit(decl, o)
        for decl in o[-1]:
            if decl.name == "main":
                if type(decl.return_type) is VoidType and len(decl.paramSortType) == 0:
                    return
        flagMainExisted = False
        if flagMainExisted == False:
            raise NoEntryPoint()

    def visitFuncDecl(self, ast, o:object):
        global parentExisted
        global funcDeclSort
        for x in o[0]:
            if ast.name == x.name:
                raise Redeclared(Function(), ast.name)

        return_type = self.visit(ast.return_type, o)
        env = [[]] + o
        paramSortType = []
        body = []

        for decl in ast.params:
            env = self.visit(decl, env)
        for func in funcDeclSort:
            if func.name == ast.name:
                env = [func.paramSortType] + o
                body = func.body
                return_type = func.return_type
                break

        for param in env[0]:
            paramSortType += [param.typ]
        temp = func.body

        if ast.inherit is not None:
            for father in funcDeclSort:
                if father.name == ast.inherit:
                    parentExisted = True
                    if len(body) != 0:
                        if type(body[0]) is CallStmt:
                            if body[0].name == "preventDefault":
                                break
                            if body[0].name != "super":
                                raise InvalidStatementInFunction(body[0].name)
                        else:
                            raise InvalidStatementInFunction(ast.name)
                    self.checkVaildParent(father.paramSortType)
                    for param_father in father.paramSortType:
                                for x in env[0]:
                                    if param_father.name == x.name:
                                        if param_father.inherit is not None:
                                            raise Invalid(Parameter(), param_father.name)
                                if param_father.inherit == True:
                                    env[0] = [param_father] + env[0]
                    for child in funcDeclSort:
                        if child.name == ast.name:
                            if len(body) == 0:
                                child.body += [CallStmt("super", [])]
                            body = temp
                            if type(child.body[0]) is not CallStmt:
                                raise InvalidStatementInFunction(child.body[0])
                            if child.body[0].name != "super" and child.body[0].name != "preventDefault":
                                raise InvalidStatementInFunction(child.body[0])
                            if child.body[0].name == "super":
                                superCalledFromChild = []
                                for arg in child.body[0].args:
                                    superCalledFromChild += [self.visit(arg, env)]
                                if len(father.paramSortType) != 0 and len(superCalledFromChild) != 0:
                                    for i in range(len(superCalledFromChild)):
                                        if i == len(father.paramSortType):
                                            break
                                        childArgsType = type(superCalledFromChild[i])
                                        if type(father.paramSortType[i].typ) is AutoType:
                                            if childArgsType is BooleanType:
                                                father.paramSortType[i].typ = BooleanType()
                                            if childArgsType is StringType:
                                                father.paramSortType[i].typ = StringType()
                                            if childArgsType is IntegerType:
                                                father.paramSortType[i].typ = IntegerType()
                                            if childArgsType is FloatType:
                                                father.paramSortType[i].typ = FloatType()

                                        if childArgsType is AutoType:
                                            if type(father.paramSortType[i].typ) is StringType:
                                                childArgsType = Utils.infer(env, child.body[0].args[i].name, StringType())
                                            if type(father.paramSortType[i].typ) is BooleanType:
                                                childArgsType = Utils.infer(env, child.body[0].args[i].name, BooleanType())
                                            if type(father.paramSortType[i].typ) is IntegerType:
                                                childArgsType = Utils.infer(env, child.body[0].args[i].name, IntegerType())
                                            if type(father.paramSortType[i].typ) is FloatType:
                                                childArgsType = Utils.infer(env, child.body[0].args[i].name, FloatType())
                                        if childArgsType != type(father.paramSortType[i].typ):
                                            if childArgsType is IntegerType and type(father.paramSortType[i].typ) is FloatType:
                                                continue
                                            else:
                                                raise TypeMismatchInExpression(child.body[0].args[i])

                                if len(superCalledFromChild) != len(father.paramSortType):
                                    if len(superCalledFromChild) > len(father.paramSortType):
                                            if len(father.paramSortType) != 0:
                                                raise TypeMismatchInExpression (child.body[0].args[len(father.paramSortType)])
                                            else: raise TypeMismatchInExpression("")
                                    else:
                                        if len(superCalledFromChild) != 0:
                                            raise TypeMismatchInExpression("")

                            if child.body[0].name == "preventDefault":
                                break
                    break
            if parentExisted == False:
                raise Undeclared(Function(), ast.inherit)

        cntReturn = 0
        cntLoop = 0
        callList = ['FuncDecl']
        dive = [cntReturn, ast.name, env, callList, cntLoop]
        dive = self.visit(ast.body, dive)

        for x in funcDeclSort:
            if x.name == ast.name:
                if type(ast.return_type) is AutoType:
                    return_type = x.return_type
                    break
        o[0] = [FuncSymbol(ast.name, return_type, paramSortType, ast.inherit, env, body)] + o[0]
        parentExisted = False
        return o

    def checkVaildParent(self, o):
        size = len(o)
        for i in range(1, size):
            for j in range(0, i):
                if o[i].name == o[j].name:
                    raise Redeclared(Parameter(), o[i].name)

    def getParamType(self, ast, o):
        o = [self.visit(ast.typ, o)] + o
        return o

    def visitParamDecl(self, ast, o):
        for x in o[0]:
            if ast.name == x.name:
                raise Redeclared(Parameter(), ast.name)
        o[0] = [ParamSymbol(ast.name, ast.typ, ast.inherit, ast.out)] + o[0]
        return o

    def inferVarDecl(self, ast, init, o):
        if type(init) is StringType:
            o[0] = [Symbol(ast.name, StringType())] + o[0]
        if type(init) is IntegerType:
            o[0] = [Symbol(ast.name, IntegerType())] + o[0]
        if type(init) is FloatType:
            o[0] = [Symbol(ast.name, FloatType())] + o[0]
        if type(init) is BooleanType:
            o[0] = [Symbol(ast.name, BooleanType())] + o[0]
        if type(init) is ArrayType:
            o[0] = [Symbol(ast.name, ArrayType(init.dimensions, init.typ))] + o[0]
        return o

    def inferArrayLit(self, ast, o): pass

    def inferArrayLitEle(self, typ_, exprs): pass

    def inferFuncDecl(self, ast, typ_, o):
        global funcDeclSort
        global notDeclaredFunction
        gblScope = len(o) - 1
        ret = None
        for x in o[gblScope]:
            if x.name == ast.name:
                if type(typ_) is IntegerType:
                    ret = Utils.infer(ast.name, o, IntegerType())
                elif type(typ_) is ArrayType:
                    pass
                elif type(typ_) is StringType:
                    ret = Utils.infer(ast.name, o, StringType())
                elif type(typ_) is FloatType:
                    ret = Utils.infer(ast.name, o, FloatType())
                elif type(typ_) is BooleanType:
                    ret = Utils.infer(ast.name, o, BooleanType())
                return ret

        for x in funcDeclSort:
            if x.name == ast.name:
                notDeclaredFunction = True
                if type(typ_) is IntegerType:
                    ret = Utils.infer(funcDeclSort, ast.name, IntegerType())
                elif type(typ_) is StringType:
                    ret = Utils.infer(funcDeclSort, ast.name, StringType())
                elif type(typ_) is FloatType:
                    ret = Utils.infer(funcDeclSort, ast.name, FloatType())
                elif type(typ_) is BooleanType:
                    ret = Utils.infer(funcDeclSort, ast.name, BooleanType())
                elif type(typ_) is ArrayType:
                    pass
                return ret

        raise Undeclared(Function(), ast.name)

    def inferID(self, ast, typ_, o):
        for listSymbols in o:
            for symbol in listSymbols:
                if symbol.name == ast.name:
                    if type(typ_) is IntegerType:
                        ret = Utils.infer(o, ast.name, IntegerType())
                    elif type(typ_) is StringType:
                        ret = Utils.infer(o, ast.name, StringType())
                    elif type(typ_) is FloatType:
                        ret = Utils.infer(o, ast.name, FloatType())
                    elif type(typ_) is BooleanType:
                        ret = Utils.infer(o, ast.name, BooleanType())
                    elif type(typ_) is ArrayType: pass
                    return typ_

    def visitVarDecl(self, ast, o):
        for x in o[0]:
            if ast.name == x.name:
                raise Redeclared(Variable(), ast.name)
        typ = ast.typ
        if ast.init is not None:
            init = self.visit(ast.init, o)
            if type(typ) is AutoType:
                if type(init) is not ArrayType:
                    return self.inferVarDecl(ast, init, o)
                if type(init) is ArrayType and type(init.typ) is not AutoType:
                    return self.inferVarDecl(ast, init, o)

            if type(init) is ArrayType:
                if type(init.typ) is AutoType:
                    self.inferArrayLit(ast, o)
                if type(typ) is ArrayType:
                    if type(init.typ) != type(typ.typ) or len(init.dimensions) != len(typ.dimensions):
                        raise TypeMismatchInVarDecl(ast)
                    for i in range(len(init.dimensions)):
                        if init.dimensions[i] != typ.dimensions[i]:
                            raise TypeMismatchInVarDecl(ast)

                o[0] = [Symbol(ast.name, ArrayType(init.dimensions, init.typ))] + o[0]
                return o

            if type(init) is AutoType:
                if type(typ) is AutoType:
                    return o
                else:
                    if type(ast.init) is FuncCall:
                        init = self.inferFuncDecl(ast.init, typ, o)
                    else:
                        if type(ast.init) is UnExpr:
                            init = self.inferID(ast.init.val, typ, o)
                        else:
                            init = self.inferID(ast.name, typ, o)

            if type(typ) is FloatType and type(init) is IntegerType:
                o[0] = [Symbol(ast.name, typ)] + o[0]
                return o

            if type(typ) != type(init):
                raise TypeMismatchInVarDecl(ast)

        if type(typ) is AutoType and ast.init is None:
            raise Invalid(Variable(), ast.name)

        o[0] = [Symbol(ast.name, typ)] + o[0]
        return o

    def visitId(self, ast, o:object):
        for listSymbols in o:
            for symbol in listSymbols:
                if symbol.name == ast.name:
                    if type(symbol) is FuncSymbol:
                        return symbol.return_type
                    return symbol.typ
        raise Undeclared(Identifier(), ast.name)

    def visitAutoType(self, ast, o):
        return AutoType()

    def visitBooleanType(self, ast, o):
        return BooleanType()

    def visitVoidType(self, ast, o):
        return VoidType()

    def visitIntegerType(self, ast, o):
        return IntegerType()

    def visitFloatType(self, ast, o):
        return FloatType()

    def visitArrayType(self, ast, o):
        typ = self.visit(ast.typ, o)
        return ArrayType(ast.dimension, typ)

    def visitBinExpr(self, ast, o):
        lhs = self.visit(ast.left, o)
        rhs = self.visit(ast.right, o)
        arithmetic_op = ['*', '/', '-', '+', '%']
        bool_op = ['!', '&&', '||']
        string_op = ['::']
        relation_op = ['==', '<', '>=', '!=', '<=', '>']
        if ast.op in arithmetic_op:
            if ast.op =='%':
                if type(lhs) is AutoType:
                    lhs = Utils.infer(o, ast.left.name, IntegerType())
                if type(rhs) is AutoType:
                    rhs = Utils.infer(o, ast.right.name, IntegerType())
                if type(rhs) == IntegerType and type(lhs) == IntegerType:
                    return IntegerType()
                raise TypeMismatchInExpression(ast)

            if type(lhs) is AutoType:
                if type(rhs) is IntegerType:
                    lhs = Utils.infer(o, ast.left.name, IntegerType())
                if type(rhs) is FloatType:
                    lhs = Utils.infer(o, ast.left.name, FloatType())

            if type(rhs) is AutoType:
                if type(lhs) is IntegerType:
                    rhs = Utils.infer(o, ast.right.name, IntegerType())
                if type(lhs) is FloatType:
                    rhs = Utils.infer(o, ast.right.name, FloatType())

            if type(rhs) is not FloatType and type(rhs) is not IntegerType:
                raise TypeMismatchInExpression(ast)

            if type(lhs) is not FloatType and type(lhs) is not IntegerType:
                raise TypeMismatchInExpression(ast)

            if type(rhs) == FloatType or type(lhs) == FloatType:
                return FloatType()
            return IntegerType()

        if ast.op in string_op:
            if type(lhs) is AutoType:
                lhs = Utils.infer(o, ast.left.name, StringType())
            if type(rhs) is AutoType:
                rhs = Utils.infer(o, ast.right.name, StringType())
            if type(rhs) is not StringType or type(lhs) is not StringType:
                raise TypeMismatchInExpression(ast)
            return StringType()

        # for boolean op
        if ast.op in bool_op:
            if type(lhs) is AutoType:
                lhs = Utils.infer(o, ast.left.name, BooleanType())
            if type(rhs) is AutoType:
                rhs = Utils.infer(o, ast.right.name, BooleanType())
            if type(rhs) is not BooleanType or type(lhs) is not BooleanType:
                raise TypeMismatchInExpression(ast)
            return BooleanType()

        # for relation op
        if ast.op in relation_op:
            if ast.op in ['!=', '==']:
                if type(lhs) is AutoType:
                    if type(rhs) is IntegerType:
                        lhs = Utils.infer(o, ast.left.name, IntegerType())
                    if type(rhs) is BooleanType:
                        lhs = Utils.infer(o, ast.left.name, BooleanType())
                if type(rhs) is AutoType:
                    if type(lhs) is IntegerType:
                        rhs = Utils.infer(o, ast.right.name, IntegerType())
                    if type(lhs) is BooleanType:
                        rhs = Utils.infer(o, ast.right.name, BooleanType())

                if type(rhs) is not BooleanType and type(rhs) is not IntegerType:
                    raise TypeMismatchInExpression(ast)
                if type(lhs) is not BooleanType and type(lhs) is not IntegerType:
                    raise TypeMismatchInExpression(ast)
                return BooleanType()

            if type(rhs) is AutoType:
                if type(lhs) is IntegerType:
                    rhs = Utils.infer(o, ast.right.name, IntegerType())
                if type(lhs) is FloatType:
                    rhs = Utils.infer(o, ast.right.name, FloatType())

            if type(lhs) is AutoType:
                if type(rhs) is IntegerType:
                    lhs = Utils.infer(o, ast.left.name, IntegerType())
                if type(rhs) is FloatType:
                    lhs = Utils.infer(o, ast.left.name, FloatType())

            if type(lhs) is not FloatType and type(lhs) is not IntegerType:
                raise TypeMismatchInExpression(ast)
            if type(rhs) is not FloatType and type(rhs) is not IntegerType:
                raise TypeMismatchInExpression(ast)
            return BooleanType()

    def visitStringType(self, ast, o):
        return StringType()

    def visitUnExpr(self, ast, o):
        one = self.visit(ast.val, o)

        if ast.op in ['!']:
            if type(one) is AutoType:
                one = Utils.infer(o, ast.val.name, BooleanType())
            if type(one) != BooleanType:
                raise TypeMismatchInExpression(ast)
            return BooleanType()
        if type(one) is AutoType:
            return AutoType()
        if type(one) != IntegerType and type(one) != FloatType:
            raise TypeMismatchInExpression(ast)
        return one

    def visitArrayCell(self, ast, o):
        for listSymbols in o:
            for symbol in listSymbols:
                if symbol.name == ast.name:
                    if type(symbol.typ) is not ArrayType:
                        raise Undeclared(Variable(), type(symbol.typ))
                    cell = []
                    for expr in ast.cell:
                        typ = self.visit(expr, o)
                        if type(typ) is not IntegerType:
                            raise TypeMismatchInExpression(expr) # ele trong cell ko integer -> Mismatch
                        cell = cell + [expr]
                    futureLen = len(symbol.typ.dimensions)
                    passLen = len(cell)
                    if futureLen !=  passLen:
                        if futureLen < passLen:
                            raise TypeMismatchInExpression(ast)
                        else:
                            return ArrayType(symbol.typ.dimensions[(futureLen):], symbol.typ.typ)
                    return symbol.typ.typ
        raise Undeclared(Variable(), ast.name)

    def visitStringLit(self, ast, o):
        return StringType()

    def visitBooleanLit(self, ast, o):
        return BooleanType()

    def visitFloatLit(self, ast, o):
        return FloatType()

    def visitIntegerLit(self, ast, o):
        return IntegerType()

    def visitFuncCall(self, ast, o):
        args = ast.args
        for listSymbols in o:
            for x in listSymbols:
                if ast.name == x.name:
                    if type(x) is not FuncSymbol:
                        raise TypeMismatchInExpression(ast)
                    else:
                        if len(args) != len(x.paramSortType):
                            raise TypeMismatchInExpression(ast)
                        for i in range(0, len(args)):
                            argsType = type(self.visit(args[i], o))
                            paramType = type(x.paramSortType[i])

                            if argsType is AutoType and paramType is AutoType:
                                return

                            if paramType is AutoType:
                                if argsType is StringType:
                                    Utils.infer(x.env, x.env[i].name, StringType())
                                    x.paramSortType[i] = StringType()
                                if argsType is ArrayType:
                                    paramType = Utils.infer(o, args[i].name, paramType)
                                    x.paramSortType[i] = paramType
                                if argsType is IntegerType:
                                    Utils.infer(x.env, x.env[i].name, IntegerType())
                                    x.paramSortType[i] = IntegerType()
                                if argsType is BooleanType:
                                    Utils.infer(x.env, x.env[i].name, BooleanType())
                                    x.paramSortType[i] = BooleanType()
                                if argsType is FloatType:
                                    Utils.infer(x.env, x.env[i].name, FloatType())
                                    x.paramSortType[i] = FloatType()
                                paramType = x.paramSortType[i]

                            if argsType is AutoType:
                                if paramType is StringType:
                                    argsType = Utils.infer(o, args[i].name, StringType())
                                if paramType is ArrayType:
                                    argsType = Utils.infer(o, args[i].name, paramType)
                                argsType = type(argsType)
                                if paramType is IntegerType:
                                    argsType = Utils.infer(o, args[i].name, IntegerType())
                                if paramType is BooleanType:
                                    argsType = Utils.infer(o, args[i].name, BooleanType())
                                if paramType is FloatType:
                                    argsType = Utils.infer(o, args[i].name, FloatType())

                            if argsType != paramType:
                                if argsType is IntegerType and paramType is FloatType:
                                    continue
                                raise TypeMismatchInExpression (ast)

                    if type(x.return_type) is VoidType:
                        raise TypeMismatchInExpression(ast)
                    return x.return_type

        global notDeclaredFunction
        for x in funcDeclSort:
            if x.name == ast.name:
                if len(args) != len(x.paramSortType):
                        raise TypeMismatchInExpression(ast)
                for i in range(0, len(args)):
                    argsType = type(self.visit(args[i], o))
                    paramType = type(x.paramSortType[i].typ)

                    if argsType is AutoType and paramType is AutoType:
                        return
                    if argsType is AutoType:
                        if paramType is StringType:
                            argsType = Utils.infer(o, args[i].name, StringType())
                        if paramType is ArrayType:
                            argsType = Utils.infer(o, args[i].name, paramType)
                        if paramType is IntegerType:
                            argsType = Utils.infer(o, args[i].name, IntegerType())
                        if paramType is BooleanType:
                            argsType = Utils.infer(o, args[i].name, BooleanType())
                        if paramType is FloatType:
                            argsType = Utils.infer(o, args[i].name, FloatType())
                        argsType = type(argsType)

                    if paramType is AutoType:
                        if argsType is StringType:
                            x.paramSortType[i].typ =Utils.infer(x.env, x.env[i].name, StringType())
                        if argsType is ArrayType:
                            x.paramSortType[i].typ = Utils.infer(x.env, x.env[i].name, paramType)
                        if argsType is IntegerType:
                            x.paramSortType[i].typ = Utils.infer(x.env, x.env[i].name, IntegerType())
                        if argsType is BooleanType:
                            x.paramSortType[i].typ = Utils.infer(x.env, x.env[i].name, BooleanType())
                        if argsType is FloatType:
                            x.paramSortType[i].typ = Utils.infer(x.env, x.env[i].name, FloatType())
                        paramType = type(x.paramSortType[i].typ)

                    if argsType != paramType:
                        if argsType is IntegerType and paramType is FloatType:
                            continue
                        raise TypeMismatchInExpression (ast)
                notDeclaredFunction = True
                if type(x.return_type) is VoidType:
                    raise TypeMismatchInExpression(ast)
                return x.return_type
        raise Undeclared(Function(), ast.name)

    def visitArrayLit(self, ast, o):
        ele_type = [self.visit(exp, o) for exp in ast.explist]
        for x in ele_type:
            if type(x) is AutoType:
                pass
        tmpType = ele_type[0]
        sameType = True
        for x in ele_type:
            if type(x) is not type(tmpType):
                sameType = False
                break
        if sameType == True:
            for x in ele_type:
                if type(x) is ArrayType:
                    curInsideDim = self.visitArrayLit(ast.explist[0], o).dimensions
                    curInsideType = self.visitArrayLit(ast.explist[0], o).typ

                    for x in ast.explist[1:]:
                        if curInsideDim != self.visitArrayLit(x, o).dimensions:
                            raise IllegalArrayLiteral(ast)
                        if curInsideType != self.visitArrayLit(x, o).typ:
                            raise IllegalArrayLiteral(ast)
                    return ArrayType([len(ast.explist)] + curInsideDim, curInsideType)
                return ArrayType([len(ast.explist)], tmpType)
        raise IllegalArrayLiteral(ast)

    def visitSingleStmt(self, ast, o):
        global parentExisted
        if type(ast) is VarDecl:
            o[2] = self.visit(ast, o[2])
        elif type(ast) is ContinueStmt or type(ast) is BreakStmt:
            self.visit(ast, o)
        elif type(ast) is AssignStmt or type(ast) is CallStmt:
            if type(ast) is CallStmt:
                if ast.name is "super" or ast.name is "preventDefault":
                    raise InvalidStatementInFunction(ast)
            self.visit(ast, o[2])
        elif type(ast) is ReturnStmt:
            self.visit(ast, o)
            return o
        else:
            self.visit(ast, o)
        return o

    def visitAssignStmt(self, ast, o):
        rhs = self.visit(ast.rhs, o)
        lhs = self.visit(ast.lhs, o)

        if type(lhs) is VoidType or type(rhs) is VoidType:
            raise TypeMismatchInStatement(ast)
        if type(lhs) is ArrayType or type(rhs) is ArrayType:
            raise TypeMismatchInStatement(ast)
        if type(lhs) is AutoType:
            if type(rhs) is AutoType:
                return
            if type(rhs) is StringType:
                lhs = Utils.infer(o, ast.lhs.name, StringType())
            if type(rhs) is BooleanType:
                lhs = Utils.infer(o, ast.lhs.name, BooleanType())
            if type(rhs) is IntegerType:
                lhs = Utils.infer(o, ast.lhs.name, IntegerType())
            if type(rhs) is FloatType:
                lhs = Utils.infer(o, ast.lhs.name, FloatType())

        if type(rhs) is AutoType:
            if type(lhs) is AutoType:
                return
            if type(lhs) is StringType:
                rhs = Utils.infer(o, ast.rhs.name, StringType())
            if type(lhs) is BooleanType:
                rhs = Utils.infer(o, ast.rhs.name, BooleanType())
            if type(lhs) is IntegerType:
                rhs = Utils.infer(o, ast.rhs.name, IntegerType())
            if type(lhs) is FloatType:
                rhs = Utils.infer(o, ast.rhs.name, FloatType())

        if type(lhs) != type(rhs):
            if type(lhs) == IntegerType and type(rhs) == FloatType:
                raise TypeMismatchInStatement(ast)
            if type(lhs) == FloatType and type(rhs) == IntegerType:
                return FloatType()
            raise TypeMismatchInStatement(ast)
        return lhs

    def visitBlockStmt(self, ast, o):
        global parentExisted

        for i in range(0, len(ast.body)):
            if type(ast.body[i]) is VarDecl:
                o[2] = self.visit(ast.body[i], o[2])
            elif type(ast.body[i]) is ReturnStmt:
                self.visit(ast.body[i], o)
            elif type(ast.body[i]) is ContinueStmt or type(ast.body[i]) is BreakStmt:
                self.visit(ast.body[i], o)

            elif type(ast.body[i]) is BlockStmt:
                o[2] = [[]] + o[2]
                self.visit(ast.body[i], o)
            elif type(ast.body[i]) is AssignStmt or type(ast.body[i]) is CallStmt:
                if type(ast.body[i]) is CallStmt:
                    if ast.body[i].name is "super" or ast.body[i].name is "preventDefault":
                        if i == 0: continue
                        else: raise InvalidStatementInFunction(ast.body[i])
                self.visit(ast.body[i], o[2])
            elif type(ast.body[i]) is ForStmt or type(ast.body[i]) is WhileStmt or type(ast.body[i]) is DoWhileStmt:
                self.visit(ast.body[i], o)
            else:
                self.visit(ast.body[i], o)

        if len(o[2]) > 2:
            o[2].pop(0)
        return o

    def visitIfStmt(self, ast, o):
        condType = self.visit(ast.cond, o[2])
        if type(condType) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        o[3] = o[3] + ["IfStmt"]

        if type(ast.tstmt) is BlockStmt:
            o[2] = [[]] + o[2]
            self.visit(ast.tstmt, o)
            o[0] = 0
        else: self.visitSingleStmt(ast.tstmt, o)

        if ast.fstmt is not None:
            if type(ast.fstmt) is BlockStmt:
                o[2] = [[]] + o[2]
                self.visit(ast.fstmt, o)
                o[0] = 0
            else: self.visitSingleStmt(ast.fstmt, o)

        o[3].pop()

    def visitForStmt(self, ast, o):
        initType = self.visit(ast.init, o[2])
        if type(initType) is not IntegerType:
            raise TypeMismatchInStatement(ast)

        condType = self.visit(ast.cond, o[2])
        if type(condType) is not BooleanType:
            raise TypeMismatchInStatement(ast)

        type_update = self.visit(ast.upd, o[2])
        if type(type_update) is not IntegerType:
            raise TypeMismatchInStatement(ast)
        o[3] += ["ForStmt"]

        if type(ast.stmt) is BlockStmt:
            o[2] = [[]] + o[2]
            self.visit(ast.stmt, o)
            o[0] = 0
        else: self.visitSingleStmt(ast.stmt, o)

        o[3].pop()

    def visitWhileStmt(self, ast, o):
        condType = self.visit(ast.cond, o[2])
        if type(condType) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        o[3] += ["WhileStmt"]
        o[0] = 0
        if type(ast.stmt) is BlockStmt:
            o[2] = [[]] + o[2]
            self.visit(ast.stmt, o)
            o[0] = 0
        else: self.visitSingleStmt(ast.stmt, o)
        o[3].pop()

    def visitDoWhileStmt(self, ast, o):
        condType = self.visit(ast.cond, o[2])
        if type(condType) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        o[3] += ["DoWhileStmt"]
        o[2] = [[]] + o[2]
        self.visit(ast.stmt, o)
        o[3].pop()
        o[0] = 0

    def visitContinueStmt(self, ast, o):
        o[4] = o[4] + 1
        for x in reversed(o[3]):
            if x == "ForStmt" or x == "WhileStmt" or x == "DoWhileStmt":
                return
        raise MustInLoop(ast)

    def visitBreakStmt(self, ast, o):
        o[4] = o[4] + 1
        for x in reversed(o[3]):
            if x == "ForStmt" or x == "WhileStmt" or x == "DoWhileStmt":
                return
        raise MustInLoop(ast)

    def visitCallStmt(self, ast, o):
        global funcDeclSort
        if ast.name == "super" or ast.name == "preventDefault":
            return VoidType()
        args = ast.args

        for x in funcDeclSort:
            if x.name == ast.name:
                if len(args) != len(x.paramSortType):
                    raise TypeMismatchInStatement(ast)
                for i in range(0, len(args)):
                    argsType = type(self.visit(args[i], o))
                    paramType = type(x.paramSortType[i].typ)

                    if argsType is AutoType and paramType is AutoType:
                        return

                    if paramType is AutoType:
                        if argsType is StringType:
                            x.paramSortType[i].typ =Utils.infer(x.env, x.env[i].name, StringType())
                        if argsType is IntegerType:
                            x.paramSortType[i].typ = Utils.infer(x.env, x.env[i].name, IntegerType())
                        if argsType is BooleanType:
                            x.paramSortType[i].typ = Utils.infer(x.env, x.env[i].name, BooleanType())
                        if argsType is FloatType:
                            x.paramSortType[i].typ = Utils.infer(x.env, x.env[i].name, FloatType())
                        if argsType is ArrayType:
                            x.paramSortType[i].typ = Utils.infer(x.env, x.env[i].name, paramType)
                        paramType = type(x.paramSortType[i].typ)

                    if argsType is AutoType:
                        if paramType is StringType:
                            argsType = Utils.infer(o, args[i].name, StringType())
                        if paramType is BooleanType:
                            argsType = Utils.infer(o, args[i].name, BooleanType())
                        if paramType is IntegerType:
                            argsType = Utils.infer(o, args[i].name, IntegerType())
                        if paramType is FloatType:
                            argsType = Utils.infer(o, args[i].name, FloatType())
                        if paramType is ArrayType:
                            argsType = Utils.infer(o, args[i].name, paramType)
                        argsType = type(argsType)

                    if argsType != paramType:
                        if argsType is IntegerType and paramType is FloatType:
                            continue
                        raise TypeMismatchInStatement (ast)
                return VoidType()

        for listSymbols in o:
            for x in listSymbols:
                if ast.name == x.name:
                    if type(x) is not FuncSymbol:
                        raise TypeMismatchInStatement(ast)
                    else:
                        if len(args) != len(x.paramSortType):
                            raise TypeMismatchInStatement(ast)
                        for i in range(0, len(args)):
                            argsType = type(self.visit(args[i], o))
                            paramType = type(x.paramSortType[i])

                            if argsType is AutoType and paramType is AutoType:
                                return

                            if paramType is AutoType:
                                if argsType is StringType:
                                    Utils.infer(x.env, x.env[i].name, StringType())
                                if argsType is IntegerType:
                                    Utils.infer(x.env, x.env[i].name, IntegerType())
                                    x.paramSortType[i] = IntegerType()
                                if argsType is FloatType:
                                    Utils.infer(x.env, x.env[i].name, FloatType())
                                    x.paramSortType[i] = FloatType()
                                if argsType is ArrayType:
                                    paramType = Utils.infer(o, args[i].name, paramType)
                                    x.paramSortType[i] = paramType
                                if argsType is BooleanType:
                                    Utils.infer(x.env, x.env[i].name, BooleanType())
                                    x.paramSortType[i] = BooleanType()
                                    x.paramSortType[i] = StringType()
                                paramType = x.paramSortType[i]

                            if argsType is AutoType:
                                if paramType is IntegerType:
                                    argsType = Utils.infer(o, args[i].name, IntegerType())
                                if paramType is BooleanType:
                                    argsType = Utils.infer(o, args[i].name, BooleanType())
                                if paramType is FloatType:
                                    argsType = Utils.infer(o, args[i].name, FloatType())
                                if paramType is StringType:
                                    argsType = Utils.infer(o, args[i].name, StringType())
                                if paramType is ArrayType:
                                    argsType = Utils.infer(o, args[i].name, paramType)
                                argsType = type(argsType)

                            if argsType != paramType:
                                if argsType is IntegerType and paramType is FloatType:
                                    continue
                                raise TypeMismatchInStatement (ast)
                        return VoidType()

        raise Undeclared(Function(), ast.name)

    def visitReturnStmt(self, ast, o):
        o[0] = o[0] + 1
        typ = None
        if o[0] == 1:
            for x in funcDeclSort:
                if x.name == o[1]:
                    if ast.expr is None:
                        typ = VoidType()
                    else: typ = self.visit(ast.expr, o[2])
                    if type(x.return_type) is AutoType:
                        x.return_type = typ
                    if type(x.return_type) is FloatType and type(typ) is IntegerType:
                        return x.return_type
                    if type(x.return_type) != type(typ):
                        raise TypeMismatchInStatement(ast)
                    return typ
        for x in funcDeclSort:
            if x.name == o[1]:
                if ast.expr is None:
                    typ = VoidType()
                else: typ = self.visit(ast.expr, o[2])
                if type(x.return_type) != type(typ):
                    raise TypeMismatchInStatement(ast)
        return typ

class GetEnv(Visitor):
    def __init__(self, ast, preDefined):
        self.ast = ast
        self.preDefined = preDefined
    def check(self):
        return self.visitProgram(self.ast, self.preDefined)
    def visitProgram(self, ast, o:object):
        for decl in ast.decls:
            if type(decl) is FuncDecl:
                o = self.visit(decl, o)
        return o
    def visitFuncDecl(self, ast, o):
        if ast.name in o:
            return o
        return_type = ast.return_type
        global flagMainExisted
        if ast.name == 'main':
            if type(return_type) == VoidType and len(ast.params) == 0:
                flagMainExisted = True
        paramSortType = []
        for decl in ast.params: # to get typ order.
            paramSortType = self.visit(decl, paramSortType)
        body = self.visit(ast.body, o)
        o = [FuncSymbol(ast.name, return_type, paramSortType, ast.inherit, [], body)] + o
        return o

    def visitParamDecl(self, ast, o):
        o = o + [ParamSymbol(ast.name, self.visit(ast.typ, o), ast.inherit, ast.out)]
        return o

    def visitIntegerType(self, ast, o):
        return IntegerType()

    def visitFloatType(self, ast, o):
        return FloatType()

    def visitBooleanType(self, ast, o):
        return BooleanType()

    def visitStringType(self, ast, o):
        return StringType()

    def visitArrayType(self, ast, o):
        typ = self.visit(ast.typ, o)
        return ArrayType(ast.dimensions, typ)

    def visitAutoType(self, ast, o):
        return AutoType()

    def visitVoidType(self, ast, o):
        return VoidType()
    def visitBlockStmt(self, ast, param):
        return ast.body

