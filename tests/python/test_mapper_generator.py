import pytest
from core.generator.php_mapper_generator import PhpMapperGenerator
from core.config import MabelConfig
from pathlib import Path

@pytest.fixture
def config():
    return MabelConfig.from_file()

def test_mapper_generation_with_relationships(config, tmp_path):
    generator = PhpMapperGenerator(config)
    contract = {
        "entity": {"name": "Post"},
        "fields": [
            {"name": "id", "type": "int"},
            {"name": "title", "type": "string"},
            {"name": "author", "belongs_to": "User"},
            {"name": "comments", "has_many": "Comment"},
            {"name": "createdAt", "type": "datetime"}
        ]
    }
    
    # Generate
    generator.generate(contract, tmp_path)
    
    mapper_suffix = config.get_generator_config("mapper").get("namespace_suffix", "Infrastructure/Mapper")
    generated_file = tmp_path / mapper_suffix / "PostMapper.php"
    
    assert generated_file.exists()
    content = generated_file.read_text()
    
    # Check imports
    assert "use App\\Domain\\User;" in content
    assert "use App\\Domain\\Comment;" in content
    assert "use App\\Infrastructure\\Mapper\\UserMapper;" in content
    assert "use App\\Infrastructure\\Mapper\\CommentMapper;" in content
    
    # Check fromArray
    assert "UserMapper::fromArray($data['author'])" in content
    assert "array_map(fn(array $item) => CommentMapper::fromArray($item), $data['comments'] ?? [])" in content
    assert "new \\DateTimeImmutable($data['createdAt'])" in content
    
    # Check toArray
    assert "UserMapper::toArray($entity->author)" in content
    assert "array_map(fn(Comment $item) => CommentMapper::toArray($item), $entity->comments)" in content
    assert "$entity->createdAt->format(\\DateTimeInterface::ATOM)" in content
