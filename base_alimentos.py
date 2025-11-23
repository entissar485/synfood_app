# -*- coding: utf-8 -*-
"""
Base de datos de alimentos con categorías trofológicas
Basado en protocolos reales de trofología
"""

CATEGORIAS = {
    "PROTEINA_ANIMAL": "Proteína Animal",
    "PROTEINA_VEGETAL": "Proteína Vegetal", 
    "TUBERCULO": "Tubérculo/Raíz",
    "VEGETAL": "Vegetal",
    "GRASA_SALUDABLE": "Grasa Saludable",
    "FRUTA_NEUTRA": "Fruta Neutra",
    "FRUTA_ACIDA": "Fruta Ácida",
    "FERMENTO": "Fermento",
    "CONDIMENTO": "Condimento",
    "CEREAL": "Cereal"
}

ALIMENTOS = {
    # PROTEÍNAS ANIMALES
    "pollo": {
        "categoria": "PROTEINA_ANIMAL",
        "subcategorias": ["carne_blanca"],
        "gramos_proteina_por_30g": 8,
        "omega3": False,
        "antiinflamatorio": False
    },
    "pavo": {
        "categoria": "PROTEINA_ANIMAL",
        "subcategorias": ["carne_blanca"],
        "gramos_proteina_por_30g": 8,
        "omega3": False,
        "antiinflamatorio": False
    },
    "res": {
        "categoria": "PROTEINA_ANIMAL",
        "subcategorias": ["carne_roja"],
        "gramos_proteina_por_30g": 8,
        "omega3": False,
        "antiinflamatorio": False
    },
    "pescado": {
        "categoria": "PROTEINA_ANIMAL",
        "subcategorias": ["pescado"],
        "gramos_proteina_por_30g": 8,
        "omega3": True,
        "antiinflamatorio": True
    },
    "salmon": {
        "categoria": "PROTEINA_ANIMAL",
        "subcategorias": ["pescado", "omega3"],
        "gramos_proteina_por_30g": 8,
        "omega3": True,
        "antiinflamatorio": True
    },
    "trucha": {
        "categoria": "PROTEINA_ANIMAL",
        "subcategorias": ["pescado", "omega3"],
        "gramos_proteina_por_30g": 8,
        "omega3": True,
        "antiinflamatorio": True
    },
    "huevo": {
        "categoria": "PROTEINA_ANIMAL",
        "subcategorias": ["huevo"],
        "gramos_proteina_por_30g": 6,
        "omega3": False,
        "antiinflamatorio": False
    },
    
    # PROTEÍNAS VEGETALES
    "proteina en polvo": {
        "categoria": "PROTEINA_VEGETAL",
        "subcategorias": ["proteina_polvo"],
        "gramos_proteina_por_30g": 20,
        "omega3": False,
        "antiinflamatorio": True
    },
    
    # TUBÉRCULOS Y RAÍCES
    "papa": {
        "categoria": "TUBERCULO",
        "subcategorias": ["tuberculo"],
        "omega3": False,
        "antiinflamatorio": False
    },
    "yuca": {
        "categoria": "TUBERCULO",
        "subcategorias": ["tuberculo"],
        "omega3": False,
        "antiinflamatorio": False
    },
    "platano": {
        "categoria": "TUBERCULO",
        "subcategorias": ["tuberculo"],
        "omega3": False,
        "antiinflamatorio": False
    },
    "zapallo": {
        "categoria": "TUBERCULO",
        "subcategorias": ["tuberculo", "antioxidante"],
        "omega3": False,
        "antiinflamatorio": True
    },
    "zanahoria": {
        "categoria": "TUBERCULO",
        "subcategorias": ["tuberculo", "antioxidante"],
        "omega3": False,
        "antiinflamatorio": True
    },
    "remolacha": {
        "categoria": "TUBERCULO",
        "subcategorias": ["tuberculo"],
        "omega3": False,
        "antiinflamatorio": True
    },
    
    # CEREALES
    "arroz": {
        "categoria": "CEREAL",
        "subcategorias": ["cereal"],
        "omega3": False,
        "antiinflamatorio": False
    },
    
    # VEGETALES
    "ensalada": {
        "categoria": "VEGETAL",
        "subcategorias": ["hoja_verde", "fibra"],
        "omega3": False,
        "antiinflamatorio": True
    },
    "pepino": {
        "categoria": "VEGETAL",
        "subcategorias": ["hidratante"],
        "omega3": False,
        "antiinflamatorio": True
    },
    "apio": {
        "categoria": "VEGETAL",
        "subcategorias": ["hidratante", "fibra"],
        "omega3": False,
        "antiinflamatorio": True
    },
    "champinones": {
        "categoria": "VEGETAL",
        "subcategorias": ["hongo"],
        "omega3": False,
        "antiinflamatorio": True
    },
    "hongos": {
        "categoria": "VEGETAL",
        "subcategorias": ["hongo"],
        "omega3": False,
        "antiinflamatorio": True
    },
    "pimenton": {
        "categoria": "VEGETAL",
        "subcategorias": ["vitamina_c"],
        "omega3": False,
        "antiinflamatorio": True
    },
    
    # GRASAS SALUDABLES
    "aguacate": {
        "categoria": "GRASA_SALUDABLE",
        "subcategorias": ["grasa_monoinsaturada", "fibra"],
        "omega3": False,
        "antiinflamatorio": True
    },
    "aceite de oliva": {
        "categoria": "GRASA_SALUDABLE",
        "subcategorias": ["grasa_monoinsaturada", "polifenoles"],
        "omega3": False,
        "antiinflamatorio": True
    },
    "aceite de coco": {
        "categoria": "GRASA_SALUDABLE",
        "subcategorias": ["grasa_saturada_vegetal"],
        "omega3": False,
        "antiinflamatorio": True
    },
    "aceitunas": {
        "categoria": "GRASA_SALUDABLE",
        "subcategorias": ["grasa_monoinsaturada"],
        "omega3": False,
        "antiinflamatorio": True
    },
    "almendras": {
        "categoria": "GRASA_SALUDABLE",
        "subcategorias": ["fibra", "fruto_seco"],
        "omega3": False,
        "antiinflamatorio": True
    },
    "semillas de calabaza": {
        "categoria": "GRASA_SALUDABLE",
        "subcategorias": ["semilla", "zinc"],
        "omega3": False,
        "antiinflamatorio": True
    },
    "maranones": {
        "categoria": "GRASA_SALUDABLE",
        "subcategorias": ["fruto_seco"],
        "omega3": False,
        "antiinflamatorio": True
    },
    "ghee": {
        "categoria": "GRASA_SALUDABLE",
        "subcategorias": ["grasa_animal"],
        "omega3": False,
        "antiinflamatorio": False
    },
    
    # FRUTAS NEUTRAS
    "mango": {
        "categoria": "FRUTA_NEUTRA",
        "subcategorias": ["fibra_soluble"],
        "omega3": False,
        "antiinflamatorio": True
    },
    "papaya": {
        "categoria": "FRUTA_NEUTRA",
        "subcategorias": ["enzimas_digestivas"],
        "omega3": False,
        "antiinflamatorio": True
    },
    "coco": {
        "categoria": "FRUTA_NEUTRA",
        "subcategorias": ["grasa_saturada"],
        "omega3": False,
        "antiinflamatorio": True
    },
    
    # FRUTAS ÁCIDAS
    "limon": {
        "categoria": "FRUTA_ACIDA",
        "subcategorias": ["vitamina_c"],
        "omega3": False,
        "antiinflamatorio": True
    },
    "pina": {
        "categoria": "FRUTA_ACIDA",
        "subcategorias": ["enzimas_digestivas", "vitamina_c"],
        "omega3": False,
        "antiinflamatorio": True
    },
    
    # FERMENTOS
    "caldo de hueso": {
        "categoria": "FERMENTO",
        "subcategorias": ["colageno", "minerales"],
        "omega3": False,
        "antiinflamatorio": True
    },
    "vinagre de manzana": {
        "categoria": "FERMENTO",
        "subcategorias": ["acido"],
        "omega3": False,
        "antiinflamatorio": True
    },
    "kimchi": {
        "categoria": "FERMENTO",
        "subcategorias": ["probiotico"],
        "omega3": False,
        "antiinflamatorio": True
    },
    "chucrut": {
        "categoria": "FERMENTO",
        "subcategorias": ["probiotico"],
        "omega3": False,
        "antiinflamatorio": True
    },
    
    # CONDIMENTOS
    "oregano": {
        "categoria": "CONDIMENTO",
        "subcategorias": ["antiinflamatorio"],
        "omega3": False,
        "antiinflamatorio": True
    },
    "ajo": {
        "categoria": "CONDIMENTO",
        "subcategorias": ["antiinflamatorio"],
        "omega3": False,
        "antiinflamatorio": True
    },
    "curry": {
        "categoria": "CONDIMENTO",
        "subcategorias": ["antiinflamatorio"],
        "omega3": False,
        "antiinflamatorio": True
    },
    "cilantro": {
        "categoria": "CONDIMENTO",
        "subcategorias": ["digestivo"],
        "omega3": False,
        "antiinflamatorio": True
    }
}

