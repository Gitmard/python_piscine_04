#!/usr/bin/env python3

from io import TextIOWrapper


def main() -> None:
    discovery_file: TextIOWrapper | None = None

    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print("Initializing new storage unit: new_discovery.txt")

    discovery_file = open("../new_discovery.txt", mode="w")
    discovery_file.write("[ENTRY 001] New quantum algorithm discovered\n")
    discovery_file.write("[ENTRY 002] Efficiency increased by 347%\n")
    discovery_file.write(
        "[ENTRY 003] Archived by Data Archivist trainee\n"
    )

    discovery_file = open("../new_discovery.txt", mode="r")
    print(discovery_file.read())

    print("Data inscription complete. Storage unit sealed.")
    discovery_file.close()
    print("Archive 'new_discovery.txt' ready for long-term preservation")


if __name__ == "__main__":
    main()
