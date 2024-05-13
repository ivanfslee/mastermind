import random
import urllib.request
from urllib.error import HTTPError, URLError


def generate_random_numbers(count: int, min_val: int, max_val: int) -> list[int]:
    """Gets random numbers from random.org API or generates random numbers using the random module if the API is down."""
    try:
        url: str = (
            f"https://www.random.org/integers/?num={count}&min={min_val}&max={max_val}&col=1&base=10&format=plain&rnd=new"
        )

        response = urllib.request.urlopen(url)
        response_data: str = response.read().decode("utf-8")

        numeric_strings: list[str] = response_data.strip().split("\n")
        random_numbers: list[int] = [int(num_str) for num_str in numeric_strings]

        print("Generating random numbers using random.org API")
        return random_numbers

    except (HTTPError, URLError) as e:
        print("Network error occurred: ", e)
        print("Generating random numbers using random module instead.")
        random_numbers: list[int] = [
            random.randint(min_val, max_val) for _ in range(count)
        ]
        return random_numbers
    except Exception as e:
        print("Error in getting random numbers: ", e)
