def disconnected_users(net, users, source, crushes):
    # net : a list
    # users :a dict
    # source : string
    # crushes : a list


    if source in crushes:
        return sum(users.values())
    
    safe = [source]

    while True:
        n1 = len(set(safe))

        for a,b in net:
            if a in safe and b not in crushes:
                safe.append(b)
            elif b in safe and a not in crushes:
                safe.append(a)

        n2 = len(set(safe))

        if n1==n2:
            break

    return sum(users.values()) - sum([users[i] for i in set(safe)])
















if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert disconnected_users([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 20,
        'C': 30,
        'D': 40
    },
        'A', ['C']) == 70, "First"

    assert disconnected_users([
        ['A', 'B'],
        ['B', 'D'],
        ['A', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 0,
        'C': 0,
        'D': 40
    },
        'A', ['B']) == 0, "Second"

    assert disconnected_users([
        ['A', 'B'],
        ['A', 'C'],
        ['A', 'D'],
        ['A', 'E'],
        ['A', 'F']
    ], {
        'A': 10,
        'B': 10,
        'C': 10,
        'D': 10,
        'E': 10,
        'F': 10
    },
        'C', ['A']) == 50, "Third"

    print('Done. Try to check now. There are a lot of other tests')
