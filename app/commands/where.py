import logging

log = logging.getLogger(__name__)


def filter_data(
    data: list[dict[str, str]],
    column: str,
    operator: str,
    value: str,
) -> list[dict[str, str]]:
    operations = {
        ">": lambda a, b: a > b,
        "<": lambda a, b: a < b,
        "=": lambda a, b: a == b,
    }
    try:
        value = float(value)
        converter = float
    except ValueError:
        converter = str

    result = []
    for row in data:
        try:
            if operations[operator](converter(row[column]), value):
                result.append(row)
        except KeyError:
            log.error("Столбца с именем '%s' не существует в файле", column)
            break
        except ValueError:
            log.error("Ошибка сравнения, сравниваем колонку '%s' cо значением '%d'", column, value)
            break
    return result
