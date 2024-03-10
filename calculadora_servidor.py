import socket
import pickle
import time

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5000))
    server_socket.listen(5)

    print("Esperando conexiones...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Cliente conectado desde {client_address}")

        data = client_socket.recv(1024)
        client_data = pickle.loads(data)

        numero1 = client_data['numero1']
        numero2 = client_data['numero2']
        operacion = client_data['operacion']

        resultado = 0

        # Realizar la operación según lo solicitado
        if operacion == "suma":
            resultado = numero1 + numero2
        elif operacion == "resta":
            resultado = numero1 - numero2
        elif operacion == "multiplicacion":
            resultado = numero1 * numero2
        elif operacion == "division":
            if numero2 != 0:
                resultado = numero1 / numero2
            else:
                resultado = float('nan')  # Manejar división por cero

        # Enviar el resultado al cliente
        response = {'resultado': resultado}
        client_socket.send(pickle.dumps(response))

        # Esperar un breve retraso antes de cerrar la conexión
        time.sleep(1)
        client_socket.close()

if __name__ == "__main__":
    main()
