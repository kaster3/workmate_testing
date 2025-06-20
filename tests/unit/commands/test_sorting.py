import pytest
from app.commands.sorting import sort_data
from app.enums import SortingDirection

from tests.fixtures.parser import sample_products, sample_products_for_sorting


class TestSortData:
    @pytest.mark.parametrize("column,direction,expected_order", [
        ("name", "asc", ["A", "B", "C"]),
        ("name", "desc", ["C", "B", "A"]),
        ("price", "asc", ["100", "200", "300"]),
        ("price", "desc", ["300", "200", "100"]),
        ("rating", "asc", ["4.2", "4.5", "4.7"]),
        ("rating", "desc", ["4.7", "4.5", "4.2"]),
    ])
    def test_valid_sorting(self, sample_products_for_sorting, column, direction, expected_order) -> None:
        result = sort_data(sample_products_for_sorting, column, direction)
        assert [item[column] for item in result] == expected_order

    @pytest.mark.parametrize("wrong_direction", [
        "cesc",
        "descc",
        "acd",
    ])
    def test_invalid_direction(self, sample_products, caplog, wrong_direction) -> None:
        result = sort_data(sample_products, "name", wrong_direction)

        assert result is None
        assert "Некорректное направление сортировки" in caplog.text
        assert SortingDirection.ASC.value in caplog.text
        assert SortingDirection.DESC.value in caplog.text


    @pytest.mark.parametrize("wrong_column", [
        "brant",
        "proce",
        "ranting",
        "namee"
    ])
    def test_missing_column(self, sample_products, caplog, wrong_column) -> None:
        result = sort_data(sample_products, wrong_column, "asc")

        assert result is None
        assert f"Колонка '{wrong_column}' не найдена для сортировки" in caplog.text
