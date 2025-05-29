grammar Expr;

// Regla principal
gramatica: programa EOF;  // La gramática comienza con un bloque de sentencias y debe terminar en EOF

// Regla para el inicio del programa
programa: MAIN LLAVES_INICIAL bloque LLAVES_FINAL; 

// Bloque de sentencias
bloque: sentencia*;  // Un bloque puede contener cero o más sentencias

// Reglas de sentencias
sentencia: 
    sentencia_if  
  | sentencia_while  
  | sentencia_for 
  | reasignacion  
  | mostrar 
  | declaracion_sin_asignacion  
  | declaracion  
  | actualizacion PUNTO_Y_COMA 
  | declaracion_funcion
  | funcion_llamada
  | retorna
  | sentencia_switch
;

// Sentencia if
sentencia_if:
    IF bloque_condicional
    (ELSE_IF bloque_condicional)*
    (ELSE bloque_de_sentencia)?
;

// Sentencia while
sentencia_while:
    WHILE bloque_condicional
; 

// Sentencia for
sentencia_for:
    FOR PARENTESIS_INICIAL declaracion expr PUNTO_Y_COMA actualizacion PARENTESIS_FINAL bloque_de_sentencia
;  

// Declaración de funciones
declaracion_funcion:
    FUNCION VARIABLE tipo PARENTESIS_INICIAL parametros? PARENTESIS_FINAL LLAVES_INICIAL bloque (retorna)? LLAVES_FINAL
;

// Llamada a funciones
funcion_llamada:
    VARIABLE PARENTESIS_INICIAL argumentos? PARENTESIS_FINAL PUNTO_Y_COMA
;

funcion_llamada_expr:
    VARIABLE PARENTESIS_INICIAL argumentos? PARENTESIS_FINAL
;

// Retorno
retorna:
    RETURN expr PUNTO_Y_COMA
; 

// Parámetros y argumentos
parametros:
    parametro (COMA parametro)* 
;

parametro:
    VARIABLE tipo 
;

argumentos:
    expr (COMA expr)*
;

// Bloques condicionales
bloque_condicional:
    PARENTESIS_INICIAL expr PARENTESIS_FINAL bloque_de_sentencia
;  

bloque_de_sentencia:
    sentencia  // Una sola sentencia
  | LLAVES_INICIAL bloque LLAVES_FINAL  // Bloque entre llaves
;

// Declaraciones y reasignaciones
declaracion:
    VARIABLE tipo ASIGNACION (expr | funcion_llamada) PUNTO_Y_COMA
;  // Una declaración es una variable asignada a una expresión seguida de un punto y coma

declaracion_sin_asignacion:
    VARIABLE tipo PUNTO_Y_COMA
;

reasignacion:
    VARIABLE ASIGNACION expr PUNTO_Y_COMA
;

// Tipos de datos
tipo:
    TIPO_ENTERO
  | TIPO_DECIMAL 
  | TIPO_BOOLEANO
  | TIPO_CADENA 
  | TIPO_VOID
;

// Mostrar
mostrar:
    MOSTRAR PARENTESIS_INICIAL expr PARENTESIS_FINAL PUNTO_Y_COMA
;

// Expresiones
expr:
    expr (AND | OR) expr  // Operadores lógicos
  | expr (MENOR_QUE | MAYOR_QUE | MENOR_IGUAL_QUE | MAYOR_IGUAL_QUE | IGUAL | DIFERENTE) expr  
  | term ((MAS | MENOS) term)*  
  | term (MODULO term)*  // Soporte para módulo
;

term:
    factor ((MULTIPLICACION | DIVISION) factor)*  
  | factor (POTENCIA factor)*  // Soporte para potencias
;

factor:
    RAIZ PARENTESIS_INICIAL expr PARENTESIS_FINAL  // Soporte para raíces
  | MENOS factor              
  | VARIABLE MASMAS            
  | VARIABLE MENOSMENOS        
  | PARENTESIS_INICIAL expr PARENTESIS_FINAL  
  | NUMERO                     
  | DECIMAL                    
  | BOOLEANO                   
  | CADENA                     
  | VARIABLE                   
  | funcion_llamada_expr
;

// Actualización
actualizacion:
    VARIABLE ASIGNACION expr
  | VARIABLE MASMAS 
  | VARIABLE MENOSMENOS 
;

// Sentencia switch
sentencia_switch:
    'switch' PARENTESIS_INICIAL expr PARENTESIS_FINAL LLAVES_INICIAL
    ( 'case' expr ':' bloque )*
    ( 'default' ':' bloque )?
    LLAVES_FINAL
;

// Tokens
TIPO_VOID: 'void';
TIPO_ENTERO: 'entero';
TIPO_DECIMAL: 'decimal';
TIPO_CADENA: 'cadena';
TIPO_BOOLEANO: 'bool';

ASIGNACION: '=';  

PARENTESIS_INICIAL: '(';  // Paréntesis de apertura
PARENTESIS_FINAL: ')';  // Paréntesis de cierre
LLAVES_INICIAL: '{';  // Llave de apertura
LLAVES_FINAL: '}';  // Llave de cierre

MAS: '+';  
MENOS: '-';  
MULTIPLICACION: '*';  
DIVISION: '/';  
MODULO: '%';  
POTENCIA: '^';  

MENOR_QUE: '<';  
MAYOR_QUE: '>';  
MENOR_IGUAL_QUE: '<=';  
MAYOR_IGUAL_QUE: '>=';  
IGUAL: '==';  
DIFERENTE: '!=';  

MASMAS: '++';  
MENOSMENOS: '--';

COMA: ',';
PUNTO_Y_COMA: ';';  

MAIN: 'hola';
FUNCION: 'funcion';
RETURN: 'retorna';

IF: 'if';
ELSE_IF: 'else if';
ELSE: 'else';
WHILE: 'while';
FOR: 'for';
MOSTRAR: 'mostrar';
AND: '&&';
OR: '||';

NUMERO: '-'? [0-9]+;  // Número entero
BOOLEANO: 'verdadero' | 'falso';  // Valores booleanos permitidos
CADENA: '"' (~["])* '"';  // Cadenas de texto entre comillas dobles
VARIABLE: [a-zA-Z_][a-zA-Z0-9_]*;  // Nombre de variable (letras y números, empezando con letra o guion bajo)
DECIMAL: [0-9]+ '.' [0-9]+;  // Número decimal
SIN_ESPACIO: [ \t\r\n]+ -> skip;

RAIZ: 'raiz';

COMENTARIO_LINEA: '//' ~[\r\n]* -> skip;  // Comentarios de una línea
COMENTARIO_BLOQUE: '/*' .*? '*/' -> skip;  // Comentarios de múltiples líneas
