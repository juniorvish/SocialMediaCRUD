```python
import unittest
from app import app, db
from app.models import User, Post, Comment

class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = db

    def test_create_user(self):
        response = self.app.post('/api/user', json={'name': 'Test User', 'email': 'test@test.com'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['name'], 'Test User')

    def test_get_user(self):
        response = self.app.get('/api/user/1')
        self.assertEqual(response.status_code, 200)

    def test_update_user(self):
        response = self.app.put('/api/user/1', json={'name': 'Updated User'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['name'], 'Updated User')

    def test_delete_user(self):
        response = self.app.delete('/api/user/1')
        self.assertEqual(response.status_code, 200)

    def test_create_post(self):
        response = self.app.post('/api/post', json={'title': 'Test Post', 'content': 'This is a test post.'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['title'], 'Test Post')

    def test_get_post(self):
        response = self.app.get('/api/post/1')
        self.assertEqual(response.status_code, 200)

    def test_update_post(self):
        response = self.app.put('/api/post/1', json={'title': 'Updated Post'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['title'], 'Updated Post')

    def test_delete_post(self):
        response = self.app.delete('/api/post/1')
        self.assertEqual(response.status_code, 200)

    def test_create_comment(self):
        response = self.app.post('/api/comment', json={'content': 'This is a test comment.'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['content'], 'This is a test comment.')

    def test_get_comment(self):
        response = self.app.get('/api/comment/1')
        self.assertEqual(response.status_code, 200)

    def test_update_comment(self):
        response = self.app.put('/api/comment/1', json={'content': 'This is an updated comment.'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['content'], 'This is an updated comment.')

    def test_delete_comment(self):
        response = self.app.delete('/api/comment/1')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
```