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

EE.....EE....                                                     13 / 13 (100%)

Time: 00:00.022, Memory: 10.00 MB

There were 4 errors:

1) App\Tests\Post\EloquentPostRepositoryTest::test_can_save_and_find_entity
RuntimeException: A facade root has not been set.

/home/runner/work/MabelPy/MabelPy/vendor/illuminate/support/Facades/Facade.php:352
/home/runner/work/MabelPy/MabelPy/src/Infrastructure/Persistence/Eloquent/EloquentPostRepository.php:73
/home/runner/work/MabelPy/MabelPy/tests/Post/EloquentPostRepositoryTest.php:35

2) App\Tests\Post\EloquentPostRepositoryTest::test_can_delete_entity
RuntimeException: A facade root has not been set.

/home/runner/work/MabelPy/MabelPy/vendor/illuminate/support/Facades/Facade.php:352
/home/runner/work/MabelPy/MabelPy/src/Infrastructure/Persistence/Eloquent/EloquentPostRepository.php:73
/home/runner/work/MabelPy/MabelPy/tests/Post/EloquentPostRepositoryTest.php:53

3) App\Tests\User\EloquentUserRepositoryTest::test_can_save_and_find_entity
TypeError: App\Domain\User::__construct(): Argument #6 ($posts) must be of type array, null given, called in /home/runner/work/MabelPy/MabelPy/tests/User/EloquentUserRepositoryTest.php on line 28

/home/runner/work/MabelPy/MabelPy/src/Domain/User.php:12
/home/runner/work/MabelPy/MabelPy/tests/User/EloquentUserRepositoryTest.php:28

4) App\Tests\User\EloquentUserRepositoryTest::test_can_delete_entity
TypeError: App\Domain\User::__construct(): Argument #6 ($posts) must be of type array, null given, called in /home/runner/work/MabelPy/MabelPy/tests/User/EloquentUserRepositoryTest.php on line 49

/home/runner/work/MabelPy/MabelPy/src/Domain/User.php:12
/home/runner/work/MabelPy/MabelPy/tests/User/EloquentUserRepositoryTest.php:49

ERRORS!
Tests: 13, Assertions: 17, Errors: 4.
Error: Process completed with exit code 2.