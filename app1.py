
"""
Przygotuj listę osób (imię + wiek).
Dla każdego wieku wyznacz imiona osób w tym wieku.
"""

from dataclasses import dataclass
from collections import defaultdict

@dataclass
class Person:
    name: str
    age: int

def main() -> None:
    people = [
        Person("ADAM", 23),
        Person("EWA", 25),
        Person("IZA", 23),
        Person("OLA", 27),
        Person("JAN", 27),
        Person("KASIA", 25),
        Person("PAWEL", 23)
    ]

grouped_names_by_age = defaultdict(list)
for person in people:
    grouped_names_by_age[person.age].append(person.name)

[print(f'{a} => {n}') for a, n in grouped_names_by_age.items()]

if __name__ == '__main__':
    main()