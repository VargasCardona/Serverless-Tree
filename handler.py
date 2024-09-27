import json

def hello(event, context):
    body = {
        "message": "Go Serverless v4.0! Your function executed successfully!",
    }

    response = {"statusCode": 200, "body": json.dumps(body)}
    tree(8, 4, 3)

    return response

def tree(leaf_height: int, trunk_height: int, trunk_width: int) -> None:
    max_width = leaf_height * 2 - 1

    for val in range(leaf_height):
        print(" " * (leaf_height - val), "x" * (val * 2 - 1))
    for val in range(trunk_height):
        print(" " * ((max_width - trunk_width) // 2), "|" * trunk_width)
