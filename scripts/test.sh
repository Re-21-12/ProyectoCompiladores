#!/bin/bash

# 1. Verificar generación de archivos
echo "=== Archivos generados ==="
ls -l outputs/

# 2. Mostrar IR LLVM
echo -e "\n=== Código LLVM ==="
head -n 20 outputs/output.ll

# 3. Ejecutar programa
echo -e "\n=== Ejecución ==="
if [ -f outputs/program ]; then
    ./outputs/program
else
    echo "¡Error! No se encontró el ejecutable"
fi

# 4. Verificar resultado
echo -e "\n=== Estado final ==="
if [ $? -eq 0 ]; then
    echo "✔ Programa ejecutado correctamente"
else
    echo "✖ Error en la ejecución"
fi