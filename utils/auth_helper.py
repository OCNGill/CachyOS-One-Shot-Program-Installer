import subprocess
import shutil

def check_sudo_access():
    """
    Checks if the current user has sudo access (cached).
    Returns True if sudo is usable without password (cached), False otherwise.
    """
    try:
        # sudo -n -v checks credentials without prompting. 
        # If cached, returns 0. If not, returns 1.
        subprocess.run(["sudo", "-n", "-v"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False
    except FileNotFoundError:
        # sudo not found (e.g. on Windows dev env)
        return False

def get_aur_helper():
    """
    Detects available AUR helper (paru or yay).
    Returns 'paru', 'yay', or None.
    """
    if shutil.which("paru"):
        return "paru"
    elif shutil.which("yay"):
        return "yay"
    return None
