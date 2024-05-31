import tkinter as tk
from tkinter import messagebox

# Lista de produtos no estoque
estoque = {
    "Coca-Cola": 5.00,
    "Sanduíche": 7.50,
    "Batata Frita": 3.00,
    "Suco de Laranja": 4.00,
    "Salada": 6.00,
    # Adicione mais produtos aqui
    "Hamburguer": 8.00,
    "Café": 2.50,
    "Água": 1.50,
    "Bolo": 4.50,
    "Sorvete": 3.00
}

# Carrinho de compras
carrinho = {}

# Função para adicionar produto ao carrinho
def adicionar_ao_carrinho(produto):
    if produto in carrinho:
        carrinho[produto] += 1
    else:
        carrinho[produto] = 1
    atualizar_carrinho()

# Função para remover produto do carrinho
def remover_do_carrinho(produto):
    if produto in carrinho:
        if carrinho[produto] > 1:
            carrinho[produto] -= 1
        else:
            del carrinho[produto]
    atualizar_carrinho()

# Função para atualizar a exibição do carrinho
def atualizar_carrinho():
    carrinho_listbox.delete(0, tk.END)
    total = 0
    for produto, quantidade in carrinho.items():
        preco = estoque[produto] * quantidade
        total += preco
        carrinho_listbox.insert(tk.END, f"{produto} x{quantidade} - R${preco:.2f}")
    total_label.config(text=f"Total: R${total:.2f}")

# Função para finalizar a compra
def finalizar_compra():
    if not carrinho:
        messagebox.showinfo("Carrinho vazio", "O carrinho está vazio!")
        return
    total = sum(estoque[produto] * quantidade for produto, quantidade in carrinho.items())
    messagebox.showinfo("Compra finalizada", f"Total a pagar: R${total:.2f}")
    carrinho.clear()
    atualizar_carrinho()

# Criando a interface gráfica
app = tk.Tk()
app.title("Lanchonete")

# Ajustar o tamanho da janela principal
app.geometry("600x400")
app.maxsize(1200,800)

# Frame de produtos
frame_produtos = tk.Frame(app)
frame_produtos.pack(side=tk.LEFT, padx=10, pady=10)

tk.Label(frame_produtos, text="Estoque").pack()
produtos_listbox = tk.Listbox(frame_produtos, width=50, height=50)
for produto in estoque:
    produtos_listbox.insert(tk.END, produto)
produtos_listbox.pack()

adicionar_button = tk.Button(frame_produtos, text="Adicionar ao Carrinho", command=lambda: adicionar_ao_carrinho(produtos_listbox.get(tk.ACTIVE)))
adicionar_button.pack(pady=5)

# Frame do carrinho
frame_carrinho = tk.Frame(app)
frame_carrinho.pack(side=tk.RIGHT, padx=10, pady=10)

tk.Label(frame_carrinho, text="Carrinho").pack()
carrinho_listbox = tk.Listbox(frame_carrinho, width=50, height=50)
carrinho_listbox.pack()

remover_button = tk.Button(frame_carrinho, text="Remover do Carrinho", command=lambda: remover_do_carrinho(carrinho_listbox.get(tk.ACTIVE).split(" x")[0]))
remover_button.pack(pady=5)

total_label = tk.Label(frame_carrinho, text="Total: R$0.00")
total_label.pack()

finalizar_button = tk.Button(frame_carrinho, text="Finalizar Compra", command=finalizar_compra)
finalizar_button.pack(pady=5)

# Iniciar o aplicativo
app.mainloop()
