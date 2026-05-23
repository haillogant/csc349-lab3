import sys

def editDistance(word1, word2):
    n = len(word1)
    m = len(word2)

    E = [[0 for j in range(m + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        E[i][0] = i

    for j in range(m + 1):
        E[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if word1[i - 1] == word2[j - 1]:
                cost = 0
            else: cost = 1

            E[i][j] = min(E[i - 1][j] + 1, E[i][j - 1] + 1, E[i - 1][j - 1] + cost)

    return E[n][m]

def main():
    word1 = sys.argv[1]
    word2 = sys.argv[2]

    print(editDistance(word1, word2))


if __name__ == "__main__":
    main()
