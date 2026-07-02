from app.services.score_validation import validate_score


def test_valid_score_is_accepted():
    is_valid, reason = validate_score(
        score=100,
        match_duration_seconds=30,
    )

    assert is_valid is True
    assert reason == "accepted"


def test_impossible_score_is_rejected():
    is_valid, reason = validate_score(
        score=99999,
        match_duration_seconds=10,
    )

    assert is_valid is False
    assert reason == "score_exceeds_possible_rate"


def test_negative_score_is_rejected():
    is_valid, reason = validate_score(
        score=-1,
        match_duration_seconds=30,
    )

    assert is_valid is False
    assert reason == "negative_score"