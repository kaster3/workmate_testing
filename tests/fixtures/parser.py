import os
import csv
import sys
import tempfile

import pytest

from app.core.parser import Parser


@pytest.fixture(scope="class")
def parser() -> Parser:
    """
    Этот код из чата гпт, я тут, честно говоря, запутался, мои флаги с пайтеста (-v, -s)
    переходили в мой Parser и тесты проходили неверно, я не знал, как это решить
    """

    # Сохраняем оригинальные аргументы
    original_argv = sys.argv.copy()

    # Очищаем аргументы командной строки
    sys.argv = [sys.argv[0]]  # Оставляем только имя программы

    # Создаем парсер (теперь он не увидит флаги pytest)
    p = Parser()

    # Восстанавливаем аргументы
    sys.argv = original_argv

    yield p


@pytest.fixture
def sample_csv_file(sample_products) -> str:
    with tempfile.NamedTemporaryFile(mode='w+', suffix='.csv', delete=False) as tmp:
        writer = csv.DictWriter(tmp, fieldnames=sample_products[0].keys())
        writer.writeheader()
        writer.writerows(sample_products)
        tmp_path = tmp.name
    yield tmp_path
    os.unlink(tmp_path)


@pytest.fixture
def sample_products() -> list[dict[str, str | int | float]]:
    return [
        {"name": "iphone 15 pro", "brand": "apple", "price": 999, "rating": 4.9},
        {"name": "galaxy s23 ultra", "brand": "samsung", "price": 1199, "rating": 4.8},
        {"name": "redmi note 12", "brand": "xiaomi", "price": 199, "rating": 4.6},
        {"name": "iphone 14", "brand": "apple", "price": 799, "rating": 4.7},
        {"name": "galaxy a54", "brand": "samsung", "price": 349, "rating": 4.2},
        {"name": "poco x5 pro", "brand": "xiaomi", "price": 299, "rating": 4.4},
        {"name": "iphone se", "brand": "apple", "price": 429, "rating": 4.1},
        {"name": "galaxy z flip 5", "brand": "samsung", "price": 999, "rating": 4.6},
        {"name": "redmi 10c", "brand": "xiaomi", "price": 149, "rating": 4.1},
        {"name": "iphone 13 mini", "brand": "apple", "price": 599, "rating": 4.5},
    ]


@pytest.fixture
def sample_products_for_sorting():
    return [
        {"name": "B", "price": "300", "rating": "4.5"},
        {"name": "A", "price": "200", "rating": "4.2"},
        {"name": "C", "price": "100", "rating": "4.7"}
    ]

