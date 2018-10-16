import paynow
from imports import app, jsonify, url_for
import requests


@app.route('/', methods=['GET', 'POST'])
def initiate():
    pay = paynow.Paynow
    status = paynow.StatusResponse

    pay.integration_id = '6102'
    pay.integration_key = '0da3ebc4-7d51-44c1-b92d-4a938ac4f593'
    status.amount = 25.00
    status.paid = False
    status.paynow_reference = 'btzw333'
    status.reference = 'pay'
    status.status = 'OK'

    return requests.get('https://www.google.com')


if __name__ == '__main__':
    app.run(port=9999, debug=True)
