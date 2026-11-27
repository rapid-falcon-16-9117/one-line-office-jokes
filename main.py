"""One-Line Office Jokes entry: writes the final line to entry.txt."""
import os

LINE = "Out-of-office reply: 'I'm on leave until Monday.' Sent at 11:47 p.m. on a Sunday, from my desk, to my own inbox."

def main():
    # Gate self-check: UTF-8 text, 1-199 chars, single line.
    assert 1 <= len(LINE) <= 199, f"length {len(LINE)} outside 1-199"
    assert "\n" not in LINE and "\r" not in LINE, "must be a single line"
    assert LINE.strip(), "must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Round-trip self-check: the file must read back byte-identical,
    # valid UTF-8, with no trailing newline or extra whitespace.
    with open(path, "rb") as f:
        raw = f.read()
    assert raw.decode("utf-8") == LINE, "round-trip mismatch"
    assert raw == LINE.encode("utf-8"), "file bytes differ from LINE"
    assert not raw.endswith(b"\n"), "no trailing newline allowed"
    print(f"wrote {len(LINE)} chars to {path}")

if __name__ == "__main__":
    main()
