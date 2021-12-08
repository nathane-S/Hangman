import hangman

def test_wrong_guess():
    game = hangman.Game("nathane")
    game.guess("l")
    assert game.state == "wrong_guess"

def test_right_guess():
    game = hangman.Game("nathane")
    game.guess("n")
    assert game.state == "right_guess"

def test_lose_game():
    game = hangman.Game("nathane")
    game.guess("z")
    assert game.state == "wrong_guess"
    game.guess("c")
    assert game.state == "wrong_guess"
    game.guess("d")
    assert game.state == "lose_game"

def test_win_game():
    game = hangman.Game("nathane")
    game.guess("n")
    game.guess("a")
    game.guess("t")
    game.guess("h")
    game.guess("e")
    assert game.state == "won_game"