def get_input():
    output = []
    with open('input.txt') as file:
        for line in file:
            output.append([char for char in line.strip()])
    return list(zip(*output))

def main():
    tree_map = get_input();
    max_x = len(tree_map)
    max_y = len(tree_map[1])

    tree_count = 0
    for y in range(max_y):
        if tree_map[(3*y) % max_x][y] == '#':
            tree_count += 1

    print('Part 1:', tree_count)

    tree_product = 1
    for x_slope, y_slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        tree_count = 0
        for y in range(0, max_y, y_slope):
            if tree_map[(x_slope * y // y_slope) % max_x][y] == '#':
                tree_count += 1
        tree_product *= tree_count

    print('Part 2:', tree_product)





if __name__ == '__main__':
    main()
