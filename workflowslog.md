Run vendor/bin/php-cs-fixer fix --dry-run --diff --allow-risky=yes
PHP CS Fixer 3.92.3 Exceptional Exception by Fabien Potencier, Dariusz Ruminski and contributors.
PHP runtime: 8.2.29
Loaded config default from "/home/runner/work/MabelPy/MabelPy/.php-cs-fixer.dist.php".
Running analysis on 1 core sequentially.
  0/40 [░░░░░░░░░░░░░░░░░░░░░░░░░░░░]   0%
  8/40 [▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░]  20%
 24/40 [▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░]  60%
 36/40 [▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░]  90%
 40/40 [▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓] 100%

   1) src/Infrastructure/Http/Requests/CreateUserRequest.php
      ---------- begin diff ----------

--- /home/runner/work/MabelPy/MabelPy/src/Infrastructure/Http/Requests/CreateUserRequest.php
Files that were not fixed due to errors reported during linting before fixing:
+++ /home/runner/work/MabelPy/MabelPy/src/Infrastructure/Http/Requests/CreateUserRequest.php
   1) /home/runner/work/MabelPy/MabelPy/src/Domain/UseCase/User/UpdateUserEmail/UpdateUserEmailResponse.php
   2) /home/runner/work/MabelPy/MabelPy/src/Domain/UseCase/User/UpdateUserEmail/UpdateUserEmailRequest.php
   3) /home/runner/work/MabelPy/MabelPy/src/Domain/UseCase/User/DeactivateUser/DeactivateUserResponse.php
   4) /home/runner/work/MabelPy/MabelPy/src/Domain/UseCase/User/DeactivateUser/DeactivateUserRequest.php
   5) /home/runner/work/MabelPy/MabelPy/src/Domain/UseCase/User/CreateUser/CreateUserResponse.php
   6) /home/runner/work/MabelPy/MabelPy/src/Domain/UseCase/User/CreateUser/CreateUserRequest.php
@@ -1,5 +1,7 @@
 <?php
 
+declare(strict_types=1);
+
 namespace App\Infrastructure\Http\Requests;
 
 use Illuminate\Foundation\Http\FormRequest;
@@ -19,4 +21,4 @@
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
@@ -1,5 +1,7 @@
 <?php
 
+declare(strict_types=1);
+
 namespace App\Infrastructure\Http\Requests;
 
 use Illuminate\Foundation\Http\FormRequest;
@@ -17,4 +19,4 @@
             'id' => ['required', 'integer'],
         ];
     }
-}
\ No newline at end of file
+}

      ----------- end diff -----------

   3) src/Infrastructure/Http/Requests/UpdateUserEmailRequest.php
      ---------- begin diff ----------
--- /home/runner/work/MabelPy/MabelPy/src/Infrastructure/Http/Requests/UpdateUserEmailRequest.php
+++ /home/runner/work/MabelPy/MabelPy/src/Infrastructure/Http/Requests/UpdateUserEmailRequest.php
@@ -1,5 +1,7 @@
 <?php
 
+declare(strict_types=1);
+
 namespace App\Infrastructure\Http\Requests;
 
 use Illuminate\Foundation\Http\FormRequest;
@@ -18,4 +20,4 @@
             'email' => ['required', 'string', 'regex:/.+@.+\..+/', 'unique:users,email'],
         ];
     }
-}
\ No newline at end of file
+}

      ----------- end diff -----------

   4) src/Infrastructure/Http/Controllers/CreateUserController.php
      ---------- begin diff ----------
--- /home/runner/work/MabelPy/MabelPy/src/Infrastructure/Http/Controllers/CreateUserController.php
+++ /home/runner/work/MabelPy/MabelPy/src/Infrastructure/Http/Controllers/CreateUserController.php
@@ -4,9 +4,9 @@
 
 namespace App\Infrastructure\Http\Controllers;
 
+use App\Domain\UseCase\User\CreateUser\CreateUserRequest as UseCaseRequest;
+use App\Domain\UseCase\User\CreateUser\CreateUserUseCase;
 use App\Infrastructure\Http\Requests\CreateUserRequest as HttpRequest;
