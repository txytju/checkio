
def is_family(tree):

    fathers = [i[0] for i in tree]
    sons = [i[1] for i in tree]
    # fathers 中的名字不能有超过一个出现在 sons 中
    if len([i for i in set(fathers) if i not in set(sons)]) > 1 :
      return False

    # 父子不能反向
    for i in tree :
      if i[::-1] in tree :
        return False

    # 兄弟不能成父子
    for i in range(len(fathers)):
      for j in range(i+1,len(fathers)):
        if fathers[i]==fathers[j] :
          if [sons[i],sons[j]] in tree or [sons[j], sons[i]] in tree :
            return False

    return True


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_family([
      ['Logan', 'Mike']
    ]) == True, 'One father, one son'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack']
    ]) == True, 'Two sons'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Alexander']
    ]) == True, 'Grandfather'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Logan']
    ]) == False, 'Can you be a father for your father?'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Jack']
    ]) == False, 'Can you be a father for your brather?'
    assert is_family([
      ['Logan', 'William'],
      ['Logan', 'Jack'],
      ['Mike', 'Alexander']
    ]) == False, 'Looks like Mike is stranger in Logan\'s family'
    print("Looks like you know everything. It is time for 'Check'!")
