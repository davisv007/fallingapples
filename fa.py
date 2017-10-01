def gravity(grid):
    final_grid = []
    column_generator = column_gen(grid)
    fixed_columns = [[fixed_column for fixed_column in next(fix_gen(fix_stepper(column)))] for column in
                     column_generator]
    final_grid = (row for row in column_rearranger(fixed_columns))
    print('final grid:')
    [print(x) for x in final_grid]


def column_gen(grid):
    yield from ([grid[col][row] for col in range(len(grid))] for row in range(len(grid[0])))


def fix_gen(fix_stepper, prev_column=[]):
    current_column = next(fix_stepper)
    while prev_column != current_column:
        prev_column = [x for x in current_column]
        current_column = next(fix_stepper)
    yield current_column


def fix_stepper(column):
    new_column = [x for x in column]
    while True:
        i = 0
        while i < len(new_column) - 1:
            pair = [new_column[i], new_column[i + 1]]
            if '#' not in pair and pair[0] == 'a' and pair[1] != 'a':
                # a is in the list and # is not and pair0=a
                new_column[i], new_column[i + 1] = new_column[i + 1], new_column[i]
            i += 1
        yield new_column


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
    # grid = [['a', 'a', 'a', 'a'], ['#', '.', 'a', '.'], ['a', '.', '.', 'a'], ['.', '.', '.', 'a'], ]
    grid = [['a', 'a', 'a', 'a'], ['a', 'a', 'a', '.'], ['a', 'a', '.', '.'], ['a', '.', '.', '.']]
    print('starting grid:')
    [print(x) for x in grid]
    gravity(grid)


main()
