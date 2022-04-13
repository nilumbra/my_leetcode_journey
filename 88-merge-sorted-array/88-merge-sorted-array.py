class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        top1, top2 = 0, 0
        # print(top1)
        _nums1 = nums1[:m]
        # print(_nums1)
        while top1 != m and top2 != n:
            if _nums1[top1] <= nums2[top2]:
                nums1[top1 + top2] = _nums1[top1]
                top1 += 1
            else:
                nums1[top1 + top2] = nums2[top2]
                top2 += 1
        
        
        if top1 == m:
            while top2 != n:
                # print("top2", top2)
                nums1[top1 + top2] = nums2[top2]
                top2 += 1
        else:
            while top1 != m:
                # print("top1", top1)
                nums1[top1 + top2] = _nums1[top1]
                top1 += 1
        