from typing import Dict, Any, Callable, Iterable

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]

def query(data: DataType, selector: ModifierFunc,
          *filters: ModifierFunc) -> DataType:
    filtered_data = selector(data)
    for filter in filters:
        filtered_data = filter(filtered_data)
    return filtered_data
    pass

def select(*columns: str) -> ModifierFunc:
    """Return function that selects only specific columns from dataset"""
    selected_data = list(columns)
    def select_core(data):
        result = []
        for row in data:
            b = {}
            for k in row:
                if k in selected_data:
                    b[k] = row[k]
            result.append(b)
        return result
    return select_core
    pass

def field_filter(column: str, *values: Any) -> ModifierFunc:
    """Return function that filters specific column to be one of `values`"""
    flt_key = column
    flt_values = values
    def filter_core(data):
        filtered_list = []
        for row in data:
            if (flt_key in row.keys() and row[flt_key] in flt_values) or not (flt_key in row.keys()):
                filtered_list.append(row)
        data = filtered_list
        return data
    return filter_core
    pass

friends = [
    {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'},
    {'name': 'Emily', 'gender': 'female', 'sport': 'volleyball'},
]