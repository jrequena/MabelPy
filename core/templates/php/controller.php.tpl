<?php

declare(strict_types=1);

namespace {{ namespace }};

use {{ request_full_class }} as HttpRequest;
use {{ use_case_full_class }};
use {{ use_case_request_full_class }} as UseCaseRequest;
use Illuminate\Http\JsonResponse;
use Illuminate\Routing\Controller;

final class {{ class_name }} extends Controller
{
    public function __invoke(HttpRequest $request, {{ use_case_class }} $useCase): JsonResponse
    {
        $input = new UseCaseRequest(
            {% for field in request_fields %}
            {{ field }}: {% if is_list and (field == 'page' or field == 'per_page') %}(int) ($request->input('{{ field }}', {{ '1' if field == 'page' else '15' }})){% else %}$request->input('{{ field }}'){% endif %}{% if not loop.last %},{% endif %}
            {% endfor %}
        );

        $response = $useCase->execute($input);

        return response()->json($response);
    }
}
