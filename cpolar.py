
import json
import os
import requests
import urllib.request
import zipfile

class Cpolar:
    def install(self, url):
        urllib.request.urlretrieve(url, "cpolar-stable-linux-amd64.zip")
        with zipfile.ZipFile("cpolar-stable-linux-amd64.zip", 'r') as zip_ref:
            zip_ref.extractall()        
        os.chmod("cpolar", 0o777)
        os.remove("cpolar-stable-linux-amd64.zip")
        auth_token = os.environ["CPOLAR_AUTH_TOKEN"]
        os.system(f'./cpolar authtoken {auth_token}')

    def get_url(self):
        publicUrl, localAddr = "", ""
        try:
            resp = requests.get("http://127.0.0.1:4040/http/in")
            lines = resp.text.split("\n")
            data = {}
            for line in lines:
                if line.find("window.data = JSON.parse")>0:
                    data = json.loads(line[line.find("window.data = JSON.parse")+25:-2])
                    data = json.loads(data)
                    break
            if len(data.keys()) > 0:
                publicUrl = data["UiState"]["Tunnels"][0]["PublicUrl"]
                localAddr = data["UiState"]["Tunnels"][0]["LocalAddr"]

                publicUrl = publicUrl[publicUrl.rfind('/')+1:]
                localAddr = localAddr[localAddr.rfind('/')+1:]
        except:
            import traceback
            traceback.print_exc()
            pass
        return publicUrl, localAddr

