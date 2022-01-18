from blockchain_exception import BlockchainException
from block import Block
from time import time
from dataclasses import dataclass, field


GENESIS_BLOCK_TIMESTAMP = 1642437904


@dataclass
class Blockchain:
    """
    Append-only data structure that maintains a consistent list of transactions and avoids double spends
    by using a Proof-of-Work mechanism (sha256-based).
    """

    blocks: list = field(init=False)
    difficulty: int = 2

    def __post_init__(self):
        self.blocks = []
        self._generate_genesis_block()

    def _generate_genesis_block(self):
        self.blocks.append(
            Block(0, GENESIS_BLOCK_TIMESTAMP, [], 0, "deadbeef")
        )

    @property
    def last_block(self) -> Block:
        if len(self.blocks) > 0:
            return self.blocks[0]
        raise BlockchainException("Genesis block not found!")

    def append(self, block: Block):
        if not block.previous_hash == self.last_block.hash:  # TODO: create full tree, not just a single linked list
            raise BlockchainException(f"The previous hash of the following block does not match the current head: {block}")
        if not block.hash.startswith("0" * self.difficulty):  # TODO: use binary zeros
            raise BlockchainException("The hash does not contain enough leading zeros")
        # TODO: if running full node, verify transactions coherence, i.e. all spenders have enough money
        self.blocks.append(block)
