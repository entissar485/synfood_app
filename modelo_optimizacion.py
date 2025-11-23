# -*- coding: utf-8 -*-
"""
Modelo de Optimización de Menús Trofológicos
Genera menús semanales siguiendo reglas estrictas de trofología
"""

import random
import pandas as pd
from base_alimentos import ALIMENTOS, RESTRICCIONES_OBJETIVO

class OptimizadorMenuTrofologico:
    
    def __init__(self, edad, sexo, actividad, objetivo):
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
        self.objetivo = objetivo
        self.restricciones_obj = RESTRICCIONES_OBJETIVO.get(objetivo, {})
        self.dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        self.momentos = ["Desayuno", "Almuerzo", "Cena", "Snack"]
        self.alimentos_usados = {"desayuno": {}, "almuerzo": {}, "cena": {}, "snack": {}}
        
    def seleccionar_sin_repetir(self, opciones, tipo_comida, max_repeticiones=2):
        """Selecciona un alimento evitando repeticiones excesivas"""
        disponibles = [a for a in opciones if self.alimentos_usados[tipo_comida].get(a, 0) < max_repeticiones]
        if not disponibles:
            disponibles = opciones
        seleccionado = random.choice(disponibles)
        self.alimentos_usados[tipo_comida][seleccionado] = self.alimentos_usados[tipo_comida].get(seleccionado, 0) + 1
        return seleccionado
        
    def generar_desayuno(self):
        """Genera desayuno: Proteína + Grasa + Fermento"""
        proteinas = ["huevo", "pollo", "proteina en polvo"]
        grasas = ["aguacate", "aceite de oliva", "aceite de coco", "almendras", "semillas de calabaza", "aceitunas"]
        fermentos = ["caldo de hueso", "vinagre de manzana", "kimchi"]
        
        proteina = self.seleccionar_sin_repetir(proteinas, "desayuno", 3)
        grasa = self.seleccionar_sin_repetir(grasas, "desayuno", 2)
        fermento = self.seleccionar_sin_repetir(fermentos, "desayuno", 2)
        
        return f"{proteina.title()} + {grasa.title()} + {fermento.title()}"
    
    def generar_almuerzo(self, usar_res=False):
        """Genera almuerzo: Proteína + Grasa + Vegetal + Tubérculo (si no es res)"""
        if usar_res:
            proteina = "res"
            tuberculo = None
        else:
            proteinas = ["pollo", "pescado", "salmon", "pavo", "trucha"]
            proteina = self.seleccionar_sin_repetir(proteinas, "almuerzo", 2)
            tuberculos = ["papa", "yuca", "platano", "zapallo", "zanahoria", "arroz", "remolacha"]
            tuberculo = self.seleccionar_sin_repetir(tuberculos, "almuerzo", 2)
        
        grasas = ["aguacate", "aceite de oliva", "aceitunas", "almendras", "semillas de calabaza", "maranones"]
        vegetales = ["ensalada", "pepino", "hongos", "pimenton", "apio", "champinones"]
        
        grasa = self.seleccionar_sin_repetir(grasas, "almuerzo", 2)
        vegetal = self.seleccionar_sin_repetir(vegetales, "almuerzo", 2)
        
        if tuberculo:
            return f"{proteina.title()} + {grasa.title()} + {vegetal.title()} + {tuberculo.title()}"
        else:
            return f"{proteina.title()} + {grasa.title()} + {vegetal.title()}"
    
    def generar_cena(self):
        """Genera cena: Proteína + Grasa + Vegetal + Tubérculo opcional"""
        proteinas = ["pollo", "pescado", "salmon", "huevo", "pavo", "trucha"]
        grasas = ["aguacate", "aceite de oliva", "aceitunas", "maranones", "almendras"]
        vegetales = ["ensalada", "pepino", "champinones", "pimenton", "apio", "hongos"]
        tuberculos = ["papa", "zapallo", "zanahoria", None, None]
        
        proteina = self.seleccionar_sin_repetir(proteinas, "cena", 2)
        grasa = self.seleccionar_sin_repetir(grasas, "cena", 2)
        vegetal = self.seleccionar_sin_repetir(vegetales, "cena", 2)
        tuberculo = random.choice(tuberculos)
        
        if tuberculo:
            return f"{proteina.title()} + {grasa.title()} + {vegetal.title()} + {tuberculo.title()}"
        else:
            return f"{proteina.title()} + {grasa.title()} + {vegetal.title()}"
    
    def generar_snack(self):
        """Genera snack: Fruta + Grasa"""
        frutas = ["mango", "papaya", "coco", "pina"]
        grasas = ["almendras", "semillas de calabaza", "maranones", "coco"]
        
        fruta = self.seleccionar_sin_repetir(frutas, "snack", 2)
        grasa = self.seleccionar_sin_repetir(grasas, "snack", 2)
        
        return f"{fruta.title()} + {grasa.title()}"
    
    def optimizar(self):
        """Genera el menú semanal completo"""
        menu = {}
        tuberculos_usados = 0
        max_tuberculos = self.restricciones_obj.get("max_tuberculos_semana", 10)
        evitar_res = self.restricciones_obj.get("evitar_carne_roja", False)
        
        for dia in self.dias:
            menu[dia] = {}
            
            menu[dia]["Desayuno"] = self.generar_desayuno()
            
            usar_res = False
            if not evitar_res and dia == "Martes" and random.random() > 0.5:
                usar_res = True
            
            almuerzo = self.generar_almuerzo(usar_res=usar_res)
            menu[dia]["Almuerzo"] = almuerzo
            
            if not usar_res and any(t in almuerzo.lower() for t in ["papa", "yuca", "platano", "zapallo", "zanahoria", "arroz"]):
                tuberculos_usados += 1
            
            if tuberculos_usados < max_tuberculos:
                menu[dia]["Cena"] = self.generar_cena()
                if any(t in menu[dia]["Cena"].lower() for t in ["papa", "zapallo", "zanahoria"]):
                    tuberculos_usados += 1
            else:
                proteinas = ["pollo", "pescado", "salmon", "huevo"]
                grasas = ["aguacate", "aceite de oliva", "aceitunas"]
                vegetales = ["ensalada", "pepino"]
                
                menu[dia]["Cena"] = f"{random.choice(proteinas).title()} + {random.choice(grasas).title()} + {random.choice(vegetales).title()}"
            
            menu[dia]["Snack"] = self.generar_snack()
        
        return menu, "Menú generado exitosamente"
    
    def menu_a_dataframe(self, menu):
        """Convierte el menú a DataFrame"""
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
    """Función principal para generar menú"""
    optimizador = OptimizadorMenuTrofologico(edad, sexo, actividad, objetivo)
    menu, mensaje = optimizador.optimizar()
    df_menu = optimizador.menu_a_dataframe(menu)
    return df_menu, mensaje