def gravity(grid):
    rows = len(grid)
    columns = len(grid[0])
    columns_list_upside_down = []
    for i in range(columns):
        col = []
        for j in range(rows - 1, -1, -1):
            col.append(grid[j][i])
        columns_list_upside_down.append(col)
    print('reformed to show falling apples:')
    [print(x) for x in columns_list_upside_down]
    for j in range(len(grid)):
        for lst in columns_list_upside_down:
            for i in range(len(lst) - 1):
                pair = [lst[i], lst[i + 1]]
                if 'a' not in pair or '#' in pair:
                    continue
                else:
                    # a is in the list and # is not
                    if pair[1] == 'a':
                        lst[i], lst[i + 1] = lst[i + 1], lst[i]
    print('gravity points left')
    [print(x) for x in columns_list_upside_down]
    row_list_right_side_up = []
    for i in range(len(columns_list_upside_down[0]) - 1, -1, -1):
        row =[]
        for element in columns_list_upside_down:
            row.append(element[i])
        row_list_right_side_up.append(row)
    print('reoriented:')
    [print(x) for x in row_list_right_side_up]



def main():
    # for i in range(int(input())):
    #     #make grid (get c,r)
    #     row,col=input().split()
    #     grid=[]
    #     for i in range(int(row)):
    #         grid.append(input())
    grid = [['a', 'a', 'a', 'a'], ['#', '.', 'a', '.'], ['.', '.', '.', 'a']]
    # grid = [['a', 'a', 'a', 'a'], ['a', 'a', 'a', '.'], ['a', 'a', '.', '.'], ['a', '.', '.', '.']]
    print('starting grid:')
    [print(x) for x in grid]
    gravity(grid)


main()
