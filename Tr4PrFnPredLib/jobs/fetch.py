import aiofiles
import pickle


async def fetch_results(job_id: int,
                        result_directory="/home/dershao/scratch/4thYearProject/"):

    """
        Fetch results saved from disk.

        :param job_id: Job id of results we wish to fetch.
        :param result_directory: Directory containing all the results.
        :return: result entries, sequences, and the predicted GO terms.
    """

    async with aiofiles.open(result_directory + str(job_id), mode='rb') as file:
        results = await pickle.load(file)

    # result file is pandas dataframe with columns
    # | entries | sequences | terms |

    return results.entries, results.sequences, results.terms
