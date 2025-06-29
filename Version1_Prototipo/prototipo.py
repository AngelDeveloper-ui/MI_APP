from playsound import playsound
import sqlite3 as sql
from datetime import dat
from playsound import playsound
from datetime import datetime
import sqlite3 as sql
import time


class logger:
        try:
            def presentacion():
                print("Hola, ¡bienvenido a tu ayudante de tareas para el día a día de tu vida!")
                print("Tambíen me puedes llamar Bob")
                print("¿Qué tal si para conocernos mejor te hago unas preguntas?")
                global name
                global years
                global country
                global pasword
                name = input("¿Cómo te llamas? : ").lower()
                years = int(input("¿Cuántos años tienes? : "))
                country = input("¿De qué país eres? : ").lower()
                pasword = input("Coloca una contraseña para tu cuenta : ")
                print(f"Eso seria todo {name}, ahora avanzemos")
        except Exception as e:
            print(f"ocurrio el error {e}")
        def crearBase():
            try:
                conn = sql.connect("datos.db")
                conn.commit()
                conn.close()
            except sql.Error as e:
                print(f"Ocurrio el error, {e}")
        def CrearTablas():
            try:
                conn = sql.connect("datos.db")
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS datos (
                        nombre_completo TEXT,
                        edad INTEGER,
                        pais TEXT,
                        contraseña TEXT
                    )
                ''')
                conn.commit()
                conn.close()
            except sql.Error as e:
                print(f"Ocurrio el error, {e}")
        def AgregarDatos(nombre_completo, edad, pais, contraseña):
            try:
                conn = sql.connect("datos.db")
                cursor = conn.cursor()
                while True:
                    cursor.execute("SELECT * FROM datos WHERE contraseña = ?", (contraseña,))
                    duplicado = cursor.fetchone()

                    if duplicado:
                        print("La contraseña ya está registrada. Intenta con otra.")
                        contraseña = input("Coloca una nueva contraseña para tu cuenta: ")
                    else:
                        instruccion = "INSERT INTO datos (nombre_completo, edad, pais, contraseña) VALUES (?, ?, ?, ?)"
                        cursor.execute(instruccion, (nombre_completo, edad, pais, contraseña))
                        conn.commit()
                        break
                conn.close()
            except sql.Error as e:
                print(f"Ocurrio el error, {e}")


logger.presentacion()
logger.crearBase()
logger.CrearTablas()
logger.AgregarDatos(nombre_completo=name, edad=years, pais=country,contraseña=pasword)