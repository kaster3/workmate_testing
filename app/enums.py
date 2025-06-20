from enum import Enum


class AggregationFunc(Enum):
    MIN = "min"
    MAX = "max"
    AVG = "avg"


class SortingDirection(Enum):
    ASC = "asc"
    DESC = "desc"


class Flag(Enum):
    FILE = "--file"
    WHERE = "--where"
    AGGREGATE = "--aggregate"
    SORTING = "--order-by"
