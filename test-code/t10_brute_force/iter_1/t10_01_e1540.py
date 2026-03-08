import sys

def solve(nums: list[int]):
    for i in range(len(nums)):
        sub_nums = nums[:i] + nums[i+1:]
        if _solve(sub_nums,nums[i],str(nums[i])):
            return True

    return False
def _solve(nums: list[int],value,expr:str):
    # print(nums, value,f"expr: {expr}")

    if len(nums) == 0:
        return value == 23

    for i in range(len(nums)):
        sub_nums = nums[:i] + nums[i+1:]
        if _solve(sub_nums, value + nums[i],expr + f" + {nums[i]}"):
            return True
        if _solve(sub_nums, value - nums[i],expr + f" - {nums[i]}"):
            return True
        if _solve(sub_nums, value * nums[i],expr + f" * {nums[i]}"):
            return True
    return False

if __name__ == "__main__":
    f = open("input.txt")
    for line in f:
        nums = list(map(int,line.split()))
        if nums == [0]*5:
            break
        if solve(nums):
            print("Possible")
        else:
            print("Impossible")

    f.close()