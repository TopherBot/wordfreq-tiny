import pathlib
import subprocess
import sys


def run_cli(tmp_path: pathlib.Path, content: str) -> str:
    file_path = tmp_path / "sample.txt"
    file_path.write_text(content, encoding="utf-8")
    result = subprocess.run(
        [sys.executable, "-m", "wordfreq", str(file_path)],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def test_basic_counts(tmp_path):
    out = run_cli(tmp_path, "Hello world! Hello again.")
    lines = out.splitlines()
    # Expected order: hello (2), world (1), again (1)
    assert lines[0] == "hello: 2"
    assert "world: 1" in lines[1]
    assert "again: 1" in lines[2]
