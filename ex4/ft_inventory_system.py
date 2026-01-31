import sys


def main():
    inventory = dict()

    if len(sys.argv) < 2:
        print("Usage: python3 ft_inventory_system.py item:qty item:qty")
        return

    for arg in sys.argv[1:]:
        if ':' not in arg:
            continue
        parts = arg.split(':')
        name = parts[0]
        try:
            qty = int(parts[1])
        except ValueError:
            continue

        current_qty = inventory.get(name, 0)
        inventory.update({name: current_qty + qty})

    if not inventory:
        print("Inventory is empty!")
        return

    total_items = 0
    for v in inventory.values():
        total_items += v

    unique_items = len(inventory)

    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_items}\n")

    items_list = [[k, v] for k, v in inventory.items()]

    n = len(items_list)
    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            if items_list[j+1][1] > items_list[j][1]:
                temp = items_list[j]
                items_list[j] = items_list[j+1]
                items_list[j+1] = temp
            j += 1
        i += 1

    print("=== Current Inventory ===")
    for item in items_list:
        name = item[0]
        val = item[1]
        percent = (val / total_items) * 100 if total_items > 0 else 0
        print(f"{name}: {val} units ({percent:.1f}%)")

    print("\n=== Inventory Statistics ===")
    print(f"Most abundant: {items_list[0][0]} ({items_list[0][1]} units)")
    print(f"Least abundant: {items_list[-1][0]} ({items_list[-1][1]} unit)")

    print("\n=== Item Categories ===")
    moderate = dict()
    scarce = dict()

    for k, v in inventory.items():
        if v >= 5:
            moderate.update({k: v})
        else:
            scarce.update({k: v})

    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")

    print("\n=== Management Suggestions ===")
    restock = [k for k in inventory.keys() if inventory[k] < 2]
    print(f"Restock needed: {restock}")


if __name__ == "__main__":
    main()
