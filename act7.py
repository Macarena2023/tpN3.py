isleños= {"daniela":13, "ana":9, "lucia":54, "candelaria":22, "Elias":12}
print("agregando una nueva clave/valor...")

isleños["leslie"]= 22
print(isleños)

print("eliminando los usuarios menores de edad...")
eliminado= isleños.pop("daniela")
eliminado= isleños.pop("Elias")
print(isleños)

print("buscando el usuario con mayor edad....")
mayor= max(isleños)
print("el usuario con mayor edad es:", mayor)

print("buscando el usuario con menor edad...")
menor= min(isleños)
print("el usuario con menor edad es:", menor)

