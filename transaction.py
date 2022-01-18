from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass(frozen=True, eq=True, unsafe_hash=True)
class Transaction:
    source_address: str
    destination_address: str
    amount: int
    fee: int
