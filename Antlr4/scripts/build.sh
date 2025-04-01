#!/bin/bash

# Configuración
LL_FILE="../outputs/program.ll"
OUTPUT_DIR="../outputs"

# Generar IR LLVM (esto lo ejecuta tu código Python)
python3 ../src/main.py

# Compilar a objeto
echo "Compilando LLVM IR a objeto..."
llc -filetype=obj $LL_FILE -o $OUTPUT_DIR/program.o

# Generar ensamblador
echo "Generando código ensamblador..."
llc -march=x86-64 $LL_FILE -o $OUTPUT_DIR/program.s

# Optimizar (opcional)
echo "Optimizando IR..."
opt -O3 -S $LL_FILE -o $OUTPUT_DIR/optimized.ll

# Enlazar para crear ejecutable
echo "Generando ejecutable..."
clang $OUTPUT_DIR/program.o -o $OUTPUT_DIR/program

# Dar permisos de ejecución
chmod +x $OUTPUT_DIR/program

echo "Compilación completada!"
echo "Ejecutable disponible en: $OUTPUT_DIR/program"