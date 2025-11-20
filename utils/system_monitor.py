import shutil
import psutil

def get_disk_usage(path="/"):
    """
    Returns disk usage statistics for the given path.
    Returns: (total, used, free) in GB
    """
    try:
        total, used, free = shutil.disk_usage(path)
        return (
            total / (2**30),
            used / (2**30),
            free / (2**30)
        )
    except Exception as e:
        return (0, 0, 0)

def get_ram_usage():
    """
    Returns RAM usage statistics.
    Returns: (total, available, percent, used) in GB (except percent)
    """
    try:
        mem = psutil.virtual_memory()
        return (
            mem.total / (2**30),
            mem.available / (2**30),
            mem.percent,
            mem.used / (2**30)
        )
    except Exception as e:
        return (0, 0, 0, 0)

def get_cpu_usage():
    """
    Returns current CPU usage percentage.
    """
    try:
        return psutil.cpu_percent(interval=0.1)
    except Exception as e:
        return 0.0
