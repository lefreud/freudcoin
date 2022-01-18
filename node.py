from blockchain import Blockchain
from block import Block


# NODE_CLASSES = {
#     "miner": Miner
# }


PEER_LIST = [
    "127.0.0.1:9000",
    "127.0.0.1:9001",
    "127.0.0.1:9002"
]

POSSIBLE_PORTS = [
    9000, 9001, 9002
]



def broadcast_block(block: Block):
    # TODO
    print(f"Broadcasting block... {block}")


class Node:
    def __init__(self):
        self._peer_list = PEER_LIST
        self._possible_ports = POSSIBLE_PORTS
        self._broadcast_callback = broadcast_block

    def start(self):
        raise NotImplementedError


# def create_node(*, node_type):
#     return NODE_CLASSES[node_type]()
