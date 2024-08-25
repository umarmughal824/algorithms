Here's a proper README content for your project:

---

# Nearest Black Pixel Distance Calculator

This project solves the problem of calculating the distance of each pixel in a binary image to the nearest black pixel. The solution converts a black-and-white image to a grayscale image by making each pixel darker the closer it is to the nearest black pixel, and lighter the farther it is from the nearest black pixel. The Manhattan distance is used to determine proximity between pixels.

![img](https://github.com/user-attachments/assets/493f17fe-bed6-43b2-9cdf-c81c58224c82)


## Problem Description

### Input Format

- The input consists of `H` rows and `W` columns of pixels, where:
  - `H` is the number of vertical pixels.
  - `W` is the number of horizontal pixels.
  - Each pixel is represented as either `#` (black) or `.` (white).

- The first line of input contains two integers `H` and `W`, separated by a space.
- The next `H` lines each contain a string of length `W`, where each character is either `#` or `.`.

### Output Format

- The output should consist of `H` lines.
- Each line should contain the distance of each pixel to the nearest black pixel, with distances separated by a space.

### Example

#### Input Example 1
```
4 4
..##
...#
#...
....
```

#### Output Example 1
```
2 1 0 0
1 2 1 0
0 1 2 1
1 2 3 2
```

#### Input Example 2
```
3 5
.#.#.
#.#.#
.#.#.
```

#### Output Example 2
```
1 0 1 0 1
0 1 0 1 0
1 0 1 0 1
```

#### Input Example 3
```
1 1
#
```

#### Output Example 3
```
0
```

### Constraints

- `1 ≤ H, W ≤ 500`
- Each string `s_i` is of length `W` and consists of `#` and `.`.
- At least one `#` exists in the input.

## Solution Approach

The solution uses a **Breadth-First Search (BFS)** algorithm to efficiently calculate the shortest distance from each white pixel to the nearest black pixel. The algorithm initializes all black pixels with a distance of `0` and enqueues them. Then, it explores neighboring pixels (up, down, left, right) and updates their distances if a shorter path is found.

### Code Implementation

```python
from collections import deque

def nearest_black_pixel(H, W, image):
    # Initialize distance array with a large value (infinity)
    inf = float('inf')
    distance = [[inf] * W for _ in range(H)]
    
    # Initialize BFS queue
    queue = deque()
    
    # Find all black pixels and set their distance to 0
    for i in range(H):
        for j in range(W):
            if image[i][j] == '#':
                distance[i][j] = 0
                queue.append((i, j))
    
    # Directions for up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Perform BFS
    while queue:
        x, y = queue.popleft()
        current_distance = distance[x][y]
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W:
                if current_distance + 1 < distance[nx][ny]:
                    distance[nx][ny] = current_distance + 1
                    queue.append((nx, ny))
    
    # Print the distance array
    for row in distance:
        print(' '.join(map(str, row)))

# Main function to handle user input
if __name__ == "__main__":
    # Take input for H and W
    H, W = map(int, input().strip().split())
    
    # Take input for the image
    image = []
    for _ in range(H):
        row = input().strip()
        image.append(row)
    
    # Compute and print the nearest black pixel distances
    nearest_black_pixel(H, W, image)
```

## How to Run

1. Clone this repository to your local machine.
2. Run the Python script and input the image dimensions and pixel data as described in the input format.
3. The program will output the distance matrix, showing the distance of each pixel to the nearest black pixel.

## License

This project is open-source and available under the [MIT License](LICENSE).

---

This README provides a comprehensive overview of your project, guiding users on how to use the program and understand its functionality.
