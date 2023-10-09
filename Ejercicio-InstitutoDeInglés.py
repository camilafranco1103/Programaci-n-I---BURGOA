"""
dias = ["lunes", "martes", "miercoles", "jueves", "viernes"]
fecha_completa=input("Ingrese el día en el siguiente formato \n[dias], [fecha]/[mes]")

dia_semana = fecha_completa[0:fecha_completa.find(',')]

print(dia_semana)
day=int(fecha_completa[fecha_completa.find(" ")+1:fecha_completa.find("/")])
print(day)
month=int(fecha_completa[fecha_completa.find("/")+1:])
print(month)
"""

