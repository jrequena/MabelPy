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

E......E.....                                                     13 / 13 (100%)

Time: 00:00.051, Memory: 16.00 MB

There were 2 errors:

1) App\Tests\Post\EloquentPostRepositoryTest::test_can_save_and_find_entity
Error: Class "User" not found

/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Concerns/HasRelationships.php:793
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Concerns/HasRelationships.php:225
/home/runner/work/MabelPy/MabelPy/src/Infrastructure/Persistence/Eloquent/Post.php:21
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Builder.php:804
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Relations/Relation.php:110
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Builder.php:802
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Builder.php:776
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Builder.php:756
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Builder.php:724
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Concerns/BuildsQueries.php:333
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Builder.php:449
/home/runner/work/MabelPy/MabelPy/src/Infrastructure/Persistence/Eloquent/EloquentPostRepository.php:27
/home/runner/work/MabelPy/MabelPy/tests/Post/EloquentPostRepositoryTest.php:38

2) App\Tests\User\EloquentUserRepositoryTest::test_can_save_and_find_entity
Error: Class "Post" not found

/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Concerns/HasRelationships.php:793
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Concerns/HasRelationships.php:388
/home/runner/work/MabelPy/MabelPy/src/Infrastructure/Persistence/Eloquent/User.php:22
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Builder.php:804
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Relations/Relation.php:110
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Builder.php:802
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Builder.php:776
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Builder.php:756
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Builder.php:724
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Concerns/BuildsQueries.php:333
/home/runner/work/MabelPy/MabelPy/vendor/illuminate/database/Eloquent/Builder.php:449
/home/runner/work/MabelPy/MabelPy/src/Infrastructure/Persistence/Eloquent/EloquentUserRepository.php:27
/home/runner/work/MabelPy/MabelPy/tests/User/EloquentUserRepositoryTest.php:41

ERRORS!
Tests: 13, Assertions: 19, Errors: 2.
Error: Process completed with exit code 2.