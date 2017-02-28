# Python_AutoUploadImage
using python auto upload local image to cloud, get the url of the image

Only Test on macOS.
##使用方式

>在日常工作的时候，每次截图，都需要手动打开云空间选择文件进行上传,能自动化的，坚决不手动，于是有了下面这个脚本小工具，称之为**图片伴侣**

##环境
1. OS: `macOS`
2. Language: `Python`

## 使用步骤
1. 首先安装[七牛](https://developer.qiniu.com/kodo/sdk/python)的Python SDK
	
	```shell
	pip install qiniu
	
	```
2. 安装[pync](https://pypi.python.org/pypi/pync/1.1) Python Package，以便上传完成后进行通知

	```shell
	pip install pync
	```
3. 将以下代码的变量替换成自己的参数
  * `#1换成七牛云空间的access_key`
  * `#2换成七牛云空间的secret_key`
  *  `#3换成本地图片文件存放的目录的绝对路径`
  * `#4换成云空间中文件的统一前缀，每个云空间不一样`
  * `#5换成自己喜欢的上传成功提示语,like 'upload successfully'`
  
	```
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
```
4. 每次保存完图片到指定的文件夹之后，按`Command+C`，复制完图片后，命令行执行`python upload.py`即可，按`Command+V`即可使用云空间的图片了




##TODO
* 支持又拍云
