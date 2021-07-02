import hashlib
import os

from dmoj.judgeenv import get_problem_root


# Read at most 10MB at a time
BLOCKSIZE = 1024 * 1024 * 10


def get_file_sha(file):
    sha1 = hashlib.sha1()
    file_buffer = file.read(BLOCKSIZE)
    while len(file_buffer) > 0:
        sha1.update(file_buffer)
        file_buffer = file.read(BLOCKSIZE)
    return sha1.hexdigest()


def check_sync(problem_id):
    folder = get_problem_root(problem_id)
    files = os.listdir(folder)
    result = {}
    for file_name in files:
        result[file_name] = get_file_sha(open(os.path.join(folder, file_name), "rb"))
    return result
