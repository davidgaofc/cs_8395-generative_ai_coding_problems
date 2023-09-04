from problems.problem_6 import Blog

def test_create_post():
    blog = Blog()

    post_id1 = blog.create_post("First Post", "This is the content of the first post.")
    post_id2 = blog.create_post("Second Post", "Content of the second post.")

    assert len(blog.list_posts()) == 2
    assert blog.list_posts()[0]['title'] == "First Post"
    assert blog.list_posts()[1]['content'] == "Content of the second post."

def test_add_comment():
    blog = Blog()

    post_id1 = blog.create_post("First Post", "This is the content of the first post.")
    post_id2 = blog.create_post("Second Post", "Content of the second post.")

    blog.add_comment(post_id1, "User1", "Nice post!")
    blog.add_comment(post_id2, "User2", "I enjoyed reading this.")

    assert len(blog.list_posts()[0]['comments']) == 1
    assert len(blog.list_posts()[1]['comments']) == 1
    assert blog.list_posts()[1]['comments'][0]['author'] == "User2"

def test_list_posts():
    blog = Blog()

    post_id1 = blog.create_post("First Post", "This is the content of the first post.")
    post_id2 = blog.create_post("Second Post", "Content of the second post.")

    assert len(blog.list_posts()) == 2
    assert blog.list_posts()[0]['title'] == "First Post"
    assert blog.list_posts()[1]['content'] == "Content of the second post."