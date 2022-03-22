def isMatch(s: str, p: str) -> bool:
    dp = {}

    def dp_match(i, j):
        # if p = '' and s = '' then they are a match. This is expected to serve as a base case for a series of recursive calls of dp_match
        if (i, j) not in dp:
            if j == len(p):
                ans = i == len(s)
            else:
                first_match = i < len(s) and p[j] in {s[i], '.'}
                if j + 1 < len(p)  and p[j+1] == "*":
                    # if(first_match):
                    #     print(p[j])
                    ans = dp_match(i, j+2) or first_match and dp_match(i+1, j)
                else:
                    ans = first_match and dp_match(i+1, j+1)

            dp[i, j] = ans

        return dp[i, j]

    return dp_match(0, 0)



if __name__ == '__main__':
    print(isMatch("aa", "a*"))
    # print(isMatch("match", "......"))
