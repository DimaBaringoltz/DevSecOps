import socket
from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloworld():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)

    output = "Hello World!\n\n"
    output += f"Host Name: {hostname}\n"
    output += f"Host IP Address: {IPAddr}\n"

    return output

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

