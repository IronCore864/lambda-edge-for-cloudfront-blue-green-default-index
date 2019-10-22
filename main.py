import re


def _get_hostname_by_host(host):
    url_parts = host.split('.')
    hostname = url_parts[0]
    return hostname


def _get_bucket_by_hostname(hostname):
    bucket = "your-blue-bucket" if hostname == "blue" else "your-green-bucket"
    return bucket


def _get_origin_by_host(host):
    hostname = _get_hostname_by_host(host)
    bucket = _get_bucket_by_hostname(hostname)
    return "{}.s3.amazonaws.com".format(bucket)


def _update_request_headers_host(request):
    original_host = request['headers']['host'][0]['value']
    print("Original req header host: {}".format(original_host))
    new_host = _get_origin_by_host(original_host)
    request['origin'] = {
        's3': {
            'domainName': new_host,
            # your region here
            'region': 'eu-central-1',
            # need origin access identity in your cloudfront settings
            'authMethod': 'origin-access-identity',
            'path': '',
            'customHeaders': {}
        }
    }
    request['headers']['host'] = [{'key': 'host', 'value': new_host}]
    print("Accessing origin {}".format(new_host))
    return request


def _is_uri_file(uri):
    return True if "." in uri.split("/")[-1] else False


def _append_index_html(request):
    olduri = request["uri"]
    if not _is_uri_file(olduri) and olduri[-1] != "/":
        olduri += "/"

    newuri = re.sub(r'/$', '/index.html', olduri)
    print("Old URI: {}".format(olduri))
    print("New URI: {}".format(newuri))
    request["uri"] = newuri
    return request


def handler(event, context):
    request = event['Records'][0]['cf']['request']
    request = _update_request_headers_host(request)
    request = _append_index_html(request)
    return request
