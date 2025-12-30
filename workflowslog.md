Run vendor/bin/phpunit
PHPUnit 10.5.60 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.2.29
Configuration: /home/runner/work/MabelPy/MabelPy/phpunit.xml

......EEE                                                           9 / 9 (100%)

Time: 00:00.015, Memory: 10.00 MB

There were 3 errors:

1) App\Tests\User\UserMapperTest::test_can_map_from_array
TypeError: App\Domain\Enum\UserStatus::from(): Argument #1 ($value) must be of type string, null given

/home/runner/work/MabelPy/MabelPy/src/Infrastructure/Mapper/UserMapper.php:18
/home/runner/work/MabelPy/MabelPy/tests/User/UserMapperTest.php:24

2) App\Tests\User\UserMapperTest::test_can_map_to_array
TypeError: App\Domain\User::__construct(): Argument #4 ($status) must be of type App\Domain\Enum\UserStatus, null given, called in /home/runner/work/MabelPy/MabelPy/tests/User/UserMapperTest.php on line 31

/home/runner/work/MabelPy/MabelPy/src/Domain/User.php:12
/home/runner/work/MabelPy/MabelPy/tests/User/UserMapperTest.php:31

3) App\Tests\User\UserTest::test_can_be_instantiated
TypeError: App\Domain\User::__construct(): Argument #4 ($status) must be of type App\Domain\Enum\UserStatus, null given, called in /home/runner/work/MabelPy/MabelPy/tests/User/UserTest.php on line 14

/home/runner/work/MabelPy/MabelPy/src/Domain/User.php:12
/home/runner/work/MabelPy/MabelPy/tests/User/UserTest.php:14

ERRORS!
Tests: 9, Assertions: 9, Errors: 3.
Error: Process completed with exit code 2.