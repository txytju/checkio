def checkio(game_result):

    a = []

    # 横向的
    for element in game_result :
        a.append([i for i in element])

    # 竖向的
    for i in range(3) :
        a.append([game_result[0][i], game_result[1][i], game_result[2][i]])

    # 斜向的
    a.append([game_result[0][0], game_result[1][1], game_result[2][2]])
    a.append([game_result[0][2], game_result[1][1], game_result[2][0]])

    
    for j in a :
        if is_X(j) :
            return "X"
        if is_O(j) :
            return "O"
    else :
        return "D"





def is_X(data) :
    if data == ["X","X","X"] :
        return True

def is_O(data):
    if data == ["O","O","O"] :
        return True






if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X" , "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

