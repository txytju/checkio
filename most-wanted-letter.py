import string

def checkio(text):

    toDelete = string.punctuation + string.digits + " "
    text = "".join([i for i in text if i not in toDelete]).lower()
    # text = text.translate(None, string.punctuation)
    
    print(text)

    s = 'abcdefghijklmnopqrstuvwxyz'
    d = {}
    for i in s :
        d[i] = 0

    for i in text :
        d[i] += 1  

    return max(d, key=d.get)

from collections miport Counter

def checkio_1(text):
    t = Counter([i for i in text.lower() if i i.isalpha()])
    return max(t, key=t.get)



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")