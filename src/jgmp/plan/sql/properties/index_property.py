

from jgmp.plan.property import Property
from jgmp.plan.sql.properties.column_property import ColumnProperty
from jgmp.plan.sql.properties.sorted_property import SortedProperty
from jgmp.query.sql.sql_table_instance import SQLTableInstance
from jgmp.schema.attribute import Attribute


class IndexProperty(ColumnProperty):
    def __init__(self, table: SQLTableInstance, attribute: Attribute) -> None:
        super().__init__("Index", table, attribute)

    def includes(self, other: Property) -> bool:
        if isinstance(other, IndexProperty) or isinstance(other, SortedProperty):
            return self.same_column(other)
        return False
