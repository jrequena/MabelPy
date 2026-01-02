Run vendor/bin/phpunit
PHPUnit 10.5.60 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.2.29
Configuration: /home/runner/work/MabelPy/MabelPy/phpunit.xml

EE.....EE....                                                     13 / 13 (100%)

Time: 00:00.026, Memory: 12.00 MB

There were 4 errors:

1) App\Tests\Post\EloquentPostRepositoryTest::test_can_save_and_find_entity
Error: Call to a member function connection() on null

/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1820
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1786
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1577
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1496
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1532
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1485
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:2335
/home/runner/work/MabelPy/MabelPy/src/Infrastructure/Persistence/Eloquent/EloquentPostRepository.php:80
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:64
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/support/Facades/Facade.php:355
/home/runner/work/MabelPy/MabelPy/src/Infrastructure/Persistence/Eloquent/EloquentPostRepository.php:73
/home/runner/work/MabelPy/MabelPy/tests/Post/EloquentPostRepositoryTest.php:35

2) App\Tests\Post\EloquentPostRepositoryTest::test_can_delete_entity
Error: Call to a member function connection() on null

/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1820
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1786
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1577
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1496
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1532
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1485
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:2335
/home/runner/work/MabelPy/MabelPy/src/Infrastructure/Persistence/Eloquent/EloquentPostRepository.php:80
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:64
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/support/Facades/Facade.php:355
/home/runner/work/MabelPy/MabelPy/src/Infrastructure/Persistence/Eloquent/EloquentPostRepository.php:73
/home/runner/work/MabelPy/MabelPy/tests/Post/EloquentPostRepositoryTest.php:53

3) App\Tests\User\EloquentUserRepositoryTest::test_can_save_and_find_entity
Error: Call to a member function connection() on null

/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1820
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1786
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1577
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1496
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1532
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1485
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:2335
/home/runner/work/MabelPy/MabelPy/src/Infrastructure/Persistence/Eloquent/EloquentUserRepository.php:77
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:64
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/support/Facades/Facade.php:355
/home/runner/work/MabelPy/MabelPy/src/Infrastructure/Persistence/Eloquent/EloquentUserRepository.php:73
/home/runner/work/MabelPy/MabelPy/tests/User/EloquentUserRepositoryTest.php:38

4) App\Tests\User\EloquentUserRepositoryTest::test_can_delete_entity
Error: Call to a member function connection() on null

/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1820
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1786
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1577
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1496
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1532
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1485
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:2335
/home/runner/work/MabelPy/MabelPy/src/Infrastructure/Persistence/Eloquent/EloquentUserRepository.php:77
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:64
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/support/Facades/Facade.php:355
/home/runner/work/MabelPy/MabelPy/src/Infrastructure/Persistence/Eloquent/EloquentUserRepository.php:73
/home/runner/work/MabelPy/MabelPy/tests/User/EloquentUserRepositoryTest.php:58

ERRORS!
Tests: 13, Assertions: 17, Errors: 4.
Error: Process completed with exit code 2.