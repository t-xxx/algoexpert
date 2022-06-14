def minimumWaitingTime(queries):
    queries.sort()

    tortaltime = 0
    for idx, duration in enumerate(queries[:-1]):
        queriesLeft = len(queries) - (idx + 1)
        tortaltime += duration * queriesLeft
    return tortaltime
