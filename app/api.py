from flask import request, jsonify, Blueprint
import gnupg

api = Blueprint('api', __name__)


@api.route('/decryptMessage', methods=['POST'])
def post():
    if request.headers['Content-Type'] == 'application/json':
        args = request.get_json()
        if len(args) == 0 or ('Passphrase' not in args and 'Message' not in args):
            return jsonify("Please send a 'Passphrase' and a 'Message'")
        elif 'Passphrase' not in args:
            return jsonify("Please send a 'Passphrase'")
        elif 'Message' not in args:
            return jsonify("Please send a 'Message'")
        else:
            return jsonify(decrypt(args['Passphrase'], args['Message']))


def decrypt(passphrase, message):
    gpg_home = "/tmp/.gnupg"
    try:
        gpg = gnupg.GPG(gnupghome=gpg_home)
    except:
        gpg = gnupg.GPG(homedir=gpg_home)

    decrypted_data = gpg.decrypt(message, passphrase=passphrase)
    if not decrypted_data.ok:
        return "Bad Input: Could not decrypt the message"
    else:
        return str(decrypted_data.data)

