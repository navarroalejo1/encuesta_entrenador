# 🏗️ 1. Usar la imagen base de Python
FROM python:3.9

# 📁 2. Crear y establecer el directorio de trabajo
WORKDIR /app

# 📂 3. Copiar todos los archivos del proyecto al contenedor
COPY . /app

# 🔧 4. Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# 🚀 5. Exponer el puerto donde correrá la app
EXPOSE 8501

# 🏃 6. Ejecutar la aplicación con Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