-use App\Domain\UseCase\User\CreateUser\CreateUserUseCase;
-use App\Domain\UseCase\User\CreateUser\CreateUserRequest as UseCaseRequest;
 use Illuminate\Http\JsonResponse;
 use Illuminate\Routing\Controller;
 
@@ -15,10 +15,13 @@
     public function __invoke(HttpRequest $request, CreateUserUseCase $useCase): JsonResponse
     {
         $input = new UseCaseRequest(
-            name: $request->input('name'),            email: $request->input('email'),            status: $request->input('status')        );
+            name: $request->input('name'),
+            email: $request->input('email'),
+            status: $request->input('status')
+        );
 
         $response = $useCase->execute($input);
 
         return response()->json($response);
     }
-}
\ No newline at end of file
+}

      ----------- end diff -----------

   5) src/Infrastructure/Http/Controllers/DeactivateUserController.php
      ---------- begin diff ----------
--- /home/runner/work/MabelPy/MabelPy/src/Infrastructure/Http/Controllers/DeactivateUserController.php
+++ /home/runner/work/MabelPy/MabelPy/src/Infrastructure/Http/Controllers/DeactivateUserController.php
@@ -4,9 +4,9 @@
 
 namespace App\Infrastructure\Http\Controllers;
 
+use App\Domain\UseCase\User\DeactivateUser\DeactivateUserRequest as UseCaseRequest;
+use App\Domain\UseCase\User\DeactivateUser\DeactivateUserUseCase;
 use App\Infrastructure\Http\Requests\DeactivateUserRequest as HttpRequest;
-use App\Domain\UseCase\User\DeactivateUser\DeactivateUserUseCase;
-use App\Domain\UseCase\User\DeactivateUser\DeactivateUserRequest as UseCaseRequest;
 use Illuminate\Http\JsonResponse;
 use Illuminate\Routing\Controller;
 
@@ -15,10 +15,11 @@
     public function __invoke(HttpRequest $request, DeactivateUserUseCase $useCase): JsonResponse
     {
         $input = new UseCaseRequest(
-            id: $request->input('id')        );
+            id: $request->input('id')
+        );
 
         $response = $useCase->execute($input);
 
         return response()->json($response);
     }
-}
\ No newline at end of file
+}

      ----------- end diff -----------

   6) src/Infrastructure/Http/Controllers/UpdateUserEmailController.php
      ---------- begin diff ----------
--- /home/runner/work/MabelPy/MabelPy/src/Infrastructure/Http/Controllers/UpdateUserEmailController.php
+++ /home/runner/work/MabelPy/MabelPy/src/Infrastructure/Http/Controllers/UpdateUserEmailController.php
@@ -4,9 +4,9 @@
 
 namespace App\Infrastructure\Http\Controllers;
 
+use App\Domain\UseCase\User\UpdateUserEmail\UpdateUserEmailRequest as UseCaseRequest;
+use App\Domain\UseCase\User\UpdateUserEmail\UpdateUserEmailUseCase;
 use App\Infrastructure\Http\Requests\UpdateUserEmailRequest as HttpRequest;
-use App\Domain\UseCase\User\UpdateUserEmail\UpdateUserEmailUseCase;
-use App\Domain\UseCase\User\UpdateUserEmail\UpdateUserEmailRequest as UseCaseRequest;
 use Illuminate\Http\JsonResponse;
 use Illuminate\Routing\Controller;
 
@@ -15,10 +15,12 @@
     public function __invoke(HttpRequest $request, UpdateUserEmailUseCase $useCase): JsonResponse
     {
         $input = new UseCaseRequest(
-            id: $request->input('id'),            email: $request->input('email')        );
+            id: $request->input('id'),
+            email: $request->input('email')
+        );
 
         $response = $useCase->execute($input);
 
         return response()->json($response);
     }
-}
\ No newline at end of file
+}

      ----------- end diff -----------

   7) src/Infrastructure/Laravel/UserServiceProvider.php
      ---------- begin diff ----------
