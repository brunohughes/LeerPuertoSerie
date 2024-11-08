import tkinter as tk
import serial
import threading

def read_serial():
    try:
        ser = serial.Serial('COM3', 9600, timeout=1)  # Reemplaza 'COM3' con el puerto adecuado
        while True:
            line = ser.readline().decode('utf-8').strip()
            if line:
                values = line.split(',')  # Suponiendo que los valores vienen separados por comas
                if len(values) == 3:
                    valor1.set(values[0])
                    valor2.set(values[1])
                    valor3.set(values[2])
    except serial.SerialException as e:
        print(f"Error al abrir el puerto serie: {e}")

def send_command(command):
    try:
        ser.write(f"{command}\n".encode('utf-8'))
    except Exception as e:
        print(f"Error al enviar comando al puerto serie: {e}")

# Configurar la ventana principal
root = tk.Tk()
root.title("Lectura de Puerto Serie y Control Joystick")
root.geometry("400x400")

# Variables para almacenar los valores leídos del puerto serie
valor1 = tk.StringVar()
valor2 = tk.StringVar()
valor3 = tk.StringVar()

# Inicializar valores vacíos
valor1.set("N/A")
valor2.set("N/A")
valor3.set("N/A")

# Etiquetas para mostrar los valores
tk.Label(root, text="Valor 1:").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, textvariable=valor1).grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Valor 2:").grid(row=1, column=0, padx=10, pady=10)
tk.Label(root, textvariable=valor2).grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Valor 3:").grid(row=2, column=0, padx=10, pady=10)
tk.Label(root, textvariable=valor3).grid(row=2, column=1, padx=10, pady=10)

# Botones para el control tipo joystick
tk.Button(root, text="↑", command=lambda: send_command("UP")).grid(row=4, column=1, pady=10)
tk.Button(root, text="↓", command=lambda: send_command("DOWN")).grid(row=6, column=1, pady=10)
tk.Button(root, text="→", command=lambda: send_command("RIGHT")).grid(row=5, column=2, padx=10)
tk.Button(root, text="←", command=lambda: send_command("LEFT")).grid(row=5, column=0, padx=10)

# Iniciar el hilo para leer del puerto serie
threading.Thread(target=read_serial, daemon=True).start()

# Ejecutar la ventana principal
root.mainloop()
