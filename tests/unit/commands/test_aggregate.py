import pytest

from app.commands.aggregate import aggregate
from app.enums import AggregationFunc


class TestAggregate:
    @pytest.mark.parametrize(
        "column,operator,expected",
        [
            ("price", AggregationFunc.AVG.value, 602.0),
            ("price", AggregationFunc.MIN.value, 149),
            ("price", AggregationFunc.MAX.value, 1199),
            ("rating", AggregationFunc.AVG.value, 4.49),
            ("rating", AggregationFunc.MIN.value, 4.1),
            ("rating", AggregationFunc.MAX.value, 4.9),
        ],
    )
    def test_aggregate_operations(
        self,
        sample_products: list[dict[str, str | int | float]],
        column: str,
        operator: str,
        expected: int | float,
    ) -> None:
        result = aggregate(sample_products, column, operator)
        assert result == pytest.approx(expected, abs=0.01)

    @pytest.mark.parametrize(
        "column,operator",
        [
            ("price", "ma"),
            ("price", "ci"),
            ("price", "mac"),
            ("rating", "avt"),
            ("rating", "avt"),
            ("rating", "a"),
            ("rating", "mi"),
            ("rating", "mind"),
        ],
    )
    def test_invalid_operator(self, sample_products, column, operator):
        with pytest.raises(SystemExit):
            aggregate(sample_products, column, operator)
