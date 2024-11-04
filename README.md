# witamy-server
RESTful API server written using python flask-restx framework.

Swaggar document: [https://witamy.pythonanywhere.com](https://witnamy.pythonanywhere.com)

# Account management
- [x] Login
- [x] Sign up
- [x] Update password
- [x] Delete account


## Initial setup

```
cd /home/download/project/witamy-server
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirement.txt
chmod u+x run.sh
./run.sh
```

### API Testing
The API testing is conducted using FOSS (Free and Open Source Software), specifically [Bruno](https://www.usebruno.com/). All the test files are located in the [`witamy-api-collection`](/witamy-api-collection)
 directory.