--- /home/runner/work/MabelPy/MabelPy/src/Infrastructure/Laravel/UserServiceProvider.php
+++ /home/runner/work/MabelPy/MabelPy/src/Infrastructure/Laravel/UserServiceProvider.php
@@ -4,11 +4,11 @@
 
 namespace App\Infrastructure\Laravel;
 
-use Illuminate\Support\ServiceProvider;
+use App\Domain\Repository\PostRepository;
 use App\Domain\Repository\UserRepository;
+use App\Infrastructure\Persistence\Eloquent\EloquentPostRepository;
 use App\Infrastructure\Persistence\Eloquent\EloquentUserRepository;
-use App\Domain\Repository\PostRepository;
-use App\Infrastructure\Persistence\Eloquent\EloquentPostRepository;
+use Illuminate\Support\ServiceProvider;
 
 final class UserServiceProvider extends ServiceProvider
 {
@@ -17,4 +17,4 @@
         $this->app->bind(UserRepository::class, EloquentUserRepository::class);
         $this->app->bind(PostRepository::class, EloquentPostRepository::class);
     }
-}
\ No newline at end of file
+}

      ----------- end diff -----------

   8) src/Infrastructure/Persistence/Eloquent/Post.php
      ---------- begin diff ----------
--- /home/runner/work/MabelPy/MabelPy/src/Infrastructure/Persistence/Eloquent/Post.php
+++ /home/runner/work/MabelPy/MabelPy/src/Infrastructure/Persistence/Eloquent/Post.php
@@ -21,4 +21,4 @@
         return $this->belongsTo('User');
     }
 
-}
\ No newline at end of file
+}

      ----------- end diff -----------

   9) src/Infrastructure/Persistence/Eloquent/EloquentPostRepository.php
      ---------- begin diff ----------
--- /home/runner/work/MabelPy/MabelPy/src/Infrastructure/Persistence/Eloquent/EloquentPostRepository.php
+++ /home/runner/work/MabelPy/MabelPy/src/Infrastructure/Persistence/Eloquent/EloquentPostRepository.php
@@ -5,7 +5,6 @@
 namespace App\Infrastructure\Persistence\Eloquent;
 
 use App\Domain\Repository\PostRepository;
-use App\Infrastructure\Persistence\Eloquent\Post;
 
 final class EloquentPostRepository implements PostRepository
 {
@@ -28,4 +27,4 @@
             [] // Add mapping logic
         );
     }
-}
\ No newline at end of file
+}

      ----------- end diff -----------

  10) src/Infrastructure/Persistence/Eloquent/User.php
      ---------- begin diff ----------
--- /home/runner/work/MabelPy/MabelPy/src/Infrastructure/Persistence/Eloquent/User.php
+++ /home/runner/work/MabelPy/MabelPy/src/Infrastructure/Persistence/Eloquent/User.php
@@ -22,4 +22,4 @@
         return $this->hasMany('Post');
     }
 
-}
\ No newline at end of file
+}

      ----------- end diff -----------

  11) src/Infrastructure/Persistence/Eloquent/EloquentUserRepository.php
      ---------- begin diff ----------
--- /home/runner/work/MabelPy/MabelPy/src/Infrastructure/Persistence/Eloquent/EloquentUserRepository.php
+++ /home/runner/work/MabelPy/MabelPy/src/Infrastructure/Persistence/Eloquent/EloquentUserRepository.php
@@ -5,7 +5,6 @@
 namespace App\Infrastructure\Persistence\Eloquent;
 
 use App\Domain\Repository\UserRepository;
-use App\Infrastructure\Persistence\Eloquent\User;
 
 final class EloquentUserRepository implements UserRepository
 {
@@ -28,4 +27,4 @@
             [] // Add mapping logic
         );
     }
-}
\ No newline at end of file
+}

      ----------- end diff -----------

  12) src/Infrastructure/Mapper/PostMapper.php
      ---------- begin diff ----------
--- /home/runner/work/MabelPy/MabelPy/src/Infrastructure/Mapper/PostMapper.php
+++ /home/runner/work/MabelPy/MabelPy/src/Infrastructure/Mapper/PostMapper.php
@@ -27,4 +27,4 @@
             'user' => null // TODO: Map relation User,
         ];
     }
