import redis

from ..common.constants import CACHE_JOB_CLUSTER_ID, CACHE_JOB_STATUS, CACHE_EXPIRY_SECONDS


def _cache_job_id_redis(job_id: str, status: str, host: str, port: int, cluster_job_id: int):

    job_entry = {CACHE_JOB_STATUS: status, CACHE_JOB_CLUSTER_ID: cluster_job_id}

    r = redis.Redis(host=host, port=port)

    r.hmset(job_id, job_entry)
    r.expire(job_id, CACHE_EXPIRY_SECONDS)


def cache_job_id(job_id: str, status: str, cluster_job_id=-1):

    _cache_job_id_redis(job_id, status, "localhost", 6379, cluster_job_id)


def get_cluster_job_id(job_id: str, host="localhost", port=6379) -> int:
    """
    Get the job id identified by the Compute Canada cluster.

    :param job_id: Job id identified by web application.
    :param host: Host of the redis cache
    :param port: Port of redis cache
    :return: The job id identified by cluster
    """

    r = redis.Redis(host=host, port=port)

    # redis returns a list of results encoded in binary
    # therefore, we access the first element and decode the binary as utf-8
    cluster_job_id = r.hmget(job_id, CACHE_JOB_CLUSTER_ID)[0].decode("utf-8")

    return int(cluster_job_id)
