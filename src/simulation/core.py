import cv2

from simulation.agent.creature import Creature

from simulation.land import Land

import numpy as np

class Simulation(object):
    def __init__(self, simulation_args, land_args, creature_args):
        self.ttl, creature_percent, land_width, land_height, video_path = simulation_args

        self.time = 0
        self.creatures = []
        self.land = Land(*land_args)
        
        creature_amount = int(land_width * land_height * creature_percent)
        self.create_creatures(self.land, creature_args, creature_amount)
        
        self.recorder = self.create_recorder(video_path, land_width, land_height)

    @staticmethod
    def generate_creature(land, index, creature_args):
        creature = Creature(land, index, *creature_args)
        land.grid[index].creature = creature
        return creature

    def create_creatures(self, land, creature_args, amount):
        created = 0
        for index in land.iterate_grid():
            if created == amount:
                break
            new_creature = self.generate_creature(land, index, creature_args)
            self.creatures.append(new_creature)
            created += 1

    @staticmethod
    def create_recorder(video_path, width, height):
        return cv2.VideoWriter(
            filename=video_path,
            fourcc=cv2.VideoWriter_fourcc(*'mp4v'),
            fps=5.0,
            frameSize=(width, height),
            isColor=False,
        )
        

    def time_step(self, video=False):
        self.time += 1
        for creature in self.creatures:
            creature.take_action()
        self.recorder.write(self.land.grid.astype(np.uint8))
        

    def run(self):
        while self.time < self.ttl:
            self.time_step()
        self.recorder.release()