import journal_pb2
import sys
import time


def main() -> None:
    journal: journal_pb2.JournalEntry = journal_pb2.JournalEntry()
    journal.time = int(time.time())
    journal.message = ' '.join(sys.argv[1:])

    byte_vec: bytes = bytes(journal.SerializeToString())
    sys.stdout.buffer.write(byte_vec)


if __name__ == '__main__':
    main()
