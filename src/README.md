# Proyecto: Lectura de Puerto Serie y Visualización en Python

## Descripción
Este proyecto es un ejemplo simple que permite leer datos del puerto serie de una computadora y mostrarlos en una ventana. La aplicación está hecha en Python y utiliza las bibliotecas `tkinter` para la interfaz gráfica y `pyserial` para la comunicación con el puerto serie. Este proyecto es ideal para entender cómo interactuar con hardware mediante Python.

## Requisitos
Para poder ejecutar este proyecto, necesitas lo siguiente:

1. **Python 3.x**: Asegúrate de tener Python instalado en tu computadora. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).
2. **Biblioteca `pyserial`**: Esta biblioteca permite la comunicación con el puerto serie. Puedes instalarla con el siguiente comando:
   ```sh
   pip install pyserial
   ```

> Nota: `tkinter` ya viene incluido con Python, así que no necesitas instalarlo por separado.

## Instrucciones de Instalación

1. **Clonar el proyecto o crear una carpeta nueva** en tu computadora:
   ```sh
   mkdir LeerPuertoSerie
   cd LeerPuertoSerie
   ```

2. **Crear un entorno virtual** (opcional pero recomendado):
   ```sh
   python -m venv env
   ```

3. **Activar el entorno virtual**:
   - En Windows:
     ```sh
     .\env\Scripts\activate
     ```
  

4. **Instalar las dependencias**:
   ```sh
   pip install pyserial
   ```

## Uso del Proyecto

1. **Conectar el dispositivo al puerto serie** de tu computadora.
2. **Modificar el archivo `serial_gui_reader.py`** para que el puerto serie (`COM3` en el código) sea el adecuado para tu dispositivo. Por ejemplo, puede ser `COM4`, `COM5`, etc., dependiendo de tu configuración.
3. **Ejecutar el script**:
   ```sh
   python serial_gui_reader.py
   ```
4. **Interfaz Gráfica**: Se abrirá una ventana con tres campos: "Valor 1", "Valor 2" y "Valor 3". Estos campos mostrarán los valores recibidos desde el puerto serie.

## Funcionamiento del Código
- **Puerto Serie**: El código se conecta al puerto serie especificado (`COM3` en el ejemplo) con una velocidad de `9600` baudios.
- **Lectura de Datos**: Se lee continuamente del puerto serie. Los valores recibidos deben estar separados por comas (por ejemplo, `12,34,56`).
- **Hilo para la Lectura**: La lectura del puerto serie se realiza en un hilo separado para que la interfaz gráfica no se congele mientras se esperan los datos.
- **Mostrar Valores**: Los valores leídos se muestran en la ventana usando etiquetas (`Label`).

## Modificaciones
- **Cambiar el Puerto Serie**: Si el dispositivo está conectado a otro puerto, cambia la línea:
  ```python
  ser = serial.Serial('COM3', 9600, timeout=1)
  ```
  Reemplaza `'COM3'` por el puerto que corresponda.

- **Formato de los Datos**: El código espera que los datos lleguen separados por comas. Si el formato de los datos es diferente, deberás modificar la forma en que se dividen los valores (`line.split(',')`).

## Solución de Problemas
- **Error al abrir el puerto serie**: Asegúrate de que el puerto especificado está correcto y que no está siendo usado por otra aplicación.
- **Ventana no responde**: Esto puede ocurrir si el puerto serie no envía datos y el programa se queda esperando. Revisa las conexiones y el código del dispositivo.

## Ejemplo de Uso
Imagina que tienes un sensor de temperatura y humedad conectado al puerto serie de tu computadora. Este programa puede leer los valores del sensor y mostrarlos en tiempo real en una ventana, donde "Valor 1" podría ser la temperatura, "Valor 2" la humedad, y "Valor 3" algún otro valor adicional.
