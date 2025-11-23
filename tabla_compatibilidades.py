# -*- coding: utf-8 -*-
"""
Generador de tabla de compatibilidades
Presenta las reglas de combinación de alimentos de forma clara
"""

import pandas as pd

TABLA_COMPATIBILIDADES = [
    {
        "Combinación": "Proteína animal + grasa saludable (AOVE, aguacate)",
        "Estado": "✓ RECOMENDADO",
        "Fundamento Científico": "Mejora la absorción de vitaminas liposolubles (A, D, E, K), atenúa la respuesta glucémica postprandial mediante ralentización del vaciamiento gástrico y aumenta la saciedad vía estimulación de CCK (colecistoquinina)."
    },
    {
        "Combinación": "Proteína vegetal + grasa saludable",
        "Estado": "✓ RECOMENDADO",
        "Fundamento Científico": "Sinergia de aminoácidos vegetales (complementación proteica) con ácidos grasos esenciales. El perfil lipídico vegetal (omega-6/omega-3 equilibrado) potencia el efecto antiinflamatorio de legumbres y tofu."
    },
    {
        "Combinación": "Vegetales + grasa cruda (AOVE, aguacate)",
        "Estado": "✓ RECOMENDADO",
        "Fundamento Científico": "Los carotenoides (betacaroteno, licopeno) y vitaminas liposolubles requieren lípidos para su absorción intestinal. El AOVE aporta además polifenoles (hidroxitirosol, oleuropeína) con efecto sinérgico antioxidante."
    },
    {
        "Combinación": "Omega-3 (salmón, chía, nueces) en cualquier comida",
        "Estado": "✓ RECOMENDADO",
        "Fundamento Científico": "EPA y DHA (omega-3 de cadena larga) reducen la síntesis de eicosanoides proinflamatorios (PGE2, LTB4) y modulan la expresión génica vía PPARα. ALA vegetal (chía) requiere conversión, menos eficiente pero valiosa."
    },
    {
        "Combinación": "Fermento probiótico 20-30 min ANTES del desayuno",
        "Estado": "✓ RECOMENDADO",
        "Fundamento Científico": "La toma en ayunas permite colonización bacteriana óptima sin interferencia del pH ácido gástrico necesario para digestión proteica. Mejora biodiversidad de microbiota y producción de SCFA (ácidos grasos de cadena corta)."
    },
    {
        "Combinación": "Carne roja + tubérculo/almidón",
        "Estado": "✗ EVITAR",
        "Fundamento Científico": "Competencia enzimática: la pepsina (pH 1.5-2) necesaria para proteínas animales es inhibida por el medio alcalino que requiere la amilasa para almidones. Resultado: digestión incompleta, fermentación intestinal, producción de gases (metano, hidrógeno)."
    },
    {
        "Combinación": "Dos o más almidones complejos en una misma comida",
        "Estado": "✗ EVITAR",
        "Fundamento Científico": "Carga glucémica excesiva que genera picos de insulina pronunciados y posterior hipoglucemia reactiva. Sobrecarga enzimática (amilasa) que prolonga el tiempo de tránsito y favorece fermentación por bacterias colónicas."
    },
    {
        "Combinación": "Fruta + proteína/almidón en comida principal",
        "Estado": "✗ EVITAR",
        "Fundamento Científico": "Los azúcares simples de la fruta (fructosa, glucosa) se digieren en 20-40 minutos, mientras que proteínas y almidones requieren 3-5 horas. La fruta queda 'atrapada' en el estómago, fermentando y produciendo alcohol y ácidos orgánicos que generan distensión."
    },
    {
        "Combinación": "Fruta + grasa saludable como snack",
        "Estado": "✓ PERMITIDO",
        "Fundamento Científico": "La grasa ralentiza la absorción de azúcares, atenuando el pico glucémico. Mejora la biodisponibilidad de antioxidantes liposolubles presentes en frutas (carotenoides). Ideal como snack intermedio."
    },
    {
        "Combinación": "Fermento DURANTE comida principal",
        "Estado": "✗ EVITAR",
        "Fundamento Científico": "Las bacterias probióticas son sensibles al pH ácido del estómago durante la digestión activa. Su viabilidad disminuye significativamente. Además, pueden interferir con la producción de HCl necesaria para proteínas."
    },
    {
        "Combinación": "Agua durante las comidas",
        "Estado": "✗ EVITAR",
        "Fundamento Científico": "Diluye las enzimas digestivas (pepsina, amilasa, lipasa) y el ácido clorhídrico, comprometiendo la eficiencia digestiva. Protocolo: 500ml 30 minutos ANTES, evitar durante, reanudar 60 minutos DESPUÉS."
    },
    {
        "Combinación": "Ultraprocesados, azúcares refinados, edulcorantes artificiales",
        "Estado": "✗ ELIMINAR",
        "Fundamento Científico": "Alteran la microbiota intestinal (disbiosis), generan resistencia a la insulina, aumentan permeabilidad intestinal (leaky gut) y activan vías inflamatorias sistémicas (TLR4, NF-κB). Sin valor nutricional, alto impacto metabólico negativo."
    },
    {
        "Combinación": "Aceite de oliva virgen extra (AOVE) EN CRUDO",
        "Estado": "✓ OBLIGATORIO",
        "Fundamento Científico": "Los polifenoles del AOVE (oleocantal, oleuropeína) se degradan con el calor >180°C. En crudo, actúan como antiinflamatorios naturales comparables a ibuprofeno, mejoran perfil lipídico (↑HDL, ↓LDL oxidado) y protegen contra oxidación celular."
    },
    {
        "Combinación": "Especias antiinflamatorias (cúrcuma, jengibre)",
        "Estado": "✓ RECOMENDADO",
        "Fundamento Científico": "La curcumina (cúrcuma) inhibe COX-2 y NF-κB, reduciendo mediadores proinflamatorios. El gingerol (jengibre) mejora motilidad gástrica y tiene efecto antináusea. Combinar con pimienta negra (piperina) aumenta biodisponibilidad de curcumina en 2000%."
    },
    {
        "Combinación": "Proteína en cada comida principal (desayuno, almuerzo, cena)",
        "Estado": "✓ OBLIGATORIO",
        "Fundamento Científico": "Mantiene síntesis proteica muscular (MPS) constante, maximiza efecto térmico de los alimentos (20-30% de calorías para metabolizar proteína), mejora saciedad vía leptina y péptidos intestinales, preserva masa muscular en déficit calórico."
    },
    {
        "Combinación": "Vegetales de hoja verde en almuerzo y cena",
        "Estado": "✓ OBLIGATORIO",
        "Fundamento Científico": "Aportan fibra soluble e insoluble (prebiótica), micronutrientes (folato, vitamina K, magnesio), clorofila con efecto alcalinizante y fitoquímicos (sulforafano en crucíferas) que activan vías de detoxificación hepática (fase II)."
    }
]


def generar_tabla_compatibilidades():
    """
    Genera la tabla de compatibilidades como DataFrame
    
    Returns:
        DataFrame con las reglas de compatibilidad alimentaria
    """
    df = pd.DataFrame(TABLA_COMPATIBILIDADES)
    return df


def exportar_compatibilidades_excel(writer, sheet_name="Compatibilidades"):
    """
    Exporta la tabla de compatibilidades a un archivo Excel
    
    Args:
        writer: ExcelWriter object
        sheet_name: Nombre de la hoja
    """
    df = generar_tabla_compatibilidades()
    df.to_excel(writer, sheet_name=sheet_name, index=False)
    
    # Formato
    ws = writer.sheets[sheet_name]
    ws.set_column(0, 0, 50)  # Combinación
    ws.set_column(1, 1, 18)  # Estado
    ws.set_column(2, 2, 80)  # Fundamento
    
    # Formato wrap text
    wrap = writer.book.add_format({'text_wrap': True, 'valign': 'top'})
    for col in range(3):
        ws.set_column(col, col, ws.col_sizes.get(col, 15), wrap)
