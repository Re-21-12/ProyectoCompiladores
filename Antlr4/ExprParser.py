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
        4,1,27,148,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,5,2,39,8,2,10,2,12,2,42,
        9,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,3,4,54,8,4,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,
        7,1,7,3,7,76,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,5,9,
        89,8,9,10,9,12,9,92,9,9,1,9,1,9,3,9,96,8,9,1,10,1,10,1,10,1,10,1,
        10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,
        12,1,12,5,12,117,8,12,10,12,12,12,120,9,12,1,12,3,12,123,8,12,1,
        13,1,13,1,13,5,13,128,8,13,10,13,12,13,131,9,13,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,146,8,14,1,
        14,0,0,15,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,0,2,1,0,13,14,
        1,0,15,16,149,0,30,1,0,0,0,2,33,1,0,0,0,4,40,1,0,0,0,6,43,1,0,0,
        0,8,53,1,0,0,0,10,55,1,0,0,0,12,65,1,0,0,0,14,75,1,0,0,0,16,77,1,
        0,0,0,18,83,1,0,0,0,20,97,1,0,0,0,22,103,1,0,0,0,24,113,1,0,0,0,
        26,124,1,0,0,0,28,145,1,0,0,0,30,31,3,2,1,0,31,32,5,0,0,1,32,1,1,
        0,0,0,33,34,5,11,0,0,34,35,3,4,2,0,35,36,5,12,0,0,36,3,1,0,0,0,37,
        39,3,14,7,0,38,37,1,0,0,0,39,42,1,0,0,0,40,38,1,0,0,0,40,41,1,0,
        0,0,41,5,1,0,0,0,42,40,1,0,0,0,43,44,5,9,0,0,44,45,3,24,12,0,45,
        46,5,10,0,0,46,47,3,8,4,0,47,7,1,0,0,0,48,49,5,11,0,0,49,50,3,4,
        2,0,50,51,5,12,0,0,51,54,1,0,0,0,52,54,3,14,7,0,53,48,1,0,0,0,53,
        52,1,0,0,0,54,9,1,0,0,0,55,56,5,8,0,0,56,57,5,9,0,0,57,58,3,12,6,
        0,58,59,5,25,0,0,59,60,3,24,12,0,60,61,5,25,0,0,61,62,3,24,12,0,
        62,63,5,10,0,0,63,64,3,8,4,0,64,11,1,0,0,0,65,66,5,2,0,0,66,67,5,
        4,0,0,67,68,3,24,12,0,68,69,5,25,0,0,69,13,1,0,0,0,70,76,3,12,6,
        0,71,76,3,18,9,0,72,76,3,20,10,0,73,76,3,22,11,0,74,76,3,16,8,0,
        75,70,1,0,0,0,75,71,1,0,0,0,75,72,1,0,0,0,75,73,1,0,0,0,75,74,1,
        0,0,0,76,15,1,0,0,0,77,78,5,26,0,0,78,79,5,9,0,0,79,80,3,24,12,0,
        80,81,5,10,0,0,81,82,5,25,0,0,82,17,1,0,0,0,83,84,5,5,0,0,84,90,
        3,6,3,0,85,86,5,6,0,0,86,87,5,5,0,0,87,89,3,6,3,0,88,85,1,0,0,0,
        89,92,1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,95,1,0,0,0,92,90,1,
        0,0,0,93,94,5,6,0,0,94,96,3,8,4,0,95,93,1,0,0,0,95,96,1,0,0,0,96,
        19,1,0,0,0,97,98,5,7,0,0,98,99,5,9,0,0,99,100,3,24,12,0,100,101,
        5,10,0,0,101,102,3,8,4,0,102,21,1,0,0,0,103,104,5,8,0,0,104,105,
        5,9,0,0,105,106,3,12,6,0,106,107,5,25,0,0,107,108,3,24,12,0,108,
        109,5,25,0,0,109,110,3,24,12,0,110,111,5,10,0,0,111,112,3,8,4,0,
        112,23,1,0,0,0,113,118,3,26,13,0,114,115,7,0,0,0,115,117,3,26,13,
        0,116,114,1,0,0,0,117,120,1,0,0,0,118,116,1,0,0,0,118,119,1,0,0,
        0,119,122,1,0,0,0,120,118,1,0,0,0,121,123,5,25,0,0,122,121,1,0,0,
        0,122,123,1,0,0,0,123,25,1,0,0,0,124,129,3,28,14,0,125,126,7,1,0,
        0,126,128,3,28,14,0,127,125,1,0,0,0,128,131,1,0,0,0,129,127,1,0,
        0,0,129,130,1,0,0,0,130,27,1,0,0,0,131,129,1,0,0,0,132,133,5,14,
        0,0,133,146,3,28,14,0,134,135,5,2,0,0,135,146,5,21,0,0,136,137,5,
        2,0,0,137,146,5,22,0,0,138,139,5,9,0,0,139,140,3,24,12,0,140,141,
        5,10,0,0,141,146,1,0,0,0,142,146,5,1,0,0,143,146,5,3,0,0,144,146,
        5,2,0,0,145,132,1,0,0,0,145,134,1,0,0,0,145,136,1,0,0,0,145,138,
        1,0,0,0,145,142,1,0,0,0,145,143,1,0,0,0,145,144,1,0,0,0,146,29,1,
        0,0,0,9,40,53,75,90,95,118,122,129,145
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'='", "'if'", "'else'", "'while'", "'for'", "'('", 
                     "')'", "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", "'<'", 
                     "'>'", "'<='", "'>='", "'++'", "'--'", "'=='", "'!='", 
                     "';'", "'mostrar'" ]

    symbolicNames = [ "<INVALID>", "NUMERO", "VARIABLE", "DECIMAL", "ASIGNACION", 
                      "IF", "ELSE", "WHILE", "FOR", "PARENTESIS_INICIAL", 
                      "PARENTESIS_FINAL", "LLAVES_INICIAL", "LLAVES_FINAL", 
                      "MAS", "MENOS", "MULTIPLICACION", "DIVISION", "MENOR_QUE", 
                      "MAYOR_QUE", "MENOR_IGUAL_QUE", "MAYOR_IGUAL_QUE", 
                      "MASMAS", "MENOSMENOS", "IGUAL", "DIFERENTE", "PUNTO_Y_COMA", 
                      "MOSTRAR", "SIN_ESPACIO" ]

    RULE_gramatica = 0
    RULE_programa = 1
    RULE_bloque = 2
    RULE_bloque_condicional = 3
    RULE_bloque_de_sentencia = 4
    RULE_bloque_for = 5
    RULE_declaracion = 6
    RULE_sentencia = 7
    RULE_mostrar = 8
    RULE_sentencia_if = 9
    RULE_sentencia_while = 10
    RULE_sentencia_for = 11
    RULE_expr = 12
    RULE_term = 13
    RULE_factor = 14

    ruleNames =  [ "gramatica", "programa", "bloque", "bloque_condicional", 
                   "bloque_de_sentencia", "bloque_for", "declaracion", "sentencia", 
                   "mostrar", "sentencia_if", "sentencia_while", "sentencia_for", 
                   "expr", "term", "factor" ]

    EOF = Token.EOF
    NUMERO=1
    VARIABLE=2
    DECIMAL=3
    ASIGNACION=4
    IF=5
    ELSE=6
    WHILE=7
    FOR=8
    PARENTESIS_INICIAL=9
    PARENTESIS_FINAL=10
    LLAVES_INICIAL=11
    LLAVES_FINAL=12
    MAS=13
    MENOS=14
    MULTIPLICACION=15
    DIVISION=16
    MENOR_QUE=17
    MAYOR_QUE=18
    MENOR_IGUAL_QUE=19
    MAYOR_IGUAL_QUE=20
    MASMAS=21
    MENOSMENOS=22
    IGUAL=23
    DIFERENTE=24
    PUNTO_Y_COMA=25
    MOSTRAR=26
    SIN_ESPACIO=27

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
            self.state = 30
            self.programa()
            self.state = 31
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
            self.state = 33
            self.match(ExprParser.LLAVES_INICIAL)
            self.state = 34
            self.bloque()
            self.state = 35
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
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 67109284) != 0):
                self.state = 37
                self.sentencia()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 6, self.RULE_bloque_condicional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(ExprParser.PARENTESIS_INICIAL)
            self.state = 44
            self.expr()
            self.state = 45
            self.match(ExprParser.PARENTESIS_FINAL)
            self.state = 46
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
        self.enterRule(localctx, 8, self.RULE_bloque_de_sentencia)
        try:
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.match(ExprParser.LLAVES_INICIAL)
                self.state = 49
                self.bloque()
                self.state = 50
                self.match(ExprParser.LLAVES_FINAL)
                pass
            elif token in [2, 5, 7, 8, 26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
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


    class Bloque_forContext(ParserRuleContext):
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


        def PUNTO_Y_COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.PUNTO_Y_COMA)
            else:
                return self.getToken(ExprParser.PUNTO_Y_COMA, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def PARENTESIS_FINAL(self):
            return self.getToken(ExprParser.PARENTESIS_FINAL, 0)

        def bloque_de_sentencia(self):
            return self.getTypedRuleContext(ExprParser.Bloque_de_sentenciaContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_bloque_for

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque_for" ):
                listener.enterBloque_for(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque_for" ):
                listener.exitBloque_for(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque_for" ):
                return visitor.visitBloque_for(self)
            else:
                return visitor.visitChildren(self)




    def bloque_for(self):

        localctx = ExprParser.Bloque_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_bloque_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(ExprParser.FOR)
            self.state = 56
            self.match(ExprParser.PARENTESIS_INICIAL)
            self.state = 57
            self.declaracion()
            self.state = 58
            self.match(ExprParser.PUNTO_Y_COMA)
            self.state = 59
            self.expr()
            self.state = 60
            self.match(ExprParser.PUNTO_Y_COMA)
            self.state = 61
            self.expr()
            self.state = 62
            self.match(ExprParser.PARENTESIS_FINAL)
            self.state = 63
            self.bloque_de_sentencia()
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
        self.enterRule(localctx, 12, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(ExprParser.VARIABLE)
            self.state = 66
            self.match(ExprParser.ASIGNACION)
            self.state = 67
            self.expr()
            self.state = 68
            self.match(ExprParser.PUNTO_Y_COMA)
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

        def declaracion(self):
            return self.getTypedRuleContext(ExprParser.DeclaracionContext,0)


        def sentencia_if(self):
            return self.getTypedRuleContext(ExprParser.Sentencia_ifContext,0)


        def sentencia_while(self):
            return self.getTypedRuleContext(ExprParser.Sentencia_whileContext,0)


        def sentencia_for(self):
            return self.getTypedRuleContext(ExprParser.Sentencia_forContext,0)


        def mostrar(self):
            return self.getTypedRuleContext(ExprParser.MostrarContext,0)


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
        self.enterRule(localctx, 14, self.RULE_sentencia)
        try:
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.declaracion()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.sentencia_if()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 72
                self.sentencia_while()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 73
                self.sentencia_for()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 5)
                self.state = 74
                self.mostrar()
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
        self.enterRule(localctx, 16, self.RULE_mostrar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(ExprParser.MOSTRAR)
            self.state = 78
            self.match(ExprParser.PARENTESIS_INICIAL)
            self.state = 79
            self.expr()
            self.state = 80
            self.match(ExprParser.PARENTESIS_FINAL)
            self.state = 81
            self.match(ExprParser.PUNTO_Y_COMA)
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

        def IF(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.IF)
            else:
                return self.getToken(ExprParser.IF, i)

        def bloque_condicional(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.Bloque_condicionalContext)
            else:
                return self.getTypedRuleContext(ExprParser.Bloque_condicionalContext,i)


        def ELSE(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ELSE)
            else:
                return self.getToken(ExprParser.ELSE, i)

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
        self.enterRule(localctx, 18, self.RULE_sentencia_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(ExprParser.IF)
            self.state = 84
            self.bloque_condicional()
            self.state = 90
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 85
                    self.match(ExprParser.ELSE)
                    self.state = 86
                    self.match(ExprParser.IF)
                    self.state = 87
                    self.bloque_condicional() 
                self.state = 92
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 93
                self.match(ExprParser.ELSE)
                self.state = 94
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

        def PARENTESIS_INICIAL(self):
            return self.getToken(ExprParser.PARENTESIS_INICIAL, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def PARENTESIS_FINAL(self):
            return self.getToken(ExprParser.PARENTESIS_FINAL, 0)

        def bloque_de_sentencia(self):
            return self.getTypedRuleContext(ExprParser.Bloque_de_sentenciaContext,0)


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
        self.enterRule(localctx, 20, self.RULE_sentencia_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(ExprParser.WHILE)
            self.state = 98
            self.match(ExprParser.PARENTESIS_INICIAL)
            self.state = 99
            self.expr()
            self.state = 100
            self.match(ExprParser.PARENTESIS_FINAL)
            self.state = 101
            self.bloque_de_sentencia()
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


        def PUNTO_Y_COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.PUNTO_Y_COMA)
            else:
                return self.getToken(ExprParser.PUNTO_Y_COMA, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


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
        self.enterRule(localctx, 22, self.RULE_sentencia_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(ExprParser.FOR)
            self.state = 104
            self.match(ExprParser.PARENTESIS_INICIAL)
            self.state = 105
            self.declaracion()
            self.state = 106
            self.match(ExprParser.PUNTO_Y_COMA)
            self.state = 107
            self.expr()
            self.state = 108
            self.match(ExprParser.PUNTO_Y_COMA)
            self.state = 109
            self.expr()
            self.state = 110
            self.match(ExprParser.PARENTESIS_FINAL)
            self.state = 111
            self.bloque_de_sentencia()
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


        def PUNTO_Y_COMA(self):
            return self.getToken(ExprParser.PUNTO_Y_COMA, 0)

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




    def expr(self):

        localctx = ExprParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.term()
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13 or _la==14:
                self.state = 114
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 115
                self.term()
                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 121
                self.match(ExprParser.PUNTO_Y_COMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 26, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.factor()
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15 or _la==16:
                self.state = 125
                _la = self._input.LA(1)
                if not(_la==15 or _la==16):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 126
                self.factor()
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 28, self.RULE_factor)
        try:
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.match(ExprParser.MENOS)
                self.state = 133
                self.factor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.match(ExprParser.VARIABLE)
                self.state = 135
                self.match(ExprParser.MASMAS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 136
                self.match(ExprParser.VARIABLE)
                self.state = 137
                self.match(ExprParser.MENOSMENOS)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 138
                self.match(ExprParser.PARENTESIS_INICIAL)
                self.state = 139
                self.expr()
                self.state = 140
                self.match(ExprParser.PARENTESIS_FINAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 142
                self.match(ExprParser.NUMERO)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 143
                self.match(ExprParser.DECIMAL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 144
                self.match(ExprParser.VARIABLE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





