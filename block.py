from dataclasses import dataclass, field
from typing import *
import hashlib
import json
from transaction import Transaction


MAX_TRANSACTIONS_PER_BLOCK = 5


@dataclass
class Block:
    index: int
    timestamp: int
    transactions: List[Transaction]
    nonce: int
    previous_hash: str
    hash: str = field(init=False)

    @property
    def hash(self):
        return hashlib.sha256(json.dumps(self.__dict__).encode("utf-8")).hexdigest()

    @hash.setter
    def hash(self, _):
        pass

    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)
