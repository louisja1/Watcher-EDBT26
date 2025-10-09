import abc
from typing import Any
from jgmp.schema.attributable import Attributable
from jgmp.schema.attribute import Attribute


class ValuePicker:
    @abc.abstractmethod
    def pick_random(self, entity: Attributable, attribute: Attribute) -> Any:
        pass
