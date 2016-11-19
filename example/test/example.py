# -*- coding: utf-8 -*-

def test_login(app):
    app.session.login(app.username, app.password)
