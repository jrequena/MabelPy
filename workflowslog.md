Run vendor/bin/php-cs-fixer fix --dry-run --diff --allow-risky=yes
PHP CS Fixer 3.92.3 Exceptional Exception by Fabien Potencier, Dariusz Ruminski and contributors.
PHP runtime: 8.2.29
Loaded config default from "/home/runner/work/MabelPy/MabelPy/.php-cs-fixer.dist.php".
Running analysis on 1 core sequentially.
  0/40 [░░░░░░░░░░░░░░░░░░░░░░░░░░░░]   0%
  4/40 [▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░]  10%
 16/40 [▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░]  40%
 32/40 [▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░]  80%
 40/40 [▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓] 100%

   1) src/Infrastructure/Http/Requests/CreateUserRequest.php

      ---------- begin diff ----------
--- /home/runner/work/MabelPy/MabelPy/src/Infrastructure/Http/Requests/CreateUserRequest.php
+++ /home/runner/work/MabelPy/MabelPy/src/Infrastructure/Http/Requests/CreateUserRequest.php
@@ -21,4 +21,4 @@
             'status' => ['nullable'],
         ];
     }
-}
\ No newline at end of file
+}

      ----------- end diff -----------

   2) src/Infrastructure/Http/Requests/DeactivateUserRequest.php
      ---------- begin diff ----------
--- /home/runner/work/MabelPy/MabelPy/src/Infrastructure/Http/Requests/DeactivateUserRequest.php
+++ /home/runner/work/MabelPy/MabelPy/src/Infrastructure/Http/Requests/DeactivateUserRequest.php
@@ -19,4 +19,4 @@
             'id' => ['required', 'integer'],
         ];
     }
-}
\ No newline at end of file
+}
 {
@@ -14,7 +14,7 @@
     {
         $repository = $this->createMock(PostRepository::class);
         $useCase = new CreateUserUseCase($repository);
-        
+
         $this->assertInstanceOf(CreateUserUseCase::class, $useCase);
     }
-}
\ No newline at end of file
+}

      ----------- end diff -----------

  34) tests/Post/PostMapperTest.php
      ---------- begin diff ----------
--- /home/runner/work/MabelPy/MabelPy/tests/Post/PostMapperTest.php
+++ /home/runner/work/MabelPy/MabelPy/tests/Post/PostMapperTest.php
@@ -4,9 +4,9 @@
 
 namespace App\Tests;
 
-use PHPUnit\Framework\TestCase;
 use App\Domain\Post;
 use App\Infrastructure\Mapper\PostMapper;
+use PHPUnit\Framework\TestCase;
 
 final class PostMapperTest extends TestCase
 {
@@ -40,4 +40,4 @@
         $this->assertEquals('sample', $data['content']);
         $this->assertEquals(null, $data['user']);
     }
-}
\ No newline at end of file
+}

      ----------- end diff -----------


Found 34 of 40 files that can be fixed in 0.152 seconds, 18.00 MB memory used
Error: Process completed with exit code 12.