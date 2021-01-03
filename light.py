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
    
    def get_state(self):
        return self.state
