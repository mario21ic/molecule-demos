def test_lacework_package(host):
    p = host.package('lacework')
    assert p.is_installed
    assert p.version.startswith("5.9")

def test_lacework_service(host):
    s = host.service('datacollector')
    assert s.is_running
    assert s.is_enabled

def test_lacework_conf_file(host):
    with host.sudo():
        f = host.file("/var/lib/lacework/config/config.json")
        assert f.exists
        assert f.is_file
        assert f.user == "root"
        assert f.group == "root"
        assert f.mode == 0o640
