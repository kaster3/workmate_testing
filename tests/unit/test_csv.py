def test_csv_read_compare_with_original(sample_csv_file, sample_products):
    from app.core.csv_helper import CSVHelper
    from argparse import Namespace

    args = Namespace(file=sample_csv_file)
    loaded_data = CSVHelper.load(args)

    assert len(loaded_data) == len(sample_products)
    assert loaded_data[0].keys() == sample_products[0].keys()

    for loaded_item, original_item in zip(loaded_data, sample_products):
        assert loaded_item['name'] == original_item['name']
        assert loaded_item['brand'] == original_item['brand']

        assert float(loaded_item['price']) == original_item['price']
        assert float(loaded_item['rating']) == original_item['rating']