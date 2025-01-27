class Solution:
    def majority_element(self, arr):
        n = len(arr) // 2
        mp = {}

        for val in arr:
            mp[val] = mp.get(val, 0) + 1

        for key, val in mp.items():
            if val > n:
                return key

        return "-1"
    
    def majority_element1(self, arr):
        candidate = self.find_the_candidate(arr)
        if self.is_majority(arr=arr, canditate=candidate):
            return candidate
        else:
            return "-1"

    def find_the_candidate(self, arr):
        maj = 0
        cnt = 0
        for i in range(len(arr)):
            if arr[maj] == arr[i]:
                cnt += 1
            else:
                cnt -= 1
            
            if cnt <= 0:
                maj = i
                cnt = 1

        return arr[maj]

    def is_majority(self, arr, canditate):
        count = 0
        for val in arr:
            if canditate == val:
                count += 1
        
        if count > len(arr) // 2:
            return True
        else:
            return False


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))

        obj = Solution()
        print(obj.majority_element1(arr))
