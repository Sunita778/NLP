import base64

def decodeSound(imgstring, fileName):
    try:
        imgdata = base64.b64decode(imgstring)
        with open(fileName, 'wb') as f:
            f.write(imgdata)
    except Exception as e:
        print(f"Error decoding sound: {e}")