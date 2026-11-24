# One Line, One Chill — "The Handwriting Changed"

An entry for make.fun's **One Line, One Chill** competition
("write the single scariest sentence you can, under 200 characters").

`main.py` (Python 3, standard library only) writes one fixed line of horror
to `/output/entry.txt`:

> The handwriting in my diary changed three weeks ago, and I have not missed a single day.

The scare is identity invasion: someone has been writing my life, in my own
hand, for three weeks — and I never noticed. The dread outlasts the line
because either reading lands: an impostor has been living as me, or my own
hand stopped being mine.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

In the grader's container `/output` is used directly (no variable needed).
The output is deterministic: the same 88 bytes on every run, no trailing
newline, 1 sentence, 1–200 characters.

## License

MIT — see `LICENSE`.
