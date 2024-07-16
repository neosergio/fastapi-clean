from uuid import uuid4

import boto3
from botocore.exceptions import ClientError

from app.core.config import settings
from app.models.todo import TodoModel
from app.schemas.todo import TodoCreate, TodoUpdate

dynamodb = boto3.resource(
    'dynamodb',
    region_name=settings.REGION_NAME,
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    endpoint_url=settings.ENDPOINT_URL
)
table = dynamodb.Table(settings.DYNAMODB_TABLE)


def create_todo(todo: TodoCreate):
    todo_id = str(uuid4())
    item = {
        'id': todo_id,
        'title': todo.title,
        'description': todo.description,
        'completed': False
    }
    try:
        table.put_item(Item=item)
        return TodoModel(**item)
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None


def get_todo_by_id(todo_id: str):
    try:
        response = table.get_item(Key={'id': todo_id})
        return TodoModel(**response['Item'])
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None


def get_all_todos():
    try:
        response = table.scan()
        items = response.get('Items', [])
        return [TodoModel(**item) for item in items]
    except ClientError as e:
        print(e.response['Error']['Message'])
        return []


def update_todo(todo_id: str, todo: TodoUpdate):
    update_expression = "set "
    expression_attribute_values = {}
    if todo.title is not None:
        update_expression += "title = :title, "
        expression_attribute_values[':title'] = todo.title
    if todo.description is not None:
        update_expression += "description = :description, "
        expression_attribute_values[':description'] = todo.description
    if todo.completed is not None:
        update_expression += "completed = :completed, "
        expression_attribute_values[':completed'] = todo.completed

    if update_expression.endswith(", "):
        update_expression = update_expression[:-2]

    try:
        response = table.update_item(
            Key={'id': todo_id},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values,
            ReturnValues="ALL_NEW"
        )
        return TodoModel(**response['Attributes'])
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None


def delete_todo_by_id(todo_id: str):
    try:
        table.delete_item(Key={'id': todo_id})
        return True
    except ClientError as e:
        print(e.response['Error']['Message'])
        return False
