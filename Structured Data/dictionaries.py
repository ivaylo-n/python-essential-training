

def main():
    animals = dict(kitten='meow', puppy='ruff', lion='grrr',
            giraffe='I am a giraffe', dragon='raw')
    animals['monkey'] = 'haha'
    print('lion' in animals)
    print('found!' if 'godzilla' in animals else 'nope!')
    print(animals.get('godzilla'))
    print_dict(animals)


def print_dict(o):
    for k, v in o.items():
        print(f'{k}: {v}')


if __name__ == '__main__':
    main()


