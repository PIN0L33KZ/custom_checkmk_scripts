#!/usr/bin/env python3
import subprocess
import sys

def get_vm_status():
    try:
        result = subprocess.run(['qm', 'list'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            print(f"2 \"VM Status\" - Error: {result.stderr}")
            sys.exit(2)
        
        vm_list = result.stdout.strip().split('\n')
        if len(vm_list) <= 1:
            print("1 \"VM Status\" - No returned no data")
            sys.exit(1)

        # skip header and prcoess output.
        vm_list = vm_list[1:]
        critical_vms = []
        for vm in vm_list:
            vm_id, name, status, *_ = vm.split(maxsplit=3)
            if status.lower() != 'running':
                critical_vms.append(f"{name} (ID: {vm_id}, Status: {status})")

        if critical_vms:
            print(f"2 \"VM Status\" - {', '.join(critical_vms)}")
        else:
            print("0 \"VM Status\" - All VMs are running")
    
    except Exception as e:
        print(f"2 \"VM Status\" - Exception occurred: {str(e)}")
        sys.exit(2)

if __name__ == "__main__":
    get_vm_status()