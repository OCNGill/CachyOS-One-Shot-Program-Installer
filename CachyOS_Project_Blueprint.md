# CachyOS One-Shot Program Installer - Complete Project Blueprint

**Repository Name**: `CachyOS_one_shot_program_installer`

**Target System**: Gillsystems-HTPC (Ryzen 5600G, Radeon 7600, CachyOS Linux)

---

## 🎯 Project Overview

A power-user focused, Streamlit-based web application for CachyOS/Arch Linux that aggregates multiple package sources (Pacman, AUR, Flatpak, Snap) into a single search-and-install interface. Unlike the Windows version built for beginners, this version targets advanced users who want:

- **Multi-source search** across all package repositories
- **Version selection** (show up to 3 most recent versions per package)
- **Batch installation** with dependency visualization
- **System monitoring** (disk, RAM, CPU during AUR builds)
- **Export/Import** of package lists for reproducibility
- **Advanced filtering** by source, architecture, and regex

---

## 📋 User Stories (US)

- **US-001**: As a power user, I want to search across Pacman, AUR, Flatpak, and Snap simultaneously so I don't have to check multiple tools.
- **US-002**: As a user, I want to see up to 3 versions of each package so I can choose stable vs bleeding-edge.
- **US-003**: As a user, I want to filter results by source (Pacman only, AUR only, etc.) to control where packages come from.
- **US-004**: As a user, I want to see package sizes, dependencies, and descriptions before adding to my install queue.
- **US-005**: As a user, I want to batch-install all selected packages with one click.
- **US-006**: As a user, I want to monitor system resources (RAM, disk) during AUR compilation.
- **US-007**: As a user, I want to export my selected packages as a script or profile for future use.
- **US-008**: As a user, I want the app to handle sudo authentication once at startup and cache credentials.
- **US-009**: As a user, I want to see live terminal output during package installation.
- **US-010**: As a user, I want to update my system (`pacman -Syu`) before installing new packages (optional toggle).

---

## 🔧 Functional Requirements (FR)

### Search & Discovery
- **FR-001**: Search across Pacman, AUR (via yay/paru), Flatpak, and Snap repositories.
- **FR-002**: Display up to 3 most recent versions for each package.
- **FR-003**: Show package metadata: Name, Source, Version(s), Size, Description, Dependencies.
- **FR-004**: Allow filtering by source (checkboxes: Pacman, AUR, Flatpak, Snap).
- **FR-005**: Support regex search patterns for advanced queries.
- **FR-006**: Smart retry logic (e.g., if "7 zip" fails, try "7zip").

### Selection & Management
- **FR-007**: Maintain a queue of selected packages with chosen versions.
- **FR-008**: Allow users to select which version to install (from 3 available).
- **FR-009**: Display total download size and installed size for queue.
- **FR-010**: Show dependency tree for selected packages.
- **FR-011**: Warn if dependencies conflict or if disk space is insufficient.
- **FR-012**: Allow removing packages from queue or clearing all.

### Installation
- **FR-013**: Batch install all selected packages sequentially.
- **FR-014**: Display live terminal output during installation.
- **FR-015**: Show progress bar for multi-package installs.
- **FR-016**: Handle sudo authentication via `pkexec` or cached credentials.
- **FR-017**: Support pre-install system update (`pacman -Syu`) as optional toggle.
- **FR-018**: Clean package cache after installation (optional toggle).

### Monitoring & Feedback
- **FR-019**: Display real-time disk usage (free/total).
- **FR-020**: Display real-time RAM usage (important for AUR builds).
- **FR-021**: Show CPU usage during AUR compilation.
- **FR-022**: Group packages in sidebar by source (Pacman, AUR, Flatpak).
- **FR-023**: Visual feedback on success/failure per package.
- **FR-024**: Celebration effects (balloons) on successful completion.

### Export & Profiles
- **FR-025**: Export selected packages as a bash script for reproducibility.
- **FR-026**: Export selected packages as JSON/YAML profile.
- **FR-027**: Import previously saved profiles.
- **FR-028**: Pre-defined profiles: "Gaming Setup", "Dev Stack", etc. (optional).

---

## ⚙️ Technical Requirements (TR)

