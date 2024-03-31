import pytest
from SocNet import SocNet

def test_class_socnet_create():
	socnet = SocNet()
	assert socnet is not None

def test_login_trivial():
	socnet = SocNet()
	assert socnet.login("admin", "password") == 1

def test_send_message_1():
	socnet = SocNet()
	assert socnet.send_message("test", 1) == "success"

def test_add_friend_1():
	socnet = SocNet()
	assert socnet.add_friend("test") == "success"

def test_delete_friend_1():
	socnet = SocNet()
	assert socnet.delete_friend(1) == "success"

def test_find_user_1():
	socnet = SocNet()
	assert socnet.find_user("admin") == 1

def test_create_user_1():
	socnet = SocNet()
	assert socnet.create_user("test1", "test1") == "success"

