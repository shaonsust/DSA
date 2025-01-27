class Solution:
    def construct_lower_array(self, arr):
        n = len(arr)
        mp = []
        
        for i in range(n):
            cnt = 0
            for j in range(i+1, n):
                if arr[j] < arr[i]:
                    cnt += 1
            mp.append(cnt)
        
        return mp


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))

        obj = Solution()
        print(obj.construct_lower_array(arr=arr))
