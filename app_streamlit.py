# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
from io import BytesIO
from modelo_optimizacion import generar_menu_optimizado
from generador_parrafos import generar_parrafo_personalizado
from tabla_compatibilidades import generar_tabla_compatibilidades

st.set_page_config(
    page_title="SYNFOOD",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS Estilo Canva con formas decorativas
st.markdown("""
    <style>
    /* Fondo blanco */
    .stApp {
        background: #ffffff !important;
    }
    .main {
        background: #ffffff !important;
    }
    [data-testid="stAppViewContainer"] {
        background: #ffffff !important;
    }
    
    /* Ocultar elementos Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Botones principales */
    .stButton>button {
        background: linear-gradient(135deg, #5dced6 0%, #4dbbc4 100%);
        color: white;
        font-size: 16px;
        padding: 18px 50px;
        border-radius: 50px;
        border: none;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(93, 206, 214, 0.3);
        transition: all 0.3s ease;
        width: 100%;
        margin: 10px 0;
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, #4dbbc4 0%, #3da9b2 100%);
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(93, 206, 214, 0.4);
    }
    
    /* Títulos */
    h1 {
        color: #1e555c;
        font-weight: 800;
        font-size: 2.8em;
        margin-bottom: 15px;
    }
    
    h2 {
        color: #2d3e4f;
        text-align: center;
        font-weight: 700;
        font-size: 2.2em;
        margin-top: 30px;
        margin-bottom: 10px;
    }
    
    h3 {
        color: #6b7280;
        text-align: center;
        font-size: 1.1em;
        font-weight: 400;
        margin-bottom: 40px;
        line-height: 1.6;
    }
    
    /* Contenedor con fondo de color */
    .question-box {
        background: linear-gradient(135deg, #e8f4f8 0%, #d4ebf2 100%);
        padding: 60px 40px;
        border-radius: 30px;
        margin: 40px auto;
        max-width: 900px;
        box-shadow: 0 10px 40px rgba(93, 206, 214, 0.15);
    }
    
    /* Logo */
    .logo-container {
        padding: 30px;
        text-align: left;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: transparent;
        justify-content: center;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #e8f4f5;
        border-radius: 20px 20px 0 0;
        padding: 15px 30px;
        font-weight: 600;
        color: #2d7a82;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #5dced6 0%, #4dbbc4 100%);
        color: white;
    }
    
    /* DataFrames */
    .stDataFrame {
        border: 2px solid #e0f2f4;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
    }
    
    /* Text Area */
    .stTextArea textarea {
        border: 2px solid #e0f2f4;
        border-radius: 15px;
        background-color: #fafbfc;
        line-height: 1.8;
    }
    
    /* Espaciado */
    div[data-testid="stVerticalBlock"] > div {
        padding: 5px 0;
    }
    
    /* Formas abstractas decorativas */
    .blob-orange {
        position: fixed;
        bottom: -100px;
        right: -100px;
        width: 500px;
        height: 500px;
        background: linear-gradient(135deg, #f4a261 0%, #e76f51 100%);
        border-radius: 45% 55% 60% 40% / 55% 45% 55% 45%;
        opacity: 0.3;
        z-index: 0;
        pointer-events: none;
        animation: float 6s ease-in-out infinite;
    }
    
    .blob-blue {
        position: fixed;
        top: -50px;
        left: -50px;
        width: 400px;
        height: 400px;
        background: linear-gradient(135deg, #5dced6 0%, #4dbbc4 100%);
        border-radius: 60% 40% 50% 50% / 45% 55% 45% 55%;
        opacity: 0.2;
        z-index: 0;
        pointer-events: none;
        animation: float 8s ease-in-out infinite;
    }
    
    .blob-green {
        position: fixed;
        top: 200px;
        right: -80px;
        width: 350px;
        height: 350px;
        background: linear-gradient(135deg, #a8dadc 0%, #90c9cb 100%);
        border-radius: 50% 50% 40% 60% / 55% 45% 55% 45%;
        opacity: 0.25;
        z-index: 0;
        pointer-events: none;
        animation: float 7s ease-in-out infinite;
    }
    
    .blob-pink {
        position: fixed;
        bottom: 150px;
        left: -100px;
        width: 450px;
        height: 450px;
        background: linear-gradient(135deg, #fec5bb 0%, #fcd5ce 100%);
        border-radius: 55% 45% 50% 50% / 45% 55% 45% 55%;
        opacity: 0.2;
        z-index: 0;
        pointer-events: none;
        animation: float 9s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% {
            transform: translateY(0) rotate(0deg);
        }
        50% {
            transform: translateY(-20px) rotate(5deg);
        }
    }
    </style>
    """, unsafe_allow_html=True)

# Sistema de navegación
if 'pagina' not in st.session_state:
    st.session_state.pagina = 'inicio'
if 'edad' not in st.session_state:
    st.session_state.edad = None
if 'objetivo' not in st.session_state:
    st.session_state.objetivo = None
if 'actividad' not in st.session_state:
    st.session_state.actividad = None
if 'sexo' not in st.session_state:
    st.session_state.sexo = None

def ir_a_pagina(nombre_pagina):
    st.session_state.pagina = nombre_pagina
    st.rerun()

# PÁGINA DE INICIO
if st.session_state.pagina == 'inicio':
    st.markdown("<div class='blob-blue'></div>", unsafe_allow_html=True)
    st.markdown("<div class='blob-green'></div>", unsafe_allow_html=True)
    
    # Logo centrado
    col_logo1, col_logo2, col_logo3 = st.columns([1, 1, 1])
    with col_logo2:
        st.image("assets/logo.png", width=400)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Contenido con imagen de vegetales
    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.markdown("<h2 style='font-size: 2.5em; margin-top: 0; text-align: left;'>Bienvenido(a)<br>a Synfood</h2>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: left;'>Descubre el poder de los alimentos trabajando en sinergia con tu cuerpo</h3>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: left;'>Diseñamos menús personalizados que se adaptan a ti, basados en ciencia y bienestar</h3>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("COMENZAR MI PLAN →"):
            ir_a_pagina('edad')
    
    with col2:
        st.image("assets/vegetables.jpg", use_container_width=True)

# PÁGINA 1: EDAD
elif st.session_state.pagina == 'edad':
    st.markdown("<div class='blob-blue'></div>", unsafe_allow_html=True)
    st.markdown("<div class='blob-orange'></div>", unsafe_allow_html=True)
    
    st.markdown("<div class='logo-container'>", unsafe_allow_html=True)
    st.image("assets/logo.png", width=300)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='question-box'>", unsafe_allow_html=True)
    st.markdown("<h2>¿Cuál es tu edad?</h2>", unsafe_allow_html=True)
    st.markdown("<h3>Esto nos ayuda a entender mejor tus necesidades nutricionales</h3>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("18 - 24 años", use_container_width=True):
            st.session_state.edad = "18-25"
            ir_a_pagina('sexo')
        if st.button("25 - 34 años", use_container_width=True):
            st.session_state.edad = "26-35"
            ir_a_pagina('sexo')
        if st.button("35 - 44 años", use_container_width=True):
            st.session_state.edad = "36-45"
            ir_a_pagina('sexo')
        if st.button("45 - 54 años", use_container_width=True):
            st.session_state.edad = "46-55"
            ir_a_pagina('sexo')
        if st.button("55 - 64 años", use_container_width=True):
            st.session_state.edad = "56-65"
            ir_a_pagina('sexo')
        if st.button("65 o más", use_container_width=True):
            st.session_state.edad = "66+"
            ir_a_pagina('sexo')

# PÁGINA 2: SEXO
elif st.session_state.pagina == 'sexo':
    st.markdown("<div class='blob-green'></div>", unsafe_allow_html=True)
    st.markdown("<div class='blob-pink'></div>", unsafe_allow_html=True)
    
    st.markdown("<div class='logo-container'>", unsafe_allow_html=True)
    st.image("assets/logo.png", width=300)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='question-box' style='background: linear-gradient(135deg, #d4f1f4 0%, #b8e5e9 100%);'>", unsafe_allow_html=True)
    st.markdown("<h2>Selecciona tu sexo</h2>", unsafe_allow_html=True)
    st.markdown("<h3>Así podremos continuar creando tu perfil de bienestar</h3>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Femenino", use_container_width=True):
            st.session_state.sexo = "Femenino"
            ir_a_pagina('actividad')
        if st.button("Masculino", use_container_width=True):
            st.session_state.sexo = "Masculino"
            ir_a_pagina('actividad')

# PÁGINA 3: ACTIVIDAD
elif st.session_state.pagina == 'actividad':
    st.markdown("<div class='blob-orange'></div>", unsafe_allow_html=True)
    st.markdown("<div class='blob-blue'></div>", unsafe_allow_html=True)
    
    st.markdown("<div class='logo-container'>", unsafe_allow_html=True)
    st.image("assets/logo.png", width=300)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='question-box' style='background: linear-gradient(135deg, #fef3e8 0%, #fde7d0 100%);'>", unsafe_allow_html=True)
    st.markdown("<h2>¿Qué tan activo eres en tu día a día?</h2>", unsafe_allow_html=True)
    st.markdown("<h3>Cuéntanos un poco sobre tu rutina para personalizar tu plan</h3>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Sedentario - Paso la mayor parte del día sentado", use_container_width=True):
            st.session_state.actividad = "Nula"
            ir_a_pagina('objetivo')
        if st.button("Activo moderado - Hago ejercicio 3-4 veces por semana", use_container_width=True):
            st.session_state.actividad = "Moderada"
            ir_a_pagina('objetivo')
        if st.button("Muy activo - Entreno intensamente o tengo un trabajo físico", use_container_width=True):
            st.session_state.actividad = "Alta"
            ir_a_pagina('objetivo')

# PÁGINA 4: OBJETIVO
elif st.session_state.pagina == 'objetivo':
    st.markdown("<div class='blob-blue'></div>", unsafe_allow_html=True)
    st.markdown("<div class='blob-green'></div>", unsafe_allow_html=True)
    
    st.markdown("<div class='logo-container'>", unsafe_allow_html=True)
    st.image("assets/logo.png", width=300)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='question-box' style='background: linear-gradient(135deg, #e8f4f8 0%, #d4ebf2 100%);'>", unsafe_allow_html=True)
    st.markdown("<h2>¿Cuál es tu objetivo principal?</h2>", unsafe_allow_html=True)
    st.markdown("<h3>Cuéntanos qué te gustaría lograr con tu alimentación</h3>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Tratar la obesidad", use_container_width=True):
            st.session_state.objetivo = "Obesidad"
            ir_a_pagina('generando')
        if st.button("Tratar la inflamación", use_container_width=True):
            st.session_state.objetivo = "Inflamacion"
            ir_a_pagina('generando')
        if st.button("Mejorar hábitos alimenticios", use_container_width=True):
            st.session_state.objetivo = "Mejorar_habitos"
            ir_a_pagina('generando')

# PÁGINA DE GENERACIÓN
elif st.session_state.pagina == 'generando':
    st.markdown("<div class='blob-blue'></div>", unsafe_allow_html=True)
    st.markdown("<div class='blob-orange'></div>", unsafe_allow_html=True)
    
    st.markdown("<div class='logo-container'>", unsafe_allow_html=True)
    st.image("assets/logo.png", width=300)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<h2>Generando tu plan personalizado...</h2>", unsafe_allow_html=True)
    
    with st.spinner("Creando tu menú optimizado..."):
        menu_df, mensaje = generar_menu_optimizado(
            st.session_state.edad,
            st.session_state.sexo,
            st.session_state.actividad,
            st.session_state.objetivo
        )
        st.session_state.menu_generado = menu_df
        st.session_state.mensaje = mensaje
        ir_a_pagina('resultado')

# PÁGINA DE RESULTADOS
elif st.session_state.pagina == 'resultado':
    st.markdown("<div class='logo-container'>", unsafe_allow_html=True)
    st.image("assets/logo.png", width=300)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div style='text-align: center; margin: 40px 0;'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: #1e555c; font-size: 2.5em;'>Tu plan semanal está listo</h2>", unsafe_allow_html=True)
    st.markdown("<h3>Descubre el menú creado especialmente para ti</h3>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    menu_df = st.session_state.menu_generado
    
    tab1, tab2, tab3, tab4 = st.tabs(["Menú Semanal", "Recomendaciones", "Compatibilidades", "Descargar"])
    
    with tab1:
        st.dataframe(menu_df, use_container_width=True, height=500)
    
    with tab2:
        parrafo = generar_parrafo_personalizado(
            st.session_state.edad,
            st.session_state.sexo,
            st.session_state.actividad,
            st.session_state.objetivo
        )
        st.text_area("", parrafo, height=600)
    
    with tab3:
        tabla_comp = generar_tabla_compatibilidades()
        st.dataframe(tabla_comp, use_container_width=True, height=600)
    
    with tab4:
        st.markdown("## Descarga tu Plan Personalizado")
        st.markdown("<br>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 1, 1])
        
        # EXCEL
        with col1:
            st.markdown("### Formato Excel")
            st.markdown("Incluye menú, recomendaciones y compatibilidades en pestañas separadas")
            output_excel = BytesIO()
            with pd.ExcelWriter(output_excel, engine='xlsxwriter') as writer:
                menu_df.to_excel(writer, sheet_name='Menu_Semanal')
                parrafo = generar_parrafo_personalizado(
                    st.session_state.edad,
                    st.session_state.sexo,
                    st.session_state.actividad,
                    st.session_state.objetivo
                )
                pd.DataFrame({'Recomendaciones': [parrafo]}).to_excel(writer, sheet_name='Recomendaciones', index=False)
                tabla_comp = generar_tabla_compatibilidades()
                tabla_comp.to_excel(writer, sheet_name='Compatibilidades', index=False)
            output_excel.seek(0)
            st.download_button(
                "⬇️ Descargar Excel",
                output_excel,
                file_name=f"SYNFOOD_Plan_{st.session_state.edad}_{st.session_state.objetivo}.xlsx",
                mime="application/vnd.ms-excel",
                use_container_width=True
            )
        
        # PDF
        with col2:
            st.markdown("### Formato PDF")
            st.markdown("Plan completo en documento profesional listo para imprimir")
            if st.button("⬇️ Descargar PDF", use_container_width=True):
                from reportlab.lib.pagesizes import letter, landscape
                from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
                from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
                from reportlab.lib import colors
                from reportlab.lib.units import inch
                
                output_pdf = BytesIO()
                doc = SimpleDocTemplate(output_pdf, pagesize=landscape(letter))
                story = []
                styles = getSampleStyleSheet()
                
                title_style = ParagraphStyle(
                    'CustomTitle',
                    parent=styles['Heading1'],
                    fontSize=24,
                    textColor=colors.HexColor('#1e555c'),
                    spaceAfter=20,
                    alignment=1
                )
                story.append(Paragraph("🥗 SYNFOOD - Tu Plan Personalizado", title_style))
                story.append(Spacer(1, 0.2*inch))
                
                subtitle_style = ParagraphStyle(
                    'Subtitle',
                    parent=styles['Heading2'],
                    fontSize=16,
                    textColor=colors.HexColor('#2d7a82'),
                    spaceAfter=15
                )
                story.append(Paragraph("MENÚ SEMANAL", subtitle_style))
                story.append(Spacer(1, 0.1*inch))
                
                cell_style = ParagraphStyle(
                    'CellStyle',
                    fontSize=7,
                    leading=9,
                    wordWrap='CJK',
                    alignment=0
                )
                
                header_style = ParagraphStyle(
                    'HeaderStyle',
                    fontSize=8,
                    leading=10,
                    textColor=colors.whitesmoke,
                    fontName='Helvetica-Bold',
                    alignment=1
                )
                
                headers = [Paragraph('<b>Momento</b>', header_style)]
                for col in menu_df.columns:
                    headers.append(Paragraph(f'<b>{col}</b>', header_style))
                
                data = [headers]
                
                for idx in menu_df.index:
                    row = [Paragraph(f'<b>{idx}</b>', cell_style)]
                    for val in menu_df.loc[idx]:
                        row.append(Paragraph(str(val), cell_style))
                    data.append(row)
                
                page_width = landscape(letter)[0] - 1.5*inch
                num_cols = len(data[0])
                col_width = page_width / num_cols
                col_widths = [col_width] * num_cols
                
                row_heights = [0.35*inch] + [1.0*inch] * (len(data) - 1)
                
                t = Table(data, colWidths=col_widths, rowHeights=row_heights)
                t.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#5dced6')),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                    ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
                    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('LEFTPADDING', (0, 0), (-1, -1), 5),
                    ('RIGHTPADDING', (0, 0), (-1, -1), 5),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
                    ('TOPPADDING', (0, 0), (-1, -1), 8),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f0f9fa')),
                    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#5dced6'))
                ]))
                story.append(t)
                story.append(PageBreak())
                
                story.append(Paragraph("RECOMENDACIONES PERSONALIZADAS", subtitle_style))
                story.append(Spacer(1, 0.15*inch))
                
                parrafo = generar_parrafo_personalizado(
                    st.session_state.edad,
                    st.session_state.sexo,
                    st.session_state.actividad,
                    st.session_state.objetivo
                )
                
                body_style = ParagraphStyle(
                    'CustomBody',
                    parent=styles['BodyText'],
                    fontSize=9,
                    leading=12,
                    spaceAfter=8
                )
                
                for line in parrafo.split('\n'):
                    if line.strip():
                        story.append(Paragraph(line.strip(), body_style))
                
                # Nueva página para compatibilidades
                story.append(PageBreak())
                story.append(Paragraph("TABLA DE COMPATIBILIDADES", subtitle_style))
                story.append(Spacer(1, 0.15*inch))
                
                # Obtener tabla de compatibilidades
                tabla_comp = generar_tabla_compatibilidades()
                
                # Crear encabezados
                comp_headers = [Paragraph('<b>Alimento</b>', header_style)]
                for col in tabla_comp.columns:
                    comp_headers.append(Paragraph(f'<b>{col}</b>', header_style))
                
                comp_data = [comp_headers]
                
                # Crear filas
                for idx in tabla_comp.index:
                    row = [Paragraph(f'<b>{idx}</b>', cell_style)]
                    for val in tabla_comp.loc[idx]:
                        row.append(Paragraph(str(val), cell_style))
                    comp_data.append(row)
                
                # Crear tabla de compatibilidades
                comp_table = Table(comp_data)
                comp_table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#5dced6')),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, -1), 7),
                    ('LEFTPADDING', (0, 0), (-1, -1), 4),
                    ('RIGHTPADDING', (0, 0), (-1, -1), 4),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                    ('TOPPADDING', (0, 0), (-1, -1), 6),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f0f9fa')),
                    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#5dced6'))
                ]))
                story.append(comp_table)
                doc.build(story)
                output_pdf.seek(0)
                
                st.download_button(
                    "Confirmar Descarga PDF",
                    output_pdf,
                    file_name=f"SYNFOOD_Plan_{st.session_state.edad}_{st.session_state.objetivo}.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("← Volver al inicio", use_container_width=True):
            ir_a_pagina('inicio')