[jcluser@centos Secure-Copy]$ ansible-playbook -i hosts upload-os.yml 

PLAY [vsrx] ********************************************************************************************************************************************************************************************

TASK [upload local file to var tmp on remote device] ***************************************************************************************************************************************************
changed: [vsrx1]
changed: [vsrx2]
changed: [vsrx3]

PLAY RECAP *********************************************************************************************************************************************************************************************
vsrx1                      : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
vsrx2                      : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
vsrx3                      : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

[jcluser@centos Secure-Copy]$
