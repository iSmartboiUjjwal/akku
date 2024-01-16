import os

API_ID = API_ID = 21411989

API_HASH = os.environ.get("API_HASH", "ba89c6036c699003a37a5bb0256d6ff6")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6950666016:AAHC_AuTsdLyXfKHlEiLtsKyc0Obdc4kOKU")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 1358747363))

LOG = -1002013062742

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6687634412").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


