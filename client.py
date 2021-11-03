import socket
import ssl


HOST_NAME = "127.0.0.1"
PORT = 8443
MESSAGE_LEN = 1024
EXIT_CMD = "bye bye"


def main():
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    sock = socket.socket()
    connection = context.wrap_socket(sock, server_hostname=HOST_NAME)
    try:
        connection.connect((HOST_NAME, PORT))
        message = input("Please enter a command: ")
        while True:
            connection.send(message.encode())
            answer = connection.read(MESSAGE_LEN).decode()
            print(answer)
            if answer == EXIT_CMD:
                break
            message = input("Please enter a command: ")
        print("exiting...")
    except socket.error as sock_err:
        print(sock_err)
    finally:
        connection.close()


if __name__ == "__main__":
    main()
