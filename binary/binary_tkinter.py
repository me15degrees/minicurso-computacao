import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def decompose_number(event=None):
    try:
        num = int(entry.get())
        if num < 0 or num > 2047:
            raise ValueError
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido entre 0 e 2047.")
        return
    
    binary_representation = [0] * 11
    for i in range(10, -1, -1):
        if num >= 2**i:
            binary_representation[10-i] = 1
            num -= 2**i

    result_label.config(text="Representação binária: " + "".join(map(str, binary_representation)))

# Criação da janela principal
root = tk.Tk()
root.title("Representação no sistema binário")
root.geometry("800x500")  # define o tamanho inicial da janela

# Calcula as coordenadas para centralizar os widgets
window_width = 800
window_height = 350
x_offset = (root.winfo_screenwidth() - window_width) // 2
y_offset = (root.winfo_screenheight() - window_height) // 2

# Define as coordenadas da janela
root.geometry(f"{window_width}x{window_height}+{x_offset}+{y_offset}")

# Carrega e redimensiona a primeira imagem
img_path1 = "binary/assets/mudkip.png"  # caminho completo da primeira imagem
img1 = Image.open(img_path1)
img1 = img1.resize((200, 200))  # redimensiona a imagem para 100x100 pixels
photo1 = ImageTk.PhotoImage(img1)

# Coloca a primeira imagem no canto superior esquerdo da janela
image_label1 = tk.Label(root, image=photo1)
image_label1.image = photo1  # mantém uma referência para a imagem
image_label1.place(x=10, y=10)  # posiciona a imagem no canto superior esquerdo da janela

# Carrega e redimensiona a segunda imagem
x = 200
y = 46
img_path2 = "binary/assets/ufu_logo.png"  # caminho completo da segunda imagem
img2 = Image.open(img_path2)
img2 = img2.resize((x, y))  # redimensiona a imagem para 240x55 pixels
photo2 = ImageTk.PhotoImage(img2)

# Calcula as coordenadas para posicionar a segunda imagem no canto inferior direito da janela
x_pos = window_width - x - 12
y_pos = window_height - y - 12

# Coloca a segunda imagem no canto inferior direito da janela
image_label2 = tk.Label(root, image=photo2)
image_label2.image = photo2  # mantém uma referência para a imagem
image_label2.place(x=x_pos, y=y_pos)  # posiciona a imagem no canto inferior direito da janela

# Entrada do número
entry_label = tk.Label(root, text="Insira um número até 2047:")
entry_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
entry_label.config(font=("Arial", 14))  # ajusta o tamanho da fonte do Label

entry = tk.Entry(root, width=30)  # ajusta a largura da Entry para 30 caracteres
entry.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
entry.bind('<Return>', decompose_number)  # Adiciona o binding para a tecla Enter

# Botão para decompor o número
button = tk.Button(root, text="Resultado", command=decompose_number)
button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
button.config(font=("Arial", 12))  # ajusta o tamanho da fonte do Button

# Label para mostrar o resultado
result_label = tk.Label(root, text="")
result_label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
result_label.config(font=("Arial", 14))  # ajusta o tamanho da fonte do Label

# Execução da aplicação
root.mainloop()
