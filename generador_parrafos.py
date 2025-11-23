# -*- coding: utf-8 -*-
"""
Generador de párrafos personalizados con recomendaciones trofológicas
Incluye cálculo de proteína y recomendaciones detalladas
"""

class GeneradorParrafos:
    
    def __init__(self, edad, sexo, actividad, objetivo):
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
        self.objetivo = objetivo
    
    def calcular_proteina(self):
        """Calcula los gramos de proteína según perfil"""
        # Rangos de edad
        if self.edad in ["18-25", "26-35", "36-45"]:
            if self.actividad == "Nula":
                return "0.8 a 1.0"
            else:  # Moderada o Alta
                return "1.5"
        elif self.edad in ["46-55", "56-65", "66+"]:
            return "1.5"
        else:
            return "1.0"
    
    def generar_intro(self):
        """Genera introducción personalizada"""
        objetivos_texto = {
            "Obesidad": "reducción de grasa corporal y optimización metabólica",
            "Inflamacion": "reducción de marcadores inflamatorios sistémicos",
            "Mejorar_habitos": "establecimiento de hábitos alimenticios sostenibles"
        }
        
        texto = f"PROTOCOLO TROFOLÓGICO PERSONALIZADO\n\n"
        texto += f"Este plan ha sido diseñado específicamente para {objetivos_texto.get(self.objetivo, 'tu objetivo')}. "
        texto += f"Considerando tu perfil (edad: {self.edad}, sexo: {self.sexo}, actividad: {self.actividad}), "
        texto += "se han aplicado principios científicos de trofología para maximizar la digestión, "
        texto += "absorción de nutrientes y bienestar general.\n\n"
        
        return texto
    
    def generar_proteina_seccion(self):
        """Genera sección de cálculo de proteína"""
        gramos = self.calcular_proteina()
        
        texto = "CÁLCULO DE PROTEÍNA EFECTIVA\n\n"
        texto += f"En tu caso, teniendo en cuenta tu sexo ({self.sexo}), edad ({self.edad}), "
        texto += f"nivel de actividad física ({self.actividad}) y objetivo ({self.objetivo.replace('_', ' ')}), "
        texto += f"debes consumir {gramos} gramos de proteína efectiva (PE) por cada kilo de tu peso ideal.\n\n"
        
        texto += "CONVERSIÓN DE PROTEÍNA:\n"
        texto += "• Cada 30 gramos de pollo, pescado o carne de res (cocidos) aportan aproximadamente 8 gramos de proteína efectiva.\n"
        texto += "• Los huevos aportan aproximadamente 6 gramos de proteína efectiva por unidad.\n\n"
        
        texto += "EJEMPLO: Si pesas 70 kg y debes consumir 1.5g de PE por kilo:\n"
        texto += "70 kg × 1.5 = 105 gramos de proteína efectiva al día.\n\n"
        
        return texto
    
    def generar_estructura_menu(self):
        """Genera estructura del menú"""
        texto = "ESTRUCTURA DEL MENÚ\n\n"
        
        texto += "DESAYUNO:\n"
        texto += "1 Proteína + 1 Grasa saludable + 1 Fermento (20-30 min antes)\n"
        texto += "El fermento debe consumirse 20-30 minutos antes de la comida para optimizar la colonización bacteriana.\n\n"
        
        texto += "ALMUERZO Y CENA:\n"
        texto += "1 Proteína + 1 Grasa saludable + Vegetales + 1 Tubérculo/Cereal\n"
        texto += "EXCEPCIÓN: Si consumes carne de res, NO incluir tubérculo ni cereal en esa comida.\n\n"
        
        texto += "SNACKS:\n"
        texto += "1 Fruta neutra + 1 Grasa saludable\n"
        texto += "Siempre empezar con la grasa saludable antes de consumir la fruta.\n\n"
        
        return texto
    
    def generar_reglas_trofologicas(self):
        """Genera reglas trofológicas fundamentales"""
        texto = "REGLAS TROFOLÓGICAS FUNDAMENTALES\n\n"
        
        texto += "EVITAR:\n"
        texto += "• Mezclar carne de res con tubérculos o cereales (competencia enzimática).\n"
        texto += "• Mezclar frutas con comidas principales (fermentación).\n"
        texto += "• Mezclar varias proteínas en una misma comida.\n"
        texto += "• Mezclar varios carbohidratos complejos en una misma comida.\n"
        texto += "• Consumir agua durante las comidas (diluye enzimas digestivas).\n"
        texto += "• Alimentos procesados, fritos, azúcares y harinas refinadas.\n\n"
        
        texto += "PRIORIZAR:\n"
        texto += "• Proteína + Grasa saludable en cada comida (mejora saciedad y absorción).\n"
        texto += "• Aceite de oliva virgen extra EN CRUDO (nunca cocinado).\n"
        texto += "• Fermentos probióticos antes de las comidas.\n"
        texto += "• Vegetales en almuerzo y cena.\n\n"
        
        return texto
    
    def generar_recomendaciones_especificas(self):
        """Genera recomendaciones específicas"""
        texto = "RECOMENDACIONES ESPECÍFICAS\n\n"
        
        if self.objetivo == "Obesidad":
            texto += "PARA REDUCCIÓN DE GRASA:\n"
            texto += f"• Máximo 7 porciones de tubérculos/cereales por semana.\n"
            texto += "• Priorizar proteína en cada comida para mantener masa muscular.\n"
            texto += "• Consumir grasas saludables para saciedad prolongada.\n"
            texto += "• Evitar snacks si no hay hambre real.\n\n"
        
        elif self.objetivo == "Inflamacion":
            texto += "PARA REDUCCIÓN DE INFLAMACIÓN:\n"
            texto += "• Consumir pescados grasos (salmón, trucha) mínimo 3 veces por semana.\n"
            texto += "• Evitar completamente la carne roja.\n"
            texto += "• Incluir especias antiinflamatorias: cúrcuma, jengibre, ajo.\n"
            texto += "• Priorizar aceite de oliva crudo en todas las comidas.\n\n"
        
        else:  # Mejorar_habitos
            texto += "PARA ESTABLECER HÁBITOS:\n"
            texto += "• Hasta 10 porciones de tubérculos/cereales por semana (flexibilidad).\n"
            texto += "• Enfocarse en la consistencia, no en la perfección.\n"
            texto += "• Permitir variaciones según contexto social.\n"
            texto += "• Registrar cómo te sientes después de cada comida.\n\n"
        
        if self.sexo == "Femenino":
            texto += "CONSIDERACIONES PARA MUJERES:\n"
            texto += "• Priorizar hierro: vegetales de hoja verde, semillas de calabaza.\n"
            texto += "• Consumir suficiente calcio vegetal: brócoli, almendras.\n"
            if self.edad in ["18-25", "26-35", "36-45"]:
                texto += "• Considerar ciclo menstrual para ajustar carbohidratos según energía.\n\n"
            else:
                texto += "• En menopausia, enfatizar calcio y vitamina D para salud ósea.\n\n"
        else:
            texto += "CONSIDERACIONES PARA HOMBRES:\n"
            texto += "• Las grasas saludables apoyan producción de testosterona.\n"
            texto += "• Zinc presente en semillas de calabaza es fundamental.\n\n"
        
        if self.actividad == "Alta":
            texto += "PARA ACTIVIDAD FÍSICA ALTA:\n"
            texto += "• Consumir tubérculos preferentemente post-entrenamiento.\n"
            texto += "• Asegurar suficiente proteína para recuperación muscular.\n"
            texto += "• Hidratación constante fuera de las comidas.\n\n"
        elif self.actividad == "Nula":
            texto += "PARA SEDENTARISMO:\n"
            texto += "• Limitar tubérculos a 5-7 porciones semanales.\n"
            texto += "• Caminatas de 20-30 minutos post-comida mejoran sensibilidad a insulina.\n\n"
        
        return texto
    
    def generar_hidratacion_habitos(self):
        """Genera recomendaciones de hidratación y hábitos"""
        texto = "HIDRATACIÓN Y HÁBITOS\n\n"
        
        texto += "PROTOCOLO DE AGUA:\n"
        texto += "• Consumir 500ml de agua 30 minutos ANTES de cada comida principal.\n"
        texto += "• EVITAR líquidos durante las comidas.\n"
        texto += "• Reanudar hidratación 60 minutos DESPUÉS de comer.\n"
        texto += "• Objetivo diario: 30-35ml por kg de peso corporal.\n\n"
        
        texto += "SUPLEMENTACIÓN RECOMENDADA:\n"
        texto += "• Glutamina: 5 gramos diarios después de cenar (salud intestinal).\n"
        texto += "• Magnesio quelado: 2-3 cápsulas después de cenar (sueño y recuperación).\n"
        texto += "• Vitamina C: 1 cápsula con el desayuno (sistema inmune).\n"
        texto += "• Zinc: 1 cápsula con el desayuno (sistema inmune y hormonal).\n\n"
        
        texto += "HÁBITOS ESENCIALES:\n"
        texto += "• Dormir 7-8 horas diarias (regula leptina y grelina).\n"
        texto += "• Exponerse al sol 15-20 minutos diarios (vitamina D).\n"
        texto += "• Masticar lentamente cada bocado (mejora digestión).\n"
        texto += "• Comer solo cuando haya hambre real, no por hábito.\n\n"
        
        return texto
    
    def generar_orden_consumo(self):
        """Genera orden de consumo"""
        texto = "ORDEN DE CONSUMO DE ALIMENTOS\n\n"
        texto += "Siempre consumir en este orden dentro de cada comida:\n"
        texto += "1. Fermento (20-30 min antes)\n"
        texto += "2. Proteína\n"
        texto += "3. Grasa saludable\n"
        texto += "4. Vegetales\n"
        texto += "5. Tubérculo/Cereal (si aplica)\n\n"
        
        return texto
    
    def generar_cierre(self):
        """Genera cierre del protocolo"""
        texto = "SEGUIMIENTO Y AJUSTES\n\n"
        texto += "Este protocolo es un punto de partida. Se recomienda:\n"
        texto += "• Evaluar tu respuesta a las 2-4 semanas.\n"
        texto += "• Registrar: energía, calidad digestiva, bienestar general.\n"
        texto += "• Ajustar según tus necesidades individuales.\n"
        texto += "• Consultar con profesional de salud para condiciones médicas específicas.\n\n"
        texto += "La consistencia es más importante que la perfección. Enfócate en crear hábitos sostenibles.\n"
        
        return texto
    
    def generar_parrafo_completo(self):
        """Genera el párrafo completo"""
        parrafo = ""
        parrafo += self.generar_intro()
        parrafo += self.generar_proteina_seccion()
        parrafo += self.generar_estructura_menu()
        parrafo += self.generar_reglas_trofologicas()
        parrafo += self.generar_recomendaciones_especificas()
        parrafo += self.generar_orden_consumo()
        parrafo += self.generar_hidratacion_habitos()
        parrafo += self.generar_cierre()
        
        return parrafo


def generar_parrafo_personalizado(edad, sexo, actividad, objetivo):
    """Función principal para generar párrafo"""
    generador = GeneradorParrafos(edad, sexo, actividad, objetivo)
    return generador.generar_parrafo_completo()