-}
\ No newline at end of file
+}

      ----------- end diff -----------

  13) src/Infrastructure/Mapper/UserMapper.php
      ---------- begin diff ----------
--- /home/runner/work/MabelPy/MabelPy/src/Infrastructure/Mapper/UserMapper.php
+++ /home/runner/work/MabelPy/MabelPy/src/Infrastructure/Mapper/UserMapper.php
@@ -32,4 +32,4 @@
             'posts' => [] // TODO: Map collection Post,
         ];
     }
-}
\ No newline at end of file
+}

      ----------- end diff -----------

  14) src/Domain/Post.php
      ---------- begin diff ----------
--- /home/runner/work/MabelPy/MabelPy/src/Domain/Post.php
+++ /home/runner/work/MabelPy/MabelPy/src/Domain/Post.php
@@ -4,7 +4,6 @@
 
 namespace App\Domain;
 
-
 final class Post
 {
     public function __construct(
@@ -14,4 +13,4 @@
         public readonly User $user = null,
     ) {
     }
-}
\ No newline at end of file
+}

      ----------- end diff -----------

  15) src/Domain/UseCase/User/UpdateUserEmail/UpdateUserEmailUseCase.php
      ---------- begin diff ----------
--- /home/runner/work/MabelPy/MabelPy/src/Domain/UseCase/User/UpdateUserEmail/UpdateUserEmailUseCase.php
+++ /home/runner/work/MabelPy/MabelPy/src/Domain/UseCase/User/UpdateUserEmail/UpdateUserEmailUseCase.php
@@ -5,6 +5,7 @@
 namespace App\Domain\UseCase\User\UpdateUserEmail;
 
 use App\Domain\Repository\UserRepository;
+
 final class UpdateUserEmailUseCase
 {
     public function __construct(
@@ -26,4 +27,4 @@
         // TODO: Implement actual execution and persistence
         return new UpdateUserEmailResponse();
     }
-}
\ No newline at end of file
+}

      ----------- end diff -----------

  16) src/Domain/UseCase/User/DeactivateUser/DeactivateUserUseCase.php
      ---------- begin diff ----------
--- /home/runner/work/MabelPy/MabelPy/src/Domain/UseCase/User/DeactivateUser/DeactivateUserUseCase.php
+++ /home/runner/work/MabelPy/MabelPy/src/Domain/UseCase/User/DeactivateUser/DeactivateUserUseCase.php
@@ -4,8 +4,9 @@
 
 namespace App\Domain\UseCase\User\DeactivateUser;
 
+use App\Domain\Event\User\UserDeactivatedEvent;
 use App\Domain\Repository\UserRepository;
-use App\Domain\Event\User\UserDeactivatedEvent;
+
 final class DeactivateUserUseCase
 {
     public function __construct(
@@ -24,4 +25,4 @@
         // TODO: Implement actual execution and persistence
         return new DeactivateUserResponse();
     }
-}
\ No newline at end of file
+}

      ----------- end diff -----------

  17) src/Domain/UseCase/User/CreateUser/CreateUserUseCase.php
      ---------- begin diff ----------
--- /home/runner/work/MabelPy/MabelPy/src/Domain/UseCase/User/CreateUser/CreateUserUseCase.php
+++ /home/runner/work/MabelPy/MabelPy/src/Domain/UseCase/User/CreateUser/CreateUserUseCase.php
@@ -5,6 +5,7 @@
 namespace App\Domain\UseCase\User\CreateUser;
 
 use App\Domain\Repository\UserRepository;
+
 final class CreateUserUseCase
 {
     public function __construct(
@@ -26,4 +27,4 @@
         // TODO: Implement actual execution and persistence
         return new CreateUserResponse();
     }
-}
\ No newline at end of file
+}

      ----------- end diff -----------

  18) src/Domain/Event/User/UserDeactivatedEvent.php
      ---------- begin diff ----------
