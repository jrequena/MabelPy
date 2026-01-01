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

EE...EEEEE...                                                     13 / 13 (100%)

Time: 00:00.028, Memory: 8.00 MB

There were 7 errors:

1) App\Tests\Post\EloquentPostRepositoryTest::test_can_save_and_find_entity
Error: Call to undefined function App\Tests\Post\app()

/home/runner/work/MabelPy/MabelPy/tests/Post/EloquentPostRepositoryTest.php:21

2) App\Tests\Post\EloquentPostRepositoryTest::test_can_delete_entity
Error: Call to undefined function App\Tests\Post\app()

/home/runner/work/MabelPy/MabelPy/tests/Post/EloquentPostRepositoryTest.php:21

3) App\Tests\User\CreateUserUseCaseTest::test_can_be_instantiated
Error: Call to undefined function App\Tests\User\app()

/home/runner/work/MabelPy/MabelPy/tests/User/CreateUserUseCaseTest.php:17

4) App\Tests\User\DeactivateUserUseCaseTest::test_can_be_instantiated
Error: Call to undefined function App\Tests\User\app()

/home/runner/work/MabelPy/MabelPy/tests/User/DeactivateUserUseCaseTest.php:17

5) App\Tests\User\EloquentUserRepositoryTest::test_can_save_and_find_entity
Error: Call to undefined function App\Tests\User\app()

/home/runner/work/MabelPy/MabelPy/tests/User/EloquentUserRepositoryTest.php:22

6) App\Tests\User\EloquentUserRepositoryTest::test_can_delete_entity
Error: Call to undefined function App\Tests\User\app()

/home/runner/work/MabelPy/MabelPy/tests/User/EloquentUserRepositoryTest.php:22

7) App\Tests\User\UpdateUserEmailUseCaseTest::test_can_be_instantiated
Error: Call to undefined function App\Tests\User\app()

/home/runner/work/MabelPy/MabelPy/tests/User/UpdateUserEmailUseCaseTest.php:17

ERRORS!
Tests: 13, Assertions: 14, Errors: 7.
Error: Process completed with exit code 2.