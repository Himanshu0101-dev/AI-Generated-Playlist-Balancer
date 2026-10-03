def playlist_balancer(songs, T):
    n = len(songs)
    dp = [[0]*(T+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        dur, mood = songs[i-1]
        for t in range(T+1):
            dp[i][t] = dp[i-1][t]
            if t >= dur:
                dp[i][t] = max(dp[i][t], dp[i-1][t-dur] + mood)
    
    # Backtrack to find chosen songs
    res_mood = dp[n][T]
    chosen = []
    t = T
    for i in range(n, 0, -1):
        if dp[i][t] != dp[i-1][t]:
            dur, mood = songs[i-1]
            chosen.append(i)
            t -= dur
    
    return res_mood, chosen[::-1]

# Example
songs = [(4,6),(3,-2),(5,7),(2,3),(6,5)]
T = 10
print(playlist_balancer(songs, T))
