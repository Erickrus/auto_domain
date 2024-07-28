import requests

class RedirectPizza:
    # API document: https://redirect.pizza/docs#section/SDKs
    # Get your token: https://redirect.pizza/api-tokens
    def __init__(self, bearerId):
        self.bearerId = bearerId

    # This method only handles the update
    # assume, you have already created a redirect on the website, and you can get its redirectId
    # https://redirect.pizza/docs#tag/Redirects/operation/updateRedirect
    def update(self, redirectId, sourceUrl, destinationUrl):
        url = f"https://redirect.pizza/api/v1/redirects/{redirectId}"
        headers = {
            "Authorization": f"Bearer {self.bearerId}",
            "Content-Type": "application/json"
        }
        data = {
            "sources": [sourceUrl],
            "destination": destinationUrl,
            "redirect_type": "permanent",
            "uri_forwarding": True,
            "keep_query_string": False,
            "tracking": True
        }
        response = requests.put(url, headers=headers, json=data)
        # print(f"status: {response.status_code}")
        return response.status_code
