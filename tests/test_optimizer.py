from walk_forward_auto_optimizer.optimizer import best_param, windows

def test_windows_builds_train_test_ranges() -> None:
    assert windows(length=20, train=10, test=5, step=5) == [(0, 10, 10, 15), (5, 15, 15, 20)]

def test_best_param_returns_highest_score() -> None:
    assert best_param({"fast": 1.2, "slow": 0.8}) == "fast"