--- /home/runner/work/MabelPy/MabelPy/src/Domain/Event/User/UserDeactivatedEvent.php
+++ /home/runner/work/MabelPy/MabelPy/src/Domain/Event/User/UserDeactivatedEvent.php
@@ -9,10 +9,11 @@
 
 final class UserDeactivatedEvent
 {
-    use Dispatchable, SerializesModels;
+    use Dispatchable;
+    use SerializesModels;
 
     public function __construct(
         public readonly \App\Domain\User $entity
     ) {
     }
-}
\ No newline at end of file
+}

      ----------- end diff -----------

  19) src/Domain/Enum/UserStatus.php
      ---------- begin diff ----------
--- /home/runner/work/MabelPy/MabelPy/src/Domain/Enum/UserStatus.php
+++ /home/runner/work/MabelPy/MabelPy/src/Domain/Enum/UserStatus.php
@@ -9,4 +9,4 @@
     case ACTIVE = 'ACTIVE';
     case INACTIVE = 'INACTIVE';
     case PENDING = 'PENDING';
-}
\ No newline at end of file
+}

      ----------- end diff -----------

  20) src/Domain/Repository/UserRepository.php
      ---------- begin diff ----------
--- /home/runner/work/MabelPy/MabelPy/src/Domain/Repository/UserRepository.php
+++ /home/runner/work/MabelPy/MabelPy/src/Domain/Repository/UserRepository.php
@@ -11,4 +11,4 @@
     public function save(User $entity): void;
     public function findById(int $id): ?User;
     public function delete(int $id): void;
-}
\ No newline at end of file
+}

      ----------- end diff -----------

  21) src/Domain/Repository/PostRepository.php
      ---------- begin diff ----------
--- /home/runner/work/MabelPy/MabelPy/src/Domain/Repository/PostRepository.php
+++ /home/runner/work/MabelPy/MabelPy/src/Domain/Repository/PostRepository.php
@@ -11,4 +11,4 @@
     public function save(Post $entity): void;
     public function findById(int $id): ?Post;
     public function delete(int $id): void;
-}
\ No newline at end of file
+}

      ----------- end diff -----------

  22) src/Domain/User.php
      ---------- begin diff ----------
--- /home/runner/work/MabelPy/MabelPy/src/Domain/User.php
+++ /home/runner/work/MabelPy/MabelPy/src/Domain/User.php
@@ -4,10 +4,9 @@
 
 namespace App\Domain;
 
+use App\Domain\Enum\UserStatus;
 use DateTimeImmutable;
 
-use App\Domain\Enum\UserStatus;
-
 final class User
 {
     public function __construct(
@@ -19,4 +18,4 @@
         public readonly array $posts = [],
     ) {
     }
-}
\ No newline at end of file
+}

      ----------- end diff -----------

  23) tests/python/snapshots/test_generators/test_dto_generation_snapshot/UserDTO.php
      ---------- begin diff ----------
--- /home/runner/work/MabelPy/MabelPy/tests/python/snapshots/test_generators/test_dto_generation_snapshot/UserDTO.php
+++ /home/runner/work/MabelPy/MabelPy/tests/python/snapshots/test_generators/test_dto_generation_snapshot/UserDTO.php
@@ -14,4 +14,4 @@
         public readonly UserStatus $status,
     ) {
     }
-}
\ No newline at end of file
+}

      ----------- end diff -----------

  24) tests/python/snapshots/test_generators/test_enum_generation_snapshot/UserStatusEnum.php
      ---------- begin diff ----------
--- /home/runner/work/MabelPy/MabelPy/tests/python/snapshots/test_generators/test_enum_generation_snapshot/UserStatusEnum.php
+++ /home/runner/work/MabelPy/MabelPy/tests/python/snapshots/test_generators/test_enum_generation_snapshot/UserStatusEnum.php
@@ -9,4 +9,4 @@
     case ACTIVE = 'ACTIVE';
     case INACTIVE = 'INACTIVE';
     case PENDING = 'PENDING';
-}
\ No newline at end of file
+}

      ----------- end diff -----------

  25) tests/User/UpdateUserEmailUseCaseTest.php
      ---------- begin diff ----------
