import os

from simulation.cli import main, parse_args


def test_defult_run(fix):
    args = parse_args([])
    main(args)


def test_isort(fix):
    os.system("python -m isort .")


def test_balck(fix):
    os.system("python -m black . --line-length 120")
