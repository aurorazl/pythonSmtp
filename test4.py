import re
import requests


res = requests.post("https://login.microsoftonline.com/common/oauth2/v2.0/token",
                  data={"client_id":"6d93837b-d8ce-48b9-868a-39a9d843dc57",
                        "client_secret":"eIHVKiG2TlYa387tssMSj?E?qVGvJi[]",
                        "code":"OAQABAAIAAAAm-06blBE1TpVMil8KPQ41T9KaPgikd7qk32b1f0yDxI4LCnL88Aq74Am5b-cmgSG0ZYrYSokkFq02PoJ_WWDXdi5SeK0awgq9stgykrFFz2xwPa-ri7UO8IKg1gxCq_5YB6-EWmE1HLEXv1199pS_Y1fRYm4H47w4-mdEMYW7tlmssQNurgPD4R-cPU5HkdK7T6ZPLh-QXtx4HSmQScvWdwD25rcXpmKlKv8taRbRGcby9tW-rh4nb1pRWEU_aYufhfOWOBMGw6kUXxfx3lz5odgme44X-9BZQSJ68SBxnQy8C6uZJNbT-Q7RHGR1l2pjNENyjyPJi7yWz2eY9ldoARz9CTDu0kmtAjaldSe8C1aFgSPorugY3Win9A_aYKooIaaaoz0mElgt--Jm5OmTXUyoqxcPibbZZrQaC_Q7aXVIZwQ1nG_KqQFItvJFq1CX2SXt6G-ko_wn7o5n-ffpt2arwz7l1_OP0trp10AEi9p19YpO84Qx0L8D4ySRAzKoUNBJ5zzfSnU-Zfcz6cDZZSokq0byfopTdBzegtIYy6ha8E_40MKZZAdn9ihnFz05ytAerQ2i4lxPGGLQmnli8w2qTDoYAyV4yIvWLFNPutwBXf9jatLgnkwvo7rMkNRmSPAPdkl0ALXqZhf4cCcr7uID8SjTiPah3bpQkN0BgSAA",
                        "grant_type":"authorization_code",
                        "redirect_uri":"https://apulis-sz-dev-worker01.sigsus.cn/api/login/microsoft",
                        },
                    headers={"Content-Typ":"application/x-www-form-urlencoded"})
# res = requests.get(
#     url="https://graph.microsoft.com/v1.0/me",
#     headers = {"Authorization":"Bearer "+"eyJ0eXAiOiJKV1QiLCJub25jZSI6ImpmcWVWUWYtSXZ2TDJSaWdUakQwVWJVOXFacERydEZQUC1QRW9oVE5aYVEiLCJhbGciOiJSUzI1NiIsIng1dCI6InBpVmxsb1FEU01LeGgxbTJ5Z3FHU1ZkZ0ZwQSIsImtpZCI6InBpVmxsb1FEU01LeGgxbTJ5Z3FHU1ZkZ0ZwQSJ9.eyJhdWQiOiJodHRwczovL2dyYXBoLm1pY3Jvc29mdC5jb20iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8xOTQ0MWM2YS1mMjI0LTQxYzgtYWMzNi04MjQ2NGMyZDliMTMvIiwiaWF0IjoxNTc2NjcxMTQxLCJuYmYiOjE1NzY2NzExNDEsImV4cCI6MTU3NjY3NTA0MSwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFTUUEyLzhOQUFBQWUwVEFrQVROMlg4cVMzc3V2bWlxemx1bzN0Tnh2S3E0cWphdk84RU45UmM9IiwiYW1yIjpbInB3ZCJdLCJhcHBfZGlzcGxheW5hbWUiOiJ0ZXN0MSIsImFwcGlkIjoiNmQ5MzgzN2ItZDhjZS00OGI5LTg2OGEtMzlhOWQ4NDNkYzU3IiwiYXBwaWRhY3IiOiIxIiwiZmFtaWx5X25hbWUiOiJDaGVuIiwiZ2l2ZW5fbmFtZSI6Ilplbmdsb25nIiwiaXBhZGRyIjoiNjAuMjQ5LjExNy41MiIsIm5hbWUiOiJaZW5nbG9uZyBDaGVuICjpmYjlop7pvpkpIiwib2lkIjoiNjY4YWYzNTctODYwMS00MzRiLWEzNmEtNDcyODc4ZDBiM2I0IiwicGxhdGYiOiIzIiwicHVpZCI6IjEwMDMyMDAwODMxNjQ3MzQiLCJzY3AiOiJvZmZsaW5lX2FjY2VzcyBvcGVuaWQgcHJvZmlsZSBVc2VyLlJlYWQgVXNlci5SZWFkQmFzaWMuQWxsIiwic2lnbmluX3N0YXRlIjpbImttc2kiXSwic3ViIjoiNW5WVmhyQkFOMDA4SFFJVm84OXdudnI3aUxFTXl4dndRQkRaVUFJT09xSSIsInRpZCI6IjE5NDQxYzZhLWYyMjQtNDFjOC1hYzM2LTgyNDY0YzJkOWIxMyIsInVuaXF1ZV9uYW1lIjoiemVuZ2xvbmcuY2hlbkBhcHVsaXMuY29tIiwidXBuIjoiemVuZ2xvbmcuY2hlbkBhcHVsaXMuY29tIiwidXRpIjoiUzRMNXhEN1g0RXE5ZHVLTUlKNS1BQSIsInZlciI6IjEuMCIsInhtc190Y2R0IjoxNTUxMTIwODA5fQ.l0pklPbdOE79ZRnG3h463mXmvIlX6OPh3Xtnk0JNaTipKiNW4wbdcoF5v_Yt4JiiDDCzw8r_5Oy_jVTFcWM4CBPmxrJxPOQRp4Bclg0azL9DwhUo0K1JVRrUSkxSGIGC0S8v3rpm8bn2AQN92sO6OsS-R9ee9vNvxXPmPXN53lTJkYzrEuh8DQuv4bBgQtqCR4tqq69hrJS9PiYL9wfD5KXsr4Y1KAve6HhdPPj2TE8_M9CGdGuVZeQ5a-t36tD74W13eUjZfiuFFsFOWEuLhwI3fryIZ6SWlTTv6ZErSauFG9RO0afy0MqhGo6W16j6QIwtWttXcvofDTAlUGECLg"}
# )
print(res.status_code)
print(res.text)
import json
print(json.loads(res.text))
print("sigsus.cn".split(":")[0] if ":" in "sigsus.cn" else "sigsus.cn")
print("." +   "23 "+        "sigsus.cn".split(":")[0] if ":" in "sigsus.cn" else "sigsus.cn")
print("atlas02.sigsus.cn".split("."+"sigsus.cn".split(":")[0] if ":" in "sigsus.cn" else "sigsus.cn")[0])
print(all((x==0 for x in [0,1])))