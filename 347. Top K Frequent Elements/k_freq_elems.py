from collections import Counter
class Solution:
    def topKFrequent(self, nums: list, k: int) -> list:
        most_freq_nums =[0] *k
        freq_dict = Counter(nums)
        for i in range(k):
            largest =-(10**6)
            largest_num =-(10**6)
            for n in freq_dict:
                if freq_dict[n] > largest:
                    largest =freq_dict[n]
                    largest_num =n
            if largest_num!= -(10**6):
                most_freq_nums[i]= largest_num
                freq_dict.pop(largest_num)
        most_freq_nums.sort()
        return most_freq_nums