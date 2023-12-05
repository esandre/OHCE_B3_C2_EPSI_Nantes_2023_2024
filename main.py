LANG = 'FR'
TIME_IN_HOURS = 8

def dire_bonjour():
    if LANG == 'FR':
        return "Bonjour"
    else:
        return "Hello"


if __name__ == '__main__':
    print(dire_bonjour())
    phrase = input('Entrez une phrase :')
    inversé = phrase[::-1]

    print(inversé)

    if phrase == inversé:
        print('Bien dit')

    print('Au revoir')
