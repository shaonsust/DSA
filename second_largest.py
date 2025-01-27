class Solution():
    def second_largest_1(self, arr):
        arr.sort(reverse=True)
        for val in arr:
            if val < arr[0]:
                return val
        
        return "-1"
    
    def second_largest_2(self, arr):
        largest = -1
        second_largest = -1

        for val in arr:
            if val > largest:
                largest = val
        
        for val in arr:
            if val > second_largest and val != largest:
                second_largest = val
        
        return second_largest
    
    def second_largest_3(self, arr):
        largest = -1
        second_largest = -1

        for val in arr:
            if val > largest:
                second_largest = largest
                largest = val
            
            elif val < largest and val > second_largest:
                second_largest = val
        
        return second_largest


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
    
        obj = Solution()
        print(obj.second_largest_1(arr=arr))
        print(obj.second_largest_2(arr=arr))
        print(obj.second_largest_3(arr=arr))
