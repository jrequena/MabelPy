<?php

declare(strict_types=1);

namespace App\Tests;

use PHPUnit\Framework\TestCase as BaseTestCase;

/**
 * Mock RefreshDatabase trait if it doesn't exist
 */
if (!trait_exists('Illuminate\Foundation\Testing\RefreshDatabase')) {
    trait RefreshDatabase {
        protected function setUpRefreshDatabase(): void {}
    }
}

/**
 * Mock Eloquent Model if it doesn't exist
 */
if (!class_exists('Illuminate\Database\Eloquent\Model')) {
    eval('namespace Illuminate\Database\Eloquent { 
        abstract class Model {
            public function __call($method, $args) { return $this; }
            public static function __callStatic($method, $args) { return new static; }
            public function toArray() { return []; }
            public function belongsTo($related) { return new class { public function __call($n, $a) { return $this; } }; }
        }
    }');
}

/**
 * Mock DB facade if it doesn't exist
 */
if (!class_exists('Illuminate\Support\Facades\DB')) {
    eval('namespace Illuminate\Support\Facades { 
        class DB {
            public static function transaction($callback) { return $callback(); }
            public static function __callStatic($method, $args) { return null; }
        }
    }');
}

/**
 * Mock ConnectionResolverInterface if it doesn't exist
 */
if (!interface_exists('Illuminate\Database\ConnectionResolverInterface')) {
    eval('namespace Illuminate\Database { 
        interface ConnectionResolverInterface {
            public function connection($name = null);
            public function getDefaultConnection();
            public function setDefaultConnection($name);
        }
    }');
}

/**
 * Mock ConnectionInterface if it doesn't exist
 */
if (!interface_exists('Illuminate\Database\ConnectionInterface')) {
    eval('namespace Illuminate\Database { 
        interface ConnectionInterface {
            public function table($table, $as = null);
            public function getName();
            public function query();
        }
    }');
}

/**
 * Mock Query Builder if it doesn't exist
 */
if (!class_exists('Illuminate\Database\Query\Builder')) {
    eval('namespace Illuminate\Database\Query { 
        class Builder {
            public function __construct($connection, $grammar = null, $processor = null) {}
            public function __call($m, $a) { return $this; }
        }
    }');
}

/**
 * Helper to create dummy implementations of interfaces
 */
