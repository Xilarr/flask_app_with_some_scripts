import pytest

from src import app


@pytest.fixture
def client():
    return app.test_client()


def test_home(mocker, client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert b'Here you can see drivers statistics' in resp.data


def test_common_statistics(client):
    resp = client.get('/report/')
    assert b'1.' in resp.data
    assert b'Sebastian Vettel' in resp.data
    assert b'FERRARI' in resp.data
    assert b'0:01:04.415' in resp.data
    assert resp.status_code == 200


def test_drivers_statistics(client):
    resp = client.get('/report/drivers/?order=desc')
    assert resp.status_code == 200
    assert b'1.' in resp.data
    assert b'Sebastian Vettel' in resp.data
    assert b'FERRARI' in resp.data
    assert b'0:01:04.415' in resp.data


def test_drivers(client):
    resp = client.get('/report/drivers/')
    assert resp.status_code == 200
    assert b'DRR' in resp.data
    assert b'Daniel Ricciardo' in resp.data
    assert b'RED BULL RACING TAG HEUER' in resp.data


def test_driver(client):
    resp = client.get('/report/drivers/?driver_id=svf')
    assert resp.status_code == 200
    assert b'1.' in resp.data
    assert b'Sebastian Vettel' in resp.data
    assert b'FERRARI' in resp.data
    assert b'0:01:04.415' in resp.data
