usuarios={'jperez':{'password': '1234', 'rol': 'alumno', 'nombre': 'Juan Perez' },'amartin': {'password': '1234', 'rol': 'alumno', 'nombre': 'Ana Martin' }, 'ltrochez': {'password': '1234', 'rol': 'alumno', 'nombre': 'Luisa Trochez' }, 'adiaz': {'password': '1234', 'rol': 'alumno', 'nombre': 'Abraham Díaz' }, 'sescamilla':{'password': '1234', 'rol': 'alumno', 'nombre': 'Stephan Escamilla'}, 'jrojas': {'password': '1234', 'rol': 'alumno', 'nombre': 'Jesse Rojas' }, 'mlopez': {'password': '1234', 'rol': 'maestro', 'nombre': 'Maria Lopez' }, 'rgarcia': {'password': '1234', 'rol': 'coordinador', 'nombre': 'Rosa Garcia' }}
materias= ('Matematicas', 'Programación', 'Ingles II', 'Social-Emotional Skills', 'Arquitectura', 'Calculo')
calificaciones= {'jperez':{'Matematicas': 9.0, 'Programación': 8.7, 'Ingles II': 8.5, 'Social-Emotional Skills': 7.0, 'Arquitectura': 6.0, 'Calculo':7.5},
                 'amartin':{'Matematicas': 9.0, 'Programación': 8.0, 'Ingles II': 7.5, 'Social-Emotional Skills': 9.0, 'Arquitectura': 6.0, 'Calculo':9.5},
                 'ltrochez':{'Matematicas': 10, 'Programación': 8.9, 'Ingles II': 8.9, 'Social-Emotional Skills': 9.0, 'Arquitectura': 9.0, 'Calculo':8.7},
                 'adiaz':{'Matematicas': 9.0, 'Programación': 9.7, 'Ingles II': 9.5, 'Social-Emotional Skills': 9.0, 'Arquitectura': 9.0, 'Calculo':9.5},
                 'sescamilla':{'Matematicas': 9.0, 'Programación': 8.7, 'Ingles II': 8.5, 'Social-Emotional Skills': 7.0, 'Arquitectura': 9.6, 'Calculo':8.5},
                 'jrojas':{'Matematicas': 9.0, 'Programación': 8.7, 'Ingles II': 8.5, 'Social-Emotional Skills': 6.0, 'Arquitectura': 8.0, 'Calculo':9.5}}

#LOGIN MENU
acceso = False
while not acceso:
    usuario = input('Usuario: ')
    contraseña = input('Contraseña: ')

    if usuario in usuarios and usuarios[usuario]['password'] == contraseña:
        acceso = True
    else:
        print('Usuario o contraseña incorrectos. Intenta de nuevo.\n')

rol = usuarios[usuario]['rol']
nombre = usuarios[usuario]['nombre']
print(f'\nBienvenido, {nombre} ({rol})\n')

# ---------------------------------------------------------
# MENÚ SEGÚN ROL
# ---------------------------------------------------------

if rol == 'alumno':
    print(f'Boleta de {nombre}')

    aprobadas = set()
    for materia in materias:
        calif = calificaciones[usuario][materia]
        print(f'{materia}: {calif}')
        if calif >= 8.0:
            aprobadas.add(materia)

    pendientes = set(materias) - aprobadas

    print('')

    if aprobadas:
        print(f'Materias aprobadas: {aprobadas}')
    else:
        print('Materias aprobadas: Ninguna')

    if pendientes:
        print(f'Materias pendientes: {pendientes}')
    else:
        print('Materias pendientes: Ninguna')

elif rol == 'maestro':
    print('Lista de alumnos:')
    for clave_usuario in usuarios:
        if usuarios[clave_usuario]['rol'] == 'alumno':
            print(f"- {clave_usuario}: {usuarios[clave_usuario]['nombre']}")

    continuar = 's'
    while continuar == 's':
        alumno = input('\nAlumno (usuario): ')
        while alumno not in calificaciones:
            print('Ese alumno no existe.')
            alumno = input('Alumno (usuario): ')

        materia = input('Materia: ')
        while materia not in materias:
            print('Esa materia no existe.')
            materia = input('Materia: ')

        nueva_calificacion = float(input('Nueva calificación: '))
        calificaciones[alumno][materia] = nueva_calificacion
        print('Calificación actualizada.')

        continuar = input('\n¿Calificar a otro alumno? (s/n): ')

elif rol == 'coordinador':
    print('Lista de maestros:')
    for clave_usuario in usuarios:
        if usuarios[clave_usuario]['rol'] == 'maestro':
            print(f"- {clave_usuario}: {usuarios[clave_usuario]['nombre']}")

    print('\nLista de materias:')
    for materia in materias:
        print(f'- {materia}')

    print('\nLista de alumnos con sus calificaciones:')
    for alumno in calificaciones:
        print(f"\n{usuarios[alumno]['nombre']} ({alumno}):")
        for materia in materias:
            print(f'  {materia}: {calificaciones[alumno][materia]}')


