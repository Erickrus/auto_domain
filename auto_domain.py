import os
import sys
import traceback
import time

from cpolar import Cpolar
from redirect_pizza import RedirectPizza

class AutoDomain:
    def __init__(self, sourceUrl):
        self.publicUrl = "" # set a default value
        self.sourceUrl = sourceUrl

    def start(self):
        self.try_update_redirect()
        # while True:
        #     self.try_update_redirect()
        #     time.sleep(60)

    def try_update_redirect(self):
        try:
            publicUrl, localAddr = Cpolar().get_url()
            if publicUrl != "" and publicUrl != self.publicUrl:
                self.publicUrl = publicUrl
                print(f"update RedirectPizza {self.sourceUrl} => https://{publicUrl}")
                redirectId = os.environ["REDIRECT_PIZZA_REDIRECT_ID"]
                #print(redirectId)
                bearerId = os.environ["REDIRECT_PIZZA_TOKEN"]
                RedirectPizza(bearerId = bearerId).update(
                    redirectId = redirectId,
                    sourceUrl = self.sourceUrl,
                    destinationUrl = f"https://{publicUrl}"
                )
            elif publicUrl == "":
                print("failed to get publicUrl, cpolar is down ? ")
            else:
                print("tick")
        except:
            print(traceback.format_exc())

if __name__ == "__main__":
    AutoDomain(sys.argv[1]).start()
