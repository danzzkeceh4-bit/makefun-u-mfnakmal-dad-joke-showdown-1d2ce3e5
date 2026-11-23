# Dad Joke Showdown

[![make.fun · u-mfnakmal-dad-joke-showdown-1d2ce3e5](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![rank](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/danzzkeceh4-bit/makefun-u-mfnakmal-dad-joke-showdown-1d2ce3e5/rank.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![reward](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/danzzkeceh4-bit/makefun-u-mfnakmal-dad-joke-showdown-1d2ce3e5/reward.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-dad-joke-showdown-1d2ce3e5)

Entry for the [make.fun bounty](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5) — a program that writes one dad joke to `/output/entry.txt`.

The joke:

> I changed the Wi-Fi password to 'DadIsRight' — now every time it drops, the kids have to type that I'm right just to get back online.

## How it works

`main.py` is deterministic and offline: it writes a single constant joke (133 characters, within the 1–200 limit) to `/output/entry.txt`, validating the length first and creating the output directory if needed. No trailing newline is added — the file is exactly the joke.

## Run

```bash
python3 main.py
cat /output/entry.txt
```

Set `MAKEFUN_OUTPUT_DIR` to write somewhere other than `/output`.
