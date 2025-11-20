# CachyOS One-Shot Program Installer

<p align="center">
	<img src="assets/logo.png" alt="Gillsystems logo" width="800">
</p>

**Version:** 1.0.0  
**Status:** Active Development  
**Target System:** CachyOS Linux (Arch-based)

## 🎯 Overview

The **CachyOS One-Shot Program Installer** is a power-user tool designed to streamline the process of setting up a new CachyOS system. It provides a unified interface to search, select, and batch-install applications from multiple sources:

- **Pacman** (Official Repositories)
- **AUR** (Arch User Repository)
- **Flatpak** (Coming Soon)
- **Snap** (Coming Soon)

## 🚀 Features

- **Unified Search:** Query Pacman and AUR simultaneously.
- **Batch Installation:** Build a queue and install everything in one go.
- **System Monitoring:** Real-time disk and RAM usage tracking.
- **Sudo Integration:** Handles privileges securely for seamless installation.
- **Version Awareness:** See package versions before installing.

## 🛠️ Installation & Usage

### Prerequisites
- CachyOS (or Arch Linux)
- Python 3.x
- `paru` or `yay` (for AUR support)

### Quick Start

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/OCNGill/CachyOS-One-Shot-Program-Installer.git
    cd CachyOS-One-Shot-Program-Installer
    ```

2.  **Run the launcher:**
    ```bash
    chmod +x launch.sh
    ./launch.sh
    ```

    The launcher will:
    - Check for dependencies.
    - Create a virtual environment (optional).
    - Install Python requirements.
    - Request sudo privileges.
    - Launch the Streamlit interface in your browser.

## 📂 Project Structure

```
CachyOS-One-Shot-Program-Installer/
├── app.py                  # Main Streamlit Application
├── launch.sh               # Launcher Script
├── requirements.txt        # Python Dependencies
├── wrappers/               # Package Manager Integrations
│   ├── pacman_wrapper.py
│   ├── aur_wrapper.py
│   └── unified_search.py
├── manager/                # Logic Layer
│   └── package_manager.py
├── utils/                  # Utilities
│   ├── system_monitor.py
│   └── auth_helper.py
└── assets/                 # Images & Resources
```

## 🤝 Contributing

This project follows the **7D Agile Development Framework**.
Please refer to `Project_Definition.md` and `Requirements.md` for details.

## 💖 Support / Donate

If you find this project helpful, you can support ongoing work — thank you!

<p align="center">
	<img src="assets/qr-paypal.png" alt="PayPal QR code" width="180" style="margin:8px;">
	<img src="assets/qr-venmo.png" alt="Venmo QR code" width="180" style="margin:8px;">
</p>


**Donate:**

- [![PayPal](https://img.shields.io/badge/PayPal-Donate-009cde?logo=paypal&logoColor=white)](https://paypal.me/gillsystems) https://paypal.me/gillsystems
- [![Venmo](https://img.shields.io/badge/Venmo-Donate-3d95ce?logo=venmo&logoColor=white)](https://venmo.com/Stephen-Gill-007) https://venmo.com/Stephen-Gill-007

---

<p align="center">
	<a href="https://paypal.me/gillsystems"><img src="assets/paypal_icon.png" alt="PayPal" width="32" style="vertical-align:middle;"></a>
	<a href="https://venmo.com/Stephen-Gill-007"><img src="assets/venmo_icon.png" alt="Venmo" width="32" style="vertical-align:middle;"></a>
</p>

## 📄 License

Private Project - Gillsystems
