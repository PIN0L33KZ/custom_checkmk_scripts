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
            print("1 \"VM Status\" - No VMs returned")
            sys.exit(1)

        # Skip the header line and process the VMs
        vm_list = vm_list[1:]
        overall_status = 0

        for vm in vm_list:
            vm_id, name, status, *_ = vm.split(maxsplit=3)
            service_name = f"{vm_id}-{name}"

            if status.lower() != 'running':
                print(f"2 \"{service_name}\" - VM ID: {vm_id} status: {status}")
            else:
                print(f"0 \"{service_name}\" - VM ID: {vm_id} status: {status}")

    except Exception as e:
        print(f"2 \"VM Status\" - Exception occurred: {str(e)}")
        sys.exit(2)

if __name__ == "__main__":
    get_vm_status()
