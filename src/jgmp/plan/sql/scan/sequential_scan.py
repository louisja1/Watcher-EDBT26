

from typing import FrozenSet, List, Optional
from jgmp.plan.property import Property
from jgmp.plan.sql.scan.scan import Scan
from jgmp.query.graphlike_query import GraphlikeQuery
from jgmp.query.sql.sql_table_instance import SQLTableInstance


class SequentialScan(Scan):
    def __init__(self, table: SQLTableInstance) -> None:
        super().__init__(table, name="seqScan")

    def requires(self,
                 required: FrozenSet[Property],
                 children: List[GraphlikeQuery]) -> Optional[List[FrozenSet[Property]]]:
        if len(required) == 0:
            return []
        return None
