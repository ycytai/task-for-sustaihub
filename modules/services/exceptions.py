from dataclasses import dataclass


@dataclass
class ExceedDataRangeError(Exception):
    start: str | None = None
    end: str | None = None

    def __str__(self):
        if self.start and self.end:
            return f'Data range should between {self.start} and {self.end}'
        elif self.start:
            return f'Data range should after {self.start}.'
        elif self.end:
            return f'Data range should before {self.end}.'
