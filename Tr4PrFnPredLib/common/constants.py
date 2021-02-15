from pathlib import Path

# model name constants
MODEL_XBERT = "XBERT"
MODEL_DEEPGO = "deepgoplus"
MODEL_DEEPRED = "deepred"
MODEL_GOLABELER = "golabeler"

# Compute Canada job submission constants
JOB_SUBMIT = "sbatch"
JOB_STATUS = "seff"

# job statuses
STATUS_PENDING = "PENDING"
STATUS_RUNNING = "RUNNING"
STATUS_COMPLETE = "COMPLETED"

# cache constants
CACHE_JOB_ID_KEY = "job_id"
CACHE_JOB_STATUS = "status"
CACHE_JOB_CLUSTER_ID = "cluster_job_id"

# Folder paths
MODEL_CACHE = Path(__file__).parent.parent / "models" / ".cache"
