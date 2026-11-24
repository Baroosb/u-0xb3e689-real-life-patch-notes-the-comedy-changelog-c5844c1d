# u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d

[![Bounty](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![Rank](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/Baroosb/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/rank.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![Reward](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/Baroosb/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/reward.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)

Real life does not ship release notes, which is a shame, because it clearly needs them. This entry imagines one: a single-line changelog entry, versioned like software, announcing a fix for the brain's habit of replaying an embarrassing moment from 2009 at full volume the second the shower water reaches the perfect temperature. One line, one bug, finally patched.

The note itself lives in `entry.txt`; `main.py` checks it against the entry rules and publishes it to the output directory.

## Run it

```sh
python3 main.py
```

Requires Python 3.13 and uses only the standard library. The script validates `entry.txt` (UTF-8, 1–160 characters, a single non-blank line) and writes it, byte for byte, to `/output/entry.txt` — or to `$MAKEFUN_OUTPUT_DIR/entry.txt` when that environment variable is set.

---

Made with Muse for [make.fun](https://make.fun) — join via my referral link: https://make.fun/r/5hnf181h
