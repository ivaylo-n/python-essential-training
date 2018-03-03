
def main():
    game = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    print(game[1:5:2])
    i = game.index('Paper')
    print(game[i])
    game.append('Computer')
    game.insert(0, 'Mouse')
    game.remove('Paper')
    x = game.pop(3)
    print(x)
    del game[1:3]
    print(', '.join(game))
    print(len(game))
    print_list(game)


def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()


if __name__ == '__main__': main()

