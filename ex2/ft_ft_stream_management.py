#!/usr/bin/env python3

import sys


def write_stdout(message: str, prefix: str = "\n") -> None:
    print(f"{prefix}[STANDARD] {message}")


def write_stderr(message: str, prefix: str = "\n") -> None:
    print(f"{prefix}[ALERT] {message}", file=sys.stderr)


def read_stdin(message: str) -> str:
    return input(message)


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    arch_id = read_stdin("Input Stream active. Enter archivist ID: ")
    status_report = read_stdin("Input Stream active. Enter status report: ")

    write_stdout(
        f"Archive status from {arch_id}: {status_report}",
        prefix="\n"
    )
    write_stderr("System diagnostic: Communication channels verified")
    write_stdout("Data transmission complete")

    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    main()
