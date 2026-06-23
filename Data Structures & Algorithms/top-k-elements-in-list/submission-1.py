class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1

        sorted_items = sorted(d.items(), key = lambda x: x[1], reverse = True)

        result = []
        for num, freq in sorted_items[:k]:
            result.append(num)
        
        return result
      
            

        