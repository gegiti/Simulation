
from src.main import main, parse_args


def test_defult_run(fix):
    args, unknown = parse_args()
    main()
