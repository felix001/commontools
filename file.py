import json

def write_file(data=None, path=False, filename=None, json_dump=False):
    """
    Write data to file. Option to save as json
    """
    if not path:
        path = os.environ['HOME'] + '/'
    filepath = "%s/%s" % (path,filename)
    f = open(filepath,'w')
    os.chmod(filepath, 0600)
    if json_dump:
        import json
        f.write("%s" % json.dumps(data))
    else:
        f.write("%s" % data)
    f.close
    return True