--- /home/runner/work/MabelPy/MabelPy/tests/User/UpdateUserEmailUseCaseTest.php
+++ /home/runner/work/MabelPy/MabelPy/tests/User/UpdateUserEmailUseCaseTest.php
@@ -4,9 +4,9 @@
 
 namespace App\Tests;
 
-use PHPUnit\Framework\TestCase;
 use App\Domain\Repository\UserRepository;
 use App\Domain\UseCase\User\UpdateUserEmail\UpdateUserEmailUseCase;
+use PHPUnit\Framework\TestCase;
 
 final class UpdateUserEmailUseCaseTest extends TestCase
 {
@@ -14,7 +14,7 @@
     {
         $repository = $this->createMock(UserRepository::class);
         $useCase = new UpdateUserEmailUseCase($repository);
-        
+
         $this->assertInstanceOf(UpdateUserEmailUseCase::class, $useCase);
     }
-}
\ No newline at end of file
+}

      ----------- end diff -----------

  26) tests/User/UserMapperTest.php
      ---------- begin diff ----------
--- /home/runner/work/MabelPy/MabelPy/tests/User/UserMapperTest.php
+++ /home/runner/work/MabelPy/MabelPy/tests/User/UserMapperTest.php
@@ -4,9 +4,9 @@
 
 namespace App\Tests;
 
-use PHPUnit\Framework\TestCase;
 use App\Domain\User;
 use App\Infrastructure\Mapper\UserMapper;
+use PHPUnit\Framework\TestCase;
 
 final class UserMapperTest extends TestCase
 {
@@ -46,4 +46,4 @@
         $this->assertEquals('2023-01-01T00:00:00+00:00', $data['created_at']);
         $this->assertEquals([], $data['posts']);
     }
-}
\ No newline at end of file
+}

      ----------- end diff -----------

  27) tests/User/DeactivateUserUseCaseTest.php
      ---------- begin diff ----------
--- /home/runner/work/MabelPy/MabelPy/tests/User/DeactivateUserUseCaseTest.php
+++ /home/runner/work/MabelPy/MabelPy/tests/User/DeactivateUserUseCaseTest.php
@@ -4,9 +4,9 @@
 
 namespace App\Tests;
 
-use PHPUnit\Framework\TestCase;
 use App\Domain\Repository\UserRepository;
 use App\Domain\UseCase\User\DeactivateUser\DeactivateUserUseCase;
+use PHPUnit\Framework\TestCase;
 
 final class DeactivateUserUseCaseTest extends TestCase
 {
@@ -14,7 +14,7 @@
     {
         $repository = $this->createMock(UserRepository::class);
         $useCase = new DeactivateUserUseCase($repository);
-        
+
         $this->assertInstanceOf(DeactivateUserUseCase::class, $useCase);
     }
-}
\ No newline at end of file
+}

      ----------- end diff -----------

  28) tests/User/CreateUserUseCaseTest.php
      ---------- begin diff ----------
--- /home/runner/work/MabelPy/MabelPy/tests/User/CreateUserUseCaseTest.php
+++ /home/runner/work/MabelPy/MabelPy/tests/User/CreateUserUseCaseTest.php
@@ -4,9 +4,9 @@
 
 namespace App\Tests;
 
-use PHPUnit\Framework\TestCase;
 use App\Domain\Repository\UserRepository;
 use App\Domain\UseCase\User\CreateUser\CreateUserUseCase;
+use PHPUnit\Framework\TestCase;
 
 final class CreateUserUseCaseTest extends TestCase
 {
@@ -14,7 +14,7 @@
     {
         $repository = $this->createMock(UserRepository::class);
         $useCase = new CreateUserUseCase($repository);
-        
+
         $this->assertInstanceOf(CreateUserUseCase::class, $useCase);
     }
-}
\ No newline at end of file
+}

      ----------- end diff -----------

  29) tests/User/UserTest.php
      ---------- begin diff ----------
--- /home/runner/work/MabelPy/MabelPy/tests/User/UserTest.php
+++ /home/runner/work/MabelPy/MabelPy/tests/User/UserTest.php
@@ -4,10 +4,9 @@
 
 namespace App\Tests;
 
