# -*- coding: utf-8 -*-
"""
Base de datos de alimentos con propiedades nutricionales
Sistema de scoring para optimización multiobjetivo
"""

ALIMENTOS = {
    # PROTEÍNAS ANIMALES
    "huevo": {
        "categoria": "PROTEINA",
        "proteina_g": 6,
        "fibra_g": 0,
        "omega3": False,
        "antiinflamatorio": False,
        "carga_glucemica": 0,
        "es_tuberculo": False,
        "es_carne_roja": False
    },
    "pollo": {
        "categoria": "PROTEINA",
        "proteina_g": 8,
        "fibra_g": 0,
        "omega3": False,
        "antiinflamatorio": False,
        "carga_glucemica": 0,
        "es_tuberculo": False,
        "es_carne_roja": False
    },
    "pavo": {
        "categoria": "PROTEINA",
        "proteina_g": 8,
        "fibra_g": 0,
        "omega3": False,
        "antiinflamatorio": False,
        "carga_glucemica": 0,
        "es_tuberculo": False,
        "es_carne_roja": False
    },
    "res": {
        "categoria": "PROTEINA",
        "proteina_g": 8,
        "fibra_g": 0,
        "omega3": False,
        "antiinflamatorio": False,
        "carga_glucemica": 0,
        "es_tuberculo": False,
        "es_carne_roja": True
    },
    "pescado": {
        "categoria": "PROTEINA",
        "proteina_g": 8,
        "fibra_g": 0,
        "omega3": True,
        "antiinflamatorio": True,
        "carga_glucemica": 0,
        "es_tuberculo": False,
        "es_carne_roja": False
    },
    "salmon": {
        "categoria": "PROTEINA",
        "proteina_g": 8,
        "fibra_g": 0,
        "omega3": True,
        "antiinflamatorio": True,
        "carga_glucemica": 0,
        "es_tuberculo": False,
        "es_carne_roja": False
    },
    "trucha": {
        "categoria": "PROTEINA",
        "proteina_g": 8,
        "fibra_g": 0,
        "omega3": True,
        "antiinflamatorio": True,
        "carga_glucemica": 0,
        "es_tuberculo": False,
        "es_carne_roja": False
    },
    "caldo de hueso + proteina en polvo": {
        "categoria": "PROTEINA",
        "proteina_g": 20,
        "fibra_g": 0,
        "omega3": False,
        "antiinflamatorio": True,
        "carga_glucemica": 0,
        "es_tuberculo": False,
        "es_carne_roja": False
    },
    
    # TUBÉRCULOS Y CEREALES
    "papa": {
        "categoria": "TUBERCULO",
        "proteina_g": 0,
        "fibra_g": 2,
        "omega3": False,
        "antiinflamatorio": False,
        "carga_glucemica": 15,
        "es_tuberculo": True,
        "es_carne_roja": False
    },
    "yuca": {
        "categoria": "TUBERCULO",
        "proteina_g": 0,
        "fibra_g": 2,
        "omega3": False,
        "antiinflamatorio": False,
        "carga_glucemica": 16,
        "es_tuberculo": True,
        "es_carne_roja": False
    },
    "platano": {
        "categoria": "TUBERCULO",
        "proteina_g": 0,
        "fibra_g": 2,
        "omega3": False,
        "antiinflamatorio": False,
        "carga_glucemica": 18,
        "es_tuberculo": True,
        "es_carne_roja": False
    },
    "zapallo": {
        "categoria": "TUBERCULO",
        "proteina_g": 0,
        "fibra_g": 3,
        "omega3": False,
        "antiinflamatorio": True,
        "carga_glucemica": 8,
        "es_tuberculo": True,
        "es_carne_roja": False
    },
    "arroz": {
        "categoria": "TUBERCULO",
        "proteina_g": 0,
        "fibra_g": 1,
        "omega3": False,
        "antiinflamatorio": False,
        "carga_glucemica": 20,
        "es_tuberculo": True,
        "es_carne_roja": False
    },
    "remolacha": {
        "categoria": "TUBERCULO",
        "proteina_g": 0,
        "fibra_g": 3,
        "omega3": False,
        "antiinflamatorio": True,
        "carga_glucemica": 5,
        "es_tuberculo": True,
        "es_carne_roja": False
    },
    
    # VEGETALES
    "ensalada": {
        "categoria": "VEGETAL",
        "proteina_g": 0,
        "fibra_g": 3,
        "omega3": False,
        "antiinflamatorio": True,
        "carga_glucemica": 0,
        "es_tuberculo": False,
        "es_carne_roja": False
    },
    "pepino": {
        "categoria": "VEGETAL",
        "proteina_g": 0,
        "fibra_g": 2,
        "omega3": False,
        "antiinflamatorio": True,
        "carga_glucemica": 0,
        "es_tuberculo": False,
        "es_carne_roja": False
    },
    "apio": {
        "categoria": "VEGETAL",
        "proteina_g": 0,
        "fibra_g": 3,
        "omega3": False,
        "antiinflamatorio": True,
        "carga_glucemica": 0,
        "es_tuberculo": False,
        "es_carne_roja": False
    },
    "champinones": {
        "categoria": "VEGETAL",
        "proteina_g": 0,
        "fibra_g": 2,
        "omega3": False,
        "antiinflamatorio": True,
        "carga_glucemica": 0,
        "es_tuberculo": False,
        "es_carne_roja": False
    },
    "hongos": {
        "categoria": "VEGETAL",
        "proteina_g": 0,
        "fibra_g": 2,
        "omega3": False,
        "antiinflamatorio": True,
        "carga_glucemica": 0,
        "es_tuberculo": False,
        "es_carne_roja": False
    },
    "pimenton": {
        "categoria": "VEGETAL",
        "proteina_g": 0,
        "fibra_g": 2,
        "omega3": False,
        "antiinflamatorio": True,
        "carga_glucemica": 0,
        "es_tuberculo": False,
        "es_carne_roja": False
    },
    
    # GRASAS SALUDABLES
    "aguacate": {
        "categoria": "GRASA",
        "proteina_g": 0,
        "fibra_g": 7,
        "omega3": False,
        "antiinflamatorio": True,
        "carga_glucemica": 0,
        "es_tuberculo": False,
        "es_carne_roja": False
    },
    "aceite de oliva": {
        "categoria": "GRASA",
        "proteina_g": 0,
        "fibra_g": 0,
        "omega3": False,
        "antiinflamatorio": True,
        "carga_glucemica": 0,
        "es_tuberculo": False,
        "es_carne_roja": False
    },
    "aceite de coco": {
        "categoria": "GRASA",
        "proteina_g": 0,
        "fibra_g": 0,
        "omega3": False,
        "antiinflamatorio": True,
        "carga_glucemica": 0,
        "es_tuberculo": False,
        "es_carne_roja": False
    },
    "aceitunas": {
        "categoria": "GRASA",
        "proteina_g": 0,
        "fibra_g": 3,
        "omega3": False,
        "antiinflamatorio": True,
        "carga_glucemica": 0,
        "es_tuberculo": False,
        "es_carne_roja": False
    },
    "almendras": {
        "categoria": "GRASA",
        "proteina_g": 0,
        "fibra_g": 4,
        "omega3": False,
        "antiinflamatorio": True,
        "carga_glucemica": 0,
        "es_tuberculo": False,
        "es_carne_roja": False
    },
    "semillas de calabaza": {
        "categoria": "GRASA",
        "proteina_g": 0,
        "fibra_g": 3,
        "omega3": False,
        "antiinflamatorio": True,
        "carga_glucemica": 0,
        "es_tuberculo": False,
        "es_carne_roja": False
    },
    "maranones": {
        "categoria": "GRASA",
        "proteina_g": 0,
        "fibra_g": 3,
        "omega3": False,
        "antiinflamatorio": True,
        "carga_glucemica": 0,
        "es_tuberculo": False,
        "es_carne_roja": False
    },
    
    # FRUTAS
    "mango": {
        "categoria": "FRUTA",
        "proteina_g": 0,
        "fibra_g": 3,
        "omega3": False,
        "antiinflamatorio": True,
        "carga_glucemica": 10,
        "es_tuberculo": False,
        "es_carne_roja": False
    },
    "papaya": {
        "categoria": "FRUTA",
        "proteina_g": 0,
        "fibra_g": 2,
        "omega3": False,
        "antiinflamatorio": True,
        "carga_glucemica": 6,
        "es_tuberculo": False,
        "es_carne_roja": False
    },
    "coco": {
        "categoria": "FRUTA",
        "proteina_g": 0,
        "fibra_g": 9,
        "omega3": False,
        "antiinflamatorio": True,
        "carga_glucemica": 3,
        "es_tuberculo": False,
        "es_carne_roja": False
    },
    "frutos rojos": {
        "categoria": "FRUTA",
        "proteina_g": 0,
        "fibra_g": 9,
        "omega3": False,
        "antiinflamatorio": True,
        "carga_glucemica": 4,
        "es_tuberculo": False,
        "es_carne_roja": False
    },
    "piña": {
        "categoria": "FRUTA",
        "proteina_g": 0,
        "fibra_g": 2,
        "omega3": False,
        "antiinflamatorio": True,
        "carga_glucemica": 12,
        "es_tuberculo": False,
        "es_carne_roja": False
    },
    
    # FERMENTOS
    "caldo de hueso": {
        "categoria": "FERMENTO",
        "proteina_g": 0,
        "fibra_g": 0,
        "omega3": False,
        "antiinflamatorio": True,
        "carga_glucemica": 0,
        "es_tuberculo": False,
        "es_carne_roja": False
    },
    "vinagre de manzana": {
        "categoria": "FERMENTO",
        "proteina_g": 0,
        "fibra_g": 0,
        "omega3": False,
        "antiinflamatorio": True,
        "carga_glucemica": 0,
        "es_tuberculo": False,
        "es_carne_roja": False
    },
    "chucrut": {
        "categoria": "FERMENTO",
        "proteina_g": 0,
        "fibra_g": 2,
        "omega3": False,
        "antiinflamatorio": True,
        "carga_glucemica": 0,
        "es_tuberculo": False,
        "es_carne_roja": False
    }
}

