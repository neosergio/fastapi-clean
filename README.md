# To Do List Application

## Description

This project is a To Do List application developed with FastAPI, using DynamoDB as the non-relational database. The database infrastructure is managed using AWS CDK, and unit tests are performed using `moto` to simulate DynamoDB.

## Purpose

The purpose of this project is to demonstrate how to build a scalable web application using a clean architecture, integrating FastAPI for the backend, DynamoDB for data storage, and AWS CDK for infrastructure as code. Additionally, it shows how to effectively perform unit tests using `moto` to simulate AWS services.

## Project Structure

```plaintext
.
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── todo.py
│   ├── repositories/
│   │   ├── __init__.py
│   │   ├── todo_repository.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── todo.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── todo_service.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── deps.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── todo.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_todo.py
├── infrastructure/
│   ├── __init__.py
│   ├── localdynamodb.yml
├── .env
├── requirements.txt
```

## Installation
### Prerequisites
- Python 3.8+

### Step-by-Step
1. Clone the repo
2. Set up a virtual environment
3. Install dependencies
4. Configure environment variables
5. Run the app
6. Run the tests

## Usage

You can access the automatic API documentation once the application is running by navigating to http://localhost:8000/docs.

## Contributions

Contributions are welcome. Please open an issue or pull request to discuss any changes you would like to make.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.