+use App\Domain\User;
 use PHPUnit\Framework\TestCase;
-use App\Domain\User;
 
-
 final class UserTest extends TestCase
 {
     public function test_can_be_instantiated(): void
@@ -23,4 +22,4 @@
 
         $this->assertInstanceOf(User::class, $entity);
     }
-}
\ No newline at end of file
+}

      ----------- end diff -----------

  30) tests/Post/UpdateUserEmailUseCaseTest.php
      ---------- begin diff ----------
--- /home/runner/work/MabelPy/MabelPy/tests/Post/UpdateUserEmailUseCaseTest.php
+++ /home/runner/work/MabelPy/MabelPy/tests/Post/UpdateUserEmailUseCaseTest.php
@@ -4,9 +4,9 @@
 
 namespace App\Tests;
 
-use PHPUnit\Framework\TestCase;
 use App\Domain\Repository\PostRepository;
 use App\Domain\UseCase\Post\UpdateUserEmail\UpdateUserEmailUseCase;
+use PHPUnit\Framework\TestCase;
 
 final class UpdateUserEmailUseCaseTest extends TestCase
 {
@@ -14,7 +14,7 @@
     {
         $repository = $this->createMock(PostRepository::class);
         $useCase = new UpdateUserEmailUseCase($repository);
-        
+
         $this->assertInstanceOf(UpdateUserEmailUseCase::class, $useCase);
     }
-}
\ No newline at end of file
+}

      ----------- end diff -----------

  31) tests/Post/PostTest.php
      ---------- begin diff ----------
--- /home/runner/work/MabelPy/MabelPy/tests/Post/PostTest.php
+++ /home/runner/work/MabelPy/MabelPy/tests/Post/PostTest.php
@@ -4,10 +4,9 @@
 
 namespace App\Tests;
 
+use App\Domain\Post;
 use PHPUnit\Framework\TestCase;
-use App\Domain\Post;
 
-
 final class PostTest extends TestCase
 {
     public function test_can_be_instantiated(): void
@@ -21,4 +20,4 @@
 
         $this->assertInstanceOf(Post::class, $entity);
     }
-}
\ No newline at end of file
+}

      ----------- end diff -----------

  32) tests/Post/DeactivateUserUseCaseTest.php
      ---------- begin diff ----------
--- /home/runner/work/MabelPy/MabelPy/tests/Post/DeactivateUserUseCaseTest.php
+++ /home/runner/work/MabelPy/MabelPy/tests/Post/DeactivateUserUseCaseTest.php
@@ -4,9 +4,9 @@
 
 namespace App\Tests;
 
-use PHPUnit\Framework\TestCase;
 use App\Domain\Repository\PostRepository;
 use App\Domain\UseCase\Post\DeactivateUser\DeactivateUserUseCase;
+use PHPUnit\Framework\TestCase;
 
 final class DeactivateUserUseCaseTest extends TestCase
 {
@@ -14,7 +14,7 @@
     {
         $repository = $this->createMock(PostRepository::class);
         $useCase = new DeactivateUserUseCase($repository);
-        
+
         $this->assertInstanceOf(DeactivateUserUseCase::class, $useCase);
     }
-}
\ No newline at end of file
+}

      ----------- end diff -----------

  33) tests/Post/CreateUserUseCaseTest.php
      ---------- begin diff ----------
--- /home/runner/work/MabelPy/MabelPy/tests/Post/CreateUserUseCaseTest.php
+++ /home/runner/work/MabelPy/MabelPy/tests/Post/CreateUserUseCaseTest.php
@@ -4,9 +4,9 @@
 
 namespace App\Tests;
 
-use PHPUnit\Framework\TestCase;
 use App\Domain\Repository\PostRepository;
 use App\Domain\UseCase\Post\CreateUser\CreateUserUseCase;
+use PHPUnit\Framework\TestCase;
 
 final class CreateUserUseCaseTest extends TestCase
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


Found 34 of 40 files that can be fixed in 0.155 seconds, 18.00 MB memory used
Error: Process completed with exit code 12.