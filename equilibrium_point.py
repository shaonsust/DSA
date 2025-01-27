class Solution:
    def find_equilibrium(self, arr):
        total = sum(arr)
        left = 0

        for i, val in enumerate(arr):
            left += val
            if left - val == total - left:
                return i
        return "-1"


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        obj = Solution()
        print(obj.find_equilibrium(arr=arr))
