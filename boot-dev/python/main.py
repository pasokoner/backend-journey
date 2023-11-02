import random


def tsp(cities, paths, dist):
    perms = permutations(cities)
    for perm in perms:
        total_dist = 0
        for i in range(1, len(perm)):
            total_dist += paths[perm[i - 1]][perm[i]]
        if total_dist < dist:
            return True
    return False


# don't touch below this line


def test(num_cities, dist):
    paths = []
    cities = []
    for i in range(num_cities):
        path = []
        for j in range(num_cities):
            if i == j:
                path.append(0)
            elif j < i:
                path.append(paths[j][i])
            else:
                path.append(random.randint(0, 999))
        paths.append(path)
        cities.append(i)
    path_exists = tsp(cities, paths, dist)
    print("Paths:")
    print_matrix(paths)
    print("------------------------------------")
    print(f"Path shorter than {dist} miles exists: {path_exists}")
    print("====================================")


def main():
    random.seed(0)
    for num_cities in range(2, 10):
        dist = random.randint(0, 3999)
        test(num_cities, dist)


def permutations(arr):
    res = []
    res = helper(res, arr, len(arr))
    return res


def helper(res, arr, n):
    if n == 1:
        tmp = arr.copy()
        res.append(tmp)
    else:
        for i in range(n):
            res = helper(res, arr, n - 1)
            if n % 2 == 1:
                arr[n - 1], arr[i] = arr[i], arr[n - 1]
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]
    return res


def print_matrix(mat):
    n = len(mat)
    m = len(mat[0])
    for i in range(n):
        print(mat[i])


main()
