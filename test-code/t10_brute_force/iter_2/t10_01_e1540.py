
def solve(nums: list[int]) -> bool:

    for i in range(len(nums)):
        sub_nums = nums[: i] + nums[i + 1: ]
        if _solve(sub_nums,nums[i]):
            return True

    return False

def _solve(nums: list[int],value:int) -> bool:

    if len(nums) == 0:
        return value == 23
    # print(nums,value)
    for i in range(len(nums)):
        sub_nums = nums[:i] + nums[i + 1: ]
        if _solve(sub_nums, value + nums[i]):
            return True
        if _solve(sub_nums, value * nums[i]):
            return True
        if _solve(sub_nums, value - nums[i]):
            return True

    return False


if __name__ == "__main__":

    f = open("input.txt")
    for line in f:
        nums = [int(n) for n in line.split()]
        if nums == [0]*5:
            break

        if solve(nums):
            print("Possible")
        else:
            print("Impossible")

    f.close()



