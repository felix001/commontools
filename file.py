import json
import os

def write_file(data=None, path=False, filename=None, json_dump=False):
    """
    Write data to file

    Args:
        data: data to write to file
        path: path to file. if False path=home_dir
        filename: filename
        json_dump: 

    Returns: Bool()
    """
    if not path:
        path = os.environ['HOME'] + '/'
    filepath = "%s/%s" % (path, filename)
    f = open(filepath, 'w')
    os.chmod(filepath, 0600)
    if json_dump:
        f.write("%s" % json.dumps(data))
    else:
        f.write("%s" % data)
    f.close
    return True
