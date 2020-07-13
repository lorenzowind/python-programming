import jwt

def create_token(data, secret):
    return jwt.encode(data, secret, algorithm='HS256')

def verify_signature(token):
    try:
        return jwt.decode(token, 'acelera', algorithms=['HS256'])
    except:
        return {"error": 2}
