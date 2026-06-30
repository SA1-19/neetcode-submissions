class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            # append the length of the word
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        """
        Read the length before #
        Jump past #
        Read exactly that many characters
        Repeat
        """
        # i = start of encoded chunk
        # j = used to findd where length ends so # position
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            # this retrieves the number
            length = int(s[i:j])
            # move i to the start of the actual word
            i = j+1
            j = i+length
            # appends the word
            res.append(s[i:j])
            # move to next chunk
            i = j
        return res


