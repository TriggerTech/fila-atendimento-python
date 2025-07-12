# 🧑‍💼 Fila de Atendimento com Tkinter

Um projeto simples feito em Python para simular uma fila de atendimento com interface gráfica.

## 💡 Funcionalidades

- Adicionar clientes informando nome e idade
- Atender clientes na ordem de chegada (FIFO)
- Interface gráfica simples com atualização da fila em tempo real
- Mensagem informando quem está sendo atendido

## 📁 Estrutura do Projeto

fila_atendimento/
├── cliente.py # Classe Cliente
├── fila.py # Lógica da fila de atendimento
└── interface.py # Interface gráfica com Tkinter


## 🚀 Como executar

1. Clone o repositório:

git clone https://github.com/TriggerTech/fila-atendimento-python.git
cd fila-atendimento-python

    Execute o projeto:


python interface.py

    ⚠️ Certifique-se de ter o Python instalado. O projeto usa apenas bibliotecas nativas (Tkinter, collections).

🔧 Tecnologias 

    Python 

    Tkinter (interface gráfica)

    Deque (estrutura de fila eficiente)


📌 Possíveis melhorias

    Adicionar prioridade por idade (ex: idosos primeiro)

    Salvar fila em arquivo 

    Versão web 