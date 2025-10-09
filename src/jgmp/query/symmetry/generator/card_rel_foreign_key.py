
from typing import Optional
from jgmp.query.sql.sql_join import SQLJoin
from jgmp.query.sql.sql_query import SQLQuery
from jgmp.query.sql.sql_table_instance import SQLTableInstance
from jgmp.query.symmetry.cardinality_relation import CardinalityRelation, RelationType
from jgmp.query.symmetry.generator.cardinality_relation_generator import CardinalityRelationGenerator
from jgmp.schema.sql.sql_foreign_key import SQLForeignKey
from jgmp.schema.sql.sql_schema import SQLSchema
import random

random.seed(2023)

class CardRelForeignKey(CardinalityRelationGenerator):
    def __init__(self, schema: SQLSchema) -> None:
        super().__init__(schema)

    def generate(self, query: SQLQuery) -> Optional[CardinalityRelation]:
        foreign_query = query.shallow_copy()
        table_instances = query.nodes().copy()
        random.shuffle(table_instances)
        for table_instance in query.nodes():
            table = table_instance.table()
            edges_from = self._schema.edges_from(table)
            if len(edges_from) > 0:
                edge, to_table = random.choice(edges_from)
                to_table_instance = SQLTableInstance.build(self._schema, to_table, [])
                foreign_query.add_node(to_table_instance)
                foreign_query.add_edge(table_instance, SQLJoin(edge), to_table_instance)
                assert(isinstance(edge, SQLForeignKey))
                if any([attribute.nullable() for attribute in edge.foreign_key_attributes()]):
                    return CardinalityRelation([query], [foreign_query], RelationType.GREATEREQUAL)
                else:
                    return CardinalityRelation([query], [foreign_query], RelationType.EQUAL)
        return None
