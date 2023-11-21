import sys
from dataclasses import dataclass
from datetime import datetime
from typing import BinaryIO, List

START_BYTE = 2
END_BYTE = 3


@dataclass
class LogEntry:
    # I think this is local time?
    timestamp: datetime
    chat_filter: int
    channel: int
    body: bytes

    @property
    def body_txt(self):
        bs = bytearray()

        # Filter most of the chat tokens.
        skip = False
        for b in self.body:
            if skip:
                if b == END_BYTE:
                    skip = False
            else:
                if b == START_BYTE:
                    skip = True
                else:
                    bs.append(b)

        # If the message has a 'sender' it happens before the second 1F.
        # If no sender we can just remove the leading 1F, otherwise turn the 1F into a colon for prettiness.
        if bs.startswith(b'\x1f'):
            bs = bs[1:]
        else:
            bs = bs.replace(b'\x1f', b': ')

        return bs.decode("utf-8", "ignore")


def read_int(stream: BinaryIO):
    return int.from_bytes(stream.read(4), "little")


# TODO: Implement this
def parse_body(body: bytes):
    # 20 20 E3 80 8B 20 =    ã€‹ Allagan Tools v1.6.2.0 loaded.
    # 20 20 E2 98 80 20 = '~~snip~~  Chill Vibes with DJs xxxx, xxxx, xxxx â˜€  RP bar â˜€ 6PMîƒ‘ â˜€  Chaos - Spriggan - LB- xx -xx  â˜€ discord.gg/xxxx â˜€ twitch.tv/xxxx
    # 20 20 EE 81 AF 20 = xxxx[PriceCheck] xxxxxxxŒgxxxx î�¯ xxxled to process itemxxx
    #
    # 20 20 ? ? ? 20 = The pattern?
    #
    # https://github.com/goatcorp/Dalamud/blob/master/Dalamud/Game/Text/SeStringHandling/Payloads/ItemPayload.cs#L234
    # https://github.com/goatcorp/Dalamud/blob/c7fc943692c27750df0d720fe2bddefbb75ebfed/Dalamud/Game/Text/SeStringHandling/Payload.cs#L251C42-L251C42

    parts = []
    # for i in range(len(body)):
    #     parts.append(body[i])

    return parts


def parse_entries(stream: BinaryIO) -> List[LogEntry]:
    entries = []

    body_len = read_int(stream)
    file_len = read_int(stream)
    entry_count = file_len - body_len

    print(f"body_len: {body_len}")
    print(f"file_len: {file_len}")
    print(f"entry_count: {entry_count}")

    offsets = [read_int(stream) for _ in range(entry_count)]

    prev_offset = 0
    for i in range(entry_count):
        body_len = offsets[i] - prev_offset

        # The full body is delimited by 2x `0x1F`, the sender can be empty (zero bytes).
        # timestamp chat_filter channel zero 0x1F sender 0x1F message

        timestamp = read_int(stream)  # 4 bytes
        chat_filter = stream.read(1)[0]  # 1 byte
        channel = stream.read(1)[0]  # 1 byte
        zero_and_delim = stream.read(3)  # 3 bytes
        # summed together = 9 bytes

        rest_of_body_len = body_len - 9
        body = stream.read(rest_of_body_len)
        # parsed_body = parse_body(body)

        entries.append(LogEntry(datetime.fromtimestamp(
            timestamp), chat_filter, channel, body))

        prev_offset = offsets[i]

    return entries


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("USAGE: python3 main.py path_to_logfile")
        print("EXAMPLE: python3 main.py 'C:/Users/<user>/Documents/My Games/FINAL FANTASY XIV - A Realm Reborn/FFXIV_CHR0040002E933EB474/log/00000000.log'")
        sys.exit(1)

    with open(sys.argv[1], "rb") as f:
        entries = parse_entries(f)

    # Print all entries as (mostly) plain text
    for entry in entries:
        print(f"{entry.timestamp} {entry.body_txt}")
