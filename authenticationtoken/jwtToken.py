from constants.random import config,jwt
SECRET_KEY = config('JWT_SECRET')

def generateToken(payload):
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def verifyToken(token):
    return jwt.decode(token, "secret", algorithms=["HS256"])    


