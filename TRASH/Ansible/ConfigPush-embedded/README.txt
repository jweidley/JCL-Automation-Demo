[jcluser@centos ConfigPush-embedded]$ ansible-playbook -i hosts pushConfig.yml 

PLAY [Push Configuration to Devices] *******************************************************************************************************************************************************************

TASK [Push Embedded set commands to Devices] ***********************************************************************************************************************************************************
changed: [vmx1]
changed: [vsrx1]
changed: [vsrx3]
changed: [vsrx2]

PLAY RECAP *********************************************************************************************************************************************************************************************
vmx1                       : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
vsrx1                      : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
vsrx2                      : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
vsrx3                      : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

[jcluser@centos ConfigPush-embedded]$ 
