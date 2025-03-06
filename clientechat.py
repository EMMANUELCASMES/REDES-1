import socket

# Configuración del cliente
HOST = '127.0.0.1'  # Dirección del servidor
TCP_PORT = 65432    # Puerto TCP
UDP_PORT = 65433    # Puerto UDP

def tcp_client():
    """ Cliente TCP """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Crear socket TCP
    client.connect((HOST, TCP_PORT))  # Conectar con el servidor TCP

    while True:
        message = input("Escribe un mensaje (TCP): ")
        client.sendall(message.encode())  # Enviar mensaje
        response = client.recv(1024).decode()  # Recibir respuesta
        print(f"Servidor TCP respondió: {response}")
        if message.lower() == 'exit':  # Finalizar si se envía "exit"
            break

    client.close()

def udp_client():
    """ Cliente UDP """
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Crear socket UDP

    while True:
        message = input("Escribe un mensaje (UDP): ")
        client.sendto(message.encode(), (HOST, UDP_PORT))  # Enviar mensaje
        response, _ = client.recvfrom(1024)  # Recibir respuesta
        print(f"Servidor UDP respondió: {response.decode()}")
        if message.lower() == 'exit':  # Finalizar si se envía "exit"
            break

# Menú de selección de protocolo
protocol = input("¿Quieres usar TCP o UDP? (tcp/udp): ").strip().lower()

if protocol == 'tcp':
    tcp_client()
elif protocol == 'udp':
    udp_client()
else:
    print("Protocolo no válido. Usa 'tcp' o 'udp'.")

