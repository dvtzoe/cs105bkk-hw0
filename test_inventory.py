from inventory import add_item, running_low, total_items


def test_core_add_item_new_item_starts_at_one():
    assert add_item({}, "potion") == {"potion": 1}


def test_core_add_item_adds_to_an_existing_item():
    assert add_item({"arrow": 10}, "arrow", 5) == {"arrow": 15}


def test_core_add_item_leaves_the_original_alone():
    bag = {"potion": 3}
    result = add_item(bag, "potion")
    assert bag == {"potion": 3}
    assert result is not bag


def test_core_total_items_across_inventories():
    assert total_items({"potion": 3, "arrow": 12}, {"shield": 1}) == 16


def test_core_total_items_with_no_inventories():
    assert total_items() == 0


def test_core_running_low_uses_the_default_limit():
    assert running_low({"potion": 1, "arrow": 12, "key": 0}) == ["key", "potion"]


def test_core_running_low_leaves_out_a_count_equal_to_the_limit():
    assert running_low({"potion": 2, "map": 1}) == ["map"]
