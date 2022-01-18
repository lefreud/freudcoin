import json
from typing import *
from transaction import Transaction
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from block import Block


PACKET_LENGTH_HEADER_SIZE = 8


@dataclass_json
@dataclass
class Message:
    type: str
    block: Optional[Block]
    unconfirmed_transaction: Optional[Transaction]


def message_to_packet(message: Message) -> bytes:
    message_str = message.to_json()
    packet = f"{len(message_str):0{PACKET_LENGTH_HEADER_SIZE}}{message_str}"
    return packet.encode("utf-8")


def packet_to_message(packet: bytes) -> Message:
    return Message.from_json(packet.decode("utf-8"))
