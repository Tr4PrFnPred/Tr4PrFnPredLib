# import configparser
# TODO: configurations for job submission

from typing import List
import subprocess

from ..common.constants import JOB_SUBMIT, JOB_STATUS


def submit_job(model: str,
               sequences: List,
               script_name="job_submission.sh",
               folder="./") -> int:

    """
        Submit a job to Compute Canada cluster

        :param model: Name of model to use
        :param sequences: Sequences for job to predict
        :param script_name: Name of the script to submit job
        :param folder: Folder containing scripts
        :return: the id of the submitted job
    """

    output = subprocess.run([JOB_SUBMIT, folder + script_name], capture_output=True)

    # output is type <class 'bytes'>
    # convert to string with utf-9 decoding
    script_stdout = output.stdout.decode("utf-8")

    """
        Output of the 'sbatch' command follows the format:
        
        e.g. Submitted batch job <job_id>\n
        
        Therefore, to get the <job_id> the following steps are taken:
        
        1) strip() - to remove the newline
        2) split(" ") - to split the string by whitespace
        3) [-1] to get the last string which is the job id
    """

    job_id = int(script_stdout.strip().split(" ")[-1])
    return job_id


def check_job_status(job_id: int) -> str:
    """
        Check status of submitted Compute Canada job

        :param job_id: id of the job to check status for
        :return: the status of the submitted job
    """

    output = subprocess.run([JOB_STATUS, job_id, "|", "grep", "State"], capture_output=True)

    script_stdout = output.stdout.decode("utf-8")

    """
        Output of the 'seff' command follows the format:
        
        e.g. State: <state> <additional info>
        
        Therefor, to get the <state> the following steps are taken:
        
        1) strip() - remove the newline
        2) split(" ") - split the string by whitespace
        3) [1] - get the middle <state> string
    
    """
    job_status = script_stdout.strip().split(" ")[1]
    return job_status
