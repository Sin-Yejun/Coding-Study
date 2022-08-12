class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        for i in nums1:
            if i in nums2:
                answer.append(i)
                nums2.remove(i)
        return answer
