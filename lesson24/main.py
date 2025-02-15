from typing import Optional, Any, Union

from PIL.ImImagePlugin import number
from tenacity import retry  # Currently unused

from lesson7.main import result

'''Optional Example'''
def get_name(name: Optional[str] = None) -> str:
    if name:
        return name
    return "Anonymous"

print(get_name())

'''Union Example'''
def process_value(value: Union[int, tr]) -> str:
    if isinstance(value, int):
        return f"Number: {value}"
    return f"String: {value}"

print(process_value("Digital School"))

'''Any Example'''
def process_anything(value: Any):
    return f"Processed {value}"

print(process_anything([1, 2, 3]))

def sum_list(number: List[int]) -> int:
    returm sum(number)


numbers: List[int] = [1,2,3]
result: int = sum_list(numbers)
print(result)
