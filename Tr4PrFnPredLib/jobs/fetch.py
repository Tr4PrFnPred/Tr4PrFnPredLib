import aiofiles
import aiofiles.os
import pickle
import asyncio


async def fetch_results(job_id: str,
                        directory="/scratch/dershao/"):

    """
        Fetch results saved from disk.

        :param job_id: Job id of results we wish to fetch.
        :param directory: Directory containing all the results.
        :return: result entries, sequences, and the predicted GO terms.
    """

    result_file = f'{job_id}-pred.res'

    cmd = f'scp dershao@cedar.computecanada.ca:{directory}{job_id}/preds.res {result_file}'

    await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)

    async with aiofiles.open(result_file, mode='rb') as file:
        results = await pickle.load(file)

    await aiofiles.os.remove(result_file)

    # result is a Python dictionary with the keys:
    # 'entries' | 'sequences' | 'terms'

    return results
