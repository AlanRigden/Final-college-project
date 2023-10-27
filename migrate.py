with app.app_context():
    db.drop_all()
    db.create_all()

    test_user = User(id=1, email='alankick38@gmail.com', username='username')
    test_user.set_password('password')
    test_user2 = User(id=2, email='test@gmail.com', username='username1')
    test_user2.set_password('password')

    test_entry = Diary(entryID=1, title='test title', description='test description', step_count=66, user_id=1)
    test_entry2 = Diary(entryID=2, title='test title 2', description='test description 2', step_count=662, user_id=1)
    test_entry3 = Diary(entryID=3, title='test title 3', description='test description 3', step_count=663, user_id=2)

    db.session.add(test_user)
    db.session.add(test_user2)
    db.session.add(test_entry)
    db.session.add(test_entry2)
    db.session.add(test_entry3)

    db.session.commit()