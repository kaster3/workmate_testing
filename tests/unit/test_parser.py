import pytest


class TestParser:
    @pytest.mark.parametrize(
        "input_str,need_operator,expected",
        [
            ("rating>1000", True, ("rating", ">", "1000")),
            ("price<500", True, ("price", "<", "500")),
            ("name=test", True, ("name", "=", "test")),
            ("rating=desc", False, ("rating", "desc")),
            ("price=asc", False, ("price", "asc")),
            ("price=avg", False, ("price", "avg")),
        ],
    )
    def test_separate_by_operator(self, parser, input_str, need_operator, expected):
        assert parser._separate_by_operator(input_str, need_operator) == expected

    @pytest.mark.parametrize(
        "invalid_input",
        [
            "rating",
            ">1000",
            "rating<>1000",
            "rating>",
            "rating asc",
            "price123",
            "insd100",
        ],
    )
    def test_invalid_formats(self, parser, invalid_input):
        with pytest.raises(ValueError):
            parser._separate_by_operator(invalid_input)
