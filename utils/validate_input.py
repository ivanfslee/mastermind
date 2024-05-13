def is_valid_code(code_str: str, count, min_val, max_val) -> bool:

    numeric_strings: list[str] = [num_str for num_str in code_str.split(" ")]

    if len(numeric_strings) != count:
        raise ValueError(
            f"You must enter {count} number(s). Each number separated by a single space."
        )

    for num_str in numeric_strings:

        if num_str.isdigit() is False:
            raise ValueError(f"All numbers must be integers.")

        num = int(num_str)
        if num < min_val or num > max_val:
            raise ValueError(f"All numbers must be between {min_val} and {max_val}.")

    return True


def is_valid_1or2(user_input: str) -> bool:
    if not user_input.isdigit():
        raise ValueError("Value must be an integer.")
    elif int(user_input) < 1 or int(user_input) > 2:
        raise ValueError("Value must be 1 or 2.")
    return True
