def test_nginx_package(host):
    p = host.package('nginx')
    assert p.is_installed
    assert p.version.startswith("1.18")

def test_nginx_service(host):
    s = host.service('nginx')
    assert s.is_running
    assert s.is_enabled

def test_nginx_process(host):
    p = host.process.get(user="root", comm="nginx")
    assert 'master process' in p.args

def test_nginx_port(host):
    s = host.socket("tcp://0.0.0.0:80")
    assert s.is_listening

def test_nginx_status(host):
    output = host.check_output('curl -I http://localhost/nginx_status')
    assert '200 OK' in output

def test_nginx_user(host):
    user = host.user("www-data")
    assert user.exists
    assert user.shell == "/usr/sbin/nologin"
    assert user.home == "/var/www"
    assert user.group == "www-data"

def test_nginx_conf_file(host):
    f = host.file("/etc/nginx/nginx.conf")
    assert f.exists
    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o644

def test_nginx_site_file(host):
    f = host.file("/etc/nginx/sites-available/default")
    assert f.exists
    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o644
