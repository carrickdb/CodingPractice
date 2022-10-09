# https://leetcode.com/problems/decode-ways/


def numDecodings(s: str) -> int:
    """
    dp[n] = dp[n+1] + dp[n+2]

    dp[len(s)-1] = 1
    """
    dp = [0 for i in range(len(s))]
    dp[len(s)-1] = s[-1] != '0'
    if len(s) < 2:
        return dp[0]
    if s[-2] == '0':
        dp[-2] = 0
    else:
        dp[-2] = (int(s[-2:]) < 27) + dp[-1]
    for i in range(len(s)-3, -1, -1):
        if s[i] != '0':
            dp[i] = dp[i+1]
            if int(s[i:i+2]) < 27:
                dp[i] += dp[i+2]
        else:
            dp[i] = 0
    return dp[0]

print(numDecodings("123"))

# def decodeVariations(S):
#   memos = {}
#
#   def decVars(S):
#     # Check if prefixes are valid
#     if len(S) <= 0:
#       return 1
#     if S[0] == '0':
#       return 0
#     if S[1:] not in memos:
#       numWays1 = decVars(S[1:])
#       memos[S[1:]] = numWays1
#     else:
#       numWays1 = memos[S[1:]]
#     numWays1 += 1
#     if len(S) > 1:
#
#       if S[2:] not in memos:
#         numWays2 = decVars(S[2:])
#         memos[S[2:]] = numWays2
#       else:
#         numWays2 = memos[S[2:]]
#       numWays1 += numWays2 + 1
#
#     return numWays1
#
#   return decVars(S)
