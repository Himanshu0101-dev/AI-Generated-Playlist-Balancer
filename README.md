# AI-Generated-Playlist-Balancer
Problem Statement:  
You are given a list of songs, each with two attributes:

Duration (in minutes)

Mood score (integer, can be positive or negative)

Your task is to create a playlist such that:

The total duration does not exceed a given limit T.

The sum of mood scores is maximized.

If multiple playlists achieve the same mood score, choose the one with the shortest total duration.

Return the maximum mood score achievable and the corresponding playlist (list of song indices).


Input Format:

First line: N T → number of songs, maximum duration

Next N lines: duration mood_score

Output Format:

First line: maximum mood score

Second line: indices of songs chosen (space-separated, 1-based indexing)
