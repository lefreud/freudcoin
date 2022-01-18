from block import Block
from blockchain import Blockchain
from transaction import Transaction
from typing import *
from node import Node
import socket
from protocol import *
import threading
import logging
import time

RECEIVE_BUFFER_SIZE = 5  # 1024
MAX_NONCE = 2**64 - 1


class Miner(Node):
    def __init__(self):
        super().__init__()
        self._pending_transactions = []
        self._blockchain = Blockchain()
        self._server = None
        self._miner_thread = threading.Thread(target=self._mine)
        self._server_thread = threading.Thread(target=self._serve)

    def start(self):
        self._miner_thread.start()
        self._server_thread.start()

    def _mine(self):
        logging.info("Starting miner thread")
        nonce = 0
        while True:
            last_block = self._blockchain.last_block
            tentative_block = Block(
                index=last_block.index+1,
                timestamp=int(time.time()),
                transactions=list(self._pending_transactions),
                nonce=nonce,
                previous_hash=last_block.hash
            )
            if tentative_block.hash.startswith(self._blockchain.difficulty * "0"):
                logging.info(f"Found valid hash {tentative_block.hash}! Broadcasting...")
                # TODO: broadcast
                logging.debug(tentative_block.to_json())
                self._blockchain.append(tentative_block)
                self._pending_transactions.clear()
            nonce = (nonce + 1) % MAX_NONCE
            time.sleep(0)

    def _serve(self):
        logging.info("Starting server thread")
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server.bind(("127.0.0.1", self._possible_ports[1]))
        self._server.listen(5)
        while True:
            client_socket, address = self._server.accept()
            packet_length = int(client_socket.recv(PACKET_LENGTH_HEADER_SIZE).decode("utf-8"))
            packet = bytes()
            while len(packet) < packet_length:
                packet += client_socket.recv(RECEIVE_BUFFER_SIZE)
            client_socket.close()
            self._handle_packet(packet)
            time.sleep(0)

    def _handle_packet(self, packet):
        message = packet_to_message(packet)
        if message.type == "transaction":
            self._add_transaction(message.unconfirmed_transaction)
        else:
            self._append_block(message.block)

    def _append_block(self, block: Block):
        logging.debug(f"Adding block {block}")
        self._blockchain.append(block)
        # TODO: self._pending_transactions.difference_update(block.transactions)

    def _add_transaction(self, transaction: Transaction):
        logging.debug(f"Adding unconfirmed tx {transaction}")
        self._pending_transactions.append(transaction)
