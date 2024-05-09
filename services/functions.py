def text_by_rows(dictionary: dict[str, int | str]) -> str:
    "Function to convert a dictionary to string and split it by string"
    if not dictionary:
        return "Данные отсутствуют"
    
    max_row_length = 42
    formatted_lines = []
    
    for key, value in dictionary.items():
        sep_number = (len(str(value)[1:]) // 3 if isinstance(value, int) else 0) # number of spaces as delimiter
        current_row_length = len(str(key)) + len(":") + sep_number + len(str(value)) - (1 if isinstance(value, int) and value < 0 else 0)
        space_length = max_row_length - current_row_length
        
        if space_length <= 0:
            formatted_key = key[:len(key) + space_length - 1]
            formatted_length = 1
        else:
            formatted_key = key
            formatted_length = space_length
            
        if isinstance(value, int):
            formatted_value = f"{value:,}".replace(',', ' ')
        else:
            formatted_value = str(value)

        formatted_line = f'<code>{formatted_key}:{" " * formatted_length}{formatted_value}</code>'
        formatted_lines.append(formatted_line)
        
    return '\n'.join(formatted_lines)


def text_by_rows_simple(dictionary: dict[int | str, int | str]) -> str:
    return '\n'.join([f'<b>{key}:</b> {value}' for key, value in dictionary.items()])