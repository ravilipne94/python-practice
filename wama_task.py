# def is_valid_sudoku(grid):
#     for row in grid:
#         if len(set(row)) != len(row):
#             return False

#     for col in zip(*grid):
#         if len(set(col)) != len(col):
#             return False

#     for i in range(0, 9, 3):
#         for j in range(0, 9, 3):
#             sub_matrix = [grid[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
#             if len(set(sub_matrix)) != len(sub_matrix):
#                 return False

#     return True

# def my_puzzle(grid):
#     # if not is_valid_sudoku(grid):
#     #     return False

#     for i in range(9):  # 2
#         for j in range(9):  # 1
#             if grid[i][j] == 0:   
#                 for num in range(1, 10):
#                     if cheking_row(grid, i, j, num):
#                         grid[i][j] = num
#                         if my_puzzle(grid):
#                             return True
#                         grid[i][j] = 0
#                 return False        
#     return True


# def cheking_row(grid, row, col, num):   # (grid, 0, 2, 1)
#     for x in range(9):
#         if grid[row][x] == num:
#             return False

#     for x in range(9):
#         if grid[x][col] == num:
#             return False

#     startRow = row - row % 3
#     startCol = col - col % 3
#     for i in range(3):
#         for j in range(3):
#             if grid[i + startRow][j + startCol] == num:
#                 return False
#     return True

# grid = [
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9]
# ]

# def show(grid):
#     for row in grid:
#         print(" ".join(str(cell) for cell in row))

# if my_puzzle(grid):
#     show(grid)
# else:
#     print("Not resolved")



# ======================================================================


# class LRU:

#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.lst = []


#     def get(self, val):
#         if val not in self.lst:
#             print("Element not exists in array")
#         else:
#             self.lst.remove(val)
#             self.lst.append(val)  # we will append it means we just add it or recently use it.
#             print("most recently used value", self.lst[val])


#     def put(self, val):
#         self.lst.append(val)
#         if len(self.lst) > self.capacity:
#             self.lst.remove(self.lst[0])    
#         print(self.lst)


# a = LRU(3)
# a.put(1)
# a.put(2)
# a.put(3)
# a.get(2)
# a.put(5)
# a.put(6)
# a.get(3)
# a.put(3)
# a.get(2)




# class LRUCache:

#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.cache = {}
#         self.order = []

#     def get(self, key):
#         if key in self.cache:
#             self.order.remove(key)
#             self.order.append(key)  # to show key is recently updated.
#             return self.cache[key]
#         else:
#             return "Element not present"

#     def put(self, key, value):
#         if key in self.cache:    # same key is not allowed in dictionary so remove it..
#             self.order.remove(key)
#         elif len(self.cache) >= self.capacity:   # check length of cache inside dict.
#             LRU_key = self.order.pop(0)                   # Remove the old used element from .
#             del self.cache[LRU_key]  # 2
#         self.cache[key] = value   # add new key-value in cache
#         self.order.append(key)    # append new key in order so we can find it is latest.
#         # print(self.order)

#     def show(self):
#         print(self.cache)


# cache = LRUCache(4)
# cache.put(1, 1) 
# cache.put(2, 2)
# cache.put(3, 3)
# cache.put(4, 4)
# # print(cache.get(3))
# print(cache.get(2))
# print(cache.get(1))
# cache.put(5, 5) 
# # cache.show()

# # print(cache.get(2))
# cache.put(6, 6) 
# cache.show()


# cache = LRUCache(3)
# cache.put(1, 'a')
# cache.put(2, 'b')
# print(cache.get(2)) 
# cache.put(5, 'e')
# cache.put(6, 'f')
# print(cache.get(3))
# cache.put(3, 'c')
# print(cache.get(2))


# ===================================================================================================


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def buildOwnTree(nums, index):
#     if index >= len(nums) or nums[index] is None:
#         return None

#     root = TreeNode(nums[index])
#     root.left = buildOwnTree(nums, 2 * index + 1)
#     root.right = buildOwnTree(nums, 2 * index + 2)
#     return root

# def maxPathSum(root):
#     def maxSum(node):
#         nonlocal max_sum   # we have to update this value in inside the function not in global.
#         if not node:
#             return 0

#         left_sum = max(0, maxSum(node.left)) # it will take left value using node
#         right_sum = max(0, maxSum(node.right)) # it will take right value using node
#         max_sum = max(max_sum, node.val + left_sum + right_sum)
#         return node.val + max(left_sum, right_sum)

#     max_sum = float('-inf')
#     maxSum(root)
#     return max_sum

# if __name__ == "__main__":
#     # nums = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
#     nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
#     root = buildOwnTree(nums, 0)
#     max_sum = maxPathSum(root)
#     print("Max path sum -----", max_sum)

