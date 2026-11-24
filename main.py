#!/usr/bin/env python3
"""Write the one-sentence worst-app pitch to /output/entry.txt.

The pitch is VoicemailVault: an app that archives voicemails from numbers
you blocked, transcribes the sighs, and reads the best ones aloud each
Sunday at noon, so no rejected caller is ever truly forgotten by the phone
that rejected them. The competition gate (competition.yaml) is: the file
must hold UTF-8 text of 1 to 240 characters, not only whitespace, in one
sentence. This program checks the pitch against that gate before writing
it, then writes it with no trailing newline. No network, no input files,
no arguments, deterministic: two runs write byte-identical output.
"""

import pathlib

PITCH = (
    "VoicemailVault archives every voicemail from numbers you blocked, "
    "transcribes the sighs, then reads the best ones aloud each Sunday "
    "at noon, so no rejected caller is ever truly forgotten by the "
    "phone that rejected them."
)


def main() -> None:
    text = PITCH
    if not 1 <= len(text) <= 240:
        raise ValueError("pitch must be 1 to 240 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("pitch must not be only whitespace")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("pitch must be exactly one sentence")
    if "\n" in text or "\r" in text:
        raise ValueError("pitch must be exactly one line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("pitch must not contain control characters")
    if text != text.strip() or "  " in text:
        raise ValueError("pitch must not carry stray or doubled spaces")
    out = pathlib.Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    if out.read_bytes() != text.encode("utf-8"):
        raise ValueError("written pitch does not round-trip byte-identical")


if __name__ == "__main__":
    main()
