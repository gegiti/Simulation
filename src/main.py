import argparse

from .Simulation import Land

TTL = 1000
WIDTH = 200
LENGTH = 200
CREATURE_PERCENTAGE = 0.2

LEARN_RATE = 0.03
NEURONS = 5


def parse_args():
    parser = argparse.ArgumentParser(description='Evolution Simulation:')

    # program_group = parser.add_argument_group("program")
    # program_group.add_argument("-s", "--save-file-path", type=str, dest='save_path', default=None)
    # program_group.add_argument("-L", "--load-file-path", type=str, dest='load_path', default=None)
    
    simulation_group = parser.add_argument_group("simulation")
    simulation_group.add_argument("-t", "--simulation-time", type=int, dest='ttl', default=TTL)
    simulation_group.add_argument("-w", "--land-width", type=int, dest='land_width', default=WIDTH)
    simulation_group.add_argument("-l", "--land-length", type=int, dest='land_length', default=LENGTH)
    simulation_group.add_argument("-p", "--creature-percentage", type=int, dest='creature_percent', default=CREATURE_PERCENTAGE)
    
    creature_group = parser.add_argument_group("creature")
    creature_group.add_argument("-r", "--learning-rate", type=float, dest='learn_rate', default=LEARN_RATE)
    creature_group.add_argument("-n", "--neurons", type=int, dest='neurons', default=NEURONS)

    args, unknown = parser.parse_known_args()
    return args, unknown


def create_simulation(args):
    land_args = args.land_width, args.land_length, args.ttl, args.creature_percent
    creature_args = args.neurons, args.learn_rate
    return Land(land_args, creature_args)


def main():
    args, _ = parse_args()
    land = create_simulation(args)
    land.run()


if __name__ == '__main__':
    main()
