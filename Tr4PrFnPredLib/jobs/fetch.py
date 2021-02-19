import aiofiles
import aiofiles.os
import pickle
import asyncio
from pathlib import Path


async def fetch_results(job_id: str,
                        directory="/scratch/dershao/"):

    """
        Fetch results saved from disk.

        :param job_id: Job id of results we wish to fetch.
        :param directory: Directory containing all the results.
        :return: result entries, sequences, and the predicted GO terms.
    """

    result_file_path = Path(__file__).parent / f'{job_id}-pred.res'

    cmd = f'scp dershao@cedar.computecanada.ca:{directory}{job_id}/preds.res {result_file_path}'

    proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)

    await proc.communicate()

    async with aiofiles.open(result_file_path, mode='rb') as file:
        results = await file.read()

    await aiofiles.os.remove(result_file_path)

    # result is a Python dictionary with the keys:
    # 'entries' | 'sequences' | 'terms'

    return pickle.loads(results)
