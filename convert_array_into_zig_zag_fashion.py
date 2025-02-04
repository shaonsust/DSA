class Solution:
    def zigzag(self, arr):
        arr.sort()

        for i in range(1, len(arr) - 1, 2):
            arr[i], arr[i+1] = arr[i+1], arr[i]

        return "true"


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))

        obj = Solution()
        print(obj.zigzag(arr=arr))
