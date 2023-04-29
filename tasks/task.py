from typing import Dict, Any, Callable, Iterable

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]

def query(data: DataType, selector: ModifierFunc,
          *filters: ModifierFunc) -> DataType:
    a = selector
    for filter in filters:
        data = filter(data)
    result=[]
    for dicts in data:
        result_row = {}
        for k in dicts.keys():
            if k in a:
                result_row[k] = dicts[k]
        result.append(result_row)
    return result

    """Return function that selects only specific columns from dataset"""
    """
    Query data with column selection and filters

    :param data: List of dictionaries with columns and values
    :param selector: result of `select` function call
    :param filters: Any number of results of `field_filter` function calls
    :return: Filtered data
    """

def select(*columns: str) -> ModifierFunc:
    return list(columns)
    """Return function that selects only specific columns from dataset"""


def field_filter(column: str, *values: Any) -> ModifierFunc:
    def filter_func(data):
        return [row for row in data if row[column] in values]
    return filter_func
    """Return function that filters specific column to be one of `values`"""
    pass


def test_query():
    friends = [
        {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'},
        {'name': 'Emily', 'gender': 'female', 'sport': 'volleyball'},
    ]
    value = query(
        friends,
        select(*('name', 'gender', 'sport')),
        field_filter(*('sport', *('Basketball', 'volleyball'))),
        field_filter(*('gender', *('male',))),
    )
    assert [{'gender': 'male', 'name': 'Sam', 'sport': 'Basketball'}] == value


if __name__ == "__main__":
    test_query()
