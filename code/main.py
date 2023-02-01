from flask import Flask, request

app = Flask(__name__)

@app.route('/productionplan', methods=['POST'])
def production_plan():
    # do something with the payload
    return "Production plan received"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8888')