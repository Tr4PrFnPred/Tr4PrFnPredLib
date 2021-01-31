#!/bin/bash

###########################################
# TO BE PLACED ON COMPUTE CANADA CLUSTER  #
###########################################

#SBATCH --account=def-jrgreen
#SBATCH --output=/home/dershao/scratch/4thYearProject/output.log
#SBATCH --mem=4g
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --time=1:00:00

function script_help() {
    cat << USAGE
    Usage:
    $(basename $0) -m <model type> -s <sequences> [-script <script name>]

    -m | --model The name of the model to use for this job submission
    -s | --sequences The sequences to predict using model

USAGE
    exit 0
}

script="predict_job.py"

while [[ $# -gt 0 ]]
do

    case "$1" in
        -m | --model)
            model="$2"
            shift
            shift
            ;;
        -s | --sequences)
            sequences="$2"
            shift
            shift
            ;;
        -sc | -script)
            script="$2"
            shift
            shift
            ;;
        -n | -name)
            name="$2"
            shift
            shift
            ;;
        *)
            script_help
            shift
            ;;
esac
done

module load python/3.6
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate
pip install --yes --no-index --upgrade pip

pip install --yes --no-index --upgrade git+git://github.com/Tr4PrFnPred/Tr4PrFnPredLib.git

# get job id
job_id=$(sacct -n -X --format jobid --name $(name))
# use the job id as the unique results file
results_file="~/scratch/"$(job_id)"/preds.res"

python ~/scratch/Tr4PrFnPred/$(script) --model $(model) --sequences $(sequences) --results_file $(results_file)
