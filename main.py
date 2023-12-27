"""
Desafio 12 - Nested For Loop

Para este desafaio, vamos criar uma lista "Frutas" e outra "Vegetaias". Usando o for loop 
aninhado para imprimir todas as combinações possíveis de frutas e vegetais.

Fruta e Vegetal

"""

#Listas
frutas = ['Laranja', 'Maça', 'Uva']
vegetais = ['Cenoura', 'Batata', 'Brócolis']

#for aninhado
for fruta in frutas:
    for vegetal in vegetais:
        print(f'{fruta} e {vegetal}')