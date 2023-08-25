def test_datadog_package(host):
    p = host.package('datadog-agent')
    assert p.is_installed

def test_datadog_agent_service(host):
    s = host.service('datadog-agent')
    assert s.is_running
    assert s.is_enabled

def test_datadog_agent_sysprobe_service(host):
    s = host.service('datadog-agent-sysprobe')
    assert s.is_running
    assert s.is_enabled

def test_datadog_user(host):
    user = host.user("dd-agent")
    assert user.exists
    assert user.shell == "/usr/sbin/nologin"
    assert user.home == "/opt/datadog-agent"
    assert user.group == "dd-agent"

def test_datadog_conf_file(host):
    with host.sudo():
        f = host.file("/etc/datadog-agent/datadog.yaml")
        assert f.exists
        assert f.is_file
        assert f.user == "dd-agent"
        assert f.group == "dd-agent"
        assert f.mode == 0o640

def test_datadog_modules_conf_files(host):
    files = [
        "/etc/datadog-agent/conf.d/nginx.d/conf.yaml",
        "/etc/datadog-agent/conf.d/http_check.d/conf.yaml",
        "/etc/datadog-agent/system-probe.yaml"
    ]
    for f_conf in files:
        f = host.file(f_conf)
        assert f.exists
        assert f.is_file
        assert f.user == "dd-agent"
        assert f.group == "dd-agent"
        assert f.mode == 0o644