### Platform & Dependencies
- **TR-001**: Written in Python 3.x using Streamlit framework.
- **TR-002**: Compatible with CachyOS Linux (Arch-based).
- **TR-003**: Use `subprocess` to execute shell commands (pacman, yay, flatpak, etc.).
- **TR-004**: Detect and use available AUR helper (prefer `paru`, fallback to `yay`).
- **TR-005**: Launcher script (`launch.sh`) checks for Python, Streamlit, and AUR helper.

### Package Manager Integration
- **TR-006**: Use `pacman -Ss` for Pacman search, `pacman -Si` for package info.
- **TR-007**: Use `yay -Ss` or `paru -Ss` for AUR search.
- **TR-008**: Use `flatpak search` for Flatpak packages.
- **TR-009**: Use `snap find` for Snap packages (optional).
- **TR-010**: Parse version information from each source's output format.

### System Monitoring
- **TR-011**: Use `shutil.disk_usage()` for disk monitoring.
- **TR-012**: Use `psutil` library for RAM and CPU monitoring.
- **TR-013**: Update metrics in real-time during AUR compilation.

### Authentication & Security
- **TR-014**: Use `pkexec` or prompt for sudo password once at startup.
- **TR-015**: Cache sudo credentials for session duration (use `sudo -v` keepalive).
- **TR-016**: Handle errors gracefully if sudo fails or times out.

### UI & UX
- **TR-017**: Modern, responsive Streamlit interface optimized for desktop.
- **TR-018**: Display branding (Gillsystems logo) in sidebar.
- **TR-019**: Use color-coding for sources (blue=Pacman, purple=AUR, green=Flatpak, orange=Snap).
- **TR-020**: Live terminal output in collapsible/scrollable section.

---

## 🏗️ Architecture & Design

### Component Structure

```
CachyOS_one_shot_program_installer/
├── app.py                          # Main Streamlit application
├── wrappers/
│   ├── __init__.py
│   ├── pacman_wrapper.py           # Pacman integration
│   ├── aur_wrapper.py              # AUR (yay/paru) integration
│   ├── flatpak_wrapper.py          # Flatpak integration
│   ├── snap_wrapper.py             # Snap integration (optional)
│   └── unified_search.py           # Combines all sources, deduplicates
├── manager/
│   ├── __init__.py
│   ├── package_manager.py          # Queue management with versions
│   └── dependency_resolver.py      # Parse dependency trees
├── utils/
│   ├── __init__.py
│   ├── system_monitor.py           # Disk, RAM, CPU monitoring
│   ├── auth_helper.py              # Sudo credential management
│   └── profile_manager.py          # Export/import profiles
├── launch.sh                       # Shell launcher script
├── requirements.txt                # Python dependencies
├── Design.md                       # Architecture documentation
├── Requirements.md                 # Functional/technical requirements
├── Project_Definition.md           # Project overview
├── README.md                       # User-facing documentation
└── assets/
    └── Gillsystems_logo_*.png      # Branding assets
```

---

## 🔄 Data Flow

1. **User launches** `launch.sh`
   - Script checks for Python 3, Streamlit, AUR helper
   - Prompts for sudo password once, caches credentials
   - Launches Streamlit app in browser

2. **User searches** for a package
   - `app.py` sends query to `unified_search.py`
   - `unified_search` queries all enabled sources in parallel
   - Results aggregated, deduplicated, sorted by relevance

3. **Results displayed** in grid
   - Each row shows: Name, Source (color-coded), Version dropdown (3 options), Size, Dependencies, "Add" button
   - User selects version from dropdown, clicks "Add"

4. **Package added to sidebar queue**
   - Sidebar shows: Logo, Disk usage, RAM usage, grouped package list by source
   - Running totals for download size, installed size
   - Warnings if low disk/RAM

5. **User clicks "INSTALL ALL"**
   - App iterates through queue, groups by source
   - Executes in order: Pacman packages → AUR packages → Flatpak → Snap
   - Live terminal output shown in main area
   - Progress bar updates per package
   - System monitor updates RAM/CPU during AUR builds

6. **Completion**
   - Success/failure summary
   - Balloons animation
   - Option to export installed list as profile

---

## 📦 Package Data Structure

Each package in the queue is a dict:

