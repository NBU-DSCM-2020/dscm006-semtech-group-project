# Making a Semantic Model

Any semantic model should start from the  data (and Competency Questions).
Ontologies come into the picture later

## Data Sample

Consider this data under ZZDPDPORDMU (Закона на Пеевски):

<https://github.com/NBU-DSCM-2020/dscm006-semtech-group-project/blob/master/scraper/ZZDPDPORDMU/scraped_data/168%20ЧАСА%20ЕООД%20(ЕИК%20831400025).json>

```json
    "object_id": "173",
    "legal_entity_name": "168 ЧАСА ЕООД",
    "legal_entity_id": "831400025",
    "public_company": "неприложимо",
    "media_service_type": "Печатна медия; Печатна медия; Печатна медия; Печатна медия; Печатна медия; Печатна медия; Печатна медия; Печатна медия; Печатна медия; Печатна медия; Онлайн новинарско издание; Онлайн новинарско издание; Онлайн новинарско издание; Онлайн новинарско издание; Онлайн новинарско издание; Онлайн новинарско издание; Онлайн новинарско издание; Онлайн новинарско издание; Онлайн новинарско издание; Онлайн новинарско издание; Онлайн новинарско издание; Печатна медия",
    "media_service_name": "24 часа; 168 часа; ВСИЧКО ЗА СЕМЕЙСТВОТО; КЛУБ 100; БЪЛГАРИЯ ДНЕС; ИДЕАЛЕН ДОМ; TREND; TREND AUTO; КОСМОС; РЕЦЕПТИ ЗА ЗДРАВЕ; 24chasa.bg; 168chasa.bg; bgdnes.bg; mila.bg; mama24.bg; 24zdrave.bg; hiclub.bg; dotbg.bg; 24plovdiv.bg; spomen.bg; mentrend.bg; Идеален дом Decor",
    "real_owner": "ВЕНЕЛИНА АТАНАСОВА ГОЧЕВА",
    "executive_individual": "неприложимо",
    "contracts": [
        {
            "contract_amount_raw": "6180",
            "contract_amount": 6180,
            "contract_basis_raw": "10.04.2019 Публикуване на инф. материали",
            "contract_sponsor_raw": "Фонд мениджър на финансови инструменти в България, ЕИК 203740812"
        },
```

We want the sample to be complete, i.e. contain all possible fields, i.e. be representative of the data.

- A good rule of thumb is "pick the largest data file".
- 168 ЧАСА ЕООД is an important media, so it has nearly complete data.
- I looked in other files to find an instance of this field, but didn't find any:

```
"executive_individual": "неприложимо",
```

## Sample RDF

Use the actual data to make a model.

- Pick some URL base for resources, and prefix for the ontology.
- For now let's make a custom ontology (our own classes and props), we'll pick existing ontologies later
- Make only 1 copy of each array, in order to keep it simpler.

```ttl

```

## Identification 

*Companies* are identified using three diffrent modes. Thes are in order of preference:
* EIK number
* Wikidata Q-d for Bulgarian municipalities
* MD5 hash of the company name

*Media* are identified by a md5 hash of a combination of the media name, the media type and the parent company id

*Contracts* are identified by the row number in the source data sheet. This is temporary until a bug in the transformation tool is fixed, after which we will use blank nodes. 




## Sample Diagram

Use rdfpuml to make a diagram

## Generalized Model

Rather than real values, use field names to generalize the model
