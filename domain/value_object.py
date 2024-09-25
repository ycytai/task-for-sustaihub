from pydantic import BaseModel, ConfigDict


class ValueObject(BaseModel):
    """
    1. Immutability:
        Value objects are immutable, meaning their state cannot be changed once they are created.
        Any modification results in a new value object.

    2. Equality by Value:
        Equality of value objects is based on their attribute values rather than their identity.
        Two value objects with the same attribute values are considered equal.

    3. No Identity:
        Value objects do not have a unique identity; they are defined solely by their attributes.

    4. Shared and Immutable:
        Value objects are typically shared and can be reused across multiple entities or aggregates.

    5. Side-Effect Free: Value objects should not have any side effects or interactions with
        the outside world. They are purely used for representing data.
    """

    model_config = ConfigDict(frozen=True)

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        return all(self.__dict__.get(k) == other.__dict__.get(k) for k in self.__dict__)

    def __hash__(self):
        attrs = [str(getattr(self, key)) for key in sorted(self.model_fields.keys())]
        return hash(''.join(attrs))
