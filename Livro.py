import os
os.system('cls || clear')

class Livro:
    def __int__(self, titulo: str, autor: str, numero_paginas: int, preco: float):
        self.titulo = titulo
        self.autor = autor 
        self.numero_paginas = numero_paginas
        self.preco = preco

    def __str__(self):
        return (f'Título: {self.titulo} \n'
                f'Autor: {self.autor} \n'
                f'Número de paginas: {self.numero_paginas}\n'
                f'Preco: {self.preco:.2f}')
    

livro1 = Livro("O homem mais rico da babilonia", "Arquimade", 350, 35.90)
livro2 = Livro("Maravilhos mundo novo", "Desconheço", 200, 40.00)

print('Informações Livro 01: \n')
print(livro1)

print('Informações Livro 02: \n')
print(livro2)


