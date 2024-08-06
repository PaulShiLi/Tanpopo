import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

from textwrap import dedent
from graphql_query import Argument, Directive, Field, Operation, Query, Variable
from typing import Optional


class GenerateSchema:
    def base() -> tuple[Query, list[Variable]]:
        return Query(
            name="",
        ), []
    
    def page() -> tuple[Query, list[Variable]]:
        variables = [
            Variable(name="page", type="Int"),
            Variable(name="perPage", type="Int"),
            Variable(name="search", type="String")
        ]
        return Query(
            name="Page",
        )

    def generate(
        schemas: list[Query], 
        args: list[Variable] = [
            Variable(
                name="id",
                type="Int"
            )
        ]
    ) -> str:
        operation = Operation(
            type="query",
            name="",
            queries=[
                schemas
            ],
            variables = args
        )
        return operation.render()

view = GenerateSchema.base()

print(GenerateSchema.generate(view))
