#!/usr/bin/env python3

from io import TextIOWrapper


def main() -> None:
    discovery_file: TextIOWrapper | None = None
    write_success: bool = False

    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    data_to_write: list[str] = [
        "[ENTRY 001] New quantum algorithm discovered\n",
        "[ENTRY 002] Efficiency increased by 347%\n",
        "[ENTRY 003] Archived by Data Archivist trainee\n"
    ]

    try:
        print("Initializing new storage unit: new_discovery.txt")
        discovery_file = open("new_discovery.txt", mode="w")
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        for line in data_to_write:
            discovery_file.write(line)
            print(line, end="")
        write_success = True
    except Exception as err:
        raise err
    finally:
        discovery_file.close()
        if not write_success:
            print("\nData inscription failed. Storage unit sealed.")
        else:
            print("\nData inscription complete. Storage unit sealed.")
            print(
                "Archive 'new_discovery.txt' ready for long-term",
                "preservation"
            )


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("Unkown critical error, the matrix is compromised!\n", error)
        print("Aborting...")
