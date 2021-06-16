#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : DevelopmentMen
# Created Date: vie Jun 10 16:20:00 2021
# =============================================================================
"""este simple script muestra la ip para windows y linux"""
# =============================================================================
# Imports
# =============================================================================
import socket as s
from subprocess import check_output
# =============================================================================
def forWindows():
        try:
                print("Windows ===================")
                print("==> IP Address is: {}\n".format(s.gethostbyname(s.gethostname())))
        except Exception:
                pass
def forLinux():
        try:
                ips = check_output(['hostname', '--all-ip-addresses'])
                print("Linux =====================")
                print("==> IP Address is: {}\n".format(ips.decode()))
        except Exception:
                pass

if __name__ == "__main__":
	forWindows()
	forLinux()
