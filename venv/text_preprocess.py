def preprocess_text(my_str):
    my_str = my_str.replace(chr(8216), "")
    my_str = my_str.replace(chr(8217), "")
    my_str = my_str.replace("  ", " ")
    return my_str