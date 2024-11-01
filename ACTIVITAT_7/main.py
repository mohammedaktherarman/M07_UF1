from create import crearRegistro
from create_table import crearTabla
from delete import borrarRegistro
from read import leerRegistros
from update import actualitzaRegistro

actualitzaRegistro("arman","akther",20,"arman@iticbcn.cat",4)
print("Escull amb numeros el que vols fer:\n"
      "1 Per crear un registre\n"
      "2 Per mostrar per pantalla els registres,\n"
      "3 Per actualiza un registre i modificar un camp o tots d'un registre,\n"
      "4 Per borrar un registre amb el seu ID,\n"
      "5 Per crear la taula:\n")

numeroEscullit = int(input("Escull el numero:"))

if numeroEscullit == 1:
    nom = input("Posa el user_name:")
    cognom = input("Posa el user_surname:")
    user_age = int(input("Posa el user_age:"))
    user_email = input("Posa el user_email:")

    crearRegistro(nom, cognom, user_age, user_email)
    print("Registre creat\n")

    leerRegistros()

if numeroEscullit == 2:
    leerRegistros()

if numeroEscullit == 3:
    id = input("Posa el ID del registre a modificar:")
    nom = input("Posa el nou user_name (deixa en blanc per no modificar):")
    cognom = input("Posa el nou user_surname (deixa en blanc per no modificar):")
    user_age = input("Posa el nou user_age (deixa en blanc per no modificar):")
    user_email = input("Posa el nou user_email (deixa en blanc per no modificar):")

    actualitzaRegistro(nom, cognom, user_age, user_email, id)
    print("Registre actualitzat\n")

    leerRegistros()

if numeroEscullit == 4:
    numero = input("Posa el numero del ID a borrar:")
    borrarRegistro(numero)
    print("Registre borrat\n")

    leerRegistros()

if numeroEscullit == 5:
    crearTabla()
    print("Tabla creada")
