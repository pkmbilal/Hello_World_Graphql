import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter


def greet():
    return 'Hello World!'


@strawberry.type
class Query:
    hello: str = strawberry.field(resolver=greet)


schema = strawberry.Schema(query=Query)


graphql_app = GraphQLRouter(schema)


app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")