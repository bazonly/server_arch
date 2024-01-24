import datetime

from abc import abstractmethod
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    description: str
    publish_year: datetime.datetime
    pages_count: int
    created_at: datetime.datetime
