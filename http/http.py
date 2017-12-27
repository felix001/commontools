import urllib2
import json
import ssl

def http_get_json(request_url, headers, timeout=20):
    return json.loads(
        urllib2.urlopen(
            urllib2.Request(url=request_url, headers=headers), None, timeout=timeout
        ).read().decode('ascii')
    )

def https_get_json(request_url, headers, timeout=20, ssl_proto=ssl.PROTOCOL_TLSv1):
    return json.loads(
        urllib2.urlopen(
            urllib2.Request(url=request_url, headers=headers), None, timeout=timeout,
            context=ssl.SSLContext(ssl_proto)
        ).read().decode('ascii')
    )

def http_post_json(request_url, data, headers, timeout=20):
    return json.loads(
        urllib2.urlopen(
            urllib2.Request(url=request_url, data=json.dumps(data), headers=headers), None, timeout=timeout
        ).read().decode('ascii')
    )

def https_post_json(request_url, data, headers, timeout=20, ssl_proto=ssl.PROTOCOL_TLSv1):
    return json.loads(
        urllib2.urlopen(
            urllib2.Request(
                url=request_url, data=json.dumps(data), headers=headers), None, timeout=timeout,
            context=ssl.SSLContext(ssl_proto)
        ).read().decode('ascii')
    )
