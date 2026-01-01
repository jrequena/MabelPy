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
PHPUnit 10.5.60 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.2.29
Configuration: /home/runner/work/MabelPy/MabelPy/phpunit.xml

EE.......                                                           9 / 9 (100%)

Time: 00:00.015, Memory: 10.00 MB

There were 2 errors:

1) App\Tests\Post\PostMapperTest::test_can_map_from_array
TypeError: App\Infrastructure\Mapper\UserMapper::fromArray(): Argument #1 ($data) must be of type array, null given, called in /home/runner/work/MabelPy/MabelPy/src/Infrastructure/Mapper/PostMapper.php on line 17

/home/runner/work/MabelPy/MabelPy/src/Infrastructure/Mapper/UserMapper.php:13
/home/runner/work/MabelPy/MabelPy/src/Infrastructure/Mapper/PostMapper.php:17
/home/runner/work/MabelPy/MabelPy/tests/Post/PostMapperTest.php:22

2) App\Tests\Post\PostMapperTest::test_can_map_to_array
TypeError: App\Infrastructure\Mapper\UserMapper::toArray(): Argument #1 ($entity) must be of type App\Domain\User, null given, called in /home/runner/work/MabelPy/MabelPy/src/Infrastructure/Mapper/PostMapper.php on line 27

/home/runner/work/MabelPy/MabelPy/src/Infrastructure/Mapper/UserMapper.php:25
/home/runner/work/MabelPy/MabelPy/src/Infrastructure/Mapper/PostMapper.php:27
/home/runner/work/MabelPy/MabelPy/tests/Post/PostMapperTest.php:36

ERRORS!
Tests: 9, Assertions: 12, Errors: 2.
Error: Process completed with exit code 2.