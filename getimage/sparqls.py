sparqlQuery = """PREFIX purl: <http://purl.org/dc/terms/>
PREFIX cidoc: <http://www.cidoc-crm.org/cidoc-crm/>
SELECT COUNT (DISTINCT ?title )
WHERE {
SELECT ?title
FROM <http://stad.gent/ldes/hva> 
FROM <http://stad.gent/ldes/dmg>
FROM <http://stad.gent/ldes/industriemuseum>
FROM <http://stad.gent/ldes/archief>
FROM <http://stad.gent/ldes/stam>

WHERE {
?s cidoc:P102_has_title ?title.
?s cidoc:P129i_is_subject_of ?beeld.
?s purl:isVersionOf ?priref.
}
}
"""

sparql = SPARQL("https://stad.gent/sparql")
qlod = sparql.queryAsListOfDicts(sparqlQuery)
aantal = qlod[0]['callret-0']
offsetrange = aantal / 1000

# determine number of pages to query
pages = math.ceil(offsetrange)

# determine offset range to query
offsetrange = list(range(0, 1000 * pages, 1000))

querylist = []
for offset in offsetrange:
    querylist.append("""PREFIX purl: <http://purl.org/dc/terms/>
    PREFIX cidoc: <http://www.cidoc-crm.org/cidoc-crm/>

    SELECT DISTINCT ?title ?beeld ?priref
    FROM <http://stad.gent/ldes/hva> 
    FROM <http://stad.gent/ldes/dmg>
    FROM <http://stad.gent/ldes/industriemuseum>
    FROM <http://stad.gent/ldes/archief>
    FROM <http://stad.gent/ldes/stam>

    WHERE {
    ?s cidoc:P102_has_title ?title.
    ?s cidoc:P129i_is_subject_of ?beeld.
    ?s purl:isVersionOf ?priref.
    } LIMIT 1000""" + str(offset))

print("offsets geslaagd")
df_sparql = pd.DataFrame()

with alive_bar(60) as bar:
    for query in querylist:
        sparqlQuery = query
        sparql = SPARQL("https://stad.gent/sparql")
        qlod = sparql.queryAsListOfDicts(sparqlQuery)
        csv = CSV.toCSV(qlod)
        df_result = pd.DataFrame([x.split(',') for x in csv.split('\n')])
        df_sparql = df_sparql.append(df_result, ignore_index=True)
        bar()

df_sparql = df_sparql[df_sparql[1].str.contains("api", na=False)]
df_sparql = df_sparql.sample(frac=1)
df_sparql[1] = df_sparql[1].str.replace(r'"', '')
df_sparql[1] = df_sparql[1].str.replace(r'\r', '')
