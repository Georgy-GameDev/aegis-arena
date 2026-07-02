MAX_SCORE_PER_SECOND = 15


def validate_score(score: int, match_duration_seconds: int) -> tuple[bool, str]:
    '''
    MVP validation.

    This does not replace a real server-authoritative game loop.
    It only prevents obviously impossible leaderboard submissions.
    '''

    if score < 0:
        return False, "negative_score"

    max_allowed_score = match_duration_seconds * MAX_SCORE_PER_SECOND

    if score > max_allowed_score:
        return False, "score_exceeds_possible_rate"

    return True, "accepted"
