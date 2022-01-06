import argparse

from Simulation import Land


TTL = 1000
WIDTH = 200
LENGTH = 200


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
    
    creature_group = parser.add_argument_group("creature")
    creature_group.add_argument("-r", "--learning-rate", type=float, dest='learn_rate', default=LEARN_RATE)
    creature_group.add_argument("-n", "--neurons", type=int, dest='neurons', default=NEURONS)

    args = parser.parse_args()
    return args


def create_simulation(args):
    if args.load_path:
        return Land.load_from_file(args.load_path)
    else:
        return Land(args.width)


def main():
    args = parse_args()
    land = create_simulation(args)
    land.run()
    land.save_to_file(args.save_path)


if __name__ == '__main__':
    main()
