[jcluser@centos Backup-Config]$ ansible-playbook -i hosts config-backup.yml 

PLAY [Get Junos OS configuration] **********************************************************************************************************************************************************************

TASK [Save configuration to a file] ********************************************************************************************************************************************************************
changed: [vmx1]
changed: [vsrx2]
changed: [vsrx1]
changed: [vsrx3]

PLAY RECAP *********************************************************************************************************************************************************************************************
vmx1                       : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
vsrx1                      : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
vsrx2                      : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
vsrx3                      : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

[jcluser@centos Backup-Config]$
