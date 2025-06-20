Как запустить? 

    1) poetry install
    2) poetry shell

Дальше вводим команды для выборки, к примеру:

    1) python -m app.main --file products.csv --order-by "rating=desc"
    2) python3 -m app.main --file products.csv --where "price>500" --order-by "rating=asc"
    3) python3 -m app.main --file products.csv --aggregate "price=min"

Как запустить тесты?

     python -m pytest -s -v


  Добавил сортировку, старался аннотировать и обрабатывать самые очевидные неверные вводы
пользователем. На счет, добавления нового функционала, вроде бы несложно добавить, но можно было
бы лучше спроектировать.
