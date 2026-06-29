def format_greeting(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"


def get_even_numbers(numbers: list[int]) -> list[int]:
    return [number for number in numbers if number % 2 == 0]


def clamp(value: int, minimum: int, maximum: int) -> int:
    return max(minimum, min(value, maximum))


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            return False
    return True


def flatten(nested_list: list[list[object]]) -> list[object]:
    result = []
    for item in nested_list:
        result.extend(item)
    return result


def average(numbers: list[int | float]) -> float:
    if not numbers:
        raise ValueError("average requires at least one number")
    return sum(numbers) / len(numbers)
