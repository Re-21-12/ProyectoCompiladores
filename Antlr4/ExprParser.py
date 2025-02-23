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
        4,1,26,139,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,5,2,37,8,2,10,2,12,2,40,9,2,1,3,
        1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,3,4,52,8,4,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,3,7,73,
        8,7,1,8,1,8,1,8,1,8,1,8,5,8,80,8,8,10,8,12,8,83,9,8,1,8,1,8,3,8,
        87,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,11,1,11,1,11,5,11,108,8,11,10,11,12,11,111,9,11,
        1,11,3,11,114,8,11,1,12,1,12,1,12,5,12,119,8,12,10,12,12,12,122,
        9,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,3,13,137,8,13,1,13,0,0,14,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,0,2,1,0,13,14,1,0,15,16,140,0,28,1,0,0,0,2,31,1,0,0,0,4,38,1,
        0,0,0,6,41,1,0,0,0,8,51,1,0,0,0,10,53,1,0,0,0,12,63,1,0,0,0,14,72,
        1,0,0,0,16,74,1,0,0,0,18,88,1,0,0,0,20,94,1,0,0,0,22,104,1,0,0,0,
        24,115,1,0,0,0,26,136,1,0,0,0,28,29,3,2,1,0,29,30,5,0,0,1,30,1,1,
        0,0,0,31,32,5,11,0,0,32,33,3,4,2,0,33,34,5,12,0,0,34,3,1,0,0,0,35,
        37,3,14,7,0,36,35,1,0,0,0,37,40,1,0,0,0,38,36,1,0,0,0,38,39,1,0,
        0,0,39,5,1,0,0,0,40,38,1,0,0,0,41,42,5,9,0,0,42,43,3,22,11,0,43,
        44,5,10,0,0,44,45,3,8,4,0,45,7,1,0,0,0,46,47,5,11,0,0,47,48,3,4,
        2,0,48,49,5,12,0,0,49,52,1,0,0,0,50,52,3,14,7,0,51,46,1,0,0,0,51,
        50,1,0,0,0,52,9,1,0,0,0,53,54,5,8,0,0,54,55,5,9,0,0,55,56,3,12,6,
        0,56,57,5,25,0,0,57,58,3,22,11,0,58,59,5,25,0,0,59,60,3,22,11,0,
        60,61,5,10,0,0,61,62,3,8,4,0,62,11,1,0,0,0,63,64,5,2,0,0,64,65,5,
        4,0,0,65,66,3,22,11,0,66,67,5,25,0,0,67,13,1,0,0,0,68,73,3,12,6,
        0,69,73,3,16,8,0,70,73,3,18,9,0,71,73,3,20,10,0,72,68,1,0,0,0,72,
        69,1,0,0,0,72,70,1,0,0,0,72,71,1,0,0,0,73,15,1,0,0,0,74,75,5,5,0,
        0,75,81,3,6,3,0,76,77,5,6,0,0,77,78,5,5,0,0,78,80,3,6,3,0,79,76,
        1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,86,1,0,0,0,
        83,81,1,0,0,0,84,85,5,6,0,0,85,87,3,8,4,0,86,84,1,0,0,0,86,87,1,
        0,0,0,87,17,1,0,0,0,88,89,5,7,0,0,89,90,5,9,0,0,90,91,3,22,11,0,
        91,92,5,10,0,0,92,93,3,8,4,0,93,19,1,0,0,0,94,95,5,8,0,0,95,96,5,
        9,0,0,96,97,3,12,6,0,97,98,5,25,0,0,98,99,3,22,11,0,99,100,5,25,
        0,0,100,101,3,22,11,0,101,102,5,10,0,0,102,103,3,8,4,0,103,21,1,
        0,0,0,104,109,3,24,12,0,105,106,7,0,0,0,106,108,3,24,12,0,107,105,
        1,0,0,0,108,111,1,0,0,0,109,107,1,0,0,0,109,110,1,0,0,0,110,113,
        1,0,0,0,111,109,1,0,0,0,112,114,5,25,0,0,113,112,1,0,0,0,113,114,
        1,0,0,0,114,23,1,0,0,0,115,120,3,26,13,0,116,117,7,1,0,0,117,119,
        3,26,13,0,118,116,1,0,0,0,119,122,1,0,0,0,120,118,1,0,0,0,120,121,
        1,0,0,0,121,25,1,0,0,0,122,120,1,0,0,0,123,124,5,14,0,0,124,137,
        3,26,13,0,125,126,5,2,0,0,126,137,5,21,0,0,127,128,5,2,0,0,128,137,
        5,22,0,0,129,130,5,9,0,0,130,131,3,22,11,0,131,132,5,10,0,0,132,
        137,1,0,0,0,133,137,5,1,0,0,134,137,5,3,0,0,135,137,5,2,0,0,136,
        123,1,0,0,0,136,125,1,0,0,0,136,127,1,0,0,0,136,129,1,0,0,0,136,
        133,1,0,0,0,136,134,1,0,0,0,136,135,1,0,0,0,137,27,1,0,0,0,9,38,
        51,72,81,86,109,113,120,136
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
                     "';'" ]

    symbolicNames = [ "<INVALID>", "NUMERO", "VARIABLE", "DECIMAL", "ASIGNACION", 
                      "IF", "ELSE", "WHILE", "FOR", "PARENTESIS_INICIAL", 
                      "PARENTESIS_FINAL", "LLAVES_INICIAL", "LLAVES_FINAL", 
                      "MAS", "MENOS", "MULTIPLICACION", "DIVISION", "MENOR_QUE", 
                      "MAYOR_QUE", "MENOR_IGUAL_QUE", "MAYOR_IGUAL_QUE", 
                      "MASMAS", "MENOSMENOS", "IGUAL", "DIFERENTE", "PUNTO_Y_COMA", 
                      "SIN_ESPACIO" ]

    RULE_gramatica = 0
    RULE_programa = 1
    RULE_bloque = 2
    RULE_bloque_condicional = 3
    RULE_bloque_de_sentencia = 4
    RULE_bloque_for = 5
    RULE_declaracion = 6
    RULE_sentencia = 7
    RULE_sentencia_if = 8
    RULE_sentencia_while = 9
    RULE_sentencia_for = 10
    RULE_expr = 11
    RULE_term = 12
    RULE_factor = 13

    ruleNames =  [ "gramatica", "programa", "bloque", "bloque_condicional", 
                   "bloque_de_sentencia", "bloque_for", "declaracion", "sentencia", 
                   "sentencia_if", "sentencia_while", "sentencia_for", "expr", 
                   "term", "factor" ]

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
    SIN_ESPACIO=26

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
            self.state = 28
            self.programa()
            self.state = 29
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
            self.state = 31
            self.match(ExprParser.LLAVES_INICIAL)
            self.state = 32
            self.bloque()
            self.state = 33
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
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 420) != 0):
                self.state = 35
                self.sentencia()
                self.state = 40
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
            self.state = 41
            self.match(ExprParser.PARENTESIS_INICIAL)
            self.state = 42
            self.expr()
            self.state = 43
            self.match(ExprParser.PARENTESIS_FINAL)
            self.state = 44
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
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.match(ExprParser.LLAVES_INICIAL)
                self.state = 47
                self.bloque()
                self.state = 48
                self.match(ExprParser.LLAVES_FINAL)
                pass
            elif token in [2, 5, 7, 8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
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
            self.state = 53
            self.match(ExprParser.FOR)
            self.state = 54
            self.match(ExprParser.PARENTESIS_INICIAL)
            self.state = 55
            self.declaracion()
            self.state = 56
            self.match(ExprParser.PUNTO_Y_COMA)
            self.state = 57
            self.expr()
            self.state = 58
            self.match(ExprParser.PUNTO_Y_COMA)
            self.state = 59
            self.expr()
            self.state = 60
            self.match(ExprParser.PARENTESIS_FINAL)
            self.state = 61
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
            self.state = 63
            self.match(ExprParser.VARIABLE)
            self.state = 64
            self.match(ExprParser.ASIGNACION)
            self.state = 65
            self.expr()
            self.state = 66
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
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.declaracion()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.sentencia_if()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                self.sentencia_while()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 71
                self.sentencia_for()
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
        self.enterRule(localctx, 16, self.RULE_sentencia_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(ExprParser.IF)
            self.state = 75
            self.bloque_condicional()
            self.state = 81
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 76
                    self.match(ExprParser.ELSE)
                    self.state = 77
                    self.match(ExprParser.IF)
                    self.state = 78
                    self.bloque_condicional() 
                self.state = 83
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 84
                self.match(ExprParser.ELSE)
                self.state = 85
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
        self.enterRule(localctx, 18, self.RULE_sentencia_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(ExprParser.WHILE)
            self.state = 89
            self.match(ExprParser.PARENTESIS_INICIAL)
            self.state = 90
            self.expr()
            self.state = 91
            self.match(ExprParser.PARENTESIS_FINAL)
            self.state = 92
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
        self.enterRule(localctx, 20, self.RULE_sentencia_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(ExprParser.FOR)
            self.state = 95
            self.match(ExprParser.PARENTESIS_INICIAL)
            self.state = 96
            self.declaracion()
            self.state = 97
            self.match(ExprParser.PUNTO_Y_COMA)
            self.state = 98
            self.expr()
            self.state = 99
            self.match(ExprParser.PUNTO_Y_COMA)
            self.state = 100
            self.expr()
            self.state = 101
            self.match(ExprParser.PARENTESIS_FINAL)
            self.state = 102
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
        self.enterRule(localctx, 22, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.term()
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13 or _la==14:
                self.state = 105
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 106
                self.term()
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 112
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
        self.enterRule(localctx, 24, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.factor()
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15 or _la==16:
                self.state = 116
                _la = self._input.LA(1)
                if not(_la==15 or _la==16):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 117
                self.factor()
                self.state = 122
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
        self.enterRule(localctx, 26, self.RULE_factor)
        try:
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.match(ExprParser.MENOS)
                self.state = 124
                self.factor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.match(ExprParser.VARIABLE)
                self.state = 126
                self.match(ExprParser.MASMAS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 127
                self.match(ExprParser.VARIABLE)
                self.state = 128
                self.match(ExprParser.MENOSMENOS)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 129
                self.match(ExprParser.PARENTESIS_INICIAL)
                self.state = 130
                self.expr()
                self.state = 131
                self.match(ExprParser.PARENTESIS_FINAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 133
                self.match(ExprParser.NUMERO)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 134
                self.match(ExprParser.DECIMAL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 135
                self.match(ExprParser.VARIABLE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





