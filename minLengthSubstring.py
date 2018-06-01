    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # create hash of desired symbols with counts of each X
        # from beginning of string, create window X
        # while whole string isn't processed: X
        #       check off symbols I'm looking for (decrement "missing" and count in hash table) X
        #       when missing is 0: X
        #           move up beginning of window to first desired symbol X
        #           check if a new minimum length substring is found X
        #           increment missing and count in hash table for current symbol X
        #           move up beginning of window to next desired symbol X
        # return minimum length substring
        # 0123456789012
        # ADOBECODEBANC   ABC
        #      ^    ^
        # missing = 0
        # curr_len = 6
        # min_length = 6
        # min_substr = "ADOBEC"
        # AAAAAAA    A
        # BBBA       A
        # AAAAAAA    ABC
        # ABSDGKAJ   AAB
        tmap = {}
        for char in t:
            tmap[char] = tmap.get(char, 0) + 1
        min_substr = ""
        min_length = float("inf")
        missing = len(t)
        start = 0
        for end in range(len(s)):
            if s[end] in tmap:
                if tmap[s[end]] > 0:
                    missing -= 1
                tmap[s[end]] -= 1
            if missing == 0:
     #           "cabwefgewcwaefgcf"
        #             ^      ^
    #           "cae"
                # if start not in tmap, shrink window to next desired symbol
                while start < end: 
                    if s[start] in tmap:
                    # check if the prefix has more instances of the desired symbol than we need
                        if tmap[s[start]] < 0:
                            tmap[s[start]] += 1
                        else:
                            break
                    start += 1
                # check for minlength substring
                curr_len = end - start + 1
                if curr_len < min_length:
                    min_length = curr_len
                    min_substr = s[start:end+1]
                    print(min_substr)
                # move on to the next desired symbol
                if s[start] in tmap:
                    tmap[s[start]] += 1
                    if tmap[s[start]] > 0:
                        missing += 1
                start += 1
                while start < end and s[start] not in tmap:
                    start += 1
        return min_substr 