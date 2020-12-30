class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        if len(strs) == 0:
            return chr(258)
        return chr(257).join(x for x in strs)

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        if s == chr(258): return []
        return s.split(chr(257))
    
    # TC: O(n)
    # for both encode and decode. n is the number of stings in the input array
    
    # SC: O(n) for both encode and decode
    
    # unichr is used before python 3.1. In higher version, just use chr()


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
