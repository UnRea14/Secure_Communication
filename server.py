import socket
import ssl


IP_ADDRESS = "0.0.0.0"
PORT = 8443
QUEUE_LEN = 1
PACKET_SIZE = 1024
CERT_FILE = "certificate.crt"
KEY_FILE = "privateKey.key"
MESSAGE = "have a nice day!"
EXIT_CMD = "exit"
EXIT_RES = "bye bye"


def main():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(CERT_FILE, KEY_FILE)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind((IP_ADDRESS, PORT))
        server_socket.listen(QUEUE_LEN)
        secure_sock = context.wrap_socket(server_socket, server_side=True)
        connection, address = secure_sock.accept()
        try:
            data = connection.recv(PACKET_SIZE).decode()
            while data != EXIT_CMD:
                print("received - " + data)
                connection.send(MESSAGE.encode())
                data = connection.recv(PACKET_SIZE).decode()
            connection.send(EXIT_RES.encode())
            print("exiting...")
        except socket.error as sock_err:
            print(sock_err)
        finally:
            connection.close()
    except socket.error as sock_err:
        print(sock_err)
    finally:
        server_socket.close()


if __name__ == "__main__":
    main()
