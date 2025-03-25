import datetime
import jwt
import time

secret = "242335"

payload = {
    "my_name": "Vasyl",
    "age": 45,
    "iat": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=4),
}
encode_jwt = jwt.encode(payload=payload, key=secret, algorithm="HS256")
print(encode_jwt)
time.sleep(1)

decoded = jwt.decode(encode_jwt, secret, algorithms=["HS256"])
print(decoded)
