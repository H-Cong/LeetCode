class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        for i in range(len(chars)-1,-1,-1):
            if i and chars[i]==chars[i-1]:
                count += 1
                chars.pop(i)
            else:
                if count>1:
                    for item in str(count)[::-1]:
                        chars.insert(i+1, item)
                    count = 1
    
    # TC: O(n)
    
    # SC: O(1)
    
    # reverse str(count) is because the insert function always pointing to i+1 index
    # e.g. if count = 12, then we first insert 2 at i+1 position
    # then we insert 1 at i+1 position, this insertion will also push previously inserted
    # 2 to the i+2 position
