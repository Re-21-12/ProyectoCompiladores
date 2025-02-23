grammar Expr;

NUMERO: [0-9]+;  // Número entero
VARIABLE: [a-zA-Z_][a-zA-Z0-9_]*;  // Nombre de variable (letras y números, empezando con letra o guion bajo)
DECIMAL: [0-9]+ '.' [0-9]+;  // Número decimal
ASIGNACION: '=';  // Operador de asignación
IF: 'if';  // Palabra clave para la sentencia if
ELSE: 'else';  // Palabra clave para la sentencia else
WHILE: 'while';  // Palabra clave para la sentencia while
FOR: 'for';  // Palabra clave para la sentencia for
PARENTESIS_INICIAL: '(';  // Paréntesis de apertura
PARENTESIS_FINAL: ')';  // Paréntesis de cierre
LLAVES_INICIAL: '{';  // Llave de apertura
LLAVES_FINAL: '}';  // Llave de cierre
MAS: '+';  // Operador de suma
MENOS: '-';  // Operador de resta
MULTIPLICACION: '*';  // Operador de multiplicación
DIVISION: '/';  // Operador de división
MENOR_QUE: '<';  // Operador menor que
MAYOR_QUE: '>';  // Operador mayor que
MENOR_IGUAL_QUE: '<=';  // Operador menor o igual que
MAYOR_IGUAL_QUE: '>=';  // Operador mayor o igual que
MASMAS: '++';  // Operador de incremento
MENOSMENOS: '--';  // Operador de decremento
IGUAL: '==';  // Operador de comparación igual
DIFERENTE: '!=';  // Operador de comparación diferente
PUNTO_Y_COMA: ';';  // Separador de expresiones en el ciclo for
MOSTRAR: 'mostrar';  // Palabra clave para la sentencia mostrar
// Ignorar espacios, tabulaciones y saltos de línea
SIN_ESPACIO: [ \t\r\n]+ -> skip; 


gramatica: programa EOF;  // La gramática comienza con un bloque de sentencias y debe terminar en EOF

// Regla para el inicio del programa
programa: LLAVES_INICIAL bloque LLAVES_FINAL;  // Programa envuelto entre llaves


bloque: sentencia*;  // Un bloque puede contener cero o más sentencias

bloque_condicional:
  PARENTESIS_INICIAL expr PARENTESIS_FINAL bloque_de_sentencia;  // Condicional entre paréntesis con un bloque de sentencias

bloque_de_sentencia:
  LLAVES_INICIAL bloque LLAVES_FINAL  // Bloque entre llaves
  | sentencia  // O una sola sentencia
;

bloque_for:
  FOR PARENTESIS_INICIAL declaracion PUNTO_Y_COMA expr PUNTO_Y_COMA expr PARENTESIS_FINAL bloque_de_sentencia;  // Ciclo FOR con declaración, condición y actualización

// Regla para declaración de variables
declaracion:
  VARIABLE ASIGNACION expr PUNTO_Y_COMA;  // Una declaración es una variable asignada a una expresión seguida de un punto y coma

// Reglas de sentencias
sentencia: 
    declaracion  // Una sentencia puede ser una declaración
  | sentencia_if  // O una sentencia if
  | sentencia_while  // O una sentencia while
  | sentencia_for  // O una sentencia for
  | mostrar // O una sentencia de mostrar
;

mostrar:
  MOSTRAR PARENTESIS_INICIAL expr PARENTESIS_FINAL PUNTO_Y_COMA;  // Sentencia de mostrar un valor

sentencia_if:
  IF bloque_condicional (ELSE IF bloque_condicional)* (ELSE bloque_de_sentencia)?;  // Sentencia if con uno o más else if y un posible else

sentencia_while:
  WHILE PARENTESIS_INICIAL expr PARENTESIS_FINAL bloque_de_sentencia;  // Sentencia while que ejecuta un bloque mientras se cumple la expresión

sentencia_for:
  FOR PARENTESIS_INICIAL declaracion PUNTO_Y_COMA expr PUNTO_Y_COMA expr PARENTESIS_FINAL bloque_de_sentencia;  // Ciclo for con declaración, condición y actualización

// Expresiones (aritméticas, lógicas, etc.)
expr:
    term ((MAS | MENOS) term)* PUNTO_Y_COMA?;  // La expresión se compone de términos con sumas o restas, opcionalmente seguida de un punto y coma
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
