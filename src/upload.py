from qiniu import Auth, put_file, etag, urlsafe_base64_encode
from pync import Notifier
import qiniu.config
import xerox

access_key = '#1'
secret_key = '#2'
q = Auth(access_key, secret_key)
bucket_name = 'autoupload'
filename = xerox.paste();
localfile = '#3' + filename
token = q.upload_token(bucket_name, filename, 36000)
ret, info = put_file(token, filename, localfile)
assert ret['key'] == filename
assert ret['hash'] == etag(localfile)
xerox.copy(u'#4' + filename);
Notifier.notify(u'#5', title='Utils')