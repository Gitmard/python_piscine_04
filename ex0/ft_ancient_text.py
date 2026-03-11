#!/usr/bin/env python3

from io import TextIOWrapper


def main() -> None:
    fragments_file: TextIOWrapper | None = None
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    try:
        try:
            print("\nAccessing Storage Vault: ancient_fragment.txt")
            fragments_file = open("ancient_fragment.txt")
            print("Connection established...\n")
        except FileNotFoundError as err:
            print("ERROR: Storage vault not found.")
            raise err
        print("RECOVERED DATA:")
        print(fragments_file.read())
    finally:
        if fragments_file is not None:
            fragments_file.close()
            print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("Unkown critical error, the matrix is compromised!\n", error)
        print("Aborting...")
