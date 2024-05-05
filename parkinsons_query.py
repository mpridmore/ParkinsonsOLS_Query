import pandas as pd
from ols_client import EBIClient
pd.set_option('display.max_columns', None)
ebi_client = EBIClient()

results = ebi_client.search('parkinson',query_fields=None, params=None)

results =pd.DataFrame(results)

for x, y in results.iterrows():
  if y['ontology_name'] == 'mondo':
    print ('Name:' + str(y['label'] + '\t' + 'ID:' + y['obo_id']))
