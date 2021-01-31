###########################################
# TO BE PLACED ON COMPUTE CANADA CLUSTER  #
###########################################
import argparse
import json

from Tr4PrFnPredLib.Pipeline import pipeline
from Tr4PrFnPredLib.jobs.save import save_results

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--model', type=str, required=True,
                    help='Model type')
parser.add_argument('--sequences', type=str, nargs='+', required=True,
                    help='protein sequences to predict')
parser.add_argument('--model_type', type=str,
                    help='type of model e.g., keras, pytorch')
parser.add_argument('--results_file', type=str,
                    help='file containing the results')

model_type = "keras"

args = parser.parse_args()

model = args.model
entry_dict = json.loads(args.sequences)
results_file = args.results_file

entries = list(entry_dict.keys())
sequences = list(entry_dict.values())

# create the model pipeline
model_pipeline = pipeline(model)
preds = model_pipeline.predict(sequences, ids=[i for i in range(len(entries))], prot_ids=entries)
print(preds)

# create dataframe for the results
results = {
    "entries": entries,
    "sequences": sequences,
    "terms": preds.values()
}

# next request when job is complete will fetch those results from disk
save_results(results, results_file)
