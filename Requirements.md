# Requirements: CachyOS One-Shot Program Installer

**Version:** 1.0.0
**Status:** Approved

## 1. User Stories (US)

| ID | Story | Priority |
|----|-------|----------|
| **US-001** | As a power user, I want to search across Pacman, AUR, Flatpak, and Snap simultaneously so I don't have to check multiple tools. | High |
| **US-002** | As a user, I want to see up to 3 versions of each package so I can choose stable vs bleeding-edge. | High |
| **US-003** | As a user, I want to filter results by source (Pacman only, AUR only, etc.) to control where packages come from. | Medium |
| **US-004** | As a user, I want to see package sizes, dependencies, and descriptions before adding to my install queue. | Medium |
| **US-005** | As a user, I want to batch-install all selected packages with one click. | High |
| **US-006** | As a user, I want to monitor system resources (RAM, disk) during AUR compilation. | Medium |
| **US-007** | As a user, I want to export my selected packages as a script or profile for future use. | Low (v1.2) |
| **US-008** | As a user, I want the app to handle sudo authentication once at startup and cache credentials. | High |
| **US-009** | As a user, I want to see live terminal output during package installation. | Medium |
| **US-010** | As a user, I want to update my system (`pacman -Syu`) before installing new packages. | Low |

## 2. Functional Requirements (FR)

### Search & Discovery
- **FR-001:** System shall search Pacman and AUR (via yay/paru) based on user input. (Implements US-001)
- **FR-002:** System shall display up to 3 most recent versions for each package found. (Implements US-002)
- **FR-003:** System shall display package metadata: Name, Source, Version, Size, Description. (Implements US-004)
- **FR-004:** System shall allow filtering search results by source. (Implements US-003)
- **FR-005:** System shall support regex search patterns.

### Selection & Management
- **FR-007:** System shall maintain a queue of selected packages. (Implements US-005)
- **FR-008:** System shall allow version selection for queued packages. (Implements US-002)
- **FR-009:** System shall display total download/installed size for the queue. (Implements US-004)
- **FR-012:** System shall allow removing packages from the queue.

### Installation
- **FR-013:** System shall batch install selected packages sequentially. (Implements US-005)
- **FR-014:** System shall display installation progress and status. (Implements US-009)
- **FR-016:** System shall handle sudo authentication securely. (Implements US-008)

### Monitoring
- **FR-019:** System shall display real-time disk usage. (Implements US-006)
- **FR-020:** System shall display real-time RAM usage. (Implements US-006)

## 3. Technical Requirements (TR)

### Platform
- **TR-001:** Application shall be written in Python 3.x using the Streamlit framework.
- **TR-002:** Application shall be compatible with CachyOS Linux.
- **TR-003:** Application shall use `subprocess` for shell command execution.
- **TR-004:** Application shall auto-detect `paru` or `yay` for AUR interaction.

### Integration
- **TR-006:** Use `pacman -Ss` and `pacman -Si` for Pacman operations.
- **TR-007:** Use `yay -Ss`/`paru -Ss` for AUR operations.
- **TR-011:** Use `shutil.disk_usage()` for disk monitoring.
- **TR-012:** Use `psutil` for RAM/CPU monitoring.

### Security
- **TR-014:** Use `pkexec` or `sudo -v` for privilege escalation.
- **TR-015:** Cache credentials for the session duration.

### UI/UX
- **TR-017:** Interface shall be responsive and optimized for desktop.
- **TR-018:** Interface shall display Gillsystems branding.
- **TR-019:** Interface shall use color-coding for different package sources.
