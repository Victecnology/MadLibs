import tkinter as tk

# Definimos la función para generar la historia
def generar_historia():
  # Obtenemos las palabras del usuario
  lugar = lugar_entry.get()
  animal = animal_entry.get()
  comida = comida_entry.get()
  verbo = verbo_entry.get()
  adjetivo = adjetivo_entry.get()
  sustantivo = sustantivo_entry.get()

  # Inicializamos la variable historia
  historia = ""

  # Generamos la historia
  historia = f"Estaba caminando por {lugar} cuando vi un {animal} {verbo} una {comida}. " \
             f"El {animal} era muy {adjetivo} y tenía un {sustantivo} muy grande."

  # Imprimimos la historia por pantalla
  print(historia)

# Creamos la ventana principal
root = tk.Tk()
root.title("Juego Mad Libs")

# Creamos los cuadros de entrada para las palabras
lugar_entry = tk.Entry(root)
animal_entry = tk.Entry(root)
comida_entry = tk.Entry(root)
verbo_entry = tk.Entry(root)
adjetivo_entry = tk.Entry(root)
sustantivo_entry = tk.Entry(root)

# Colocamos los cuadros de entrada en la ventana
lugar_label = tk.Label(root, text="Lugar:")
lugar_label.grid(row=0, column=0)
lugar_entry.grid(row=0, column=1)

animal_label = tk.Label(root, text="Animal:")
animal_label.grid(row=1, column=0)
animal_entry.grid(row=1, column=1)

comida_label = tk.Label(root, text="Comida:")
comida_label.grid(row=2, column=0)
comida_entry.grid(row=2, column=1)

verbo_label = tk.Label(root, text="Verbo:")
verbo_label.grid(row=3, column=0)
verbo_entry.grid(row=3, column=1)

adjetivo_label = tk.Label(root, text="Adjetivo:")
adjetivo_label.grid(row=4, column=0)
adjetivo_entry.grid(row=4, column=1)

sustantivo_label = tk.Label(root, text="Sustantivo:")
sustantivo_label.grid(row=5, column=0)
sustantivo_entry.grid(row=5, column=1)

# Creamos un botón para generar la historia
generar_button = tk.Button(root, text="Generar historia", command=generar_historia)
generar_button.grid(row=6, column=0)

# Ejecutamos el bucle principal
root.mainloop()