grammar Expr;

gramatica: programa EOF;  // La gramática comienza con un bloque de sentencias y debe terminar en EOF

// Regla para el inicio del programa
programa: MAIN LLAVES_INICIAL bloque LLAVES_FINAL; 


bloque: sentencia*;  // Un bloque puede contener cero o más sentencias

//TODO: Aqui deberia ir el retorna 
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
;

sentencia_if:
  IF bloque_condicional
  (ELSE_IF bloque_condicional)*
  (ELSE bloque_de_sentencia)?
;

sentencia_while:
  WHILE bloque_condicional
; 

sentencia_for:
  FOR PARENTESIS_INICIAL declaracion expr PUNTO_Y_COMA actualizacion PARENTESIS_FINAL bloque_de_sentencia
;  

declaracion_funcion:
  FUNCION VARIABLE tipo PARENTESIS_INICIAL parametros? PARENTESIS_FINAL LLAVES_INICIAL bloque (retorna)? LLAVES_FINAL
;
funcion_llamada:
    VARIABLE PARENTESIS_INICIAL argumentos? PARENTESIS_FINAL PUNTO_Y_COMA
;
funcion_llamada_expr:
    VARIABLE PARENTESIS_INICIAL argumentos? PARENTESIS_FINAL
;
retorna:
RETURN expr PUNTO_Y_COMA
; 

parametros:
parametro (COMA parametro)* 
;
parametro:
VARIABLE tipo 
;
argumentos:
    expr (COMA expr)*
;

bloque_condicional:
  PARENTESIS_INICIAL expr PARENTESIS_FINAL bloque_de_sentencia
;  

bloque_de_sentencia:
  sentencia  // O una sola sentencia
  |LLAVES_INICIAL bloque LLAVES_FINAL  // Bloque entre llaves
;

declaracion:
  VARIABLE tipo ASIGNACION expr PUNTO_Y_COMA
;  // Una declaración es una variable asignada a una expresión seguida de un punto y coma

declaracion_sin_asignacion:
VARIABLE tipo PUNTO_Y_COMA
;

reasignacion:
  VARIABLE ASIGNACION expr PUNTO_Y_COMA
;

tipo:
TIPO_ENTERO
| TIPO_DECIMAL 
| TIPO_BOOLEANO
| TIPO_CADENA 
;

mostrar:
  MOSTRAR PARENTESIS_INICIAL expr PARENTESIS_FINAL PUNTO_Y_COMA
;  

expr:
    expr (MENOR_QUE | MAYOR_QUE | MENOR_IGUAL_QUE | MAYOR_IGUAL_QUE | IGUAL | DIFERENTE) expr  
  | term ((MAS | MENOS) term)*;  
term:
    factor ((MULTIPLICACION | DIVISION) factor)*;  // El término se compone de factores con multiplicaciones o divisiones
factor:
    MENOS factor              // Número negativo
  | VARIABLE MASMAS            // Incremento unario
  | VARIABLE MENOSMENOS        // Decremento unario
  | PARENTESIS_INICIAL expr PARENTESIS_FINAL  // Paréntesis
  | NUMERO                     // Número entero
  | DECIMAL                    // Número decimal
  | BOOLEANO                   // Valor booleano ('verdadero' o 'falso')
  | CADENA                     // Cadena de texto entre comillas
  | VARIABLE                   // Variable
  | funcion_llamada_expr
;

actualizacion:
    VARIABLE ASIGNACION expr
  | VARIABLE MASMAS 
  | VARIABLE MENOSMENOS 
;

// Reglas
// Palabras clave
IF: 'if';
ELSE_IF: 'else if';
ELSE: 'else';
WHILE: 'while';
FOR: 'for';
MOSTRAR: 'mostrar';

//Tipos de dato
TIPO_ENTERO: 'entero';
TIPO_DECIMAL: 'decimal';
TIPO_CADENA: 'cadena';
TIPO_BOOLEANO: 'bool';

//Simbolo de asignacion
ASIGNACION: '=';  

//Simbolos de agrupacion y estructura 
PARENTESIS_INICIAL: '(';  // Paréntesis de apertura
PARENTESIS_FINAL: ')';  // Paréntesis de cierre
LLAVES_INICIAL: '{';  // Llave de apertura
LLAVES_FINAL: '}';  // Llave de cierre

//Operadores aritmeticos
MAS: '+';  
MENOS: '-';  
MULTIPLICACION: '*';  
DIVISION: '/';  
MENOR_QUE: '<';  
MAYOR_QUE: '>';  
MENOR_IGUAL_QUE: '<=';  
MAYOR_IGUAL_QUE: '>=';  

//Operadores de decremento e incremeneto unario 
MASMAS: '++';  
MENOSMENOS: '--';

IGUAL: '==';  // Operador de comparación igual
DIFERENTE: '!=';  // Operador de comparación diferente

COMA: ',';
PUNTO_Y_COMA: ';';  // Separador de expresiones en el ciclo for

// KEYWORDS
MAIN: 'hola';
FUNCION: 'funcion';
RETURN: 'retorna';

//Tokens
NUMERO: [0-9]+;  // Número entero
BOOLEANO: 'verdadero' | 'falso';  // Valores booleanos permitidos
CADENA: '"' (~["])* '"';  // Cadenas de texto entre comillas dobles
VARIABLE: [a-zA-Z_][a-zA-Z0-9_]*;  // Nombre de variable (letras y números, empezando con letra o guion bajo)
DECIMAL: [0-9]+ '.' [0-9]+;  // Número decimal
SIN_ESPACIO: [ \t\r\n]+ -> skip; 
