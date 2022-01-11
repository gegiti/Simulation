import logging

from simulation.cli import main, parse_args

if __name__ == "__main__":
    args = parse_args()
    try:
        main(args)
    except:
        logging.exception("An unhandled exception has occured:")
