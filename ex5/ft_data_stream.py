import time
import random


def game_event_generator(n):
    """Gera eventos de jogo aleatorios usando yield. """
    names = ["alice", "bob", "charlie", "david", "eve"]
    actions = ["killed monster", "found treasure", "leveled up"]

    for i in range(n):
        name = names[random.randint(0, len(names) - 1)]
        level = random.randint(1, 20)
        action = actions[random.randint(0, len(actions) - 1)]
        yield {
            "id": i + 1,
            "player": name,
            "level": level,
            "action": action
        }


def fibonacci_generator(n):
    """Gera os primeiros numeros de Fibonacci."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_generator(n):
    """Gera os primeiros numeros primos."""
    count = 0
    num = 2
    while count < n:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            count += 1
        num += 1


def main():
    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...\n")

    total_events = 0
    high_level_count = 0
    treasure_count = 0
    level_up_count = 0

    start_time = time.time()

    for event in game_event_generator(1000):
        total_events += 1

        if event['level'] >= 10:
            high_level_count += 1

        if event['action'] == "found treasure":
            treasure_count += 1
        elif event['action'] == "leveled up":
            level_up_count += 1

        if total_events <= 3:
            print(f"Event {event['id']}: Player {event['player']}"
                  f"(level {event['level']}) {event['action']}")
        elif total_events == 4:
            print("...")

    end_time = time.time()
    duration = end_time - start_time

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {level_up_count}\n")
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {duration:.3f} seconds")

    print("\n=== Generator Demonstration ===")

    fib_list = list(fibonacci_generator(10))

    fib_str = ", ".join(str(x) for x in fib_list)
    print(f"Fibonacci sequence (first 10): {fib_str}")

    prime_list = list(prime_generator(5))
    prime_str = ", ".join(str(x) for x in prime_list)
    print(f"Prime numbers (first 5): {prime_str}")


if __name__ == "__main__":
    main()
