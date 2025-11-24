# -*- coding: utf-8 -*-
"""
Análisis de Sensibilidad del Modelo de Optimización SYNFOOD
Evalúa la robustez del modelo ante variaciones en parámetros clave
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from modelo_optimizacion import generar_menu_optimizado

# Configuración de gráficas
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 11

def contar_tuberculos_menu(df_menu):
    """Cuenta el número de tubérculos en el menú semanal"""
    tuberculos = ['papa', 'yuca', 'platano', 'zapallo', 'zanahoria', 'arroz', 'remolacha']
    contador = 0
    
    for col in df_menu.columns:
        for val in df_menu[col]:
            if any(t in str(val).lower() for t in tuberculos):
                contador += 1
    
    return contador

def contar_repeticiones_alimento(df_menu):
    """Analiza las repeticiones de alimentos en el menú"""
    alimentos = {}
    
    for col in df_menu.columns:
        for val in df_menu[col]:
            items = str(val).lower().split('+')
            for item in items:
                item = item.strip()
                if item:
                    alimentos[item] = alimentos.get(item, 0) + 1
    
    return alimentos

def calcular_diversidad(df_menu):
    """Calcula el número de alimentos únicos en el menú"""
    alimentos = contar_repeticiones_alimento(df_menu)
    return len(alimentos)

# Guardar y ejecutar
print("Archivo creado correctamente")
def analisis_sensibilidad_k_max():
    """
    Análisis 1: Sensibilidad del parámetro K_max (límite de carbohidratos)
    """
    print("\n" + "="*60)
    print("ANÁLISIS 1: SENSIBILIDAD DE K_MAX")
    print("="*60)
    
    # Parámetros fijos
    edad = 25
    sexo = "Femenino"
    actividad = "Activo"
    
    # Valores de k_max a probar (simulando diferentes objetivos)
    objetivos_test = {
        "Reducir obesidad": {"max_tuberculos_semana": 7, "evitar_carne_roja": False},
        "Control inflamación": {"max_tuberculos_semana": 7, "evitar_carne_roja": True},
        "Mejorar hábitos": {"max_tuberculos_semana": 10, "evitar_carne_roja": False}
    }
    
    resultados = []
    
    for objetivo, config in objetivos_test.items():
        print(f"\nGenerando menú para: {objetivo}")
        print(f"  Max tubérculos: {config['max_tuberculos_semana']}")
        
        # Generar menú
        df_menu, mensaje = generar_menu_optimizado(edad, sexo, actividad, objetivo)
        
        # Calcular métricas
        tuberculos = contar_tuberculos_menu(df_menu)
        diversidad = calcular_diversidad(df_menu)
        
        resultados.append({
            'Objetivo': objetivo,
            'K_max': config['max_tuberculos_semana'],
            'Tubérculos_reales': tuberculos,
            'Diversidad': diversidad,
            'Cumple_restricción': tuberculos <= config['max_tuberculos_semana']
        })
        
        print(f"  Tubérculos encontrados: {tuberculos}")
        print(f"  Diversidad: {diversidad} alimentos únicos")
        print(f"  Cumple restricción: {tuberculos <= config['max_tuberculos_semana']}")
    
    # Crear DataFrame de resultados
    df_resultados = pd.DataFrame(resultados)
    
    return df_resultados

def graficar_sensibilidad_k_max(df_resultados):
    """
    Genera gráficas del análisis de sensibilidad de K_max
    """
    print("\nGenerando gráficas...")
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Gráfica 1: K_max vs Tubérculos reales
    axes[0].bar(df_resultados['Objetivo'], df_resultados['Tubérculos_reales'], 
                color='#5dced6', alpha=0.7, label='Tubérculos en menú')
    axes[0].plot(df_resultados['Objetivo'], df_resultados['K_max'], 
                 'o-', color='#1e555c', linewidth=2, markersize=8, label='Límite K_max')
    axes[0].set_xlabel('Objetivo Nutricional')
    axes[0].set_ylabel('Cantidad de Tubérculos')
    axes[0].set_title('Sensibilidad de K_max: Límite vs Uso Real')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    plt.setp(axes[0].xaxis.get_majorticklabels(), rotation=15, ha='right')
    
    # Gráfica 2: Diversidad de alimentos
    axes[1].bar(df_resultados['Objetivo'], df_resultados['Diversidad'], 
                color='#1e555c', alpha=0.7)
    axes[1].set_xlabel('Objetivo Nutricional')
    axes[1].set_ylabel('Número de Alimentos Únicos')
    axes[1].set_title('Diversidad del Menú por Objetivo')
    axes[1].grid(True, alpha=0.3)
    plt.setp(axes[1].xaxis.get_majorticklabels(), rotation=15, ha='right')
    
    plt.tight_layout()
    plt.savefig('sensibilidad_k_max.png', dpi=300, bbox_inches='tight')
    print("Gráfica guardada: sensibilidad_k_max.png")
    
    return fig
def analisis_robustez_algoritmo():
    """
    Análisis 2: Robustez del algoritmo (consistencia de resultados)
    Ejecuta el modelo 30 veces con los mismos parámetros
    """
    print("\n" + "="*60)
    print("ANÁLISIS 2: ROBUSTEZ DEL ALGORITMO")
    print("="*60)
    
    # Parámetros fijos
    edad = 30
    sexo = "Masculino"
    actividad = "Activo"
    objetivo = "Mejorar hábitos"
    
    n_iteraciones = 30
    resultados = []
    
    print(f"\nEjecutando {n_iteraciones} iteraciones con parámetros idénticos...")
    
    for i in range(n_iteraciones):
        if (i + 1) % 10 == 0:
            print(f"  Iteración {i + 1}/{n_iteraciones}")
        
        df_menu, mensaje = generar_menu_optimizado(edad, sexo, actividad, objetivo)
        
        tuberculos = contar_tuberculos_menu(df_menu)
        diversidad = calcular_diversidad(df_menu)
        
        resultados.append({
            'Iteración': i + 1,
            'Tubérculos': tuberculos,
            'Diversidad': diversidad
        })
    
    df_robustez = pd.DataFrame(resultados)
    
    # Estadísticas
    print("\nEstadísticas de robustez:")
    print(f"  Tubérculos - Media: {df_robustez['Tubérculos'].mean():.2f}, Desv. Std: {df_robustez['Tubérculos'].std():.2f}")
    print(f"  Diversidad - Media: {df_robustez['Diversidad'].mean():.2f}, Desv. Std: {df_robustez['Diversidad'].std():.2f}")
    
    return df_robustez
def graficar_robustez(df_robustez):
    """
    Genera gráficas del análisis de robustez
    """
    print("\nGenerando gráficas de robustez...")
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Gráfica 1: Serie temporal de tubérculos
    axes[0, 0].plot(df_robustez['Iteración'], df_robustez['Tubérculos'], 
                    'o-', color='#5dced6', alpha=0.6, markersize=4)
    axes[0, 0].axhline(df_robustez['Tubérculos'].mean(), color='#1e555c', 
                       linestyle='--', linewidth=2, label='Media')
    axes[0, 0].set_xlabel('Iteración')
    axes[0, 0].set_ylabel('Cantidad de Tubérculos')
    axes[0, 0].set_title('Consistencia: Tubérculos por Iteración')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)
    
    # Gráfica 2: Histograma de tubérculos
    axes[0, 1].hist(df_robustez['Tubérculos'], bins=8, color='#5dced6', 
                    alpha=0.7, edgecolor='black')
    axes[0, 1].axvline(df_robustez['Tubérculos'].mean(), color='#1e555c', 
                       linestyle='--', linewidth=2, label='Media')
    axes[0, 1].set_xlabel('Cantidad de Tubérculos')
    axes[0, 1].set_ylabel('Frecuencia')
    axes[0, 1].set_title('Distribución: Tubérculos')
    axes[0, 1].legend()
    axes[0, 1].grid(True, alpha=0.3, axis='y')
    
    # Gráfica 3: Serie temporal de diversidad
    axes[1, 0].plot(df_robustez['Iteración'], df_robustez['Diversidad'], 
                    'o-', color='#1e555c', alpha=0.6, markersize=4)
    axes[1, 0].axhline(df_robustez['Diversidad'].mean(), color='#5dced6', 
                       linestyle='--', linewidth=2, label='Media')
    axes[1, 0].set_xlabel('Iteración')
    axes[1, 0].set_ylabel('Diversidad (alimentos únicos)')
    axes[1, 0].set_title('Consistencia: Diversidad por Iteración')
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3)
    
    # Gráfica 4: Histograma de diversidad
    axes[1, 1].hist(df_robustez['Diversidad'], bins=8, color='#1e555c', 
                    alpha=0.7, edgecolor='black')
    axes[1, 1].axvline(df_robustez['Diversidad'].mean(), color='#5dced6', 
                       linestyle='--', linewidth=2, label='Media')
    axes[1, 1].set_xlabel('Diversidad (alimentos únicos)')
    axes[1, 1].set_ylabel('Frecuencia')
    axes[1, 1].set_title('Distribución: Diversidad')
    axes[1, 1].legend()
    axes[1, 1].grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig('robustez_algoritmo.png', dpi=300, bbox_inches='tight')
    print("Gráfica guardada: robustez_algoritmo.png")
    
    return fig

def ejecutar_analisis_completo():
    """
    Ejecuta el análisis de sensibilidad completo y genera reporte
    """
    print("\n" + "="*60)
    print("SYNFOOD - ANÁLISIS DE SENSIBILIDAD")
    print("="*60)
    
    # Análisis 1: Sensibilidad de K_max
    df_k_max = analisis_sensibilidad_k_max()
    graficar_sensibilidad_k_max(df_k_max)
    
    # Guardar tabla de resultados
    df_k_max.to_csv('resultados_sensibilidad_k_max.csv', index=False)
    print("\nTabla guardada: resultados_sensibilidad_k_max.csv")
    
    # Análisis 2: Robustez del algoritmo
    df_robustez = analisis_robustez_algoritmo()
    graficar_robustez(df_robustez)
    
    # Guardar tabla de robustez
    df_robustez.to_csv('resultados_robustez.csv', index=False)
    print("\nTabla guardada: resultados_robustez.csv")
    
    # Resumen final
    print("\n" + "="*60)
    print("RESUMEN DE ANÁLISIS DE SENSIBILIDAD")
    print("="*60)
    
    print("\n1. SENSIBILIDAD DE K_MAX:")
    print(df_k_max.to_string(index=False))
    
    print("\n2. ROBUSTEZ DEL ALGORITMO:")
    print(f"   Tubérculos:")
    print(f"     - Media: {df_robustez['Tubérculos'].mean():.2f}")
    print(f"     - Desviación estándar: {df_robustez['Tubérculos'].std():.2f}")
    print(f"     - Coeficiente de variación: {(df_robustez['Tubérculos'].std() / df_robustez['Tubérculos'].mean() * 100):.2f}%")
    
    print(f"\n   Diversidad:")
    print(f"     - Media: {df_robustez['Diversidad'].mean():.2f}")
    print(f"     - Desviación estándar: {df_robustez['Diversidad'].std():.2f}")
    print(f"     - Coeficiente de variación: {(df_robustez['Diversidad'].std() / df_robustez['Diversidad'].mean() * 100):.2f}%")
    
    print("\n" + "="*60)
    print("ANÁLISIS COMPLETADO")
    print("Archivos generados:")
    print("  - sensibilidad_k_max.png")
    print("  - robustez_algoritmo.png")
    print("  - resultados_sensibilidad_k_max.csv")
    print("  - resultados_robustez.csv")
    print("="*60)


if __name__ == "__main__":
    ejecutar_analisis_completo()