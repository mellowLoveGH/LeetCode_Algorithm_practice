class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        L = len(nums)
        if L<1:
            return []
        nums = sorted(nums)
        re = []
        #check = set()
        # a<=b<=c
        i = 0
        while i<L-2:
            v1 = nums[i]            
            if i>0 and v1 == nums[i-1]:
                i = i + 1
                continue
            j=i+1
            k = L-1
            while j<L-1:
                v2 = nums[j]
                #print(v1, v2)
                if j>i+1 and v2==nums[j-1]:
                    j = j + 1
                    continue         
                while k>j:
                    v3 = nums[k]
                    if v3 < -(v1+v2):
                        break
                    if k < L-1 and v3 == nums[k+1]:
                        k=k-1
                        continue
                    #print('===', v1, v2, v3)
                    if v1+v2+v3 == 0:
                        #print('---', i, j, k)
                        #line = str(v1) + str(v2) + str(v3)
                        re.append( [v1,v2,v3] )           
                    k = k - 1
                j = j + 1
            i = i + 1
        #print(re)
        return re

class Solution:
    def intToRoman(self, num: int) -> str:
        dic1 = { 1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M', 4:"IV", 9:"IX", 40:"XL", 90:"XC", 400:"CD", 900:"CM" }
        line = ""
        base = 1
        while num > 0:
            d = num%10
            n = d*base
            sub = self.roman(n, dic1)
            line = sub + line
            base = base * 10
            num = num//10

        return line

    def roman(self, n, dic1):
        if n  == 0:
            return ""
        R = ""
        if n < 4:
            R = n*str( dic1[1] )
        elif n == 4 or n == 5:
            R = str( dic1[n] )
        elif n < 9:
            R = str( dic1[5] ) + (n-5)*str( dic1[1] )
        elif n ==9 or n ==10:
            R = str( dic1[n] )
        #
        elif n<40:
            R = (n//10)*str( dic1[10] )
        elif n == 40 or n == 50:
            R = str( dic1[n] )
        elif n < 90:
            R = str( dic1[50] ) + (n//10-5)*str( dic1[10] )
        elif n ==90 or n ==100:
            R = str( dic1[n] )
        #
        elif n<400:
            R = (n//100)*str( dic1[100] )
        elif n == 400 or n == 500:
            R = str( dic1[n] )
        elif n < 900:
            R = str( dic1[500] ) + (n//100-5)*str( dic1[100] )
        elif n ==900 or n ==1000:
            R = str( dic1[n] )
        #
        else:
            R = (n//1000)*str( dic1[1000] )
        return R

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        L = len(nums)
        if L<3:
            return 0
        nums = sorted(nums)
        N = nums[0]
        # a<=b<=c
        i = 0
        j = 0
        pv = nums[0]+nums[1]+nums[2]
        op = pv
        print(nums)
        while i<L-2:                      
            j = i + 1
            k = L - 1
            v1 = nums[i]
            while j<L-1:
                v2 = nums[j]
                while k>j:                    
                    v3 = nums[k]
                    s = v1+v2+v3
                    if self.update(target, op, s):
                        op = s
                        if op == target:
                            return op
                    if s < target:
                        break
                    k = k-1
                j = j + 1
            i = i+1
        print(op)
        return op

    def update(self, target, op, pv):
        d1 = abs(op-target)
        d2 = abs(pv-target)
        print("===", op, pv)
        if d1 <= d2:
            return False
        return True