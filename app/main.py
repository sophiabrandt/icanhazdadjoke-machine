import dadjokes
import requests.exceptions


def main():
    """ Gets a random joke from https://icanhazdadjoke.com/"""
    print_header()
    run_event_loop()


def print_header():
    print('-----------------------------------')
    print('      ICANHAZDADJOKES APP')
    print('-----------------------------------')
    print()


def run_event_loop():
    cmd = 'EMPTY'
    try:
        joke = dadjokes.get_joke()
        print(joke)
        print()

        while cmd != 'x' and cmd:
            cmd = input('[G]et a new dad joke, e[x]it.')
            cmd = cmd.lower().strip()

            if cmd == 'g':
                joke = dadjokes.get_joke()
                print()
                print(joke)
                print()
            elif cmd != 'x' and cmd:
                print(f"Sorry, I don't understand '{cmd}'.")

    except requests.exceptions.ConnectionError:
        print('Error: Your network is down.')
    except Exception as x:
        print(f'Unexpected error. Details: {x}')

    print('...exiting....\nGoodbye.')


if __name__ == '__main__':
    main()
