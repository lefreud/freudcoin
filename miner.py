from block import Block
from blockchain import Blockchain
from transaction import Transaction
from typing import *
from node import Node
import socket
from protocol import *

RECEIVE_BUFFER_SIZE = 5  # 1024


class Miner(Node):
    def __init__(self):
        super().__init__()
        self._pending_transactions = set()
        self._tentative_block = None
        self._blockchain = Blockchain()
        self._server = None

    def append_block(self, block: Block):
        self._blockchain.append(block)
        self._pending_transactions.difference_update(block.transactions)

    def add_transaction(self, transaction: Transaction):
        self._pending_transactions.add(transaction)

    def start(self):
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server.bind(("127.0.0.1", self._possible_ports[0]))
        self._server.listen(5)
        while True:
            client_socket, address = self._server.accept()
            packet_length = int(client_socket.recv(PACKET_LENGTH_HEADER_SIZE).decode("utf-8"))
            packet = bytes()
            while len(packet) < packet_length:
                packet += client_socket.recv(RECEIVE_BUFFER_SIZE)
            print(packet.decode("utf-8"))
            client_socket.close()


