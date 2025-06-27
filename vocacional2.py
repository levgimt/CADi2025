import streamlit as st

# --- Preguntas y opciones ---
preguntas = [
    ("¿Qué área de la automatización te gusta?", ["Quiero varo", "Me gustan los PLC's", "Ciberseguridad", "Cosas que exploten"]),
    ("¿Qué asignatura prefieres?", ["Lógica", "Cinemática", "Tecnología", "Hackeo"]),
    ("¿Cómo te gusta trabajar?", ["Analizando datos", "Mover cosas", "Con herramientas", "Estar en el sotano"]),
    ("¿Qué hobby te interesa más?", ["Resolver acertijos", "Automatizar", "Armar circuitos", "Molestar a personas"]),
    ("¿Qué valoras más en un trabajo?", ["Diagramas", "Líneas de Producción", "Precisión", "Impacto Ciberseguridad"]),
    ("¿Con qué palabra te identificas más?", ["Matemáticas", "Gemelos Digitales", "Práctico", "Cobrar por Todo"])
]

# --- Mapeo a perfiles ---
perfil_map = {
    "Diagramas": "PLCero",
    "Matemáticas": "PLCero",
    "Analizando datos": "PLCero",
    "Lógica": "PLCero",
    "Resolver Acertijos": "PLCero",
    "Lógico": "PLCero",
    "Cinemática": "Robótico",
    "Mover cosas": "Robótico",
    "Animaciones": "Robótico",
    "Gemelos Digitales": "Robótico",
    "Automatizar": "Robótico",
    "Lineas de Producción": "Robótico",
    "Reparar cosas": "técnico",
    "Tecnología": "técnico",
    "Con herramientas": "técnico",
    "Armar circuitos": "técnico",
    "Precisión": "técnico",
    "Práctico": "técnico",
    "Molestar a personas": "Ciberseguridad",
    "Computadoras": "Ciberseguridad",
    "Hackeo": "Ciberseguridad",
    "Cobrar por todo": "Ciberseguridad",
    "Impacto en TI": "Ciberseguridad",
    "Estar en el sotano": "Ciberseguridad"
}

# --- Recomendaciones ---
recomendaciones = {
    "PLCero": "🔬 Perfil PLCero: Podrías destacar en áreas como Educación, Eléctrica, Descompostura.",
    "Robótico": "🎨 Perfil Robótico: Podrías sobresalir en Cinemática, Mecánica, Control, Visión.",
    "Técnico": "🔧 Perfil Técnico: Mantenimiento, Instalador, Seguridad Industrial.",
    "Ciberseguridad": "👥 Perfil Ciberseguridad: Redes, IT, Bases de Datos."
}

# --- Estado inicial seguro ---
if "respuestas" not in st.session_state:
    st.session_state.respuestas = []

if "finalizado" not in st.session_state:
    st.session_state.finalizado = False

# --- Configuración de la página ---
st.set_page_config(page_title="Test Vocacional", page_icon="🧭", layout="centered")

# --- Sidebar con información ---
with st.sidebar:
    st.header("ℹ️ Acerca de este test")
    st.markdown("""
    Este test vocacional te ayudará a identificar tu perfil profesional predominante entre:
    - **PLCero** 🔬
    - **Robótica** 🎨
    - **Técnico** 🔧
    - **Ciberseguridad** 👥
    """)
    st.divider()
    st.caption("Responde honestamente a todas las preguntas para obtener un resultado preciso.")

# --- Título y progreso ---
st.title("🧭 Test De Automatización Interactivo")
st.markdown("Considera que este cuestionario es solo de ayuda. No olvides consultar a Guillermo Sandoval")

# Barra de progreso mejorada
progreso = len(st.session_state.respuestas)
col1, col2 = st.columns([1, 4])
with col1:
    st.metric("Progreso", f"{progreso}/{len(preguntas)}")
with col2:
    st.progress(progreso / len(preguntas))

# --- Lógica principal ---
if not st.session_state.finalizado:
    if progreso < len(preguntas):
        pregunta, opciones = preguntas[progreso]
        
        # Contenedor para la pregunta actual
        with st.container(border=True):
            st.markdown(f"#### Pregunta {progreso + 1}: {pregunta}")
            
            # Usamos selectbox en lugar de radio para ahorrar espacio
            seleccion = st.selectbox(
                "Selecciona la opción que mejor te describa:",
                opciones,
                key=f"preg_{progreso}",
                label_visibility="collapsed"
            )
            
            # Botones de navegación en columnas
            col_btn1, col_btn2 = st.columns(2)
            with col_btn1:
                if st.button("⏪ Anterior", disabled=(progreso == 0)):
                    st.session_state.respuestas.pop()
            with col_btn2:
                if st.button("⏩ Siguiente"):
                    st.session_state.respuestas.append(seleccion)

    if len(st.session_state.respuestas) == len(preguntas):
        st.session_state.finalizado = True
        st.rerun()

# --- Mostrar resultado ---
if st.session_state.finalizado:
    # Cálculo del perfil
    conteo = {"PLCero": 0, "Robótico": 0, "técnico": 0, "Ciberseguridad": 0}
    for r in st.session_state.respuestas:
        perfil = perfil_map.get(r)
        if perfil:
            conteo[perfil] += 1
    perfil_final = max(conteo, key=conteo.get)
    
    # Resultado principal
    st.success("🎉 ¡Test completado con éxito!")
    
    # Tarjeta de resultado
    with st.container(border=True):
        st.markdown(f"### 🔎 Tu perfil vocacional dominante es: **{perfil_final.upper()}**")
        st.info(recomendaciones[perfil_final])
        
        # Gráfico de resultados
        st.subheader("📊 Distribución de tu perfil:")
        st.bar_chart(conteo)

    # Acordeón con respuestas detalladas
    with st.expander("📋 Ver mis respuestas detalladas"):
        for i, r in enumerate(st.session_state.respuestas):
            st.markdown(f"**{i+1}. {preguntas[i][0]}**")
            st.markdown(f"→ *{r}*")
            st.divider()

    # Botón de reinicio centrado
    st.divider()
    col_centro = st.columns([1, 2, 1])[1]
    with col_centro:
        if st.button("🔄 Realizar el test nuevamente", type="primary"):
            st.session_state.respuestas = []
            st.session_state.finalizado = False
            st.rerun()
