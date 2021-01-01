import argparse

from Tr4PrFnPredLib.Pipeline import pipeline

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--model', type=str, required=True,
                    help='Model type')
parser.add_argument('--sequences', type=str, nargs='+', required=True,
                    help='protein sequences to predict')
parser.add_argument('--model_type', type=str,
                    help='type of model e.g., keras, pytorch')

model_type = "keras"

args = parser.parse_args()

model = args.model
sequences = args.sequences

# create the model pipeline
model_pipeline = pipeline(model)
preds = model_pipeline.predict(sequences)
print(preds)

# TODO: write results to disk
