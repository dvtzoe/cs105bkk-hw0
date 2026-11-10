"""HW0: a game inventory. Practises Session 1: names and objects, defaults, *args, comprehensions."""

import copy

def add_item(inventory, item, count=1):
    """Return a new inventory with count more of item. Do not change inventory."""

    new_inventory = copy.deepcopy(inventory)

    if item in new_inventory:
        new_inventory[item] += count
    else:
        new_inventory[item] = count

    return new_inventory

    # raise NotImplementedError("core: return a new inventory with the item added")


def total_items(*inventories):
    """Return how many items there are in all the inventories together."""
    
    sum = 0

    for inventory in inventories:
        for count in inventory.values():
            sum += count

    return sum

    # raise NotImplementedError("core: add up the items in every inventory")


def running_low(inventory, limit=2):
    """Return the names of items with fewer than limit left, sorted A to Z."""

    items_running_low = []

    for item, count in inventory.items():
        if count < limit:
            items_running_low.append(item)

    return sorted(items_running_low)

    # raise NotImplementedError("core: list the items running low")
