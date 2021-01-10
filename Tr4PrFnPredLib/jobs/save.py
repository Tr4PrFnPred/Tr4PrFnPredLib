import pickle


def save_results(results, results_file: str):
    """
        Save the results to disk

        :param results: Object containing results
        :param results_file: Location of the results
    """
    with open(results_file, "rb") as file:
        pickle.dump(results, file)
