first= ['Perro', 'Gallina', 'Gato', 'Sapo']

espace1 = first[0]
first[0] = first[len(first)-1]
first[len(first)-1] = espace1 

print(first)
