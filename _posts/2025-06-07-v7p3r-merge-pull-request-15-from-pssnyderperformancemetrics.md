---
layout: post
title: "V7P3R: Merge pull request #15 from pssnyder/performance_metrics"
date: 2025-06-07 00:00:00 
author: Pat Snyder
categories: chess-engine development
tags: [v7p3r, milestone, development]
repo: v7p3r
commit: 05da571b
excerpt: "Development milestone in v7p3r: Merge pull request #15 from pssnyder/performance_metrics"
---

# V7P3R: Merge pull request #15 from pssnyder/performance_metrics

**Repository:** [v7p3r](https://github.com/pssnyder/v7p3r)
**Commit:** [`05da571b`](https://github.com/pssnyder/v7p3r/commit/05da571b6767577c23ef59cee983f216a85c0046)
**Date:** 2025-06-07

## Overview

Merge pull request #15 from pssnyder/performance_metrics

## Changes

```
 .gitignore                                         |    Bin 485 -> 913 bytes
 .vscode/settings.json                              |      3 +
 README copy.md                                     |    169 -
 __pycache__/evaluation_engine.cpython-312.pyc      |    Bin 66185 -> 76048 bytes
 __pycache__/piece_square_tables.cpython-312.pyc    |    Bin 8470 -> 8437 bytes
 __pycache__/time_manager.cpython-312.pyc           |    Bin 6848 -> 6815 bytes
 chess_game.py                                      |   1721 +-
 config.yaml                                        |    308 +-
 .../__pycache__/opening_book.cpython-312.pyc       |    Bin 16148 -> 0 bytes
 .../piece_square_tables.cpython-312.pyc            |    Bin 8454 -> 0 bytes
 .../__pycache__/puzzle_manager.cpython-312.pyc     |    Bin 19623 -> 0 bytes
 .../__pycache__/time_manager.cpython-312.pyc       |    Bin 6832 -> 0 bytes
 engine_utilities/export_eval_games.py              |     64 +-
 engine_utilities/opening_book.py                   |    608 +-
 engine_utilities/piece_square_tables.py            |    410 +-
 engine_utilities/puzzle_manager.py                 |    342 -
 engine_utilities/puzzle_testing.py                 |     72 -
 engine_utilities/time_manager.py                   |    422 +-
 evaluation_engine.py                               |   2821 +-
 export_eval_games.py                               |     33 -
 games/active_game.pgn                              |     25 +-
 games/chess_ai_thoughts_20250601_145524.log        |   1073 -
 games/chess_ai_thoughts_20250601_145724.log        |   1073 -
 games/eval_game_20250606_011904.yaml               |    155 +
 games/eval_game_20250606_011911.yaml               |    155 +
 games/eval_game_20250606_011932.yaml               |    155 +
 games/eval_game_20250606_011958.yaml               |    155 +
 games/eval_game_20250606_012044.yaml               |    155 +
 games/eval_game_20250606_012104.yaml               |    155 +
 games/eval_game_20250606_012111.yaml               |    155 +
 games/eval_game_20250606_012117.yaml               |    155 +
 games/eval_game_20250606_012138.yaml               |    155 +
 games/eval_game_20250606_012152.yaml               |    155 +
 games/eval_game_20250606_013147.yaml               |    155 +
 games/eval_game_20250606_013343.yaml               |    155 +
 games/eval_game_20250606_013427.yaml               |    155 +
 games/eval_game_20250606_013822.yaml               |    155 +
 games/eval_game_20250606_013849.yaml               |    155 +
 games/eval_game_20250606_013945.yaml               |    155 +
 games/eval_game_20250606_014019.yaml               |    155 +
 games/eval_game_20250606_014032.yaml               |    155 +
 games/eval_game_20250606_014125.yaml               |    155 +
 games/eval_game_20250606_014236.yaml               |    155 +
 games/eval_game_20250606_015215.yaml               |    155 +
 games/eval_game_20250606_015929.yaml               |    155 +
 games/eval_game_20250606_020321.yaml               |    155 +
 games/eval_game_20250606_020457.yaml               |    155 +
 games/eval_game_20250606_020941.yaml               |    155 +
 games/eval_game_20250606_021220.yaml               |    155 +
 games/eval_game_20250606_021531.yaml               |    155 +
 games/eval_game_20250606_021805.yaml               |    155 +
 games/eval_game_20250606_022237.yaml               |    155 +
 games/eval_game_20250606_022516.yaml               |    155 +
 games/eval_game_20250606_031245.yaml               |    155 +
 games/eval_game_20250606_031639.yaml               |    155 +
 games/eval_game_20250606_032022.yaml               |    155 +
 games/eval_game_20250606_032615.yaml               |    155 +
 games/eval_game_20250606_033150.yaml               |    155 +
 games/eval_game_20250606_033812.yaml               |    155 +
 games/eval_game_20250606_034111.yaml               |    155 +
 games/eval_game_20250606_034528.yaml               |    155 +
 games/eval_game_20250606_035444.yaml               |    155 +
 games/eval_game_20250606_035812.yaml               |    155 +
 games/eval_game_20250606_211902.log                | 172789 +++++++++++++
 games/eval_game_20250606_211902.pgn                |     19 +
 games/eval_game_20250606_211902.yaml               |    134 +
 games/eval_game_20250606_211906.log                | 182306 ++++++++++++++
 games/eval_game_20250606_211906.pgn                |     19 +
 games/eval_game_20250606_211906.yaml               |    134 +
 games/eval_game_20250606_211911.log                | 191823 +++++++++++++++
 games/eval_game_20250606_211911.pgn                |     19 +
 games/eval_game_20250606_211911.yaml               |    134 +
 games/eval_game_20250606_211915.log                | 201340 +++++++++++++++
 games/eval_game_20250606_211915.pgn                |     19 +
 games/eval_game_20250606_211915.yaml               |    134 +
 games/eval_game_20250606_211920.log                | 210857 ++++++++++++++++
 games/eval_game_20250606_211920.pgn                |     19 +
 games/eval_game_20250606_211920.yaml               |    134 +
 games/eval_game_20250606_211924.log                | 168531 +++++++++++++
 games/eval_game_20250606_211924.pgn                |     19 +
 games/eval_game_20250606_211924.yaml               |    134 +
 games/eval_game_20250606_211929.log                | 178048 ++++++++++++++
 games/eval_game_20250606_211929.pgn                |     19 +
 games/eval_game_20250606_211929.yaml               |    134 +
 games/eval_game_20250606_211933.log                | 187565 ++++++++++++++
 games/eval_game_20250606_211933.pgn                |     19 +
 games/eval_game_20250606_211933.yaml               |    134 +
 games/eval_game_20250606_211938.log                | 197082 +++++++++++++++
 games/eval_game_20250606_211938.pgn                |     19 +
 games/eval_game_20250606_211938.yaml               |    134 +
 games/eval_game_20250606_211942.log                | 206599 ++++++++++++++++
 games/eval_game_20250606_211942.pgn                |     19 +
 games/eval_game_20250606_211942.yaml               |    134 +
 games/eval_game_20250606_212209.log                | 216116 ++++++++++++++++
 games/eval_game_20250606_212209.pgn                |     19 +
 games/eval_game_20250606_212209.yaml               |    134 +
 games/eval_game_20250606_212213.log                | 225633 +++++++++++++++++
 games/eval_game_20250606_212213.pgn                |     19 +
 games/eval_game_20250606_212213.yaml               |    134 +
 games/eval_game_20250606_212218.log                | 184646 ++++++++++++++
 games/eval_game_20250606_212218.pgn                |     19 +
 games/eval_game_20250606_212218.yaml               |    134 +
 games/eval_game_20250606_212226.log                | 194163 +++++++++++++++
 games/eval_game_20250606_212226.pgn                |     19 +
 games/eval_game_20250606_212226.yaml               |    134 +
 games/eval_game_20250606_212230.log                | 203680 +++++++++++++++
 games/eval_game_20250606_212230.pgn                |     19 +
 games/eval_game_20250606_212230.yaml               |    134 +
 games/eval_game_20250606_212234.log                | 213197 ++++++++++++++++
 games/eval_game_20250606_212234.pgn                |     19 +
 games/eval_game_20250606_212234.yaml               |    134 +
 games/eval_game_20250606_212239.log                | 222714 +++++++++++++++++
 games/eval_game_20250606_212239.pgn                |     19 +
 games/eval_game_20250606_212239.yaml               |    134 +
 games/eval_game_20250606_212243.log                | 232231 ++++++++++++++++++
 games/eval_game_20250606_212243.pgn                |     19 +
 games/eval_game_20250606_212243.yaml               |    134 +
 games/eval_game_20250606_212248.log                | 189912 ++++++++++++++
 games/eval_game_20250606_212248.pgn                |     19 +
 games/eval_game_20250606_212248.yaml               |    134 +
 games/eval_game_20250606_212252.log                | 199429 +++++++++++++++
 games/eval_game_20250606_212252.pgn                |     19 +
 games/eval_game_20250606_212252.yaml               |    134 +
 games/eval_game_20250606_212253.log                | 199429 +++++++++++++++
 games/eval_game_20250606_212253.pgn                |     19 +
 games/eval_game_20250606_212253.yaml               |    134 +
 games/export_all_eval_games_20250606_210841.pgn    |   3483 +
 lichess_bot.py                                     |    391 -
 metrics/metrics_dashboard.py                       |    802 +-
 metrics/static_metrics.csv                         |     26 +-
 metrics_dashboard.py                               |    340 -
 opening_book.py                                    |    304 -
 piece_square_tables.py                             |    206 -
 puzzle_manager.py                                  |    301 -
 puzzle_testing.py                                  |     72 -
 requirements.txt                                   |      4 +-
 streamlit_app.py                                   |    114 -
 testing-scenarios.md                               |    317 -
 testing/evaluation_manager.py                      |    590 +-
 testing/puzzle_testing.py                          |     72 -
 testing/raw_data_examples.txt                      |    328 +-
 testing/testing-scenarios.md                       |    632 +-
 time_manager.py                                    |    211 -
 web_applications/engine_metrics_app.py             |    352 +-
 web_applications/evaluation_engine_app.py          |    226 +-
 web_applications/lichess_bot.py                    |    788 +-
 146 files changed, 4196081 insertions(+), 10125 deletions(-)
```

## Development Notes

This milestone represents a significant step in the evolution of the v7p3r chess engine. These optimizations should improve engine performance and playing strength.

## Next Steps

- Continue monitoring engine performance
- Test changes against benchmark positions
- Consider additional optimizations

---

*This entry was generated from commit analysis of the v7p3r repository.*
