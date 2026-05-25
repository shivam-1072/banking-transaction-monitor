from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    data= {
        'txn_id': 'TXN12345678',
        'status': 'SUCCESS',
        'app_status': 'RUNNING',
        'server-health': 'HEALTHY'
    }
    return render_template('index.html',data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug = True)