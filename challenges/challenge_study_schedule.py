def study_schedule(permanence_period, target_time):
    counter = 0

    if target_time is None:
        return None

    for entry, exit in permanence_period:
        if (isinstance(entry, int) and isinstance(exit, int)):
            if entry <= target_time and exit >= target_time:
                counter += 1
        else:
            return None

    return counter
