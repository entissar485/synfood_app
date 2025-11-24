# -*- coding: utf-8 -*-
"""
Modelo de Optimización Multiobjetivo para Menús Trofológicos
Base matemática: f(x) = w_P*P + w_F*F + w_Omega*Ω + w_A*A - w_GL*GL + w_D*D
"""

import random
import pandas as pd
from base_alimentos import ALIMENTOS, PESOS_OBJETIVO, RESTRICCIONES_OBJETIVO

class OptimizadorMenuTrofologico:
    
    def __init__(self, edad, sexo, actividad, objetivo):
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
        self.objetivo = objetivo
        self.pesos = PESOS_OBJETIVO.get(objetivo, PESOS_OBJETIVO["Mejorar_habitos"])
        self.restricciones = RESTRICCIONES_OBJETIVO.get(objetivo, RESTRICCIONES_OBJETIVO["Mejorar_habitos"])
        self.dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        self.momentos = ["Desayuno", "Almuerzo", "Cena", "Snack"]
        self.alimentos_usados_global = {}
        
    def calcular_score_alimento(self, nombre_alimento, momento=None):
        """
        Función objetivo: Score = w_P*P + w_F*F + w_Omega*Ω + w_A*A - w_GL*GL
        Maximiza valor nutricional según pesos del objetivo
        """
        info = ALIMENTOS.get(nombre_alimento, {})
        
        score = 0
        score += self.pesos["w_P"] * info.get("proteina_g", 0)
        score += self.pesos["w_F"] * info.get("fibra_g", 0)
        score += self.pesos["w_Omega"] * (5 if info.get("omega3", False) else 0)
        score += self.pesos["w_A"] * (3 if info.get("antiinflamatorio", False) else 0)
        score -= self.pesos["w_GL"] * info.get("carga_glucemica", 0) * 0.3  # Reducir penalización
        
        # Bonus por diversidad (w_D): penalizar si ya se usó mucho
        veces_usado = self.alimentos_usados_global.get(nombre_alimento, 0)
        penalty = veces_usado * self.pesos["w_D"] * 5
        score -= penalty
        
        return score
    
    def seleccionar_mejor_alimento(self, opciones, momento=None):
        """
        Selecciona el alimento con mayor score con algo de aleatoriedad
        """
        if not opciones:
            return None
        
        candidatos = [(alimento, self.calcular_score_alimento(alimento, momento)) for alimento in opciones]
        candidatos.sort(key=lambda x: x[1], reverse=True)
        
        # Seleccionar entre los top 3 (no siempre el #1) para más variedad
        top_candidatos = candidatos[:min(3, len(candidatos))]
        seleccionado = random.choice(top_candidatos)[0]
        
        self.alimentos_usados_global[seleccionado] = self.alimentos_usados_global.get(seleccionado, 0) + 1
        
        return seleccionado
    
    def generar_desayuno(self):
        """
        Desayuno: Proteína + Grasa + Fermento
        Sin tubérculos (regla trofológica)
        """
        # Proteínas reales para desayuno
        proteinas = ["huevo", "pavo", "caldo de hueso + proteina en polvo"]
        grasas = ["aguacate", "aceite de oliva", "aceite de coco", "almendras", "semillas de calabaza", "aceitunas"]
        fermentos = ["vinagre de manzana", "kimchi", "chucrut"]
        
        proteina = self.seleccionar_mejor_alimento(proteinas)
        grasa = self.seleccionar_mejor_alimento(grasas)
        fermento = self.seleccionar_mejor_alimento(fermentos)
        
        return f"{proteina.title()} + {grasa.title()} + {fermento.title()}"
    
    def generar_almuerzo(self):
        """
        Almuerzo: Proteína + Grasa + Vegetal + Tubérculo (opcional)
        Regla: Si es carne roja, NO tubérculo
        Máximo 1 tubérculo por comida
        """
        evitar_res = self.restricciones.get("evitar_carne_roja", False)
        
        # Seleccionar proteína según objetivo
        if evitar_res:
            proteinas = ["pollo", "pescado", "salmon", "pavo", "trucha"]
        else:
            proteinas = ["pollo", "pescado", "salmon", "pavo", "trucha", "res"]
        
        proteina = self.seleccionar_mejor_alimento(proteinas)
        
        # Si es res, NO permitir tubérculo (regla trofológica)
        info_proteina = ALIMENTOS.get(proteina, {})
        es_carne_roja = info_proteina.get("es_carne_roja", False)
        
        # Grasa
        grasas = ["aguacate", "aceite de oliva", "aceitunas", "almendras", "semillas de calabaza", "marañones"]
        grasa = self.seleccionar_mejor_alimento(grasas)
        
        # Vegetal
        vegetales = ["ensalada", "pepino", "hongos", "apio", "champiñones"]
        vegetal = self.seleccionar_mejor_alimento(vegetales)
        
        # Tubérculo (solo si NO es carne roja)
        tuberculo = None
        if not es_carne_roja:
            tuberculos = ["papa", "yuca", "platano", "zapallo", "arroz", "remolacha"]
            tuberculo = self.seleccionar_mejor_alimento(tuberculos)
        
        if tuberculo:
            return f"{proteina.title()} + {grasa.title()} + {vegetal.title()} + {tuberculo.title()}"
        else:
            return f"{proteina.title()} + {grasa.title()} + {vegetal.title()}"
    
    def generar_cena(self):
        """
        Cena: Proteína + Grasa + Vegetal + Tubérculo (opcional)
        Máximo 1 tubérculo por comida
        """
        proteinas = ["pollo", "pescado", "salmon", "huevo", "pavo", "trucha"]
        grasas = ["aguacate", "aceite de oliva", "aceitunas", "maranones", "almendras"]
        vegetales = ["ensalada", "pepino", "champiñones", "apio", "hongos"]
        tuberculos = ["papa", "zapallo", "remolacha", "yuca", "platano"]
        
        proteina = self.seleccionar_mejor_alimento(proteinas)
        grasa = self.seleccionar_mejor_alimento(grasas)
        vegetal = self.seleccionar_mejor_alimento(vegetales)
        tuberculo = self.seleccionar_mejor_alimento(tuberculos)
        
        if tuberculo:
            return f"{proteina.title()} + {grasa.title()} + {vegetal.title()} + {tuberculo.title()}"
        else:
            return f"{proteina.title()} + {grasa.title()} + {vegetal.title()}"
    
    def generar_snack(self):
        """
        Snack: Fruta + Grasa
        Sin tubérculos
        """
        frutas = ["frutos rojos", "mango", "papaya", "coco", "piña","Hummus"]
        grasas = ["almendras", "semillas de calabaza", "marañones", "coco"]
        
        fruta = self.seleccionar_mejor_alimento(frutas)
        grasa = self.seleccionar_mejor_alimento(grasas)
        
        return f"{fruta.title()} + {grasa.title()}"
    
    def optimizar(self):
        """
        Genera menú semanal optimizado según función objetivo
        """
        menu = {}
        
        for dia in self.dias:
            menu[dia] = {}
            menu[dia]["Desayuno"] = self.generar_desayuno()
            menu[dia]["Almuerzo"] = self.generar_almuerzo()
            menu[dia]["Cena"] = self.generar_cena()
            menu[dia]["Snack"] = self.generar_snack()
        
        mensaje = f"Menú generado con optimización multiobjetivo para {self.objetivo}"
        return menu, mensaje
    
    def menu_a_dataframe(self, menu):
        """
        Convierte menú a DataFrame
        """
        data = []
        for momento in self.momentos:
            fila = {"Momento": momento}
            for dia in self.dias:
                fila[dia] = menu[dia][momento]
            data.append(fila)
        
        df = pd.DataFrame(data)
        df = df.set_index("Momento")
        return df


def generar_menu_optimizado(edad, sexo, actividad, objetivo):
    """
    Función principal para generar menú optimizado
    """
    optimizador = OptimizadorMenuTrofologico(edad, sexo, actividad, objetivo)
    menu, mensaje = optimizador.optimizar()
    df_menu = optimizador.menu_a_dataframe(menu)
    return df_menu, mensaje