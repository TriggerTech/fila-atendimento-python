class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f"Cliente(nome={self.nome}, idade={self.idade})"