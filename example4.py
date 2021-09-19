from debugger import debug


def twoSum(nums, target):
    seen = dict()
    res = []
    for i in range(len(nums)):
        seen[nums[i]] = i
    for key, val in seen.items():
        if target - key in seen.keys():
            res.append([val, seen[target - key]])
    return res


if __name__ == "__main__":
    nums = [2, 7, 3, 5, 4, 6]
    target = 9
    
    debug(twoSum, (nums, target))