import os
import hmac
import hashlib
import uuid
from urllib.parse import urlencode
from datetime import datetime, timezone


class DLOBuilderUtil:

    def __init__(self):
        self.keys = []
        self.base = "https://ca-walnaof.minddistrict.dev"

    def add_user_id(self, id: str):
        self.userid = id
        self.keys.append("userid")
        return self
    
    def add_user_type(self, type: str):
        self.usertype = type
        self.keys.append("usertype")
        return self
    
    def add_nonce(self):
        self.nonce =str(uuid.uuid4())
        self.keys.append("nonce")
        return self
    
    def add_timestamp(self):
        
        current_time   = datetime.now(timezone.utc)
        z_timestamp    = current_time.isoformat(timespec='seconds').replace('+00:00', 'Z')
        self.timestamp = z_timestamp
        self.keys.append("timestamp")
        return self
    
    def generate_token(self) -> str:
        keys = sorted(self.keys)
        result = ""
        
        for x in keys:
            result = result + x + getattr(self,x)
        secret = os.getenv("secret")
        token = hmac.new(bytes(secret, encoding='utf8'), bytes(result, encoding='utf8'), hashlib.sha512).hexdigest()
        return token

    def generate_dlo(self, user_id: str, user_type: str) -> str :
        self.add_user_id(user_id).add_user_type(user_type).add_nonce().add_timestamp()
        params = {x:getattr(self,x) for x in self.keys}
        params["token"] = self.generate_token() 

        return f"{self.base}?{urlencode(params)}"