---
layout: post
title: "ENGINE-TESTER: new v7p3r v7.0 engine"
date: 2025-08-23 00:00:00 
author: Pat Snyder
categories: chess-engine development
tags: [engine-tester, milestone, development]
repo: engine-tester
commit: 5bb90adc
excerpt: "Development milestone in engine-tester: new v7p3r v7.0 engine"
---

# ENGINE-TESTER: new v7p3r v7.0 engine

**Repository:** [engine-tester](https://github.com/pssnyder/engine-tester)
**Commit:** [`5bb90adc`](https://github.com/pssnyder/engine-tester/commit/5bb90adc56f02be56e38ff91ab4026b8aef47265)
**Date:** 2025-08-23

## Overview

new v7p3r v7.0 engine

## Changes

```
 ELO_SYSTEM_SUMMARY.md                              |   139 -
 GUI_PROGRESS_UPDATE.md                             |   135 -
 RATING_UPDATE_SUMMARY.md                           |    93 -
 README_PROD.md                                     |    49 -
 development/DEV_README.md                          |    42 -
 development/documentation/DASHBOARD_README.md      |    97 -
 development/documentation/GUI_PROGRESS_UPDATE.md   |   135 -
 development/documentation/INTEGRATION_PLAN.md      |   143 -
 development/documentation/PROGRESS_STATUS.md       |   157 -
 development/legacy_analyzers/analyze_cece_v2.py    |   151 -
 development/legacy_analyzers/basic_analyzer.py     |   119 -
 .../legacy_analyzers/behavioral_analyzer.py        |   475 -
 .../legacy_analyzers/comprehensive_reporter.py     |   453 -
 .../convert_unified_to_dashboard.py                |   116 -
 development/legacy_analyzers/dashboard_complex.py  |  1129 -
 .../legacy_analyzers/data_quality_checker.py       |   419 -
 development/legacy_analyzers/enhanced_analyzer.py  |   301 -
 .../legacy_analyzers/enhanced_metadata_analyzer.py |   707 -
 .../enhanced_tournament_analyzer.py                |   629 -
 .../enhanced_tournament_analyzer_simple.py         |   626 -
 .../legacy_analyzers/focused_engine_analyzer.py    |   585 -
 development/legacy_analyzers/generate_dashboard.py |   679 -
 .../legacy_analyzers/generate_dashboard_final.py   |   898 -
 .../legacy_analyzers/generate_dashboard_fixed.py   |   707 -
 .../generate_dashboard_timing_openings_fix.py      |   850 -
 .../legacy_analyzers/generate_decision_diagram.py  |   250 -
 .../legacy_analyzers/landscape_visualizer.py       |   400 -
 development/legacy_analyzers/rapid_analyzer.py     |   188 -
 development/legacy_analyzers/run_full_analytics.py |   100 -
 development/legacy_analyzers/test_pgn.py           |    26 -
 development/legacy_analyzers/visualize_results.py  |   233 -
 development/legacy_code/chess_testing_gui.py       |   829 -
 development/legacy_code/engine_tester.py           |   378 -
 development/legacy_code/tournament_analyzer.py     |   519 -
 .../legacy_code/unified_tournament_analyzer.py     |   795 -
 .../testing_and_debugging/core_search_test.py      |   215 -
 .../testing_and_debugging/deep_search_test.py      |   215 -
 .../testing_and_debugging/performance_analysis.py  |   190 -
 .../performance_goals_test.py                      |   375 -
 .../performance_test_suite.py                      |   324 -
 .../quick_performance_test.py                      |   123 -
 .../robust_performance_test.py                     |   327 -
 .../testing_and_debugging/test_chess_core.py       |    55 -
 .../testing_and_debugging/test_engine_discovery.py |    61 -
 ...chess_test_20250816_102217_20250816_102258.json |    59 -
 ...0250816_102217_20250816_102258_performance.json |    33 -
 .../testing_and_debugging/test_session_logger.py   |   328 -
 development/utility_scripts/check_rankings.py      |    56 -
 .../utility_scripts/extract_godot_opponents.py     |   159 -
 .../utility_scripts/generate_enhanced_analysis.bat |    36 -
 engines/V7P3R/V7P3R_v7.0.exe                       |     3 +
 launch_dashboards.py                               |   111 -
 man_vs_machine_scoreboard/MvM_README.md            |   132 -
 .../analyzers/mvm_analyzer.py                      |   622 -
 .../dashboard/data/mvm_analysis.json               | 61879 -------------------
 .../dashboard/mvm_dashboard.py                     |   571 -
 man_vs_machine_scoreboard/launch_mvm_dashboard.py  |    72 -
 man_vs_machine_scoreboard/requirements.txt         |    30 -
 .../SlowMate Tournament 20250720.at                |   101 -
 .../SlowMate Tournament 20250720.html              |     1 -
 .../SlowMate Tournament 20250720.log               |  5877 --
 .../SlowMate Tournament 20250720.pgn               | 21226 -------
 .../SlowMate Tournament 20250720.res               |    64 -
 .../SlowMate Tournament 20250720.txt               |    19 -
 .../SlowMate Tournament 20250720_1104.pgn          |  3212 -
 .../SlowMate Tournament 20250721.at                |   108 -
 .../SlowMate Tournament 20250721.pgn               | 12474 ----
 .../SlowMate Tournament 20250722 2323.at           |   107 -
 .../SlowMate Tournament 20250722 2323.html         |     1 -
 .../SlowMate Tournament 20250722 2323.log          |   261 -
 .../SlowMate Tournament 20250722 2323.pgn          |   849 -
 .../SlowMate Tournament 20250722 2323.res          |    57 -
 .../SlowMate Tournament 20250722 2323.txt          |    24 -
 .../SlowMate Tournament 20250722.at                |    82 -
 .../SlowMate Tournament 20250722.html              |     1 -
 .../SlowMate Tournament 20250722.log               |   717 -
 .../SlowMate Tournament 20250722.pgn               |  2266 -
 .../SlowMate Tournament 20250722.res               |    16 -
 .../SlowMate Tournament 20250722.txt               |    15 -
 .../Engine Battle 20250728.at                      |   106 -
 .../Engine Battle 20250728.html                    |     1 -
 .../Engine Battle 20250728.log                     |  1305 -
 .../Engine Battle 20250728.pgn                     |  4847 --
 .../Engine Battle 20250728.res                     |    57 -
 .../Engine Battle 20250728.txt                     |    20 -
 .../Engine Battle 20250803.at                      |    84 -
 .../Engine Battle 20250803.html                    |     1 -
 .../Engine Battle 20250803.log                     |   465 -
 .../Engine Battle 20250803.pgn                     |    98 -
 .../Engine Battle 20250803.res                     |     9 -
 .../Engine Battle 20250803.txt                     |    14 -
 .../Engine Battle 20250806.at                      |    80 -
 .../Engine Battle 20250806.pgn                     |  1915 -
 .../Engine Battle 20250807.at                      |    82 -
 .../Engine Battle 20250807.html                    |     1 -
 .../Engine Battle 20250807.log                     |   741 -
 .../Engine Battle 20250807.pgn                     |  3057 -
 .../Engine Battle 20250807.res                     |    16 -
 .../Engine Battle 20250807.txt                     |    15 -
 .../Engine Battle 20250808.at                      |   325 -
 .../Engine Battle 20250808.html                    |     1 -
 .../Engine Battle 20250808.log                     | 10725 ----
 .../Engine Battle 20250808.pgn                     | 36032 -----------
 .../Engine Battle 20250808.res                     |   484 -
 .../Engine Battle 20250808.txt                     |    33 -
 .../tournament_analysis_20250808.json              | 10484 ----
 .../tournament_analysis_20250808.md                |   264 -
 .../Engine Battle 20250809.at                      |   126 -
 .../Engine Battle 20250809.html                    |     1 -
 .../Engine Battle 20250809.log                     |  3847 --
 .../Engine Battle 20250809.pgn                     | 11761 ----
 .../Engine Battle 20250809.res                     |    81 -
 .../Engine Battle 20250809.txt                     |    20 -
 ...tournament_analysis_Engine_Battle_20250809.json |  2453 -
 .../tournament_analysis_Engine_Battle_20250809.md  |   133 -
 .../Engine Battle 20250810.at                      |   100 -
 .../Engine Battle 20250810.html                    |     1 -
 .../Engine Battle 20250810.log                     |  2517 -
 .../Engine Battle 20250810.pgn                     |  6693 --
 .../Engine Battle 20250810.res                     |    49 -
 .../Engine Battle 20250810.txt                     |    18 -
 .../Engine Battle 20250810_2.at                    |   107 -
 .../Engine Battle 20250810_2.html                  |     1 -
 .../Engine Battle 20250810_2.log                   |  2997 -
 .../Engine Battle 20250810_2.pgn                   |  6889 ---
 .../Engine Battle 20250810_2.res                   |    49 -
 .../Engine Battle 20250810_2.txt                   |    18 -
 .../Engine Battle 20250811.at                      |   138 -
 .../Engine Battle 20250811.html                    |     1 -
 .../Engine Battle 20250811.log                     | 11277 ----
 .../Engine Battle 20250811.pgn                     | 30728 ---------
 .../Engine Battle 20250811.res                     |   121 -
 .../Engine Battle 20250811.txt                     |    22 -
 .../Engine Battle 20250811_2.at                    |    89 -
 .../Engine Battle 20250811_2.html                  |     1 -
 .../Engine Battle 20250811_2.log                   |  1929 -
 .../Engine Battle 20250811_2.pgn                   |  4438 --
 .../Engine Battle 20250811_2.res                   |    25 -
 .../Engine Battle 20250811_2.txt                   |    20 -
 .../Engine Battle Demo PC 20250811.at              |   372 -
 .../Engine Battle Demo PC 20250811.html            |     1 -
 .../Engine Battle Demo PC 20250811.log             |  9873 ---
 .../Engine Battle Demo PC 20250811.pgn             | 30843 ---------
 .../Engine Battle Demo PC 20250811.res             |   576 -
 .../Engine Battle Demo PC 20250811.txt             |    35 -
 .../Engine Battle 20250812.at                      |   117 -
 .../Engine Battle 20250812.html                    |     1 -
 .../Engine Battle 20250812.log                     |   861 -
 .../Engine Battle 20250812.pgn                     |  2232 -
 .../Engine Battle 20250812.res                     |    81 -
 .../Engine Battle 20250812.txt                     |    20 -
 .../Engine Battle 20250812_2.at                    |   100 -
 .../Engine Battle 20250812_2.html                  |     1 -
 .../Engine Battle 20250812_2.log                   |  2517 -
 .../Engine Battle 20250812_2.pgn                   |  6987 ---
 .../Engine Battle 20250812_2.res                   |    49 -
 .../Engine Battle 20250812_2.txt                   |    18 -
 .../Engine Battle 20250812_3.at                    |   100 -
 .../Engine Battle 20250812_3.html                  |     1 -
 .../Engine Battle 20250812_3.log                   |   513 -
 .../Engine Battle 20250812_3.pgn                   |  1384 -
 .../Engine Battle 20250812_3.res                   |    49 -
 .../Engine Battle 20250812_3.txt                   |    18 -
 .../Engine Battle Demo PC 20250812.at              |   208 -
 .../Engine Battle Demo PC 20250812.html            |     1 -
 .../Engine Battle Demo PC 20250812.log             |  2877 -
 .../Engine Battle Demo PC 20250812.pgn             |  8400 ---
 .../Engine Battle Demo PC 20250812.res             |   256 -
 .../Engine Battle Demo PC 20250812.txt             |    27 -
 .../Engine Battle Demo PC 20250812_2.at            |   139 -
 .../Engine Battle Demo PC 20250812_2.html          |     1 -
 .../Engine Battle Demo PC 20250812_2.log           |  7917 ---
 .../Engine Battle Demo PC 20250812_2.pgn           | 19784 ------
 .../Engine Battle Demo PC 20250812_2.res           |   122 -
 .../Engine Battle Demo PC 20250812_2.txt           |    23 -
 .../Engine Battle 20250813.at                      |   107 -
 .../Engine Battle 20250813.html                    |     1 -
 .../Engine Battle 20250813.log                     |  2865 -
 .../Engine Battle 20250813.pgn                     |  7408 ---
 .../Engine Battle 20250813.res                     |    49 -
 .../Engine Battle 20250813.txt                     |    18 -
 .../Engine Battle Demo PC 20250813.at              |   150 -
 .../Engine Battle Demo PC 20250813.html            |     1 -
 .../Engine Battle Demo PC 20250813.log             |  6849 --
 .../Engine Battle Demo PC 20250813.pgn             | 19107 ------
 .../Engine Battle Demo PC 20250813.res             |   144 -
 .../Engine Battle Demo PC 20250813.txt             |    23 -
 .../Engine Battle 20250814.at                      |   108 -
 .../Engine Battle 20250814.html                    |     1 -
 .../Engine Battle 20250814.log                     |  3357 -
 .../Engine Battle 20250814.pgn                     |  8255 ---
 .../Engine Battle 20250814.res                     |    64 -
 .../Engine Battle 20250814.txt                     |    19 -
 .../Engine Battle Demo PC 20250814.at              |   117 -
 .../Engine Battle Demo PC 20250814.html            |     1 -
 .../Engine Battle Demo PC 20250814.log             |  4317 --
 .../Engine Battle Demo PC 20250814.pgn             | 10618 ----
 .../Engine Battle Demo PC 20250814.res             |    81 -
 .../Engine Battle Demo PC 20250814.txt             |    20 -
 .../Engine Battle 20250815.at                      |   100 -
 .../Engine Battle 20250815.html                    |     1 -
 .../Engine Battle 20250815.log                     |  2517 -
 .../Engine Battle 20250815.pgn                     |  6273 --
 .../Engine Battle 20250815.res                     |    49 -
 .../Engine Battle 20250815.txt                     |    18 -
 .../Engine Battle Demo PC 20250815.at              |   177 -
 .../Engine Battle Demo PC 20250815.html            |     1 -
 .../Engine Battle Demo PC 20250815.log             | 17661 ------
 .../Engine Battle Demo PC 20250815.pgn             | 48533 ---------------
 .../Engine Battle Demo PC 20250815.res             |   196 -
 .../Engine Battle Demo PC 20250815.txt             |    25 -
 .../Engine Battle Mini PC 20250815.at              |    93 -
 .../Engine Battle Mini PC 20250815.html            |     1 -
 .../Engine Battle Mini PC 20250815.log             |  3597 --
 .../Engine Battle Mini PC 20250815.pgn             |  7648 ---
 .../Engine Battle Mini PC 20250815.res             |    36 -
 .../Engine Battle Mini PC 20250815.txt             |    17 -
 .../Engine Battle Mini PC 20250816.at              |   138 -
 .../Engine Battle Mini PC 20250816.html            |     1 -
 .../Engine Battle Mini PC 20250816.log             |  6465 --
 .../Engine Battle Mini PC 20250816.pgn             | 16282 -----
 .../Engine Battle Mini PC 20250816.res             |   121 -
 .../Engine Battle Mini PC 20250816.txt             |    22 -
 .../Engine Battle 20250817.at                      |   101 -
 .../Engine Battle 20250817.html                    |     1 -
 .../Engine Battle 20250817.log                     |  1329 -
 .../Engine Battle 20250817.pgn                     |  2946 -
 .../Engine Battle 20250817.res                     |    49 -
 .../Engine Battle 20250817.txt                     |    18 -
 .../Engine Battle 20250817_2.at                    |    82 -
 .../Engine Battle 20250817_2.html                  |     1 -
 .../Engine Battle 20250817_2.log                   |   717 -
 .../Engine Battle 20250817_2.pgn                   |  1641 -
 .../Engine Battle 20250817_2.res                   |    16 -
 .../Engine Battle 20250817_2.txt                   |    15 -
 .../Engine Battle 20250817_3.at                    |   100 -
 .../Engine Battle 20250817_3.html                  |     1 -
 .../Engine Battle 20250817_3.log                   |  2517 -
 .../Engine Battle 20250817_3.pgn                   |  5860 --
 .../Engine Battle 20250817_3.res                   |    49 -
 .../Engine Battle 20250817_3.txt                   |    18 -
 .../Engine Battle Demo PC 20250817.at              |   138 -
 .../Engine Battle Demo PC 20250817.log             |  5393 --
 .../Engine Battle Demo PC 20250817.pgn             | 14290 -----
 .../Engine Battle 20250818.at                      |    93 -
 .../Engine Battle 20250818.html                    |     1 -
 .../Engine Battle 20250818.log                     |  3597 --
 .../Engine Battle 20250818.pgn                     |  7916 ---
 .../Engine Battle 20250818.res                     |    36 -
 .../Engine Battle 20250818.txt                     |    17 -
 .../Engine Battle 20250818_2.at                    |    82 -
 .../Engine Battle 20250818_2.html                  |     1 -
 .../Engine Battle 20250818_2.log                   |  1437 -
 .../Engine Battle 20250818_2.pgn                   |  3159 -
 .../Engine Battle 20250818_2.res                   |    16 -
 .../Engine Battle 20250818_2.txt                   |    15 -
 .../Engine Battle Demo PC 20250818.at              |    82 -
 .../Engine Battle Demo PC 20250818.html            |     1 -
 .../Engine Battle Demo PC 20250818.log             |   222 -
 .../Engine Battle Demo PC 20250818.pgn             |   412 -
 .../Engine Battle Demo PC 20250818.res             |    17 -
 .../Engine Battle Demo PC 20250818.txt             |    24 -
 .../Engine Battle Demo PC 20250818_2.at            |   150 -
 .../Engine Battle Demo PC 20250818_2.html          |     1 -
 .../Engine Battle Demo PC 20250818_2.log           |  7929 ---
 .../Engine Battle Demo PC 20250818_2.pgn           | 17378 ------
 .../Engine Battle Demo PC 20250818_2.res           |   144 -
 .../Engine Battle Demo PC 20250818_2.txt           |    23 -
 .../Engine Battle Demo PC 20250819.at              |    87 -
 .../Engine Battle Demo PC 20250819.html            |     1 -
 .../Engine Battle Demo PC 20250819.log             |  1197 -
 .../Engine Battle Demo PC 20250819.pgn             |  2711 -
 .../Engine Battle Demo PC 20250819.res             |    25 -
 .../Engine Battle Demo PC 20250819.txt             |    16 -
 .../Engine Battle 20250820.at                      |    87 -
 .../Engine Battle 20250820.html                    |     1 -
 .../Engine Battle 20250820.log                     |  1197 -
 .../Engine Battle 20250820.pgn                     |  2519 -
 .../Engine Battle 20250820.res                     |    25 -
 .../Engine Battle 20250820.txt                     |    16 -
 .../Engine Battle 20250820_2.at                    |    78 -
 .../Engine Battle 20250820_2.html                  |     1 -
 .../Engine Battle 20250820_2.log                   |   249 -
 .../Engine Battle 20250820_2.pgn                   |   511 -
 .../Engine Battle 20250820_2.res                   |     8 -
 .../Engine Battle 20250820_2.txt                   |    15 -
 .../Engine Battle Demo PC 20250820.at              |    93 -
 .../Engine Battle Demo PC 20250820.html            |     1 -
 .../Engine Battle Demo PC 20250820.log             |  1797 -
 .../Engine Battle Demo PC 20250820.pgn             |  4176 --
 .../Engine Battle Demo PC 20250820.res             |    36 -
 .../Engine Battle Demo PC 20250820.txt             |    17 -
 .../Best of Engine Battle 20250821.at              |    82 -
 .../Best of Engine Battle 20250821.html            |     1 -
 .../Best of Engine Battle 20250821.log             |   717 -
 .../Best of Engine Battle 20250821.pgn             |  1553 -
 .../Best of Engine Battle 20250821.res             |    16 -
 .../Best of Engine Battle 20250821.txt             |    15 -
 .../Engine Battle 20250821.at                      |    87 -
 .../Engine Battle 20250821.html                    |     1 -
 .../Engine Battle 20250821.log                     |   777 -
 .../Engine Battle 20250821.pgn                     |  1982 -
 .../Engine Battle 20250821.res                     |    25 -
 .../Engine Battle 20250821.txt                     |    16 -
 .../Engine Battle 20250821_2.at                    |    82 -
 .../Engine Battle 20250821_2.html                  |     1 -
 .../Engine Battle 20250821_2.log                   |   717 -
 .../Engine Battle 20250821_2.pgn                   |  2410 -
 .../Engine Battle 20250821_2.res                   |    16 -
 .../Engine Battle 20250821_2.txt                   |    15 -
 .../Engine Battle 20250821_3.at                    |    78 -
 .../Engine Battle 20250821_3.html                  |     1 -
 .../Engine Battle 20250821_3.log                   |   357 -
 .../Engine Battle 20250821_3.pgn                   |   975 -
 .../Engine Battle 20250821_3.res                   |     9 -
 .../Engine Battle 20250821_3.txt                   |    14 -
 .../Engine Battle Demo PC 20250821.at              |    82 -
 .../Engine Battle Demo PC 20250821.html            |     1 -
 .../Engine Battle Demo PC 20250821.log             |  1437 -
 .../Engine Battle Demo PC 20250821.pgn             |  3084 -
 .../Engine Battle Demo PC 20250821.res             |    16 -
 .../Engine Battle Demo PC 20250821.txt             |    15 -
 .../Engine Battle Demo PC 20250821_2.at            |    82 -
 .../Engine Battle Demo PC 20250821_2.html          |     1 -
 .../Engine Battle Demo PC 20250821_2.log           |   717 -
 .../Engine Battle Demo PC 20250821_2.pgn           |  1668 -
 .../Engine Battle Demo PC 20250821_2.res           |    16 -
 .../Engine Battle Demo PC 20250821_2.txt           |    15 -
 .../Engine Battle Demo PC 20250821_3.at            |    87 -
 .../Engine Battle Demo PC 20250821_3.html          |     1 -
 .../Engine Battle Demo PC 20250821_3.log           |  1197 -
 .../Engine Battle Demo PC 20250821_3.pgn           |  2657 -
 .../Engine Battle Demo PC 20250821_3.res           |    25 -
 .../Engine Battle Demo PC 20250821_3.txt           |    16 -
 .../Best of Engine Battle 20250822.at              |   100 -
 .../Best of Engine Battle 20250822.html            |     1 -
 .../Best of Engine Battle 20250822.log             |  1377 -
 .../Best of Engine Battle 20250822.pgn             |  3746 --
 .../Best of Engine Battle 20250822.res             |    49 -
 .../Best of Engine Battle 20250822.txt             |    18 -
 .../Engine Battle 20250822_2.at                    |    95 -
 .../Engine Battle 20250822_2.html                  |     1 -
 .../Engine Battle 20250822_2.log                   |   297 -
 .../Engine Battle 20250822_2.pgn                   |   853 -
 .../Engine Battle 20250822_2.res                   |    39 -
 .../Engine Battle 20250822_2.txt                   |    18 -
 unified_tournament_analyzer.py                     |   795 -
 354 files changed, 3 insertions(+), 676423 deletions(-)
```

## Files Modified

- `ELO_SYSTEM_SUMMARY.md`
- `GUI_PROGRESS_UPDATE.md`
- `INTEGRATION_PLAN.md`
- `PROGRESS_STATUS.md`
- `RATING_UPDATE_SUMMARY.md`
- `README_PROD.md`
- `development/DEV_README.md`
- `development/README.md`
- `development/documentation/DASHBOARD_README.md`
- `development/documentation/GUI_PROGRESS_UPDATE.md`
- ... and 344 more files

## Development Notes

This milestone represents a significant step in the evolution of the engine-tester chess engine. These changes contribute to the overall development and refinement of the engine.

## Next Steps

- Continue monitoring engine performance
- Test changes against benchmark positions
- Consider additional optimizations

---

*This entry was generated from commit analysis of the engine-tester repository.*
