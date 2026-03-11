#!/usr/bin/env python3

from io import TextIOWrapper


def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    classified_data: TextIOWrapper
    security_protocols: TextIOWrapper
    try:
        print("Initiating secure vault access...")
        with (
            open("classified_data.txt") as classified_data,
            open("security_protocols.txt") as security_protocols
        ):
            print("Vault connection established with failsafe protocols")

            print("\nSECURE EXTRACTION:")
            classified_data_content = classified_data.read()
            print(classified_data_content)

            print("\nSECURE PRESERVATION:")
            security_protocols_content = security_protocols.read()
            print(security_protocols_content)
    except FileNotFoundError as err:
        print(err)
        raise err
    if (
        classified_data and security_protocols is not None
        and classified_data.closed
        and security_protocols.closed
    ):
        print("Vault automatically sealed upon completion")
    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("An unhandled exception occured:", error)
        print("Exiting...")
