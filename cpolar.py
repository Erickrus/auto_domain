import requests
import json

class Cpolar:
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

