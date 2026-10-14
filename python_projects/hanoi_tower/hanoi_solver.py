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
    ti = 1 if len(towers[ui]) % 2 == 1 else 2
    si = 2 if len(towers[ui]) % 2 == 1 else 1

    i = 0
    max_iter = 5
    while len(towers[2]) < num_disks and i < max_iter:
        i += 1
        print(f'ui: {ui}, ti: {ti}, si: {si}')
        unstack = towers[ui]
        target = towers[ti]
        spare = towers[si]

        if unstack and (not target or target[-1] > unstack[-1]):
            target.append(unstack.pop())
            moves.append(get_move_str(towers))
            temp = ti
            ti = si
            si = temp
            print(moves[-1])
            continue
        
        if not unstack:
            pass
        
        if target and target[-1] < unstack[-1]:
            temp = ui
            ui = ti
            ti = si
            si = temp
        
if __name__ == '__main__':
    hanoi = hanoi_solver(2)
