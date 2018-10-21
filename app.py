from imports import app, json, redirect, request, keen, jsonify, db, hashpw, salt, URLSafeTimedSerializer, newpassword, s, url_for, SignatureExpired, system
from functions import doLogin
import smtplib


"""Routed functions"""


@app.route('/login', methods=('GET', 'POST'))
def login():

    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')

        return doLogin(email, password)


@app.route('/resetPassword', methods=('GET', 'POST'))
def resetPassword():

    if request.method == 'POST':

        password = request.form.get('password')

        studentQuery = db.Students.find({'Email': dbEmail})
        ownerQuery = db.Owners.find({'Email': dbEmail})
        authorityQuery = db.Authorities.find({'Email': dbEmail})

        if studentQuery.count() > 0:
            db.Students.update_one({'Email': dbEmail}, {
                                   '$set': {'Password': str(hashpw(password.encode('utf-8'), salt))}})
        elif ownerQuery.count() > 0:
            db.Owners.update_one({'Email': dbEmail}, {
                '$set': {'Password': str(hashpw(password.encode('utf-8'), salt))}})
        elif authorityQuery.count() > 0:
            db.Authorities.update_one({'Email': dbEmail}, {
                '$set': {'Password': str(hashpw(password.encode('utf-8'), salt))}})
        else:
            return jsonify(Error='User does not exist')
        return jsonify(Success='Password changed successfully')


@app.route('/passwordRecovery', methods=['GET', 'POST'])
def passwordRecovery():
    '''verifies the email adress and sent the password '''
    email = ""
    if request.method == 'POST':
        email = request.form['email']
    token = s.dumps(email, salt='emailRecovery')
    return redirect(url_for('sending', token=token, _external=False))


@app.route('/sending/<token>')
def sending(token):
    '''Sends a message to the email receiving the reset password token '''

    global dbEmail
    email = s.loads(token, salt='emailRecovery')
    token = s.dumps(email, salt='emailToLink')
    dbEmail = email
    link = url_for('forgotPassword', token=token, _external=True)

    msg = "User associated with Khaya account has iniated a request to recover user password.\nTo complete password recover process, click the following link to enter new password \n{}".format(
        link)

    # for testing reset password - temporary
    server = smtplib.SMTP('smtp.gmail.com')
    server.connect("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('your.email', "your.password")
    server.sendmail('your.email', email, msg)
    server.quit()
    return "Email has been sent to user emal address {}".format(email)


@app.route('/forgotPassword/<token>')
def forgotPassword(token):
    '''this runs from the link sent to the email address'''
    try:
        email = s.loads(token, salt='emailToLink', max_age=3600)

    except SignatureExpired:
        return "Link Timed Out"
    return redirect(url_for('resetPassword'))


if __name__ == '__main__':
    system(' start cd C:\\mongodb\\bin')
    system('start mongod --directoryperdb --dbpath C:\\mongodb\\data --bind_ip 127.0.0.1')
    app.run(debug=True)
