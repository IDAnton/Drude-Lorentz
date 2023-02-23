from Data import MAX_MODES


def get_charge_name_list():
    charge_list = ["Свободный заряд"]
    for i in range(0, MAX_MODES):
        charge_list.append(f"Связанный заряд №{i + 1}")
    return charge_list
