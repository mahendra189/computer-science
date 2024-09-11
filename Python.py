import threading
import asyncio
import contextlib
from typing import List, Optional
from dataclasses import dataclass, field

# Data Class Example
@dataclass
class Data:
    value: int
    name: str = "Default"

# Custom Context Manager
@contextlib.contextmanager
def managed_resource():
    print("Resource acquired")
    try:
        yield
    finally:
        print("Resource released")

# Descriptor Example
class Descriptor:
    def __get__(self, instance, owner):
        return f"Descriptor accessed from {owner}"

# Custom Iterator
class Counter:
    def __init__(self, low: int, high: int):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        self.current += 1
        return self.current - 1

# Metaclass Example
class Meta(type):
    def __new__(cls, name, bases, dct):
        dct['meta_data'] = 'Meta class attribute'
        return super().__new__(cls, name, bases, dct)

class Example(metaclass=Meta):
    pass

# Asynchronous Function
async def async_example():
    print("Start async")
    await asyncio.sleep(1)
    print("End async")

# Function with Type Hints
def process_data(data: List[Data]) -> Optional[Data]:
    return data[0] if data else None

# Threading Example
def thread_task():
    print("Thread running")

# Main Function
def main():
    # Data Class Usage
    data_instance = Data(value=42)
    print(data_instance)

    # Context Manager Usage
    with managed_resource():
        print("Inside context")

    # Descriptor Usage
    class ExampleWithDescriptor:
        attr = Descriptor()

    print(ExampleWithDescriptor.attr)

    # Iterator Usage
    for num in Counter(1, 5):
        print(num)

    # Metaclass Usage
    example_instance = Example()
    print(Example.meta_data)

    # Asyncio Usage
    asyncio.run(async_example())

    # Function with Type Hints
    data_list = [Data(value=1), Data(value=2)]
    print(process_data(data_list))

    # Threading Usage
    thread = threading.Thread(target=thread_task)
    thread.start()
    thread.join()

if __name__ == "__main__":
    main()
