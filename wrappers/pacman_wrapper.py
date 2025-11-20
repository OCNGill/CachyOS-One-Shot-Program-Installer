import subprocess
import re

def search_pacman(query):
    """
    Searches Pacman for packages matching the query.
    Returns a list of dictionaries.
    """
    results = []
    try:
        # pacman -Ss output format:
        # repo/name version (group) [installed]
        #     Description
        cmd = ["pacman", "-Ss", query]
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        
        if result.returncode != 0:
            return []

        lines = result.stdout.strip().split('\n')
        current_pkg = None

        for line in lines:
            if not line.startswith('    '):
                # Header line
                parts = line.split(' ')
                repo_name = parts[0]
                version = parts[1]
                
                if '/' in repo_name:
                    repo, name = repo_name.split('/')
                else:
                    repo = "unknown"
                    name = repo_name

                current_pkg = {
                    "Name": name,
                    "Source": "Pacman",
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
        # Pacman not found (e.g. Windows)
        pass
    except Exception as e:
        print(f"Error searching pacman: {e}")

    return results

def install_pacman_cmd(packages):
    """
    Returns the command to install a list of packages.
    """
    return ["sudo", "pacman", "-S", "--noconfirm"] + packages
