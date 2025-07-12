import tkinter as tk
from cliente import Cliente
from fila import FilaAtendimento

fila = FilaAtendimento()

def adicionar():
    nome = entry_nome.get()
    idade = entry_idade.get()
    if nome and idade.isdigit():
        cliente = Cliente(nome, int(idade))
        fila.adicionar_cliente(cliente)
        atualizar_fila()
        entry_nome.delete(0, tk.END)
        entry_idade.delete(0, tk.END)

def atender():
    cliente = fila.atender_cliente()
    if cliente:
        label_atendimento["text"] = f"Atendendo: {cliente}"
    else:
        label_atendimento["text"] = "Nenhum cliente na fila"
    atualizar_fila()

def atualizar_fila():
    fila_text.delete("1.0", tk.END)
    for c in fila.listar_fila():
        fila_text.insert(tk.END, f"{c}\n")


root = tk.Tk()
root.title("Fila de Atendimento")

tk.Label(root, text="Nome:").grid(row=0, column=0)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1)

tk.Label(root, text="Idade:").grid(row=1, column=0)
entry_idade = tk.Entry(root)
entry_idade.grid(row=1, column=1)

btn_add = tk.Button(root, text="Adicionar Cliente", command=adicionar)
btn_add.grid(row=2, column=0, columnspan=2, pady=5)

btn_atender = tk.Button(root, text="Atender Cliente", command=atender)
btn_atender.grid(row=3, column=0, columnspan=2, pady=5)

label_atendimento = tk.Label(root, text="Ninguém sendo atendido ainda.")
label_atendimento.grid(row=4, column=0, columnspan=2)

fila_text = tk.Text(root, height=10, width=40)
fila_text.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()