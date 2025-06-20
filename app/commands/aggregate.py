import logging
import sys

from app.enums import AggregationFunc

log = logging.getLogger(__name__)


def aggregate(data: dict[str:str], column: str, operator: str) -> int | float | None:

    try:
        AggregationFunc(operator)
    except ValueError:
        log.error("Ошибка агрегации, функции '%s' не существует", operator)
        sys.exit()

    operations = {
        AggregationFunc.AVG.value: lambda x: round(sum(x) / len(x), 2),
        AggregationFunc.MIN.value: lambda x: min(x),
        AggregationFunc.MAX.value: lambda x: max(x),
    }

    try:
        values = [float(row[column]) for row in data]
    except (ValueError, KeyError):
        return None

    return operations[operator](values)
