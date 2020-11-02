# DSCM006 Semantic Technologies (NBU 2020) Group Project

Тук се съдържа скрейпър на декларациите по ЗЗДПДПОРДМУ от 2020г. базиран на [Python Scrapy 2.4.0](https://scrapy.org/), както и детиали за транформация на данните в RDF

## Scraper Install & Run

```
cd dscm006-semtech-group-project/scraper
python3 -m venv .venv/
source .venv/bin/activate
pip install -r requirements.txt
scrapy crawl declarations_register 
```

## Data Model

The data model is located in the [model] folder. 

## Public endpoint

<http://edu.ontotext.com/> _repository:media-registry_ contains the endpoint. It is still a work in progress. 


### Workflow data fixes

- Do it on your local GraphDB first, then get someone to check your changes are good (run "control queries")
- If you don't have GrpahDB: create a new test repo on edu.ontotext.com, and first try there
- You can download the data from a zip, or use `Explore> Graphs Overview> Defalt Graph> Export`
- If you are adventurous, use COPY to copy the default graph to some Working grap, make the changes there, then copy (replace) back

