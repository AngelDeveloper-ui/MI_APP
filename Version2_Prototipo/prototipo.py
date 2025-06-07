from playsound import playsound
import sqlite3 as sql
from datetime import datetime

class funcionamiento:
    def crearbase():
        try:
            conn = sql.connect("actividades.db")
            conn.commit()
            conn.close()
        except sql.Error as e:
            print(f"ocurrió el error : {e}")

    def crearTablas():
        try:
            conn = sql.connect("actividades.db")
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS actividades (
                    nombre_todos_actividad TEXT,
                    hora_todas TEXT,
                    nombre_sola_actividad TEXT,
                    hora_sola TEXT
                )
            ''')
            conn.commit()
            conn.close()
        except sql.Error as e:
            print(f"ocurrió el error : {e}")

    def preguntar():
        try:
            hora_actual = datetime.now().strftime("%H:%M")
            print("Estoy aquí para ayudarte a recordar tus actividades.")
            dia = input("¿Deseas poner una alarma para una actividad diaria? S/N: ").lower()

            conn = sql.connect("actividades.db")
            cursor = conn.cursor()

            if dia == "s":
                nombre = input("¿Cómo se llamará la actividad?: ").lower()
                hora = input("¿A qué hora se ejecutará? (ejemplo 15:30): ")
                instruccion = "INSERT INTO actividades (nombre_todos_actividad, hora_todas) VALUES (?, ?)"
                cursor.execute(instruccion, (nombre, hora))
                conn.commit()

                cursor.execute("SELECT nombre_todos_actividad, hora_todas FROM actividades")
                filas = cursor.fetchall()
                for evento, hora_guardada in filas:
                    if hora_actual == hora_guardada:
                        print(f"¡Ya es hora de {evento}!")
                        playsound("alarma.mp3")

            elif dia == "n":
                nombre = input("¿Cómo se llamará la actividad?: ").lower()
                dias = input("¿Qué días se ejecutará? ej: lunes, martes, etc.: ").lower()
                hora = input("¿A qué hora se ejecutará? ejemplo 15:30: ")
                instruccion = "INSERT INTO actividades (nombre_sola_actividad, hora_sola) VALUES (?, ?)"
                cursor.execute(instruccion, (nombre, hora))
                conn.commit()

                cursor.execute("SELECT nombre_sola_actividad, hora_sola FROM actividades")
                filas2 = cursor.fetchall()
                for evento, hora_guardada in filas2:
                    if hora_actual == hora_guardada:
                        print(f"¡Ya es hora de {evento}!")
                        playsound("alarma.mp3")

            conn.close()

        except sql.Error as e:
            print(f"Ocurrió el error : {e}")

funcionamiento.preguntar()