
from pyngrok import ngrok, conf
from pathlib import Path
import os,re

# conf.get_default().config_path = ('C:/Users/modes/PycharmProjects/pythondjangotest/ngrok.yml')
# conf.get_default().config_path = ('')
# 2RtLRnwq9Vb1NXFAvGRcifLD3hc_6RBwNa1LsUFJVnSRxxBxn
ngrok.kill()
auth_token= "2RtLRnwq9Vb1NXFAvGRcifLD3hc_6RBwNa1LsUFJVnSRxxBxn"
ngrok.set_auth_token(auth_token)
ngrok.connect(8051)