# REGLAS TROFOLÓGICAS ESTRICTAS
REGLAS_INCOMPATIBILIDAD = [
    {
        "nombre": "res_con_tuberculo",
        "descripcion": "Res + tubérculo/cereal",
        "penalizacion": 100.0,
        "fundamento": "La res NO se mezcla con carbohidratos. Competencia enzimática."
    },
    {
        "nombre": "frutas_con_comida",
        "descripcion": "Frutas con comida principal",
        "penalizacion": 100.0,
        "fundamento": "Las frutas NO se mezclan con comidas principales. Solo como snack."
    },
    {
        "nombre": "multiples_proteinas",
        "descripcion": "Más de 1 proteína en misma comida",
        "penalizacion": 100.0,
        "fundamento": "Evitar mezclar varias proteínas en una comida."
    },
    {
        "nombre": "multiples_tuberculos",
        "descripcion": "Más de 1 tubérculo/cereal en misma comida",
        "penalizacion": 100.0,
        "fundamento": "Evitar mezclar varios carbohidratos en una comida."
    }
]

RESTRICCIONES_OBJETIVO = {
    "Obesidad": {
        "max_tuberculos_semana": 7,
        "prioridad_proteina": True,
        "prioridad_fibra": True
    },
    "Inflamacion": {
        "max_tuberculos_semana": 7,
        "prioridad_omega3": True,
        "evitar_carne_roja": True
    },
    "Mejorar_habitos": {
        "max_tuberculos_semana": 10,
        "balance_general": True
    }
}

def obtener_alimento(nombre_normalizado):
    return ALIMENTOS.get(nombre_normalizado, None)

def tiene_categoria(alimento_info, categoria):
    if not alimento_info:
        return False
    return alimento_info["categoria"] == categoria

def tiene_subcategoria(alimento_info, subcategoria):
    if not alimento_info:
        return False
    return subcategoria in alimento_info.get("subcategorias", [])