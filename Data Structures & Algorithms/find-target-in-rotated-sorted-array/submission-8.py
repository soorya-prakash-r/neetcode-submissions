class Solution:
    def search(self, arr: List[int], target: int) -> int:
        l = 0
        r = len(arr) - 1

        while l <= r:

            mid = l + math.ceil((r-l)/2)
           
            if arr[mid] == target:
                return mid
            elif arr[l] <= arr[mid]:
                if arr[l] <= target < arr[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if arr[mid] < target <= arr[r]:
                    l = mid + 1
                else:
                    r = mid - 1
       
        return -1