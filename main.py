import sys
from dataclasses import dataclass
from datetime import datetime
from typing import IO, List

START_BYTE = 2
END_BYTE = 3


@dataclass
class LogEntry:
    # I think this is local time?
    timestamp: datetime
    chat_filter: int
    channel: int
    _filler: bytes
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

        return bs.decode("utf-8", "ignore")


def read_int(stream: IO):
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


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("USAGE: python3 main.py path_to_logfile")
        print("EXAMPLE: python3 main.py 'C:/Users/<user>/Documents/My Games/FINAL FANTASY XIV - A Realm Reborn/FFXIV_CHR0040002E933EB474/log/00000000.log'")
        sys.exit(1)

    entries: List[LogEntry] = []

    with open(sys.argv[1], "rb") as f:
        body_len = read_int(f)
        file_len = read_int(f)
        entry_count = file_len - body_len

        print(f"body_len: {body_len}")
        print(f"file_len: {file_len}")
        print(f"entry_count: {entry_count}")

        offsets = [read_int(f) for _ in range(entry_count)]

        prev_offset = 0
        for i in range(entry_count):
            body_size = offsets[i] - prev_offset - 10
            timestamp = read_int(f)
            chat_filter = f.read(1)[0]
            channel = f.read(1)[0]
            filler = f.read(4)  # 00 00 1F 1F
            body = f.read(body_size)
            # parsed_body = parse_body(body)

            entries.append(LogEntry(datetime.fromtimestamp(
                timestamp), chat_filter, channel, filler, body))

            prev_offset = offsets[i]

    # Print all entries as (mostly) plain text
    for entry in entries:
        print(f"{entry.timestamp} {entry.body_txt}")
