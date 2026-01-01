<?php

declare(strict_types=1);

namespace {{ namespace }};

/**
 * @template T
 */
final readonly class PaginatedResult
{
    /**
     * @param array<T> $items
     */
    public function __construct(
        public array $items,
        public int $total,
        public int $perPage,
        public int $currentPage,
        public int $lastPage
    ) {
    }

    public static function empty(): self
    {
        return new self([], 0, 15, 1, 1);
    }
}
