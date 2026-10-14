# 📡 Linux Core Core Control Modules (Toolbox & Computing Suite)

> A highly optimized, modular interactive CLI Control Panel for Linux core diagnostics, system automation, network analysis, and secure computing.

[![Python Version](https://shields.io)](https://python.org)
[![Platform](https://shields.io)](https://kernel.org)
[![DevOps Mode](https://shields.io)](https://github.com)
[![Maintainer](https://shields.io)](https://github.commraz0tix-code)

## 🩻 Infrastructure Overview

This repository hosts a monolithic, production-ready system automation toolkit designed for Junior Systems Infrastructure tasks. Instead of fragmented files, this codebase implements a multi-tier modular loop architecture, allowing seamless runtime hot-swapping between the **SysPulse Diagnostics Suite** and a protected cryptographic calculation engine.

## 🛠️ Monolith Architecture & Modules

The core architecture is split into high-speed functional domain blocks:

### 1. Unified Control Block (`Main_Menu`)
- Implements a low-latency execution routing tree state manager.
- Features automatic terminal buffer clearing via `os.system("clear || cls")` for responsive cross-platform GUI simulation.

### 2. Diagnostics Daemon Loop (`Run_Toolbox`)
- **Network Engine (`Internet`)**: Handles active ICMP echoes and network routing ping sweeps.
- **Kernel Auditor (`Kernel`)**: Direct sub-process interface with the OS kernel configurations (`uname -a`).
- **Port Inspector (`Network_ports`)**: Scans socket interfaces and active listening interfaces (`ss -tuln`).
- **Resource Monitors (`htop` / `Fastfetch`)**: Deep execution profiling via standard process diagnostic viewports.
- **Storage Sub-Module (`get_disk_progress_bar`)**: Algorithmic parser of `shutil.disk_usage` that renders dynamic ASCII storage load bars.

### 3. Compute Sandbox (`Calculator`)
- High-precision computing block executing variables through the `float` data architecture.
- Features a built-in **Zero-Downtime Kernel Firewall** (`if b == 0:`) which intercepts division anomalies and triggers a custom `0 / 0 == ERROR!` log without dropping the main application runtime thread loop.

## 💻 Tech Stack & Environment

- **Language:** Pure Python (3.10+)
- **Standard Library Hooks:** `subprocess` process forks, `os` bindings, `shutil` environment stats, `webbrowser` telemetry.
- **Optimized Terminal Target:** Arch Linux running natively within the `Kitty` terminal emulator environment.

## 🚀 Deployment Manual

1. **Pull the monolithic payload to your host machine:**
   ```bash
   git clone https://github.commraz0tix-code/SysPulse.git
   cd SysPulse
   ```

2. **Grant execution permissions to the system binary:**
   ```bash
   chmod +x fastsyspulse.py
   ```

3. **Deploy the runtime environment:**
   ```bash
   python fastsyspulse.py
   ```

## 📋 Code Specifications
- **Code Volume:** ~256 lines of refactored, clean, indentation-mapped code blocks.
- **Failure Domain Protection:** Complete failure isolation through nested `while True` recursive infinite loops with manual block `break` interrupt states.
