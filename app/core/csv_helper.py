import csv
import logging
from argparse import Namespace

log = logging.getLogger(__name__)


class CSVHelper:
    """
    Скорее всего тут класс излишен, думал мб еще добавить методов в будущем
    и логически классом их связать, но пока топчу yagni и kiss)))
    """

    @staticmethod
    def load(args: Namespace) -> list[dict[str, str]]:
        try:
            with open(file=args.file, mode="r", encoding="utf-8") as file:
                return list(csv.DictReader(file))
        except FileNotFoundError:
            log.error(f"Ошибка: файл {args.file} не найден")
