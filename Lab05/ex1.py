print("""
+-------------------------------------------+
|    Program Name: Count Unique Item        |      
|    Coded by: Tashi Dorji Tamang           |
|    Language used: Python (3.11.3)         |
|    Remark: Lab05 (Exercise 1)             |
+-------------------------------------------+
""")


def main():
    country_list = ['Australia', 'Japan', 'India', 'Bhutan', 'Japan', 'India', 'Australia', True, 0, False, 1, True]

    shopping_list = ['Apple', 'Potato', 'Diaper', 'Rice', 'Salt', 'Rice', 'Diaper', 'Potato']

    car_list = ['Toyota', 'Tesla', 'Ford', 'Hyundai', 'Renault', 'Ford', 'Audi', 'Tesla', 'Toyota']

    final_list = [country_list, shopping_list, car_list]

    for i in final_list:
        count_unique_item_inside_list(i)


def count_unique_item_inside_list(_list):
    true_or_false_list = []
    temp_list = []

    for item in _list:
        if type(item) == bool and item not in true_or_false_list:
            true_or_false_list.append(item)

        if type(item) != bool and item not in temp_list:
            temp_list.append(item)

    temp_list.extend(true_or_false_list)

    print(f"There are {len(temp_list)} unique items inside {_list}")


# calling the main function
main()
