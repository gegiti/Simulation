from simulation.cli import parse_args, main


def test_defult_run(fix):
    args = parse_args([])
    main(args)
