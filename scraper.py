import os
import boto
import boto.s3
from boto.s3.key import Key


def upload():
    conn = boto.connect_s3(os.environ.get('MORPH_AWS_ACCESS_KEY_ID'),
                           os.environ.get('MORPH_AWS_SECRET_ACCESS_KEY'),
                           validate_certs=False)
    bucket = conn.get_bucket('morph-upload-test')
    k = Key(bucket)
    k.key = 'popolo-test.txt'
    k.set_contents_from_string("I'm a banana!")
    k.set_metadata('Content-Type', 'text/plain')
    k.make_public()
    print k.generate_url(0, query_auth=False, force_http=True)

if __name__ == '__main__':
    upload()
