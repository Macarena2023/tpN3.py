cofre_1= [10, 20, 30, 40]
cofre_2= [50, 60, 70, 80]

def cofres (cofre_final):
  cofre_1.extend(cofre_2)
  return cofre_1
cofre_fin= cofres(cofre_1)

print("el cofre final es:", cofre_fin)
