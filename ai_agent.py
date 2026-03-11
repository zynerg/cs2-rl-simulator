class AIAgent:
    def __init__(self):
        self.name = 'AI Agent'
        self.strategies = self.define_strategies()

    def define_strategies(self):
        return {
            'planting': self.plant_bomb,
            'defusing': self.defuse_bomb,
            'peeking': self.peek,
            'aiming': self.aim,
            'buying': self.buy,
            'teamwork': self.team_up
        }

    def plant_bomb(self):
        print(f'{self.name} is planting the bomb.')

    def defuse_bomb(self):
        print(f'{self.name} is defusing the bomb.')

    def peek(self):
        print(f'{self.name} is peeking around a corner.')

    def aim(self):
        print(f'{self.name} is aiming at the target.')

    def buy(self):
        print(f'{self.name} is buying equipment.')

    def team_up(self):
        print(f'{self.name} is helping teammates.')

    def perform_action(self, action):
        if action in self.strategies:
            self.strategies[action]()
        else:
            print(f'Action {action} not recognized.')
