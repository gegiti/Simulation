import argparse

from simulation.core import Simulation


def parse_args(args=None):
    parser = argparse.ArgumentParser(prog="simulation.py", description="Evolution Simulation:")

    program_group = parser.add_argument_group("program")
    program_group.add_argument("-v", "--video-path", dest="video_path", default="simulation.mp4")
    program_group.add_argument("-l", "--log", dest="log_path")
    program_group.add_argument("-a", "--log-actions", action="store_true", dest="log_actions")

    simulation_group = parser.add_argument_group("simulation")
    simulation_group.add_argument("-t", "--simulation-time", type=int, dest="ttl", default=1000)
    simulation_group.add_argument("--land-width", type=int, dest="land_width", default=50)
    simulation_group.add_argument("--land-height", type=int, dest="land_height", default=50)
    simulation_group.add_argument("-p", "--creature-percentage", type=float, dest="creature_percent", default=1 / 2500)

    creature_group = parser.add_argument_group("creature")
    creature_group.add_argument("-r", "--learning-rate", type=float, dest="learn_rate", default=0.03)
    creature_group.add_argument("--layers", type=int, nargs="+", dest="layers", default=[3, 3, 3])

    args = parser.parse_args(args=args)
    print(args.layers)
    print(type(args.layers))

    if args.log_actions and not args.log_path:
        parser.error("Actions are only logged to the file, it is not possible to log actions without -l\\--log.")

    return args


def create_simulation(args):
    simulation_args = (
        args.ttl,
        args.creature_percent,
        args.land_width,
        args.land_height,
        args.video_path,
        args.log_path,
        args.log_actions,
    )
    land_args = args.land_width, args.land_height
    creature_args = args.layers, args.learn_rate
    return Simulation(simulation_args, land_args, creature_args)


def main(args):
    sim = create_simulation(args)
    sim.run()
