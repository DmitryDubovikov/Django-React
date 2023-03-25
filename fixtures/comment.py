import pytest

from fixtures.user import user
from fixtures.post import post

from main.comment.models import Comment


@pytest.fixture
def comment(db, user, post):
    return Comment.objects.create(author=user, post=post, body="Test Comment Body")
