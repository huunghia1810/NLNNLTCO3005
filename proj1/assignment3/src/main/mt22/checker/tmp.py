def visitFuncDecl(self, ast, o: object):
    global funcDeclOrder
    global fatherExist
    for x in o[0]:
        if ast.name == x.name:
            raise Redeclared(Function(), ast.name)
    return_type = self.visit(ast.return_type, o)
    env = [[]] + o
    paramTypeOrder = []
    body = []
    for decl in ast.params:  # to check if redeclared happen in parameter
        env = self.visit(decl, env)
    for func in funcDeclOrder:  # No error ? We inherit the order from round 1 !
        if func.name == ast.name:
            env = [func.paramTypeOrder] + o
            body = func.body
            return_type = func.return_type
            break
    for param in env[0]:
        paramTypeOrder += [param.typ]
    temp = func.body
    if ast.inherit is not None:
        for father in funcDeclOrder:
            if father.name == ast.inherit:
                fatherExist = True
                if len(body) != 0:
                    if type(body[0]) is CallStmt:
                        if body[0].name == "preventDefault":
                            break
                        if body[0].name != "super":
                            raise InvalidStatementInFunction(body[0].name)
                    else:
                        raise InvalidStatementInFunction(ast.name)
                self.checkVaildParent(father.paramTypeOrder)
                for param_father in father.paramTypeOrder:
                    for x in env[0]:
                        if param_father.name == x.name:
                            if param_father.inherit is not None:
                                raise Invalid(Parameter(), param_father.name)
                            # else: raise Redeclared(Parameter(),param_father.name)
                    if param_father.inherit == True:
                        env[0] = [param_father] + env[0]
                for child in funcDeclOrder:
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
                                # vaildFirstStmt = False
                            if len(father.paramTypeOrder) != 0 and len(superCalledFromChild) != 0:
                                for i in range(len(superCalledFromChild)):
                                    if i == len(father.paramTypeOrder):
                                        break
                                    superfromChild_arg_type = type(superCalledFromChild[i])
                                    if type(father.paramTypeOrder[i].typ) is AutoType:
                                        if superfromChild_arg_type is BooleanType:
                                            father.paramTypeOrder[i].typ = BooleanType()
                                        if superfromChild_arg_type is IntegerType:
                                            father.paramTypeOrder[i].typ = IntegerType()
                                        if superfromChild_arg_type is FloatType:
                                            father.paramTypeOrder[i].typ = FloatType()
                                        if superfromChild_arg_type is StringType:
                                            father.paramTypeOrder[i].typ = StringType()

                                    if superfromChild_arg_type is AutoType:
                                        if type(father.paramTypeOrder[i].typ) is BooleanType:
                                            superfromChild_arg_type = Utils.infer(env, child.body[0].args[i].name,
                                                                                  BooleanType())
                                        if type(father.paramTypeOrder[i].typ) is IntegerType:
                                            superfromChild_arg_type = Utils.infer(env, child.body[0].args[i].name,
                                                                                  IntegerType())
                                        if type(father.paramTypeOrder[i].typ) is FloatType:
                                            superfromChild_arg_type = Utils.infer(env, child.body[0].args[i].name,
                                                                                  FloatType())
                                        if type(father.paramTypeOrder[i].typ) is StringType:
                                            superfromChild_arg_type = Utils.infer(env, child.body[0].args[i].name,
                                                                                  StringType())
                                    if superfromChild_arg_type != type(father.paramTypeOrder[i].typ):
                                        if superfromChild_arg_type is IntegerType and type(
                                                father.paramTypeOrder[i].typ) is FloatType:
                                            continue
                                        else:
                                            raise TypeMismatchInExpression(child.body[0].args[i])
                            if len(superCalledFromChild) != len(father.paramTypeOrder):
                                if len(superCalledFromChild) > len(father.paramTypeOrder):
                                    if len(father.paramTypeOrder) != 0:
                                        raise TypeMismatchInExpression(child.body[0].args[len(father.paramTypeOrder)])
                                    else:
                                        raise TypeMismatchInExpression("")
                                else:
                                    if len(superCalledFromChild) != 0:
                                        raise TypeMismatchInExpression("")
                        if child.body[0].name == "preventDefault":
                            break
                break
        if fatherExist == False:
            raise Undeclared(Function(), ast.inherit)
    cntReturn = 0
    cntLoop = 0
    callList = ['FuncDecl']
    dive = [cntReturn, ast.name, env, callList, cntLoop]
    dive = self.visit(ast.body, dive)
    # raise Undeclared(Function(),ast.name)
    for x in funcDeclOrder:
        if x.name == ast.name:
            if type(ast.return_type) is AutoType:
                return_type = x.return_type
                break
    o[0] = [FuncSymbol(ast.name, return_type, paramTypeOrder, ast.inherit, env, body)] + o[0]
    # callOrder = []
    fatherExist = False
    return o