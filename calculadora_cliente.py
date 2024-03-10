import socket
import pickle

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5000))

    # Solicitar al usuario que ingrese números y la operación
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))
    operacion = input("Ingrese la operación (suma, resta, multiplicacion, division): ")

    # Empaquetar los datos en un diccionario
    client_data = {'numero1': numero1, 'numero2': numero2, 'operacion': operacion}

    # Enviar los datos al servidor
    client_socket.send(pickle.dumps(client_data))

    # Esperar antes de cerrar el programa
    input("Presione Enter para salir.")

    client_socket.close()

if __name__ == "__main__":
    main()
