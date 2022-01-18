import socket
from protocol import *


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 9001))
    message = Message(type="transaction", block=None, unconfirmed_transaction=Transaction(
        source_address="alice",
        destination_address="bob",
        amount=1999,
        fee=4
    ))
    s.send(message_to_packet(message))
    s.close()


if __name__ == "__main__":
    main()
