
import logging
import os


network_share_available = os.path.isdir(network_share_path)

if network_share_available:
    log.info("Share already connected.")
else:
    log.info("Connecting to share")

    mount_command = "net use " + SHARE_PATH + " "
    os.system(mount_command)
    network_share_available = os.path.isdir(network_share_path)

    if network_share_available:
        log.fine("Connection success.")
    else:
        raise Exception("Failed to find storage directory.")