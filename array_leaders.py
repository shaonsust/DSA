class Solution:
    def leaders(self, arr):
        ans = []
        n = len(arr) - 1
        maxx = arr[n]
        
        for i in range(n, -1, -1):
            if arr[i] >= maxx:
                ans.append(arr[i])
                maxx = arr[i]

        ans.reverse()
        return ans


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))

        obj = Solution()
        print(obj.leaders(arr))
