# aileens_musing

## Cambridge, MA

![N|Solid](https://ca.slack-edge.com/T0495HV8H-U01AM69UW3E-ae635702c574-72)

###### 
What is or are knowledge graphs?
Grpah-structured data model / topology to represent and operate on data. Often store interlinked descriptions of entitites (objects, events, concepts) and encoding the free-form sematics or relationships between the entities
> _A knowledge graph formally represents semantics by describing entities and their relationships. Knowledge graphs may make use of ontologies as a schema layer. By doing this, they allow logical inference for retrieving implicit knowledge rather than only allowing queries requesting explicit knowledge._

> a digital map of information where entities (like people, places, or concepts) are nodes, and relationships (like "is the capital of" or "wrote") are edges that link them. This interconnected structure allows computers to understand how data relates to one another, enabling more intelligent search, data integration, and even the inference of new knowledge.
####
ArcadeDB
> multi-model database management system (DBMS)

### example
```sh
docker run --rm -p 2480:2480 -p 2424:2424
           -e JAVA_OPTS="-Darcadedb.server.rootPassword=playwithdata -Darcadedb.server.defaultDatabases=Imported[root]{import:https://github.com/ArcadeData/arcadedb-datasets/raw/main/orientdb/OpenBeer.gz}"
           arcadedata/arcadedb:latest
```

docker run --rm -p 2480:2480 -p 2424:2424 -e JAVA_OPTS="-Darcadedb.server.rootPassword=playwithdata-Darcadedb.server.defaultDatabases=Imported[root]{import:https://github.com/ArcadeData/arcadedb-datasets/raw/main/orientdb/OpenBeer.gz}" arcadedata/arcadedb:latest
        

# questions
- source code and information gathering; point person team
- what is the current workflow 
- what is the current version ? can we upgrade to >  ArcadeDB 21.10.1
>  https://blog.arcadedb.com/released-arcadedb-21101
- shell script / cron job

- can we update further to > 25 helm suport
https://github.com/ArcadeData/arcadedb/blob/main/k8s/helm/README.md