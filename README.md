# HyprRestore

![C++](https://img.shields.io/badge/C%2B%2B-17-blue.svg)
![Hyprland](https://img.shields.io/badge/Hyprland-Compatible-green.svg)
![Systemd](https://img.shields.io/badge/systemd-user--service-orange.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

**HyprRestore** is a lightweight session persistence tool for **Hyprland** that automatically saves and restores your workspace state, running applications, and window layout using a native **C++ backend** integrated with **systemd user services**.

---

## Overview

HyprRestore enables a persistent desktop experience on Hyprland by capturing active sessions and restoring them on login. It is designed to be minimal, fast, and tightly integrated with the Linux user session.

---

## Features

- Session snapshot capture (workspaces + applications)
- Automatic session restore on login
- Systemd user service integration
- Hyprland-native control via `hyprctl`
- Lightweight C++ implementation with minimal dependencies
- JSON-based snapshot storage

---

## Architecture

HyprRestore is composed of two core components:

- **Save Engine**
  - Periodically captures active Hyprland state
  - Stores data in structured JSON snapshots

- **Restore Engine**
  - Reads saved snapshot
  - Re-launches applications and reconstructs workspace layout

---

## Project Structure

```bash
hyprrestore/
├── src/
│   ├── save.cpp              # Session capture logic
│   ├── restore.cpp           # Session restoration logic
│
├── build/
│   ├── save                  # Compiled save binary
│   ├── restore               # Compiled restore binary
│
├── snapshots/
│   ├── snapshot.json         # Session data storage
│
├── systemd/
│   ├── hyprrestore-save.service
│   ├── hyprrestore-save.timer
│   ├── hyprrestore-restore.service
│
└── README.md
```
---

## Requirements

- Linux with Hyprland compositor
- C++17 or later
- systemd (user mode enabled)
- `hyprctl` available in PATH

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/ysuovnii/HyprRestore.git
cd HyprRestore
mkdir -p build
g++ src/save.cpp -o build/save
g++ src/restore.cpp -o build/restore
mkdir -p ~/.config/systemd/user
cp systemd/*.service ~/.config/systemd/user/
cp systemd/*.timer ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable hyprrestore-save.timer
systemctl --user enable hyprrestore-restore.service
systemctl --user start hyprrestore-save.service
systemctl --user start hyprrestore-restore.service
journalctl --user -u hyprrestore-save.service -f
journalctl --user -u hyprrestore-restore.service -f
```

---

## Known Issues
- Some applications may fail to launch if command mapping is incorrect (Flatpak vs native binaries)
- Certain window classes require manual mapping in restore logic

---

## Roadmap
- Flatpak + native app resolver
- Multi-monitor layout restoration
- Window geometry persistence
- Improved error handling and recovery system

---

## License

This project is licensed under the MIT License.