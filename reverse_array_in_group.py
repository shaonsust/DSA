class Solution:
    def reverse_in_group(self, arr, k):
        for i in range(0, len(arr), k):
            arr[i:i+k] = arr[i:i+k][::-1]

        return arr

    def reverse_in_group_two_pointer(self, arr, k):
        n = len(arr)
        for i in range(0, n, k):
            l = i
            h = n - 1 if i + k >= n else i + k - 1

            while l <= h:
                arr[l], arr[h] = arr[h], arr[l]
                l += 1
                h -= 1
        return arr


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.reverse_in_group_two_pointer(arr=arr, k=k))
