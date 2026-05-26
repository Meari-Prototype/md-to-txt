from pathlib import Path
import sys
import time


def read_text(path: Path) -> str:
    for encoding in ("utf-8-sig", "utf-8", "gb18030"):
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue
    return path.read_text(encoding="utf-8", errors="replace")


def available_output_path(path: Path) -> Path:
    output = path.with_suffix(".txt")
    if not output.exists():
        return output

    index = 2
    while True:
        candidate = path.with_name(f"{path.stem}_{index}.txt")
        if not candidate.exists():
            return candidate
        index += 1


def convert(path_text: str) -> tuple[bool, str]:
    path = Path(path_text)
    if not path.is_file():
        return False, f"SKIP not a file: {path}"
    if path.suffix.lower() != ".md":
        return False, f"SKIP not .md: {path}"

    output = available_output_path(path)
    output.write_text(read_text(path), encoding="utf-8", newline="")
    return True, f"OK {path.name} -> {output.name}"


def main() -> int:
    if len(sys.argv) < 2:
        print("Drag one or more .md files onto this script.")
        wait_before_exit()
        return 1

    ok_count = 0
    for item in sys.argv[1:]:
        ok, message = convert(item)
        if ok:
            ok_count += 1
        print(message)

    print(f"Done. Converted {ok_count} file(s).")
    wait_before_exit()
    return 0


def wait_before_exit() -> None:
    print("Window will close in 5 seconds...")
    time.sleep(5)


if __name__ == "__main__":
    raise SystemExit(main())