if (!function_exists('App\Tests\createDummyInterface')) {
    function createDummyInterface($interface, $className) {
        if (!interface_exists($interface) || class_exists($className)) return;
        $rc = new \ReflectionClass($interface);
        $methods = '';
        foreach ($rc->getMethods() as $method) {
            $params = [];
            foreach ($method->getParameters() as $param) {
                $p = '';
                if ($param->hasType()) {
                    $type = $param->getType();
                    if ($type instanceof \ReflectionNamedType) {
                        $typeName = $type->getName();
                        if ($typeName !== 'mixed' && (PHP_VERSION_ID >= 80000 || $typeName !== 'static')) {
                            // Prefix with \ if it's a class/interface
                            if (!$type->isBuiltin()) {
                                $typeName = '\\' . ltrim($typeName, '\\');
                            }
                            $p .= ($type->allowsNull() ? '?' : '') . $typeName . ' ';
                        }
                    }
                }
                $p .= '$' . $param->getName();
                if ($param->isDefaultValueAvailable()) {
                    $p .= ' = ' . var_export($param->getDefaultValue(), true);
                } elseif ($param->isOptional()) {
                    $p .= ' = null';
                }
                $params[] = $p;
            }
            $returnType = '';
            $returnValue = '$this';
            if (PHP_VERSION_ID >= 70000 && $method->hasReturnType()) {
                $rType = $method->getReturnType();
                if ($rType instanceof \ReflectionNamedType) {
                    $rName = $rType->getName();
                    if ($rName === 'void') {
                        $returnValue = '';
                    } elseif ($rName === 'bool') {
                        $returnValue = 'true';
                    } elseif ($rName === 'array') {
                        $returnValue = '[]';
                    } elseif ($rName === 'int' || $rName === 'float') {
                        $returnValue = '0';
                    } elseif ($rName === 'string') {
                        $returnValue = "''";
                    } elseif (!$rType->isBuiltin() && $rName !== $rc->getName() && $rName !== 'static' && $rName !== 'self') {
                        $fullRName = '\\' . ltrim($rName, '\\');
                        $returnValue = "(\$this instanceof $fullRName ? \$this : \\App\\Tests\\createDummyInstance('$fullRName'))";
                    }

                    if ($rName !== 'mixed' && $rName !== 'static') {
                        if (!$rType->isBuiltin()) {
                            $rName = '\\' . ltrim($rName, '\\');
                        }
                        $returnType = ': ' . ($rType->allowsNull() ? '?' : '') . $rName;
                    }
                }
            }
            $methods .= "public function {$method->getName()}(" . implode(', ', $params) . ")$returnType { " . ($returnValue !== '' ? "return $returnValue;" : "") . " }\n";
        }
        $parts = explode('\\', $className);
        $shortName = array_pop($parts);
        $namespace = implode('\\', $parts);
        eval(($namespace ? "namespace $namespace; " : "") . "class $shortName implements \\$interface { $methods public function __call(" . '$m, $a' . ") { return null; } }");
    }

    function createDummyInstance($className) {
        static $instances = [];
        if (isset($instances[$className])) return $instances[$className];
        
        if (!class_exists($className) && !interface_exists($className)) {
            return null;
        }

        if (interface_exists($className)) {
            $mockName = 'App\\Tests\\Dummy' . str_replace('\\', '', $className);
            if (!class_exists($mockName)) {
                createDummyInterface($className, $mockName);
            }
            return $instances[$className] = new $mockName();
        }

        try {
            return $instances[$className] = new $className();
        } catch (\Throwable $e) {
            return null;
        }
    }
}

createDummyInterface('Illuminate\Database\ConnectionInterface', 'App\Tests\DummyConnection');
createDummyInterface('Illuminate\Database\ConnectionResolverInterface', 'App\Tests\DummyConnectionResolver');

abstract class TestCase extends BaseTestCase
{
    private static bool $initialized = false;

    protected function setUp(): void
    {
        parent::setUp();
        
        $this->initializeEnvironment();

        if (method_exists($this, 'setUpRefreshDatabase')) {
            $this->setUpRefreshDatabase();
        }
    }

