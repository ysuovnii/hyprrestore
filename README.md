# 🌟 HyprRestore

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Hyprland](https://img.shields.io/badge/Hyprland-Ready-green.svg)
![License](https://img.shields.io/badge/License-MIT-lightgray.svg)

**HyprRestore** is a lightweight, Python-based utility for [Hyprland](https://hyprland.org/) designed to seamlessly save your current workspace state and restore your sessions (applications, windows, and workspaces) exactly as you left them upon your next login.

## ✨ Features

- **Session Saving**: Capture the state of your current workspaces.
- **Session Restoring**: Automatically re-launch applications.
- **Login Automation**: Easily integrate with `hyprland.conf` to restore your last session the moment you log in.

## 📂 Repository Structure

- `hyprrestore/` - Contains the core Python scripts and logic for interacting with `hyprctl`.
- `sessions/` - The directory where your workspace states and session data are safely stored.
- `README.md` - This documentation file.

## 🛠️ Prerequisites

Before using HyprRestore, ensure you have the following installed on your system:
- **[Hyprland](https://hyprland.org/)** (with `hyprctl` accessible in your PATH)
- **Python 3.x**

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/ysuovnii/HyprRestore.git](https://github.com/ysuovnii/HyprRestore.git)
   cd HyprRestore