```python
{
    'Name': 'firefox',
    'Id': 'firefox',  # Unique identifier
    'Source': 'Pacman',  # or 'AUR', 'Flatpak', 'Snap'
    'SelectedVersion': '121.0.1-1',
    'AvailableVersions': ['121.0.1-1', '121.0-1', '120.0.1-1'],
    'Size': '250 MB',
    'InstalledSize': '280 MB',
    'Description': 'Fast, private & safe web browser',
    'Dependencies': ['gtk3', 'dbus', 'ffmpeg'],
    'Repository': 'extra'  # For Pacman packages
}
```

---

## 🎨 UI Layout

### **Sidebar** (Left, ~25% width)
```
┌─────────────────────────┐
│  [Gillsystems Logo]     │
├─────────────────────────┤
│  📦 Selected Packages   │
│  ━━━━━━━━━━━━━━━━━━━━━│
│  💾 Disk: 450 GB free   │
│  🧠 RAM: 12.5 GB free   │
│  🔥 CPU: 15% usage      │
├─────────────────────────┤
│  Pacman (3)             │
│    firefox  [v121.0.1]  │
│    vlc      [v3.0.20]   │
│    htop     [v3.3.0]    │
│  ━━━━━━━━━━━━━━━━━━━━━│
│  AUR (1)                │
│    spotify  [v1.2.28]   │
│  ━━━━━━━━━━━━━━━━━━━━━│
│  Total: 4 packages      │
│  Download: 450 MB       │
│  Installed: 520 MB      │
├─────────────────────────┤
│  [🗑️ Clear All]         │
│  [⚙️ Options ▼]         │
│     □ Update system     │
│     □ Clean cache       │
│  [🚀 INSTALL ALL]       │
└─────────────────────────┘
```

### **Main Area** (Right, ~75% width)

**Top Section**:
```
┌─────────────────────────────────────────────────┐
│  CachyOS One-Shot Installer 🐧                  │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━│
│  [Search: ________________] [🔍 Search]         │
│                                                  │
│  Sources: ☑ Pacman  ☑ AUR  ☑ Flatpak  ☐ Snap  │
│  Mode: ○ Normal  ● Regex                        │
└─────────────────────────────────────────────────┘
```

**Results Grid**:
```
┌────────────────────────────────────────────────────────────────┐
│  Name        Source    Version ▼         Size    Action       │
├────────────────────────────────────────────────────────────────┤
│  Firefox     Pacman    [121.0.1] ▼      250 MB   [➕ Add]      │
│  Firefox     Flatpak   [121.0.0] ▼      180 MB   [➕ Add]      │
│  VLC         Pacman    [3.0.20]  ▼       80 MB   [✅ Added]    │
└────────────────────────────────────────────────────────────────┘
```

**Installation View** (replaces results when installing):
```
┌────────────────────────────────────────────────────────────────┐
│  🚀 Installation in Progress...                                │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━│
│  [████████████████████░░░░░░░░] 75% (3/4 packages)            │
│                                                                 │
│  Current: Building spotify from AUR...                         │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━│
│  Terminal Output:                                              │
│  ┌────────────────────────────────────────────────────────┐   │
│  │ ==> Making package: spotify 1.2.28-1                   │   │
│  │ ==> Checking runtime dependencies...                   │   │
│  │ ==> Checking buildtime dependencies...                 │   │
│  │ ==> Retrieving sources...                              │   │
│  │   -> Downloading spotify-1.2.28.tar.gz...              │   │
│  └────────────────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────────────┘
```

---

## 🚀 Implementation Plan

### Phase 1: Core Foundation (v1.0 - First Build)
**Goal**: Get it working with Pacman + AUR, basic UI

✅ **Include**:
- Pacman wrapper (`pacman_wrapper.py`)
- AUR wrapper (`aur_wrapper.py`) - detect yay/paru
- Unified search (`unified_search.py`) - combine results
- Basic package manager (`package_manager.py`) - queue with versions
- Streamlit UI with search, results grid, sidebar
- Version dropdown (3 versions)
- Disk monitoring (`shutil`)
- Batch install with progress bar
- Sudo authentication helper (`auth_helper.py`)
- Launcher script (`launch.sh`)
- Smart retry logic (from Windows version)
- Gillsystems branding

❌ **Defer to v1.1+**:
- Flatpak/Snap integration (add later, architecture supports it)
- Dependency visualization (complex, needs graphing)
- RAM/CPU monitoring (nice-to-have, not critical)
- Live terminal output (tricky with Streamlit, use logging first)
- Export/import profiles (easy to add later)
- Pre-defined profiles (content-dependent)

