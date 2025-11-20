from wrappers.pacman_wrapper import search_pacman
from wrappers.aur_wrapper import search_aur
from utils.auth_helper import get_aur_helper
import concurrent.futures

def unified_search(query, enable_pacman=True, enable_aur=True):
    """
    Searches enabled sources in parallel and returns combined results.
    """
    results = []
    aur_helper = get_aur_helper()
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        
        if enable_pacman:
            futures.append(executor.submit(search_pacman, query))
        
        if enable_aur and aur_helper:
            futures.append(executor.submit(search_aur, query, aur_helper))
            
        for future in concurrent.futures.as_completed(futures):
            try:
                data = future.result()
                results.extend(data)
            except Exception as e:
                print(f"Search error: {e}")
                
    return results
