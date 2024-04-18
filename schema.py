import strawberry


def greet():
    return 'Hello World!'


@strawberry.type
class Query:
    hello: str = strawberry.field(resolver=greet)


schema = strawberry.Schema(query=Query)