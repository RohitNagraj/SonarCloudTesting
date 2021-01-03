import time

class Light:

    GREEN_COUNT = 0

    def __init__(self):
        self.state = 'red'

    def red(self):
        self.state = 'red'

    def amber(self):
        self.state = 'amber'
        self.GREEN_COUNT -= 1

    def green(self):
        if self.GREEN_COUNT == 0:
            self.state = 'green'
            self.GREEN_COUNT += 1
        else:
            print('ERROR')

    def get_state(self):
        return self.state

mode = int(input("Choose a mode: \n1. Auto\n2. Manual"))

lights = [Light(), Light(), Light(), Light()]

current = 0
lights[current].green()

def printer(lights):
    print([lights[i].get_state() + "\t" for i in range(4)])

if mode == 1:
    for i in range(10000):
        activate = (i) % 4
        lights[current].amber()
        printer(lights)
        time.sleep(1)
        lights[current].red()
        lights[activate].green()
        current  = activate
        printer(lights)
        time.sleep(3)


else:
    while True:
        activate = int(input("Select: \n1. Turn light 1 green\n2. Turn light 2 green\n3. Turn light 3 green\n4. Turn light 4 green\n")) - 1
        lights[current].amber()
        printer(lights)
        time.sleep(1)
        lights[current].red()
        lights[activate].green()
        current = activate
        printer(lights)

