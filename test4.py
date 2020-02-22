import re
import requests




res = requests.post("https://login.microsoftonline.com/common/oauth2/token",
                  data={"client_id":"6d93837b-d8ce-48b9-868a-39a9d843dc57",
                        "client_secret":"eIHVKiG2TlYa387tssMSj?E?qVGvJi[]",
                        "code":"OAQABAAIAAACQN9QBRU3jT6bcBQLZNUj7CUzQFvQCQ_rjuz-ibC6HCprf11Wfz7URYdJWL-w9qSFNMk44Gj8XtbE-1E_Sdownr5iWuXmwa6ZWCODEt50klUV-8HXtL8SGtzFi-j345nmjpl2PyK4J-yJnAA4_R6ua8kiu4mholxH-6VrNbdd6kUVRIk_inxWtlgDO3oZPcsvqmITM6soiIcmXe8tXG67C1NtmmVNJli9WRvO-OhlTZBq9XDLd2RyAj5yFpwGWRB_gxEr2tK133JvY4cq9EdId__40QY1CLh5WP5_Zu3x8fZ6Hndu_DTNzC711LIQMuqPrS5AVjpHl0OSZb3bKPuG5IUC9PK39MKuy8xyI4Mh75_oCjKQX57Ink13rdO1uSPGqxRAkmZ4MOR_39_Twbc8NrxDwZJIPpN-aWs1UBSIc-lMNy4GLwTpHzoHccttUidj1sHme4Nmr7AvV4khqQemSC-wTdAlR8MAFRDsEkCWhX861wbNRKIZONq99bynXZb9rMEEDEzjZLedRziFZcY6IRDbH9zC2EXhJB9FX_3nPjwwJ3lQR54SAk2z9BB9XarvQBl38ngUV-ImhT5rkhmX8dkD4wxK28fGJddlk13hmdW5KBcLO6szwO0T7I0uysBlxiWs6lqLJFX-QGUR5CF6DIAA",
                        "grant_type":"authorization_code",
                        "redirect_uri":"https://localhost:44326/api/login/microsoft",
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
