

from typing import Optional
from jgmp.query.graphlike_query import GraphlikeQuery
from jgmp.query.symmetry.cardinality_relation import CardinalityRelation
from jgmp.query.symmetry.generator.cardinality_relation_generator import CardinalityRelationGenerator


class CardRelMergeMonotonicity(CardinalityRelationGenerator):
    def generate(self, query: GraphlikeQuery) -> Optional[CardinalityRelation]:
        return None
