import logging

from app.enums import SortingDirection

log = logging.getLogger(__name__)


def sort_data(
    data: list[dict],
    column: str,
    direction: str,
) -> list[dict] | None:

    try:
        direction = SortingDirection(direction.strip().lower())
    except ValueError:
        options = [option.value for option in SortingDirection]
        log.error("Некорректное направление сортировки '%s'. Используйте %s", direction, options)
        return

    try:
        return sorted(
            data,
            key=lambda x: float(x[column]) if x[column].isdigit() else x[column],
            reverse=(direction == SortingDirection.DESC),
        )
    except KeyError:
        log.error("Колонка '%s' не найдена для сортировки", column)
