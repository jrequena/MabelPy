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

EEEEEEEEEEEEE                                                     13 / 13 (100%)

Time: 00:00.018, Memory: 10.00 MB

There were 13 errors:

1) App\Tests\Post\EloquentPostRepositoryTest::test_can_save_and_find_entity
Error: Class "Illuminate\Events\Dispatcher" not found

/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:57
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:33
/home/runner/work/MabelPy/MabelPy/tests/Post/EloquentPostRepositoryTest.php:20

2) App\Tests\Post\EloquentPostRepositoryTest::test_can_delete_entity
Error: Class "Illuminate\Events\Dispatcher" not found

/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:57
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:33
/home/runner/work/MabelPy/MabelPy/tests/Post/EloquentPostRepositoryTest.php:20

3) App\Tests\Post\PostMapperTest::test_can_map_from_array
Error: Class "Illuminate\Events\Dispatcher" not found

/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:57
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:33

4) App\Tests\Post\PostMapperTest::test_can_map_to_array
Error: Class "Illuminate\Events\Dispatcher" not found

/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:57
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:33

5) App\Tests\Post\PostTest::test_can_be_instantiated
Error: Class "Illuminate\Events\Dispatcher" not found

/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:57
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:33

6) App\Tests\User\CreateUserUseCaseTest::test_can_be_instantiated
Error: Class "Illuminate\Events\Dispatcher" not found

/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:57
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:33

7) App\Tests\User\DeactivateUserUseCaseTest::test_can_be_instantiated
Error: Class "Illuminate\Events\Dispatcher" not found

/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:57
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:33

8) App\Tests\User\EloquentUserRepositoryTest::test_can_save_and_find_entity
Error: Class "Illuminate\Events\Dispatcher" not found

/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:57
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:33
/home/runner/work/MabelPy/MabelPy/tests/User/EloquentUserRepositoryTest.php:21

9) App\Tests\User\EloquentUserRepositoryTest::test_can_delete_entity
Error: Class "Illuminate\Events\Dispatcher" not found

/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:57
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:33
/home/runner/work/MabelPy/MabelPy/tests/User/EloquentUserRepositoryTest.php:21

10) App\Tests\User\UpdateUserEmailUseCaseTest::test_can_be_instantiated
Error: Class "Illuminate\Events\Dispatcher" not found

/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:57
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:33

11) App\Tests\User\UserMapperTest::test_can_map_from_array
Error: Class "Illuminate\Events\Dispatcher" not found

/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:57
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:33

12) App\Tests\User\UserMapperTest::test_can_map_to_array
Error: Class "Illuminate\Events\Dispatcher" not found

/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:57
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:33

13) App\Tests\User\UserTest::test_can_be_instantiated
Error: Class "Illuminate\Events\Dispatcher" not found

/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:57
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:33

ERRORS!
Tests: 13, Assertions: 0, Errors: 13.
Error: Process completed with exit code 2.