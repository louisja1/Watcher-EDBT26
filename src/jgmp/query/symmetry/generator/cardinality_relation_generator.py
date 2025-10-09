

from abc import abstractmethod
from typing import Optional
from jgmp.query.graphlike_query import GraphlikeQuery
from jgmp.query.symmetry.cardinality_relation import CardinalityRelation
from jgmp.schema.graphlike_schema import GraphlikeSchema


class CardinalityRelationGenerator:
    def __init__(self, schema: GraphlikeSchema) -> None:
        self._schema = schema

    @abstractmethod
    def generate(self, query: GraphlikeQuery) -> Optional[CardinalityRelation]:
        pass
