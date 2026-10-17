def get_move_str(towers):
    tower_parts = []
    for tower in towers:
        tower_str = '['
        tower_str += ', '.join([str(i) for i in tower])
        tower_str += ']'
        tower_parts.append(tower_str)
    return ' '.join(tower_parts)

def hanoi_solver(num_disks):
    towers = [[], [], []]
    for i in range(num_disks, 0, -1):
        towers[0].append(i)

    moves = [get_move_str(towers)]

    ui = 0

    i = 0
    max_iter = 10000
    while len(towers[2]) < num_disks and i < max_iter:
        if ui == 0 and len(towers[ui]) > 0:
            if len(towers[ui]) % 2 == 1:
                ti, si = 2, 1
            else:
                ti, si = 1, 2
        elif ui == 1 and len(towers[ui]) > 0:
            if len(towers[ui]) % 2 == 1:
                ti, si = 2, 0
            else:
                ti, si = 0, 2
        elif ui == 2 and len(towers[ui]) > 0:
            if len(towers[ui]) % 2 == 1:
                ti, si = 1, 0
            else:
                ti, si = 0, 1
        i += 1
        print(f'ui: {ui}, ti: {ti}, si: {si}')
        unstack = towers[ui]
        target = towers[ti]
        spare = towers[si]

        if unstack and (not target or target[-1] > unstack[-1]):
            target.append(unstack.pop())
            moves.append(get_move_str(towers))
            print(moves[-1])
            continue
        
        if not unstack:
            print(f'ui: {ui} is empty, switching to si: {si}')
            ui = si
            continue
        
        if target and target[-1] < unstack[-1]:
            print(f'Cannot move from ui: {ui} to ti: {ti}, switching to ti: {ti}')
            ui = ti
    print(f'solved in {len(moves) - 1} iterations')
    return '\n'.join(moves)
        
if __name__ == '__main__':
    hanoi = hanoi_solver(10)
    # print(hanoi)
