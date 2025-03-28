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
        4,1,38,219,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,2,5,2,54,8,2,10,
        2,12,2,57,9,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,68,8,3,1,4,
        1,4,1,4,1,4,5,4,74,8,4,10,4,12,4,77,9,4,1,4,1,4,3,4,81,8,4,1,5,1,
        5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,3,
        7,100,8,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,3,8,113,8,
        8,1,8,1,8,1,8,1,9,1,9,1,9,5,9,121,8,9,10,9,12,9,124,9,9,1,10,1,10,
        1,10,1,11,1,11,1,11,5,11,132,8,11,10,11,12,11,135,9,11,1,12,1,12,
        1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,3,13,147,8,13,1,14,1,14,
        1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,17,1,17,
        1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,5,18,172,8,18,10,18,12,18,
        175,9,18,1,18,1,18,1,18,5,18,180,8,18,10,18,12,18,183,9,18,1,19,
        1,19,1,19,5,19,188,8,19,10,19,12,19,191,9,19,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,208,
        8,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,217,8,21,1,21,0,1,36,
        22,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        0,4,1,0,7,10,1,0,16,17,2,0,20,23,26,27,1,0,18,19,225,0,44,1,0,0,
        0,2,47,1,0,0,0,4,55,1,0,0,0,6,67,1,0,0,0,8,69,1,0,0,0,10,82,1,0,
        0,0,12,85,1,0,0,0,14,94,1,0,0,0,16,109,1,0,0,0,18,117,1,0,0,0,20,
        125,1,0,0,0,22,128,1,0,0,0,24,136,1,0,0,0,26,146,1,0,0,0,28,148,
        1,0,0,0,30,154,1,0,0,0,32,159,1,0,0,0,34,161,1,0,0,0,36,167,1,0,
        0,0,38,184,1,0,0,0,40,207,1,0,0,0,42,216,1,0,0,0,44,45,3,2,1,0,45,
        46,5,0,0,1,46,1,1,0,0,0,47,48,5,30,0,0,48,49,5,14,0,0,49,50,3,4,
        2,0,50,51,5,15,0,0,51,3,1,0,0,0,52,54,3,6,3,0,53,52,1,0,0,0,54,57,
        1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,5,1,0,0,0,57,55,1,0,0,0,58,
        68,3,34,17,0,59,68,3,8,4,0,60,68,3,10,5,0,61,68,3,12,6,0,62,68,3,
        30,15,0,63,68,3,28,14,0,64,68,3,42,21,0,65,68,3,14,7,0,66,68,3,16,
        8,0,67,58,1,0,0,0,67,59,1,0,0,0,67,60,1,0,0,0,67,61,1,0,0,0,67,62,
        1,0,0,0,67,63,1,0,0,0,67,64,1,0,0,0,67,65,1,0,0,0,67,66,1,0,0,0,
        68,7,1,0,0,0,69,70,5,1,0,0,70,75,3,24,12,0,71,72,5,2,0,0,72,74,3,
        24,12,0,73,71,1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,
        76,80,1,0,0,0,77,75,1,0,0,0,78,79,5,3,0,0,79,81,3,26,13,0,80,78,
        1,0,0,0,80,81,1,0,0,0,81,9,1,0,0,0,82,83,5,4,0,0,83,84,3,24,12,0,
        84,11,1,0,0,0,85,86,5,5,0,0,86,87,5,12,0,0,87,88,3,28,14,0,88,89,
        3,36,18,0,89,90,5,29,0,0,90,91,3,42,21,0,91,92,5,13,0,0,92,93,3,
        26,13,0,93,13,1,0,0,0,94,95,5,31,0,0,95,96,5,36,0,0,96,97,3,32,16,
        0,97,99,5,12,0,0,98,100,3,18,9,0,99,98,1,0,0,0,99,100,1,0,0,0,100,
        101,1,0,0,0,101,102,5,13,0,0,102,103,5,14,0,0,103,104,3,4,2,0,104,
        105,5,32,0,0,105,106,3,36,18,0,106,107,5,29,0,0,107,108,5,15,0,0,
        108,15,1,0,0,0,109,110,5,36,0,0,110,112,5,12,0,0,111,113,3,22,11,
        0,112,111,1,0,0,0,112,113,1,0,0,0,113,114,1,0,0,0,114,115,5,13,0,
        0,115,116,5,29,0,0,116,17,1,0,0,0,117,122,3,20,10,0,118,119,5,28,
        0,0,119,121,3,20,10,0,120,118,1,0,0,0,121,124,1,0,0,0,122,120,1,
        0,0,0,122,123,1,0,0,0,123,19,1,0,0,0,124,122,1,0,0,0,125,126,5,36,
        0,0,126,127,3,32,16,0,127,21,1,0,0,0,128,133,3,36,18,0,129,130,5,
        28,0,0,130,132,3,36,18,0,131,129,1,0,0,0,132,135,1,0,0,0,133,131,
        1,0,0,0,133,134,1,0,0,0,134,23,1,0,0,0,135,133,1,0,0,0,136,137,5,
        12,0,0,137,138,3,36,18,0,138,139,5,13,0,0,139,140,3,26,13,0,140,
        25,1,0,0,0,141,142,5,14,0,0,142,143,3,4,2,0,143,144,5,15,0,0,144,
        147,1,0,0,0,145,147,3,6,3,0,146,141,1,0,0,0,146,145,1,0,0,0,147,
        27,1,0,0,0,148,149,5,36,0,0,149,150,3,32,16,0,150,151,5,11,0,0,151,
        152,3,36,18,0,152,153,5,29,0,0,153,29,1,0,0,0,154,155,5,36,0,0,155,
        156,5,11,0,0,156,157,3,36,18,0,157,158,5,29,0,0,158,31,1,0,0,0,159,
        160,7,0,0,0,160,33,1,0,0,0,161,162,5,6,0,0,162,163,5,12,0,0,163,
        164,3,36,18,0,164,165,5,13,0,0,165,166,5,29,0,0,166,35,1,0,0,0,167,
        168,6,18,-1,0,168,173,3,38,19,0,169,170,7,1,0,0,170,172,3,38,19,
        0,171,169,1,0,0,0,172,175,1,0,0,0,173,171,1,0,0,0,173,174,1,0,0,
        0,174,181,1,0,0,0,175,173,1,0,0,0,176,177,10,2,0,0,177,178,7,2,0,
        0,178,180,3,36,18,3,179,176,1,0,0,0,180,183,1,0,0,0,181,179,1,0,
        0,0,181,182,1,0,0,0,182,37,1,0,0,0,183,181,1,0,0,0,184,189,3,40,
        20,0,185,186,7,3,0,0,186,188,3,40,20,0,187,185,1,0,0,0,188,191,1,
        0,0,0,189,187,1,0,0,0,189,190,1,0,0,0,190,39,1,0,0,0,191,189,1,0,
        0,0,192,193,5,17,0,0,193,208,3,40,20,0,194,195,5,36,0,0,195,208,
        5,24,0,0,196,197,5,36,0,0,197,208,5,25,0,0,198,199,5,12,0,0,199,
        200,3,36,18,0,200,201,5,13,0,0,201,208,1,0,0,0,202,208,5,33,0,0,
        203,208,5,37,0,0,204,208,5,34,0,0,205,208,5,35,0,0,206,208,5,36,
        0,0,207,192,1,0,0,0,207,194,1,0,0,0,207,196,1,0,0,0,207,198,1,0,
        0,0,207,202,1,0,0,0,207,203,1,0,0,0,207,204,1,0,0,0,207,205,1,0,
        0,0,207,206,1,0,0,0,208,41,1,0,0,0,209,210,5,36,0,0,210,211,5,11,
        0,0,211,217,3,36,18,0,212,213,5,36,0,0,213,217,5,24,0,0,214,215,
        5,36,0,0,215,217,5,25,0,0,216,209,1,0,0,0,216,212,1,0,0,0,216,214,
        1,0,0,0,217,43,1,0,0,0,14,55,67,75,80,99,112,122,133,146,173,181,
        189,207,216
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else if'", "'else'", "'while'", 
                     "'for'", "'mostrar'", "'entero'", "'decimal'", "'cadena'", 
                     "'bool'", "'='", "'('", "')'", "'{'", "'}'", "'+'", 
                     "'-'", "'*'", "'/'", "'<'", "'>'", "'<='", "'>='", 
                     "'++'", "'--'", "'=='", "'!='", "','", "';'", "'hola'", 
                     "'funcion'", "'retorna'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE_IF", "ELSE", "WHILE", "FOR", 
                      "MOSTRAR", "TIPO_ENTERO", "TIPO_DECIMAL", "TIPO_CADENA", 
                      "TIPO_BOOLEANO", "ASIGNACION", "PARENTESIS_INICIAL", 
                      "PARENTESIS_FINAL", "LLAVES_INICIAL", "LLAVES_FINAL", 
                      "MAS", "MENOS", "MULTIPLICACION", "DIVISION", "MENOR_QUE", 
                      "MAYOR_QUE", "MENOR_IGUAL_QUE", "MAYOR_IGUAL_QUE", 
                      "MASMAS", "MENOSMENOS", "IGUAL", "DIFERENTE", "COMA", 
                      "PUNTO_Y_COMA", "MAIN", "FUNCION", "RETURN", "NUMERO", 
                      "BOOLEANO", "CADENA", "VARIABLE", "DECIMAL", "SIN_ESPACIO" ]

    RULE_gramatica = 0
    RULE_programa = 1
    RULE_bloque = 2
    RULE_sentencia = 3
    RULE_sentencia_if = 4
    RULE_sentencia_while = 5
    RULE_sentencia_for = 6
    RULE_declaracion_funcion = 7
    RULE_funcion_llamada = 8
    RULE_parametros = 9
    RULE_parametro = 10
    RULE_argumentos = 11
    RULE_bloque_condicional = 12
    RULE_bloque_de_sentencia = 13
    RULE_declaracion = 14
    RULE_reasignacion = 15
    RULE_tipo = 16
    RULE_mostrar = 17
    RULE_expr = 18
    RULE_term = 19
    RULE_factor = 20
    RULE_actualizacion = 21

    ruleNames =  [ "gramatica", "programa", "bloque", "sentencia", "sentencia_if", 
                   "sentencia_while", "sentencia_for", "declaracion_funcion", 
                   "funcion_llamada", "parametros", "parametro", "argumentos", 
                   "bloque_condicional", "bloque_de_sentencia", "declaracion", 
                   "reasignacion", "tipo", "mostrar", "expr", "term", "factor", 
                   "actualizacion" ]

    EOF = Token.EOF
    IF=1
    ELSE_IF=2
    ELSE=3
    WHILE=4
    FOR=5
    MOSTRAR=6
    TIPO_ENTERO=7
    TIPO_DECIMAL=8
    TIPO_CADENA=9
    TIPO_BOOLEANO=10
    ASIGNACION=11
    PARENTESIS_INICIAL=12
    PARENTESIS_FINAL=13
    LLAVES_INICIAL=14
    LLAVES_FINAL=15
    MAS=16
    MENOS=17
    MULTIPLICACION=18
    DIVISION=19
    MENOR_QUE=20
    MAYOR_QUE=21
    MENOR_IGUAL_QUE=22
    MAYOR_IGUAL_QUE=23
    MASMAS=24
    MENOSMENOS=25
    IGUAL=26
    DIFERENTE=27
    COMA=28
    PUNTO_Y_COMA=29
    MAIN=30
    FUNCION=31
    RETURN=32
    NUMERO=33
    BOOLEANO=34
    CADENA=35
    VARIABLE=36
    DECIMAL=37
    SIN_ESPACIO=38

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
            self.state = 44
            self.programa()
            self.state = 45
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
            self.state = 47
            self.match(ExprParser.MAIN)
            self.state = 48
            self.match(ExprParser.LLAVES_INICIAL)
            self.state = 49
            self.bloque()
            self.state = 50
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
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 70866960498) != 0):
                self.state = 52
                self.sentencia()
                self.state = 57
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

        def mostrar(self):
            return self.getTypedRuleContext(ExprParser.MostrarContext,0)


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


        def actualizacion(self):
            return self.getTypedRuleContext(ExprParser.ActualizacionContext,0)


        def declaracion_funcion(self):
            return self.getTypedRuleContext(ExprParser.Declaracion_funcionContext,0)


        def funcion_llamada(self):
            return self.getTypedRuleContext(ExprParser.Funcion_llamadaContext,0)


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
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.mostrar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.sentencia_if()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 60
                self.sentencia_while()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 61
                self.sentencia_for()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 62
                self.reasignacion()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 63
                self.declaracion()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 64
                self.actualizacion()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 65
                self.declaracion_funcion()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 66
                self.funcion_llamada()
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
            self.state = 69
            self.match(ExprParser.IF)
            self.state = 70
            self.bloque_condicional()
            self.state = 75
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 71
                    self.match(ExprParser.ELSE_IF)
                    self.state = 72
                    self.bloque_condicional() 
                self.state = 77
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 80
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 78
                self.match(ExprParser.ELSE)
                self.state = 79
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
            self.state = 82
            self.match(ExprParser.WHILE)
            self.state = 83
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
            self.state = 85
            self.match(ExprParser.FOR)
            self.state = 86
            self.match(ExprParser.PARENTESIS_INICIAL)
            self.state = 87
            self.declaracion()
            self.state = 88
            self.expr(0)
            self.state = 89
            self.match(ExprParser.PUNTO_Y_COMA)
            self.state = 90
            self.actualizacion()
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


    class Declaracion_funcionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCION(self):
            return self.getToken(ExprParser.FUNCION, 0)

        def VARIABLE(self):
            return self.getToken(ExprParser.VARIABLE, 0)

        def tipo(self):
            return self.getTypedRuleContext(ExprParser.TipoContext,0)


        def PARENTESIS_INICIAL(self):
            return self.getToken(ExprParser.PARENTESIS_INICIAL, 0)

        def PARENTESIS_FINAL(self):
            return self.getToken(ExprParser.PARENTESIS_FINAL, 0)

        def LLAVES_INICIAL(self):
            return self.getToken(ExprParser.LLAVES_INICIAL, 0)

        def bloque(self):
            return self.getTypedRuleContext(ExprParser.BloqueContext,0)


        def RETURN(self):
            return self.getToken(ExprParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def PUNTO_Y_COMA(self):
            return self.getToken(ExprParser.PUNTO_Y_COMA, 0)

        def LLAVES_FINAL(self):
            return self.getToken(ExprParser.LLAVES_FINAL, 0)

        def parametros(self):
            return self.getTypedRuleContext(ExprParser.ParametrosContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_declaracion_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion_funcion" ):
                listener.enterDeclaracion_funcion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion_funcion" ):
                listener.exitDeclaracion_funcion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion_funcion" ):
                return visitor.visitDeclaracion_funcion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion_funcion(self):

        localctx = ExprParser.Declaracion_funcionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_declaracion_funcion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(ExprParser.FUNCION)
            self.state = 95
            self.match(ExprParser.VARIABLE)
            self.state = 96
            self.tipo()
            self.state = 97
            self.match(ExprParser.PARENTESIS_INICIAL)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 98
                self.parametros()


            self.state = 101
            self.match(ExprParser.PARENTESIS_FINAL)
            self.state = 102
            self.match(ExprParser.LLAVES_INICIAL)
            self.state = 103
            self.bloque()
            self.state = 104
            self.match(ExprParser.RETURN)
            self.state = 105
            self.expr(0)
            self.state = 106
            self.match(ExprParser.PUNTO_Y_COMA)
            self.state = 107
            self.match(ExprParser.LLAVES_FINAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funcion_llamadaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(ExprParser.VARIABLE, 0)

        def PARENTESIS_INICIAL(self):
            return self.getToken(ExprParser.PARENTESIS_INICIAL, 0)

        def PARENTESIS_FINAL(self):
            return self.getToken(ExprParser.PARENTESIS_FINAL, 0)

        def PUNTO_Y_COMA(self):
            return self.getToken(ExprParser.PUNTO_Y_COMA, 0)

        def argumentos(self):
            return self.getTypedRuleContext(ExprParser.ArgumentosContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_funcion_llamada

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncion_llamada" ):
                listener.enterFuncion_llamada(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncion_llamada" ):
                listener.exitFuncion_llamada(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncion_llamada" ):
                return visitor.visitFuncion_llamada(self)
            else:
                return visitor.visitChildren(self)




    def funcion_llamada(self):

        localctx = ExprParser.Funcion_llamadaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_funcion_llamada)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(ExprParser.VARIABLE)
            self.state = 110
            self.match(ExprParser.PARENTESIS_INICIAL)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 266288107520) != 0):
                self.state = 111
                self.argumentos()


            self.state = 114
            self.match(ExprParser.PARENTESIS_FINAL)
            self.state = 115
            self.match(ExprParser.PUNTO_Y_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parametro(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ParametroContext)
            else:
                return self.getTypedRuleContext(ExprParser.ParametroContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMA)
            else:
                return self.getToken(ExprParser.COMA, i)

        def getRuleIndex(self):
            return ExprParser.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros" ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros" ):
                listener.exitParametros(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametros" ):
                return visitor.visitParametros(self)
            else:
                return visitor.visitChildren(self)




    def parametros(self):

        localctx = ExprParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_parametros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.parametro()
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 118
                self.match(ExprParser.COMA)
                self.state = 119
                self.parametro()
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(ExprParser.VARIABLE, 0)

        def tipo(self):
            return self.getTypedRuleContext(ExprParser.TipoContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_parametro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametro" ):
                listener.enterParametro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametro" ):
                listener.exitParametro(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametro" ):
                return visitor.visitParametro(self)
            else:
                return visitor.visitChildren(self)




    def parametro(self):

        localctx = ExprParser.ParametroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_parametro)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(ExprParser.VARIABLE)
            self.state = 126
            self.tipo()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMA)
            else:
                return self.getToken(ExprParser.COMA, i)

        def getRuleIndex(self):
            return ExprParser.RULE_argumentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentos" ):
                listener.enterArgumentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentos" ):
                listener.exitArgumentos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentos" ):
                return visitor.visitArgumentos(self)
            else:
                return visitor.visitChildren(self)




    def argumentos(self):

        localctx = ExprParser.ArgumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_argumentos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.expr(0)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 129
                self.match(ExprParser.COMA)
                self.state = 130
                self.expr(0)
                self.state = 135
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
        self.enterRule(localctx, 24, self.RULE_bloque_condicional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(ExprParser.PARENTESIS_INICIAL)
            self.state = 137
            self.expr(0)
            self.state = 138
            self.match(ExprParser.PARENTESIS_FINAL)
            self.state = 139
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
        self.enterRule(localctx, 26, self.RULE_bloque_de_sentencia)
        try:
            self.state = 146
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.match(ExprParser.LLAVES_INICIAL)
                self.state = 142
                self.bloque()
                self.state = 143
                self.match(ExprParser.LLAVES_FINAL)
                pass
            elif token in [1, 4, 5, 6, 31, 36]:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
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
        self.enterRule(localctx, 28, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(ExprParser.VARIABLE)
            self.state = 149
            self.tipo()
            self.state = 150
            self.match(ExprParser.ASIGNACION)
            self.state = 151
            self.expr(0)
            self.state = 152
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
        self.enterRule(localctx, 30, self.RULE_reasignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(ExprParser.VARIABLE)
            self.state = 155
            self.match(ExprParser.ASIGNACION)
            self.state = 156
            self.expr(0)
            self.state = 157
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

        def TIPO_BOOLEANO(self):
            return self.getToken(ExprParser.TIPO_BOOLEANO, 0)

        def TIPO_CADENA(self):
            return self.getToken(ExprParser.TIPO_CADENA, 0)

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
        self.enterRule(localctx, 32, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1920) != 0)):
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
        self.enterRule(localctx, 34, self.RULE_mostrar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(ExprParser.MOSTRAR)
            self.state = 162
            self.match(ExprParser.PARENTESIS_INICIAL)
            self.state = 163
            self.expr(0)
            self.state = 164
            self.match(ExprParser.PARENTESIS_FINAL)
            self.state = 165
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
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.term()
            self.state = 173
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 169
                    _la = self._input.LA(1)
                    if not(_la==16 or _la==17):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 170
                    self.term() 
                self.state = 175
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

            self._ctx.stop = self._input.LT(-1)
            self.state = 181
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 176
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 177
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 217055232) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 178
                    self.expr(3) 
                self.state = 183
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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
        self.enterRule(localctx, 38, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.factor()
            self.state = 189
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 185
                    _la = self._input.LA(1)
                    if not(_la==18 or _la==19):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 186
                    self.factor() 
                self.state = 191
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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

        def BOOLEANO(self):
            return self.getToken(ExprParser.BOOLEANO, 0)

        def CADENA(self):
            return self.getToken(ExprParser.CADENA, 0)

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
        self.enterRule(localctx, 40, self.RULE_factor)
        try:
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.match(ExprParser.MENOS)
                self.state = 193
                self.factor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.match(ExprParser.VARIABLE)
                self.state = 195
                self.match(ExprParser.MASMAS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 196
                self.match(ExprParser.VARIABLE)
                self.state = 197
                self.match(ExprParser.MENOSMENOS)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 198
                self.match(ExprParser.PARENTESIS_INICIAL)
                self.state = 199
                self.expr(0)
                self.state = 200
                self.match(ExprParser.PARENTESIS_FINAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 202
                self.match(ExprParser.NUMERO)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 203
                self.match(ExprParser.DECIMAL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 204
                self.match(ExprParser.BOOLEANO)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 205
                self.match(ExprParser.CADENA)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 206
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
        self.enterRule(localctx, 42, self.RULE_actualizacion)
        try:
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.match(ExprParser.VARIABLE)
                self.state = 210
                self.match(ExprParser.ASIGNACION)
                self.state = 211
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.match(ExprParser.VARIABLE)
                self.state = 213
                self.match(ExprParser.MASMAS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 214
                self.match(ExprParser.VARIABLE)
                self.state = 215
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
        self._predicates[18] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




