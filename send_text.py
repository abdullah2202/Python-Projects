from creds import tm
import requests

url_to_fetch = "{url}?username={username}&password={password}&message={message}&orig={orig}&number={number}".format(
    url = tm.tm_url,
    username = tm.tm_u,
    password = tm.tm_p,
    message = "Test Message from PY",
    orig = "PYTest",
    number = tm.tm_n,
)

response = requests.get(url_to_fetch)

print(response.status_code)


