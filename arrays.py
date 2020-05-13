def find_missing_integer_array(missing_array):
    """Array from 1 to X, ascending order containing one missing integer
    """
    array_len = len(missing_array) + 1 #include extra for missing integer.
    missing_integer = int((array_len * (array_len + 1)) / 2) - sum(missing_array)
    return missing_integer
