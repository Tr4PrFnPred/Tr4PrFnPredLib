import redis
from typing import Optional

from ..common.constants import CACHE_JOB_CLUSTER_ID, CACHE_JOB_STATUS


def _cache_job_id_redis(job_id: str, status: str, host: str, port: int, cluster_job_id=-1):

    job_entry = {CACHE_JOB_STATUS: status, CACHE_JOB_CLUSTER_ID: cluster_job_id}

    r = redis.Redis(host=host, port=port)

    r.hmset(job_id, job_entry)


def cache_job_id(job_id: str, status: str, cluster_job_id: Optional[int]):

    _cache_job_id_redis(job_id, status, "localhost", 6379, cluster_job_id)

