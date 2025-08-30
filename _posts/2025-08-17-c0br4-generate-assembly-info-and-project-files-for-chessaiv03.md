---
layout: post
title: "C0BR4: Generate assembly info and project files for ChessAI_v0.3"
date: 2025-08-17 00:00:00 
author: Pat Snyder
categories: chess-engine development
tags: [c0br4, milestone, development]
repo: c0br4
commit: a3bdb048
excerpt: "Development milestone in c0br4: Generate assembly info and project files for ChessAI_v0.3"
---

# C0BR4: Generate assembly info and project files for ChessAI_v0.3

**Repository:** [c0br4](https://github.com/pssnyder/c0br4)
**Commit:** [`a3bdb048`](https://github.com/pssnyder/c0br4/commit/a3bdb0486bd53f89ad6e67889b6f402e8d02751a)
**Date:** 2025-08-17

## Overview

Generate assembly info and project files for ChessAI_v0.3

## Changes

```
 CHECKLIST.md                                       |  38 +-
 README.md                                          |  40 +-
 backups/dist_backup_20250817_172447/README.md      |  59 +++
 .../v0.0/ChessEngine.deps.json                     |  23 +
 .../v0.0/ChessEngine.runtimeconfig.json            |  12 +
 .../v0.1/ChessEngine.deps.json                     |  23 +
 .../v0.1/ChessEngine.runtimeconfig.json            |  12 +
 .../v0.2/ChessEngine.deps.json                     |  23 +
 .../v0.2/ChessEngine.runtimeconfig.json            |  12 +
 .../v0.3/ChessAI_v0.3.deps.json                    |  23 +
 .../v0.3/ChessAI_v0.3.runtimeconfig.json           |  12 +
 backups/dist_backup_20250817_172447/v0.3/VERSION   |   1 +
 .../src_backup_20250817_172446/ChessEngine.csproj  |  31 ++
 .../ChessEngine/Core/Board.cs                      | 357 +++++++++++++++
 .../ChessEngine/Core/BoardHelper.cs                |  25 ++
 .../ChessEngine/Core/Move.cs                       | 127 ++++++
 .../ChessEngine/Core/MoveGenerator.cs              | 479 +++++++++++++++++++++
 .../ChessEngine/Core/Piece.cs                      |  54 +++
 .../ChessEngine/Core/PieceType.cs                  |  13 +
 .../ChessEngine/Core/Square.cs                     |  64 +++
 .../ChessEngine/Evaluation/SimpleEvaluator.cs      | 247 +++++++++++
 .../ChessEngine/Search/AlphaBetaSearchBot.cs       | 129 ++++++
 .../ChessEngine/Search/IChessBot.cs                |   9 +
 .../ChessEngine/Search/RandomBot.cs                |  21 +
 .../ChessEngine/Search/SimpleSearchBot.cs          | 119 +++++
 .../ChessEngine/Testing/PerformanceBenchmark.cs    | 124 ++++++
 .../ChessEngine/UCI/UCIEngine.cs                   | 329 ++++++++++++++
 backups/src_backup_20250817_172446/Program.cs      |  16 +
 backups/src_backup_20250817_172446/VERSION         |   1 +
 .../bin/Debug/net6.0/ChessAI_v0.3.deps.json        |  23 +
 .../bin/Debug/net6.0/ChessAI_v0.3.pdb              | Bin 0 -> 26068 bytes
 .../Debug/net6.0/ChessAI_v0.3.runtimeconfig.json   |   9 +
 .../bin/Debug/net6.0/VERSION                       |   1 +
 .../bin/Release/net6.0/ChessAI_v0.3.deps.json      |  23 +
 .../Release/net6.0/ChessAI_v0.3.runtimeconfig.json |  12 +
 .../bin/Release/net6.0/VERSION                     |   1 +
 .../obj/ChessEngine.csproj.nuget.dgspec.json       |  84 ++++
 .../obj/ChessEngine.csproj.nuget.g.props           |  15 +
 .../obj/ChessEngine.csproj.nuget.g.targets         |   2 +
 .../.NETCoreApp,Version=v6.0.AssemblyAttributes.cs |   4 +
 .../obj/Debug/net6.0/ChessAI_v0.3.pdb              | Bin 0 -> 26068 bytes
 .../obj/Debug/net6.0/ChessEngine.AssemblyInfo.cs   |  22 +
 .../net6.0/ChessEngine.AssemblyInfoInputs.cache    |   1 +
 ...ngine.GeneratedMSBuildEditorConfig.editorconfig |  13 +
 .../obj/Debug/net6.0/ChessEngine.GlobalUsings.g.cs |   8 +
 .../obj/Debug/net6.0/ChessEngine.assets.cache      | Bin 0 -> 152 bytes
 .../ChessEngine.csproj.CoreCompileInputs.cache     |   1 +
 .../net6.0/ChessEngine.csproj.FileListAbsolute.txt |  16 +
 .../net6.0/ChessEngine.genruntimeconfig.cache      |   1 +
 .../obj/Debug/net6.0/ChessEngine.sourcelink.json   |   1 +
 .../.NETCoreApp,Version=v6.0.AssemblyAttributes.cs |   4 +
 .../obj/Release/net6.0/ChessEngine.AssemblyInfo.cs |  22 +
 .../net6.0/ChessEngine.AssemblyInfoInputs.cache    |   1 +
 ...ngine.GeneratedMSBuildEditorConfig.editorconfig |  13 +
 .../Release/net6.0/ChessEngine.GlobalUsings.g.cs   |   8 +
 .../obj/Release/net6.0/ChessEngine.assets.cache    | Bin 0 -> 152 bytes
 .../ChessEngine.csproj.CoreCompileInputs.cache     |   1 +
 .../net6.0/ChessEngine.csproj.FileListAbsolute.txt |  13 +
 .../net6.0/ChessEngine.genruntimeconfig.cache      |   1 +
 .../Release/net6.0/PublishOutputs.0744f8c7a5.txt   |   5 +
 .../Release/net6.0/PublishOutputs.5bfbc98c5c.txt   |   4 +
 .../Release/net6.0/PublishOutputs.8968d62112.txt   |   4 +
 .../Release/net6.0/PublishOutputs.bcb599e8c3.txt   |   4 +
 .../obj/project.assets.json                        |  89 ++++
 .../obj/project.nuget.cache                        |  13 +
 chess-challenge-source                             |   1 +
 opponent-bots                                      |   1 +
 src/ChessEngine.csproj                             |  27 ++
 src/ChessEngine/Core/Board.cs                      | 357 +++++++++++++++
 src/ChessEngine/Core/BoardHelper.cs                |  25 ++
 src/ChessEngine/Core/Move.cs                       | 127 ++++++
 src/ChessEngine/Core/MoveGenerator.cs              | 479 +++++++++++++++++++++
 src/ChessEngine/Core/Piece.cs                      |  54 +++
 src/ChessEngine/Core/PieceType.cs                  |  13 +
 src/ChessEngine/Core/Square.cs                     |  64 +++
 src/ChessEngine/Evaluation/SimpleEvaluator.cs      | 247 +++++++++++
 src/ChessEngine/Search/AlphaBetaSearchBot.cs       | 129 ++++++
 src/ChessEngine/Search/IChessBot.cs                |   9 +
 src/ChessEngine/Search/RandomBot.cs                |  21 +
 src/ChessEngine/Search/SimpleSearchBot.cs          | 119 +++++
 src/ChessEngine/Testing/PerformanceBenchmark.cs    | 124 ++++++
 src/ChessEngine/UCI/UCIEngine.cs                   | 329 ++++++++++++++
 src/Program.cs                                     |  16 +
 src/VERSION                                        |   1 +
 src/bin/Debug/net6.0/ChessAI_v0.3.deps.json        |  23 +
 src/bin/Debug/net6.0/ChessAI_v0.3.pdb              | Bin 0 -> 26068 bytes
 .../Debug/net6.0/ChessAI_v0.3.runtimeconfig.json   |   9 +
 src/bin/Debug/net6.0/VERSION                       |   1 +
 src/bin/Release/net6.0/ChessAI_v0.3.deps.json      |  23 +
 .../Release/net6.0/ChessAI_v0.3.runtimeconfig.json |  12 +
 src/bin/Release/net6.0/VERSION                     |   1 +
 src/obj/ChessEngine.csproj.nuget.dgspec.json       |  84 ++++
 src/obj/ChessEngine.csproj.nuget.g.props           |  15 +
 src/obj/ChessEngine.csproj.nuget.g.targets         |   2 +
 .../.NETCoreApp,Version=v6.0.AssemblyAttributes.cs |   4 +
 src/obj/Debug/net6.0/ChessAI_v0.3.pdb              | Bin 0 -> 26068 bytes
 src/obj/Debug/net6.0/ChessEngine.AssemblyInfo.cs   |  22 +
 .../net6.0/ChessEngine.AssemblyInfoInputs.cache    |   1 +
 ...ngine.GeneratedMSBuildEditorConfig.editorconfig |  13 +
 src/obj/Debug/net6.0/ChessEngine.GlobalUsings.g.cs |   8 +
 src/obj/Debug/net6.0/ChessEngine.assets.cache      | Bin 0 -> 152 bytes
 .../ChessEngine.csproj.CoreCompileInputs.cache     |   1 +
 .../net6.0/ChessEngine.csproj.FileListAbsolute.txt |  16 +
 .../net6.0/ChessEngine.genruntimeconfig.cache      |   1 +
 src/obj/Debug/net6.0/ChessEngine.sourcelink.json   |   1 +
 .../.NETCoreApp,Version=v6.0.AssemblyAttributes.cs |   4 +
 src/obj/Release/net6.0/ChessEngine.AssemblyInfo.cs |  22 +
 .../net6.0/ChessEngine.AssemblyInfoInputs.cache    |   1 +
 ...ngine.GeneratedMSBuildEditorConfig.editorconfig |  13 +
 .../Release/net6.0/ChessEngine.GlobalUsings.g.cs   |   8 +
 src/obj/Release/net6.0/ChessEngine.assets.cache    | Bin 0 -> 152 bytes
 .../ChessEngine.csproj.CoreCompileInputs.cache     |   1 +
 .../net6.0/ChessEngine.csproj.FileListAbsolute.txt |  13 +
 .../net6.0/ChessEngine.genruntimeconfig.cache      |   1 +
 .../Release/net6.0/PublishOutputs.0744f8c7a5.txt   |   5 +
 .../Release/net6.0/PublishOutputs.2bb1bdfc17.txt   |   5 +
 .../Release/net6.0/PublishOutputs.5457c26baf.txt   |   5 +
 .../Release/net6.0/PublishOutputs.5bfbc98c5c.txt   |   4 +
 .../Release/net6.0/PublishOutputs.8968d62112.txt   |   4 +
 .../Release/net6.0/PublishOutputs.bcb599e8c3.txt   |   4 +
 .../Release/net6.0/PublishOutputs.cdd3174532.txt   |   5 +
 src/obj/project.assets.json                        |  89 ++++
 src/obj/project.nuget.cache                        |  13 +
 123 files changed, 5389 insertions(+), 30 deletions(-)
```

## Files Modified

- `CHECKLIST.md`
- `README.md`
- `backups/dist_backup_20250817_172447/README.md`
- `backups/dist_backup_20250817_172447/v0.0/ChessEngine.deps.json`
- `backups/dist_backup_20250817_172447/v0.0/ChessEngine.runtimeconfig.json`
- `backups/dist_backup_20250817_172447/v0.1/ChessEngine.deps.json`
- `backups/dist_backup_20250817_172447/v0.1/ChessEngine.runtimeconfig.json`
- `backups/dist_backup_20250817_172447/v0.2/ChessEngine.deps.json`
- `backups/dist_backup_20250817_172447/v0.2/ChessEngine.runtimeconfig.json`
- `backups/dist_backup_20250817_172447/v0.3/ChessAI_v0.3.deps.json`
- ... and 113 more files

## Development Notes

This milestone represents a significant step in the evolution of the c0br4 chess engine. These changes contribute to the overall development and refinement of the engine.

## Next Steps

- Continue monitoring engine performance
- Test changes against benchmark positions
- Consider additional optimizations

---

*This entry was generated from commit analysis of the c0br4 repository.*
