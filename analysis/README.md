# Summary Sheet 

This is the sheet with analysis and some post transformation queries

<https://docs.google.com/spreadsheets/d/15XvQzN2P5Bk8l-QJGCnk9W_8zYF_dWYlmpVgUklKUDQ/edit#gid=0>

# Analysis

```sparql
PREFIX : <http://edu.ontotext.com/media-register/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
select ?s ?eik (sample(?name) as ?NAME) (sum(?amount) as ?sum_amount) (count(*) as ?n_contracts) where { 
	?s a :Company ; ^:buyer/:amount ?amount ; 
                        rdfs:label ?name .
    optional{?s :eik ?eik}
} group by ?s ?eik order by desc(?sum_amount)
```

# Postprocessing

Delete empty names
```spaqrl
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX : <http://edu.ontotext.com/media-register/ontology/>
delete where { 
	?s :legalName ""@bg .
} 
```

Create unique rdfs:label using the shortest name (poorman's datatfusion)
```spaqrl
PREFIX : <http://edu.ontotext.com/media-register/ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
construct {
    ?s rdfs:label ?name .
} where
{
    select ?s (sample(?n) as ?name) {
        ?s :legalName ?n .
        filter(strlen(?n) = ?min)
        {
            select ?s (min(strlen(?n)) as ?min) where {
                ?s :legalName ?n .
            } group by ?s
        }
    } group by ?s 
}
```

delete multiple eik for obshtina 
```sparql
PREFIX : <http://edu.ontotext.com/media-register/ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
delete
{
    ?s :eik ?o .
} where { 
	?s :eik ?o ; rdfs:label ?n .
    filter(contains(lcase(?n),"община")) 
} 
```
