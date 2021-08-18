[jcluser@centos RunCommand]$ ansible-playbook -i hosts runCommand.yml

PLAY [Run Command Playbook] ****************************************************************************************************************************************************************************

TASK [run show chassis hardware detail] ****************************************************************************************************************************************************************
ok: [vmx1]
ok: [vsrx2]
ok: [vsrx3]
ok: [vsrx1]

TASK [Get stdout or stderr from the output] ************************************************************************************************************************************************************
ok: [vsrx2] => 
  cli_result.stdout:
  - |-
    Hardware inventory:
    Item             Version  Part number  Serial number     Description
    Chassis                                785714CF696C      VSRX
    Midplane         REV 08   750-058562   422229EE          VSRX
    Pseudo CB 0
    Routing Engine 0          BUILTIN      BUILTIN           VSRX-S
    FPC 0            REV 07   611-049549   RL3714040884      FPC
      PIC 0                   BUILTIN      BUILTIN           VSRX DPDK GE
ok: [vmx1] => 
  cli_result.stdout:
  - |-
    Hardware inventory:
    Item             Version  Part number  Serial number     Description
    Chassis                                VM611179344A      VMX
    Midplane
    Routing Engine 0                                         RE-VMX
      ada0  27649 MB  VMware Virtual IDE Har 00000000000000000001 Hard Disk
    CB 0                                                     VMX SCB
    FPC 0                                                    Virtual FPC
      CPU            Rev. 1.0 RIOT-LITE    BUILTIN
      MIC 0                                                  Virtual
        PIC 0                 BUILTIN      BUILTIN           Virtual
ok: [vsrx1] => 
  cli_result.stdout:
  - |-
    Hardware inventory:
    Item             Version  Part number  Serial number     Description
    Chassis                                4A91C5F6CAC1      VSRX
    Midplane         REV 08   750-058562   422243B9          VSRX
    Pseudo CB 0
    Routing Engine 0          BUILTIN      BUILTIN           VSRX-S
    FPC 0            REV 07   611-049549   RL3714040884      FPC
      PIC 0                   BUILTIN      BUILTIN           VSRX DPDK GE
ok: [vsrx3] => 
  cli_result.stdout:
  - |-
    Hardware inventory:
    Item             Version  Part number  Serial number     Description
    Chassis                                509A915D4753      VSRX
    Midplane         REV 08   750-058562   422298F7          VSRX
    Pseudo CB 0
    Routing Engine 0          BUILTIN      BUILTIN           VSRX-S
    FPC 0            REV 07   611-049549   RL3714040884      FPC
      PIC 0                   BUILTIN      BUILTIN           VSRX DPDK GE

PLAY RECAP *********************************************************************************************************************************************************************************************
vmx1                       : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
vsrx1                      : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
vsrx2                      : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
vsrx3                      : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

[jcluser@centos RunCommand]$


===================

[jcluser@centos RunCommand]$ ansible-playbook -i hosts showChassisAlarms.yml 

PLAY [Run Command Playbook] ****************************************************************************************************************************************************************************

TASK [run show chassis and system alarms] **************************************************************************************************************************************************************
ok: [vmx1]
ok: [vsrx1]
ok: [vsrx2]
ok: [vsrx3]

TASK [Get stdout or stderr from the output] ************************************************************************************************************************************************************
ok: [vsrx1] => 
  cli_result.stdout:
  - No alarms currently active
  - |-
    3 alarms currently active
    Alarm time               Class  Description
    2021-08-13 19:01:56 UTC  Minor  Sky ATP: Cloud Based Advanced Threat Prevention on SRX firewalls usage requires a license
    2021-08-13 19:01:56 UTC  Minor  1 Logical System requires a license
    2021-08-11 20:33:46 UTC  Minor  Rescue configuration is not set
ok: [vmx1] => 
  cli_result.stdout:
  - No alarms currently active
  - |-
    2 alarms currently active
    Alarm time               Class  Description
    2021-08-12 18:02:51 UTC  Minor  License for feature VMX-SCALE(167) is about to expire
    2021-08-09 18:51:34 UTC  Minor  Rescue configuration is not set
ok: [vsrx2] => 
  cli_result.stdout:
  - No alarms currently active
  - |-
    3 alarms currently active
    Alarm time               Class  Description
    2021-08-13 19:01:25 UTC  Minor  Sky ATP: Cloud Based Advanced Threat Prevention on SRX firewalls usage requires a license
    2021-08-13 19:01:25 UTC  Minor  1 Logical System requires a license
    2021-08-11 20:34:13 UTC  Minor  Rescue configuration is not set
ok: [vsrx3] => 
  cli_result.stdout:
  - No alarms currently active
  - |-
    3 alarms currently active
    Alarm time               Class  Description
    2021-08-13 19:01:20 UTC  Minor  Sky ATP: Cloud Based Advanced Threat Prevention on SRX firewalls usage requires a license
    2021-08-13 19:01:20 UTC  Minor  1 Logical System requires a license
    2021-08-11 20:34:10 UTC  Minor  Rescue configuration is not set

PLAY RECAP *********************************************************************************************************************************************************************************************
vmx1                       : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
vsrx1                      : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
vsrx2                      : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
vsrx3                      : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

[jcluser@centos RunCommand]$
