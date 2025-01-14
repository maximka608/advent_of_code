
def reader(path: str):
    left_side, right_side = [], []
    with open(path, 'r') as file:
        for pair in file:
            pair = pair.split()
            left_side.append(int(pair[0]))
            right_side.append(int(pair[1]))
    return left_side, right_side

def calc_dist(nums1: list, nums2: list):
    all_dist = 0
    for i in range(len(nums1)):
        all_dist += abs(nums1[i] - nums2[i])
    return all_dist

def count_frequency(nums: list) -> dict:
    hashmap = {}
    for num in nums:
        if num not in hashmap:
            hashmap[num] = 1
        else:
            hashmap[num] += 1
    return hashmap

def calc_similarity(nums1: list, nums2: list):
    freq, similarity = count_frequency(nums2), 0
    for num in nums1:
        if num in freq:
           similarity += num * freq[num]
    return similarity

def task1():
    nums1, nums2 = reader('2024/01/input2.txt')
    sorted_nums1, sorted_nums2 = sorted(nums1), sorted(nums2)
    dist = calc_dist(sorted_nums1, sorted_nums2)
    print(dist)

def task2():
    nums1, nums2 = reader('2024/01/puzzle_input.txt')
    similarity = calc_similarity(nums1, nums2)
    print(similarity)

if __name__ == '__main__':
    task2()
