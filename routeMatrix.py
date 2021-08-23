def route_exists(from_row, from_column, to_row, to_column, map_matrix):
    
    size = (len(map_matrix), len(map_matrix[0]))
    s = []
    s.append((from_row, from_column))
    visited = [[False] * size[1] for _ in range(size[0])]

    while True:
        if len(s) == 0:
            return False

        current = s.pop()
        if current[0] == to_row and current[1] == to_column:
            return True
        
        visited[current[0]][current[1]] = True
        up = (current[0] - 1, current[1])
        down = (current[0] + 1, current[1])
        left = (current[0], current[1] - 1)
        right = (current[0], current[1] + 1)

        next_candidates = (up, right, down, left)
        for direction in next_candidates:
            if 0 <= direction[0] and direction[0] < size[0] \
                and 0 <= direction[1] and direction[1] < size[1]:

                if map_matrix[direction[0]][direction[1]] and \
                    not visited[direction[0]][direction[1]]:

                    s.append(direction)

if __name__ == '__main__':
    map_matrix = [
        [True, False, False],
        [True, True, False],
        [False, True, True]
    ];

    print(route_exists(0, 0, 2, 2, map_matrix))