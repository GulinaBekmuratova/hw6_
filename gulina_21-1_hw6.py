def get_list() -> list:
    return list(range(0, 1000000, 2))

class Solution:

    def find_target(self, list_, target):
        low = 0
        high = len(list_) - 1


        while low <= high:
            mid = (low + high) // 2
            guess = list_[mid]
            if guess == target:
                return mid

            if guess > target:
                high = mid - 1
            else:
                low = mid + 1
        return None

list1 = Solution()
print(list1.find_target(get_list(), 10000))

# with open('binary_search.txt', 'x') as file:
#     file.read()