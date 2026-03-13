
alphabet: list[str]
N: int
k: int
count: int = 0

def solve(word: str):
    global count


    if len(word) == N:

        count += 1
        # print(count, word)
        return word

    for letter in alphabet:
        if letter not in word:
            res = solve(word + letter)
            if count == k:
                return res

if __name__ == "__main__":
    N,k = map(int,input().strip().split())

    alphabet = [chr(ord("a") + i) for i in range(N)]
    print(solve(""))