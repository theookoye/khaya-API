from imports import jsonify, db, hashpw, salt


def doLogin(email, password):
    dbPassword, error = (None, '')

    if db.Students.find({'Email': email}).count() > 0:
        query = db.Students.find(
            {'Email': email}, {'_id': '0', 'Password': '1'})

        for i in query:
            dbPassword = i['Password']

        if str(hashpw(password.encode('utf-8'), salt)) == dbPassword:
            return jsonify(Message='Logged In', error=error)
        else:
            return jsonify(error='Invalid credentials')

    elif db.Owners.find({'Email': email}).count() > 0:
        query = db.Owners.find(
            {'Email': email}, {'_id': '0', 'Password': '1'})

        for i in query:
            dbPassword = i['Password']

        if str(hashpw(password.encode('utf-8'), salt)) == dbPassword:
            return jsonify(Message='Logged In', error=error)
        else:
            return jsonify(error='Invalid credentials')

    elif db.Authorities.find({'Email': email}).count() > 0:
        query = db.Authorities.find(
            {'Email': email}, {'_id': '0', 'Password': '1'})

        for i in query:
            dbPassword = i['Password']

        if str(hashpw(password.encode('utf-8'), salt)) == dbPassword:
            return jsonify(Message='Logged In', error=error)
        else:
            return jsonify(error='Invalid credentials')

    else:
        return jsonify(Message='Not Found')
