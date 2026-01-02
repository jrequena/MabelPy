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

Time: 00:00.028, Memory: 12.00 MB

There were 4 errors:

1) App\Tests\Post\EloquentPostRepositoryTest::test_can_save_and_find_entity
TypeError: Illuminate\Database\Eloquent\Builder::__construct(): Argument #1 ($query) must be of type Illuminate\Database\Query\Builder, Illuminate\Database\ConnectionResolverInterface@anonymous given, called in /home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php on line 1567

/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Builder.php:147
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1567
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1495
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1532
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1485
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:2335
/home/runner/work/MabelPy/MabelPy/src/Infrastructure/Persistence/Eloquent/EloquentPostRepository.php:80
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:87
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/support/Facades/Facade.php:355
/home/runner/work/MabelPy/MabelPy/src/Infrastructure/Persistence/Eloquent/EloquentPostRepository.php:73
/home/runner/work/MabelPy/MabelPy/tests/Post/EloquentPostRepositoryTest.php:35

2) App\Tests\Post\EloquentPostRepositoryTest::test_can_delete_entity
TypeError: Illuminate\Database\Eloquent\Builder::__construct(): Argument #1 ($query) must be of type Illuminate\Database\Query\Builder, Illuminate\Database\ConnectionResolverInterface@anonymous given, called in /home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php on line 1567

/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Builder.php:147
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1567
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1495
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1532
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1485
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:2335
/home/runner/work/MabelPy/MabelPy/src/Infrastructure/Persistence/Eloquent/EloquentPostRepository.php:80
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:87
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/support/Facades/Facade.php:355
/home/runner/work/MabelPy/MabelPy/src/Infrastructure/Persistence/Eloquent/EloquentPostRepository.php:73
/home/runner/work/MabelPy/MabelPy/tests/Post/EloquentPostRepositoryTest.php:53

3) App\Tests\User\EloquentUserRepositoryTest::test_can_save_and_find_entity
TypeError: Illuminate\Database\Eloquent\Builder::__construct(): Argument #1 ($query) must be of type Illuminate\Database\Query\Builder, Illuminate\Database\ConnectionResolverInterface@anonymous given, called in /home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php on line 1567

/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Builder.php:147
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1567
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1495
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1532
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1485
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:2335
/home/runner/work/MabelPy/MabelPy/src/Infrastructure/Persistence/Eloquent/EloquentUserRepository.php:77
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:87
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/support/Facades/Facade.php:355
/home/runner/work/MabelPy/MabelPy/src/Infrastructure/Persistence/Eloquent/EloquentUserRepository.php:73
/home/runner/work/MabelPy/MabelPy/tests/User/EloquentUserRepositoryTest.php:38

4) App\Tests\User\EloquentUserRepositoryTest::test_can_delete_entity
TypeError: Illuminate\Database\Eloquent\Builder::__construct(): Argument #1 ($query) must be of type Illuminate\Database\Query\Builder, Illuminate\Database\ConnectionResolverInterface@anonymous given, called in /home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php on line 1567

/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Builder.php:147
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1567
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1495
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1532
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:1485
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Model.php:2335
/home/runner/work/MabelPy/MabelPy/src/Infrastructure/Persistence/Eloquent/EloquentUserRepository.php:77
/home/runner/work/MabelPy/MabelPy/tests/TestCase.php:87
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/support/Facades/Facade.php:355
/home/runner/work/MabelPy/MabelPy/src/Infrastructure/Persistence/Eloquent/EloquentUserRepository.php:73
/home/runner/work/MabelPy/MabelPy/tests/User/EloquentUserRepositoryTest.php:58

ERRORS!
Tests: 13, Assertions: 17, Errors: 4.
Error: Process completed with exit code 2.