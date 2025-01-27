class Solution:
    def remove_duplicates(self, arr):
        largest = -1
        ans = []
        for val in arr:
            if val > largest:
                largest = val
        
        temp = list([0] * (largest + 1))
        for val in arr:
            temp[val] = temp[val] + 1
            if temp[val] == 1:
                ans.append(val)
        
        return ans

    def remove_duplicates_1(self, arr):
        st = set()
        v = []
        for item in arr:
            if item not in st:
                st.add(item)
                v.append(item)
        
        return v


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))

        obj = Solution()
        # arr = obj.remove_duplicates(arr)
        arr = obj.remove_duplicates_1(arr)
        print(*arr)
        print("~")
