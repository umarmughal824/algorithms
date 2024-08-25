# # coding: utf-8

from collections import deque


def nearest_black_pixel(H, W, image):
    # distance array with inf
    inf = float('inf')
    distances = [[inf] * W for _ in range(H)]

    # BFS queue
    queue = deque()

    # find all black pixels and set distance to 0
    for i in range(H):
        for j in range(W):
            if image[i][j] == '#':
                distances[i][j] = 0
                queue.append((i, j))

    # direction to up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()
        distance = distances[x][y]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W:
                if distance + 1 < distances[nx][ny]:
                    distances[nx][ny] = distance + 1
                    queue.append((nx, ny))

    for row in distances:
        print(' '.join(map(str, row)))


if __name__ == "__main__":

    # take user input
    # H, W = map(int, input().strip().split())
    #
    # image = []
    # for _ in range(H):
    #     row = input().strip()
    #     image.append(row)
    #
    # nearest_black_pixel(H, W, image)

    # ex 1
    H, W = 4, 4
    image = [
        "..##",
        "...#",
        "#...",
        "....",
    ]
    nearest_black_pixel(H, W, image)

    # ex @
    H, W = 3, 5
    image = [
        ".#.#."
        "#.#.#",
        ".#.#.",
    ]
    nearest_black_pixel(H, W, image)


    H, W = 1, 1
    image = [
        "#"
    ]
    nearest_black_pixel(H, W, image)
