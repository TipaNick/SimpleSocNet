import pytest
from SocNet import SocNet

def test_class_socnet_create():
	socnet = SocNet()
	assert socnet is not None

def test_login_trivial():
	socnet = SocNet()
	assert socnet.login("admin", "password") == 1

def test_login_invalid_user():
	socnet = SocNet()
	assert socnet.login("wrong_user", "wrong_user") == -1

def test_send_message():
	socnet = SocNet()
	assert socnet.send_message(1, 2, "test") == "success"

def test_add_friend_not_created():
	socnet = SocNet()
	assert socnet.add_friend(2, [3, "friend1"]) == "success"

def test_add_friend_already_created():
	socnet = SocNet()
	assert socnet.add_friend(1, [2, "test"]) == "User already in friend list"

def test_delete_friend():
	socnet = SocNet()
	assert socnet.delete_friend(1, [2, "test"]) == "success"

def test_delete_non_existed_friend():
	socnet = SocNet()
	assert socnet.delete_friend(2, [3, "friend1"]) == "User is not in friend list"

def test_find_user_by_name():
	socnet = SocNet()
	assert socnet.find_user_by_name("admin") == 1

def test_create_user_not_created():
	socnet = SocNet()
	assert socnet.create_user("test1", "test1") == 11

def test_create_user_already_created():
	socnet = SocNet()
	assert socnet.create_user("admin", "password") == -1

def test_get_list_friends():
	socnet = SocNet()
	assert socnet.get_list_friends(1) == [[2, "test"], [3, "friend1"]]

def test_list_messages_1_and_2():
	socnet = SocNet()
	assert socnet.get_list_messages(1, [2, "test"]) == ["Вы: Test text", "test: Test text 2", "Вы: test"]

def test_list_messages_2_and_1():
	socnet = SocNet()
	assert socnet.get_list_messages(2, [1, "admin"]) == ["admin: Test text", "Вы: Test text 2", "admin: test"]