import socket
import threading

# Configuración del servidor
HOST = '127.0.0.1'  # Dirección IP del servidor (localhost)
TCP_PORT = 65432     # Puerto para el servidor TCP
UDP_PORT = 65433     # Puerto para el servidor UDP

def handle_tcp_client(conn, addr):
    """ Manejo de clientes TCP """
    print(f"Conexión TCP establecida con {addr}")
    while True:
        data = conn.recv(1024).decode()  # Recibir mensaje
        if not data or data.lower() == 'exit':  # Si recibe "exit", cerrar conexión
            print(f"Conexión TCP cerrada con {addr}")
            break
        print(f"[TCP] Recibido de {addr}: {data}")
        conn.sendall(f"Servidor TCP recibió: {data}".encode())  # Responder al cliente
    conn.close()

def tcp_server():
    """ Servidor TCP """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Crear socket TCP
    server.bind((HOST, TCP_PORT))  # Asignar IP y puerto
    server.listen()  # Escuchar conexiones
    print("Servidor TCP esperando conexiones...")
    
    while True:
        conn, addr = server.accept()  # Aceptar conexión
        threading.Thread(target=handle_tcp_client, args=(conn, addr)).start()  # Crear hilo para cliente

def udp_server():
    """ Servidor UDP """
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Crear socket UDP
    server.bind((HOST, UDP_PORT))  # Asignar IP y puerto
    print("Servidor UDP esperando mensajes...")

    while True:
        data, addr = server.recvfrom(1024)  # Recibir mensaje
        message = data.decode()
        if message.lower() == 'exit':  # Si recibe "exit", cerrar conexión
            print(f"Servidor UDP cerrando conexión con {addr}")
            break
        print(f"[UDP] Recibido de {addr}: {message}")
        server.sendto(f"Servidor UDP recibió: {message}".encode(), addr)  # Responder al cliente

# Crear hilos para los servidores
tcp_thread = threading.Thread(target=tcp_server)
udp_thread = threading.Thread(target=udp_server)

# Iniciar los servidores
tcp_thread.start()
udp_thread.start()
