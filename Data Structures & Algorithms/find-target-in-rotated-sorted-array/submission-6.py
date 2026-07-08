class Solution:
    def search(self, arr: List[int], target: int) -> int:
        l = 0
        r = len(arr) - 1

        while l <= r:

            mid = l + math.ceil((r-l)/2)
            print(l,r,mid)
            if arr[mid] == target:
                return mid
            elif arr[l] <= arr[mid]:
                if arr[l] <= target < arr[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if arr[l] <= target > arr[mid] or target < arr[mid] <= arr[l]:
                    r = mid - 1
                else:
                    l = mid + 1
        print(mid, l, r)
        return -1