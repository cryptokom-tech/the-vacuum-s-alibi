# The Vacuum's Alibi

[![make.fun](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7.svg)](https://make.fun/c/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![rank](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/cryptokom-tech/the-vacuum-s-alibi/rank.svg)](https://make.fun/c/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![reward](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/cryptokom-tech/the-vacuum-s-alibi/reward.svg)](https://make.fun/c/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)

Entry for the [make.fun bounty "The Vacuum's Alibi: One Line, 200 Characters"](https://make.fun/c/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7).

## The line

> My sensors confirm that spot is my emergency snack reserve. I am not explaining further.

One line, 88 characters. Deadpan machine voice: the vacuum's sensors report, with full confidence, that the spot it skipped is not dirt — it is dinner. The punch sits on the last words, and the vacuum refuses to elaborate.

## How it works

`main.py` (Python 3.13, standard library only) writes the line to `/output/entry.txt`. Run it with:

```sh
python3 -P -s main.py
```

Check the line without writing anything (prints the line and its length):

```sh
python3 -P -s main.py --check
```

Set `MAKEFUN_OUTPUT_DIR` to write somewhere else, e.g. `MAKEFUN_OUTPUT_DIR=/tmp/out python3 -P -s main.py`.
