from block import Block
from blockchain import Blockchain
from miner import Miner
import logging

logging.basicConfig(level=logging.DEBUG)


def main():
    miner_node = Miner()
    miner_node.start()


if __name__ == '__main__':
    main()
