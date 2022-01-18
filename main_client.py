import socket
from protocol import *


def get_packet(message: str):
    packet = f"{len(message):0{PACKET_LENGTH_HEADER_SIZE}}{message}"
    print(packet)
    return packet


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 9000))
    s.send(get_packet("yolo, yolo, swag").encode("utf-8"))
    s.close()


if __name__ == "__main__":
    main()
