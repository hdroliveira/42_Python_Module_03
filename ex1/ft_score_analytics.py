import sys


def process_scores(ac: list) -> None:
    """Processa uma lista de strings, converte para inteiros
    e calcula estatisticas"""
    scores = []

    for arg in ac:
        try:
            score = int(arg)
            scores.append(score)
        except ValueError:
            pass
    if not scores:
        print("No scores provided. Usage: python3 "
              " ft_score_analytics.py <score1> <score2>...")
        return

    total_players = len(scores)
    total_score = sum(scores)
    average_score = total_score / total_players
    high_score = max(scores)
    low_score = min(scores)
    score_range = high_score - low_score

    print(f"Scores processed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score:.1f}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")


def main() -> None:
    print("=== Player Score Analytics ===")

    if len(sys.argv) < 2:
        print("No scores provided. Usage: python3 "
              " ft_score_analytics.py <score1> <score2>...")
    else:
        process_scores(sys.argv[1:])


if __name__ == "__main__":
    main()
