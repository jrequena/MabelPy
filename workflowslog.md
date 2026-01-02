Run vendor/bin/phpunit
PHPUnit 10.5.60 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.2.29
Configuration: /home/runner/work/MabelPy/MabelPy/phpunit.xml

EEEEEEEEEEEEE                                                     13 / 13 (100%)

Time: 00:00.017, Memory: 10.00 MB

There were 13 errors:

1) App\Tests\Post\EloquentPostRepositoryTest::test_can_save_and_find_entity
TypeError: Illuminate\Database\Eloquent\Model::setConnectionResolver(): Argument #1 ($resolver) must be of type Illuminate\Database\ConnectionResolverInterface, class@anonymous given, called in /home/runner/work/MabelPy/MabelPy/tests/TestCase.php on line 101

/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1839
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:101
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:55
/home/runner/work/MabelPy/MabelPy/tests/Post/EloquentPostRepositoryTest.php:20

2) App\Tests\Post\EloquentPostRepositoryTest::test_can_delete_entity
TypeError: Illuminate\Database\Eloquent\Model::setConnectionResolver(): Argument #1 ($resolver) must be of type Illuminate\Database\ConnectionResolverInterface, class@anonymous given, called in /home/runner/work/MabelPy/MabelPy/tests/TestCase.php on line 101

/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1839
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:101
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:55
/home/runner/work/MabelPy/MabelPy/tests/Post/EloquentPostRepositoryTest.php:20

3) App\Tests\Post\PostMapperTest::test_can_map_from_array
TypeError: Illuminate\Database\Eloquent\Model::setConnectionResolver(): Argument #1 ($resolver) must be of type Illuminate\Database\ConnectionResolverInterface, class@anonymous given, called in /home/runner/work/MabelPy/MabelPy/tests/TestCase.php on line 101

/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1839
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:101
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:55

4) App\Tests\Post\PostMapperTest::test_can_map_to_array
TypeError: Illuminate\Database\Eloquent\Model::setConnectionResolver(): Argument #1 ($resolver) must be of type Illuminate\Database\ConnectionResolverInterface, class@anonymous given, called in /home/runner/work/MabelPy/MabelPy/tests/TestCase.php on line 101

/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1839
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:101
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:55

5) App\Tests\Post\PostTest::test_can_be_instantiated
TypeError: Illuminate\Database\Eloquent\Model::setConnectionResolver(): Argument #1 ($resolver) must be of type Illuminate\Database\ConnectionResolverInterface, class@anonymous given, called in /home/runner/work/MabelPy/MabelPy/tests/TestCase.php on line 101

/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1839
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:101
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:55

6) App\Tests\User\CreateUserUseCaseTest::test_can_be_instantiated
TypeError: Illuminate\Database\Eloquent\Model::setConnectionResolver(): Argument #1 ($resolver) must be of type Illuminate\Database\ConnectionResolverInterface, class@anonymous given, called in /home/runner/work/MabelPy/MabelPy/tests/TestCase.php on line 101

/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1839
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:101
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:55

7) App\Tests\User\DeactivateUserUseCaseTest::test_can_be_instantiated
TypeError: Illuminate\Database\Eloquent\Model::setConnectionResolver(): Argument #1 ($resolver) must be of type Illuminate\Database\ConnectionResolverInterface, class@anonymous given, called in /home/runner/work/MabelPy/MabelPy/tests/TestCase.php on line 101

/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1839
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:101
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:55

8) App\Tests\User\EloquentUserRepositoryTest::test_can_save_and_find_entity
TypeError: Illuminate\Database\Eloquent\Model::setConnectionResolver(): Argument #1 ($resolver) must be of type Illuminate\Database\ConnectionResolverInterface, class@anonymous given, called in /home/runner/work/MabelPy/MabelPy/tests/TestCase.php on line 101

/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1839
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:101
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:55
/home/runner/work/MabelPy/MabelPy/tests/User/EloquentUserRepositoryTest.php:21

9) App\Tests\User\EloquentUserRepositoryTest::test_can_delete_entity
TypeError: Illuminate\Database\Eloquent\Model::setConnectionResolver(): Argument #1 ($resolver) must be of type Illuminate\Database\ConnectionResolverInterface, class@anonymous given, called in /home/runner/work/MabelPy/MabelPy/tests/TestCase.php on line 101

/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1839
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:101
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:55
/home/runner/work/MabelPy/MabelPy/tests/User/EloquentUserRepositoryTest.php:21

10) App\Tests\User\UpdateUserEmailUseCaseTest::test_can_be_instantiated
TypeError: Illuminate\Database\Eloquent\Model::setConnectionResolver(): Argument #1 ($resolver) must be of type Illuminate\Database\ConnectionResolverInterface, class@anonymous given, called in /home/runner/work/MabelPy/MabelPy/tests/TestCase.php on line 101

/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1839
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:101
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:55

11) App\Tests\User\UserMapperTest::test_can_map_from_array
TypeError: Illuminate\Database\Eloquent\Model::setConnectionResolver(): Argument #1 ($resolver) must be of type Illuminate\Database\ConnectionResolverInterface, class@anonymous given, called in /home/runner/work/MabelPy/MabelPy/tests/TestCase.php on line 101

/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1839
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:101
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:55

12) App\Tests\User\UserMapperTest::test_can_map_to_array
TypeError: Illuminate\Database\Eloquent\Model::setConnectionResolver(): Argument #1 ($resolver) must be of type Illuminate\Database\ConnectionResolverInterface, class@anonymous given, called in /home/runner/work/MabelPy/MabelPy/tests/TestCase.php on line 101

/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1839
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:101
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:55

13) App\Tests\User\UserTest::test_can_be_instantiated
TypeError: Illuminate\Database\Eloquent\Model::setConnectionResolver(): Argument #1 ($resolver) must be of type Illuminate\Database\ConnectionResolverInterface, class@anonymous given, called in /home/runner/work/MabelPy/MabelPy/tests/TestCase.php on line 101

/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1839
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:101
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:55

ERRORS!
Tests: 13, Assertions: 0, Errors: 13.
Error: Process completed with exit code 2.