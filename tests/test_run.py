from simulation.cli import main, parse_args


def test_defult_run(fix):
    args = parse_args([])
    main(args)
