def text_by_rows(dictionary: dict[str, int | str]) -> str:
    "Function to convert a dictionary to string and split it by string"
    dictionary = {str(key): value for key, value in dictionary.items()}
    
    max_length = max(len(key) + len(str(value)) for key, value in dictionary.items())
    formatted_lines = []
    for key, value in dictionary.items():
        if isinstance(value, int):
            formatted_value = f'{value:,}'.replace(',', ' ')
            # formatted_value = f'{formatted_value:>20}'
        else:
            formatted_value = str(value)
        formatted_line = f'<code>{key}:{" "*(max_length+5-len(key)-len(formatted_value))}{formatted_value}</code>'
        formatted_lines.append(formatted_line)
    return '\n'.join(formatted_lines)


def text_by_rows_simple(dictionary: dict[int | str, int | str]) -> str:
    return '\n'.join([f'<b>{key}:</b> {value}' for key, value in dictionary.items()])