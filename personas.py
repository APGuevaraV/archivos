from io import open

# lectura de fichero
fichero = open("personas.txt","r", encoding="utf8")
lineas = fichero.readlines()
fichero.close()

personas = []

for linea in lineas:
    
    campos = linea.replace("\n","").split(";")
    persona = { "id":campos[0], "nombre":campos[1], "apellido":campos[2],"fecha":campos[3]}
    personas.append(persona)
    
for p in personas:
    print(f"(id={p['id']}) {p['nombre']} {p['apellido']} => {p['fecha']}")
    
    