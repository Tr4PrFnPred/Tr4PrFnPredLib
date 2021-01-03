# import configparser
# TODO: configurations for job submission

from typing import List
import asyncio

from ..common.constants import JOB_SUBMIT, JOB_STATUS


async def _submit_job(model: str,
                      sequences: List,
                      script_name: str,
                      folder: str) -> (bytes, bytes):

    """
        Submit a job to Compute Canada cluster

        :param model: Name of model to use
        :param sequences: Sequences for job to predict
        :param script_name: Name of the script to submit job
        :param folder: Folder containing scripts
        :return: output of job submission
    """

    cmd = f'{JOB_SUBMIT} {folder}{script_name} -m {model} -s {sequences}'

    proc = await asyncio.create_subprocess_exec(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

    return stdout, stderr


def submit_and_get_job_id(model: str,
                                sequences: List,
                                script_name="job_submission.sh",
                                folder="./") -> int:

    """
        Submit a job to Compute Canada cluster and get the job id of the submitted job

        :param model: Name of model to use
        :param sequences: Sequences for job to predict
        :param script_name: Name of the script to submit job
        :param folder: Folder containing scripts
        :return: the id of the submitted job
    """

    stdout, stderr = asyncio.run(_submit_job(model, sequences, script_name, folder))

    # output is type <class 'bytes'>
    # convert to string with utf-9 decoding
    script_stdout = stdout.decode("utf-8")

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


async def _get_job_info(job_id: int) -> (bytes, bytes):

    """
        Get information on an existing Compute Canada job

        :param job_id: id of the job to check status for
        :return: the status of the submitted job
    """

    cmd = f'{JOB_STATUS} {job_id} | grep State'

    proc = await asyncio.create_subprocess_exec(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

    return stdout, stderr


def check_job_status(job_id: int) -> str:

    """
        Return status of submitted Compute Canada job

        :param job_id: id of the job to check status for
        :return: the status of the submitted job
    """

    stdout, stderr = asyncio.run(_get_job_info(job_id))

    script_stdout = stdout.decode("utf-8")

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
