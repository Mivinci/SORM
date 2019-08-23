from time import localtime, struct_time
from typing import Union, Callable

fill_zero: Callable[[int], Union[str, int]] = lambda n: n if n > 9 else f"0{n}"


def stringify(lt: Union[struct_time, struct_time]) -> str:
    return f"{lt.tm_year}" \
           f"-{fill_zero(lt.tm_mon)}" \
           f"-{fill_zero(lt.tm_mday)}" \
           f" {fill_zero(lt.tm_hour)}" \
           f":{fill_zero(lt.tm_min)}" \
           f":{fill_zero(lt.tm_sec)}"


now: Callable[[], str] = lambda: stringify(localtime())
