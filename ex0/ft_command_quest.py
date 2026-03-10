#!/usr/bin/env python3

def main() -> None:
    fragments_file = None
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    try:
        try:
            print("\nAccessing Storage Vault: ancient_fragment.txt")
            fragments_file = open("../ancient_fragment.txt")
            print("Connection established...\n")
        except FileNotFoundError as err:
            print("ERROR: Storage vault not found.")
            raise err
        print(fragments_file.read())
    except Exception as err:
        raise err
    finally:
        if fragments_file is not None:
            fragments_file.close()
            print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    main()
