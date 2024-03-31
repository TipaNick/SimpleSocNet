import pytest
from SocNet import SocNet

def test_class_socnet_create():
	socnet = SocNet()
	assert socnet is not None

def test_login_trivial():
	# todo: finish method
	socnet = SocNet()
	assert socnet.login("admin", "password") == 1

def test_send_message():
	# todo: finish method
	socnet = SocNet()
	assert socnet.send_message("test", 1) == "success"

def test_add_friend():
	# todo: finish method
	socnet = SocNet()
	assert socnet.add_friend("test") == "success"

def test_delete_friend():
	# todo: finish method
	socnet = SocNet()
	assert socnet.delete_friendd(1) == "success"