import streamlit as st
import pandas as pd
import os

# 📌 Nueva ruta dentro del contenedor en Render
EXCEL_FILE = "resultados_entrenadores.xlsx"


# 📌 Función para cargar datos desde el Excel en OneDrive
def cargar_datos():
    if os.path.exists(EXCEL_FILE):
        return pd.read_excel(EXCEL_FILE, engine="openpyxl")
    else:
        columnas = ["Fecha de Registro", "Nombre Entrenador", "Liga", "Documento de Identidad",
                    "Evento", "Fecha", "Lugar", "Prueba", "Tipo de Función",
                    "Oro", "Plata", "Bronce", "Posición 4-8", "Nombre Deportistas"]
        df = pd.DataFrame(columns=columnas)
        df.to_excel(EXCEL_FILE, index=False, engine="openpyxl")
        return df

# 📌 Función para guardar datos en Excel
def guardar_datos(nuevos_datos):
    df = cargar_datos()
    df = pd.concat([df, pd.DataFrame([nuevos_datos])], ignore_index=True)
    df.to_excel(EXCEL_FILE, index=False, engine="openpyxl")

# 📌 Diseño de la aplicación Streamlit
st.set_page_config(page_title="Encuesta Indeportes", page_icon="🏅", layout="wide")

# 📌 Mostrar el Logo
logo_path = "style/logo_indeportes_2025.jpg"
if os.path.exists(logo_path):
    st.image(logo_path, width=250)
else:
    st.warning(f"⚠ No se encontró el logo en {logo_path}")

st.title("🏆 Encuesta de Resultados - Indeportes Antioquia")
st.write("Registra los eventos deportivos y resultados de los entrenadores.")

# 📌 BLOQUE 1: INFORMACIÓN PERSONAL
with st.expander("📌 **Bloque 1: Información Personal**"):
    col1, col2 = st.columns(2)
    with col1:
        nombre_entrenador = st.text_input("Nombre Completo", key="nombre_entrenador")
        documento = st.text_input("Documento de Identidad", key="documento_entrenador")
    with col2:
        liga = st.text_input("Liga", key="liga_entrenador")

# 📌 BLOQUE 2: EVENTOS NACIONALES
with st.expander("📌 **Bloque 2: Eventos Nacionales**"):
    tipo_evento_nac = st.selectbox("Evento Nacional", [
        "Juegos Nacionales",
        "Campeonato Nacional"
    ], key="evento_nacional")

    col1, col2 = st.columns(2)
    with col1:
        fecha_nac = st.date_input("Fecha del Evento", key="fecha_nacional")
        lugar_nac = st.text_input("Lugar del Evento", key="lugar_nacional")
    with col2:
        prueba_nac = st.text_input("Prueba en la que participó", key="prueba_nacional")
        tipo_funcion_nac = st.radio("Tipo de Función", ["Principal", "Asistente"], key="funcion_nacional")

    st.subheader("📌 Resultados")
    col1, col2 = st.columns(2)
    with col1:
        oro_nac = st.number_input("Medallas de Oro", min_value=0, step=1, key="oro_nacional")
        plata_nac = st.number_input("Medallas de Plata", min_value=0, step=1, key="plata_nacional")
    with col2:
        bronce_nac = st.number_input("Medallas de Bronce", min_value=0, step=1, key="bronce_nacional")
        posicion_nac = st.number_input("Posiciones 4-8", min_value=0, step=1, key="posicion_nacional")

    atletas_nac = st.text_area("Nombre de los deportistas", key="deportistas_nacional")

    if st.button("Guardar Evento Nacional"):
        guardar_datos({
            "Fecha de Registro": pd.Timestamp.now(),
            "Nombre Entrenador": nombre_entrenador,
            "Liga": liga,
            "Documento de Identidad": documento,
            "Evento": tipo_evento_nac,
            "Fecha": fecha_nac,
            "Lugar": lugar_nac,
            "Prueba": prueba_nac,
            "Tipo de Función": tipo_funcion_nac,
            "Oro": oro_nac,
            "Plata": plata_nac,
            "Bronce": bronce_nac,
            "Posición 4-8": posicion_nac,
            "Nombre Deportistas": atletas_nac
        })
        st.success("✅ Registro guardado correctamente")

