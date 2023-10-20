import unittest
from app.models import User, Post, Comment

class TestModels(unittest.TestCase):

    def setUp(self):
        self.user = User('testuser', 'testemail@gmail.com', 'testpassword')
        self.post = Post('testpost', 'This is a test post', self.user.id)
        self.comment = Comment('testcomment', 'This is a test comment', self.user.id, self.post.id)

    def test_create_user(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testemail@gmail.com')
        self.assertEqual(self.user.password, 'testpassword')

    def test_create_post(self):
        self.assertEqual(self.post.title, 'testpost')
        self.assertEqual(self.post.content, 'This is a test post')
        self.assertEqual(self.post.user_id, self.user.id)

    def test_create_comment(self):
        self.assertEqual(self.comment.content, 'testcomment')
        self.assertEqual(self.comment.user_id, self.user.id)
        self.assertEqual(self.comment.post_id, self.post.id)

if __name__ == '__main__':
    unittest.main()