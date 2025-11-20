import streamlit as st
import pandas as pd
import time
from wrappers.unified_search import unified_search
from manager.package_manager import PackageManager
from utils.system_monitor import get_disk_usage, get_ram_usage
from utils.auth_helper import check_sudo_access

# --- Configuration ---
st.set_page_config(
    page_title="CachyOS One-Shot Installer",
    page_icon="🐧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- State Initialization ---
if 'package_manager' not in st.session_state:
    st.session_state['package_manager'] = PackageManager()

if 'search_results' not in st.session_state:
    st.session_state['search_results'] = []

import os

# --- Sidebar ---
with st.sidebar:
    logo_path = os.path.join(os.path.dirname(__file__), "assets", "logo.png")
    if os.path.exists(logo_path):
        st.image(logo_path, use_container_width=True)
    else:
        st.warning(f"Logo not found at {logo_path}")
    st.title("📦 One-Shot Installer")
    st.markdown("---")
    
    # System Stats
    st.subheader("System Status")
    
    # Disk
    total_disk, used_disk, free_disk = get_disk_usage()
    st.metric("Disk Free", f"{free_disk:.1f} GB", f"Total: {total_disk:.1f} GB")
    st.progress(used_disk / total_disk if total_disk > 0 else 0)
    
    # RAM
    total_ram, avail_ram, percent_ram, used_ram = get_ram_usage()
    st.metric("RAM Free", f"{avail_ram:.1f} GB", f"Total: {total_ram:.1f} GB")
    st.progress(percent_ram / 100)
    
    st.markdown("---")
    
    # Queue
    st.subheader("Installation Queue")
    pm = st.session_state['package_manager']
    grouped_queue = pm.get_queue_by_source()
    
    total_pkgs = len(pm.queue)
    
    if total_pkgs == 0:
        st.info("Queue is empty.")
    else:
        for source, pkgs in grouped_queue.items():
            if pkgs:
                st.markdown(f"**{source}** ({len(pkgs)})")
                for i, pkg in enumerate(pkgs):
                    st.text(f"- {pkg['Name']} ({pkg['Version']})")

        st.markdown("---")
        if st.button("🗑️ Clear Queue"):
            pm.clear_queue()
            st.rerun()
            
        if st.button("🚀 INSTALL ALL", type="primary"):
            if not check_sudo_access():
                st.error("Sudo access required! Please check terminal.")
            else:
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                for msg, progress in pm.install_queue():
                    status_text.text(msg)
                    progress_bar.progress(progress)
                    time.sleep(0.5) # UI smoothing
                
                st.balloons()
                st.success("Installation Complete!")
                pm.clear_queue()
                time.sleep(2)
                st.rerun()

# --- Main Area ---
st.title("CachyOS One-Shot Program Installer 🐧")

# Search Section
col1, col2 = st.columns([3, 1])
with col1:
    query = st.text_input("Search for packages...", placeholder="e.g., firefox, vlc, spotify")
with col2:
    st.write("") # Spacer
    st.write("")
    search_clicked = st.button("🔍 Search", use_container_width=True)

# Filters
col_f1, col_f2, col_f3 = st.columns(3)
with col_f1:
    use_pacman = st.checkbox("Pacman", value=True)
with col_f2:
    use_aur = st.checkbox("AUR", value=True)

if search_clicked and query:
    with st.spinner(f"Searching for '{query}'..."):
        results = unified_search(query, enable_pacman=use_pacman, enable_aur=use_aur)
        st.session_state['search_results'] = results

# Results Display
results = st.session_state['search_results']

if results:
    st.subheader(f"Found {len(results)} packages")
    
    # Convert to DataFrame for easier display if needed, but custom layout is better for actions
    for pkg in results:
        with st.container():
            c1, c2, c3, c4, c5 = st.columns([2, 1, 1, 2, 1])
            
            # Color code source
            source_color = "blue" if pkg['Source'] == "Pacman" else "purple"
            
            with c1:
                st.markdown(f"**{pkg['Name']}**")
                st.caption(pkg['Description'])
            with c2:
                st.markdown(f":{source_color}[{pkg['Source']}]")
            with c3:
                st.text(pkg['Version'])
            with c4:
                st.text(pkg['Repository'])
            with c5:
                # Check if already in queue
                in_queue = False
                for q_pkg in st.session_state['package_manager'].queue:
                    if q_pkg['Name'] == pkg['Name'] and q_pkg['Source'] == pkg['Source']:
                        in_queue = True
                        break
                
                if in_queue:
                    st.button("✅ Added", key=f"btn_{pkg['Source']}_{pkg['Name']}", disabled=True)
                else:
                    if st.button("➕ Add", key=f"btn_{pkg['Source']}_{pkg['Name']}"):
                        st.session_state['package_manager'].add_to_queue(pkg)
                        st.rerun()
            
            st.divider()
elif search_clicked:
    st.warning("No packages found.")
