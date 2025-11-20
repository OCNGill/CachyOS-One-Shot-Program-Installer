# Project Definition: CachyOS One-Shot Program Installer

**Version:** 1.0.0
**Status:** Active
**Last Updated:** 2025-11-20

## 1. Project Overview
The **CachyOS One-Shot Program Installer** is a power-user focused, Streamlit-based web application designed for the Gillsystems-HTPC (Ryzen 5600G, Radeon 7600) running CachyOS Linux. It aggregates multiple package sources (Pacman, AUR, Flatpak, Snap) into a single, unified search-and-install interface.

Unlike standard GUI package managers (like Pamac or Octopi), this tool is optimized for "one-shot" setup scenarios—allowing a user to rapidly select a large list of software from mixed sources, configure versions, and batch install them with full visibility into the process.

## 2. Objectives
- **Unify Search:** Provide a single search bar that queries Pacman, AUR, Flatpak, and Snap simultaneously.
- **Version Control:** Allow users to see and select specific versions (up to 3 most recent) where available.
- **Batch Efficiency:** Enable building a queue of mixed-source packages and installing them in the optimal order.
- **System Awareness:** Monitor system resources (Disk, RAM, CPU) to prevent failures during resource-intensive AUR compilations.
- **Reproducibility:** Allow exporting and importing package lists to replicate setups across machines.

## 3. Target Audience
- **Primary:** Advanced Linux users / Power users.
- **Specific:** The user of the Gillsystems-HTPC.
- **Needs:** Speed, transparency (terminal output), control (versions), and efficiency.

## 4. Success Criteria
- **v1.0 (MVP):**
    - [ ] Successful search across Pacman and AUR.
    - [ ] Ability to select from available versions.
    - [ ] Batch installation queue functionality.
    - [ ] Real-time disk usage monitoring.
    - [ ] "Install All" execution with progress feedback.
    - [ ] Stable execution on CachyOS.

## 5. Constraints & Assumptions
- **OS:** CachyOS (Arch-based).
- **Hardware:** Ryzen 5600G, Radeon 7600, sufficient RAM/Disk.
- **Dependencies:** Python 3.x, Streamlit, `pacman`, `yay` or `paru`.
- **Permissions:** Requires `sudo` access for installation.

## 6. Key Stakeholders
- **Project Owner:** Gillsystems
- **Developer:** AI Assistant (Antigravity)
