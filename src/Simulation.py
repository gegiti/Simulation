import numpy as np
import cv2

from Creature import Creature


class Land(object):

    class Cell(object):

        def __init__(self):
            self.creature = None
            self.smell = None
            self.blocked = False

        def __bool__(self):
            return bool(self.creature)

        def __int__(self):
            return 255 * bool(self)
    
    def __init__(self, land_args, creature_args, video_path):
        self._time = 0        
        self._width, self._height, self._ttl, creature_percent = land_args
        self._creature_args = creature_args        

        self.creatures = []
        self.recorder = self.create_recorder(video_path)
        self.grid = np.array([[Land.Cell() for _ in range(self._height)] for _ in range(self._width)])
        self.creature_amount = int(self.grid.size * creature_percent)
        self.init_grid()


    # Initialization:

    def generate_creature(self, index):
        creature = Creature(self, index, *self._creature_args)
        self.grid[index].creature = creature
        self.creatures.append(creature)
        return creature

    def init_grid(self):
        created = 0
        for index in self.iterate_grid():
            if created == self.creature_amount:
                break
            self.generate_creature(index)
            created += 1

    def create_recorder(self, video_path):
        return cv2.VideoWriter(
            filename=video_path,
            fourcc=cv2.VideoWriter_fourcc(*'mp4v'),
            fps=3.0,
            frameSize=(self._height, self._width),
            isColor=False,
        )


    # Run simulation:

    def time_step(self, video=False):
        self._time += 1
        for index in self.iterate_grid():
            if not self.occupied(index):
                continue
            self.grid[index].creature.take_action()
        self.recorder.write(self.grid.astype(np.uint8))
        

    def run(self):
        while self._time < self._ttl:
            self.time_step()
        self.recorder.release()


    # Utils:

    def iterate_grid(self):
        indices = list(np.ndindex(self.grid.shape))
        np.random.shuffle(indices)
        for index in indices:
            yield index

    def occupied(self, index):
        return self.grid[index].creature
