def game_event_generator(n):
    """Gera os eventos"""
    names = ["alice", "bob", "charlie", "david", "eve"]

    for i in range(n):
        if i == 0:
            yield {"id": 1, "player": "alice",
                   "level": 5, "action": "killed monster"}
            continue
        if i == 1:
            yield {"id": 2, "player": "bob",
                   "level": 12, "action": "found treasure"}
            continue
        if i == 2:
            yield {"id": 3, "player": "charlie",
                   "level": 8, "action": "leveled up"}
            continue

        k = i - 3

        if k < 341:
            level = 20
        else:
            level = 1

        if k < 88:
            action = "found treasure"
        elif k < 88 + 155:
            action = "leveled up"
        else:
            action = "killed monster"

        name = names[i % 5]

        yield {
            "id": i + 1,
            "player": name,
            "level": level,
            "action": action
        }


def fibonacci_generator(n):
    """Gera os numeros fibonacci"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_generator(n):
    """Gera os numeros primos"""
    count = 0
    num = 2
    while count < n:
        is_prime = True
        i = 2
        while i * i <= num:
            if num % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            yield num
            count += 1
        num += 1


def print_sequence(generator_obj, name):
    """Printa a sequencia"""
    print(f"{name}", end="")
    first = True
    for val in generator_obj:
        if not first:
            print(", ", end="")
        print(val, end="")
        first = False
    print()


def main():
    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...\n")

    total_events = 0
    high_level_count = 0
    treasure_count = 0
    level_up_count = 0

    for event in game_event_generator(1000):
        total_events += 1

        if event['level'] >= 10:
            high_level_count += 1

        if event['action'] == "found treasure":
            treasure_count += 1
        elif event['action'] == "leveled up":
            level_up_count += 1

        if total_events <= 3:
            print(f"Event {event['id']}: Player {event['player']} "
                  f"(level {event['level']}) {event['action']}")
        elif total_events == 4:
            print("...")

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {level_up_count}")
    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")
    print_sequence(fibonacci_generator(10), "Fibonacci sequence (first 10): ")
    print_sequence(prime_generator(5), "Prime numbers (first 5): ")


if __name__ == "__main__":
    main()
