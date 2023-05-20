from typing import Dict, Any, Callable, Iterable

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]


def query(data: DataType, selector: ModifierFunc,
          *filters: ModifierFunc) -> DataType:
    a = selector
    result = []
    for row in data:
        b = {}
        for k in row:
            if k in a:
                b[k] = row[k]
        result.append(b)
    # print(result)

    for filter in filters:
        filter_value = []
        # print(filter)
        for i in filter.keys():
            f_key = str(i)
            for j in filter[i]:
                filter_value.append(j)
        # print(f_key, filter_value)
        for row in result:
            if row[f_key] not in filter_value:
                result.remove(row)

    return result

    """
    Query data with column selection and filters

    :param data: List of dictionaries with columns and values
    :param selector: result of `select` function call
    :param filters: Any number of results of `field_filter` function calls
    :return: Filtered data
    """
    pass

def select(*columns: str) -> ModifierFunc:
    """Return function that selects only specific columns from dataset"""
    selected_data = list(columns)
    return selected_data

def field_filter(column: str, *values: Any) -> ModifierFunc:
    """Return function that filters specific column to be one of `values`"""
    filter={}
    filter[column]=values
    return filter

friends = [
    {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'},
    {'name': 'Emily', 'gender': 'female', 'sport': 'volleyball'},
]

# def test_query():
#     friends = [
#         {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'}
#     ]
#     value = query(
#         friends,
#         select(*('name', 'gender', 'sport')),
#         field_filter(*('sport', *('Basketball', 'volleyball'))),
#         field_filter(*('gender', *('male',))),
#     )
#     assert [{'gender': 'male', 'name': 'Sam', 'sport': 'Basketball'}] == value
#
#
# if __name__ == "__main__":
#     test_query()