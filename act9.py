manuscrito= ["hola", "hola", "nose", "si", "nose", "equisde", "nose"]

frecuencia= {}

for palabra in manuscrito:
  if palabra in frecuencia:
    frecuencia[palabra] += 1
  else:
    frecuencia[palabra] = 1

mayor_frecuencia= max(frecuencia)
print("la palabra con mayor frecuencia es:", palabra)

