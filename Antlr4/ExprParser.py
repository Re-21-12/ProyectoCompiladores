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
        4,1,50,301,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,1,0,1,0,1,
        0,1,1,1,1,1,1,1,1,1,1,1,2,5,2,62,8,2,10,2,12,2,65,9,2,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,81,8,3,1,4,1,4,
        1,4,1,4,5,4,87,8,4,10,4,12,4,90,9,4,1,4,1,4,3,4,94,8,4,1,5,1,5,1,
        5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,3,7,113,
        8,7,1,7,1,7,1,7,1,7,3,7,119,8,7,1,7,1,7,1,8,1,8,1,8,3,8,126,8,8,
        1,8,1,8,1,8,1,9,1,9,1,9,3,9,134,8,9,1,9,1,9,1,10,1,10,1,10,1,10,
        1,11,1,11,1,11,5,11,145,8,11,10,11,12,11,148,9,11,1,12,1,12,1,12,
        1,13,1,13,1,13,5,13,156,8,13,10,13,12,13,159,9,13,1,14,1,14,1,14,
        1,14,1,14,1,15,1,15,1,15,1,15,1,15,3,15,171,8,15,1,16,1,16,1,16,
        1,16,1,16,3,16,178,8,16,1,16,1,16,1,17,1,17,1,17,1,17,1,18,1,18,
        1,18,1,18,1,18,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,
        1,21,1,21,5,21,203,8,21,10,21,12,21,206,9,21,1,21,1,21,1,21,5,21,
        211,8,21,10,21,12,21,214,9,21,3,21,216,8,21,1,21,1,21,1,21,1,21,
        1,21,1,21,5,21,224,8,21,10,21,12,21,227,9,21,1,22,1,22,1,22,5,22,
        232,8,22,10,22,12,22,235,9,22,1,22,1,22,1,22,5,22,240,8,22,10,22,
        12,22,243,9,22,3,22,245,8,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,3,23,268,8,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,3,24,277,8,
        24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,5,25,289,8,
        25,10,25,12,25,292,9,25,1,25,1,25,1,25,3,25,297,8,25,1,25,1,25,1,
        25,0,1,42,26,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        38,40,42,44,46,48,50,0,5,1,0,5,9,1,0,15,16,1,0,40,41,1,0,21,26,1,
        0,17,18,318,0,52,1,0,0,0,2,55,1,0,0,0,4,63,1,0,0,0,6,80,1,0,0,0,
        8,82,1,0,0,0,10,95,1,0,0,0,12,98,1,0,0,0,14,107,1,0,0,0,16,122,1,
        0,0,0,18,130,1,0,0,0,20,137,1,0,0,0,22,141,1,0,0,0,24,149,1,0,0,
        0,26,152,1,0,0,0,28,160,1,0,0,0,30,170,1,0,0,0,32,172,1,0,0,0,34,
        181,1,0,0,0,36,185,1,0,0,0,38,190,1,0,0,0,40,192,1,0,0,0,42,215,
        1,0,0,0,44,244,1,0,0,0,46,267,1,0,0,0,48,276,1,0,0,0,50,278,1,0,
        0,0,52,53,3,2,1,0,53,54,5,0,0,1,54,1,1,0,0,0,55,56,5,31,0,0,56,57,
        5,13,0,0,57,58,3,4,2,0,58,59,5,14,0,0,59,3,1,0,0,0,60,62,3,6,3,0,
        61,60,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,5,1,0,
        0,0,65,63,1,0,0,0,66,81,3,8,4,0,67,81,3,10,5,0,68,81,3,12,6,0,69,
        81,3,36,18,0,70,81,3,40,20,0,71,81,3,34,17,0,72,81,3,32,16,0,73,
        74,3,48,24,0,74,75,5,30,0,0,75,81,1,0,0,0,76,81,3,14,7,0,77,81,3,
        16,8,0,78,81,3,20,10,0,79,81,3,50,25,0,80,66,1,0,0,0,80,67,1,0,0,
        0,80,68,1,0,0,0,80,69,1,0,0,0,80,70,1,0,0,0,80,71,1,0,0,0,80,72,
        1,0,0,0,80,73,1,0,0,0,80,76,1,0,0,0,80,77,1,0,0,0,80,78,1,0,0,0,
        80,79,1,0,0,0,81,7,1,0,0,0,82,83,5,34,0,0,83,88,3,28,14,0,84,85,
        5,35,0,0,85,87,3,28,14,0,86,84,1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,
        0,88,89,1,0,0,0,89,93,1,0,0,0,90,88,1,0,0,0,91,92,5,36,0,0,92,94,
        3,30,15,0,93,91,1,0,0,0,93,94,1,0,0,0,94,9,1,0,0,0,95,96,5,37,0,
        0,96,97,3,28,14,0,97,11,1,0,0,0,98,99,5,38,0,0,99,100,5,11,0,0,100,
        101,3,32,16,0,101,102,3,42,21,0,102,103,5,30,0,0,103,104,3,48,24,
        0,104,105,5,12,0,0,105,106,3,30,15,0,106,13,1,0,0,0,107,108,5,32,
        0,0,108,109,5,45,0,0,109,110,3,38,19,0,110,112,5,11,0,0,111,113,
        3,22,11,0,112,111,1,0,0,0,112,113,1,0,0,0,113,114,1,0,0,0,114,115,
        5,12,0,0,115,116,5,13,0,0,116,118,3,4,2,0,117,119,3,20,10,0,118,
        117,1,0,0,0,118,119,1,0,0,0,119,120,1,0,0,0,120,121,5,14,0,0,121,
        15,1,0,0,0,122,123,5,45,0,0,123,125,5,11,0,0,124,126,3,26,13,0,125,
        124,1,0,0,0,125,126,1,0,0,0,126,127,1,0,0,0,127,128,5,12,0,0,128,
        129,5,30,0,0,129,17,1,0,0,0,130,131,5,45,0,0,131,133,5,11,0,0,132,
        134,3,26,13,0,133,132,1,0,0,0,133,134,1,0,0,0,134,135,1,0,0,0,135,
        136,5,12,0,0,136,19,1,0,0,0,137,138,5,33,0,0,138,139,3,42,21,0,139,
        140,5,30,0,0,140,21,1,0,0,0,141,146,3,24,12,0,142,143,5,29,0,0,143,
        145,3,24,12,0,144,142,1,0,0,0,145,148,1,0,0,0,146,144,1,0,0,0,146,
        147,1,0,0,0,147,23,1,0,0,0,148,146,1,0,0,0,149,150,5,45,0,0,150,
        151,3,38,19,0,151,25,1,0,0,0,152,157,3,42,21,0,153,154,5,29,0,0,
        154,156,3,42,21,0,155,153,1,0,0,0,156,159,1,0,0,0,157,155,1,0,0,
        0,157,158,1,0,0,0,158,27,1,0,0,0,159,157,1,0,0,0,160,161,5,11,0,
        0,161,162,3,42,21,0,162,163,5,12,0,0,163,164,3,30,15,0,164,29,1,
        0,0,0,165,171,3,6,3,0,166,167,5,13,0,0,167,168,3,4,2,0,168,169,5,
        14,0,0,169,171,1,0,0,0,170,165,1,0,0,0,170,166,1,0,0,0,171,31,1,
        0,0,0,172,173,5,45,0,0,173,174,3,38,19,0,174,177,5,10,0,0,175,178,
        3,42,21,0,176,178,3,16,8,0,177,175,1,0,0,0,177,176,1,0,0,0,178,179,
        1,0,0,0,179,180,5,30,0,0,180,33,1,0,0,0,181,182,5,45,0,0,182,183,
        3,38,19,0,183,184,5,30,0,0,184,35,1,0,0,0,185,186,5,45,0,0,186,187,
        5,10,0,0,187,188,3,42,21,0,188,189,5,30,0,0,189,37,1,0,0,0,190,191,
        7,0,0,0,191,39,1,0,0,0,192,193,5,39,0,0,193,194,5,11,0,0,194,195,
        3,42,21,0,195,196,5,12,0,0,196,197,5,30,0,0,197,41,1,0,0,0,198,199,
        6,21,-1,0,199,204,3,44,22,0,200,201,7,1,0,0,201,203,3,44,22,0,202,
        200,1,0,0,0,203,206,1,0,0,0,204,202,1,0,0,0,204,205,1,0,0,0,205,
        216,1,0,0,0,206,204,1,0,0,0,207,212,3,44,22,0,208,209,5,19,0,0,209,
        211,3,44,22,0,210,208,1,0,0,0,211,214,1,0,0,0,212,210,1,0,0,0,212,
        213,1,0,0,0,213,216,1,0,0,0,214,212,1,0,0,0,215,198,1,0,0,0,215,
        207,1,0,0,0,216,225,1,0,0,0,217,218,10,4,0,0,218,219,7,2,0,0,219,
        224,3,42,21,5,220,221,10,3,0,0,221,222,7,3,0,0,222,224,3,42,21,4,
        223,217,1,0,0,0,223,220,1,0,0,0,224,227,1,0,0,0,225,223,1,0,0,0,
        225,226,1,0,0,0,226,43,1,0,0,0,227,225,1,0,0,0,228,233,3,46,23,0,
        229,230,7,4,0,0,230,232,3,46,23,0,231,229,1,0,0,0,232,235,1,0,0,
        0,233,231,1,0,0,0,233,234,1,0,0,0,234,245,1,0,0,0,235,233,1,0,0,
        0,236,241,3,46,23,0,237,238,5,20,0,0,238,240,3,46,23,0,239,237,1,
        0,0,0,240,243,1,0,0,0,241,239,1,0,0,0,241,242,1,0,0,0,242,245,1,
        0,0,0,243,241,1,0,0,0,244,228,1,0,0,0,244,236,1,0,0,0,245,45,1,0,
        0,0,246,247,5,48,0,0,247,248,5,11,0,0,248,249,3,42,21,0,249,250,
        5,12,0,0,250,268,1,0,0,0,251,252,5,16,0,0,252,268,3,46,23,0,253,
        254,5,45,0,0,254,268,5,27,0,0,255,256,5,45,0,0,256,268,5,28,0,0,
        257,258,5,11,0,0,258,259,3,42,21,0,259,260,5,12,0,0,260,268,1,0,
        0,0,261,268,5,42,0,0,262,268,5,46,0,0,263,268,5,43,0,0,264,268,5,
        44,0,0,265,268,5,45,0,0,266,268,3,18,9,0,267,246,1,0,0,0,267,251,
        1,0,0,0,267,253,1,0,0,0,267,255,1,0,0,0,267,257,1,0,0,0,267,261,
        1,0,0,0,267,262,1,0,0,0,267,263,1,0,0,0,267,264,1,0,0,0,267,265,
        1,0,0,0,267,266,1,0,0,0,268,47,1,0,0,0,269,270,5,45,0,0,270,271,
        5,10,0,0,271,277,3,42,21,0,272,273,5,45,0,0,273,277,5,27,0,0,274,
        275,5,45,0,0,275,277,5,28,0,0,276,269,1,0,0,0,276,272,1,0,0,0,276,
        274,1,0,0,0,277,49,1,0,0,0,278,279,5,1,0,0,279,280,5,11,0,0,280,
        281,3,42,21,0,281,282,5,12,0,0,282,290,5,13,0,0,283,284,5,2,0,0,
        284,285,3,42,21,0,285,286,5,3,0,0,286,287,3,4,2,0,287,289,1,0,0,
        0,288,283,1,0,0,0,289,292,1,0,0,0,290,288,1,0,0,0,290,291,1,0,0,
        0,291,296,1,0,0,0,292,290,1,0,0,0,293,294,5,4,0,0,294,295,5,3,0,
        0,295,297,3,4,2,0,296,293,1,0,0,0,296,297,1,0,0,0,297,298,1,0,0,
        0,298,299,5,14,0,0,299,51,1,0,0,0,24,63,80,88,93,112,118,125,133,
        146,157,170,177,204,212,215,223,225,233,241,244,267,276,290,296
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'switch'", "'case'", "':'", "'default'", 
                     "'void'", "'entero'", "'decimal'", "'cadena'", "'bool'", 
                     "'='", "'('", "')'", "'{'", "'}'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'^'", "'<'", "'>'", "'<='", "'>='", 
                     "'=='", "'!='", "'++'", "'--'", "','", "';'", "'hola'", 
                     "'funcion'", "'retorna'", "'if'", "'else if'", "'else'", 
                     "'while'", "'for'", "'mostrar'", "'&&'", "'||'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'raiz'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "TIPO_VOID", "TIPO_ENTERO", "TIPO_DECIMAL", 
                      "TIPO_CADENA", "TIPO_BOOLEANO", "ASIGNACION", "PARENTESIS_INICIAL", 
                      "PARENTESIS_FINAL", "LLAVES_INICIAL", "LLAVES_FINAL", 
                      "MAS", "MENOS", "MULTIPLICACION", "DIVISION", "MODULO", 
                      "POTENCIA", "MENOR_QUE", "MAYOR_QUE", "MENOR_IGUAL_QUE", 
                      "MAYOR_IGUAL_QUE", "IGUAL", "DIFERENTE", "MASMAS", 
                      "MENOSMENOS", "COMA", "PUNTO_Y_COMA", "MAIN", "FUNCION", 
                      "RETURN", "IF", "ELSE_IF", "ELSE", "WHILE", "FOR", 
                      "MOSTRAR", "AND", "OR", "NUMERO", "BOOLEANO", "CADENA", 
                      "VARIABLE", "DECIMAL", "SIN_ESPACIO", "RAIZ", "COMENTARIO_LINEA", 
                      "COMENTARIO_BLOQUE" ]

    RULE_gramatica = 0
    RULE_programa = 1
    RULE_bloque = 2
    RULE_sentencia = 3
    RULE_sentencia_if = 4
    RULE_sentencia_while = 5
    RULE_sentencia_for = 6
    RULE_declaracion_funcion = 7
    RULE_funcion_llamada = 8
    RULE_funcion_llamada_expr = 9
    RULE_retorna = 10
    RULE_parametros = 11
    RULE_parametro = 12
    RULE_argumentos = 13
    RULE_bloque_condicional = 14
    RULE_bloque_de_sentencia = 15
    RULE_declaracion = 16
    RULE_declaracion_sin_asignacion = 17
    RULE_reasignacion = 18
    RULE_tipo = 19
    RULE_mostrar = 20
    RULE_expr = 21
    RULE_term = 22
    RULE_factor = 23
    RULE_actualizacion = 24
    RULE_sentencia_switch = 25

    ruleNames =  [ "gramatica", "programa", "bloque", "sentencia", "sentencia_if", 
                   "sentencia_while", "sentencia_for", "declaracion_funcion", 
                   "funcion_llamada", "funcion_llamada_expr", "retorna", 
                   "parametros", "parametro", "argumentos", "bloque_condicional", 
                   "bloque_de_sentencia", "declaracion", "declaracion_sin_asignacion", 
                   "reasignacion", "tipo", "mostrar", "expr", "term", "factor", 
                   "actualizacion", "sentencia_switch" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    TIPO_VOID=5
    TIPO_ENTERO=6
    TIPO_DECIMAL=7
    TIPO_CADENA=8
    TIPO_BOOLEANO=9
    ASIGNACION=10
    PARENTESIS_INICIAL=11
    PARENTESIS_FINAL=12
    LLAVES_INICIAL=13
    LLAVES_FINAL=14
    MAS=15
    MENOS=16
    MULTIPLICACION=17
    DIVISION=18
    MODULO=19
    POTENCIA=20
    MENOR_QUE=21
    MAYOR_QUE=22
    MENOR_IGUAL_QUE=23
    MAYOR_IGUAL_QUE=24
    IGUAL=25
    DIFERENTE=26
    MASMAS=27
    MENOSMENOS=28
    COMA=29
    PUNTO_Y_COMA=30
    MAIN=31
    FUNCION=32
    RETURN=33
    IF=34
    ELSE_IF=35
    ELSE=36
    WHILE=37
    FOR=38
    MOSTRAR=39
    AND=40
    OR=41
    NUMERO=42
    BOOLEANO=43
    CADENA=44
    VARIABLE=45
    DECIMAL=46
    SIN_ESPACIO=47
    RAIZ=48
    COMENTARIO_LINEA=49
    COMENTARIO_BLOQUE=50

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
            self.state = 52
            self.programa()
            self.state = 53
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
            self.state = 55
            self.match(ExprParser.MAIN)
            self.state = 56
            self.match(ExprParser.LLAVES_INICIAL)
            self.state = 57
            self.bloque()
            self.state = 58
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 60
                    self.sentencia() 
                self.state = 65
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

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


        def mostrar(self):
            return self.getTypedRuleContext(ExprParser.MostrarContext,0)


        def declaracion_sin_asignacion(self):
            return self.getTypedRuleContext(ExprParser.Declaracion_sin_asignacionContext,0)


        def declaracion(self):
            return self.getTypedRuleContext(ExprParser.DeclaracionContext,0)


        def actualizacion(self):
            return self.getTypedRuleContext(ExprParser.ActualizacionContext,0)


        def PUNTO_Y_COMA(self):
            return self.getToken(ExprParser.PUNTO_Y_COMA, 0)

        def declaracion_funcion(self):
            return self.getTypedRuleContext(ExprParser.Declaracion_funcionContext,0)


        def funcion_llamada(self):
            return self.getTypedRuleContext(ExprParser.Funcion_llamadaContext,0)


        def retorna(self):
            return self.getTypedRuleContext(ExprParser.RetornaContext,0)


        def sentencia_switch(self):
            return self.getTypedRuleContext(ExprParser.Sentencia_switchContext,0)


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
            self.state = 80
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.sentencia_if()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.sentencia_while()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.sentencia_for()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 69
                self.reasignacion()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 70
                self.mostrar()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 71
                self.declaracion_sin_asignacion()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 72
                self.declaracion()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 73
                self.actualizacion()
                self.state = 74
                self.match(ExprParser.PUNTO_Y_COMA)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 76
                self.declaracion_funcion()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 77
                self.funcion_llamada()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 78
                self.retorna()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 79
                self.sentencia_switch()
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
            self.state = 82
            self.match(ExprParser.IF)
            self.state = 83
            self.bloque_condicional()
            self.state = 88
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 84
                    self.match(ExprParser.ELSE_IF)
                    self.state = 85
                    self.bloque_condicional() 
                self.state = 90
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 91
                self.match(ExprParser.ELSE)
                self.state = 92
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
            self.state = 95
            self.match(ExprParser.WHILE)
            self.state = 96
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
            self.state = 98
            self.match(ExprParser.FOR)
            self.state = 99
            self.match(ExprParser.PARENTESIS_INICIAL)
            self.state = 100
            self.declaracion()
            self.state = 101
            self.expr(0)
            self.state = 102
            self.match(ExprParser.PUNTO_Y_COMA)
            self.state = 103
            self.actualizacion()
            self.state = 104
            self.match(ExprParser.PARENTESIS_FINAL)
            self.state = 105
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


        def LLAVES_FINAL(self):
            return self.getToken(ExprParser.LLAVES_FINAL, 0)

        def parametros(self):
            return self.getTypedRuleContext(ExprParser.ParametrosContext,0)


        def retorna(self):
            return self.getTypedRuleContext(ExprParser.RetornaContext,0)


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
            self.state = 107
            self.match(ExprParser.FUNCION)
            self.state = 108
            self.match(ExprParser.VARIABLE)
            self.state = 109
            self.tipo()
            self.state = 110
            self.match(ExprParser.PARENTESIS_INICIAL)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==45:
                self.state = 111
                self.parametros()


            self.state = 114
            self.match(ExprParser.PARENTESIS_FINAL)
            self.state = 115
            self.match(ExprParser.LLAVES_INICIAL)
            self.state = 116
            self.bloque()
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 117
                self.retorna()


            self.state = 120
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
            self.state = 122
            self.match(ExprParser.VARIABLE)
            self.state = 123
            self.match(ExprParser.PARENTESIS_INICIAL)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 417814418622464) != 0):
                self.state = 124
                self.argumentos()


            self.state = 127
            self.match(ExprParser.PARENTESIS_FINAL)
            self.state = 128
            self.match(ExprParser.PUNTO_Y_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funcion_llamada_exprContext(ParserRuleContext):
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

        def argumentos(self):
            return self.getTypedRuleContext(ExprParser.ArgumentosContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_funcion_llamada_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncion_llamada_expr" ):
                listener.enterFuncion_llamada_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncion_llamada_expr" ):
                listener.exitFuncion_llamada_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncion_llamada_expr" ):
                return visitor.visitFuncion_llamada_expr(self)
            else:
                return visitor.visitChildren(self)




    def funcion_llamada_expr(self):

        localctx = ExprParser.Funcion_llamada_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_funcion_llamada_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(ExprParser.VARIABLE)
            self.state = 131
            self.match(ExprParser.PARENTESIS_INICIAL)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 417814418622464) != 0):
                self.state = 132
                self.argumentos()


            self.state = 135
            self.match(ExprParser.PARENTESIS_FINAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetornaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ExprParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def PUNTO_Y_COMA(self):
            return self.getToken(ExprParser.PUNTO_Y_COMA, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_retorna

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRetorna" ):
                listener.enterRetorna(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRetorna" ):
                listener.exitRetorna(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRetorna" ):
                return visitor.visitRetorna(self)
            else:
                return visitor.visitChildren(self)




    def retorna(self):

        localctx = ExprParser.RetornaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_retorna)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(ExprParser.RETURN)
            self.state = 138
            self.expr(0)
            self.state = 139
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
        self.enterRule(localctx, 22, self.RULE_parametros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.parametro()
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 142
                self.match(ExprParser.COMA)
                self.state = 143
                self.parametro()
                self.state = 148
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
        self.enterRule(localctx, 24, self.RULE_parametro)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(ExprParser.VARIABLE)
            self.state = 150
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
        self.enterRule(localctx, 26, self.RULE_argumentos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.expr(0)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 153
                self.match(ExprParser.COMA)
                self.state = 154
                self.expr(0)
                self.state = 159
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
        self.enterRule(localctx, 28, self.RULE_bloque_condicional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(ExprParser.PARENTESIS_INICIAL)
            self.state = 161
            self.expr(0)
            self.state = 162
            self.match(ExprParser.PARENTESIS_FINAL)
            self.state = 163
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

        def sentencia(self):
            return self.getTypedRuleContext(ExprParser.SentenciaContext,0)


        def LLAVES_INICIAL(self):
            return self.getToken(ExprParser.LLAVES_INICIAL, 0)

        def bloque(self):
            return self.getTypedRuleContext(ExprParser.BloqueContext,0)


        def LLAVES_FINAL(self):
            return self.getToken(ExprParser.LLAVES_FINAL, 0)

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
        self.enterRule(localctx, 30, self.RULE_bloque_de_sentencia)
        try:
            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 32, 33, 34, 37, 38, 39, 45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.sentencia()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.match(ExprParser.LLAVES_INICIAL)
                self.state = 167
                self.bloque()
                self.state = 168
                self.match(ExprParser.LLAVES_FINAL)
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

        def PUNTO_Y_COMA(self):
            return self.getToken(ExprParser.PUNTO_Y_COMA, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def funcion_llamada(self):
            return self.getTypedRuleContext(ExprParser.Funcion_llamadaContext,0)


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
        self.enterRule(localctx, 32, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(ExprParser.VARIABLE)
            self.state = 173
            self.tipo()
            self.state = 174
            self.match(ExprParser.ASIGNACION)
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 175
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 176
                self.funcion_llamada()
                pass


            self.state = 179
            self.match(ExprParser.PUNTO_Y_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaracion_sin_asignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(ExprParser.VARIABLE, 0)

        def tipo(self):
            return self.getTypedRuleContext(ExprParser.TipoContext,0)


        def PUNTO_Y_COMA(self):
            return self.getToken(ExprParser.PUNTO_Y_COMA, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_declaracion_sin_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion_sin_asignacion" ):
                listener.enterDeclaracion_sin_asignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion_sin_asignacion" ):
                listener.exitDeclaracion_sin_asignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion_sin_asignacion" ):
                return visitor.visitDeclaracion_sin_asignacion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion_sin_asignacion(self):

        localctx = ExprParser.Declaracion_sin_asignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_declaracion_sin_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(ExprParser.VARIABLE)
            self.state = 182
            self.tipo()
            self.state = 183
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
        self.enterRule(localctx, 36, self.RULE_reasignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(ExprParser.VARIABLE)
            self.state = 186
            self.match(ExprParser.ASIGNACION)
            self.state = 187
            self.expr(0)
            self.state = 188
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

        def TIPO_VOID(self):
            return self.getToken(ExprParser.TIPO_VOID, 0)

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
        self.enterRule(localctx, 38, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 992) != 0)):
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
        self.enterRule(localctx, 40, self.RULE_mostrar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(ExprParser.MOSTRAR)
            self.state = 193
            self.match(ExprParser.PARENTESIS_INICIAL)
            self.state = 194
            self.expr(0)
            self.state = 195
            self.match(ExprParser.PARENTESIS_FINAL)
            self.state = 196
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

        def MODULO(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.MODULO)
            else:
                return self.getToken(ExprParser.MODULO, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def AND(self):
            return self.getToken(ExprParser.AND, 0)

        def OR(self):
            return self.getToken(ExprParser.OR, 0)

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
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 199
                self.term()
                self.state = 204
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 200
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 201
                        self.term() 
                    self.state = 206
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                pass

            elif la_ == 2:
                self.state = 207
                self.term()
                self.state = 212
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 208
                        self.match(ExprParser.MODULO)
                        self.state = 209
                        self.term() 
                    self.state = 214
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 225
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 223
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 217
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 218
                        _la = self._input.LA(1)
                        if not(_la==40 or _la==41):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 219
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 220
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 221
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 132120576) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 222
                        self.expr(4)
                        pass

             
                self.state = 227
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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

        def POTENCIA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.POTENCIA)
            else:
                return self.getToken(ExprParser.POTENCIA, i)

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
        self.enterRule(localctx, 44, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.factor()
                self.state = 233
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 229
                        _la = self._input.LA(1)
                        if not(_la==17 or _la==18):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 230
                        self.factor() 
                    self.state = 235
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.factor()
                self.state = 241
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 237
                        self.match(ExprParser.POTENCIA)
                        self.state = 238
                        self.factor() 
                    self.state = 243
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

                pass


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

        def RAIZ(self):
            return self.getToken(ExprParser.RAIZ, 0)

        def PARENTESIS_INICIAL(self):
            return self.getToken(ExprParser.PARENTESIS_INICIAL, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def PARENTESIS_FINAL(self):
            return self.getToken(ExprParser.PARENTESIS_FINAL, 0)

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

        def NUMERO(self):
            return self.getToken(ExprParser.NUMERO, 0)

        def DECIMAL(self):
            return self.getToken(ExprParser.DECIMAL, 0)

        def BOOLEANO(self):
            return self.getToken(ExprParser.BOOLEANO, 0)

        def CADENA(self):
            return self.getToken(ExprParser.CADENA, 0)

        def funcion_llamada_expr(self):
            return self.getTypedRuleContext(ExprParser.Funcion_llamada_exprContext,0)


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
        self.enterRule(localctx, 46, self.RULE_factor)
        try:
            self.state = 267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.match(ExprParser.RAIZ)
                self.state = 247
                self.match(ExprParser.PARENTESIS_INICIAL)
                self.state = 248
                self.expr(0)
                self.state = 249
                self.match(ExprParser.PARENTESIS_FINAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                self.match(ExprParser.MENOS)
                self.state = 252
                self.factor()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 253
                self.match(ExprParser.VARIABLE)
                self.state = 254
                self.match(ExprParser.MASMAS)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 255
                self.match(ExprParser.VARIABLE)
                self.state = 256
                self.match(ExprParser.MENOSMENOS)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 257
                self.match(ExprParser.PARENTESIS_INICIAL)
                self.state = 258
                self.expr(0)
                self.state = 259
                self.match(ExprParser.PARENTESIS_FINAL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 261
                self.match(ExprParser.NUMERO)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 262
                self.match(ExprParser.DECIMAL)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 263
                self.match(ExprParser.BOOLEANO)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 264
                self.match(ExprParser.CADENA)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 265
                self.match(ExprParser.VARIABLE)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 266
                self.funcion_llamada_expr()
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
        self.enterRule(localctx, 48, self.RULE_actualizacion)
        try:
            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.match(ExprParser.VARIABLE)
                self.state = 270
                self.match(ExprParser.ASIGNACION)
                self.state = 271
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 272
                self.match(ExprParser.VARIABLE)
                self.state = 273
                self.match(ExprParser.MASMAS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 274
                self.match(ExprParser.VARIABLE)
                self.state = 275
                self.match(ExprParser.MENOSMENOS)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sentencia_switchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARENTESIS_INICIAL(self):
            return self.getToken(ExprParser.PARENTESIS_INICIAL, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def PARENTESIS_FINAL(self):
            return self.getToken(ExprParser.PARENTESIS_FINAL, 0)

        def LLAVES_INICIAL(self):
            return self.getToken(ExprParser.LLAVES_INICIAL, 0)

        def LLAVES_FINAL(self):
            return self.getToken(ExprParser.LLAVES_FINAL, 0)

        def bloque(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.BloqueContext)
            else:
                return self.getTypedRuleContext(ExprParser.BloqueContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_sentencia_switch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia_switch" ):
                listener.enterSentencia_switch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia_switch" ):
                listener.exitSentencia_switch(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia_switch" ):
                return visitor.visitSentencia_switch(self)
            else:
                return visitor.visitChildren(self)




    def sentencia_switch(self):

        localctx = ExprParser.Sentencia_switchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_sentencia_switch)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(ExprParser.T__0)
            self.state = 279
            self.match(ExprParser.PARENTESIS_INICIAL)
            self.state = 280
            self.expr(0)
            self.state = 281
            self.match(ExprParser.PARENTESIS_FINAL)
            self.state = 282
            self.match(ExprParser.LLAVES_INICIAL)
            self.state = 290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 283
                self.match(ExprParser.T__1)
                self.state = 284
                self.expr(0)
                self.state = 285
                self.match(ExprParser.T__2)
                self.state = 286
                self.bloque()
                self.state = 292
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 293
                self.match(ExprParser.T__3)
                self.state = 294
                self.match(ExprParser.T__2)
                self.state = 295
                self.bloque()


            self.state = 298
            self.match(ExprParser.LLAVES_FINAL)
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
        self._predicates[21] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




