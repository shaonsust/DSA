class Solution:
    def get_min_max(self, arr):
        mx = float('-inf')
        mn = float('inf')

        for val in arr:
            if val > mx:
                mx = val
            
            if val < mn:
                mn = val
        
        return mn, mx


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))

        obj = Solution()
        mn, mx = obj.get_min_max(arr)
        print(mn, mx)
