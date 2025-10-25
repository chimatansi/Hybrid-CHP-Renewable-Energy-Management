class SystemConfig:
    def __init__(self):
        self.NUM_PERIODS = 24
        self.LEARNING_RATE = 1e-3
        self.GAMMA = 0.99
        self.EPSILON_START = 1.0
        self.EPSILON_MIN = 0.01
        self.EPSILON_DECAY = 0.995
        self.BATCH_SIZE = 64
        self.REPLAY_MEMORY_SIZE = 2000
        self.TRAINING_EPISODES = 200
        self.EVALUATION_EPISODES = 10
        self.RELIABILITY_WEIGHT = 0.5
        self.COST_OPTIMIZATION_WEIGHT = 0.2
        self.RENEWABLE_WEIGHT = 0.3

CONFIG = SystemConfig()