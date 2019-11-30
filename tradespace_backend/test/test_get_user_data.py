import pytest
import requests

def login():
  response = requests.post(
    'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyDXj-1A4-KiCMtxbqgkEh6uJnwdN2Bb-40',
    data={
      'email':'test1234@gmail.com',
      'password': 'test1234',
      'returnSecureToken': True
    })
  json_response = response.json()
  assert 'idToken' in json_response
  return json_response['idToken']

def test_success_without_uid(client):
  idToken = login()
  rv = client.get(
    '/users/',
    headers={'Authorization': 'token {}'.format(idToken)})
  json_data = rv.get_json()
  assert json_data['display_name'] == 'test1234'
  assert json_data['email'] == 'test1234@gmail.com'
  assert json_data['phone_number'] == '+11111111111'
  assert json_data['photo_url'] == 'gs://tradespace-22f37.appspot.com/user1/profile.jpg'

def test_success_with_uid(client):
  idToken = login()
  rv = client.get(
    '/users/c1sU9A9OEEfrsxrT6Qp9WnbPm4p2',
    headers={'Authorization': 'token {}'.format(idToken)})
  json_data = rv.get_json()
  assert json_data['display_name'] == 'test12345'
  assert json_data['email'] == 'test12345@gmail.com'
  assert json_data['phone_number'] == '+12222222222'
  assert json_data['photo_url'] == 'gs://tradespace-22f37.appspot.com/user2/profile.jpg'
