import subprocess
from wrappers.pacman_wrapper import install_pacman_cmd
from wrappers.aur_wrapper import install_aur_cmd
from utils.auth_helper import get_aur_helper

class PackageManager:
    def __init__(self):
        self.queue = []

    def add_to_queue(self, package):
        """
        Adds a package to the installation queue.
        Package is a dict with 'Name', 'Source', 'Version', etc.
        """
        # Check if already in queue
        for p in self.queue:
            if p['Name'] == package['Name'] and p['Source'] == package['Source']:
                return False
        self.queue.append(package)
        return True

    def remove_from_queue(self, index):
        """
        Removes a package from the queue by index.
        """
        if 0 <= index < len(self.queue):
            self.queue.pop(index)

    def clear_queue(self):
        self.queue = []

    def get_queue_by_source(self):
        """
        Returns queue grouped by source.
        {'Pacman': [pkgs], 'AUR': [pkgs]}
        """
        grouped = {'Pacman': [], 'AUR': [], 'Flatpak': [], 'Snap': []}
        for pkg in self.queue:
            source = pkg.get('Source', 'Unknown')
            if source in grouped:
                grouped[source].append(pkg)
        return grouped

    def install_queue(self, progress_callback=None):
        """
        Installs all packages in the queue.
        Yields status updates (message, progress_float).
        """
        grouped = self.get_queue_by_source()
        total_groups = sum(1 for k in grouped if grouped[k])
        if total_groups == 0:
            return

        current_group = 0
        
        # 1. Install Pacman packages
        if grouped['Pacman']:
            pkg_names = [p['Name'] for p in grouped['Pacman']]
            yield f"Installing Pacman packages: {', '.join(pkg_names)}...", current_group / total_groups
            
            cmd = install_pacman_cmd(pkg_names)
            try:
                # Using subprocess.Popen to stream output could be added later
                # For now, blocking call
                subprocess.run(cmd, check=True)
            except subprocess.CalledProcessError as e:
                yield f"Error installing Pacman packages: {e}", current_group / total_groups
                # Continue to next source? Or stop? 
                # Usually best to continue if possible, or stop if critical.
            
            current_group += 1

        # 2. Install AUR packages
        if grouped['AUR']:
            pkg_names = [p['Name'] for p in grouped['AUR']]
            yield f"Installing AUR packages: {', '.join(pkg_names)}...", current_group / total_groups
            
            helper = get_aur_helper()
            if helper:
                cmd = install_aur_cmd(pkg_names, helper)
                try:
                    subprocess.run(cmd, check=True)
                except subprocess.CalledProcessError as e:
                    yield f"Error installing AUR packages: {e}", current_group / total_groups
            else:
                yield "No AUR helper found. Skipping AUR packages.", current_group / total_groups
            
            current_group += 1

        yield "Installation complete!", 1.0
