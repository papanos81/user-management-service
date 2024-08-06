from neo4j import GraphDatabase
from datetime import datetime
import neo4j

URI = "neo4j://localhost:7687"
AUTH = ("neo4j", "Kidos1416")

user = {
    'name': 'MIFI',
    'lastname': 'MIFOU',
    'age': 42,
    'created_at': datetime.now()
}

def get_connection():
    return GraphDatabase.driver(URI, auth=AUTH)


def save(query, param):
    with get_connection() as driver:
        with driver.session(default_access_mode=neo4j.WRITE_ACCESS) as session:
            tx = session.begin_transaction()
            result = tx.run(query, params=param, name="default").data()
            print(result)
            tx.commit()        

def get_data(query):
    with get_connection() as driver:
        with driver.session() as session:
            tx = session.begin_transaction()
            result = tx.run(query).data()
            [print(i) for i in result]


def create_user():
    query = "CREATE(e: Person $params) return e"
    return query

def create_host():
    query = "CREATE(e: Host $params) return e"
    return query

def get_user():
    query = "MATCH(n:Person ) return n"
    return query

def get_host():
    query = "MATCH(n:Host ) return n"
    return query


if __name__ == '__main__':
    # save(create_host(), user)
    get_data(get_host())