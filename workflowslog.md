
0s
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


An error occurred inside PHPUnit.

Message:  Class "Tests\TestCase" not found
Location: /home/runner/work/MabelPy/MabelPy/tests/Post/EloquentPostRepositoryTest.php:12

#0 /home/runner/work/MabelPy/MabelPy/vendor/phpunit/phpunit/src/Runner/TestSuiteLoader.php(115): require_once()
#1 /home/runner/work/MabelPy/MabelPy/vendor/phpunit/phpunit/src/Runner/TestSuiteLoader.php(48): PHPUnit\Runner\TestSuiteLoader->loadSuiteClassFile()
#2 /home/runner/work/MabelPy/MabelPy/vendor/phpunit/phpunit/src/Framework/TestSuite.php(251): PHPUnit\Runner\TestSuiteLoader->load()
#3 /home/runner/work/MabelPy/MabelPy/vendor/phpunit/phpunit/src/Framework/TestSuite.php(269): PHPUnit\Framework\TestSuite->addTestFile()
#4 /home/runner/work/MabelPy/MabelPy/vendor/phpunit/phpunit/src/TextUI/Configuration/Xml/TestSuiteMapper.php(102): PHPUnit\Framework\TestSuite->addTestFiles()
#5 /home/runner/work/MabelPy/MabelPy/vendor/phpunit/phpunit/src/TextUI/Configuration/TestSuiteBuilder.php(75): PHPUnit\TextUI\XmlConfiguration\TestSuiteMapper->map()
#6 /home/runner/work/MabelPy/MabelPy/vendor/phpunit/phpunit/src/TextUI/Application.php(394): PHPUnit\TextUI\Configuration\TestSuiteBuilder->build()
#7 /home/runner/work/MabelPy/MabelPy/vendor/phpunit/phpunit/src/TextUI/Application.php(114): PHPUnit\TextUI\Application->buildTestSuite()
#8 /home/runner/work/MabelPy/MabelPy/vendor/phpunit/phpunit/phpunit(104): PHPUnit\TextUI\Application->run()
#9 /home/runner/work/MabelPy/MabelPy/vendor/bin/phpunit(122): include('...')
#10 {main}
Error: Process completed with exit code 255.
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


An error occurred inside PHPUnit.

Message:  Class "Tests\TestCase" not found
Location: /home/runner/work/MabelPy/MabelPy/tests/Post/EloquentPostRepositoryTest.php:12

#0 /home/runner/work/MabelPy/MabelPy/vendor/phpunit/phpunit/src/Runner/TestSuiteLoader.php(115): require_once()
#1 /home/runner/work/MabelPy/MabelPy/vendor/phpunit/phpunit/src/Runner/TestSuiteLoader.php(48): PHPUnit\Runner\TestSuiteLoader->loadSuiteClassFile()
#2 /home/runner/work/MabelPy/MabelPy/vendor/phpunit/phpunit/src/Framework/TestSuite.php(251): PHPUnit\Runner\TestSuiteLoader->load()
#3 /home/runner/work/MabelPy/MabelPy/vendor/phpunit/phpunit/src/Framework/TestSuite.php(269): PHPUnit\Framework\TestSuite->addTestFile()
#4 /home/runner/work/MabelPy/MabelPy/vendor/phpunit/phpunit/src/TextUI/Configuration/Xml/TestSuiteMapper.php(102): PHPUnit\Framework\TestSuite->addTestFiles()
#5 /home/runner/work/MabelPy/MabelPy/vendor/phpunit/phpunit/src/TextUI/Configuration/TestSuiteBuilder.php(75): PHPUnit\TextUI\XmlConfiguration\TestSuiteMapper->map()
#6 /home/runner/work/MabelPy/MabelPy/vendor/phpunit/phpunit/src/TextUI/Application.php(394): PHPUnit\TextUI\Configuration\TestSuiteBuilder->build()
#7 /home/runner/work/MabelPy/MabelPy/vendor/phpunit/phpunit/src/TextUI/Application.php(114): PHPUnit\TextUI\Application->buildTestSuite()
#8 /home/runner/work/MabelPy/MabelPy/vendor/phpunit/phpunit/phpunit(104): PHPUnit\TextUI\Application->run()
#9 /home/runner/work/MabelPy/MabelPy/vendor/bin/phpunit(122): include('...')
#10 {main}
Error: Process completed with exit code 255.