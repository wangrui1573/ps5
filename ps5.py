from flask import Flask, request, render_template, make_response
import socket
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')

        data = {
            "url": url
        }

        json_data = json.dumps(data)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(("192.168.31.237", 9090))
            s.sendall(json_data.encode('utf-8'))
            response = s.recv(1024)
            print(f"Received response: {response.decode('utf-8')}")
        
        resp = make_response(render_template('index.html'))
        resp.set_cookie('message', 'succeed', max_age=10)
        
        #return resp
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=9091)
