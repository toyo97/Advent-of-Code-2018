def entries_sum_r(tree):

    num_c, num_e = tree[0:2]
    s = [0] * num_c
    offset = [0] * num_c
    entries = [0] * num_c

    if num_c != 0:
        for i in range(num_c):
            s[i], offset[i], entries[i] = entries_sum_r(tree[2 + sum(offset):])

        # print(str(s) + ' ' + str(offset))  # mostra le somme dei figli e le lunghezze dei sottoalberi (figli)
        tot_offset = sum(offset)  # somma delle dimensioni dei sottoalberi
        node_value = 0

        for j in tree[2 + tot_offset: 2 + tot_offset + num_e]:
            if j <= num_c:
                node_value += entries[j-1]

        return sum(s) + sum(tree[2 + tot_offset:2 + tot_offset + num_e]), 2 + tot_offset + num_e, node_value

    else:
        node_value = sum(tree[2:2 + num_e])
        return node_value, 2 + num_e, node_value


tree = open('input.txt', 'r').read().split()
tree = [int(s) for s in tree]

entries_sum, tot_length, value = entries_sum_r(tree)

print('Sum of metadata entries: ' + str(entries_sum))
print('Value of root node: ' + str(value))


