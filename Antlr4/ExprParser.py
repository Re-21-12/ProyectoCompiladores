# Generated from Expr.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,31,163,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,
        2,5,2,44,8,2,10,2,12,2,47,9,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,56,
        8,3,1,4,1,4,1,4,1,4,5,4,62,8,4,10,4,12,4,65,9,4,1,4,1,4,3,4,69,8,
        4,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,
        7,1,7,1,8,1,8,1,8,1,8,1,8,3,8,93,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,
        1,10,1,10,1,10,1,10,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,13,
        1,13,1,13,1,13,5,13,118,8,13,10,13,12,13,121,9,13,1,13,1,13,1,13,
        5,13,126,8,13,10,13,12,13,129,9,13,1,14,1,14,1,14,5,14,134,8,14,
        10,14,12,14,137,9,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,3,15,152,8,15,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,3,16,161,8,16,1,16,0,1,26,17,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,0,4,1,0,7,8,1,0,14,15,2,0,18,21,24,25,1,0,16,17,166,
        0,34,1,0,0,0,2,37,1,0,0,0,4,45,1,0,0,0,6,55,1,0,0,0,8,57,1,0,0,0,
        10,70,1,0,0,0,12,73,1,0,0,0,14,82,1,0,0,0,16,92,1,0,0,0,18,94,1,
        0,0,0,20,100,1,0,0,0,22,105,1,0,0,0,24,107,1,0,0,0,26,113,1,0,0,
        0,28,130,1,0,0,0,30,151,1,0,0,0,32,160,1,0,0,0,34,35,3,2,1,0,35,
        36,5,0,0,1,36,1,1,0,0,0,37,38,5,27,0,0,38,39,5,12,0,0,39,40,3,4,
        2,0,40,41,5,13,0,0,41,3,1,0,0,0,42,44,3,6,3,0,43,42,1,0,0,0,44,47,
        1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,5,1,0,0,0,47,45,1,0,0,0,48,
        56,3,8,4,0,49,56,3,10,5,0,50,56,3,12,6,0,51,56,3,20,10,0,52,56,3,
        18,9,0,53,56,3,24,12,0,54,56,3,32,16,0,55,48,1,0,0,0,55,49,1,0,0,
        0,55,50,1,0,0,0,55,51,1,0,0,0,55,52,1,0,0,0,55,53,1,0,0,0,55,54,
        1,0,0,0,56,7,1,0,0,0,57,58,5,1,0,0,58,63,3,14,7,0,59,60,5,2,0,0,
        60,62,3,14,7,0,61,59,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,
        0,0,0,64,68,1,0,0,0,65,63,1,0,0,0,66,67,5,3,0,0,67,69,3,16,8,0,68,
        66,1,0,0,0,68,69,1,0,0,0,69,9,1,0,0,0,70,71,5,4,0,0,71,72,3,14,7,
        0,72,11,1,0,0,0,73,74,5,5,0,0,74,75,5,10,0,0,75,76,3,18,9,0,76,77,
        3,26,13,0,77,78,5,26,0,0,78,79,3,32,16,0,79,80,5,11,0,0,80,81,3,
        16,8,0,81,13,1,0,0,0,82,83,5,10,0,0,83,84,3,26,13,0,84,85,5,11,0,
        0,85,86,3,16,8,0,86,15,1,0,0,0,87,88,5,12,0,0,88,89,3,4,2,0,89,90,
        5,13,0,0,90,93,1,0,0,0,91,93,3,6,3,0,92,87,1,0,0,0,92,91,1,0,0,0,
        93,17,1,0,0,0,94,95,5,29,0,0,95,96,3,22,11,0,96,97,5,9,0,0,97,98,
        3,26,13,0,98,99,5,26,0,0,99,19,1,0,0,0,100,101,5,29,0,0,101,102,
        5,9,0,0,102,103,3,26,13,0,103,104,5,26,0,0,104,21,1,0,0,0,105,106,
        7,0,0,0,106,23,1,0,0,0,107,108,5,6,0,0,108,109,5,10,0,0,109,110,
        3,26,13,0,110,111,5,11,0,0,111,112,5,26,0,0,112,25,1,0,0,0,113,114,
        6,13,-1,0,114,119,3,28,14,0,115,116,7,1,0,0,116,118,3,28,14,0,117,
        115,1,0,0,0,118,121,1,0,0,0,119,117,1,0,0,0,119,120,1,0,0,0,120,
        127,1,0,0,0,121,119,1,0,0,0,122,123,10,2,0,0,123,124,7,2,0,0,124,
        126,3,26,13,3,125,122,1,0,0,0,126,129,1,0,0,0,127,125,1,0,0,0,127,
        128,1,0,0,0,128,27,1,0,0,0,129,127,1,0,0,0,130,135,3,30,15,0,131,
        132,7,3,0,0,132,134,3,30,15,0,133,131,1,0,0,0,134,137,1,0,0,0,135,
        133,1,0,0,0,135,136,1,0,0,0,136,29,1,0,0,0,137,135,1,0,0,0,138,139,
        5,15,0,0,139,152,3,30,15,0,140,141,5,29,0,0,141,152,5,22,0,0,142,
        143,5,29,0,0,143,152,5,23,0,0,144,145,5,10,0,0,145,146,3,26,13,0,
        146,147,5,11,0,0,147,152,1,0,0,0,148,152,5,28,0,0,149,152,5,30,0,
        0,150,152,5,29,0,0,151,138,1,0,0,0,151,140,1,0,0,0,151,142,1,0,0,
        0,151,144,1,0,0,0,151,148,1,0,0,0,151,149,1,0,0,0,151,150,1,0,0,
        0,152,31,1,0,0,0,153,154,5,29,0,0,154,155,5,9,0,0,155,161,3,26,13,
        0,156,157,5,29,0,0,157,161,5,22,0,0,158,159,5,29,0,0,159,161,5,23,
        0,0,160,153,1,0,0,0,160,156,1,0,0,0,160,158,1,0,0,0,161,33,1,0,0,
        0,10,45,55,63,68,92,119,127,135,151,160
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else if'", "'else'", "'while'", 
                     "'for'", "'mostrar'", "'entero'", "'decimal'", "'='", 
                     "'('", "')'", "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", 
                     "'<'", "'>'", "'<='", "'>='", "'++'", "'--'", "'=='", 
                     "'!='", "';'", "'main'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE_IF", "ELSE", "WHILE", "FOR", 
                      "MOSTRAR", "TIPO_ENTERO", "TIPO_DECIMAL", "ASIGNACION", 
                      "PARENTESIS_INICIAL", "PARENTESIS_FINAL", "LLAVES_INICIAL", 
                      "LLAVES_FINAL", "MAS", "MENOS", "MULTIPLICACION", 
                      "DIVISION", "MENOR_QUE", "MAYOR_QUE", "MENOR_IGUAL_QUE", 
                      "MAYOR_IGUAL_QUE", "MASMAS", "MENOSMENOS", "IGUAL", 
                      "DIFERENTE", "PUNTO_Y_COMA", "MAIN", "NUMERO", "VARIABLE", 
                      "DECIMAL", "SIN_ESPACIO" ]

    RULE_gramatica = 0
    RULE_programa = 1
    RULE_bloque = 2
    RULE_sentencia = 3
    RULE_sentencia_if = 4
    RULE_sentencia_while = 5
    RULE_sentencia_for = 6
    RULE_bloque_condicional = 7
    RULE_bloque_de_sentencia = 8
    RULE_declaracion = 9
    RULE_reasignacion = 10
    RULE_tipo = 11
    RULE_mostrar = 12
    RULE_expr = 13
    RULE_term = 14
    RULE_factor = 15
    RULE_actualizacion = 16

    ruleNames =  [ "gramatica", "programa", "bloque", "sentencia", "sentencia_if", 
                   "sentencia_while", "sentencia_for", "bloque_condicional", 
                   "bloque_de_sentencia", "declaracion", "reasignacion", 
                   "tipo", "mostrar", "expr", "term", "factor", "actualizacion" ]

    EOF = Token.EOF
    IF=1
    ELSE_IF=2
    ELSE=3
    WHILE=4
    FOR=5
    MOSTRAR=6
    TIPO_ENTERO=7
    TIPO_DECIMAL=8
    ASIGNACION=9
    PARENTESIS_INICIAL=10
    PARENTESIS_FINAL=11
    LLAVES_INICIAL=12
    LLAVES_FINAL=13
    MAS=14
    MENOS=15
    MULTIPLICACION=16
    DIVISION=17
    MENOR_QUE=18
    MAYOR_QUE=19
    MENOR_IGUAL_QUE=20
    MAYOR_IGUAL_QUE=21
    MASMAS=22
    MENOSMENOS=23
    IGUAL=24
    DIFERENTE=25
    PUNTO_Y_COMA=26
    MAIN=27
    NUMERO=28
    VARIABLE=29
    DECIMAL=30
    SIN_ESPACIO=31

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class GramaticaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def programa(self):
            return self.getTypedRuleContext(ExprParser.ProgramaContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_gramatica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGramatica" ):
                listener.enterGramatica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGramatica" ):
                listener.exitGramatica(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGramatica" ):
                return visitor.visitGramatica(self)
            else:
                return visitor.visitChildren(self)




    def gramatica(self):

        localctx = ExprParser.GramaticaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_gramatica)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.programa()
            self.state = 35
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAIN(self):
            return self.getToken(ExprParser.MAIN, 0)

        def LLAVES_INICIAL(self):
            return self.getToken(ExprParser.LLAVES_INICIAL, 0)

        def bloque(self):
            return self.getTypedRuleContext(ExprParser.BloqueContext,0)


        def LLAVES_FINAL(self):
            return self.getToken(ExprParser.LLAVES_FINAL, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = ExprParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(ExprParser.MAIN)
            self.state = 38
            self.match(ExprParser.LLAVES_INICIAL)
            self.state = 39
            self.bloque()
            self.state = 40
            self.match(ExprParser.LLAVES_FINAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(ExprParser.SentenciaContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = ExprParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 536871026) != 0):
                self.state = 42
                self.sentencia()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentencia_if(self):
            return self.getTypedRuleContext(ExprParser.Sentencia_ifContext,0)


        def sentencia_while(self):
            return self.getTypedRuleContext(ExprParser.Sentencia_whileContext,0)


        def sentencia_for(self):
            return self.getTypedRuleContext(ExprParser.Sentencia_forContext,0)


        def reasignacion(self):
            return self.getTypedRuleContext(ExprParser.ReasignacionContext,0)


        def declaracion(self):
            return self.getTypedRuleContext(ExprParser.DeclaracionContext,0)


        def mostrar(self):
            return self.getTypedRuleContext(ExprParser.MostrarContext,0)


        def actualizacion(self):
            return self.getTypedRuleContext(ExprParser.ActualizacionContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia" ):
                return visitor.visitSentencia(self)
            else:
                return visitor.visitChildren(self)




    def sentencia(self):

        localctx = ExprParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_sentencia)
        try:
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.sentencia_if()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.sentencia_while()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 50
                self.sentencia_for()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 51
                self.reasignacion()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 52
                self.declaracion()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 53
                self.mostrar()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 54
                self.actualizacion()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sentencia_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ExprParser.IF, 0)

        def bloque_condicional(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.Bloque_condicionalContext)
            else:
                return self.getTypedRuleContext(ExprParser.Bloque_condicionalContext,i)


        def ELSE_IF(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ELSE_IF)
            else:
                return self.getToken(ExprParser.ELSE_IF, i)

        def ELSE(self):
            return self.getToken(ExprParser.ELSE, 0)

        def bloque_de_sentencia(self):
            return self.getTypedRuleContext(ExprParser.Bloque_de_sentenciaContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_sentencia_if

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia_if" ):
                listener.enterSentencia_if(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia_if" ):
                listener.exitSentencia_if(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia_if" ):
                return visitor.visitSentencia_if(self)
            else:
                return visitor.visitChildren(self)




    def sentencia_if(self):

        localctx = ExprParser.Sentencia_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_sentencia_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(ExprParser.IF)
            self.state = 58
            self.bloque_condicional()
            self.state = 63
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 59
                    self.match(ExprParser.ELSE_IF)
                    self.state = 60
                    self.bloque_condicional() 
                self.state = 65
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 68
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 66
                self.match(ExprParser.ELSE)
                self.state = 67
                self.bloque_de_sentencia()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sentencia_whileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(ExprParser.WHILE, 0)

        def bloque_condicional(self):
            return self.getTypedRuleContext(ExprParser.Bloque_condicionalContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_sentencia_while

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia_while" ):
                listener.enterSentencia_while(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia_while" ):
                listener.exitSentencia_while(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia_while" ):
                return visitor.visitSentencia_while(self)
            else:
                return visitor.visitChildren(self)




    def sentencia_while(self):

        localctx = ExprParser.Sentencia_whileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_sentencia_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(ExprParser.WHILE)
            self.state = 71
            self.bloque_condicional()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sentencia_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ExprParser.FOR, 0)

        def PARENTESIS_INICIAL(self):
            return self.getToken(ExprParser.PARENTESIS_INICIAL, 0)

        def declaracion(self):
            return self.getTypedRuleContext(ExprParser.DeclaracionContext,0)


        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def PUNTO_Y_COMA(self):
            return self.getToken(ExprParser.PUNTO_Y_COMA, 0)

        def actualizacion(self):
            return self.getTypedRuleContext(ExprParser.ActualizacionContext,0)


        def PARENTESIS_FINAL(self):
            return self.getToken(ExprParser.PARENTESIS_FINAL, 0)

        def bloque_de_sentencia(self):
            return self.getTypedRuleContext(ExprParser.Bloque_de_sentenciaContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_sentencia_for

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia_for" ):
                listener.enterSentencia_for(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia_for" ):
                listener.exitSentencia_for(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia_for" ):
                return visitor.visitSentencia_for(self)
            else:
                return visitor.visitChildren(self)




    def sentencia_for(self):

        localctx = ExprParser.Sentencia_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_sentencia_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(ExprParser.FOR)
            self.state = 74
            self.match(ExprParser.PARENTESIS_INICIAL)
            self.state = 75
            self.declaracion()
            self.state = 76
            self.expr(0)
            self.state = 77
            self.match(ExprParser.PUNTO_Y_COMA)
            self.state = 78
            self.actualizacion()
            self.state = 79
            self.match(ExprParser.PARENTESIS_FINAL)
            self.state = 80
            self.bloque_de_sentencia()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bloque_condicionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARENTESIS_INICIAL(self):
            return self.getToken(ExprParser.PARENTESIS_INICIAL, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def PARENTESIS_FINAL(self):
            return self.getToken(ExprParser.PARENTESIS_FINAL, 0)

        def bloque_de_sentencia(self):
            return self.getTypedRuleContext(ExprParser.Bloque_de_sentenciaContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_bloque_condicional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque_condicional" ):
                listener.enterBloque_condicional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque_condicional" ):
                listener.exitBloque_condicional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque_condicional" ):
                return visitor.visitBloque_condicional(self)
            else:
                return visitor.visitChildren(self)




    def bloque_condicional(self):

        localctx = ExprParser.Bloque_condicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_bloque_condicional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(ExprParser.PARENTESIS_INICIAL)
            self.state = 83
            self.expr(0)
            self.state = 84
            self.match(ExprParser.PARENTESIS_FINAL)
            self.state = 85
            self.bloque_de_sentencia()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bloque_de_sentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLAVES_INICIAL(self):
            return self.getToken(ExprParser.LLAVES_INICIAL, 0)

        def bloque(self):
            return self.getTypedRuleContext(ExprParser.BloqueContext,0)


        def LLAVES_FINAL(self):
            return self.getToken(ExprParser.LLAVES_FINAL, 0)

        def sentencia(self):
            return self.getTypedRuleContext(ExprParser.SentenciaContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_bloque_de_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque_de_sentencia" ):
                listener.enterBloque_de_sentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque_de_sentencia" ):
                listener.exitBloque_de_sentencia(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque_de_sentencia" ):
                return visitor.visitBloque_de_sentencia(self)
            else:
                return visitor.visitChildren(self)




    def bloque_de_sentencia(self):

        localctx = ExprParser.Bloque_de_sentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_bloque_de_sentencia)
        try:
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.match(ExprParser.LLAVES_INICIAL)
                self.state = 88
                self.bloque()
                self.state = 89
                self.match(ExprParser.LLAVES_FINAL)
                pass
            elif token in [1, 4, 5, 6, 29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.sentencia()
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


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(ExprParser.VARIABLE, 0)

        def tipo(self):
            return self.getTypedRuleContext(ExprParser.TipoContext,0)


        def ASIGNACION(self):
            return self.getToken(ExprParser.ASIGNACION, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def PUNTO_Y_COMA(self):
            return self.getToken(ExprParser.PUNTO_Y_COMA, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion(self):

        localctx = ExprParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(ExprParser.VARIABLE)
            self.state = 95
            self.tipo()
            self.state = 96
            self.match(ExprParser.ASIGNACION)
            self.state = 97
            self.expr(0)
            self.state = 98
            self.match(ExprParser.PUNTO_Y_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReasignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(ExprParser.VARIABLE, 0)

        def ASIGNACION(self):
            return self.getToken(ExprParser.ASIGNACION, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def PUNTO_Y_COMA(self):
            return self.getToken(ExprParser.PUNTO_Y_COMA, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_reasignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReasignacion" ):
                listener.enterReasignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReasignacion" ):
                listener.exitReasignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReasignacion" ):
                return visitor.visitReasignacion(self)
            else:
                return visitor.visitChildren(self)




    def reasignacion(self):

        localctx = ExprParser.ReasignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_reasignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(ExprParser.VARIABLE)
            self.state = 101
            self.match(ExprParser.ASIGNACION)
            self.state = 102
            self.expr(0)
            self.state = 103
            self.match(ExprParser.PUNTO_Y_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIPO_ENTERO(self):
            return self.getToken(ExprParser.TIPO_ENTERO, 0)

        def TIPO_DECIMAL(self):
            return self.getToken(ExprParser.TIPO_DECIMAL, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo" ):
                return visitor.visitTipo(self)
            else:
                return visitor.visitChildren(self)




    def tipo(self):

        localctx = ExprParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            _la = self._input.LA(1)
            if not(_la==7 or _la==8):
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


    class MostrarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MOSTRAR(self):
            return self.getToken(ExprParser.MOSTRAR, 0)

        def PARENTESIS_INICIAL(self):
            return self.getToken(ExprParser.PARENTESIS_INICIAL, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def PARENTESIS_FINAL(self):
            return self.getToken(ExprParser.PARENTESIS_FINAL, 0)

        def PUNTO_Y_COMA(self):
            return self.getToken(ExprParser.PUNTO_Y_COMA, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_mostrar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMostrar" ):
                listener.enterMostrar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMostrar" ):
                listener.exitMostrar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMostrar" ):
                return visitor.visitMostrar(self)
            else:
                return visitor.visitChildren(self)




    def mostrar(self):

        localctx = ExprParser.MostrarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_mostrar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(ExprParser.MOSTRAR)
            self.state = 108
            self.match(ExprParser.PARENTESIS_INICIAL)
            self.state = 109
            self.expr(0)
            self.state = 110
            self.match(ExprParser.PARENTESIS_FINAL)
            self.state = 111
            self.match(ExprParser.PUNTO_Y_COMA)
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

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.TermContext)
            else:
                return self.getTypedRuleContext(ExprParser.TermContext,i)


        def MAS(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.MAS)
            else:
                return self.getToken(ExprParser.MAS, i)

        def MENOS(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.MENOS)
            else:
                return self.getToken(ExprParser.MENOS, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def MENOR_QUE(self):
            return self.getToken(ExprParser.MENOR_QUE, 0)

        def MAYOR_QUE(self):
            return self.getToken(ExprParser.MAYOR_QUE, 0)

        def MENOR_IGUAL_QUE(self):
            return self.getToken(ExprParser.MENOR_IGUAL_QUE, 0)

        def MAYOR_IGUAL_QUE(self):
            return self.getToken(ExprParser.MAYOR_IGUAL_QUE, 0)

        def IGUAL(self):
            return self.getToken(ExprParser.IGUAL, 0)

        def DIFERENTE(self):
            return self.getToken(ExprParser.DIFERENTE, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.term()
            self.state = 119
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 115
                    _la = self._input.LA(1)
                    if not(_la==14 or _la==15):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 116
                    self.term() 
                self.state = 121
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self._ctx.stop = self._input.LT(-1)
            self.state = 127
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 122
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 123
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 54263808) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 124
                    self.expr(3) 
                self.state = 129
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.FactorContext)
            else:
                return self.getTypedRuleContext(ExprParser.FactorContext,i)


        def MULTIPLICACION(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.MULTIPLICACION)
            else:
                return self.getToken(ExprParser.MULTIPLICACION, i)

        def DIVISION(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.DIVISION)
            else:
                return self.getToken(ExprParser.DIVISION, i)

        def getRuleIndex(self):
            return ExprParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = ExprParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.factor()
            self.state = 135
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 131
                    _la = self._input.LA(1)
                    if not(_la==16 or _la==17):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 132
                    self.factor() 
                self.state = 137
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MENOS(self):
            return self.getToken(ExprParser.MENOS, 0)

        def factor(self):
            return self.getTypedRuleContext(ExprParser.FactorContext,0)


        def VARIABLE(self):
            return self.getToken(ExprParser.VARIABLE, 0)

        def MASMAS(self):
            return self.getToken(ExprParser.MASMAS, 0)

        def MENOSMENOS(self):
            return self.getToken(ExprParser.MENOSMENOS, 0)

        def PARENTESIS_INICIAL(self):
            return self.getToken(ExprParser.PARENTESIS_INICIAL, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def PARENTESIS_FINAL(self):
            return self.getToken(ExprParser.PARENTESIS_FINAL, 0)

        def NUMERO(self):
            return self.getToken(ExprParser.NUMERO, 0)

        def DECIMAL(self):
            return self.getToken(ExprParser.DECIMAL, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = ExprParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_factor)
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.match(ExprParser.MENOS)
                self.state = 139
                self.factor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.match(ExprParser.VARIABLE)
                self.state = 141
                self.match(ExprParser.MASMAS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 142
                self.match(ExprParser.VARIABLE)
                self.state = 143
                self.match(ExprParser.MENOSMENOS)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 144
                self.match(ExprParser.PARENTESIS_INICIAL)
                self.state = 145
                self.expr(0)
                self.state = 146
                self.match(ExprParser.PARENTESIS_FINAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 148
                self.match(ExprParser.NUMERO)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 149
                self.match(ExprParser.DECIMAL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 150
                self.match(ExprParser.VARIABLE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActualizacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(ExprParser.VARIABLE, 0)

        def ASIGNACION(self):
            return self.getToken(ExprParser.ASIGNACION, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def MASMAS(self):
            return self.getToken(ExprParser.MASMAS, 0)

        def MENOSMENOS(self):
            return self.getToken(ExprParser.MENOSMENOS, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_actualizacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActualizacion" ):
                listener.enterActualizacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActualizacion" ):
                listener.exitActualizacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActualizacion" ):
                return visitor.visitActualizacion(self)
            else:
                return visitor.visitChildren(self)




    def actualizacion(self):

        localctx = ExprParser.ActualizacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_actualizacion)
        try:
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.match(ExprParser.VARIABLE)
                self.state = 154
                self.match(ExprParser.ASIGNACION)
                self.state = 155
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.match(ExprParser.VARIABLE)
                self.state = 157
                self.match(ExprParser.MASMAS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 158
                self.match(ExprParser.VARIABLE)
                self.state = 159
                self.match(ExprParser.MENOSMENOS)
                pass


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
        self._predicates[13] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




