Run vendor/bin/phpunit
PHPUnit 10.5.60 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.2.29
Configuration: /home/runner/work/MabelPy/MabelPy/phpunit.xml

EE...EEEEE...                                                     13 / 13 (100%)

Time: 00:00.016, Memory: 8.00 MB

There were 7 errors:

1) App\Tests\Post\EloquentPostRepositoryTest::test_can_save_and_find_entity
Error: Class "App\Infrastructure\Repository\EloquentPostRepository" not found

/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:32
/home/runner/work/MabelPy/MabelPy/tests/Post/EloquentPostRepositoryTest.php:21

2) App\Tests\Post\EloquentPostRepositoryTest::test_can_delete_entity
Error: Class "App\Infrastructure\Repository\EloquentPostRepository" not found

/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:32
/home/runner/work/MabelPy/MabelPy/tests/Post/EloquentPostRepositoryTest.php:21

3) App\Tests\User\CreateUserUseCaseTest::test_can_be_instantiated
TypeError: App\Domain\UseCase\User\CreateUser\CreateUserUseCase::__construct(): Argument #1 ($repository) must be of type App\Domain\Repository\UserRepository, class@anonymous given, called in /home/runner/work/MabelPy/MabelPy/tests/TestCase.php on line 32

/home/runner/work/MabelPy/MabelPy/src/Domain/UseCase/User/CreateUser/CreateUserUseCase.php:11
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:32
/home/runner/work/MabelPy/MabelPy/tests/User/CreateUserUseCaseTest.php:17

4) App\Tests\User\DeactivateUserUseCaseTest::test_can_be_instantiated
TypeError: App\Domain\UseCase\User\DeactivateUser\DeactivateUserUseCase::__construct(): Argument #1 ($repository) must be of type App\Domain\Repository\UserRepository, class@anonymous given, called in /home/runner/work/MabelPy/MabelPy/tests/TestCase.php on line 32

/home/runner/work/MabelPy/MabelPy/src/Domain/UseCase/User/DeactivateUser/DeactivateUserUseCase.php:12
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:32
/home/runner/work/MabelPy/MabelPy/tests/User/DeactivateUserUseCaseTest.php:17

5) App\Tests\User\EloquentUserRepositoryTest::test_can_save_and_find_entity
Error: Class "App\Infrastructure\Repository\EloquentUserRepository" not found

/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:32
/home/runner/work/MabelPy/MabelPy/tests/User/EloquentUserRepositoryTest.php:22

6) App\Tests\User\EloquentUserRepositoryTest::test_can_delete_entity
Error: Class "App\Infrastructure\Repository\EloquentUserRepository" not found

/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:32
/home/runner/work/MabelPy/MabelPy/tests/User/EloquentUserRepositoryTest.php:22

7) App\Tests\User\UpdateUserEmailUseCaseTest::test_can_be_instantiated
TypeError: App\Domain\UseCase\User\UpdateUserEmail\UpdateUserEmailUseCase::__construct(): Argument #1 ($repository) must be of type App\Domain\Repository\UserRepository, class@anonymous given, called in /home/runner/work/MabelPy/MabelPy/tests/TestCase.php on line 32

/home/runner/work/MabelPy/MabelPy/src/Domain/UseCase/User/UpdateUserEmail/UpdateUserEmailUseCase.php:11
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:32
/home/runner/work/MabelPy/MabelPy/tests/User/UpdateUserEmailUseCaseTest.php:17

ERRORS!
Tests: 13, Assertions: 14, Errors: 7.
Error: Process completed with exit code 2.