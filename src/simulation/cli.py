import argparse

from simulation.land import Land


def parse_args(args=None):
    parser = argparse.ArgumentParser(description='Evolution Simulation:')

    program_group = parser.add_argument_group("program")
    program_group.add_argument("-v", "--video-path", dest='video_path', default="simulation.mp4")
    
    simulation_group = parser.add_argument_group("simulation")
    simulation_group.add_argument("-t", "--simulation-time", type=int, dest='ttl', default=30)
    simulation_group.add_argument("-w", "--land-width", type=int, dest='land_width', default=200)
    simulation_group.add_argument("-l", "--land-height", type=int, dest='land_height', default=200)
    simulation_group.add_argument("-p", "--creature-percentage", type=float, dest='creature_percent', default=0.1)
    
    creature_group = parser.add_argument_group("creature")
    creature_group.add_argument("-r", "--learning-rate", type=float, dest='learn_rate', default=0.03)
    creature_group.add_argument("-n", "--neurons", type=int, dest='neurons', default=3)

    return parser.parse_args(args=args)


def create_simulation(args):
    land_args = args.land_width, args.land_height, args.ttl, args.creature_percent
    creature_args = args.neurons, args.learn_rate
    return Land(land_args, creature_args, args.video_path)


def main(args):
    land = create_simulation(args)
    land.run()
