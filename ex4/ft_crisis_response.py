#!/usr/bin/env python3

def read_archive_request(path: str) -> str:
    try:
        with open(path) as file:
            return f"RESPONSE: Archive recovered = ``{file.read()}``"
    except FileNotFoundError:
        return "RESPONSE: Archive not found in storage matrix"
    except PermissionError:
        return "RESPONSE: Security protocols deny access"
    except Exception:
        return "RESPONSE: Unkown critical error, the matrix is compromised!"


def write_archive_request(path: str, data: str) -> str:
    try:
        with open(path, mode="w") as f:
            f.write(data)
    except PermissionError:
        return "RESPONSE: Security protocols deny access"
    except Exception:
        return "RESPONSE: Unkown critical error, the matrix is compromised!"
    return "RESPONSE: Wrote data to archive"


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    print("\nCRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    print(read_archive_request("lost_archive.txt"))
    print("STATUS: Crisis handled, system stable")

    print("\nCRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    print(write_archive_request("classified_vault.txt", "classified data"))
    print("STATUS: Crisis handled, system stable")

    print("\nROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    print(read_archive_request("standard_archive.txt"))
    print("STATUS: Normal operations resumed")

    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
