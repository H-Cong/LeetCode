class Solution:
    def countOfAtoms(self, formula: str) -> str:
        '''
        Recursive
        '''
        i = 0
        res = ''
        count_dict, _ = self.countHelper(formula, i)
        
        for atom, num in sorted(count_dict.items()):
            res += atom
            if num > 1:
                res += str(num)
        
        return res
    
    def countHelper(self, formula, i):
        count_dict = collections.defaultdict(int)
        
        while i < len(formula) and formula[i] != ')':
            if formula[i] == '(':
                sub_count_dict, i = self.countHelper(formula, i+1) # 2
                num_of_sub, i = self.getCount(formula, i)          # 3
                for k, v in sub_count_dict.items():
                    count_dict[k] += v * num_of_sub
            else:
                atom, i = self.getName(formula, i)
                num, i = self.getCount(formula, i)
                count_dict[atom] += num
        
        return count_dict, i + 1                                   # 4
    
    def getName(self, formula, i):
        atom = formula[i]
        i += 1
        while i < len(formula) and formula[i].islower():
            atom += formula[i]
            i += 1
        
        return atom, i
    
    def getCount(self, formula, i):
        num = 0
        while i < len(formula) and formula[i].isdigit():
            num = 10 * num + int(formula[i])                     # 1
            i += 1
        if num == 0:
            num = 1
        
        return num, i
    
    # TC: worst O(n^2)
    # scan the string takes O(n) time. 
    # whenever there is a ')', the for key, value loop will be executed. As the number
    # of ')' is not bounded by any constant (in fact it can be equal to number of atoms)
    # thus it should be a O(n^2) in worst case.
    
    # SC: O(n)
    # this is the space taken by the dict. To be more precise, there are only 26*26 number of 
    # UPPERlower letter combinations, thus this n has a upper bound.
    # To be even more precise, by 2020, there are only 118 different chemical elements discovered.
    # Thus n <= 118.
    
    # 1: this is do deal with when the number > 10. As we scan number from left to right,
    #    we need to *10 for the previous recorded number
    # 2: this helper function call wont stop untill it meets a ')'. Thus the returned i is
    #    the position right after ')'
    # 3: then we need to figure out how many copies of this sub formula are there
    # 4: DONT FORGET TO ADD 1
        
