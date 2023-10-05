"""
2- Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el
0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene.
Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.
"""
num = int(input("Ingrese numeros  enteros positivos: "))
par_final=0
impar_final=0
while num != 0:
    num_par=0
    num_impar=0
    while num>0:
        ult_digito=num%10
        if ult_digito % 2== 0:
            num_par += 1
        else:
            num_impar += 1
        num=(num-ult_digito)/10
    print("La cantidad de num pares es: ",num_par,", y de impares: ",num_impar)      
    par_final+=num_par
    impar_final+=num_impar
    num = int(input("Ingrese numeros  enteros positivos: "))
print("")
print("Cantidad total de pares: ",par_final,", y el total de los impares: ",impar_final)