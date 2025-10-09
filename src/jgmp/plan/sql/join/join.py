
from jgmp.plan.property import Property
from jgmp.query.graphlike_query import GraphlikeQuery
from jgmp.query.sql.sql_join import SQLJoin
from jgmp.query.sql.sql_table_instance import SQLTableInstance
from typing import List, Tuple, FrozenSet, Optional
from jgmp.plan.operator import Operator


class Join(Operator):
    def __init__(self, join_conditions: List[Tuple[SQLTableInstance, SQLJoin, SQLTableInstance, bool]], name: str = "join") -> None:
        edges = [(from_node, edge, to_node) for from_node, edge, to_node, _ in join_conditions]
        super().__init__(name, 2, [], edges)
        self._join_conditions = join_conditions

    def join_conditions(self) -> List[Tuple[SQLTableInstance, SQLJoin, SQLTableInstance, bool]]:
        return self._join_conditions

    def requires(self,
                 required: FrozenSet[Property],
                 children: List[GraphlikeQuery]) -> Optional[List[FrozenSet[Property]]]:
        return [frozenset(), frozenset()]
