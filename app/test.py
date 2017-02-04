from flask import Flask, json, jsonify
from app import create_app


def test_no_passphrase():
    app = create_app()
    with app.test_request_context('/decryptMessage', method="post",
                                  data=json.dumps({"Message": None}),
                                  content_type='application/json'):
        res = app.full_dispatch_request()
        assert res.status_code == 200
        assert res.data == b'"Please send a \'Passphrase\'"\n'


def test_no_message():
    app = create_app()
    with app.test_request_context('/decryptMessage', method="post",
                                  data=json.dumps({"Passphrase": None}),
                                  content_type='application/json'):
        res = app.full_dispatch_request()
        assert res.status_code == 200
        assert res.data == b'"Please send a \'Message\'"\n'


def test_no_passphrase_no_message():
    app = create_app()
    with app.test_request_context('/decryptMessage', method="post",
                                  data=json.dumps({}),
                                  content_type='application/json'):
        res = app.full_dispatch_request()
        assert res.status_code == 200
        assert res.data == b'"Please send a \'Passphrase\' and a \'Message\'"\n'


def test_decrypt_message():
    app = create_app()
    with app.test_request_context('/decryptMessage', method="post",
                                  data=json.dumps({"Passphrase":"topsecret",
                                                   "Message": "-----BEGIN PGP MESSAGE-----\nVersion: GnuPG v2\n\njA0ECQMCVady3RUyJw3X0kcBF+zdkfZOMhISoYBRwR3uk3vNv+TEg+rJnp4/yYIS\npEoI2S82cDiCNBIVAYWB8WKPtH2R2YSussKhpSJ4mFgqyOA01uwroA==\n=KvJQ\n-----END PGP MESSAGE-----"}),
                                  content_type='application/json'):
        res = app.full_dispatch_request()
        assert res.status_code == 200
        assert res.data == '"Nice work!\\n"\n'
