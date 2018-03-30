
def partitionLabels(S):
    """
    :type S: str
    :rtype: List[int]
    """
    # make array of all letters
    # iterate backwards through list once making a note of the last index where that letter appears
    # iterate through list, chopping up string at characters with higher indices than previous
    # aldkhlrnskfdjhal
        arr = [-1 for i in range(26)]
        for j in range(len(S) - 1, -1, -1):
            currVal = ord(S[j]) - ord('a')
            #print(currVal)
            if arr[currVal] == -1:
                arr[currVal] = j
        result = []
        currStartIndex = 0
        currLastIndex = 0
        i = 0
        while i < len(S):
            letter = S[i]
            if i > currLastIndex:
                # reached letter after last index
                result.append(currLastIndex - currStartIndex + 1)
                currStartIndex = i
                currLastIndex = i
            elif arr[ord(letter) - ord('a')] > currLastIndex:
                # last index of this letter is greater than current span under consideration
                currLastIndex = arr[ord(letter) - ord('a')]
                print(currLastIndex)
                i += 1
            else:
                i += 1
        result.append(len(S) - currStartIndex)
        return result


print(partitionLabels("ababcdsd"))
