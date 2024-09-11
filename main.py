
from battleshipgame import MesaJuego


def main():
    juego = MesaJuego()
    nombre_jugador1 = juego.nombre_jugador1
    nombre_jugador2 = juego.nombre_jugador2
    juego.tabla_defensa(juego.tabla_defensa_jugador1)
    juego.ubicar_barco_usuario(5, nombre_jugador1, juego.tabla_defensa_jugador1)
    juego.ubicar_barco_usuario(4, nombre_jugador1, juego.tabla_defensa_jugador1)
    juego.ubicar_barco_usuario(3, nombre_jugador1, juego.tabla_defensa_jugador1)
    juego.ubicar_barco_usuario(2, nombre_jugador1, juego.tabla_defensa_jugador1)

    # Limpiar la pantalla
    juego.limpiar_terminal()

    # Ubicación de barcos del Jugador 2
    juego.tabla_defensa(juego.tabla_defensa_jugador2)
    juego.ubicar_barco_usuario(5, nombre_jugador2, juego.tabla_defensa_jugador2)
    juego.ubicar_barco_usuario(4, nombre_jugador2, juego.tabla_defensa_jugador2)
    juego.ubicar_barco_usuario(3, nombre_jugador1, juego.tabla_defensa_jugador1)
    juego.ubicar_barco_usuario(2, nombre_jugador1, juego.tabla_defensa_jugador1)

    # Limpiar la pantalla
    juego.limpiar_terminal()

    # Iniciar el juego
    juego.game_on()


if __name__ == "__main__":
    main()

