from flask import request, session


def test_app(app):
    # We can test app-level stuff, such as the setting of the secret key.
    assert app.secret_key == "dskfjdfdg igvk gereregopritr re"


def test_session(client):
    # This code pre-loads some session keys and their starter values for this test.
    with client.session_transaction() as sess:
        sess["count"] = 0
        sess["previous"] = "some pattern"

    # This URL adds 1 to the count session value.
    response = client.get("/session")

    # Let's assert that we get what we expect... did the count increment?
    assert response.status_code == 200
    assert "count" in session
    assert session["count"] == 1
    assert b"The previous pattern is: " in response.data

    # Let's access the URL once more... note: we expect count to increment again.
    response = client.get("/session")

    # Let's assert that we get what we expect... did the count increment (it should be 2)?
    assert session["count"] == 2


def test_up(client):
    assert client.get("/").status_code == 200


def test_form(client):
    response = client.get("/cheat")
    assert response.status_code == 200
    assert response.data.startswith(b"<!DOCTYPE html>") == True
    assert b'<form method="POST" action="/displaycheats">' in response.data


def test_api(client):
    response = client.get("/api/cheat/_y__o_")
    assert response.status_code == 200
    assert isinstance(response.data, bytes) == True


def test_results(client):
    response = client.post("/displaycheats", data={"pattern": "_y__o_"})
    assert request.method == "POST"
    assert request.form["pattern"] == "_y__o_"
    assert response.status_code == 200
    resp = response.data
    assert resp.startswith(b"<!DOCTYPE html>") == True
    assert b"<h2>Possible Pattern Matches</h2>" in resp
    assert b"<li>" in resp


# Does it even make sense to test for empty results (i.e., no <li> tags)?
def test_empty(client):
    response = client.post("/displaycheats", data={"pattern": ""})
    assert request.method == "POST"
    assert request.form["pattern"] == ""
    assert response.status_code == 200
    resp = response.data
    assert resp.startswith(b"<!DOCTYPE html>") == True
    assert b"<h2>Possible Pattern Matches</h2>" in resp
    assert b"<li>" not in resp
