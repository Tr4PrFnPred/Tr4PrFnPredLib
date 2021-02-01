import aiofiles
import pickle


async def fetch_results(job_id: str,
                        directory="~/scratch/"):

    """
        Fetch results saved from disk.

        :param job_id: Job id of results we wish to fetch.
        :param directory: Directory containing all the results.
        :return: result entries, sequences, and the predicted GO terms.
    """

    result_file = f'ssh -t dershao@cedar.computecanada.ca {directory}{job_id}/preds.res'

    async with aiofiles.open(result_file, mode='rb') as file:
        results = await pickle.load(file)

    # result file is pandas dataframe with columns
    # | entries | sequences | terms |

    return results
