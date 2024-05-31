import tkinter as tk
from tkinter import messagebox

# Lista de produtos no estoque
estoque = {
  "Coca-Cola": {"preco": 5.00, "quantidade": 10},
    "Sanduíche": {"preco": 7.50, "quantidade": 15},
    "Batata Frita": {"preco": 3.00, "quantidade": 20},
    "Suco de Laranja": {"preco": 4.00, "quantidade": 8},
    "Salada": {"preco": 6.00, "quantidade": 12},
    "Hamburguer": {"preco": 8.00, "quantidade": 5},
    "Café": {"preco": 2.50, "quantidade": 30},
    "Água": {"preco": 1.50, "quantidade": 25},
    "Bolo": {"preco": 4.50, "quantidade": 10},
    "Sorvete": {"preco": 3.00, "quantidade": 7}
}

# Carrinho de compras
carrinho = {}

# Função para adicionar produto ao carrinho
def adicionar_ao_carrinho(produto):
    if estoque[produto]['quantidade'] == 0:
        messagebox.showinfo("Estoque Vazio", f"{produto} esta fora do estoque!")
        return 
    if produto in carrinho:
        carrinho[produto] += 1
    else:
        carrinho[produto] = 1
    estoque[produto]["Quantidade"] -= 1
    atualizar_estoque()
    atualizar_carrinho()
    
# Função para remover produto do carrinho
def remover_do_carrinho(produto):
    if produto in carrinho:
        if carrinho[produto] > 1:
            carrinho[produto] -= 1
        else:
            del carrinho[produto]
        estoque[produto]['quantidade'] += 1
        atualizar_estoque()
    atualizar_carrinho()

# Função para atualizar a exibição do carrinho
def atualizar_carrinho():
    carrinho_listbox.delete(0, tk.END)
    total = 0
    for produto, quantidade in carrinho.items():
        preco = estoque[produto]["preco"] * quantidade
        total += preco
        carrinho_listbox.insert(tk.END, f"{produto} x{quantidade} - R${preco:.2f}")
    total_label.config(text=f"Total: R${total:.2f}")
    
    
#Função que atualiza a exibição do estoque
def atualizar_estoque():
    produtos_listbox.delete(0, tk.END)
    for produto, info in estoque.items():
        produtos_listbox.insert(tk.END, f"{produto} - RS{info['preco']:.2f}- {info['quantidade']} unidades")

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

#Titulo do projeto
title_label = tk.Label(master=app, text="Lanchonete David", font= 'Calibri 24 bold')
title_label.pack()

#Gerando alguns inputs
text_input = tk.Label(master= app, text="Inserir codigo do produto")
input_frame = tk.Frame(master= app)
entry = tk.Entry(master=app)
button = tk.Button(master = input_frame, text = 'Inserir')
input_frame.pack()
entry.pack()
button.pack()
text_input.pack()


# Ajustar o tamanho da janela principal
app.geometry("600x400")


# Frame de produtos
frame_produtos = tk.Frame(app)
frame_produtos.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

tk.Label(frame_produtos, text="Estoque").pack()
produtos_listbox = tk.Listbox(frame_produtos, width=50, height=50)
for produto in estoque:
    produtos_listbox.insert(tk.END, produto)
produtos_listbox.pack(fill=tk.BOTH, expand=True)

adicionar_button = tk.Button(frame_produtos, text="Adicionar ao Carrinho", command=lambda: adicionar_ao_carrinho(produtos_listbox.get(tk.ACTIVE)))
adicionar_button.pack(pady=5, fill=tk.X)

# Frame do carrinho
frame_carrinho = tk.Frame(app)
frame_carrinho.pack(side=tk.RIGHT, fill=tk.BOTH, padx=10, pady=10, expand=True)

tk.Label(frame_carrinho, text="Carrinho").pack()
carrinho_listbox = tk.Listbox(frame_carrinho, width=50, height=50)
carrinho_listbox.pack(fill=tk.BOTH, expand=True)

remover_button = tk.Button(frame_carrinho, text="Remover do Carrinho", command=lambda: remover_do_carrinho(carrinho_listbox.get(tk.ACTIVE).split(" x")[0]))
remover_button.pack(pady=5, fill=tk.X)

total_label = tk.Label(frame_carrinho, text="Total: R$0.00")
total_label.pack()

finalizar_button = tk.Button(frame_carrinho, text="Finalizar Compra", command=finalizar_compra)
finalizar_button.pack(pady=5, fill=tk.X)

# Iniciar o aplicativo
app.mainloop()
