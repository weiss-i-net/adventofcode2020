with open('input.txt') as file:
    groups = [group.split('\n') for group in file.read().split('\n\n')]
    for g in groups:
        if '' in g:
            g.remove('')

    groupsets = [set(char for char in ''.join(group)) for group in groups]
    print('Part 1:', sum(len(g) for g in groupsets))

    print(groups)
    sum_ans = 0
    for g in groups:
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if all(c in p for p in g):
                sum_ans += 1

    print('Part 2:', sum_ans)
