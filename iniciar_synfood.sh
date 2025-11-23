#!/bin/bash

# Script de inicio para SYNFOOD

echo "======================================"
echo "  SYNFOOD - Menús Trofológicos"
echo "======================================"
echo ""

# Verificar si Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 no está instalado"
    echo "Por favor, instale Python 3.9 o superior"
    exit 1
fi

echo "✓ Python instalado: $(python3 --version)"

# Verificar si las dependencias están instaladas
echo ""
echo "Verificando dependencias..."

if ! python3 -c "import streamlit" &> /dev/null; then
    echo "⚠️  Dependencias no encontradas. Instalando..."
    pip install -r requirements.txt
    echo "✓ Dependencias instaladas"
else
    echo "✓ Dependencias ya instaladas"
fi

echo ""
echo "======================================"
echo "Iniciando aplicación SYNFOOD..."
echo "======================================"
echo ""
echo "La aplicación se abrirá automáticamente"
echo "en su navegador en: http://localhost:8501"
echo ""
echo "Presione Ctrl+C para detener la aplicación"
echo ""

# Iniciar Streamlit
streamlit run app_streamlit.py
