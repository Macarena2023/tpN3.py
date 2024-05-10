frecuencia= ["a", "b", "a", "d", "b"]

frecuencia_palabras= {}

for palabra in frecuencia:
  if palabra in frecuencia_palabras:
    frecuencia_palabras[palabra] += 1
  else:
    frecuencia_palabras[palabra] = 1
print("frecuencia de las palabras:", frecuencia_palabras)

