

import random
from typing import List
from jgmp.query.graphlike_query import GraphlikeQuery
from jgmp.query.query_generator import QueryGenerator

random.seed(2023)

class QueryGeneratorChoice(QueryGenerator):
    def __init__(self, queries: List[GraphlikeQuery]) -> None:
        super().__init__()
        self._queries = queries

    def generate_query_default(self) -> GraphlikeQuery:
        return random.choice(self._queries)
