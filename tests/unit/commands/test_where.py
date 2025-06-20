import pytest

from app.commands.where import filter_data
from tests.fixtures.parser import sample_products


class TestFilterData:
    @pytest.mark.parametrize("column,operator,value,expected_count", [
        ("price", ">", "500", 5),
        ("price", "<", "500", 5),
        ("price", "=", "799", 1),
        ("rating", ">", "4.5", 5),
        ("rating", "<", "4.2", 2),
        ("rating", "=", "4.2", 1),
    ])
    def test_filter_operations(self, sample_products, column, operator, value, expected_count):
        result = filter_data(sample_products, column, operator, value)
        assert len(result) == expected_count

    def test_empty_data(self):
        result = filter_data([], "price", ">", "100")
        assert len(result) == 0

    # value error
    @pytest.mark.parametrize("wrong_column", [
        "rsing",
        "prici",
        "pr",
    ])
    def test_invalid_column(self, sample_products, caplog, wrong_column):
        filter_data(sample_products, wrong_column, ">", "100")
        assert f"Столбца с именем '{wrong_column}' не существует в файле" in caplog.text

    # key error
    def test_invalid_comparison(self, sample_products, caplog):
        result = filter_data(sample_products, "name", ">", "100")
        assert len(result) == 0
        assert "Ошибка сравнения" in caplog.text