    private function initializeEnvironment(): void
    {
        if (self::$initialized) {
            return;
        }

        if (class_exists('Illuminate\Support\Facades\Facade')) {
            if (!function_exists('app') || !(@\app() instanceof \Illuminate\Container\Container)) {
                $container = new \Illuminate\Container\Container();
                
                if (class_exists('App\Tests\DummyConnection')) {
                    $connMock = new \App\Tests\DummyConnection();
                } else {
                    $connMock = new class {
                        public function table($table, $as = null) { return $this; }
                        public function getName() { return 'default'; }
                        public function query() { return $this; }
                        public function __call($m, $a) { return $this; }
                    };
                }

                // Override some methods to have real-ish behavior
                $dbMock = new class($connMock) implements \Illuminate\Database\ConnectionResolverInterface {
                    private $conn;
                    public function __construct($conn) { $this->conn = $conn; }
                    public function transaction($callback) { return $callback(); }
                    public function connection($n = null) { return $this->conn; }
                    public function getDefaultConnection() { return 'default'; }
                    public function setDefaultConnection($name) {}
                    public function getName() { return 'default'; }
                    public function __call($m, $a) { 
                        if (method_exists($this->conn, $m) || method_exists($this->conn, '__call')) {
                            return $this->conn->$m(...$a);
                        }
                        return $this->conn;
                    }
                };

                // Ensure connMock->query() returns a Query Builder if possible
                if ($connMock instanceof \App\Tests\DummyConnection || method_exists($connMock, 'query')) {
                    // We can't easily override methods on an existing instance, but we can use a proxy or just rely on __call if we didn't implement query() in DummyConnection
                }
                
                // Let's refine connMock to return a Query Builder
                $connMock = new class($connMock) {
                    private $inner;
                    public function __construct($inner) { $this->inner = $inner; }
                    public function table($table, $as = null) { 
                        if (class_exists(\Illuminate\Database\Query\Builder::class)) {
                            return new \Illuminate\Database\Query\Builder($this);
                        }
                        return $this;
                    }
                    public function query() { 
                        if (class_exists(\Illuminate\Database\Query\Builder::class)) {
                            return new \Illuminate\Database\Query\Builder($this);
                        }
                        return $this;
                    }
                    public function __call($m, $a) { return $this->inner->$m(...$a); }
                    // To satisfy type hints
                    public function getName() { return 'default'; }
                };
                
                // Wait, if I use the anonymous class above, it won't implement ConnectionInterface.
                // I need to use the DummyConnection class if it exists.
                
                if (class_exists('App\Tests\DummyConnection')) {
                    eval('namespace App\Tests; class EnhancedConnection extends DummyConnection {
                        public function table($table, $as = null) { 
                            if (class_exists(\Illuminate\Database\Query\Builder::class)) {
                                return new \Illuminate\Database\Query\Builder($this);
                            }
                            return $this;
                        }
                        public function query() { 
                            if (class_exists(\Illuminate\Database\Query\Builder::class)) {
                                return new \Illuminate\Database\Query\Builder($this);
                            }
                            return $this;
                        }
                        public function getQueryGrammar() { return null; }
                        public function getPostProcessor() { return null; }
                    }');
                    $connMock = new \App\Tests\EnhancedConnection();
                }

                // Re-create dbMock with the correct connMock
                $dbMock = new class($connMock) implements \Illuminate\Database\ConnectionResolverInterface {
                    private $conn;
                    public function __construct($conn) { $this->conn = $conn; }
                    public function transaction($callback) { return $callback(); }
                    public function connection($n = null) { return $this->conn; }
                    public function getDefaultConnection() { return 'default'; }
                    public function setDefaultConnection($name) {}
                    public function getName() { return 'default'; }
                    public function __call($m, $a) { return $this->conn->$m(...$a); }
                };

                $container->singleton('db', fn() => $dbMock);
                $container->alias('db', 'db.factory');
                \Illuminate\Support\Facades\Facade::setFacadeApplication($container);
                
                if (class_exists('Illuminate\Database\Eloquent\Model')) {
                    \Illuminate\Database\Eloquent\Model::setConnectionResolver($dbMock);
                }
            }
        }
        
        self::$initialized = true;
    }

    protected function app(string $abstract)
    {
        $this->initializeEnvironment();

        if (function_exists('app')) {
            return \app($abstract);
        }
        
        try {
            $reflection = new \ReflectionClass($abstract);
            
            if ($reflection->isInterface()) {
                return $this->createMock($abstract);
            }

            $constructor = $reflection->getConstructor();
            
            if (null === $constructor) {
                return new $abstract();
            }
            
            $parameters = $constructor->getParameters();
            $dependencies = [];
            
            foreach ($parameters as $parameter) {
                if ($parameter->isDefaultValueAvailable()) {
                    $dependencies[] = $parameter->getDefaultValue();
                    continue;
                }

                $type = $parameter->getType();
                if ($type instanceof \ReflectionNamedType && !$type->isBuiltin()) {
                    $dependencies[] = $this->app($type->getName());
                } else {
                    $dependencies[] = ($type instanceof \ReflectionNamedType && $type->getName() === 'array') ? [] : null;
                }
            }
            
            return $reflection->newInstanceArgs($dependencies);
        } catch (\Throwable $e) {
            if (class_exists($abstract)) {
                $reflection = new \ReflectionClass($abstract);
                if (!$reflection->isFinal()) {
                    return $this->createMock($abstract);
                }
            }
            throw $e;
        }
    }
}
