from clases.clases import Perro
#####-
# crear instancias
perro1 = Perro("Firulais", 3)#lamado por detras al consrtuctor
perro2 = Perro("Luna", 5)

######
print(f"{perro1.nombre} tiene {perro1.edad} {perro1.ladra()}")
print(f"{perro2.nombre} tiene {perro2.edad} {perro2.ladra()}")