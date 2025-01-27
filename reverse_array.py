class Solution():
    def reverse_array(self, arr):
        return arr[::-1]


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        obj = Solution()
        ans = obj.reverse_array(arr)
        ans.sort()
        print(" ".join(map(str, ans)))
        print(*ans)
        arr = list([0] * 10)
        print(*arr)
