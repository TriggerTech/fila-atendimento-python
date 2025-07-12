from collections import deque

class FilaAtendimento:
    def __init__(self):
        self.fila = deque()

    def adicionar_cliente(self, cliente):
        self.fila.append(cliente)

    def atender_cliente(self):
        if self.fila:
            return self.fila.popleft()
        return None

    def listar_fila(self):
        return list(self.fila)