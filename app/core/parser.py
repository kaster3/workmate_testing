import argparse
import logging
import re
import sys

from tabulate import tabulate

from app.commands.aggregate import aggregate
from app.commands.sorting import sort_data
from app.commands.where import filter_data
from app.core.config import SEPARATE_PATTERN
from app.enums import Flag

log = logging.getLogger(__name__)


class Parser:
    def __init__(self) -> None:
        """
        Инициализация самого парсера, обработка кастомной ошибки, о ней я пишу ниже
        и здесь же идет присвоение всех доступных аргументов их класса Enum
        """
        self.parser = argparse.ArgumentParser()
        self.parser.error = self._custom_error_handler

        for flag in list(Flag):
            self.parser.add_argument(flag.value)

        self.args = self.parser.parse_args()

    def print_query_result(self, data) -> None:
        """
        Тут идет основная логика выборки данных, выборка меняется после каждого if,
        если флаг был введен пользователем
        """
        try:

            if self.args.where:
                column, operator, value = self._separate_by_operator(self.args.where)
                data = filter_data(data, column, operator, value)

            if self.args.order_by:
                column, direction = self._separate_by_operator(
                    self.args.order_by, need_operator=False
                )
                data = sort_data(data, column, direction)

            if self.args.aggregate:
                column, operation = self._separate_by_operator(
                    self.args.aggregate, need_operator=False
                )
                data = aggregate(data, column, operation)
                data = [[f"{operation}({column})"], [data]]

        except ValueError as ex:
            if not data:
                log.warning("Данных нет")
            else:
                log.error("%s", ex)
            return

        headers = "keys" if not self.args.aggregate else ""
        print(tabulate(data, headers=headers, tablefmt="grid"))

    @staticmethod
    def _custom_error_handler(message: str) -> None:
        """
        Кастомный обработчик ошибок argparse, на случай, если ввели неверный флаг,
        допустим не --where, а --wheha, сравнивая флаг с допустимыми в Enum
        """
        if "unrecognized arguments" in message:
            unrecognized = message.split("unrecognized arguments:")[1].strip()
            log.error(f"Неизвестная команда или аргумент: {unrecognized}")
            available_flags = [flag.value for flag in Flag]
            log.info("Доступные команды: %s", available_flags)
        else:
            log.error(message)
        sys.exit()

    @staticmethod
    def _separate_by_operator(
        argument: str,
        need_operator: bool = True,
    ) -> tuple[str, str, str] | tuple[str, str]:
        """
        Помогает разделять и возвращать, введенное значение пользователем (rating>1000)
        на название колонки (rating), значение (1000) и оператор(>), если стоит флаг
        need_operator = True
        """

        match = re.match(SEPARATE_PATTERN, argument)
        if not match:
            raise ValueError(f"Некорректный формат условия: {argument}")

        column = match.group(1).strip()
        operator = match.group(2)
        value = match.group(3).strip()

        if need_operator is True:
            return column, operator, value
        return column, value
