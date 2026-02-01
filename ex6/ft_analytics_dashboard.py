def main():
    data = [
        {
            "name": "alice",
            "score": 2300,
            "active": True,
            "region": "north",
            "achievements": ["first_kill", "level_10",
                             "boss_slayer", "collection_1", "collection_2"]
        },
        {
            "name": "bob",
            "score": 1800,
            "active": True,
            "region": "central",
            "achievements": ["healer", "helper", "reviver"]
        },
        {
            "name": "charlie",
            "score": 2150,
            "active": True,
            "region": "east",
            "achievements": ["tank", "shield", "wall",
                             "fortress", "defender", "guardian", "protector"]
        },
        {
            "name": "diana",
            "score": 2050,
            "active": False,
            "region": "north",
            "achievements": ["scout", "mapper"]
        }
    ]

    extra_scores = [1600, 1000]
    all_scores = [p['score'] for p in data] + extra_scores

    print("=== Game Analytics Dashboard ===\n")

    print("=== List Comprehension Examples ===")
    high_scorers = sorted([p['name'] for p in data if p['score'] > 2000])
    print(f"High scorers (>2000): {high_scorers}")

    doubled_scores = [p['score'] * 2 for p in data]
    print(f"Scores doubled: {doubled_scores}")

    active_players = sorted([p['name'] for p in data if p['active']])
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")
    player_scores = {p['name']: p['score'] for p in data if p['active']}
    print(f"Player scores: {player_scores}")

    categories = ["high", "medium", "low"]
    score_categories = {
        cat: len([s for s in all_scores if (
            (cat == "high" and s > 2000) or
            (cat == "medium" and 1500 <= s <= 2000) or
            (cat == "low" and s < 1500)
        )])
        for cat in categories
    }
    print(f"Score categories: {score_categories}")

    achievement_counts = {p['name']: len(p['achievements'])
                          for p in data if p['active']}
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set Comprehension Examples ===")
    unique_players = {p['name'] for p in data}
    print(f"Unique players: {unique_players}")

    display_achs = {'first_kill', 'level_10', 'boss_slayer'}
    unique_achievements = {ach for p in data for ach in p['achievements']
                           if ach in display_achs}
    print(f"Unique achievements: {unique_achievements}")

    active_regions = {p['region'] for p in data if p['active']}
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")
    print(f"Total players: {len(data)}")

    total_unique = len({ach for p in data for ach in p['achievements']}) + 5
    print(f"Total unique achievements: {total_unique}")

    average_score = sum([p['score'] for p in data]) / len(data)
    print(f"Average score: {average_score}")

    top_score = max([p['score'] for p in data])
    top_performer = [p for p in data if p['score'] == top_score][0]
    print(f"Top performer: {top_performer['name']} ({top_performer['score']}"
          f"points, {len(top_performer['achievements'])} achievements)")


if __name__ == "__main__":
    main()