# PESOS DE LA FUNCIÓN OBJETIVO POR TIPO DE OBJETIVO
PESOS_OBJETIVO = {
    "Obesidad": {
        "w_P": 1.5,      # Proteína alta
        "w_F": 2.0,      # Fibra MUY alta
        "w_Omega": 1.0,  # Omega-3 normal
        "w_A": 1.0,      # Antioxidantes normal
        "w_GL": 1.5,     # Penalizar MUCHO carga glucémica
        "w_D": 1.2       # Diversidad moderada
    },
    "Inflamacion": {
        "w_P": 1.2,      # Proteína moderada
        "w_F": 1.5,      # Fibra alta
        "w_Omega": 3.0,  # Omega-3 MUY alta (pescado prioritario)
        "w_A": 2.5,      # Antioxidantes MUY altos
        "w_GL": 0,     # Penalizar carga glucémica
        "w_D": 1.0       # Diversidad normal
    },
    "Mejorar_habitos": {
        "w_P": 1.0,      # Proteína balanceada
        "w_F": 1.0,      # Fibra balanceada
        "w_Omega": 1.0,  # Omega-3 balanceado
        "w_A": 1.0,      # Antioxidantes balanceados
        "w_GL": 0,     # Carga glucémica balanceada
        "w_D": 2.0       # Diversidad MUY alta (prioridad)
    }
}

# RESTRICCIONES POR OBJETIVO
RESTRICCIONES_OBJETIVO = {
    "Obesidad": {
        "evitar_carne_roja": False,
        "descripcion": "Alta proteína, alta fibra, baja carga glucémica"
    },
    "Inflamacion": {
        "evitar_carne_roja": True,
        "descripcion": "Alto omega-3, altos antioxidantes, prioridad pescado"
    },
    "Mejorar_habitos": {
        "evitar_carne_roja": False,
        "descripcion": "Balance general, máxima diversidad de alimentos"
    }
}