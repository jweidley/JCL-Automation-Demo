[jcluser@centos RollbackConfig]$ ansible-playbook -i hosts rollBackConfig.yml 

PLAY [Configuration Rollback] **************************************************************************************************************************************************************************

TASK [rollback 1 Configuration Change] *****************************************************************************************************************************************************************
changed: [vmx1]
changed: [vsrx1]
changed: [vsrx3]
changed: [vsrx2]

PLAY RECAP *********************************************************************************************************************************************************************************************
vmx1                       : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
vsrx1                      : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
vsrx2                      : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
vsrx3                      : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

[jcluser@centos RollbackConfig]$
