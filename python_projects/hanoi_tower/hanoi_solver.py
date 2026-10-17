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

    unstack_index = 0

    i = 0
    max_iter = (2 ** num_disks) - 1
    print(f'{i}: {moves[-1]}')
    while len(towers[2]) < num_disks and i < max_iter:
        if unstack_index == 0 and len(towers[unstack_index]) > 0:
            if len(towers[unstack_index]) % 2 == 1:
                target_index, spare_index = 2, 1
            else:
                target_index, spare_index = 1, 2
        elif unstack_index == 1 and len(towers[unstack_index]) > 0:
            if len(towers[unstack_index]) % 2 == 1:
                target_index, spare_index = 2, 0
            else:
                target_index, spare_index = 0, 2
        elif unstack_index == 2 and len(towers[unstack_index]) > 0:
            if len(towers[unstack_index]) % 2 == 1:
                target_index, spare_index = 1, 0
            else:
                target_index, spare_index = 0, 1
        unstack = towers[unstack_index]
        target = towers[target_index]
        spare = towers[spare_index]

        if unstack and (not target or target[-1] > unstack[-1]):
            i += 1
            target.append(unstack.pop())
            moves.append(get_move_str(towers))
            print(f'{i}: {moves[-1]}')
            continue
        
        if not unstack:
            unstack_index = spare_index
            continue
        
        if target and target[-1] < unstack[-1]:
            unstack_index = target_index
    print(f'solved in {len(moves) - 1} iterations')
    return '\n'.join(moves)
        
if __name__ == '__main__':
    hanoi = hanoi_solver(5)
    print(hanoi)