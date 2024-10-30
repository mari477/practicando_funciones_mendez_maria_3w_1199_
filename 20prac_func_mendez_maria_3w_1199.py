print(" ")
print("Mendez Maria Guadalupe Yazmin 3w 1199")
print(" ")
def tri_recursion(k):                     #Definir mi funcion
    if k > 0:                             #Se pone if
        result = k + tri_recursion(k - 1) #Defino re sultado
        print(result)                     #Llamo al resultado
    else:                                 #Else
        result = 0                        #Resultado =0
    return result                         #Return reslutado

print("\n\nResultados")    #Imprimo el resultado
tri_recursion(10)  # Imprime la suma acumulada
print(" ")
