nums1 = [1, 2, 3, 4, 5]
nums2 = [1, 2, 3, 4, 5]

# print(nums1 is nums2)
#
# print(nums1 == nums2)
# print(id(nums1) == id(nums2))
# print(id(nums1) is id(nums2))


# a=[1,2,3]
# b=a.copy()
# b.append([99,100])
# print(a)
#
# b=a
# b.append([99,100])
# print(a)


# import copy
# data1 = [[1, 2, 3], [4, 5, 6]]
# data2 = copy.deepcopy(data1)
# data1[0].append(7)
# data2[1].append(8)
# print(id(data1), data1)
# print(id(data2), data2)

data1 = [1, 2]
data2 = list(data1)
data1.append(3)
data2.append(4)

print(data1)
print(data2)



