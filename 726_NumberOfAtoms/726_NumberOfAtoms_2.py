class Solution:
    def countOfAtoms(self, formula: str) -> str:
        '''
        Stack + Hashmap. Reverse Order.
        '''
        dict = {}
        m = [1]
        digit = '' 
        lower = ''
        
        for i in range(len(formula)-1, -1, -1):
            element = formula[i] + lower
            if element.isdigit():
                digit = element + digit                                    # 1
                continue
            elif element.islower():
                lower = element
                continue
            elif element == ')':
                m.append(m[-1] * int(digit or 1))                          # 2
                digit = ''
                continue
            elif element == '(':
                m.pop()
                continue
            dict[element] = dict.get(element, 0) + m[-1]*int(digit or 1)   # 3
            digit = ''
            lower = ''

        output = ''
        for key, value in sorted(dict.items()):
            if value == 1:
                value = ''
            output = output + key + str(value)
        return output
    
    # TC: O(nlogn)
    # as sort() takes O(nlogn) time. Scan the string takes O(n).
    
    # SC: O(n)
    # space taken by dict()
    
    # 1. This + is due with when the number is bigger than 9
    # 2. This digit or 1 is to deal with the cases like '(H)' where there is no number after ')'.
    # 3. This m[-1]*int(digit or 1) is to deal with the number with no ')' in front of it. As in
    #    this case, the digit wont be pushed to the m stack. 
