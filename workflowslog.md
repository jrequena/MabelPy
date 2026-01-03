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
PHP Fatal error:  Trait "App\Tests\RefreshDatabase" not found in /home/runner/work/MabelPy/MabelPy/tests/Post/EloquentPostRepositoryTest.php on line 12
Error: Process completed with exit code 255.