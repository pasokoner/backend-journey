import random


def verify_tsp(paths, dist, actual_path):
    total_distance = 0

    for i in range(len(actual_path) - 1):
        total_distance += paths[actual_path[i]][
            actual_path[i + 1]
        ]  # Calculate the distance between consecutive cities

    total_distance += paths[actual_path[-1]][
        actual_path[0]
    ]  # Return to the starting city

    if total_distance < dist:
        return True  # If the path's distance is shorter than dist, return True

    return False


# don't touch below this line


def test(num_cities, dist, actual_path):
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
    path_exists = verify_tsp(paths, dist, actual_path)
    print("Paths:")
    print_matrix(paths)
    print("------------------------------------")
    print(f"Path shorter than {dist} miles exists: {path_exists}")
    print("====================================")


def main():
    random.seed(0)
    actual_paths = [
        [0, 1],
        [1, 2, 0],
        [1, 0, 2, 3],
    ]
    for num_cities in range(2, 5):
        dist = random.randint(0, 3999)
        test(num_cities, dist, actual_paths[num_cities - 2])


def print_matrix(mat):
    n = len(mat)
    m = len(mat[0])
    for i in range(n):
        print(mat[i])


main()
