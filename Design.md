# Design: CachyOS One-Shot Program Installer

**Version:** 1.0.0
**Status:** Draft

## 1. Architecture Overview

The application follows a modular architecture separating the UI (Streamlit), Logic (Manager), and Data Access (Wrappers).

```mermaid
graph TD
    User[User] --> UI[Streamlit UI (app.py)]
    UI --> PM[Package Manager]
    UI --> SM[System Monitor]
    UI --> US[Unified Search]
    
    US --> PW[Pacman Wrapper]
    US --> AW[AUR Wrapper]
    US --> FW[Flatpak Wrapper]
    
    PM --> PW
    PM --> AW
    PM --> FW
    
    PW --> SysPac[System Pacman]
    AW --> SysAur[System Yay/Paru]
    FW --> SysFlat[System Flatpak]
    
    SM --> OS[OS Resources]
```

### Components
1.  **app.py:** The presentation layer. Handles user input, displays results, and manages the session state.
2.  **wrappers/**:
    *   `pacman_wrapper.py`: Interface for `pacman` commands.
    *   `aur_wrapper.py`: Interface for `yay` or `paru`.
    *   `unified_search.py`: Orchestrates searches across all enabled wrappers and aggregates results.
3.  **manager/**:
    *   `package_manager.py`: Manages the list of selected packages, handles version selection logic, and orchestrates the installation process.
4.  **utils/**:
    *   `system_monitor.py`: Provides real-time system stats (Disk, RAM).
    *   `auth_helper.py`: Manages sudo authentication.

## 2. Data Flow

1.  **Initialization:** `launch.sh` checks env -> `app.py` loads -> `auth_helper` checks sudo -> `system_monitor` gets initial stats.
2.  **Search:** User types query -> `app.py` calls `unified_search.search(query)` -> Wrappers execute commands -> Results parsed -> Returned to UI.
3.  **Selection:** User clicks "Add" -> Package object added to `st.session_state['queue']`.
4.  **Installation:** User clicks "Install All" -> `package_manager.install_queue()` iterates queue -> Calls appropriate wrapper install method -> Updates UI progress.

## 3. Data Structures

### Package Object
```python
class Package:
    name: str
    id: str
    source: str  # 'Pacman', 'AUR', 'Flatpak'
    selected_version: str
    available_versions: List[str]
    size: str
    description: str
    dependencies: List[str]
    installed: bool
```

## 4. UI Layout

### Sidebar
- **Header:** Gillsystems Logo.
- **Stats:** Disk Free, RAM Free.
- **Queue:** List of selected packages grouped by source.
- **Actions:** "Clear All", "Install All".

### Main Area
- **Title:** CachyOS One-Shot Installer.
- **Search Bar:** Text input + "Search" button.
- **Filters:** Checkboxes for sources.
- **Results:** Data grid or list of cards showing found packages.
- **Terminal:** Expander showing command output during operations.

## 5. Security Design
- **Sudo:** The app requires root privileges for installation.
- **Mechanism:** We will use `sudo -v` to validate/refresh credentials at startup. If the session expires, the user may need to re-authenticate in the terminal launching the script, or we can use `pkexec` for a GUI prompt if available.
