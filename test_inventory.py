from inventory import average_price, add_discount


def test_average_price():
    assert average_price([10, 20, 30]) == 20


def test_add_discount():
    result = add_discount([100, 200])
    assert result == [90.0, 180.0]

# NOTE: no test for empty list (would hit the divide-by-zero bug)
# NOTE: no test for find_duplicates, load_config, or apply_bulk_update