# 📌 BLOQUE 3: EVENTOS INTERNACIONALES - CICLO OLÍMPICO
with st.expander("📌 **Bloque 3: Eventos Internacionales - Ciclo Olímpico**"):
    tipo_evento_ciclo = st.selectbox("Evento Internacional", [
        "Juegos Suramericanos",
        "Juegos Panamericanos",
        "Juegos Olímpicos"
    ], key="evento_ciclo")

    col1, col2 = st.columns(2)
    with col1:
        fecha_ciclo = st.date_input("Fecha del Evento", key="fecha_ciclo")
        lugar_ciclo = st.text_input("Lugar del Evento", key="lugar_ciclo")
    with col2:
        prueba_ciclo = st.text_input("Prueba en la que participó", key="prueba_ciclo")
        tipo_funcion_ciclo = st.radio("Tipo de Función", ["Principal", "Asistente"], key="funcion_ciclo")

    st.subheader("📌 Resultados")
    oro_ciclo = st.number_input("Medallas de Oro", min_value=0, step=1, key="oro_ciclo")
    plata_ciclo = st.number_input("Medallas de Plata", min_value=0, step=1, key="plata_ciclo")
    bronce_ciclo = st.number_input("Medallas de Bronce", min_value=0, step=1, key="bronce_ciclo")
    posicion_ciclo = st.number_input("Posiciones 4-8", min_value=0, step=1, key="posicion_ciclo")

    atletas_ciclo = st.text_area("Nombre de los deportistas", key="deportistas_ciclo")

    if st.button("Guardar Evento Internacional"):
        guardar_datos({
            "Fecha de Registro": pd.Timestamp.now(),
            "Nombre Entrenador": nombre_entrenador,
            "Liga": liga,
            "Documento de Identidad": documento,
            "Evento": tipo_evento_ciclo,
            "Fecha": fecha_ciclo,
            "Lugar": lugar_ciclo,
            "Prueba": prueba_ciclo,
            "Tipo de Función": tipo_funcion_ciclo,
            "Oro": oro_ciclo,
            "Plata": plata_ciclo,
            "Bronce": bronce_ciclo,
            "Posición 4-8": posicion_ciclo,
            "Nombre atletas": atletas_ciclo
        })


# 📌 BLOQUE 4: EVENTOS INTERNACIONALES - CAMPEONATOS
with st.expander("📌 **Bloque 4: Eventos Internacionales - Campeonatos**"):
    tipo_campeonato = st.selectbox("Campeonato Internacional", [
        "Campeonato Suramericano",
        "Campeonato Centroamericano",
        "Campeonato Panamericano",
        "Campeonato Mundial"
    ], key="evento_campeonato")

    col1, col2 = st.columns(2)
    with col1:
        fecha_camp = st.date_input("Fecha del Evento", key="fecha_campeonato")
        lugar_camp = st.text_input("Lugar del Evento", key="lugar_campeonato")
    with col2:
        prueba_camp = st.text_input("Prueba en la que participó", key="prueba_campeonato")
        tipo_funcion_camp = st.radio("Tipo de Función", ["Principal", "Asistente"], key="funcion_campeonato")

    st.subheader("📌 Resultados")
    col1, col2 = st.columns(2)
    with col1:
        oro_camp = st.number_input("Medallas de Oro", min_value=0, step=1, key="oro_campeonato")
        plata_camp = st.number_input("Medallas de Plata", min_value=0, step=1, key="plata_campeonato")
    with col2:
        bronce_camp = st.number_input("Medallas de Bronce", min_value=0, step=1, key="bronce_campeonato")
        posicion_camp = st.number_input("Posiciones 4-8", min_value=0, step=1, key="posicion_campeonato")

    atletas_camp = st.text_area("Nombre de los deportistas", key="deportistas_campeonato")

    if st.button("Guardar Campeonato Internacional"):
        guardar_datos({
            "Fecha de Registro": pd.Timestamp.now(),
            "Nombre Entrenador": nombre_entrenador,
            "Liga": liga,
            "Documento de Identidad": documento,
            "Evento": tipo_campeonato,
            "Fecha": fecha_camp,
            "Lugar": lugar_camp,
            "Prueba": prueba_camp,
            "Tipo de Función": tipo_funcion_camp,
            "Oro": oro_camp,
            "Plata": plata_camp,
            "Bronce": bronce_camp,
            "Posición 4-8": posicion_camp,
            "Nombre Deportistas": atletas_camp
        })
        st.success("✅ Registro guardado correctamente")

# 📌 Mostrar Registros Guardados
st.subheader("📋 Registros Guardados")
df = cargar_datos()
st.dataframe(df)

# 📌 Botón para actualizar datos sin errores
if st.button("🔄 Actualizar Datos"):
    st.rerun()

