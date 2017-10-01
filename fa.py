def gravity(grid):
    lst = []
    final_grid = []
    for column in column_generator(grid):
        prev_column = []
        while prev_column != column:
            prev_column = column
            column = column_fixer(column)
        lst.append(column)
    final_grid = [x for x in column_rearranger(lst)]
    print('final grid:')
    [print(x) for x in final_grid]


def column_generator(grid):
    yield from ([grid[col][row] for col in range(len(grid))] for row in range(len(grid[0])))


def column_fixer(column):
    i = 0
    new_column = [x for x in column]
    while i < len(new_column) - 1:
        pair = [new_column[i], new_column[i + 1]]
        if '#' not in pair and pair[0] == 'a' and pair[1] != 'a':
            # a is in the list and # is not and pair0=a
            new_column[i], new_column[i + 1] = new_column[i + 1], new_column[i]
        i += 1
    return new_column


def column_rearranger(column_list):
    yield from ([column[i] for column in column_list] for i in range(len(column_list[0])))


def main():
    # for i in range(int(input())):
    #     #make grid (get c,r)
    #     row,col=input().split()
    #     grid=[]
    #     for i in range(int(row)):
    #         grid.append(input())
    # grid = [[1,0,1],[2,0,2],[3,0,3]]
    grid = [['a', 'a', 'a', 'a'], ['#', '.', 'a', '.'], ['a', '.', '.', 'a'], ['.', '.', '.', 'a'], ]
    # grid = [['a', 'a', 'a', 'a'], ['a', 'a', 'a', '.'], ['a', 'a', '.', '.'], ['a', '.', '.', '.']]
    print('starting grid:')
    [print(x) for x in grid]
    gravity(grid)


main()
