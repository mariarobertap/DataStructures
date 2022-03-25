
def jumpingOnClouds(c):
    i = count_jumps = 0
    length = len(c)

    while i < length - 2:
        if c[i+2] == 1:
            i += 1
        else:
            i += 2
        count_jumps += 1

    if i == length - 2:
        count_jumps += 1

    return count_jumps


#https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen