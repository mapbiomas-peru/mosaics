# 🚀 Instrucciones para ejecutar

Sigue estos pasos para configurar y ejecutar el proyecto de manera correcta.

---

### 1️⃣ **Crear una cuenta de Google Earth Engine (GEE)** 🌍
- Si aún no tienes una cuenta en Google Earth Engine, [regístrate aquí](https://signup.earthengine.google.com/).

### 2️⃣ **Instalar y configurar la librería Google Earth Engine en Python** 🐍
- Es recomendable usar Python **3.10.x** para una instalación sin problemas.
- Puedes usar VisualStudioCode u otro editor de texto
- Instala la librería con el siguiente comando:
  ```bash
  pip install earthengine-api
### 3️⃣ **Copiar la estructura de carpetas del repositorio en tu local** 💻
- Descarga y/o clona este repositorio en una carpeta local:
  ```bash
  git clone https://github.com/usuario/repositorio.git
### 4️⃣ **Abrir el proyecto en Visual Studio Code** 💻
- Abre el proyecto mosaics-main en Visual Studio Code en modo de carpeta.

### 5️⃣ **Abrir el script mapbiomas_mosaics_collection_4_raisg_card_v5.py** 📝
- Navega hasta el script ubicado en mapbiomas/mapbiomas_mosaics_collection_4_raisg_card_v5.py.

### 6️⃣ **Configurar el archivo CSV de la parametrización** 📊
- En la línea 38 del script, configura el archivo CSV con los parámetros correspondientes. Asegúrate de que el archivo CSV mantenga la estructura correcta.

Ejemplos de la estructura del CSV se encuentran en la carpeta mapbiomas/data.

### 7️⃣ **Configurar la ruta de los mosaicos** 🗺️
- En las líneas 57 a 63 del script, establece la ruta al asset donde se guardarán los mosaicos. En nuestro caso, la ruta es mosaics-2.

### 8️⃣ **Correr el script** ▶️
- Si todo está correctamente configurado, ejecuta el script. Si no hay errores, se generarán las tareas usando tu cuenta de GEE.
