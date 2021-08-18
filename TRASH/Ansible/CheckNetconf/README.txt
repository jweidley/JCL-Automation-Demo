[jcluser@centos CheckNetconf]$ ansible-playbook -i hosts ./checkNetconf.yml 

PLAY [Device Connectivity Check] ***********************************************************************************************************************************************************************

TASK [Verify netconf reachability of junos devices] ****************************************************************************************************************************************************
ok: [vmx1]
ok: [vsrx3]
ok: [vsrx1]
ok: [vsrx2]

PLAY RECAP *********************************************************************************************************************************************************************************************
vmx1                       : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
vsrx1                      : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
vsrx2                      : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
vsrx3                      : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

[jcluser@centos CheckNetconf]$ 