### Phase 2: Enhanced Features (v1.1)
- Add Flatpak wrapper
- Add RAM/CPU monitoring with `psutil`
- Live terminal output in expander

### Phase 3: Advanced Features (v1.2)
- Snap wrapper
- Dependency tree visualization
- Export/import profiles
- Pre-defined profiles

### Phase 4: Power User Polish (v2.0)
- Update checker (show outdated packages)
- Package comparison mode
- Favorites/bookmarks
- Theme customization

---

## 🔑 Key Learnings from Windows Project to Apply

1. **Smart Search Retry**: Implement space-removal retry for failed searches
2. **Clean UI**: Use structured grids with buttons, not raw text dumps
3. **Sidebar Organization**: Group related info (system stats, package queue, actions)
4. **Error Handling**: Graceful degradation if a source is unavailable
5. **Visual Feedback**: Progress bars, toasts, balloons for engagement
6. **Branding**: Logo at top of sidebar, donation links in README
7. **One-Click Launch**: Shell script handles all dependencies
8. **Documentation**: Comprehensive README with screenshots/gifs
9. **Version Control**: Tag releases, follow semantic versioning
10. **7D Agile Process**: Define → Design → Develop → Debug → Document → Deliver → Deploy

---

## 🛠️ Technical Implementation Notes

### Pacman Wrapper
```python
# Search: pacman -Ss <query>
# Info: pacman -Si <package>
# Versions: Parse output, typically only shows latest in official repos
# Install: sudo pacman -S --noconfirm <package>
```

### AUR Wrapper
```python
# Detect helper: which paru || which yay
# Search: yay -Ss <query>
# Info: yay -Si <package>
# Versions: AUR typically has latest + git versions
# Install: yay -S --noconfirm <package>
```

### Flatpak Wrapper
```python
# Search: flatpak search <query>
# Info: flatpak info <app-id>
# Versions: flatpak remote-info --log <app-id>
# Install: flatpak install -y <app-id>
```

### Sudo Authentication
```python
# Option 1: pkexec (graphical password prompt)
# Option 2: Get password once with getpass, use sudo -S
# Option 3: Prompt at startup, keepalive with `sudo -v` in background thread
```

### Version Parsing
```python
# Pacman: "firefox 121.0.1-1"
# AUR: "spotify 1.2.28-1" or "spotify-git r5678.abc123-1"
# Flatpak: "org.mozilla.firefox 121.0"
# Parse with regex, normalize to semantic versioning
```

---

## 📝 Success Criteria

**v1.0 is ready when**:
1. User can search Pacman + AUR simultaneously
2. Results show 3 versions with dropdown selection
3. User can add packages to queue
4. Sidebar shows disk usage and queue grouped by source
5. "Install All" button executes all packages
6. Progress bar updates during installation
7. Success/failure feedback shown
8. Launcher script works on fresh CachyOS install
9. README is comprehensive with branding
10. No crashes on common operations

---

## 🎯 Post-Launch Enhancements (Ideas for v2.0+)

- **Update Notifier**: Show which installed packages have updates
- **Rollback**: Integrate with `timeshift` or `snapper` for pre-install snapshots
- **Benchmarking**: Show AUR build times for similar hardware
- **Community Ratings**: Integrate AUR vote counts
- **Changelog Viewer**: Display package changelogs before install
- **Multi-language**: i18n support for UI
- **Dark/Light Theme**: Toggle in settings
- **Keyboard Shortcuts**: Power user navigation

---

## 🚦 When You Feed This to Me

**Say**: "I've created the repository `CachyOS-One-Shot-Program-Installer`. Follow this blueprint and start with Phase 1 (v1.0). Use the 7D Agile process. Create the project structure, implement core wrappers, and build the Streamlit UI. Remember: Gillsystems-HTPC, CachyOS, Ryzen 5600G, Radeon 7600. Let's make it fast and powerful."

**I will**:
1. Create project structure
2. Write `launch.sh`
3. Implement `pacman_wrapper.py` and `aur_wrapper.py`
4. Build `unified_search.py`
5. Create `package_manager.py` with version support
6. Design Streamlit UI (`app.py`)
7. Add `auth_helper.py` for sudo
8. Integrate Gillsystems branding
9. Write comprehensive README
10. Test and iterate

---

**Ready to rock?** 🚀
