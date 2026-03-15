from inspect import stack


def solve(nums: int, pieces: int, value: int):

    max_value = 0
    stack = [(nums,pieces,value)]
    while stack:
        nums,pieces,value = stack.pop()
        product = int(nums) * value
        if product <= max_value:
            continue
        elif pieces == 1:
            max_value = product
            continue

        for i in range(1,len(nums) - pieces + 2):
            sub_nums = nums[i:]
            sub_value = int(nums[:i]) * value
            stack.append((sub_nums,pieces - 1, sub_value))

    return max_value

if __name__ == "__main__":
    f = open("input.txt")
    for line in f:
        n,m = line.split()
        max_value = 0

        print(solve(n,int(m),1))

    f.close()

