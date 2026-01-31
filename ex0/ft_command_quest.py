import sys


def main() -> None:
    """Recebe e apresenta os argumentos da linha de comando"""
    ac = sys.argv
    total_ac = len(ac)

    print("=== Command Quest ===")

    if total_ac == 1:
        print("No arguments provided!")
        print(f"Program name: {ac[0]}")
        print(f"Total arguments: {total_ac}")
    else:
        print(f"Program name: {ac[0]}")
        print(f"Arguments received: {total_ac-1}")

        i = 1
        while i < total_ac:
            print(f"Argument {i}: {ac[i]}")
            i += 1

        print(f"Total arguments: {total_ac}")


if __name__ == "__main__":
    main()
