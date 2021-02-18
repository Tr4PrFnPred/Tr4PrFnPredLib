# import configparser
import sys
# TODO: configurations for job submission

import asyncio
import uuid
import json
from typing import Union

from ..common.constants import JOB_SUBMIT, JOB_STATUS, STATUS_PENDING, STATUS_RUNNING
from ..utils.storage import cache_job_id, get_cluster_job_id

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__file__)


if 'win32' in sys.platform:
    asyncio.set_event_loop(asyncio.ProactorEventLoop())


async def _create_submission_folder(job_id: str) -> int:

    create_folder_cmd = f"ssh -t dershao@cedar.computecanada.ca 'mkdir /home/dershao/scratch/{job_id}'"

    proc = await asyncio.create_subprocess_shell(create_folder_cmd,
                                                 stdout=asyncio.subprocess.PIPE,
                                                 stderr=asyncio.subprocess.PIPE)

    await proc.communicate()

    return proc.returncode


async def _create_job_folder(job_id: str):
    """
        Create a job submission folder containing all relevant files for the specified job_id.
        :param job_id:
    """
    cmd = f'ssh -t dershao@cedar.computecanada.ca \'mkdir ~/scratch/{job_id}\''

    proc = await asyncio.create_subprocess_shell(cmd)

    await proc.communicate()

    return proc.returncode


async def _submit_job(job_id: str,
                      model: str,
                      entry_dict: dict,
                      script_name: str,
                      folder: str):

    """
        Submit a job to Compute Canada cluster

        :param job_id: Id of the job generated from application
        :param model: Name of model to use
        :param entry_dict: Entry names and Sequences for job to predict
        :param script_name: Name of the script to submit job
        :param folder: Folder containing scripts
        :return: output of job submission
    """

    # python dictionary has single quotes but json has double quotes
    # json.dumps converts to necessary quotes and replace whitespaces created
    # whitespaces needed to be removed since otherwise it will be considered as separate args in script
    sequences = json.dumps(entry_dict).replace(" ", "").replace(",", "\\,")

    cmd = f'ssh -t dershao@cedar.computecanada.ca \'cd /scratch/dershao && ' \
        f'{JOB_SUBMIT} /scratch/dershao/{script_name} -m {model} -s \'\\\'\'{sequences}\'\\\'\' -i {job_id}\' ' \
        '| grep Submitted'

    logger.info(f'Command: {cmd}')

    proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

    # output is type <class 'bytes'>
    # convert to string with utf-9 decoding
    script_stdout = stdout.decode("utf-8")

    print("SCRIPT STDOUT: ", script_stdout)

    """
        Output of the 'sbatch' command follows the format:

        e.g. Submitted batch job <job_id>\n
             Connection to cedar.computecanada.ca closed.

        Therefore, to get the <job_id> the following steps are taken:

        1) split("\n") - to get first sentence containing the job_id
        2) [0] to select the first sentence
        3) split(" ") - to split the string by whitespace
        4) [-1] to get the last string which is the job id
    """

    cluster_job_id = int(script_stdout.split("\n")[0].split(" ")[-1])

    # cache the compute canada job id and change status to RUNNING
    cache_job_id(job_id, STATUS_RUNNING, cluster_job_id)


async def submit_and_get_job_id(model: str,
                                entry_dict: dict,
                                script_name="prediction_job.sh",
                                folder="") -> str:

    """
        Submit a job to Compute Canada cluster and get the job id of the submitted job

        :param model: Name of model to use
        :param entry_dict: Entries and their sequences for job to predict
        :param script_name: Name of the script to submit job
        :param folder: Folder containing scripts
        :return: the id of the submitted job
    """

    # create unique job id
    job_id = str(uuid.uuid4())

    # cache the job id with status
    # currently cache id as -1 since no cluster job id available yet
    cache_job_id(job_id, STATUS_PENDING, -1)

    # async - run job submission script
    asyncio.create_task(_create_job_folder(job_id))

    # submit the job to the Compute Canada cluster
    asyncio.create_task(_submit_job(job_id, model, entry_dict, script_name, folder))

    return job_id


async def _get_job_info(job_id: Union[str, int]) -> (bytes, bytes):

    """
        Get information on an existing Compute Canada job

        :param job_id: id of the job to check status for
        :return: the status of the submitted job
    """

    cluster_job_id = get_cluster_job_id(job_id)

    cmd = f'ssh -t dershao@cedar.computecanada.ca \'{JOB_STATUS} {cluster_job_id} | grep State\''
    logger.info(f'Getting job info with command: {cmd}')

    proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

    return stdout, stderr


async def check_job_status(job_id: str) -> str:

    """
        Return status of submitted Compute Canada job

        :param job_id: id of the job to check status for
        :return: the status of the submitted job
    """

    stdout, stderr = await _get_job_info(job_id)

    script_stdout = stdout.decode("utf-8")

    """
        Output of the 'seff' command follows the format:
        
        e.g. State: <state> <additional info>\n
             Connection to cedar.computecanada.ca closed.
        
        Therefore, we want to get the <state>.
        However, the output is not always consistent. The only thing that is consistent
        is that the 'State': <state> is not separate lines. To get the <state> we:
        
        1) split("\n") to get each line of the output
        2) Filter out the line with the word "State" in the sentence
        3) split(" ") - split the sentence by whitespace
        4) [1] - get the middle <state> string
    
    """
    lines = script_stdout.split("\n")
    state_line = list(filter(lambda x: "State" in x, lines))

    if len(state_line) == 0:
        # if nothing is present, this means that the job is not running on compute canada
        return STATUS_PENDING
    else:
        logger.info(f'State line: {state_line[0]}')
        return state_line[0].split(" ")[1]
