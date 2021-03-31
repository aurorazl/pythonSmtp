import jwt
import time
jwt_token = "eyJhbGciOiJSUzI1NiIsImtpZCI6InYybmNhc3B5Sk9hNGttNGF6LUcwazRFWktYUjlKMFcyOHh1TVR5a3cxOVUifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6ImRlZmF1bHQtdG9rZW4tMmdoOXYiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiZGVmYXVsdCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6IjE1MzlkODNjLTBhM2EtNDE4ZC04OWQ4LTMxYzM0MTRiZGFhNiIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRlZmF1bHQifQ.BOtin9ygvYMSfm89m6LNtJorTkhOFNaNsVT-mFBovmMuWvgsnM0cFKyykNRpC6ObcPwzM5FQMgoaCfsK-YKm5QVlJGwxhLmIgPOZOECVc7oxUt_fWO8l8D5SWJBHEk0PNRPWrkl6cDmgNudu1BZ8U47ovPmaI-3AW7tRcPmg0wzBbegZI1Vn-QDFMg3Ic4-9IaZaZ0WXNeS7nJXTXYVkQ1zCdTltHi5X1ThgpFwdAKyB9Zmu4wDf40tR2ewrRZw5mymHhHLlrle9cmRLmXNptmaxqz42qnM4DSWIs06Z6hZcb0ance895tgfFGmGJAijf_TW9VlTEaZiu-YsUFUZnA"
jwt_token2 = "eyJhbGciOiJSUzI1NiIsImtpZCI6IlJ1Z2NIT1JpX2h5R3pBWkcxLVpJSDEzWnlIQXpfZ1YtYWFacHVTRDE5SHcifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6ImRlZmF1bHQtdG9rZW4tejlrZ2giLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiZGVmYXVsdCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6IjE1MzlkODNjLTBhM2EtNDE4ZC04OWQ4LTMxYzM0MTRiZGFhNiIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRlZmF1bHQifQ.IcM7pbW9OM0gMJy33rR8vDijj1-KQwHyvM3KA3wXJSmN5xLs1kaaijSC18y8fKQ6eaH8UXGBPY5MWqfcbNaF4ANo7iINWF3ZCqrrRbNFNQRGwOBuuYzkosoqDOoYX9eAXvYpnkEODoOM4e0kcv8DZgY3nxnoyK-3Nke3mgCiw8B4rWNz1sXbI3NE30znhkSBK-TFqms4Wzcl2cc-t5ZClzrsBVKo8WRnlu3xCv4gw9iuchCRzjm9aeT57ETE72qFnRHaSRRRLL91xBeD7uVn4_4eyWMpafgwQJkFCXbn74YK1HVUdfUWSJo4U2McseFaBcgXM6gOGN80lQHb7uE5xA"

data = None
try:
    data = jwt.decode(jwt_token, "Sign key for JWT", algorithms=['HS256'],verify=False)
    data2 = jwt.decode(jwt_token2, "Sign key for JWT", algorithms=['HS256'],verify=False)
    print(data)
    print(data2)
except Exception as e:
    print(e)

def create_jwt_token(headers=None):
    jwt_token = jwt.encode({"uid":30001,"exp":int(time.time())+3600*24,"userName":"admin1"},
                           "Sign key for JWT",
                           algorithm="HS256",
                           headers=headers
                           ).decode('utf-8')
    return jwt_token
import base64
print(create_jwt_token())
print(base64.b64decode("MzA5Mzc="))
print(time.strftime("%y%m%d%H%M%S"))
print(["s"]+["b"])
print(sorted([2,1]))
print(float("-inf")+1)

print(__file__)
print(__file__.rfind("test"))