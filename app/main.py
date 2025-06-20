import logging

from app.core.config import LOG_FORMAT
from app.core.csv_helper import CSVHelper
from app.core.parser import Parser

log = logging.getLogger(__name__)


def main() -> None:

    logging.basicConfig(
        level=logging.INFO,
        format=LOG_FORMAT,
    )

    parser = Parser()
    csv_helper = CSVHelper()
    data = csv_helper.load(args=parser.args)
    parser.print_query_result(data)


if __name__ == "__main__":
    main()
