from game import game_performance

def test_low_performance():
    assert game_performance(20) == "LOW PERFORMANCE"

def test_moderate_performance():
    assert game_performance(45) == "MODERATE PERFORMANCE"

def test_smooth_gameplay():
    assert game_performance(75) == "SMOOTH GAMEPLAY"