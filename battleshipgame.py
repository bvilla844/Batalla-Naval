import subprocess
import platform
import time


class MesaJuego:
    def __init__(self):
        self.nombre_jugador1 = str(input("Jugador 1 por favor ingresa tu nombre : "))
        self.nombre_jugador2 = str(input("Jugador 2 por favor ingresa tu nombre : "))
        self.tabla_defensa_jugador1 = self.inicializar_tabla()
        self.tabla_defensa_jugador2 = self.inicializar_tabla()
        self.tabla_ataque_jugador1 = self.inicializar_tabla()
        self.tabla_ataque_jugador2 = self.inicializar_tabla()

    def inicializar_tabla(self):
        # Inicializa una tabla de 9x9 con espacios vacíos
        return [[" " for _ in range(9)] for _ in range(9)]

    def letras_a_numeros(self):
        letras_a_numeros = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8}
        return letras_a_numeros

    def tabla_defensa(self, tabla):
        print("   A B C D E F G H I ")
        print("   +-+-+-+-+-+-+-+-+-")

        for numero_fila, fila in enumerate(tabla, start=1):
            print(f"{numero_fila} |{'|'.join(fila)}|")

    def tabla_ataque(self, tabla):
        print("   A B C D E F G H I ")
        print("   +-+-+-+-+-+-+-+-+-")

        for numero_fila, fila in enumerate(tabla, start=1):
            print(f"{numero_fila} |{'|'.join(fila)}|")

    def verificar_posiciones_libres(self, tabla, fila, columna, longitud, direccion):
        max_filas = len(tabla)
        max_columnas = len(tabla[0])

        if direccion == "HR":  # Horizontal derecha
            if columna + longitud > max_columnas:  # Verificar si el barco cabe en el tablero
                return False
            for i in range(longitud):
                if tabla[fila][columna + i] != " ":
                    return False
        elif direccion == "HL":  # Horizontal izquierda
            if columna - longitud + 1 < 0:  # Verificar si el barco cabe en el tablero
                return False
            for i in range(longitud):
                if tabla[fila][columna - i] != " ":
                    return False
        elif direccion == "VB":  # Vertical abajo
            if fila + longitud > max_filas:  # Verificar si el barco cabe en el tablero
                return False
            for i in range(longitud):
                if tabla[fila + i][columna] != " ":
                    return False
        elif direccion == "VA":  # Vertical arriba
            if fila - longitud + 1 < 0:  # Verificar si el barco cabe en el tablero
                return False
            for i in range(longitud):
                if tabla[fila - i][columna] != " ":
                    return False
        return True

    def ubicar_barco_usuario(self, longitud, nombre_jugador, tabla):
        print(f"Jugador {nombre_jugador} ubica tu barco de {longitud} posiciones, asegurate que no te esten mirando!!.")
        while True:
            try:
                # Solicita la orientación del barco
                orientacion = input("¿Quieres ubicar el barco horizontal (H) o vertical (V)? : ").upper()
                if orientacion not in ["H", "V"]:
                    print("Por favor ingresa 'H' para horizontal o 'V' para vertical.")
                    continue

                fila = int(input("Por favor ingresa una fila (1-9): "))
                if fila < 1 or fila > 9:
                    print("Por favor ingresa una fila válida (1-9).")
                    continue

                columna = input("Por favor ingresa una columna (A-I): ").upper()
                if columna not in self.letras_a_numeros():
                    print("Por favor ingresa una columna válida (A-I).")
                    continue

                columna_num = self.letras_a_numeros()[columna]

                if orientacion == "H":  # Horizontal
                    direccion = input("¿Deseas colocar el barco hacia la derecha (R) o izquierda (L)? ").upper()
                    if direccion not in ["R", "L"]:
                        print("Por favor ingresa 'R' para derecha o 'L' para izquierda.")
                        continue
                    direccion = "HR" if direccion == "R" else "HL"

                elif orientacion == "V":  # Vertical
                    direccion = input("¿Deseas colocar el barco hacia abajo (B) o arriba (A)? ").upper()
                    if direccion not in ["B", "A"]:
                        print("Por favor ingresa 'B' para abajo o 'A' para arriba.")
                        continue
                    direccion = "VB" if direccion == "B" else "VA"

                if not self.verificar_posiciones_libres(tabla, fila - 1, columna_num, longitud,
                                                        direccion):
                    print(
                        "El barco no cabe en la tabla en la dirección especificada o las posiciones están ocupadas. Intenta de nuevo.")
                    continue

                for offset in range(longitud):
                    if orientacion == "H":
                        if direccion == "HR":
                            tabla[fila - 1][columna_num + offset] = "X"
                        elif direccion == "HL":
                            tabla[fila - 1][columna_num - offset] = "X"
                    elif orientacion == "V":
                        if direccion == "VB":
                            tabla[fila - 1 + offset][columna_num] = "X"
                        elif direccion == "VA":
                            tabla[fila - 1 - offset][columna_num] = "X"
                self.tabla_defensa(tabla)
                break
            except ValueError:
                print("Entrada no válida. Por favor, ingresa un número para la fila.")
            except KeyError:
                print("Entrada no válida para la columna.")

    def limpiar_terminal(self):
        sistema = platform.system()
        if sistema == "Windows":
            subprocess.run(['cls'], shell=True)
        else:
            subprocess.run(['clear'])

    def atacar(self, jugador, tabla_defensa, tabla_ataque):
        self.tabla_ataque(tabla_ataque)
        while True:
            try:
                x_fila = input(f"Es hora de atacar!!,{jugador} favor ingresa la fila del barco que piensas atacar: ")
                while x_fila not in '123456789':
                    print('No es una seleccion valida, por favor ingresa una fila valida')
                    x_fila = input(
                        f"Es hora de atacar!!,{jugador} favor ingresa la fila del barco que piensas atacar: ")
                    break
                y_columna = input(
                    f"Es hora de atacar!!,{jugador} favor ingresa la columna del barco que piensas atacar: ").upper()
                while y_columna not in 'ABCDEFGHI':
                    print('No es una seleccion valida, por favor ingresa una columna valida')
                    y_columna = input(
                        f"Es hora de atacar!!,{jugador} favor ingresa la columna del barco que piensas atacar: ").upper()
                columna_num = self.letras_a_numeros()[y_columna]
                fila_num = int(x_fila) - 1
                if tabla_defensa[fila_num][columna_num] == "X":
                    print(f"¡Buena puntería, {jugador}! ¡Has acertado en el blanco!")
                    tabla_ataque[fila_num][columna_num] = "X"
                else:
                    print(f"¡Fallaste el ataque, {jugador}!")
                    tabla_ataque[fila_num][columna_num] = "O"
                break
            except ValueError:
                print("Entrada no válida. Asegúrate de ingresar un número para la fila.")
            except KeyError:
                print("Entrada no válida para la columna.")
        self.tabla_ataque(tabla_ataque)
        time.sleep(5)
        self.limpiar_terminal()

    def game_win(self, tabla_defensa, tabla_ataque):
        for fila_defensa, fila_ataque in zip(tabla_defensa, tabla_ataque):
            for celda_defensa, celda_ataque in zip(fila_defensa, fila_ataque):
                if celda_defensa == "X" and celda_ataque != "X":
                    return False
        return True

    def game_on(self):
        while True:
            self.atacar(self.nombre_jugador1, self.tabla_defensa_jugador2, self.tabla_ataque_jugador1)
            if self.game_win(self.tabla_defensa_jugador2, self.tabla_ataque_jugador1):
                print(f"¡Felicidades {self.nombre_jugador1}, has ganado el juego!")
                break

            self.atacar(self.nombre_jugador2, self.tabla_defensa_jugador1, self.tabla_ataque_jugador2)
            if self.game_win(self.tabla_defensa_jugador1, self.tabla_ataque_jugador2):
                print(f"¡Felicidades {self.nombre_jugador2}, has ganado el juego!")
                break  # Terminar el juego
