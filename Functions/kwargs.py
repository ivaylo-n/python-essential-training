

def main():
    x = dict(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr')
    kitten(**x)


def kitten(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} say {}'.format(k, kwargs[k]))
    else:
        print('Meow.')


if __name__ == '__main__':
    main()
