"""
COPIAR ESTE CODIGO EN main.py
"""
import forms
import reports
import sys
import os

# TODO (por hacer): Agregar un parámetro para poder cargar un form FormIndiceMasaCorporal
# TODO (por hacer): Agregar un parámetro para poder usar el ReportEdad
# TODO (por hacer): Agregar un parámetro para poder usar el reportIndiceMasaCorporal

print(sys.argv)

if len(sys.argv) == 1:
    print("No se ingreso ni un argumento")
    exit()

if sys.argv[1] == "--help" or sys.argv[1] == "-h":
    print("--cargar-form\tsirve para realizar una carga de formulario nuevo")
    print("--reporte\timprime un reporte optional -c para imprimir reporte con color")
    exit()

if sys.argv[1] == "--cargar-form":

    if not os.path.exists("./info"):        
        os.mkdir("./info")
        print("Se Creo la carpeta ./info")

    respuesta = input("¿Quiere cargar un Usuario? Si o No ")
    
    if respuesta.lower() == "si":
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        fecha_nacimiento = input("Fecha Nacimiento: ")
        pais = input("Pais: ")
        password = input("password: ")
        form_usuario = forms.FormUsuario(password, nombre, apellido, fecha_nacimiento, pais)
        form_usuario.validar_campos()
        form_usuario.guardar_formulario()
    
    elif respuesta.lower() == "no":
        respuesta = input("¿Quiere cargar un Persona? Si o No")
    
        if respuesta.lower() == "si":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            fecha_nacimiento = input("Fecha Nacimiento: ")
            pais = input("Pais: ")
            form_persona = forms.FormPersona(nombre, apellido, fecha_nacimiento, pais)
            form_persona.validar_campos()
            form_persona.guardar_formulario()
    
        elif respuesta.lower() == "no":
            print("Fin programa")
        else:
            print(f"No conozco el comand {respuesta}")
    
    else:
        print(f"No conozco el comando {respuesta}")

elif len(sys.argv) == 3 and sys.argv[1] == "--reporte" and sys.argv[2] == "-c":
    reporte = reports.ReportConColores("./info/form_usuario.csv", "Informe usuarios")
    reporte.procesar()
    reporte.imprimir()

elif  sys.argv[1] == "--reporte":
    reporte = reports.ReportGenerico("./info/form_usuario.csv", "Informe usuarios")
    reporte.procesar()
    reporte.imprimir()

else:
    print(f"No conozco el comando {sys.argv[1]}")
