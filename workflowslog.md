Run vendor/bin/phpunit
  vendor/bin/phpunit
  shell: /usr/bin/bash -e {0}
  env:
    pythonLocation: /opt/hostedtoolcache/Python/3.12.12/x64
    PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.12.12/x64/lib/pkgconfig
    Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.12/x64
    Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.12/x64
    Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.12/x64
    LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.12.12/x64/lib
    COMPOSER_PROCESS_TIMEOUT: 0
    COMPOSER_NO_INTERACTION: 1
    COMPOSER_NO_AUDIT: 1
PHP Fatal error:  Could not check compatibility between App\Tests\DummyConnection::transaction(App\Tests\Closure $callback, $attempts = 1) and Illuminate\Database\ConnectionInterface::transaction(Closure $callback, $attempts = 1), because class App\Tests\Closure is not available in /home/runner/work/MabelPy/MabelPy/tests/TestCase.php(132) : eval()'d code on line 21
Error: Process completed with exit code 255.