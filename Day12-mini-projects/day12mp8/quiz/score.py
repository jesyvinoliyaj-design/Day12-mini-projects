def calculate_score(results: list[bool]) -> int:
    return sum(1 for r in results if r)

def display_score(results: list[bool]) -> None:
    print(f"\nYour Score: {calculate_score(results)} / {len(results)}")
