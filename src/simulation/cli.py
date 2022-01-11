import argparse
from simulation.core import Simulation


def parse_args(args=None):
    parser = argparse.ArgumentParser(description='Evolution Simulation:')

    program_group = parser.add_argument_group("program")
    program_group.add_argument("-v", "--video-path", dest='video_path', default="simulation.mp4")
    program_group.add_argument("-l", "--log", dest='log_path', default="simulation.log")
    
    simulation_group = parser.add_argument_group("simulation")
    simulation_group.add_argument("-t", "--simulation-time", type=int, dest='ttl', default=30)
    simulation_group.add_argument("--land-width", type=int, dest='land_width', default=200)
    simulation_group.add_argument("--land-height", type=int, dest='land_height', default=200)
    simulation_group.add_argument("-p", "--creature-percentage", type=float, dest='creature_percent', default=0.1)
    
    creature_group = parser.add_argument_group("creature")
    creature_group.add_argument("-r", "--learning-rate", type=float, dest='learn_rate', default=0.03)
    creature_group.add_argument("-n", "--neurons", type=int, dest='neurons', default=3)

    return parser.parse_args(args=args)


def create_simulation(args):
    simulation_args = args.ttl, args.creature_percent, args.land_width, args.land_height, args.video_path
    land_args = args.land_width, args.land_height
    creature_args = args.neurons, args.learn_rate
    return Simulation(simulation_args, land_args, creature_args)


def main(args):
    sim = create_simulation(args)
    sim.run()
