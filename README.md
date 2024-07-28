# auto_domain

AutoDomain is a solution for automatically set up the tunnel and url redirect based on the tunnel endpoint url.

## install cpolar

```
from cpolar import Cpolar
import getpass
import os
CPOLAR_AUTH_TOKEN = getpass.getpass('Enter CPOLAR_AUTH_TOKEN: ')
os.environ["CPOLAR_AUTH_TOKEN"] = CPOLAR_AUTH_TOKEN
Cpolar().install(url...)
```

## start auto_domain
```
import getpass
import os

REDIRECT_PIZZA_TOKEN = getpass.getpass('Enter REDIRECT_PIZZA_TOKEN: ')

os.environ["REDIRECT_PIZZA_REDIRECT_ID"] = '...'
os.environ["REDIRECT_PIZZA_TOKEN"] = REDIRECT_PIZZA_TOKEN

!python3 auto_domain.py url...
```
