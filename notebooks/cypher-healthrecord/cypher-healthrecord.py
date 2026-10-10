from wowool.sdk import Pipeline
from wowool.document import Document
from pathlib import Path


pipeline = Pipeline(
    [
        "english",
        "entity",
        "healthcare",
        {
            "name": "snippet.app",
            "options": 
                {
                    "source": """
                        rule:{ "#Patient(.)+" } = Patient; 
                        rule:{ "Age" ":" {<>} = AgeGroup};
                    """,
                },
        },
        {
            "name": "entity-graph.app",
            "options": {
                  "nodes": {
                     "_Patient": { "name": "Patient", "store": "first_seen"},
                     "_HealthIssue": { "name": "HealthIssue.lemma.lower()", "label": "HealthIssue"},
                     "_AgeGroup": { "name": "AgeGroup.literal", "label": "AgeGroup"},
                },
                "links": [
                    {"from": "HealthIssue", "to": "Drug", "relation":"TREATMENT"},
                    {"from": "_Patient", "relation": "HAS_SYMPTOM", "to": "_HealthIssue"},
                    {"from": "_Patient", "relation": "TAKES", "to": "Drug"},
                    {"from": "_Patient", "relation": "AGE", "to": "_AgeGroup"},
                ]

            },
        },
        {
            "name": "cypher.app",
            "options": {
                "namespace": "MySpace",
                "collection": "MyCollection",
                "counters": ["HealthIssue", "Drug"],
            },
        },
    ]
)

cypher_rows = []
input_path = Path("data").expanduser()

for ip in Document.glob(input_path, "*.txt"):


    # Process the input text using the create pipeline
    doc = pipeline(ip.data)
    cypher_results = doc.results("cypher.app")
    print(cypher_results)
    
    cypher_rows.extend(cypher_results['cypher'])

for line in cypher_rows:
        print(f"{line};")



# these results can be sent to a Neo4j database
#for line in cypher_results["cypher"]:
#    print(f"{line};")
from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

CONNECTION_URI = os.getenv("CONNECTION_URI")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")


driver = GraphDatabase.driver(
    CONNECTION_URI,
    auth=(USERNAME, PASSWORD)
)

with driver.session() as session:
    for line in cypher_rows:
        r = session.run(line)
        print(r.data())


driver.close()