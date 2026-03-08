def ping_pong(sounds):
    # Your code here!
    working_list = sounds.split('-')
    score_mr_ping = 0
    score_mr_pong = 0
    current_server = None
    last_hitter = None
    last_rally_winner = None

    for hit in working_list:
        if not hit == "ping" or not hit == "pong":
            continue
        

    return "ping"  # or "pong"