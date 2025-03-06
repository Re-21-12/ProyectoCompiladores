grammar Expr;


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

PUNTO_Y_COMA: ';';  // Separador de expresiones en el ciclo for

//Tokens
NUMERO: [0-9]+;  // Número entero
VARIABLE: [a-zA-Z_][a-zA-Z0-9_]*;  // Nombre de variable (letras y números, empezando con letra o guion bajo)
DECIMAL: [0-9]+ '.' [0-9]+;  // Número decimal

SIN_ESPACIO: [ \t\r\n]+ -> skip; 


gramatica: programa EOF;  // La gramática comienza con un bloque de sentencias y debe terminar en EOF

// Regla para el inicio del programa
programa: VARIABLE LLAVES_INICIAL bloque LLAVES_FINAL; 


bloque: sentencia*;  // Un bloque puede contener cero o más sentencias

// Reglas de sentencias
sentencia: 
    sentencia_if  
  | sentencia_while  
  | sentencia_for 
  | reasignacion  
  | declaracion  
  | mostrar 
  | actualizacion
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
  FOR PARENTESIS_INICIAL declaracion PUNTO_Y_COMA expr PUNTO_Y_COMA actualizacion PARENTESIS_FINAL bloque_de_sentencia;  


bloque_condicional:
  PARENTESIS_INICIAL expr PARENTESIS_FINAL bloque_de_sentencia;  

bloque_de_sentencia:
  LLAVES_INICIAL bloque LLAVES_FINAL  // Bloque entre llaves
  | sentencia  // O una sola sentencia
;

declaracion:
  VARIABLE tipo ASIGNACION expr PUNTO_Y_COMA;  // Una declaración es una variable asignada a una expresión seguida de un punto y coma

reasignacion:
  VARIABLE ASIGNACION expr PUNTO_Y_COMA;

tipo:
TIPO_ENTERO
| TIPO_DECIMAL 
;

mostrar:
  MOSTRAR PARENTESIS_INICIAL expr PARENTESIS_FINAL PUNTO_Y_COMA;  



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
  | VARIABLE                   // Variable
;
actualizacion:
    VARIABLE ASIGNACION expr
  | VARIABLE MASMAS
  | VARIABLE MENOSMENOS
;

