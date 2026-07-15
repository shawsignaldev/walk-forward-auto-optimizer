def windows(length: int, train: int, test: int, step: int) -> list[tuple[int, int, int, int]]:
    if min(length, train, test, step) <= 0:
        raise ValueError("all inputs must be positive")
    result: list[tuple[int, int, int, int]] = []
    start = 0
    while start + train + test <= length:
        result.append((start, start + train, start + train, start + train + test))
        start += step
    return result

def best_param(scores: dict[str, float]) -> str:
    if not scores:
        raise ValueError("scores cannot be empty")
    return max(scores, key=scores.get)
