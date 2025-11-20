import subprocess

def search_aur(query, helper="paru"):
    """
    Searches AUR using the specified helper (paru or yay).
    Returns a list of dictionaries.
    """
    results = []
    try:
        # yay/paru -Ss output format is similar to pacman
        cmd = [helper, "-Ss", query]
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        
        if result.returncode != 0:
            return []

        lines = result.stdout.strip().split('\n')
        current_pkg = None

        for line in lines:
            if not line.startswith('    '):
                # Header line
                # aur/name version (+votes) [installed]
                parts = line.split(' ')
                repo_name = parts[0]
                version = parts[1]
                
                if '/' in repo_name:
                    repo, name = repo_name.split('/')
                else:
                    repo = "unknown"
                    name = repo_name

                # Filter only AUR packages (yay/paru search both)
                if repo != "aur":
                    continue

                current_pkg = {
                    "Name": name,
                    "Source": "AUR",
                    "Repository": repo,
                    "Version": version,
                    "Description": "",
                    "Installed": "[installed]" in line
                }
                results.append(current_pkg)
            else:
                # Description line
                if current_pkg:
                    current_pkg["Description"] = line.strip()

    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Error searching AUR: {e}")

    return results

def install_aur_cmd(packages, helper="paru"):
    """
    Returns the command to install a list of packages.
    """
    return [helper, "-S", "--noconfirm"] + packages
