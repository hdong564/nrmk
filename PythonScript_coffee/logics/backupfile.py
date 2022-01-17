Last login: Wed Jan  5 11:49:33 on ttys000

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
ihandong@ihandong-ui-MacBookPro:~$ ssh user@192.168.10.21
user@192.168.10.21's password: 
Welcome to Ubuntu 14.04.4 LTS (GNU/Linux 3.18.20-xeno-StepTP i686)

 * Documentation:  https://help.ubuntu.com/
Last login: Wed Jan  5 12:58:33 2022 from 192.168.10.120
user@Step-TP:~$ ls
3rd_packages     Desktop           glxgearstest.sh             mov.txt       pyserial-3.5.tar.gz  update
bMaxPower~       dev               gotoCoffeeMachineScript.sh  Music         Qt5.5.1              Videos
bMaxPowez~       Documents         grub                        nrmkbox.txt   record-videos        webrtc
Conty            Downloads         gs_code_backup              Pictures      release              workspace
Conty.Old        eclipse           install                     Public        save-videos
crash-delete.sh  examples.desktop  libgstsplitmuxsink.so       pyserial-3.5  sys
user@Step-TP:~$ cd release/TasksDeployment/PythonScript
user@Step-TP:~/release/TasksDeployment/PythonScript$ ls
config.backup.yml  context.py  examples    order.log           README.md         run_test.py     start.sh
Config.py          devices     indy_utils  process_handler.py  requirements.txt  service
config.yml         events      logics      __pycache__         run.py            service_backup
user@Step-TP:~/release/TasksDeployment/PythonScript$ cd events
user@Step-TP:~/release/TasksDeployment/PythonScript/events$ ls
event_args.py     __pycache__   worker.log.1   worker.log.3  worker.log.6  worker.log.9
event_manager.py  scheduler.py  worker.log.10  worker.log.4  worker.log.7  worker.py
__init__.py       worker.log    worker.log.2   worker.log.5  worker.log.8
user@Step-TP:~/release/TasksDeployment/PythonScript/events$ cat worker.log
[INFO | main_logic.py:310]	2022-01-04 14:00:25,677	> Logic job retrieved <LogicState.PREPARE>.
[INFO | main_logic.py:347]	2022-01-04 14:01:09,108	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:348]	2022-01-04 14:01:09,108	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:351]	2022-01-04 14:01:09,209	> Logic state <RECIPE> begin.
[INFO | main_logic.py:369]	2022-01-04 14:01:28,734	> Logic state <RECIPE> finish.
[INFO | main_logic.py:310]	2022-01-04 14:01:28,835	> Logic job retrieved <LogicState.PREPARE>.
[INFO | main_logic.py:347]	2022-01-04 14:02:09,452	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:348]	2022-01-04 14:02:09,453	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:351]	2022-01-04 14:02:09,554	> Logic state <RECIPE> begin.
[INFO | main_logic.py:369]	2022-01-04 14:02:31,387	> Logic state <RECIPE> finish.
[INFO | main_logic.py:321]	2022-01-04 14:02:31,489	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:372]	2022-01-04 14:02:31,590	> Logic state <LIFT> begin.
[INFO | main_logic.py:397]	2022-01-04 14:02:31,590	> CM Slot[0] -> Lift Slot[0]
[INFO | main_logic.py:415]	2022-01-04 14:02:46,610	> CM Slot[0] -> Lift Slot[0] - Logically done.
[INFO | main_logic.py:425]	2022-01-04 14:02:46,612	> Set order state to DONE. PE_ID:2022010400130001
[INFO | main_logic.py:441]	2022-01-04 14:02:46,614	> Clear job appended.
[INFO | main_logic.py:444]	2022-01-04 14:02:46,615	> Logic state <LIFT> finish.
[INFO | main_logic.py:321]	2022-01-04 14:02:46,716	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:372]	2022-01-04 14:02:46,817	> Logic state <LIFT> begin.
[INFO | main_logic.py:397]	2022-01-04 14:02:46,818	> CM Slot[1] -> Lift Slot[1]
[INFO | main_logic.py:415]	2022-01-04 14:03:05,843	> CM Slot[1] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:425]	2022-01-04 14:03:05,844	> Set order state to DONE. PE_ID:2022010400130001
[INFO | main_logic.py:441]	2022-01-04 14:03:05,846	> Clear job appended.
[INFO | main_logic.py:444]	2022-01-04 14:03:05,847	> Logic state <LIFT> finish.
[INFO | main_logic.py:325]	2022-01-04 14:03:05,948	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:447]	2022-01-04 14:03:06,049	> Logic state <CLEAN> begin.
[INFO | main_logic.py:454]	2022-01-04 14:03:06,050	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:464]	2022-01-04 14:03:40,097	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:454]	2022-01-04 14:03:40,098	> Trying to clean filter - idx: 1 ...
[INFO | main_logic.py:464]	2022-01-04 14:04:20,648	> Trying to clean filter - idx: 1 ... Done.
[INFO | main_logic.py:466]	2022-01-04 14:04:20,649	> Logic state <CLEAN> finish.
[INFO | main_logic.py:325]	2022-01-04 14:04:20,750	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:447]	2022-01-04 14:04:20,851	> Logic state <CLEAN> begin.
[INFO | main_logic.py:466]	2022-01-04 14:04:20,852	> Logic state <CLEAN> finish.
[INFO | main_logic.py:310]	2022-01-04 14:26:30,890	> Logic job retrieved <LogicState.PREPARE>.
[INFO | main_logic.py:347]	2022-01-04 14:27:14,015	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:348]	2022-01-04 14:27:14,016	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:351]	2022-01-04 14:27:14,117	> Logic state <RECIPE> begin.
[INFO | main_logic.py:369]	2022-01-04 14:27:36,950	> Logic state <RECIPE> finish.
[INFO | main_logic.py:310]	2022-01-04 14:27:37,054	> Logic job retrieved <LogicState.PREPARE>.
[INFO | main_logic.py:347]	2022-01-04 14:28:17,673	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:348]	2022-01-04 14:28:17,674	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:351]	2022-01-04 14:28:17,775	> Logic state <RECIPE> begin.
[INFO | main_logic.py:369]	2022-01-04 14:28:39,607	> Logic state <RECIPE> finish.
[INFO | main_logic.py:321]	2022-01-04 14:28:39,708	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:372]	2022-01-04 14:28:39,809	> Logic state <LIFT> begin.
[INFO | main_logic.py:397]	2022-01-04 14:28:39,810	> CM Slot[0] -> Lift Slot[0]
[INFO | main_logic.py:415]	2022-01-04 14:28:54,829	> CM Slot[0] -> Lift Slot[0] - Logically done.
[INFO | main_logic.py:441]	2022-01-04 14:28:54,831	> Clear job appended.
[INFO | main_logic.py:444]	2022-01-04 14:28:54,832	> Logic state <LIFT> finish.
[INFO | main_logic.py:321]	2022-01-04 14:28:54,933	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:372]	2022-01-04 14:28:55,034	> Logic state <LIFT> begin.
[INFO | main_logic.py:397]	2022-01-04 14:28:55,035	> CM Slot[1] -> Lift Slot[1]
[INFO | main_logic.py:415]	2022-01-04 14:29:14,060	> CM Slot[1] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:425]	2022-01-04 14:29:14,061	> Set order state to DONE. PE_ID:2022010400140001
[INFO | main_logic.py:441]	2022-01-04 14:29:14,064	> Clear job appended.
[INFO | main_logic.py:444]	2022-01-04 14:29:14,065	> Logic state <LIFT> finish.
[INFO | main_logic.py:325]	2022-01-04 14:29:14,166	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:447]	2022-01-04 14:29:14,267	> Logic state <CLEAN> begin.
[INFO | main_logic.py:454]	2022-01-04 14:29:14,268	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:464]	2022-01-04 14:29:48,319	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:454]	2022-01-04 14:29:48,320	> Trying to clean filter - idx: 1 ...
[INFO | main_logic.py:464]	2022-01-04 14:30:28,870	> Trying to clean filter - idx: 1 ... Done.
[INFO | main_logic.py:466]	2022-01-04 14:30:28,871	> Logic state <CLEAN> finish.
[INFO | main_logic.py:325]	2022-01-04 14:30:28,972	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:447]	2022-01-04 14:30:29,073	> Logic state <CLEAN> begin.
[INFO | main_logic.py:466]	2022-01-04 14:30:29,075	> Logic state <CLEAN> finish.
[INFO | main_logic.py:310]	2022-01-04 14:36:23,435	> Logic job retrieved <LogicState.PREPARE>.
[INFO | main_logic.py:347]	2022-01-04 14:37:06,963	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:348]	2022-01-04 14:37:06,963	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:351]	2022-01-04 14:37:07,064	> Logic state <RECIPE> begin.
[INFO | main_logic.py:369]	2022-01-04 14:37:26,591	> Logic state <RECIPE> finish.
[INFO | main_logic.py:310]	2022-01-04 14:37:26,692	> Logic job retrieved <LogicState.PREPARE>.
[INFO | main_logic.py:347]	2022-01-04 14:38:07,712	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:348]	2022-01-04 14:38:07,713	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:351]	2022-01-04 14:38:07,814	> Logic state <RECIPE> begin.
[INFO | main_logic.py:369]	2022-01-04 14:38:26,145	> Logic state <RECIPE> finish.
[INFO | main_logic.py:321]	2022-01-04 14:38:26,246	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:372]	2022-01-04 14:38:26,347	> Logic state <LIFT> begin.
[INFO | main_logic.py:397]	2022-01-04 14:38:26,350	> CM Slot[0] -> Lift Slot[0]
[INFO | main_logic.py:415]	2022-01-04 14:38:41,370	> CM Slot[0] -> Lift Slot[0] - Logically done.
[INFO | main_logic.py:441]	2022-01-04 14:38:41,372	> Clear job appended.
[INFO | main_logic.py:444]	2022-01-04 14:38:41,372	> Logic state <LIFT> finish.
[INFO | main_logic.py:321]	2022-01-04 14:38:41,474	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:372]	2022-01-04 14:38:41,575	> Logic state <LIFT> begin.
[INFO | main_logic.py:397]	2022-01-04 14:38:41,576	> CM Slot[1] -> Lift Slot[1]
[INFO | main_logic.py:415]	2022-01-04 14:39:00,599	> CM Slot[1] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:425]	2022-01-04 14:39:00,601	> Set order state to DONE. PE_ID:2022010400160001
[INFO | main_logic.py:441]	2022-01-04 14:39:00,603	> Clear job appended.
[INFO | main_logic.py:444]	2022-01-04 14:39:00,604	> Logic state <LIFT> finish.
[INFO | main_logic.py:325]	2022-01-04 14:39:00,705	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:447]	2022-01-04 14:39:00,806	> Logic state <CLEAN> begin.
[INFO | main_logic.py:454]	2022-01-04 14:39:00,807	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:464]	2022-01-04 14:39:34,853	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:454]	2022-01-04 14:39:34,854	> Trying to clean filter - idx: 1 ...
[INFO | main_logic.py:464]	2022-01-04 14:40:15,403	> Trying to clean filter - idx: 1 ... Done.
[INFO | main_logic.py:466]	2022-01-04 14:40:15,404	> Logic state <CLEAN> finish.
[INFO | main_logic.py:325]	2022-01-04 14:40:15,505	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:447]	2022-01-04 14:40:15,606	> Logic state <CLEAN> begin.
[INFO | main_logic.py:466]	2022-01-04 14:40:15,606	> Logic state <CLEAN> finish.
[INFO | main_logic.py:310]	2022-01-04 14:40:15,707	> Logic job retrieved <LogicState.PREPARE>.
[INFO | main_logic.py:347]	2022-01-04 14:40:58,831	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:348]	2022-01-04 14:40:58,832	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:351]	2022-01-04 14:40:58,933	> Logic state <RECIPE> begin.
[INFO | main_logic.py:369]	2022-01-04 14:41:21,766	> Logic state <RECIPE> finish.
[INFO | main_logic.py:310]	2022-01-04 14:41:21,867	> Logic job retrieved <LogicState.PREPARE>.
[INFO | main_logic.py:347]	2022-01-04 14:42:02,485	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:348]	2022-01-04 14:42:02,485	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:351]	2022-01-04 14:42:02,586	> Logic state <RECIPE> begin.
[INFO | main_logic.py:369]	2022-01-04 14:42:24,418	> Logic state <RECIPE> finish.
[INFO | main_logic.py:321]	2022-01-04 14:42:24,520	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:372]	2022-01-04 14:42:24,621	> Logic state <LIFT> begin.
[INFO | main_logic.py:397]	2022-01-04 14:42:24,621	> CM Slot[0] -> Lift Slot[0]
[INFO | main_logic.py:415]	2022-01-04 14:42:39,639	> CM Slot[0] -> Lift Slot[0] - Logically done.
[INFO | main_logic.py:441]	2022-01-04 14:42:39,641	> Clear job appended.
[INFO | main_logic.py:444]	2022-01-04 14:42:39,642	> Logic state <LIFT> finish.
[INFO | main_logic.py:321]	2022-01-04 14:42:39,743	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:372]	2022-01-04 14:42:39,844	> Logic state <LIFT> begin.
[INFO | main_logic.py:397]	2022-01-04 14:42:39,845	> CM Slot[1] -> Lift Slot[1]
[INFO | main_logic.py:415]	2022-01-04 14:42:58,871	> CM Slot[1] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:425]	2022-01-04 14:42:58,872	> Set order state to DONE. PE_ID:2022010400170001
[INFO | main_logic.py:441]	2022-01-04 14:42:58,875	> Clear job appended.
[INFO | main_logic.py:444]	2022-01-04 14:42:58,876	> Logic state <LIFT> finish.
[INFO | main_logic.py:325]	2022-01-04 14:42:58,977	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:447]	2022-01-04 14:42:59,078	> Logic state <CLEAN> begin.
[INFO | main_logic.py:454]	2022-01-04 14:42:59,079	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:464]	2022-01-04 14:43:33,123	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:454]	2022-01-04 14:43:33,124	> Trying to clean filter - idx: 1 ...
[INFO | main_logic.py:464]	2022-01-04 14:44:13,670	> Trying to clean filter - idx: 1 ... Done.
[INFO | main_logic.py:466]	2022-01-04 14:44:13,671	> Logic state <CLEAN> finish.
[INFO | main_logic.py:325]	2022-01-04 14:44:13,772	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:447]	2022-01-04 14:44:13,873	> Logic state <CLEAN> begin.
[INFO | main_logic.py:466]	2022-01-04 14:44:13,874	> Logic state <CLEAN> finish.
[INFO | main_logic.py:310]	2022-01-04 16:09:36,304	> Logic job retrieved <LogicState.PREPARE>.
[INFO | main_logic.py:347]	2022-01-04 16:10:19,428	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:348]	2022-01-04 16:10:19,429	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:351]	2022-01-04 16:10:19,530	> Logic state <RECIPE> begin.
[INFO | main_logic.py:369]	2022-01-04 16:10:42,363	> Logic state <RECIPE> finish.
[INFO | main_logic.py:321]	2022-01-04 16:10:54,080	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:372]	2022-01-04 16:10:54,180	> Logic state <LIFT> begin.
[INFO | main_logic.py:397]	2022-01-04 16:10:54,182	> CM Slot[0] -> Lift Slot[0]
[INFO | main_logic.py:415]	2022-01-04 16:11:09,202	> CM Slot[0] -> Lift Slot[0] - Logically done.
[INFO | main_logic.py:425]	2022-01-04 16:11:09,203	> Set order state to DONE. PE_ID:2022010400200001
[INFO | main_logic.py:441]	2022-01-04 16:11:09,206	> Clear job appended.
[INFO | main_logic.py:444]	2022-01-04 16:11:09,206	> Logic state <LIFT> finish.
[INFO | main_logic.py:325]	2022-01-04 16:11:09,308	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:447]	2022-01-04 16:11:09,409	> Logic state <CLEAN> begin.
[INFO | main_logic.py:454]	2022-01-04 16:11:09,409	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:464]	2022-01-04 16:11:43,449	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:466]	2022-01-04 16:11:43,450	> Logic state <CLEAN> finish.
[INFO | process_handler.py:81]	2022-01-04 16:16:10,706	> Shutting down...
[INFO | process_handler.py:86]	2022-01-04 16:16:10,707	> Disposing device 'Kiosk'...
[INFO | process_handler.py:88]	2022-01-04 16:16:10,715	> Successfully disposed device 'Kiosk'
[INFO | process_handler.py:86]	2022-01-04 16:16:10,716	> Disposing device 'IceDispenser'...
[INFO | process_handler.py:88]	2022-01-04 16:16:10,717	> Successfully disposed device 'IceDispenser'
[INFO | process_handler.py:86]	2022-01-04 16:16:10,718	> Disposing device 'CupDispenser'...
[INFO | process_handler.py:88]	2022-01-04 16:16:10,726	> Successfully disposed device 'CupDispenser'
[INFO | process_handler.py:86]	2022-01-04 16:16:10,727	> Disposing device 'BarcodeReader'...
[INFO | process_handler.py:88]	2022-01-04 16:16:10,729	> Successfully disposed device 'BarcodeReader'
[INFO | process_handler.py:94]	2022-01-04 16:16:10,732	> Shutting down...Done.
[INFO | process_handler.py:33]	2022-01-04 16:16:28,879	> Configurations_
{'robot_dof': 6, 'db_host': '192.168.10.22', 'db_name': 'KIOSK', 'db_user': 'NEUROMEKA', 'db_pwd': 'NEUROMEKA1234', 'db_timeout': 5, 'db_login_timeout': 5, 'db_charset': 'utf8', 'ice_only': 4, 'water_only': 0, 'ice_and_water': 1, 'coffee_map': {'00000001': 0, '00000002': 3, '00000003': 4, '00000004': 1, '00000005': 5, '00000006': 2}, 'coffee_expiry_time': 600, 'cup_disp_packet_len': 11, 'ice_disp_packet_len': 5, 'milk_refresh_duration': 4800, 'lift_delay': 2, 'lift_cup_delay': 1, 'espresso_machine_shot_delay_1': 6, 'espresso_machine_shot_delay_2': 6, 'espresso_machine_long_delay_1': 12, 'espresso_machine_long_delay_2': 12}
[INFO | process_handler.py:33]	2022-01-04 16:17:42,837	> Configurations_
{'robot_dof': 6, 'db_host': '192.168.10.22', 'db_name': 'KIOSK', 'db_user': 'NEUROMEKA', 'db_pwd': 'NEUROMEKA1234', 'db_timeout': 5, 'db_login_timeout': 5, 'db_charset': 'utf8', 'ice_only': 4, 'water_only': 0, 'ice_and_water': 1, 'coffee_map': {'00000001': 0, '00000002': 3, '00000003': 4, '00000004': 1, '00000005': 5, '00000006': 2}, 'coffee_expiry_time': 600, 'cup_disp_packet_len': 11, 'ice_disp_packet_len': 5, 'milk_refresh_duration': 4800, 'lift_delay': 2, 'lift_cup_delay': 1, 'espresso_machine_shot_delay_1': 6, 'espresso_machine_shot_delay_2': 6, 'espresso_machine_long_delay_1': 12, 'espresso_machine_long_delay_2': 12}
[INFO | process_handler.py:98]	2022-01-04 16:17:56,866	> Program started.
[INFO | process_handler.py:43]	2022-01-04 16:17:56,868	> Preparing program...
[INFO | process_handler.py:52]	2022-01-04 16:17:56,874	> initializing device '<class 'devices.kiosk.Kiosk'>'...
[DEBUG | process_handler.py:58]	2022-01-04 16:17:56,875	> Called on_create of device '<class 'devices.kiosk.Kiosk'>'
[INFO | kiosk.py:94]	2022-01-04 16:17:56,875	> Kiosk - OnCreate
[INFO | kiosk.py:94]	2022-01-04 16:17:56,876	> Kiosk - Trying to connect to Database - host: 192.168.10.22, db: KIOSK.
[INFO | kiosk.py:94]	2022-01-04 16:17:56,933	> Kiosk - Successfully connected to Database.
[INFO | kiosk.py:94]	2022-01-04 16:17:56,934	> Kiosk - OnCreate Done.
[DEBUG | process_handler.py:60]	2022-01-04 16:17:56,935	> on_create of device '<class 'devices.kiosk.Kiosk'>' done.
[INFO | process_handler.py:63]	2022-01-04 16:17:56,935	> Successfully initialized. Device name: Kiosk
[INFO | process_handler.py:52]	2022-01-04 16:17:56,936	> initializing device '<class 'devices.ice_disp.IceDispenser'>'...
[DEBUG | process_handler.py:58]	2022-01-04 16:17:56,937	> Called on_create of device '<class 'devices.ice_disp.IceDispenser'>'
[DEBUG | process_handler.py:60]	2022-01-04 16:17:56,940	> on_create of device '<class 'devices.ice_disp.IceDispenser'>' done.
[INFO | process_handler.py:63]	2022-01-04 16:17:56,941	> Successfully initialized. Device name: IceDispenser
[INFO | process_handler.py:52]	2022-01-04 16:17:56,942	> initializing device '<class 'devices.cup_disp.CupDispenser'>'...
[DEBUG | process_handler.py:58]	2022-01-04 16:17:56,943	> Called on_create of device '<class 'devices.cup_disp.CupDispenser'>'
[DEBUG | process_handler.py:60]	2022-01-04 16:17:56,947	> on_create of device '<class 'devices.cup_disp.CupDispenser'>' done.
[INFO | process_handler.py:63]	2022-01-04 16:17:56,948	> Successfully initialized. Device name: CupDispenser
[INFO | process_handler.py:52]	2022-01-04 16:17:56,949	> initializing device '<class 'devices.barcode_reader.BarcodeReader'>'...
[DEBUG | process_handler.py:58]	2022-01-04 16:17:56,950	> Called on_create of device '<class 'devices.barcode_reader.BarcodeReader'>'
[INFO | barcode_reader.py:26]	2022-01-04 16:17:56,951	> BarcodeReader - OnCreate
[INFO | barcode_reader.py:30]	2022-01-04 16:17:56,953	> barcode thread start
[DEBUG | process_handler.py:60]	2022-01-04 16:17:56,955	> on_create of device '<class 'devices.barcode_reader.BarcodeReader'>' done.
[INFO | process_handler.py:63]	2022-01-04 16:17:56,956	> Successfully initialized. Device name: BarcodeReader
[INFO | process_handler.py:75]	2022-01-04 16:17:56,958	> Preparing program...Done.
[INFO | main_logic.py:526]	2022-01-04 16:21:01,714	> Event on_kiosk_listener called. New Menu: ICED_AMERICANO, PEID: 2022010400220001, OJ_NO: 1
[INFO | main_logic.py:526]	2022-01-04 16:21:01,719	> Event on_kiosk_listener called. New Menu: ICED_AMERICANO, PEID: 2022010400220001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-04 16:21:05,304	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-04 16:21:05,316	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb5fb40ec>
[INFO | main_logic.py:567]	2022-01-04 16:21:48,726	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-04 16:21:48,730	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-04 16:21:48,730	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-04 16:21:48,831	> Logic state <RECIPE> begin.
[INFO | ice_disp.py:48]	2022-01-04 16:21:52,339	> Event occurred! Event Type: 0, Args: <logics.coffee.Coffee object at 0xb5fb40ec>
[INFO | ice_disp.py:50]	2022-01-04 16:21:52,340	> ice serial is already opend!
[INFO | ice_disp.py:106]	2022-01-04 16:21:52,342	> Called CheckIceDispenser
[INFO | ice_disp.py:107]	2022-01-04 16:21:52,344	> ice status check: {packet}
[INFO | ice_disp.py:116]	2022-01-04 16:21:52,355	> Try read packet...
[INFO | ice_disp.py:120]	2022-01-04 16:21:52,358	> reconnet to serialIceDispenser...
[INFO | ice_disp.py:176]	2022-01-04 16:21:52,425	> status check done
[INFO | ice_disp.py:48]	2022-01-04 16:21:59,306	> Event occurred! Event Type: 1, Args: None
[INFO | ice_disp.py:50]	2022-01-04 16:21:59,309	> ice serial is already opend!
[INFO | ice_disp.py:61]	2022-01-04 16:21:59,599	> Close icedisp serial done
[INFO | main_logic.py:363]	2022-01-04 16:22:08,157	> Logic state <RECIPE> finish.
[INFO | main_logic.py:304]	2022-01-04 16:22:08,258	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-04 16:22:08,268	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb5fb414c>
[INFO | main_logic.py:554]	2022-01-04 16:22:19,480	> Event on_coffee_done called.
[INFO | main_logic.py:567]	2022-01-04 16:22:49,238	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-04 16:22:49,277	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-04 16:22:49,278	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-04 16:22:49,379	> Logic state <RECIPE> begin.
[INFO | ice_disp.py:48]	2022-01-04 16:22:52,906	> Event occurred! Event Type: 0, Args: <logics.coffee.Coffee object at 0xb5fb414c>
[INFO | ice_disp.py:53]	2022-01-04 16:22:52,913	> create new icedisp serial
[INFO | ice_disp.py:106]	2022-01-04 16:22:52,913	> Called CheckIceDispenser
[INFO | ice_disp.py:107]	2022-01-04 16:22:52,914	> ice status check: {packet}
[INFO | ice_disp.py:116]	2022-01-04 16:22:52,925	> Try read packet...
[INFO | ice_disp.py:120]	2022-01-04 16:22:52,929	> reconnet to serialIceDispenser...
[INFO | ice_disp.py:176]	2022-01-04 16:22:52,995	> status check done
[INFO | ice_disp.py:48]	2022-01-04 16:22:59,883	> Event occurred! Event Type: 1, Args: None
[INFO | ice_disp.py:50]	2022-01-04 16:22:59,884	> ice serial is already opend!
[INFO | ice_disp.py:61]	2022-01-04 16:23:00,168	> Close icedisp serial done
[INFO | main_logic.py:363]	2022-01-04 16:23:07,709	> Logic state <RECIPE> finish.
[INFO | main_logic.py:315]	2022-01-04 16:23:07,810	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-04 16:23:07,911	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-04 16:23:07,912	> CM Slot[0] -> Lift Slot[0]
[INFO | main_logic.py:172]	2022-01-04 16:23:17,835	> di idx 10 : 1
[INFO | main_logic.py:172]	2022-01-04 16:23:17,963	> di idx 10 : 0
[INFO | main_logic.py:172]	2022-01-04 16:23:18,005	> di idx 10 : 1
[INFO | main_logic.py:554]	2022-01-04 16:23:18,858	> Event on_coffee_done called.
[INFO | main_logic.py:535]	2022-01-04 16:23:21,692	> Event on_barcode_listener called. Barcode: 2022010400220001
[INFO | main_logic.py:543]	2022-01-04 16:23:21,693	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-04 16:23:21,694	> State: False, The slot[1] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-04 16:23:21,699	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:409]	2022-01-04 16:23:22,929	> CM Slot[0] -> Lift Slot[0] - Logically done.
[INFO | main_logic.py:435]	2022-01-04 16:23:22,931	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-04 16:23:22,932	> Logic state <LIFT> finish.
[INFO | main_logic.py:315]	2022-01-04 16:23:23,033	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-04 16:23:23,134	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-04 16:23:23,135	> CM Slot[1] -> Lift Slot[1]
[INFO | main_logic.py:535]	2022-01-04 16:23:31,867	> Event on_barcode_listener called. Barcode: 2022010400220001
[INFO | main_logic.py:541]	2022-01-04 16:23:31,870	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-04 16:23:31,871	> Barcode: 2022010400220001, PE ID: 2022010400220001, Compare: True
[INFO | main_logic.py:547]	2022-01-04 16:23:31,873	> Expired: False
[INFO | main_logic.py:543]	2022-01-04 16:23:31,878	> State: False, The slot[1] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-04 16:23:31,879	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-04 16:23:35,526	> di idx 11 : 1
[INFO | main_logic.py:172]	2022-01-04 16:23:35,734	> di idx 10 : 0
[INFO | main_logic.py:203]	2022-01-04 16:23:36,693	> Removed cup by customer. Index: 0
[INFO | main_logic.py:535]	2022-01-04 16:23:36,887	> Event on_barcode_listener called. Barcode: 2022010400220001
[INFO | main_logic.py:541]	2022-01-04 16:23:36,888	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-04 16:23:36,890	> Barcode: 2022010400220001, PE ID: 2022010400220001, Compare: True
[INFO | main_logic.py:547]	2022-01-04 16:23:36,893	> Expired: False
[INFO | main_logic.py:543]	2022-01-04 16:23:36,896	> State: False, The slot[1] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-04 16:23:36,898	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:203]	2022-01-04 16:23:36,904	> Removed cup by customer. Index: 0
[INFO | main_logic.py:535]	2022-01-04 16:23:38,725	> Event on_barcode_listener called. Barcode: 2022010400220001
[INFO | main_logic.py:541]	2022-01-04 16:23:38,727	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-04 16:23:38,729	> Barcode: 2022010400220001, PE ID: 2022010400220001, Compare: True
[INFO | main_logic.py:547]	2022-01-04 16:23:38,730	> Expired: False
[INFO | main_logic.py:543]	2022-01-04 16:23:38,735	> State: False, The slot[1] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-04 16:23:38,735	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:203]	2022-01-04 16:23:38,742	> Removed cup by customer. Index: 0
[DEBUG | main_logic.py:234]	2022-01-04 16:23:41,909	> Removing Coffee confirmed : lift_index: 0, PE_ID: 2022010400220001, menu: ICED_AMERICANO
[INFO | main_logic.py:172]	2022-01-04 16:23:42,034	> di idx 10 : 1
[INFO | main_logic.py:409]	2022-01-04 16:23:42,159	> CM Slot[1] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-04 16:23:42,161	> Set order state to DONE. PE_ID:2022010400220001
[INFO | main_logic.py:435]	2022-01-04 16:23:42,164	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-04 16:23:42,165	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-04 16:23:42,266	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-04 16:23:42,367	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-04 16:23:42,368	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-04 16:23:45,017	> Event on_barcode_listener called. Barcode: 2022010400220001
[INFO | main_logic.py:543]	2022-01-04 16:23:45,020	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-04 16:23:45,020	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-04 16:23:45,022	> Barcode: 2022010400220001, PE ID: 2022010400220001, Compare: True
[INFO | main_logic.py:547]	2022-01-04 16:23:45,023	> Expired: False
[INFO | main_logic.py:543]	2022-01-04 16:23:45,028	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-04 16:23:48,803	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-04 16:23:49,793	> Removed cup by customer. Index: 1
[DEBUG | main_logic.py:234]	2022-01-04 16:23:54,633	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010400220001, menu: ICED_AMERICANO
[INFO | main_logic.py:241]	2022-01-04 16:23:54,635	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010400220001, menu: ICED_AMERICANO
[INFO | main_logic.py:535]	2022-01-04 16:24:07,436	> Event on_barcode_listener called. Barcode: 2022010400220001
[INFO | main_logic.py:543]	2022-01-04 16:24:07,439	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-04 16:24:07,439	> State: False, The slot[1] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-04 16:24:07,442	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:458]	2022-01-04 16:24:16,410	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:448]	2022-01-04 16:24:16,411	> Trying to clean filter - idx: 1 ...
[INFO | main_logic.py:458]	2022-01-04 16:24:56,958	> Trying to clean filter - idx: 1 ... Done.
[INFO | main_logic.py:460]	2022-01-04 16:24:56,959	> Logic state <CLEAN> finish.
[INFO | main_logic.py:319]	2022-01-04 16:24:57,060	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-04 16:24:57,161	> Logic state <CLEAN> begin.
[INFO | main_logic.py:460]	2022-01-04 16:24:57,162	> Logic state <CLEAN> finish.
[INFO | main_logic.py:172]	2022-01-04 16:25:10,130	> di idx 10 : 0
[INFO | main_logic.py:172]	2022-01-04 16:59:15,815	> di idx 10 : 1
[INFO | main_logic.py:172]	2022-01-04 16:59:16,644	> di idx 10 : 0
[INFO | main_logic.py:172]	2022-01-04 16:59:16,852	> di idx 10 : 1
[INFO | main_logic.py:172]	2022-01-04 16:59:17,303	> di idx 10 : 0
[INFO | main_logic.py:172]	2022-01-04 16:59:17,593	> di idx 10 : 1
[INFO | main_logic.py:172]	2022-01-04 16:59:17,968	> di idx 10 : 0
[INFO | main_logic.py:526]	2022-01-04 17:03:40,539	> Event on_kiosk_listener called. New Menu: AMERICANO, PEID: 2022010400240001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-04 17:03:46,127	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-04 17:03:46,136	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb5fb420c>
[INFO | main_logic.py:567]	2022-01-04 17:04:29,170	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-04 17:04:29,254	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-04 17:04:29,255	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-04 17:04:29,356	> Logic state <RECIPE> begin.
[INFO | main_logic.py:363]	2022-01-04 17:04:52,189	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-04 17:05:03,510	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-04 17:05:03,907	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-04 17:05:04,008	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-04 17:05:04,008	> CM Slot[0] -> Lift Slot[0]
[INFO | main_logic.py:172]	2022-01-04 17:05:13,858	> di idx 10 : 1
[INFO | main_logic.py:409]	2022-01-04 17:05:19,027	> CM Slot[0] -> Lift Slot[0] - Logically done.
[INFO | main_logic.py:419]	2022-01-04 17:05:19,029	> Set order state to DONE. PE_ID:2022010400240001
[INFO | main_logic.py:435]	2022-01-04 17:05:19,032	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-04 17:05:19,033	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-04 17:05:19,134	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-04 17:05:19,235	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-04 17:05:19,236	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-04 17:05:25,822	> Event on_barcode_listener called. Barcode: 2022010400240001
[INFO | main_logic.py:541]	2022-01-04 17:05:25,824	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-04 17:05:25,825	> Barcode: 2022010400240001, PE ID: 2022010400240001, Compare: True
[INFO | main_logic.py:547]	2022-01-04 17:05:25,827	> Expired: False
[INFO | main_logic.py:543]	2022-01-04 17:05:25,830	> State: False, The slot[1] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-04 17:05:25,832	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-04 17:05:32,003	> di idx 10 : 0
[INFO | main_logic.py:203]	2022-01-04 17:05:32,998	> Removed cup by customer. Index: 0
[DEBUG | main_logic.py:234]	2022-01-04 17:05:38,093	> Removing Coffee confirmed : lift_index: 0, PE_ID: 2022010400240001, menu: AMERICANO
[INFO | main_logic.py:241]	2022-01-04 17:05:38,097	> State changed [2] -> [3], lift_index: 0, PE_ID: 2022010400240001, menu: AMERICANO
[INFO | main_logic.py:458]	2022-01-04 17:05:53,277	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-04 17:05:53,278	> Logic state <CLEAN> finish.
[INFO | main_logic.py:526]	2022-01-04 17:21:17,249	> Event on_kiosk_listener called. New Menu: AMERICANO, PEID: 2022010400250001, OJ_NO: 1
[INFO | main_logic.py:526]	2022-01-04 17:21:17,254	> Event on_kiosk_listener called. New Menu: AMERICANO, PEID: 2022010400250001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-04 17:21:22,606	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-04 17:21:22,628	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb5fb48ec>
[INFO | main_logic.py:567]	2022-01-04 17:22:05,661	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-04 17:22:05,729	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-04 17:22:05,730	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-04 17:22:05,831	> Logic state <RECIPE> begin.
[INFO | main_logic.py:363]	2022-01-04 17:22:28,664	> Logic state <RECIPE> finish.
[INFO | main_logic.py:304]	2022-01-04 17:22:28,769	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-04 17:22:28,783	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb5fb430c>
[INFO | main_logic.py:554]	2022-01-04 17:22:39,978	> Event on_coffee_done called.
[INFO | main_logic.py:567]	2022-01-04 17:23:09,358	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-04 17:23:09,389	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-04 17:23:09,390	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-04 17:23:09,491	> Logic state <RECIPE> begin.
[INFO | main_logic.py:363]	2022-01-04 17:23:31,323	> Logic state <RECIPE> finish.
[INFO | main_logic.py:315]	2022-01-04 17:23:31,424	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-04 17:23:31,525	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-04 17:23:31,526	> CM Slot[0] -> Lift Slot[0]
[INFO | main_logic.py:172]	2022-01-04 17:23:41,371	> di idx 10 : 1
[INFO | main_logic.py:554]	2022-01-04 17:23:42,480	> Event on_coffee_done called.
[INFO | main_logic.py:409]	2022-01-04 17:23:46,546	> CM Slot[0] -> Lift Slot[0] - Logically done.
[INFO | main_logic.py:435]	2022-01-04 17:23:46,548	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-04 17:23:46,549	> Logic state <LIFT> finish.
[INFO | main_logic.py:315]	2022-01-04 17:23:46,650	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-04 17:23:46,751	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-04 17:23:46,752	> CM Slot[1] -> Lift Slot[1]
[INFO | main_logic.py:535]	2022-01-04 17:23:49,240	> Event on_barcode_listener called. Barcode: 2022010400250001
[INFO | main_logic.py:541]	2022-01-04 17:23:49,242	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-04 17:23:49,243	> Barcode: 2022010400250001, PE ID: 2022010400250001, Compare: True
[INFO | main_logic.py:547]	2022-01-04 17:23:49,246	> Expired: False
[INFO | main_logic.py:543]	2022-01-04 17:23:49,249	> State: False, The slot[1] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-04 17:23:49,252	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-04 17:23:55,263	> di idx 10 : 0
[INFO | main_logic.py:203]	2022-01-04 17:23:56,263	> Removed cup by customer. Index: 0
[INFO | main_logic.py:172]	2022-01-04 17:23:58,922	> di idx 11 : 1
[DEBUG | main_logic.py:234]	2022-01-04 17:24:01,352	> Removing Coffee confirmed : lift_index: 0, PE_ID: 2022010400250001, menu: AMERICANO
[INFO | main_logic.py:535]	2022-01-04 17:24:03,641	> Event on_barcode_listener called. Barcode: 2022010400250001
[INFO | main_logic.py:543]	2022-01-04 17:24:03,642	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-04 17:24:03,644	> State: False, The slot[1] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-04 17:24:03,646	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:409]	2022-01-04 17:24:05,777	> CM Slot[1] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-04 17:24:05,779	> Set order state to DONE. PE_ID:2022010400250001
[INFO | main_logic.py:435]	2022-01-04 17:24:05,782	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-04 17:24:05,783	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-04 17:24:05,884	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-04 17:24:05,985	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-04 17:24:05,986	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-04 17:24:06,869	> Event on_barcode_listener called. Barcode: 2022010400250001
[INFO | main_logic.py:543]	2022-01-04 17:24:06,871	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-04 17:24:06,873	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-04 17:24:06,874	> Barcode: 2022010400250001, PE ID: 2022010400250001, Compare: True
[INFO | main_logic.py:547]	2022-01-04 17:24:06,876	> Expired: False
[INFO | main_logic.py:543]	2022-01-04 17:24:06,881	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-04 17:24:11,783	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-04 17:24:12,780	> Removed cup by customer. Index: 1
[DEBUG | main_logic.py:234]	2022-01-04 17:24:17,624	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010400250001, menu: AMERICANO
[INFO | main_logic.py:241]	2022-01-04 17:24:17,628	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010400250001, menu: AMERICANO
[INFO | main_logic.py:458]	2022-01-04 17:24:40,027	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:448]	2022-01-04 17:24:40,028	> Trying to clean filter - idx: 1 ...
[INFO | main_logic.py:458]	2022-01-04 17:25:20,576	> Trying to clean filter - idx: 1 ... Done.
[INFO | main_logic.py:460]	2022-01-04 17:25:20,576	> Logic state <CLEAN> finish.
[INFO | main_logic.py:319]	2022-01-04 17:25:20,678	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-04 17:25:20,779	> Logic state <CLEAN> begin.
[INFO | main_logic.py:460]	2022-01-04 17:25:20,780	> Logic state <CLEAN> finish.
[INFO | main_logic.py:526]	2022-01-04 17:36:18,981	> Event on_kiosk_listener called. New Menu: ICED_AMERICANO, PEID: 2022010400270001, OJ_NO: 1
[INFO | main_logic.py:526]	2022-01-04 17:36:18,985	> Event on_kiosk_listener called. New Menu: ICED_AMERICANO, PEID: 2022010400270001, OJ_NO: 1
[INFO | main_logic.py:572]	2022-01-04 17:36:20,578	> Refresh milk called, but
[INFO | main_logic.py:304]	2022-01-04 17:36:22,955	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-04 17:36:22,964	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb5fe234c>
[INFO | main_logic.py:567]	2022-01-04 17:37:06,388	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-04 17:37:06,483	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-04 17:37:06,486	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-04 17:37:06,587	> Logic state <RECIPE> begin.
[INFO | ice_disp.py:48]	2022-01-04 17:37:10,107	> Event occurred! Event Type: 0, Args: <logics.coffee.Coffee object at 0xb5fe234c>
[INFO | ice_disp.py:53]	2022-01-04 17:37:10,114	> create new icedisp serial
[INFO | ice_disp.py:106]	2022-01-04 17:37:10,114	> Called CheckIceDispenser
[INFO | ice_disp.py:107]	2022-01-04 17:37:10,115	> ice status check: {packet}
[INFO | ice_disp.py:116]	2022-01-04 17:37:10,126	> Try read packet...
[INFO | ice_disp.py:120]	2022-01-04 17:37:10,129	> reconnet to serialIceDispenser...
[INFO | ice_disp.py:176]	2022-01-04 17:37:10,195	> status check done
[INFO | ice_disp.py:48]	2022-01-04 17:37:17,092	> Event occurred! Event Type: 1, Args: None
[INFO | ice_disp.py:50]	2022-01-04 17:37:17,094	> ice serial is already opend!
[INFO | ice_disp.py:61]	2022-01-04 17:37:17,370	> Close icedisp serial done
[INFO | main_logic.py:363]	2022-01-04 17:37:25,913	> Logic state <RECIPE> finish.
[INFO | main_logic.py:304]	2022-01-04 17:37:26,015	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-04 17:37:26,021	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb5fe20ac>
[INFO | main_logic.py:554]	2022-01-04 17:37:37,240	> Event on_coffee_done called.
[INFO | main_logic.py:567]	2022-01-04 17:38:06,977	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-04 17:38:07,035	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-04 17:38:07,036	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-04 17:38:07,137	> Logic state <RECIPE> begin.
[INFO | ice_disp.py:48]	2022-01-04 17:38:10,667	> Event occurred! Event Type: 0, Args: <logics.coffee.Coffee object at 0xb5fe20ac>
[INFO | ice_disp.py:53]	2022-01-04 17:38:10,674	> create new icedisp serial
[INFO | ice_disp.py:106]	2022-01-04 17:38:10,675	> Called CheckIceDispenser
[INFO | ice_disp.py:107]	2022-01-04 17:38:10,675	> ice status check: {packet}
[INFO | ice_disp.py:116]	2022-01-04 17:38:10,686	> Try read packet...
[INFO | ice_disp.py:120]	2022-01-04 17:38:10,690	> reconnet to serialIceDispenser...
[INFO | ice_disp.py:176]	2022-01-04 17:38:10,756	> status check done
[INFO | ice_disp.py:48]	2022-01-04 17:38:17,693	> Event occurred! Event Type: 1, Args: None
[INFO | ice_disp.py:50]	2022-01-04 17:38:17,695	> ice serial is already opend!
[INFO | ice_disp.py:61]	2022-01-04 17:38:17,980	> Close icedisp serial done
[INFO | main_logic.py:363]	2022-01-04 17:38:25,660	> Logic state <RECIPE> finish.
[INFO | main_logic.py:315]	2022-01-04 17:38:25,761	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-04 17:38:25,862	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-04 17:38:25,863	> CM Slot[0] -> Lift Slot[0]
[INFO | main_logic.py:172]	2022-01-04 17:38:35,749	> di idx 10 : 1
[INFO | main_logic.py:172]	2022-01-04 17:38:35,917	> di idx 10 : 0
[INFO | main_logic.py:172]	2022-01-04 17:38:35,959	> di idx 10 : 1
[INFO | main_logic.py:554]	2022-01-04 17:38:36,803	> Event on_coffee_done called.
[INFO | main_logic.py:409]	2022-01-04 17:38:40,883	> CM Slot[0] -> Lift Slot[0] - Logically done.
[INFO | main_logic.py:435]	2022-01-04 17:38:40,885	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-04 17:38:40,886	> Logic state <LIFT> finish.
[INFO | main_logic.py:315]	2022-01-04 17:38:40,987	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-04 17:38:41,088	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-04 17:38:41,089	> CM Slot[1] -> Lift Slot[1]
[INFO | main_logic.py:535]	2022-01-04 17:38:42,280	> Event on_barcode_listener called. Barcode: 2022010400270001
[INFO | main_logic.py:541]	2022-01-04 17:38:42,282	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-04 17:38:42,283	> Barcode: 2022010400270001, PE ID: 2022010400270001, Compare: True
[INFO | main_logic.py:547]	2022-01-04 17:38:42,285	> Expired: False
[INFO | main_logic.py:543]	2022-01-04 17:38:42,289	> State: False, The slot[1] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-04 17:38:42,292	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-04 17:38:46,190	> di idx 10 : 0
[INFO | main_logic.py:203]	2022-01-04 17:38:47,190	> Removed cup by customer. Index: 0
[DEBUG | main_logic.py:234]	2022-01-04 17:38:52,273	> Removing Coffee confirmed : lift_index: 0, PE_ID: 2022010400270001, menu: ICED_AMERICANO
[INFO | main_logic.py:172]	2022-01-04 17:38:53,525	> di idx 11 : 1
[INFO | main_logic.py:535]	2022-01-04 17:38:54,848	> Event on_barcode_listener called. Barcode: 2022010400270001
[INFO | main_logic.py:543]	2022-01-04 17:38:54,849	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-04 17:38:54,851	> State: False, The slot[1] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-04 17:38:54,854	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:535]	2022-01-04 17:38:58,891	> Event on_barcode_listener called. Barcode: 2022010400270001
[INFO | main_logic.py:543]	2022-01-04 17:38:58,893	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-04 17:38:58,896	> State: False, The slot[1] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-04 17:38:58,896	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:409]	2022-01-04 17:39:00,111	> CM Slot[1] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-04 17:39:00,113	> Set order state to DONE. PE_ID:2022010400270001
[INFO | main_logic.py:435]	2022-01-04 17:39:00,116	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-04 17:39:00,117	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-04 17:39:00,218	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-04 17:39:00,320	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-04 17:39:00,320	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-04 17:39:00,736	> Event on_barcode_listener called. Barcode: 2022010400270001
[INFO | main_logic.py:543]	2022-01-04 17:39:00,740	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-04 17:39:00,741	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-04 17:39:00,743	> Barcode: 2022010400270001, PE ID: 2022010400270001, Compare: True
[INFO | main_logic.py:547]	2022-01-04 17:39:00,745	> Expired: False
[INFO | main_logic.py:543]	2022-01-04 17:39:00,748	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-04 17:39:04,311	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-04 17:39:05,299	> Removed cup by customer. Index: 1
[DEBUG | main_logic.py:234]	2022-01-04 17:39:10,039	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010400270001, menu: ICED_AMERICANO
[INFO | main_logic.py:241]	2022-01-04 17:39:10,042	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010400270001, menu: ICED_AMERICANO
[INFO | main_logic.py:172]	2022-01-04 17:39:11,698	> di idx 10 : 1
[INFO | main_logic.py:458]	2022-01-04 17:39:34,363	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:448]	2022-01-04 17:39:34,363	> Trying to clean filter - idx: 1 ...
[INFO | main_logic.py:458]	2022-01-04 17:40:14,908	> Trying to clean filter - idx: 1 ... Done.
[INFO | main_logic.py:460]	2022-01-04 17:40:14,909	> Logic state <CLEAN> finish.
[INFO | main_logic.py:319]	2022-01-04 17:40:15,010	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-04 17:40:15,111	> Logic state <CLEAN> begin.
[INFO | main_logic.py:460]	2022-01-04 17:40:15,112	> Logic state <CLEAN> finish.
[INFO | main_logic.py:172]	2022-01-04 17:47:31,620	> di idx 10 : 0
[INFO | main_logic.py:526]	2022-01-04 17:49:01,622	> Event on_kiosk_listener called. New Menu: ICED_AMERICANO, PEID: 2022010400280001, OJ_NO: 1
[INFO | main_logic.py:526]	2022-01-04 17:49:01,627	> Event on_kiosk_listener called. New Menu: ICED_AMERICANO, PEID: 2022010400280001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-04 17:49:03,703	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-04 17:49:03,719	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb5fe21cc>
[INFO | main_logic.py:567]	2022-01-04 17:49:47,124	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-04 17:49:47,128	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-04 17:49:47,129	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-04 17:49:47,230	> Logic state <RECIPE> begin.
[INFO | ice_disp.py:48]	2022-01-04 17:49:50,750	> Event occurred! Event Type: 0, Args: <logics.coffee.Coffee object at 0xb5fe21cc>
[INFO | ice_disp.py:53]	2022-01-04 17:49:50,757	> create new icedisp serial
[INFO | ice_disp.py:106]	2022-01-04 17:49:50,758	> Called CheckIceDispenser
[INFO | ice_disp.py:107]	2022-01-04 17:49:50,759	> ice status check: {packet}
[INFO | ice_disp.py:116]	2022-01-04 17:49:50,770	> Try read packet...
[INFO | ice_disp.py:120]	2022-01-04 17:49:50,775	> reconnet to serialIceDispenser...
[INFO | ice_disp.py:176]	2022-01-04 17:49:50,842	> status check done
[INFO | ice_disp.py:48]	2022-01-04 17:49:57,718	> Event occurred! Event Type: 1, Args: None
[INFO | ice_disp.py:50]	2022-01-04 17:49:57,721	> ice serial is already opend!
[INFO | ice_disp.py:61]	2022-01-04 17:49:58,016	> Close icedisp serial done
[INFO | main_logic.py:363]	2022-01-04 17:50:06,555	> Logic state <RECIPE> finish.
[INFO | main_logic.py:304]	2022-01-04 17:50:06,656	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-04 17:50:06,665	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb5fe2c8c>
[INFO | main_logic.py:554]	2022-01-04 17:50:17,871	> Event on_coffee_done called.
[INFO | main_logic.py:567]	2022-01-04 17:50:47,631	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-04 17:50:47,675	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-04 17:50:47,676	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-04 17:50:47,777	> Logic state <RECIPE> begin.
[INFO | ice_disp.py:48]	2022-01-04 17:50:51,290	> Event occurred! Event Type: 0, Args: <logics.coffee.Coffee object at 0xb5fe2c8c>
[INFO | ice_disp.py:53]	2022-01-04 17:50:51,298	> create new icedisp serial
[INFO | ice_disp.py:106]	2022-01-04 17:50:51,298	> Called CheckIceDispenser
[INFO | ice_disp.py:107]	2022-01-04 17:50:51,299	> ice status check: {packet}
[INFO | ice_disp.py:116]	2022-01-04 17:50:51,310	> Try read packet...
[INFO | ice_disp.py:120]	2022-01-04 17:50:51,314	> reconnet to serialIceDispenser...
[INFO | ice_disp.py:176]	2022-01-04 17:50:51,380	> status check done
[INFO | ice_disp.py:48]	2022-01-04 17:50:58,311	> Event occurred! Event Type: 1, Args: None
[INFO | ice_disp.py:50]	2022-01-04 17:50:58,314	> ice serial is already opend!
[INFO | ice_disp.py:61]	2022-01-04 17:50:58,602	> Close icedisp serial done
[INFO | main_logic.py:363]	2022-01-04 17:51:06,302	> Logic state <RECIPE> finish.
[INFO | main_logic.py:315]	2022-01-04 17:51:06,403	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-04 17:51:06,504	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-04 17:51:06,505	> CM Slot[0] -> Lift Slot[0]
[INFO | main_logic.py:172]	2022-01-04 17:51:16,609	> di idx 10 : 1
[INFO | main_logic.py:554]	2022-01-04 17:51:17,444	> Event on_coffee_done called.
[INFO | main_logic.py:535]	2022-01-04 17:51:20,187	> Event on_barcode_listener called. Barcode: 2022010400280001
[INFO | main_logic.py:543]	2022-01-04 17:51:20,188	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-04 17:51:20,191	> State: False, The slot[1] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-04 17:51:20,192	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:409]	2022-01-04 17:51:21,524	> CM Slot[0] -> Lift Slot[0] - Logically done.
[INFO | main_logic.py:435]	2022-01-04 17:51:21,526	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-04 17:51:21,527	> Logic state <LIFT> finish.
[INFO | main_logic.py:315]	2022-01-04 17:51:21,628	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-04 17:51:21,729	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-04 17:51:21,730	> CM Slot[1] -> Lift Slot[1]
[INFO | main_logic.py:535]	2022-01-04 17:51:23,592	> Event on_barcode_listener called. Barcode: 2022010400280001
[INFO | main_logic.py:541]	2022-01-04 17:51:23,593	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-04 17:51:23,596	> Barcode: 2022010400280001, PE ID: 2022010400280001, Compare: True
[INFO | main_logic.py:547]	2022-01-04 17:51:23,596	> Expired: False
[INFO | main_logic.py:543]	2022-01-04 17:51:23,602	> State: False, The slot[1] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-04 17:51:23,603	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-04 17:51:27,605	> di idx 10 : 0
[INFO | main_logic.py:172]	2022-01-04 17:51:34,066	> di idx 11 : 1
[INFO | main_logic.py:203]	2022-01-04 17:51:39,472	> Removed cup by customer. Index: 0
[INFO | main_logic.py:409]	2022-01-04 17:51:40,754	> CM Slot[1] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-04 17:51:40,756	> Set order state to DONE. PE_ID:2022010400280001
[INFO | main_logic.py:435]	2022-01-04 17:51:40,758	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-04 17:51:40,759	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-04 17:51:40,861	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-04 17:51:40,962	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-04 17:51:40,962	> Trying to clean filter - idx: 0 ...
[DEBUG | main_logic.py:234]	2022-01-04 17:51:44,560	> Removing Coffee confirmed : lift_index: 0, PE_ID: 2022010400280001, menu: ICED_AMERICANO
[INFO | main_logic.py:241]	2022-01-04 17:51:44,565	> State changed [2] -> [3], lift_index: 0, PE_ID: 2022010400280001, menu: ICED_AMERICANO
[INFO | main_logic.py:535]	2022-01-04 17:51:46,163	> Event on_barcode_listener called. Barcode: 2022010400280001
[INFO | main_logic.py:543]	2022-01-04 17:51:46,165	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-04 17:51:46,165	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-04 17:51:46,169	> Barcode: 2022010400280001, PE ID: 2022010400280001, Compare: True
[INFO | main_logic.py:547]	2022-01-04 17:51:46,171	> Expired: False
[INFO | main_logic.py:543]	2022-01-04 17:51:46,174	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-04 17:51:50,686	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-04 17:51:51,678	> Removed cup by customer. Index: 1
[DEBUG | main_logic.py:234]	2022-01-04 17:51:56,440	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010400280001, menu: ICED_AMERICANO
[INFO | main_logic.py:458]	2022-01-04 17:52:15,004	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:448]	2022-01-04 17:52:15,005	> Trying to clean filter - idx: 1 ...
[INFO | main_logic.py:458]	2022-01-04 17:52:55,553	> Trying to clean filter - idx: 1 ... Done.
[INFO | main_logic.py:460]	2022-01-04 17:52:55,554	> Logic state <CLEAN> finish.
[INFO | main_logic.py:319]	2022-01-04 17:52:55,655	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-04 17:52:55,756	> Logic state <CLEAN> begin.
[INFO | main_logic.py:460]	2022-01-04 17:52:55,757	> Logic state <CLEAN> finish.
[WARNING | main_logic.py:129]	2022-01-04 17:58:03,599	> Stop button pushed. Requesting stop entire program from the co-routine in the main logic process.
[INFO | process_handler.py:81]	2022-01-04 17:58:03,657	> Shutting down...
[INFO | process_handler.py:86]	2022-01-04 17:58:03,658	> Disposing device 'Kiosk'...
[INFO | kiosk.py:94]	2022-01-04 17:58:03,659	> Kiosk - OnDispose
[INFO | kiosk.py:94]	2022-01-04 17:58:03,660	> Kiosk - Trying to disconnect to Database.
[INFO | kiosk.py:94]	2022-01-04 17:58:03,663	> Kiosk - Successfully disconnected to Database.
[INFO | kiosk.py:94]	2022-01-04 17:58:03,664	> Kiosk - OnDispose Done.
[INFO | process_handler.py:88]	2022-01-04 17:58:03,665	> Successfully disposed device 'Kiosk'
[INFO | process_handler.py:86]	2022-01-04 17:58:03,665	> Disposing device 'IceDispenser'...
[INFO | process_handler.py:88]	2022-01-04 17:58:03,666	> Successfully disposed device 'IceDispenser'
[INFO | process_handler.py:86]	2022-01-04 17:58:03,667	> Disposing device 'CupDispenser'...
[INFO | process_handler.py:88]	2022-01-04 17:58:03,675	> Successfully disposed device 'CupDispenser'
[INFO | process_handler.py:86]	2022-01-04 17:58:03,676	> Disposing device 'BarcodeReader'...
[INFO | barcode_reader.py:35]	2022-01-04 17:58:03,677	> BarcodeReader - OnDispose
[INFO | barcode_reader.py:37]	2022-01-04 17:58:03,677	> barcode thread end
[INFO | process_handler.py:88]	2022-01-04 17:58:03,678	> Successfully disposed device 'BarcodeReader'
[INFO | process_handler.py:94]	2022-01-04 17:58:03,682	> Shutting down...Done.
[INFO | process_handler.py:33]	2022-01-04 17:58:22,403	> Configurations_
{'robot_dof': 6, 'db_host': '192.168.10.22', 'db_name': 'KIOSK', 'db_user': 'NEUROMEKA', 'db_pwd': 'NEUROMEKA1234', 'db_timeout': 5, 'db_login_timeout': 5, 'db_charset': 'utf8', 'ice_only': 4, 'water_only': 0, 'ice_and_water': 1, 'coffee_map': {'00000001': 0, '00000002': 3, '00000003': 4, '00000004': 1, '00000005': 5, '00000006': 2}, 'coffee_expiry_time': 600, 'cup_disp_packet_len': 11, 'ice_disp_packet_len': 5, 'milk_refresh_duration': 4800, 'lift_delay': 2, 'lift_cup_delay': 1, 'espresso_machine_shot_delay_1': 6, 'espresso_machine_shot_delay_2': 6, 'espresso_machine_long_delay_1': 12, 'espresso_machine_long_delay_2': 12}
[INFO | process_handler.py:33]	2022-01-04 17:59:26,431	> Configurations_
{'robot_dof': 6, 'db_host': '192.168.10.22', 'db_name': 'KIOSK', 'db_user': 'NEUROMEKA', 'db_pwd': 'NEUROMEKA1234', 'db_timeout': 5, 'db_login_timeout': 5, 'db_charset': 'utf8', 'ice_only': 4, 'water_only': 0, 'ice_and_water': 1, 'coffee_map': {'00000001': 0, '00000002': 3, '00000003': 4, '00000004': 1, '00000005': 5, '00000006': 2}, 'coffee_expiry_time': 600, 'cup_disp_packet_len': 11, 'ice_disp_packet_len': 5, 'milk_refresh_duration': 4800, 'lift_delay': 2, 'lift_cup_delay': 1, 'espresso_machine_shot_delay_1': 6, 'espresso_machine_shot_delay_2': 6, 'espresso_machine_long_delay_1': 12, 'espresso_machine_long_delay_2': 12}
[INFO | process_handler.py:98]	2022-01-04 17:59:35,852	> Program started.
[INFO | process_handler.py:43]	2022-01-04 17:59:35,854	> Preparing program...
[INFO | process_handler.py:52]	2022-01-04 17:59:35,858	> initializing device '<class 'devices.kiosk.Kiosk'>'...
[DEBUG | process_handler.py:58]	2022-01-04 17:59:35,859	> Called on_create of device '<class 'devices.kiosk.Kiosk'>'
[INFO | kiosk.py:94]	2022-01-04 17:59:35,860	> Kiosk - OnCreate
[INFO | kiosk.py:94]	2022-01-04 17:59:35,860	> Kiosk - Trying to connect to Database - host: 192.168.10.22, db: KIOSK.
[INFO | kiosk.py:94]	2022-01-04 17:59:35,917	> Kiosk - Successfully connected to Database.
[INFO | kiosk.py:94]	2022-01-04 17:59:35,917	> Kiosk - OnCreate Done.
[DEBUG | process_handler.py:60]	2022-01-04 17:59:35,918	> on_create of device '<class 'devices.kiosk.Kiosk'>' done.
[INFO | process_handler.py:63]	2022-01-04 17:59:35,919	> Successfully initialized. Device name: Kiosk
[INFO | process_handler.py:52]	2022-01-04 17:59:35,920	> initializing device '<class 'devices.ice_disp.IceDispenser'>'...
[DEBUG | process_handler.py:58]	2022-01-04 17:59:35,920	> Called on_create of device '<class 'devices.ice_disp.IceDispenser'>'
[DEBUG | process_handler.py:60]	2022-01-04 17:59:35,923	> on_create of device '<class 'devices.ice_disp.IceDispenser'>' done.
[INFO | process_handler.py:63]	2022-01-04 17:59:35,923	> Successfully initialized. Device name: IceDispenser
[INFO | process_handler.py:52]	2022-01-04 17:59:35,924	> initializing device '<class 'devices.cup_disp.CupDispenser'>'...
[DEBUG | process_handler.py:58]	2022-01-04 17:59:35,925	> Called on_create of device '<class 'devices.cup_disp.CupDispenser'>'
[DEBUG | process_handler.py:60]	2022-01-04 17:59:35,928	> on_create of device '<class 'devices.cup_disp.CupDispenser'>' done.
[INFO | process_handler.py:63]	2022-01-04 17:59:35,929	> Successfully initialized. Device name: CupDispenser
[INFO | process_handler.py:52]	2022-01-04 17:59:35,930	> initializing device '<class 'devices.barcode_reader.BarcodeReader'>'...
[DEBUG | process_handler.py:58]	2022-01-04 17:59:35,931	> Called on_create of device '<class 'devices.barcode_reader.BarcodeReader'>'
[INFO | barcode_reader.py:26]	2022-01-04 17:59:35,931	> BarcodeReader - OnCreate
[INFO | barcode_reader.py:30]	2022-01-04 17:59:35,933	> barcode thread start
[DEBUG | process_handler.py:60]	2022-01-04 17:59:35,935	> on_create of device '<class 'devices.barcode_reader.BarcodeReader'>' done.
[INFO | process_handler.py:63]	2022-01-04 17:59:35,936	> Successfully initialized. Device name: BarcodeReader
[INFO | process_handler.py:75]	2022-01-04 17:59:35,938	> Preparing program...Done.
[INFO | main_logic.py:526]	2022-01-04 18:00:16,172	> Event on_kiosk_listener called. New Menu: ICED_AMERICANO, PEID: 2022010400290001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-04 18:00:19,095	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-04 18:00:19,100	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb5f8d10c>
[INFO | main_logic.py:567]	2022-01-04 18:01:02,526	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-04 18:01:02,622	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-04 18:01:02,623	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-04 18:01:02,724	> Logic state <RECIPE> begin.
[INFO | ice_disp.py:48]	2022-01-04 18:01:06,258	> Event occurred! Event Type: 0, Args: <logics.coffee.Coffee object at 0xb5f8d10c>
[INFO | ice_disp.py:50]	2022-01-04 18:01:06,259	> ice serial is already opend!
[INFO | ice_disp.py:106]	2022-01-04 18:01:06,261	> Called CheckIceDispenser
[INFO | ice_disp.py:107]	2022-01-04 18:01:06,262	> ice status check: {packet}
[INFO | ice_disp.py:116]	2022-01-04 18:01:06,274	> Try read packet...
[INFO | ice_disp.py:120]	2022-01-04 18:01:06,278	> reconnet to serialIceDispenser...
[INFO | ice_disp.py:176]	2022-01-04 18:01:06,345	> status check done
[INFO | ice_disp.py:48]	2022-01-04 18:01:13,284	> Event occurred! Event Type: 1, Args: None
[INFO | ice_disp.py:50]	2022-01-04 18:01:13,287	> ice serial is already opend!
[INFO | ice_disp.py:61]	2022-01-04 18:01:13,570	> Close icedisp serial done
[INFO | main_logic.py:363]	2022-01-04 18:01:22,249	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-04 18:01:33,564	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-04 18:01:33,966	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-04 18:01:34,067	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-04 18:01:34,068	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-04 18:01:44,664	> di idx 11 : 1
[INFO | main_logic.py:409]	2022-01-04 18:01:50,088	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-04 18:01:50,090	> Set order state to DONE. PE_ID:2022010400290001
[INFO | main_logic.py:435]	2022-01-04 18:01:50,093	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-04 18:01:50,094	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-04 18:01:50,195	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-04 18:01:50,296	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-04 18:01:50,296	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-04 18:02:04,438	> Event on_barcode_listener called. Barcode: 2022010400290001
[INFO | main_logic.py:543]	2022-01-04 18:02:04,439	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-04 18:02:04,441	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-04 18:02:04,443	> Barcode: 2022010400290001, PE ID: 2022010400290001, Compare: True
[INFO | main_logic.py:547]	2022-01-04 18:02:04,445	> Expired: False
[INFO | main_logic.py:543]	2022-01-04 18:02:04,448	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-04 18:02:08,155	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-04 18:02:09,153	> Removed cup by customer. Index: 1
[DEBUG | main_logic.py:234]	2022-01-04 18:02:13,924	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010400290001, menu: ICED_AMERICANO
[INFO | main_logic.py:241]	2022-01-04 18:02:13,927	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010400290001, menu: ICED_AMERICANO
[INFO | main_logic.py:458]	2022-01-04 18:02:24,338	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-04 18:02:24,339	> Logic state <CLEAN> finish.
[INFO | main_logic.py:526]	2022-01-04 18:31:40,180	> Event on_kiosk_listener called. New Menu: ICED_AMERICANO, PEID: 2022010400330001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-04 18:31:44,189	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-04 18:31:44,216	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb45f5c8c>
[INFO | main_logic.py:567]	2022-01-04 18:32:27,667	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-04 18:32:27,721	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-04 18:32:27,721	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-04 18:32:27,822	> Logic state <RECIPE> begin.
[INFO | ice_disp.py:48]	2022-01-04 18:32:31,352	> Event occurred! Event Type: 0, Args: <logics.coffee.Coffee object at 0xb45f5c8c>
[INFO | ice_disp.py:53]	2022-01-04 18:32:31,358	> create new icedisp serial
[INFO | ice_disp.py:106]	2022-01-04 18:32:31,359	> Called CheckIceDispenser
[INFO | ice_disp.py:107]	2022-01-04 18:32:31,360	> ice status check: {packet}
[INFO | ice_disp.py:116]	2022-01-04 18:32:31,371	> Try read packet...
[INFO | ice_disp.py:120]	2022-01-04 18:32:31,376	> reconnet to serialIceDispenser...
[INFO | ice_disp.py:176]	2022-01-04 18:32:31,442	> status check done
[INFO | ice_disp.py:48]	2022-01-04 18:32:38,376	> Event occurred! Event Type: 1, Args: None
[INFO | ice_disp.py:50]	2022-01-04 18:32:38,376	> ice serial is already opend!
[INFO | ice_disp.py:61]	2022-01-04 18:32:38,665	> Close icedisp serial done
[INFO | main_logic.py:363]	2022-01-04 18:32:47,348	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-04 18:32:58,685	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-04 18:32:59,065	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-04 18:32:59,166	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-04 18:32:59,167	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-04 18:33:09,828	> di idx 11 : 1
[INFO | main_logic.py:409]	2022-01-04 18:33:15,187	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-04 18:33:15,189	> Set order state to DONE. PE_ID:2022010400330001
[INFO | main_logic.py:435]	2022-01-04 18:33:15,192	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-04 18:33:15,192	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-04 18:33:15,294	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-04 18:33:15,395	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-04 18:33:15,395	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-04 18:33:23,248	> Event on_barcode_listener called. Barcode: 2022010400330001
[INFO | main_logic.py:543]	2022-01-04 18:33:23,249	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-04 18:33:23,251	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-04 18:33:23,254	> Barcode: 2022010400330001, PE ID: 2022010400330001, Compare: True
[INFO | main_logic.py:547]	2022-01-04 18:33:23,257	> Expired: False
[INFO | main_logic.py:543]	2022-01-04 18:33:23,261	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-04 18:33:27,193	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-04 18:33:28,153	> Removed cup by customer. Index: 1
[INFO | main_logic.py:172]	2022-01-04 18:33:29,104	> di idx 11 : 1
[INFO | main_logic.py:172]	2022-01-04 18:33:29,186	> di idx 11 : 0
[DEBUG | main_logic.py:234]	2022-01-04 18:33:34,007	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010400330001, menu: ICED_AMERICANO
[INFO | main_logic.py:241]	2022-01-04 18:33:34,012	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010400330001, menu: ICED_AMERICANO
[INFO | main_logic.py:458]	2022-01-04 18:33:49,437	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-04 18:33:49,438	> Logic state <CLEAN> finish.
[INFO | main_logic.py:526]	2022-01-04 19:04:12,574	> Event on_kiosk_listener called. New Menu: ICED_AMERICANO, PEID: 2022010400340001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-04 19:04:13,169	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-04 19:04:13,186	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb5f8d1cc>
[INFO | main_logic.py:567]	2022-01-04 19:04:56,626	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-04 19:04:56,697	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-04 19:04:56,697	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-04 19:04:56,799	> Logic state <RECIPE> begin.
[INFO | ice_disp.py:48]	2022-01-04 19:05:00,306	> Event occurred! Event Type: 0, Args: <logics.coffee.Coffee object at 0xb5f8d1cc>
[INFO | ice_disp.py:53]	2022-01-04 19:05:00,313	> create new icedisp serial
[INFO | ice_disp.py:106]	2022-01-04 19:05:00,314	> Called CheckIceDispenser
[INFO | ice_disp.py:107]	2022-01-04 19:05:00,315	> ice status check: {packet}
[INFO | ice_disp.py:116]	2022-01-04 19:05:00,325	> Try read packet...
[INFO | ice_disp.py:120]	2022-01-04 19:05:00,331	> reconnet to serialIceDispenser...
[INFO | ice_disp.py:176]	2022-01-04 19:05:00,398	> status check done
[INFO | ice_disp.py:48]	2022-01-04 19:05:07,277	> Event occurred! Event Type: 1, Args: None
[INFO | ice_disp.py:50]	2022-01-04 19:05:07,279	> ice serial is already opend!
[INFO | ice_disp.py:61]	2022-01-04 19:05:07,572	> Close icedisp serial done
[INFO | main_logic.py:363]	2022-01-04 19:05:16,124	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-04 19:05:27,441	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-04 19:05:27,842	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-04 19:05:27,943	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-04 19:05:27,944	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-04 19:05:38,579	> di idx 11 : 1
[INFO | main_logic.py:409]	2022-01-04 19:05:43,963	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-04 19:05:43,965	> Set order state to DONE. PE_ID:2022010400340001
[INFO | main_logic.py:435]	2022-01-04 19:05:43,967	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-04 19:05:43,968	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-04 19:05:44,069	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-04 19:05:44,170	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-04 19:05:44,171	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-04 19:06:04,593	> Event on_barcode_listener called. Barcode: 2022010400340001
[INFO | main_logic.py:543]	2022-01-04 19:06:04,594	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-04 19:06:04,597	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-04 19:06:04,598	> Barcode: 2022010400340001, PE ID: 2022010400340001, Compare: True
[INFO | main_logic.py:547]	2022-01-04 19:06:04,600	> Expired: False
[INFO | main_logic.py:543]	2022-01-04 19:06:04,605	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-04 19:06:08,908	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-04 19:06:09,900	> Removed cup by customer. Index: 1
[DEBUG | main_logic.py:234]	2022-01-04 19:06:14,624	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010400340001, menu: ICED_AMERICANO
[INFO | main_logic.py:241]	2022-01-04 19:06:14,628	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010400340001, menu: ICED_AMERICANO
[INFO | main_logic.py:458]	2022-01-04 19:06:18,211	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-04 19:06:18,212	> Logic state <CLEAN> finish.
[INFO | main_logic.py:572]	2022-01-04 19:17:59,221	> Refresh milk called, but
[INFO | main_logic.py:526]	2022-01-04 19:37:30,497	> Event on_kiosk_listener called. New Menu: ICED_AMERICANO, PEID: 2022010400350001, OJ_NO: 1
[INFO | main_logic.py:526]	2022-01-04 19:37:30,501	> Event on_kiosk_listener called. New Menu: ICED_AMERICANO, PEID: 2022010400350001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-04 19:37:34,218	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-04 19:37:34,227	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb45f5fac>
[INFO | main_logic.py:567]	2022-01-04 19:38:17,681	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-04 19:38:17,744	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-04 19:38:17,745	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-04 19:38:17,846	> Logic state <RECIPE> begin.
[INFO | ice_disp.py:48]	2022-01-04 19:38:21,365	> Event occurred! Event Type: 0, Args: <logics.coffee.Coffee object at 0xb45f5fac>
[INFO | ice_disp.py:53]	2022-01-04 19:38:21,372	> create new icedisp serial
[INFO | ice_disp.py:106]	2022-01-04 19:38:21,373	> Called CheckIceDispenser
[INFO | ice_disp.py:107]	2022-01-04 19:38:21,374	> ice status check: {packet}
[INFO | ice_disp.py:116]	2022-01-04 19:38:21,384	> Try read packet...
[INFO | ice_disp.py:120]	2022-01-04 19:38:21,388	> reconnet to serialIceDispenser...
[INFO | ice_disp.py:176]	2022-01-04 19:38:21,454	> status check done
[INFO | ice_disp.py:48]	2022-01-04 19:38:28,336	> Event occurred! Event Type: 1, Args: None
[INFO | ice_disp.py:50]	2022-01-04 19:38:28,338	> ice serial is already opend!
[INFO | ice_disp.py:61]	2022-01-04 19:38:28,629	> Close icedisp serial done
[INFO | main_logic.py:363]	2022-01-04 19:38:37,169	> Logic state <RECIPE> finish.
[INFO | main_logic.py:304]	2022-01-04 19:38:37,270	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-04 19:38:37,280	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb45f5fcc>
[INFO | main_logic.py:554]	2022-01-04 19:38:48,498	> Event on_coffee_done called.
[INFO | main_logic.py:567]	2022-01-04 19:39:18,258	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-04 19:39:18,292	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-04 19:39:18,292	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-04 19:39:18,393	> Logic state <RECIPE> begin.
[INFO | ice_disp.py:48]	2022-01-04 19:39:21,920	> Event occurred! Event Type: 0, Args: <logics.coffee.Coffee object at 0xb45f5fcc>
[INFO | ice_disp.py:53]	2022-01-04 19:39:21,927	> create new icedisp serial
[INFO | ice_disp.py:106]	2022-01-04 19:39:21,928	> Called CheckIceDispenser
[INFO | ice_disp.py:107]	2022-01-04 19:39:21,929	> ice status check: {packet}
[INFO | ice_disp.py:116]	2022-01-04 19:39:21,940	> Try read packet...
[INFO | ice_disp.py:120]	2022-01-04 19:39:21,943	> reconnet to serialIceDispenser...
[INFO | ice_disp.py:176]	2022-01-04 19:39:22,009	> status check done
[INFO | ice_disp.py:48]	2022-01-04 19:39:28,950	> Event occurred! Event Type: 1, Args: None
[INFO | ice_disp.py:50]	2022-01-04 19:39:28,952	> ice serial is already opend!
[INFO | ice_disp.py:61]	2022-01-04 19:39:29,233	> Close icedisp serial done
[INFO | main_logic.py:363]	2022-01-04 19:39:36,918	> Logic state <RECIPE> finish.
[INFO | main_logic.py:315]	2022-01-04 19:39:37,020	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-04 19:39:37,121	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-04 19:39:37,122	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-04 19:39:47,780	> di idx 11 : 1
[INFO | main_logic.py:554]	2022-01-04 19:39:48,075	> Event on_coffee_done called.
[INFO | main_logic.py:535]	2022-01-04 19:39:49,783	> Event on_barcode_listener called. Barcode: 2022010400350001
[INFO | main_logic.py:543]	2022-01-04 19:39:49,786	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-04 19:39:49,788	> State: False, The slot[1] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-04 19:39:49,791	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:409]	2022-01-04 19:39:53,142	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-04 19:39:53,143	> Set order state to DONE. PE_ID:2022010400350001
[INFO | main_logic.py:435]	2022-01-04 19:39:53,145	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-04 19:39:53,146	> Logic state <LIFT> finish.
[INFO | main_logic.py:315]	2022-01-04 19:39:53,248	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-04 19:39:53,349	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-04 19:39:53,350	> CM Slot[1] -> Lift Slot[2]
[INFO | main_logic.py:535]	2022-01-04 19:39:54,458	> Event on_barcode_listener called. Barcode: 2022010400350001
[INFO | main_logic.py:543]	2022-01-04 19:39:54,459	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-04 19:39:54,461	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-04 19:39:54,462	> Barcode: 2022010400350001, PE ID: 2022010400350001, Compare: True
[INFO | main_logic.py:547]	2022-01-04 19:39:54,464	> Expired: False
[INFO | main_logic.py:543]	2022-01-04 19:39:54,469	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:535]	2022-01-04 19:39:55,337	> Event on_barcode_listener called. Barcode: 2022010400350001
[INFO | main_logic.py:543]	2022-01-04 19:39:55,338	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-04 19:39:55,341	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-04 19:39:55,343	> Barcode: 2022010400350001, PE ID: 2022010400350001, Compare: True
[INFO | main_logic.py:547]	2022-01-04 19:39:55,343	> Expired: False
[INFO | main_logic.py:543]	2022-01-04 19:39:55,348	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-04 19:39:59,096	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-04 19:40:00,097	> Removed cup by customer. Index: 1
[DEBUG | main_logic.py:234]	2022-01-04 19:40:04,887	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010400350001, menu: ICED_AMERICANO
[INFO | main_logic.py:244]	2022-01-04 19:40:04,891	> State changed [2] -> [1], lift_index: 1, PE_ID: 2022010400350001, menu: ICED_AMERICANO
[INFO | main_logic.py:172]	2022-01-04 19:40:06,158	> di idx 12 : 1
[INFO | main_logic.py:409]	2022-01-04 19:40:11,873	> CM Slot[1] -> Lift Slot[2] - Logically done.
[INFO | main_logic.py:419]	2022-01-04 19:40:11,875	> Set order state to DONE. PE_ID:2022010400350001
[INFO | main_logic.py:435]	2022-01-04 19:40:11,877	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-04 19:40:11,878	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-04 19:40:11,979	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-04 19:40:12,081	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-04 19:40:12,081	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-04 19:40:14,227	> Event on_barcode_listener called. Barcode: 2022010400350001
[INFO | main_logic.py:543]	2022-01-04 19:40:14,228	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-04 19:40:14,229	> State: False, The slot[1] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-04 19:40:14,232	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-04 19:40:14,235	> Barcode: 2022010400350001, PE ID: 2022010400350001, Compare: True
[INFO | main_logic.py:547]	2022-01-04 19:40:14,235	> Expired: False
[INFO | main_logic.py:535]	2022-01-04 19:40:14,960	> Event on_barcode_listener called. Barcode: 2022010400350001
[INFO | main_logic.py:543]	2022-01-04 19:40:14,963	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-04 19:40:14,963	> State: False, The slot[1] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-04 19:40:14,965	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-04 19:40:14,966	> Barcode: 2022010400350001, PE ID: 2022010400350001, Compare: True
[INFO | main_logic.py:547]	2022-01-04 19:40:14,968	> Expired: False
[INFO | main_logic.py:172]	2022-01-04 19:40:18,423	> di idx 12 : 0
[INFO | main_logic.py:203]	2022-01-04 19:40:19,415	> Removed cup by customer. Index: 2
[DEBUG | main_logic.py:234]	2022-01-04 19:40:24,378	> Removing Coffee confirmed : lift_index: 2, PE_ID: 2022010400350001, menu: ICED_AMERICANO
[INFO | main_logic.py:241]	2022-01-04 19:40:24,381	> State changed [2] -> [3], lift_index: 2, PE_ID: 2022010400350001, menu: ICED_AMERICANO
[INFO | main_logic.py:458]	2022-01-04 19:40:46,122	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:448]	2022-01-04 19:40:46,122	> Trying to clean filter - idx: 1 ...
[INFO | main_logic.py:458]	2022-01-04 19:41:26,672	> Trying to clean filter - idx: 1 ... Done.
[INFO | main_logic.py:460]	2022-01-04 19:41:26,672	> Logic state <CLEAN> finish.
[INFO | main_logic.py:319]	2022-01-04 19:41:26,774	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-04 19:41:26,874	> Logic state <CLEAN> begin.
[INFO | main_logic.py:460]	2022-01-04 19:41:26,875	> Logic state <CLEAN> finish.
[INFO | main_logic.py:526]	2022-01-04 19:45:06,259	> Event on_kiosk_listener called. New Menu: ICED_AMERICANO, PEID: 2022010400360001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-04 19:45:07,672	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-04 19:45:07,678	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb45f552c>
[INFO | main_logic.py:567]	2022-01-04 19:45:51,087	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-04 19:45:51,096	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-04 19:45:51,097	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-04 19:45:51,198	> Logic state <RECIPE> begin.
[INFO | ice_disp.py:48]	2022-01-04 19:45:54,731	> Event occurred! Event Type: 0, Args: <logics.coffee.Coffee object at 0xb45f552c>
[INFO | ice_disp.py:53]	2022-01-04 19:45:54,737	> create new icedisp serial
[INFO | ice_disp.py:106]	2022-01-04 19:45:54,738	> Called CheckIceDispenser
[INFO | ice_disp.py:107]	2022-01-04 19:45:54,739	> ice status check: {packet}
[INFO | ice_disp.py:116]	2022-01-04 19:45:54,750	> Try read packet...
[INFO | ice_disp.py:120]	2022-01-04 19:45:54,753	> reconnet to serialIceDispenser...
[INFO | ice_disp.py:176]	2022-01-04 19:45:54,818	> status check done
[INFO | ice_disp.py:48]	2022-01-04 19:46:01,748	> Event occurred! Event Type: 1, Args: None
[INFO | ice_disp.py:50]	2022-01-04 19:46:01,750	> ice serial is already opend!
[INFO | ice_disp.py:61]	2022-01-04 19:46:02,042	> Close icedisp serial done
[INFO | main_logic.py:363]	2022-01-04 19:46:10,723	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-04 19:46:22,061	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-04 19:46:22,440	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-04 19:46:22,542	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-04 19:46:22,543	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-04 19:46:33,198	> di idx 11 : 1
[INFO | main_logic.py:409]	2022-01-04 19:46:38,565	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-04 19:46:38,566	> Set order state to DONE. PE_ID:2022010400360001
[INFO | main_logic.py:435]	2022-01-04 19:46:38,569	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-04 19:46:38,570	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-04 19:46:38,671	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-04 19:46:38,772	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-04 19:46:38,773	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:458]	2022-01-04 19:47:12,815	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-04 19:47:12,816	> Logic state <CLEAN> finish.
[INFO | main_logic.py:535]	2022-01-04 19:47:25,777	> Event on_barcode_listener called. Barcode: 2022010400360001
[INFO | main_logic.py:543]	2022-01-04 19:47:25,778	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-04 19:47:25,780	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-04 19:47:25,782	> Barcode: 2022010400360001, PE ID: 2022010400360001, Compare: True
[INFO | main_logic.py:547]	2022-01-04 19:47:25,783	> Expired: False
[INFO | main_logic.py:543]	2022-01-04 19:47:25,788	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-04 19:47:29,332	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-04 19:47:30,331	> Removed cup by customer. Index: 1
[DEBUG | main_logic.py:234]	2022-01-04 19:47:36,332	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010400360001, menu: ICED_AMERICANO
[INFO | main_logic.py:241]	2022-01-04 19:47:36,334	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010400360001, menu: ICED_AMERICANO
[INFO | main_logic.py:526]	2022-01-04 20:27:13,621	> Event on_kiosk_listener called. New Menu: ICED_AMERICANO, PEID: 2022010400370001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-04 20:27:17,326	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-04 20:27:17,337	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb5f8daec>
[INFO | main_logic.py:567]	2022-01-04 20:28:00,742	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-04 20:28:00,753	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-04 20:28:00,754	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-04 20:28:00,855	> Logic state <RECIPE> begin.
[INFO | ice_disp.py:48]	2022-01-04 20:28:04,388	> Event occurred! Event Type: 0, Args: <logics.coffee.Coffee object at 0xb5f8daec>
[INFO | ice_disp.py:53]	2022-01-04 20:28:04,395	> create new icedisp serial
[INFO | ice_disp.py:106]	2022-01-04 20:28:04,396	> Called CheckIceDispenser
[INFO | ice_disp.py:107]	2022-01-04 20:28:04,397	> ice status check: {packet}
[INFO | ice_disp.py:116]	2022-01-04 20:28:04,408	> Try read packet...
[INFO | ice_disp.py:120]	2022-01-04 20:28:04,411	> reconnet to serialIceDispenser...
[INFO | ice_disp.py:176]	2022-01-04 20:28:04,477	> status check done
[INFO | ice_disp.py:48]	2022-01-04 20:28:11,404	> Event occurred! Event Type: 1, Args: None
[INFO | ice_disp.py:50]	2022-01-04 20:28:11,406	> ice serial is already opend!
[INFO | ice_disp.py:61]	2022-01-04 20:28:11,703	> Close icedisp serial done
[INFO | main_logic.py:363]	2022-01-04 20:28:20,381	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-04 20:28:31,719	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-04 20:28:32,097	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-04 20:28:32,198	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-04 20:28:32,199	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-04 20:28:42,765	> di idx 11 : 1
[INFO | main_logic.py:409]	2022-01-04 20:28:48,220	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-04 20:28:48,222	> Set order state to DONE. PE_ID:2022010400370001
[INFO | main_logic.py:435]	2022-01-04 20:28:48,224	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-04 20:28:48,225	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-04 20:28:48,326	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-04 20:28:48,428	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-04 20:28:48,428	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-04 20:29:05,885	> Event on_barcode_listener called. Barcode: 2022010400370001
[INFO | main_logic.py:543]	2022-01-04 20:29:05,888	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-04 20:29:05,890	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-04 20:29:05,892	> Barcode: 2022010400370001, PE ID: 2022010400370001, Compare: True
[INFO | main_logic.py:547]	2022-01-04 20:29:05,895	> Expired: False
[INFO | main_logic.py:543]	2022-01-04 20:29:05,898	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-04 20:29:12,275	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-04 20:29:13,242	> Removed cup by customer. Index: 1
[DEBUG | main_logic.py:234]	2022-01-04 20:29:17,866	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010400370001, menu: ICED_AMERICANO
[INFO | main_logic.py:241]	2022-01-04 20:29:17,870	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010400370001, menu: ICED_AMERICANO
[INFO | main_logic.py:458]	2022-01-04 20:29:22,468	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-04 20:29:22,468	> Logic state <CLEAN> finish.
[INFO | main_logic.py:572]	2022-01-04 20:36:22,741	> Refresh milk called, but
[INFO | main_logic.py:526]	2022-01-04 20:45:48,782	> Event on_kiosk_listener called. New Menu: AMERICANO, PEID: 2022010400380001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-04 20:45:49,874	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-04 20:45:49,885	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb458a5ec>
[INFO | main_logic.py:567]	2022-01-04 20:46:32,888	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-04 20:46:32,899	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-04 20:46:32,900	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-04 20:46:33,001	> Logic state <RECIPE> begin.
[INFO | main_logic.py:363]	2022-01-04 20:46:55,832	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-04 20:47:07,148	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-04 20:47:07,550	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-04 20:47:07,651	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-04 20:47:07,652	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-04 20:47:18,101	> di idx 11 : 1
[INFO | main_logic.py:409]	2022-01-04 20:47:23,673	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-04 20:47:23,674	> Set order state to DONE. PE_ID:2022010400380001
[INFO | main_logic.py:435]	2022-01-04 20:47:23,677	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-04 20:47:23,677	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-04 20:47:23,779	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-04 20:47:23,880	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-04 20:47:23,881	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-04 20:47:31,009	> Event on_barcode_listener called. Barcode: 2022010400380001
[INFO | main_logic.py:543]	2022-01-04 20:47:31,012	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-04 20:47:31,013	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-04 20:47:31,015	> Barcode: 2022010400380001, PE ID: 2022010400380001, Compare: True
[INFO | main_logic.py:547]	2022-01-04 20:47:31,015	> Expired: False
[INFO | main_logic.py:543]	2022-01-04 20:47:31,020	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:458]	2022-01-04 20:47:57,923	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-04 20:47:57,924	> Logic state <CLEAN> finish.
[INFO | main_logic.py:172]	2022-01-04 20:48:08,844	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-04 20:48:09,835	> Removed cup by customer. Index: 1
[DEBUG | main_logic.py:234]	2022-01-04 20:48:14,609	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010400380001, menu: AMERICANO
[INFO | main_logic.py:241]	2022-01-04 20:48:14,611	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010400380001, menu: AMERICANO
[INFO | main_logic.py:526]	2022-01-04 21:53:35,900	> Event on_kiosk_listener called. New Menu: AMERICANO, PEID: 2022010400390001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-04 21:53:41,478	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-04 21:53:41,503	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb458a48c>
[INFO | main_logic.py:567]	2022-01-04 21:54:24,509	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-04 21:54:24,609	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-04 21:54:24,610	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-04 21:54:24,711	> Logic state <RECIPE> begin.
[INFO | main_logic.py:572]	2022-01-04 21:54:46,282	> Refresh milk called, but
[INFO | main_logic.py:363]	2022-01-04 21:54:47,543	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-04 21:54:58,883	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-04 21:54:59,262	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-04 21:54:59,364	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-04 21:54:59,364	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-04 21:55:09,802	> di idx 11 : 1
[INFO | main_logic.py:409]	2022-01-04 21:55:15,384	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-04 21:55:15,386	> Set order state to DONE. PE_ID:2022010400390001
[INFO | main_logic.py:435]	2022-01-04 21:55:15,388	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-04 21:55:15,389	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-04 21:55:15,490	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-04 21:55:15,591	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-04 21:55:15,592	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:458]	2022-01-04 21:55:49,633	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-04 21:55:49,634	> Logic state <CLEAN> finish.
[INFO | main_logic.py:172]	2022-01-04 21:56:59,485	> di idx 11 : 0
[INFO | main_logic.py:241]	2022-01-04 21:57:00,479	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010400390001, menu: AMERICANO
[INFO | coffee.py:87]	2022-01-04 22:04:24,573	> Coffee expired. CM Slot: 0, Lift slot: 1, Menu: AMERICANO, PEID: 2022010400390001, OJ_NO: 1
[DEBUG | main_logic.py:230]	2022-01-04 22:04:24,601	> Job appending - TRASH : lift_index: 1, expired: True, menu: AMERICANO
[DEBUG | main_logic.py:234]	2022-01-04 22:04:24,604	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010400390001, menu: AMERICANO
[INFO | main_logic.py:323]	2022-01-04 22:04:26,635	> Logic job retrieved <LogicState.TRASH>.
[INFO | main_logic.py:463]	2022-01-04 22:04:26,736	> Logic state <TRASH> begin.
[INFO | main_logic.py:480]	2022-01-04 22:04:26,737	> Logic state <TRASH> finish.
[INFO | main_logic.py:526]	2022-01-04 22:18:01,771	> Event on_kiosk_listener called. New Menu: AMERICANO, PEID: 2022010400400001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-04 22:18:05,726	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-04 22:18:05,734	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb45f5cec>
[INFO | main_logic.py:567]	2022-01-04 22:18:48,743	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-04 22:18:48,749	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-04 22:18:48,750	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-04 22:18:48,851	> Logic state <RECIPE> begin.
[INFO | main_logic.py:363]	2022-01-04 22:19:11,685	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-04 22:19:23,020	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-04 22:19:23,402	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-04 22:19:23,503	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-04 22:19:23,504	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-04 22:19:33,974	> di idx 11 : 1
[INFO | main_logic.py:409]	2022-01-04 22:19:39,523	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-04 22:19:39,525	> Set order state to DONE. PE_ID:2022010400400001
[INFO | main_logic.py:435]	2022-01-04 22:19:39,528	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-04 22:19:39,528	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-04 22:19:39,630	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-04 22:19:39,731	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-04 22:19:39,731	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-04 22:19:57,354	> Event on_barcode_listener called. Barcode: 2022010400400001
[INFO | main_logic.py:543]	2022-01-04 22:19:57,356	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-04 22:19:57,358	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-04 22:19:57,360	> Barcode: 2022010400400001, PE ID: 2022010400400001, Compare: True
[INFO | main_logic.py:547]	2022-01-04 22:19:57,361	> Expired: False
[INFO | main_logic.py:543]	2022-01-04 22:19:57,366	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-04 22:20:02,124	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-04 22:20:03,116	> Removed cup by customer. Index: 1
[DEBUG | main_logic.py:234]	2022-01-04 22:20:07,972	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010400400001, menu: AMERICANO
[INFO | main_logic.py:241]	2022-01-04 22:20:07,975	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010400400001, menu: AMERICANO
[INFO | main_logic.py:458]	2022-01-04 22:20:13,772	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-04 22:20:13,772	> Logic state <CLEAN> finish.
[INFO | main_logic.py:572]	2022-01-04 23:13:09,870	> Refresh milk called, but
[INFO | main_logic.py:572]	2022-01-05 00:31:33,197	> Refresh milk called, but
[INFO | main_logic.py:572]	2022-01-05 01:49:56,664	> Refresh milk called, but
[INFO | main_logic.py:572]	2022-01-05 03:08:20,122	> Refresh milk called, but
[INFO | main_logic.py:572]	2022-01-05 04:26:43,519	> Refresh milk called, but
[INFO | main_logic.py:572]	2022-01-05 05:45:06,841	> Refresh milk called, but
[INFO | main_logic.py:526]	2022-01-05 06:21:17,166	> Event on_kiosk_listener called. New Menu: AMERICANO, PEID: 2022010500010001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-05 06:21:18,343	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 06:21:18,355	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb45f598c>
[INFO | main_logic.py:535]	2022-01-05 06:21:33,202	> Event on_barcode_listener called. Barcode: 2022010500010001
[INFO | main_logic.py:543]	2022-01-05 06:21:33,204	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-05 06:21:33,205	> State: False, The slot[1] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-05 06:21:33,207	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:567]	2022-01-05 06:22:01,394	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 06:22:01,469	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 06:22:01,470	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 06:22:01,571	> Logic state <RECIPE> begin.
[INFO | main_logic.py:363]	2022-01-05 06:22:24,403	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-05 06:22:35,726	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-05 06:22:36,121	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 06:22:36,222	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 06:22:36,223	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-05 06:22:46,661	> di idx 11 : 1
[INFO | main_logic.py:409]	2022-01-05 06:22:52,241	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 06:22:52,243	> Set order state to DONE. PE_ID:2022010500010001
[INFO | main_logic.py:435]	2022-01-05 06:22:52,245	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 06:22:52,246	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-05 06:22:52,347	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 06:22:52,448	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-05 06:22:52,449	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-05 06:23:11,393	> Event on_barcode_listener called. Barcode: 2022010500010001
[INFO | main_logic.py:543]	2022-01-05 06:23:11,395	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 06:23:11,398	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 06:23:11,399	> Barcode: 2022010500010001, PE ID: 2022010500010001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 06:23:11,401	> Expired: False
[INFO | main_logic.py:543]	2022-01-05 06:23:11,404	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-05 06:23:15,956	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-05 06:23:16,944	> Removed cup by customer. Index: 1
[DEBUG | main_logic.py:234]	2022-01-05 06:23:21,657	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010500010001, menu: AMERICANO
[INFO | main_logic.py:241]	2022-01-05 06:23:21,662	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010500010001, menu: AMERICANO
[INFO | main_logic.py:458]	2022-01-05 06:23:26,490	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-05 06:23:26,491	> Logic state <CLEAN> finish.
[INFO | main_logic.py:572]	2022-01-05 07:03:30,150	> Refresh milk called, but
[INFO | main_logic.py:526]	2022-01-05 07:37:39,178	> Event on_kiosk_listener called. New Menu: AMERICANO, PEID: 2022010500020001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-05 07:37:41,113	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 07:37:41,123	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb45df8cc>
[INFO | main_logic.py:567]	2022-01-05 07:38:24,163	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 07:38:24,245	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 07:38:24,246	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 07:38:24,347	> Logic state <RECIPE> begin.
[INFO | main_logic.py:535]	2022-01-05 07:38:35,586	> Event on_barcode_listener called. Barcode: 2022010500020001
[INFO | main_logic.py:543]	2022-01-05 07:38:35,587	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-05 07:38:35,589	> State: False, The slot[1] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-05 07:38:35,591	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:535]	2022-01-05 07:38:39,372	> Event on_barcode_listener called. Barcode: 2022010500020001
[INFO | main_logic.py:543]	2022-01-05 07:38:39,374	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-05 07:38:39,377	> State: False, The slot[1] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-05 07:38:39,380	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:363]	2022-01-05 07:38:47,180	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-05 07:38:58,518	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-05 07:38:58,897	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 07:38:58,998	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 07:38:58,999	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-05 07:39:09,458	> di idx 11 : 1
[INFO | main_logic.py:409]	2022-01-05 07:39:15,019	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 07:39:15,021	> Set order state to DONE. PE_ID:2022010500020001
[INFO | main_logic.py:435]	2022-01-05 07:39:15,023	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 07:39:15,024	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-05 07:39:15,125	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 07:39:15,226	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-05 07:39:15,227	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-05 07:39:16,710	> Event on_barcode_listener called. Barcode: 2022010500020001
[INFO | main_logic.py:543]	2022-01-05 07:39:16,711	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 07:39:16,713	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 07:39:16,715	> Barcode: 2022010500020001, PE ID: 2022010500020001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 07:39:16,716	> Expired: False
[INFO | main_logic.py:543]	2022-01-05 07:39:16,721	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-05 07:39:21,340	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-05 07:39:22,328	> Removed cup by customer. Index: 1
[DEBUG | main_logic.py:234]	2022-01-05 07:39:27,197	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010500020001, menu: AMERICANO
[INFO | main_logic.py:241]	2022-01-05 07:39:27,201	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010500020001, menu: AMERICANO
[INFO | main_logic.py:458]	2022-01-05 07:39:49,269	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-05 07:39:49,270	> Logic state <CLEAN> finish.
[INFO | main_logic.py:526]	2022-01-05 08:13:48,168	> Event on_kiosk_listener called. New Menu: AMERICANO, PEID: 2022010500030001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-05 08:13:53,713	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 08:13:53,725	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb45df74c>
[INFO | main_logic.py:567]	2022-01-05 08:14:36,733	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 08:14:36,739	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 08:14:36,740	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 08:14:36,841	> Logic state <RECIPE> begin.
[INFO | main_logic.py:363]	2022-01-05 08:14:59,674	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-05 08:15:10,995	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-05 08:15:11,393	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 08:15:11,494	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 08:15:11,495	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-05 08:15:21,993	> di idx 11 : 1
[INFO | main_logic.py:409]	2022-01-05 08:15:27,516	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 08:15:27,518	> Set order state to DONE. PE_ID:2022010500030001
[INFO | main_logic.py:435]	2022-01-05 08:15:27,520	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 08:15:27,521	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-05 08:15:27,622	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 08:15:27,723	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-05 08:15:27,724	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-05 08:15:49,303	> Event on_barcode_listener called. Barcode: 2022010500030001
[INFO | main_logic.py:543]	2022-01-05 08:15:49,304	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 08:15:49,306	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 08:15:49,307	> Barcode: 2022010500030001, PE ID: 2022010500030001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 08:15:49,309	> Expired: False
[INFO | main_logic.py:543]	2022-01-05 08:15:49,313	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-05 08:15:54,773	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-05 08:15:55,766	> Removed cup by customer. Index: 1
[DEBUG | main_logic.py:234]	2022-01-05 08:16:00,548	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010500030001, menu: AMERICANO
[INFO | main_logic.py:241]	2022-01-05 08:16:00,552	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010500030001, menu: AMERICANO
[INFO | main_logic.py:458]	2022-01-05 08:16:01,766	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-05 08:16:01,767	> Logic state <CLEAN> finish.
[INFO | main_logic.py:526]	2022-01-05 08:16:56,959	> Event on_kiosk_listener called. New Menu: AMERICANO, PEID: 2022010500040001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-05 08:16:59,944	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 08:16:59,949	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb45df16c>
[INFO | main_logic.py:567]	2022-01-05 08:17:42,955	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 08:17:42,969	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 08:17:42,969	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 08:17:43,070	> Logic state <RECIPE> begin.
[INFO | main_logic.py:363]	2022-01-05 08:18:05,903	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-05 08:18:17,228	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-05 08:18:17,619	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 08:18:17,721	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 08:18:17,721	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-05 08:18:28,131	> di idx 11 : 1
[INFO | main_logic.py:409]	2022-01-05 08:18:33,740	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 08:18:33,741	> Set order state to DONE. PE_ID:2022010500040001
[INFO | main_logic.py:435]	2022-01-05 08:18:33,744	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 08:18:33,744	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-05 08:18:33,846	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 08:18:33,947	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-05 08:18:33,948	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-05 08:18:39,888	> Event on_barcode_listener called. Barcode: 2022010500040001
[INFO | main_logic.py:543]	2022-01-05 08:18:39,889	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 08:18:39,890	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 08:18:39,892	> Barcode: 2022010500040001, PE ID: 2022010500040001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 08:18:39,894	> Expired: False
[INFO | main_logic.py:543]	2022-01-05 08:18:39,897	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-05 08:18:45,052	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-05 08:18:46,045	> Removed cup by customer. Index: 1
[DEBUG | main_logic.py:234]	2022-01-05 08:18:50,819	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010500040001, menu: AMERICANO
[INFO | main_logic.py:241]	2022-01-05 08:18:50,823	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010500040001, menu: AMERICANO
[INFO | main_logic.py:458]	2022-01-05 08:19:07,991	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-05 08:19:07,992	> Logic state <CLEAN> finish.
[INFO | main_logic.py:572]	2022-01-05 08:21:53,669	> Refresh milk called, but
[INFO | main_logic.py:526]	2022-01-05 08:38:40,756	> Event on_kiosk_listener called. New Menu: ICED_AMERICANO, PEID: 2022010500050001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-05 08:38:41,266	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 08:38:41,283	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb45cad2c>
[INFO | main_logic.py:567]	2022-01-05 08:39:24,718	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 08:39:24,795	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 08:39:24,797	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 08:39:24,898	> Logic state <RECIPE> begin.
[INFO | ice_disp.py:48]	2022-01-05 08:39:28,408	> Event occurred! Event Type: 0, Args: <logics.coffee.Coffee object at 0xb45cad2c>
[INFO | ice_disp.py:53]	2022-01-05 08:39:28,415	> create new icedisp serial
[INFO | ice_disp.py:106]	2022-01-05 08:39:28,416	> Called CheckIceDispenser
[INFO | ice_disp.py:107]	2022-01-05 08:39:28,417	> ice status check: {packet}
[INFO | ice_disp.py:116]	2022-01-05 08:39:28,427	> Try read packet...
[INFO | ice_disp.py:120]	2022-01-05 08:39:28,431	> reconnet to serialIceDispenser...
[INFO | ice_disp.py:176]	2022-01-05 08:39:28,497	> status check done
[INFO | ice_disp.py:48]	2022-01-05 08:39:35,393	> Event occurred! Event Type: 1, Args: None
[INFO | ice_disp.py:50]	2022-01-05 08:39:35,395	> ice serial is already opend!
[INFO | ice_disp.py:61]	2022-01-05 08:39:35,670	> Close icedisp serial done
[INFO | main_logic.py:363]	2022-01-05 08:39:44,223	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-05 08:39:55,538	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-05 08:39:55,939	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 08:39:56,041	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 08:39:56,041	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-05 08:40:06,602	> di idx 11 : 1
[INFO | main_logic.py:409]	2022-01-05 08:40:12,061	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 08:40:12,063	> Set order state to DONE. PE_ID:2022010500050001
[INFO | main_logic.py:435]	2022-01-05 08:40:12,066	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 08:40:12,066	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-05 08:40:12,168	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 08:40:12,269	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-05 08:40:12,270	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-05 08:40:16,103	> Event on_barcode_listener called. Barcode: 2022010500050001
[INFO | main_logic.py:543]	2022-01-05 08:40:16,103	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 08:40:16,106	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 08:40:16,108	> Barcode: 2022010500050001, PE ID: 2022010500050001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 08:40:16,112	> Expired: False
[INFO | main_logic.py:543]	2022-01-05 08:40:16,115	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-05 08:40:20,444	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-05 08:40:21,445	> Removed cup by customer. Index: 1
[DEBUG | main_logic.py:234]	2022-01-05 08:40:26,109	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010500050001, menu: ICED_AMERICANO
[INFO | main_logic.py:241]	2022-01-05 08:40:26,114	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010500050001, menu: ICED_AMERICANO
[INFO | main_logic.py:458]	2022-01-05 08:40:46,312	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-05 08:40:46,313	> Logic state <CLEAN> finish.
[INFO | main_logic.py:526]	2022-01-05 08:53:16,837	> Event on_kiosk_listener called. New Menu: AMERICANO, PEID: 2022010500060001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-05 08:53:21,426	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 08:53:21,439	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb45ded6c>
[INFO | main_logic.py:567]	2022-01-05 08:54:04,465	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 08:54:04,552	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 08:54:04,553	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 08:54:04,654	> Logic state <RECIPE> begin.
[INFO | main_logic.py:363]	2022-01-05 08:54:27,488	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-05 08:54:38,814	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-05 08:54:39,205	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 08:54:39,306	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 08:54:39,307	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-05 08:54:49,743	> di idx 11 : 1
[INFO | main_logic.py:409]	2022-01-05 08:54:55,327	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 08:54:55,328	> Set order state to DONE. PE_ID:2022010500060001
[INFO | main_logic.py:435]	2022-01-05 08:54:55,331	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 08:54:55,332	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-05 08:54:55,433	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 08:54:55,534	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-05 08:54:55,535	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:458]	2022-01-05 08:55:29,576	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-05 08:55:29,577	> Logic state <CLEAN> finish.
[INFO | main_logic.py:535]	2022-01-05 08:55:33,464	> Event on_barcode_listener called. Barcode: 2022010500060001
[INFO | main_logic.py:543]	2022-01-05 08:55:33,467	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 08:55:33,468	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 08:55:33,470	> Barcode: 2022010500060001, PE ID: 2022010500060001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 08:55:33,471	> Expired: False
[INFO | main_logic.py:543]	2022-01-05 08:55:33,476	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-05 08:55:38,124	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-05 08:55:39,113	> Removed cup by customer. Index: 1
[DEBUG | main_logic.py:234]	2022-01-05 08:55:43,920	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010500060001, menu: AMERICANO
[INFO | main_logic.py:241]	2022-01-05 08:55:43,924	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010500060001, menu: AMERICANO
[INFO | main_logic.py:526]	2022-01-05 08:59:52,380	> Event on_kiosk_listener called. New Menu: AMERICANO, PEID: 2022010500070001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-05 08:59:56,835	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 08:59:56,863	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb458a88c>
[INFO | main_logic.py:567]	2022-01-05 09:00:39,915	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 09:00:39,963	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 09:00:39,964	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 09:00:40,066	> Logic state <RECIPE> begin.
[INFO | main_logic.py:363]	2022-01-05 09:01:02,898	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-05 09:01:14,229	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-05 09:01:14,616	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 09:01:14,717	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 09:01:14,718	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-05 09:01:25,145	> di idx 11 : 1
[INFO | main_logic.py:409]	2022-01-05 09:01:30,736	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 09:01:30,737	> Set order state to DONE. PE_ID:2022010500070001
[INFO | main_logic.py:435]	2022-01-05 09:01:30,740	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 09:01:30,741	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-05 09:01:30,842	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 09:01:30,943	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-05 09:01:30,943	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-05 09:01:54,836	> Event on_barcode_listener called. Barcode: 2022010500070001
[INFO | main_logic.py:543]	2022-01-05 09:01:54,837	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 09:01:54,839	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 09:01:54,841	> Barcode: 2022010500070001, PE ID: 2022010500070001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 09:01:54,842	> Expired: False
[INFO | main_logic.py:543]	2022-01-05 09:01:54,846	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-05 09:02:00,160	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-05 09:02:01,155	> Removed cup by customer. Index: 1
[INFO | main_logic.py:458]	2022-01-05 09:02:04,985	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-05 09:02:04,986	> Logic state <CLEAN> finish.
[DEBUG | main_logic.py:234]	2022-01-05 09:02:05,930	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010500070001, menu: AMERICANO
[INFO | main_logic.py:241]	2022-01-05 09:02:05,933	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010500070001, menu: AMERICANO
[INFO | main_logic.py:526]	2022-01-05 09:06:33,728	> Event on_kiosk_listener called. New Menu: AMERICANO, PEID: 2022010500080001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-05 09:06:38,055	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 09:06:38,074	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb458ae8c>
[INFO | main_logic.py:567]	2022-01-05 09:07:21,112	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 09:07:21,181	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 09:07:21,182	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 09:07:21,283	> Logic state <RECIPE> begin.
[INFO | main_logic.py:363]	2022-01-05 09:07:44,116	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-05 09:07:55,437	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-05 09:07:55,833	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 09:07:55,935	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 09:07:55,936	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-05 09:08:06,384	> di idx 11 : 1
[INFO | main_logic.py:535]	2022-01-05 09:08:09,424	> Event on_barcode_listener called. Barcode: 2022010500080001
[INFO | main_logic.py:543]	2022-01-05 09:08:09,425	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-05 09:08:09,428	> State: False, The slot[1] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-05 09:08:09,428	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:409]	2022-01-05 09:08:11,955	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 09:08:11,958	> Set order state to DONE. PE_ID:2022010500080001
[INFO | main_logic.py:435]	2022-01-05 09:08:11,960	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 09:08:11,961	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-05 09:08:12,062	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 09:08:12,163	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-05 09:08:12,164	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-05 09:08:12,303	> Event on_barcode_listener called. Barcode: 2022010500080001
[INFO | main_logic.py:543]	2022-01-05 09:08:12,306	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 09:08:12,308	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 09:08:12,309	> Barcode: 2022010500080001, PE ID: 2022010500080001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 09:08:12,311	> Expired: False
[INFO | main_logic.py:543]	2022-01-05 09:08:12,314	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:535]	2022-01-05 09:08:13,776	> Event on_barcode_listener called. Barcode: 2022010500080001
[INFO | main_logic.py:543]	2022-01-05 09:08:13,777	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 09:08:13,779	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 09:08:13,782	> Barcode: 2022010500080001, PE ID: 2022010500080001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 09:08:13,783	> Expired: False
[INFO | main_logic.py:543]	2022-01-05 09:08:13,786	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:535]	2022-01-05 09:08:14,620	> Event on_barcode_listener called. Barcode: 2022010500080001
[INFO | main_logic.py:543]	2022-01-05 09:08:14,621	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 09:08:14,624	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 09:08:14,627	> Barcode: 2022010500080001, PE ID: 2022010500080001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 09:08:14,630	> Expired: False
[INFO | main_logic.py:543]	2022-01-05 09:08:14,633	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:535]	2022-01-05 09:08:15,468	> Event on_barcode_listener called. Barcode: 2022010500080001
[INFO | main_logic.py:543]	2022-01-05 09:08:15,469	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 09:08:15,471	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 09:08:15,472	> Barcode: 2022010500080001, PE ID: 2022010500080001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 09:08:15,474	> Expired: False
[INFO | main_logic.py:543]	2022-01-05 09:08:15,479	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-05 09:08:18,027	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-05 09:08:19,561	> Removed cup by customer. Index: 1
[DEBUG | main_logic.py:234]	2022-01-05 09:08:24,401	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010500080001, menu: AMERICANO
[INFO | main_logic.py:241]	2022-01-05 09:08:24,403	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010500080001, menu: AMERICANO
[INFO | main_logic.py:458]	2022-01-05 09:08:46,206	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-05 09:08:46,207	> Logic state <CLEAN> finish.
[INFO | main_logic.py:526]	2022-01-05 09:22:13,109	> Event on_kiosk_listener called. New Menu: ICED_AMERICANO, PEID: 2022010500090001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-05 09:22:13,587	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 09:22:13,612	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb45f5b8c>
[INFO | main_logic.py:567]	2022-01-05 09:22:57,038	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 09:22:57,114	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 09:22:57,115	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 09:22:57,216	> Logic state <RECIPE> begin.
[INFO | ice_disp.py:48]	2022-01-05 09:23:00,722	> Event occurred! Event Type: 0, Args: <logics.coffee.Coffee object at 0xb45f5b8c>
[INFO | ice_disp.py:53]	2022-01-05 09:23:00,729	> create new icedisp serial
[INFO | ice_disp.py:106]	2022-01-05 09:23:00,730	> Called CheckIceDispenser
[INFO | ice_disp.py:107]	2022-01-05 09:23:00,731	> ice status check: {packet}
[INFO | ice_disp.py:116]	2022-01-05 09:23:00,741	> Try read packet...
[INFO | ice_disp.py:120]	2022-01-05 09:23:00,745	> reconnet to serialIceDispenser...
[INFO | ice_disp.py:176]	2022-01-05 09:23:00,812	> status check done
[INFO | ice_disp.py:48]	2022-01-05 09:23:07,743	> Event occurred! Event Type: 1, Args: None
[INFO | ice_disp.py:50]	2022-01-05 09:23:07,744	> ice serial is already opend!
[INFO | ice_disp.py:61]	2022-01-05 09:23:08,037	> Close icedisp serial done
[INFO | main_logic.py:363]	2022-01-05 09:23:16,741	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-05 09:23:28,073	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-05 09:23:28,461	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 09:23:28,562	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 09:23:28,563	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-05 09:23:39,168	> di idx 11 : 1
[INFO | main_logic.py:535]	2022-01-05 09:23:43,754	> Event on_barcode_listener called. Barcode: 2022010500090001
[INFO | main_logic.py:543]	2022-01-05 09:23:43,755	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-05 09:23:43,757	> State: False, The slot[1] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-05 09:23:43,760	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:409]	2022-01-05 09:23:44,583	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 09:23:44,585	> Set order state to DONE. PE_ID:2022010500090001
[INFO | main_logic.py:435]	2022-01-05 09:23:44,589	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 09:23:44,590	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-05 09:23:44,691	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 09:23:44,792	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-05 09:23:44,793	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-05 09:23:46,326	> Event on_barcode_listener called. Barcode: 2022010500090001
[INFO | main_logic.py:543]	2022-01-05 09:23:46,329	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 09:23:46,329	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 09:23:46,331	> Barcode: 2022010500090001, PE ID: 2022010500090001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 09:23:46,334	> Expired: False
[INFO | main_logic.py:543]	2022-01-05 09:23:46,337	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-05 09:23:50,651	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-05 09:23:51,608	> Removed cup by customer. Index: 1
[DEBUG | main_logic.py:234]	2022-01-05 09:23:56,495	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010500090001, menu: ICED_AMERICANO
[INFO | main_logic.py:241]	2022-01-05 09:23:56,498	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010500090001, menu: ICED_AMERICANO
[INFO | main_logic.py:526]	2022-01-05 09:24:13,576	> Event on_kiosk_listener called. New Menu: AMERICANO, PEID: 2022010500100001, OJ_NO: 1
[INFO | main_logic.py:526]	2022-01-05 09:24:13,581	> Event on_kiosk_listener called. New Menu: AMERICANO, PEID: 2022010500100001, OJ_NO: 1
[INFO | main_logic.py:526]	2022-01-05 09:24:13,586	> Event on_kiosk_listener called. New Menu: AMERICANO, PEID: 2022010500100001, OJ_NO: 1
[INFO | main_logic.py:526]	2022-01-05 09:24:13,632	> Event on_kiosk_listener called. New Menu: ICED_AMERICANO, PEID: 2022010500100001, OJ_NO: 2
[INFO | main_logic.py:458]	2022-01-05 09:24:18,836	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-05 09:24:18,837	> Logic state <CLEAN> finish.
[INFO | main_logic.py:304]	2022-01-05 09:24:18,938	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 09:24:18,959	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb5f8dc2c>
[INFO | main_logic.py:567]	2022-01-05 09:25:01,977	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 09:25:02,063	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 09:25:02,064	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 09:25:02,165	> Logic state <RECIPE> begin.
[INFO | main_logic.py:363]	2022-01-05 09:25:24,998	> Logic state <RECIPE> finish.
[INFO | main_logic.py:304]	2022-01-05 09:25:25,102	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 09:25:25,124	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb5f8d6ec>
[INFO | main_logic.py:554]	2022-01-05 09:25:36,332	> Event on_coffee_done called.
[INFO | main_logic.py:526]	2022-01-05 09:25:37,186	> Event on_kiosk_listener called. New Menu: AMERICANO, PEID: 2022010500110001, OJ_NO: 1
[INFO | main_logic.py:567]	2022-01-05 09:26:05,691	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 09:26:05,722	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 09:26:05,723	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 09:26:05,824	> Logic state <RECIPE> begin.
[INFO | main_logic.py:363]	2022-01-05 09:26:27,657	> Logic state <RECIPE> finish.
[INFO | main_logic.py:315]	2022-01-05 09:26:27,761	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 09:26:27,862	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 09:26:27,863	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-05 09:26:38,301	> di idx 11 : 1
[INFO | main_logic.py:554]	2022-01-05 09:26:38,815	> Event on_coffee_done called.
[INFO | main_logic.py:409]	2022-01-05 09:26:43,883	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 09:26:43,885	> Set order state to DONE. PE_ID:2022010500100001
[INFO | main_logic.py:435]	2022-01-05 09:26:43,887	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 09:26:43,888	> Logic state <LIFT> finish.
[INFO | main_logic.py:315]	2022-01-05 09:26:43,989	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 09:26:44,090	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 09:26:44,091	> CM Slot[1] -> Lift Slot[2]
[INFO | main_logic.py:172]	2022-01-05 09:26:56,484	> di idx 12 : 1
[INFO | main_logic.py:409]	2022-01-05 09:27:02,617	> CM Slot[1] -> Lift Slot[2] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 09:27:02,619	> Set order state to DONE. PE_ID:2022010500100001
[INFO | main_logic.py:435]	2022-01-05 09:27:02,621	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 09:27:02,622	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-05 09:27:02,724	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 09:27:02,825	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-05 09:27:02,826	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:458]	2022-01-05 09:27:36,866	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:448]	2022-01-05 09:27:36,867	> Trying to clean filter - idx: 1 ...
[INFO | main_logic.py:535]	2022-01-05 09:27:37,859	> Event on_barcode_listener called. Barcode: 2022010500100001
[INFO | main_logic.py:543]	2022-01-05 09:27:37,860	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 09:27:37,861	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 09:27:37,864	> Barcode: 2022010500100001, PE ID: 2022010500100001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 09:27:37,867	> Expired: False
[INFO | main_logic.py:541]	2022-01-05 09:27:37,870	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 09:27:37,872	> Barcode: 2022010500100001, PE ID: 2022010500100001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 09:27:37,876	> Expired: False
[INFO | main_logic.py:172]	2022-01-05 09:27:42,552	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-05 09:27:43,551	> Removed cup by customer. Index: 1
[INFO | main_logic.py:172]	2022-01-05 09:27:43,635	> di idx 12 : 0
[INFO | main_logic.py:203]	2022-01-05 09:27:44,596	> Removed cup by customer. Index: 2
[DEBUG | main_logic.py:234]	2022-01-05 09:27:49,062	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010500100001, menu: AMERICANO
[INFO | main_logic.py:244]	2022-01-05 09:27:49,065	> State changed [2] -> [1], lift_index: 1, PE_ID: 2022010500100001, menu: AMERICANO
[DEBUG | main_logic.py:234]	2022-01-05 09:27:49,561	> Removing Coffee confirmed : lift_index: 2, PE_ID: 2022010500100001, menu: AMERICANO
[INFO | main_logic.py:458]	2022-01-05 09:28:17,419	> Trying to clean filter - idx: 1 ... Done.
[INFO | main_logic.py:460]	2022-01-05 09:28:17,419	> Logic state <CLEAN> finish.
[INFO | main_logic.py:319]	2022-01-05 09:28:17,520	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 09:28:17,621	> Logic state <CLEAN> begin.
[INFO | main_logic.py:460]	2022-01-05 09:28:17,622	> Logic state <CLEAN> finish.
[INFO | main_logic.py:304]	2022-01-05 09:28:17,723	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 09:28:17,729	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb5f8dd6c>
[INFO | main_logic.py:567]	2022-01-05 09:29:00,739	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 09:29:00,749	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 09:29:00,750	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 09:29:00,851	> Logic state <RECIPE> begin.
[INFO | main_logic.py:363]	2022-01-05 09:29:23,685	> Logic state <RECIPE> finish.
[INFO | main_logic.py:304]	2022-01-05 09:29:23,786	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 09:29:23,809	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb5f8dbec>
[INFO | main_logic.py:554]	2022-01-05 09:29:35,004	> Event on_coffee_done called.
[INFO | main_logic.py:567]	2022-01-05 09:30:04,776	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 09:30:04,808	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 09:30:04,809	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 09:30:04,910	> Logic state <RECIPE> begin.
[INFO | ice_disp.py:48]	2022-01-05 09:30:08,436	> Event occurred! Event Type: 0, Args: <logics.coffee.Coffee object at 0xb5f8dbec>
[INFO | ice_disp.py:53]	2022-01-05 09:30:08,443	> create new icedisp serial
[INFO | ice_disp.py:106]	2022-01-05 09:30:08,444	> Called CheckIceDispenser
[INFO | ice_disp.py:107]	2022-01-05 09:30:08,445	> ice status check: {packet}
[INFO | ice_disp.py:116]	2022-01-05 09:30:08,456	> Try read packet...
[INFO | ice_disp.py:120]	2022-01-05 09:30:08,459	> reconnet to serialIceDispenser...
[INFO | ice_disp.py:176]	2022-01-05 09:30:08,526	> status check done
[INFO | ice_disp.py:48]	2022-01-05 09:30:15,464	> Event occurred! Event Type: 1, Args: None
[INFO | ice_disp.py:50]	2022-01-05 09:30:15,465	> ice serial is already opend!
[INFO | ice_disp.py:61]	2022-01-05 09:30:15,750	> Close icedisp serial done
[INFO | main_logic.py:363]	2022-01-05 09:30:23,434	> Logic state <RECIPE> finish.
[INFO | main_logic.py:315]	2022-01-05 09:30:23,536	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 09:30:23,637	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 09:30:23,637	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-05 09:30:34,119	> di idx 11 : 1
[INFO | main_logic.py:554]	2022-01-05 09:30:34,586	> Event on_coffee_done called.
[INFO | main_logic.py:409]	2022-01-05 09:30:39,660	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 09:30:39,661	> Set order state to DONE. PE_ID:2022010500100001
[INFO | main_logic.py:435]	2022-01-05 09:30:39,664	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 09:30:39,664	> Logic state <LIFT> finish.
[INFO | main_logic.py:315]	2022-01-05 09:30:39,766	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 09:30:39,867	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 09:30:39,868	> CM Slot[1] -> Lift Slot[2]
[INFO | main_logic.py:172]	2022-01-05 09:30:52,628	> di idx 12 : 1
[INFO | main_logic.py:409]	2022-01-05 09:30:58,392	> CM Slot[1] -> Lift Slot[2] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 09:30:58,394	> Set order state to DONE. PE_ID:2022010500100001
[INFO | main_logic.py:435]	2022-01-05 09:30:58,396	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 09:30:58,397	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-05 09:30:58,498	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 09:30:58,599	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-05 09:30:58,600	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-05 09:31:00,117	> Event on_barcode_listener called. Barcode: 2022010500100001
[INFO | main_logic.py:543]	2022-01-05 09:31:00,119	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 09:31:00,122	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 09:31:00,122	> Barcode: 2022010500100001, PE ID: 2022010500100001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 09:31:00,125	> Expired: False
[INFO | main_logic.py:541]	2022-01-05 09:31:00,128	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 09:31:00,130	> Barcode: 2022010500100001, PE ID: 2022010500100001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 09:31:00,131	> Expired: False
[INFO | main_logic.py:172]	2022-01-05 09:31:04,467	> di idx 11 : 0
[INFO | main_logic.py:172]	2022-01-05 09:31:04,509	> di idx 12 : 0
[INFO | main_logic.py:172]	2022-01-05 09:31:04,551	> di idx 12 : 1
[INFO | main_logic.py:172]	2022-01-05 09:31:04,635	> di idx 12 : 0
[INFO | main_logic.py:203]	2022-01-05 09:31:05,462	> Removed cup by customer. Index: 1
[INFO | main_logic.py:203]	2022-01-05 09:31:05,632	> Removed cup by customer. Index: 2
[DEBUG | main_logic.py:234]	2022-01-05 09:31:10,296	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010500100001, menu: AMERICANO
[INFO | main_logic.py:241]	2022-01-05 09:31:10,300	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010500100001, menu: AMERICANO
[DEBUG | main_logic.py:234]	2022-01-05 09:31:10,581	> Removing Coffee confirmed : lift_index: 2, PE_ID: 2022010500100001, menu: ICED_AMERICANO
[INFO | main_logic.py:241]	2022-01-05 09:31:10,584	> State changed [2] -> [3], lift_index: 2, PE_ID: 2022010500100001, menu: ICED_AMERICANO
[INFO | main_logic.py:458]	2022-01-05 09:31:32,641	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:448]	2022-01-05 09:31:32,642	> Trying to clean filter - idx: 1 ...
[INFO | main_logic.py:458]	2022-01-05 09:32:13,190	> Trying to clean filter - idx: 1 ... Done.
[INFO | main_logic.py:460]	2022-01-05 09:32:13,191	> Logic state <CLEAN> finish.
[INFO | main_logic.py:319]	2022-01-05 09:32:13,292	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 09:32:13,393	> Logic state <CLEAN> begin.
[INFO | main_logic.py:460]	2022-01-05 09:32:13,394	> Logic state <CLEAN> finish.
[INFO | main_logic.py:304]	2022-01-05 09:32:13,495	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 09:32:13,498	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb5f8d0cc>
[INFO | main_logic.py:567]	2022-01-05 09:32:56,529	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 09:32:56,619	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 09:32:56,621	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 09:32:56,722	> Logic state <RECIPE> begin.
[INFO | main_logic.py:363]	2022-01-05 09:33:19,558	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-05 09:33:30,878	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-05 09:33:31,274	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 09:33:31,375	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 09:33:31,376	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-05 09:33:41,822	> di idx 11 : 1
[INFO | main_logic.py:535]	2022-01-05 09:33:45,466	> Event on_barcode_listener called. Barcode: 2022010500110001
[INFO | main_logic.py:543]	2022-01-05 09:33:45,469	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-05 09:33:45,469	> State: False, The slot[1] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-05 09:33:45,472	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:409]	2022-01-05 09:33:47,396	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 09:33:47,398	> Set order state to DONE. PE_ID:2022010500110001
[INFO | main_logic.py:435]	2022-01-05 09:33:47,400	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 09:33:47,401	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-05 09:33:47,502	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:535]	2022-01-05 09:33:47,557	> Event on_barcode_listener called. Barcode: 2022010500110001
[INFO | main_logic.py:543]	2022-01-05 09:33:47,558	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 09:33:47,560	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 09:33:47,562	> Barcode: 2022010500110001, PE ID: 2022010500110001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 09:33:47,563	> Expired: False
[INFO | main_logic.py:543]	2022-01-05 09:33:47,568	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:441]	2022-01-05 09:33:47,603	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-05 09:33:47,604	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-05 09:33:48,451	> Event on_barcode_listener called. Barcode: 2022010500110001
[INFO | main_logic.py:543]	2022-01-05 09:33:48,454	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 09:33:48,456	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 09:33:48,457	> Barcode: 2022010500110001, PE ID: 2022010500110001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 09:33:48,459	> Expired: False
[INFO | main_logic.py:543]	2022-01-05 09:33:48,463	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-05 09:33:54,107	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-05 09:33:55,102	> Removed cup by customer. Index: 1
[DEBUG | main_logic.py:234]	2022-01-05 09:33:59,970	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010500110001, menu: AMERICANO
[INFO | main_logic.py:241]	2022-01-05 09:33:59,973	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010500110001, menu: AMERICANO
[INFO | main_logic.py:458]	2022-01-05 09:34:21,646	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-05 09:34:21,647	> Logic state <CLEAN> finish.
[INFO | main_logic.py:572]	2022-01-05 09:40:17,211	> Refresh milk called, but
[INFO | main_logic.py:526]	2022-01-05 09:42:28,362	> Event on_kiosk_listener called. New Menu: ICED_AMERICANO, PEID: 2022010500120001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-05 09:42:29,600	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 09:42:29,608	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb5fbdcac>
[INFO | main_logic.py:567]	2022-01-05 09:43:13,040	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 09:43:13,127	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 09:43:13,128	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 09:43:13,229	> Logic state <RECIPE> begin.
[INFO | ice_disp.py:48]	2022-01-05 09:43:16,756	> Event occurred! Event Type: 0, Args: <logics.coffee.Coffee object at 0xb5fbdcac>
[INFO | ice_disp.py:53]	2022-01-05 09:43:16,764	> create new icedisp serial
[INFO | ice_disp.py:106]	2022-01-05 09:43:16,765	> Called CheckIceDispenser
[INFO | ice_disp.py:107]	2022-01-05 09:43:16,765	> ice status check: {packet}
[INFO | ice_disp.py:116]	2022-01-05 09:43:16,776	> Try read packet...
[INFO | ice_disp.py:120]	2022-01-05 09:43:16,780	> reconnet to serialIceDispenser...
[INFO | ice_disp.py:176]	2022-01-05 09:43:16,846	> status check done
[INFO | ice_disp.py:48]	2022-01-05 09:43:23,733	> Event occurred! Event Type: 1, Args: None
[INFO | ice_disp.py:50]	2022-01-05 09:43:23,734	> ice serial is already opend!
[INFO | ice_disp.py:61]	2022-01-05 09:43:24,019	> Close icedisp serial done
[INFO | main_logic.py:363]	2022-01-05 09:43:32,554	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-05 09:43:43,891	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-05 09:43:44,275	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 09:43:44,376	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 09:43:44,377	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-05 09:43:54,954	> di idx 11 : 1
[INFO | main_logic.py:409]	2022-01-05 09:44:00,399	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 09:44:00,401	> Set order state to DONE. PE_ID:2022010500120001
[INFO | main_logic.py:435]	2022-01-05 09:44:00,404	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 09:44:00,404	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-05 09:44:00,505	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 09:44:00,606	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-05 09:44:00,607	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-05 09:44:13,478	> Event on_barcode_listener called. Barcode: 2022010500120001
[INFO | main_logic.py:543]	2022-01-05 09:44:13,480	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 09:44:13,482	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 09:44:13,486	> Barcode: 2022010500120001, PE ID: 2022010500120001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 09:44:13,487	> Expired: False
[INFO | main_logic.py:543]	2022-01-05 09:44:13,492	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-05 09:44:17,703	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-05 09:44:18,693	> Removed cup by customer. Index: 1
[DEBUG | main_logic.py:234]	2022-01-05 09:44:23,467	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010500120001, menu: ICED_AMERICANO
[INFO | main_logic.py:241]	2022-01-05 09:44:23,470	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010500120001, menu: ICED_AMERICANO
[INFO | main_logic.py:458]	2022-01-05 09:44:34,649	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-05 09:44:34,649	> Logic state <CLEAN> finish.
[INFO | main_logic.py:526]	2022-01-05 10:19:30,722	> Event on_kiosk_listener called. New Menu: AMERICANO, PEID: 2022010500130001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-05 10:19:31,333	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 10:19:31,361	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb45ca32c>
[INFO | main_logic.py:567]	2022-01-05 10:20:14,394	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 10:20:14,459	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 10:20:14,460	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 10:20:14,561	> Logic state <RECIPE> begin.
[INFO | main_logic.py:363]	2022-01-05 10:20:37,395	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-05 10:20:48,712	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-05 10:20:49,112	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 10:20:49,213	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 10:20:49,214	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-05 10:20:59,661	> di idx 11 : 1
[INFO | main_logic.py:409]	2022-01-05 10:21:05,236	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 10:21:05,238	> Set order state to DONE. PE_ID:2022010500130001
[INFO | main_logic.py:435]	2022-01-05 10:21:05,240	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 10:21:05,241	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-05 10:21:05,342	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 10:21:05,443	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-05 10:21:05,444	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-05 10:21:28,018	> Event on_barcode_listener called. Barcode: 2022010500130001
[INFO | main_logic.py:543]	2022-01-05 10:21:28,020	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 10:21:28,020	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 10:21:28,024	> Barcode: 2022010500130001, PE ID: 2022010500130001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 10:21:28,024	> Expired: False
[INFO | main_logic.py:543]	2022-01-05 10:21:28,029	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-05 10:21:32,358	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-05 10:21:33,353	> Removed cup by customer. Index: 1
[DEBUG | main_logic.py:234]	2022-01-05 10:21:38,119	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010500130001, menu: AMERICANO
[INFO | main_logic.py:241]	2022-01-05 10:21:38,121	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010500130001, menu: AMERICANO
[INFO | main_logic.py:458]	2022-01-05 10:21:39,487	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-05 10:21:39,488	> Logic state <CLEAN> finish.
[INFO | main_logic.py:526]	2022-01-05 10:30:19,265	> Event on_kiosk_listener called. New Menu: ICED_AMERICANO, PEID: 2022010500140001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-05 10:30:22,288	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 10:30:22,291	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb45ca82c>
[INFO | main_logic.py:567]	2022-01-05 10:31:05,703	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 10:31:05,717	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 10:31:05,717	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 10:31:05,818	> Logic state <RECIPE> begin.
[INFO | ice_disp.py:48]	2022-01-05 10:31:09,348	> Event occurred! Event Type: 0, Args: <logics.coffee.Coffee object at 0xb45ca82c>
[INFO | ice_disp.py:53]	2022-01-05 10:31:09,356	> create new icedisp serial
[INFO | ice_disp.py:106]	2022-01-05 10:31:09,357	> Called CheckIceDispenser
[INFO | ice_disp.py:107]	2022-01-05 10:31:09,358	> ice status check: {packet}
[INFO | ice_disp.py:116]	2022-01-05 10:31:09,368	> Try read packet...
[INFO | ice_disp.py:120]	2022-01-05 10:31:09,372	> reconnet to serialIceDispenser...
[INFO | ice_disp.py:176]	2022-01-05 10:31:09,439	> status check done
[INFO | ice_disp.py:48]	2022-01-05 10:31:16,367	> Event occurred! Event Type: 1, Args: None
[INFO | ice_disp.py:50]	2022-01-05 10:31:16,369	> ice serial is already opend!
[INFO | ice_disp.py:61]	2022-01-05 10:31:16,663	> Close icedisp serial done
[INFO | main_logic.py:363]	2022-01-05 10:31:25,343	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-05 10:31:36,680	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-05 10:31:37,061	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 10:31:37,162	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 10:31:37,162	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-05 10:31:47,797	> di idx 11 : 1
[INFO | main_logic.py:409]	2022-01-05 10:31:53,182	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 10:31:53,184	> Set order state to DONE. PE_ID:2022010500140001
[INFO | main_logic.py:435]	2022-01-05 10:31:53,187	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 10:31:53,188	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-05 10:31:53,289	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 10:31:53,390	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-05 10:31:53,391	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-05 10:31:56,846	> Event on_barcode_listener called. Barcode: 2022010500140001
[INFO | main_logic.py:543]	2022-01-05 10:31:56,847	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 10:31:56,849	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 10:31:56,852	> Barcode: 2022010500140001, PE ID: 2022010500140001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 10:31:56,852	> Expired: False
[INFO | main_logic.py:543]	2022-01-05 10:31:56,857	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-05 10:32:00,344	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-05 10:32:02,083	> Removed cup by customer. Index: 1
[DEBUG | main_logic.py:234]	2022-01-05 10:32:06,909	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010500140001, menu: ICED_AMERICANO
[INFO | main_logic.py:241]	2022-01-05 10:32:06,911	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010500140001, menu: ICED_AMERICANO
[INFO | main_logic.py:458]	2022-01-05 10:32:27,432	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-05 10:32:27,433	> Logic state <CLEAN> finish.
[INFO | main_logic.py:572]	2022-01-05 10:58:40,736	> Refresh milk called, but
[INFO | main_logic.py:526]	2022-01-05 11:11:39,095	> Event on_kiosk_listener called. New Menu: AMERICANO, PEID: 2022010500150001, OJ_NO: 1
[INFO | main_logic.py:526]	2022-01-05 11:11:39,099	> Event on_kiosk_listener called. New Menu: AMERICANO, PEID: 2022010500150001, OJ_NO: 1
[INFO | main_logic.py:526]	2022-01-05 11:11:39,104	> Event on_kiosk_listener called. New Menu: AMERICANO, PEID: 2022010500150001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-05 11:11:39,652	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 11:11:39,676	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb5fbd08c>
[INFO | main_logic.py:567]	2022-01-05 11:12:22,710	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 11:12:22,780	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 11:12:22,781	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 11:12:22,882	> Logic state <RECIPE> begin.
[INFO | main_logic.py:363]	2022-01-05 11:12:45,714	> Logic state <RECIPE> finish.
[INFO | main_logic.py:304]	2022-01-05 11:12:45,815	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 11:12:45,842	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb5fbd4ec>
[INFO | main_logic.py:554]	2022-01-05 11:12:57,031	> Event on_coffee_done called.
[INFO | main_logic.py:567]	2022-01-05 11:13:26,414	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 11:13:26,437	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 11:13:26,437	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 11:13:26,538	> Logic state <RECIPE> begin.
[INFO | main_logic.py:526]	2022-01-05 11:13:28,310	> Event on_kiosk_listener called. New Menu: ICED_AMERICANO, PEID: 2022010500160001, OJ_NO: 1
[INFO | main_logic.py:363]	2022-01-05 11:13:48,371	> Logic state <RECIPE> finish.
[INFO | main_logic.py:315]	2022-01-05 11:13:48,477	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 11:13:48,578	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 11:13:48,579	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-05 11:13:59,018	> di idx 11 : 1
[INFO | main_logic.py:554]	2022-01-05 11:13:59,521	> Event on_coffee_done called.
[INFO | main_logic.py:409]	2022-01-05 11:14:04,598	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 11:14:04,600	> Set order state to DONE. PE_ID:2022010500150001
[INFO | main_logic.py:435]	2022-01-05 11:14:04,602	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 11:14:04,603	> Logic state <LIFT> finish.
[INFO | main_logic.py:315]	2022-01-05 11:14:04,705	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 11:14:04,806	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 11:14:04,807	> CM Slot[1] -> Lift Slot[2]
[INFO | main_logic.py:172]	2022-01-05 11:14:17,220	> di idx 12 : 1
[INFO | main_logic.py:409]	2022-01-05 11:14:23,330	> CM Slot[1] -> Lift Slot[2] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 11:14:23,332	> Set order state to DONE. PE_ID:2022010500150001
[INFO | main_logic.py:435]	2022-01-05 11:14:23,333	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 11:14:23,334	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-05 11:14:23,436	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 11:14:23,537	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-05 11:14:23,537	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:458]	2022-01-05 11:14:57,578	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:448]	2022-01-05 11:14:57,578	> Trying to clean filter - idx: 1 ...
[INFO | main_logic.py:458]	2022-01-05 11:15:38,129	> Trying to clean filter - idx: 1 ... Done.
[INFO | main_logic.py:460]	2022-01-05 11:15:38,129	> Logic state <CLEAN> finish.
[INFO | main_logic.py:319]	2022-01-05 11:15:38,230	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 11:15:38,331	> Logic state <CLEAN> begin.
[INFO | main_logic.py:460]	2022-01-05 11:15:38,332	> Logic state <CLEAN> finish.
[INFO | main_logic.py:535]	2022-01-05 11:16:23,860	> Event on_barcode_listener called. Barcode: 2022010500150001
[INFO | main_logic.py:543]	2022-01-05 11:16:23,860	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 11:16:23,863	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 11:16:23,865	> Barcode: 2022010500150001, PE ID: 2022010500150001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 11:16:23,866	> Expired: False
[INFO | main_logic.py:541]	2022-01-05 11:16:23,870	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 11:16:23,872	> Barcode: 2022010500150001, PE ID: 2022010500150001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 11:16:23,873	> Expired: False
[INFO | main_logic.py:172]	2022-01-05 11:16:29,493	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-05 11:16:30,490	> Removed cup by customer. Index: 1
[INFO | main_logic.py:172]	2022-01-05 11:16:30,656	> di idx 12 : 0
[INFO | main_logic.py:203]	2022-01-05 11:16:31,647	> Removed cup by customer. Index: 2
[DEBUG | main_logic.py:234]	2022-01-05 11:16:35,866	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010500150001, menu: AMERICANO
[INFO | main_logic.py:244]	2022-01-05 11:16:35,869	> State changed [2] -> [1], lift_index: 1, PE_ID: 2022010500150001, menu: AMERICANO
[INFO | main_logic.py:304]	2022-01-05 11:16:35,872	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 11:16:35,894	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb5fbdaec>
[DEBUG | main_logic.py:234]	2022-01-05 11:16:36,484	> Removing Coffee confirmed : lift_index: 2, PE_ID: 2022010500150001, menu: AMERICANO
[INFO | main_logic.py:567]	2022-01-05 11:17:18,900	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 11:17:19,000	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 11:17:19,000	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 11:17:19,101	> Logic state <RECIPE> begin.
[INFO | main_logic.py:363]	2022-01-05 11:17:41,934	> Logic state <RECIPE> finish.
[INFO | main_logic.py:304]	2022-01-05 11:17:42,035	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 11:17:42,048	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb45f546c>
[INFO | main_logic.py:554]	2022-01-05 11:17:53,254	> Event on_coffee_done called.
[INFO | main_logic.py:567]	2022-01-05 11:18:23,001	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 11:18:23,057	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 11:18:23,057	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 11:18:23,158	> Logic state <RECIPE> begin.
[INFO | ice_disp.py:48]	2022-01-05 11:18:26,686	> Event occurred! Event Type: 0, Args: <logics.coffee.Coffee object at 0xb45f546c>
[INFO | ice_disp.py:53]	2022-01-05 11:18:26,692	> create new icedisp serial
[INFO | ice_disp.py:106]	2022-01-05 11:18:26,693	> Called CheckIceDispenser
[INFO | ice_disp.py:107]	2022-01-05 11:18:26,694	> ice status check: {packet}
[INFO | ice_disp.py:116]	2022-01-05 11:18:26,705	> Try read packet...
[INFO | ice_disp.py:120]	2022-01-05 11:18:26,709	> reconnet to serialIceDispenser...
[INFO | ice_disp.py:176]	2022-01-05 11:18:26,775	> status check done
[INFO | ice_disp.py:48]	2022-01-05 11:18:33,671	> Event occurred! Event Type: 1, Args: None
[INFO | ice_disp.py:50]	2022-01-05 11:18:33,673	> ice serial is already opend!
[INFO | ice_disp.py:61]	2022-01-05 11:18:33,949	> Close icedisp serial done
[INFO | main_logic.py:363]	2022-01-05 11:18:41,682	> Logic state <RECIPE> finish.
[INFO | main_logic.py:315]	2022-01-05 11:18:41,783	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 11:18:41,884	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 11:18:41,885	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-05 11:18:52,323	> di idx 11 : 1
[INFO | main_logic.py:554]	2022-01-05 11:18:52,826	> Event on_coffee_done called.
[INFO | main_logic.py:535]	2022-01-05 11:18:56,572	> Event on_barcode_listener called. Barcode: 2022010500150001
[INFO | main_logic.py:543]	2022-01-05 11:18:56,574	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-05 11:18:56,577	> State: False, The slot[1] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-05 11:18:56,580	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:409]	2022-01-05 11:18:57,906	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 11:18:57,908	> Set order state to DONE. PE_ID:2022010500150001
[INFO | main_logic.py:435]	2022-01-05 11:18:57,911	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 11:18:57,912	> Logic state <LIFT> finish.
[INFO | main_logic.py:315]	2022-01-05 11:18:58,013	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 11:18:58,114	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 11:18:58,115	> CM Slot[1] -> Lift Slot[2]
[INFO | main_logic.py:535]	2022-01-05 11:19:00,629	> Event on_barcode_listener called. Barcode: 2022010500150001
[INFO | main_logic.py:543]	2022-01-05 11:19:00,631	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 11:19:00,633	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 11:19:00,634	> Barcode: 2022010500150001, PE ID: 2022010500150001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 11:19:00,636	> Expired: False
[INFO | main_logic.py:543]	2022-01-05 11:19:00,639	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:535]	2022-01-05 11:19:01,567	> Event on_barcode_listener called. Barcode: 2022010500150001
[INFO | main_logic.py:543]	2022-01-05 11:19:01,569	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 11:19:01,570	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 11:19:01,572	> Barcode: 2022010500150001, PE ID: 2022010500150001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 11:19:01,575	> Expired: False
[INFO | main_logic.py:543]	2022-01-05 11:19:01,578	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-05 11:19:04,996	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-05 11:19:05,992	> Removed cup by customer. Index: 1
[DEBUG | main_logic.py:234]	2022-01-05 11:19:10,781	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010500150001, menu: AMERICANO
[INFO | main_logic.py:241]	2022-01-05 11:19:10,783	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010500150001, menu: AMERICANO
[INFO | main_logic.py:172]	2022-01-05 11:19:10,862	> di idx 12 : 1
[INFO | main_logic.py:535]	2022-01-05 11:19:12,900	> Event on_barcode_listener called. Barcode: 2022010500160001
[INFO | main_logic.py:543]	2022-01-05 11:19:12,902	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-05 11:19:12,905	> State: False, The slot[1] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-05 11:19:12,905	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:409]	2022-01-05 11:19:16,640	> CM Slot[1] -> Lift Slot[2] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 11:19:16,642	> Set order state to DONE. PE_ID:2022010500160001
[INFO | main_logic.py:435]	2022-01-05 11:19:16,644	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 11:19:16,645	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-05 11:19:16,746	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 11:19:16,847	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-05 11:19:16,848	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-05 11:19:26,117	> Event on_barcode_listener called. Barcode: 2022010500160001
[INFO | main_logic.py:543]	2022-01-05 11:19:26,119	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-05 11:19:26,122	> State: False, The slot[1] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 11:19:26,123	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 11:19:26,125	> Barcode: 2022010500160001, PE ID: 2022010500160001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 11:19:26,127	> Expired: False
[INFO | main_logic.py:172]	2022-01-05 11:19:30,887	> di idx 12 : 0
[INFO | main_logic.py:203]	2022-01-05 11:19:31,876	> Removed cup by customer. Index: 2
[DEBUG | main_logic.py:234]	2022-01-05 11:19:36,762	> Removing Coffee confirmed : lift_index: 2, PE_ID: 2022010500160001, menu: ICED_AMERICANO
[INFO | main_logic.py:241]	2022-01-05 11:19:36,766	> State changed [2] -> [3], lift_index: 2, PE_ID: 2022010500160001, menu: ICED_AMERICANO
[INFO | main_logic.py:458]	2022-01-05 11:19:50,889	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:448]	2022-01-05 11:19:50,890	> Trying to clean filter - idx: 1 ...
[INFO | main_logic.py:458]	2022-01-05 11:20:31,440	> Trying to clean filter - idx: 1 ... Done.
[INFO | main_logic.py:460]	2022-01-05 11:20:31,441	> Logic state <CLEAN> finish.
[INFO | main_logic.py:319]	2022-01-05 11:20:31,542	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 11:20:31,643	> Logic state <CLEAN> begin.
[INFO | main_logic.py:460]	2022-01-05 11:20:31,644	> Logic state <CLEAN> finish.
[INFO | main_logic.py:526]	2022-01-05 11:32:30,727	> Event on_kiosk_listener called. New Menu: ICED_AMERICANO, PEID: 2022010500170001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-05 11:32:31,886	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 11:32:31,887	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb45ded4c>
[INFO | main_logic.py:567]	2022-01-05 11:33:15,306	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 11:33:15,311	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 11:33:15,312	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 11:33:15,413	> Logic state <RECIPE> begin.
[INFO | ice_disp.py:48]	2022-01-05 11:33:18,934	> Event occurred! Event Type: 0, Args: <logics.coffee.Coffee object at 0xb45ded4c>
[INFO | ice_disp.py:53]	2022-01-05 11:33:18,940	> create new icedisp serial
[INFO | ice_disp.py:106]	2022-01-05 11:33:18,941	> Called CheckIceDispenser
[INFO | ice_disp.py:107]	2022-01-05 11:33:18,942	> ice status check: {packet}
[INFO | ice_disp.py:116]	2022-01-05 11:33:18,953	> Try read packet...
[INFO | ice_disp.py:120]	2022-01-05 11:33:18,956	> reconnet to serialIceDispenser...
[INFO | ice_disp.py:176]	2022-01-05 11:33:19,022	> status check done
[INFO | ice_disp.py:48]	2022-01-05 11:33:25,900	> Event occurred! Event Type: 1, Args: None
[INFO | ice_disp.py:50]	2022-01-05 11:33:25,902	> ice serial is already opend!
[INFO | ice_disp.py:61]	2022-01-05 11:33:26,195	> Close icedisp serial done
[INFO | main_logic.py:363]	2022-01-05 11:33:34,738	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-05 11:33:46,055	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-05 11:33:46,455	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 11:33:46,556	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 11:33:46,557	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-05 11:33:57,163	> di idx 11 : 1
[INFO | main_logic.py:409]	2022-01-05 11:34:02,577	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 11:34:02,579	> Set order state to DONE. PE_ID:2022010500170001
[INFO | main_logic.py:435]	2022-01-05 11:34:02,581	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 11:34:02,582	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-05 11:34:02,683	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 11:34:02,784	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-05 11:34:02,785	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-05 11:34:06,376	> Event on_barcode_listener called. Barcode: 2022010500170001
[INFO | main_logic.py:543]	2022-01-05 11:34:06,377	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 11:34:06,379	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 11:34:06,381	> Barcode: 2022010500170001, PE ID: 2022010500170001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 11:34:06,382	> Expired: False
[INFO | main_logic.py:543]	2022-01-05 11:34:06,387	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-05 11:34:10,224	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-05 11:34:11,221	> Removed cup by customer. Index: 1
[DEBUG | main_logic.py:234]	2022-01-05 11:34:16,021	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010500170001, menu: ICED_AMERICANO
[INFO | main_logic.py:241]	2022-01-05 11:34:16,025	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010500170001, menu: ICED_AMERICANO
[INFO | main_logic.py:458]	2022-01-05 11:34:36,826	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-05 11:34:36,827	> Logic state <CLEAN> finish.
[WARNING | main_logic.py:129]	2022-01-05 11:35:17,512	> Stop button pushed. Requesting stop entire program from the co-routine in the main logic process.
[INFO | process_handler.py:81]	2022-01-05 11:35:17,581	> Shutting down...
[INFO | process_handler.py:86]	2022-01-05 11:35:17,582	> Disposing device 'Kiosk'...
[INFO | kiosk.py:94]	2022-01-05 11:35:17,583	> Kiosk - OnDispose
[INFO | kiosk.py:94]	2022-01-05 11:35:17,583	> Kiosk - Trying to disconnect to Database.
[INFO | kiosk.py:94]	2022-01-05 11:35:17,589	> Kiosk - Successfully disconnected to Database.
[INFO | kiosk.py:94]	2022-01-05 11:35:17,590	> Kiosk - OnDispose Done.
[INFO | process_handler.py:88]	2022-01-05 11:35:17,590	> Successfully disposed device 'Kiosk'
[INFO | process_handler.py:86]	2022-01-05 11:35:17,591	> Disposing device 'IceDispenser'...
[INFO | process_handler.py:88]	2022-01-05 11:35:17,592	> Successfully disposed device 'IceDispenser'
[INFO | process_handler.py:86]	2022-01-05 11:35:17,593	> Disposing device 'CupDispenser'...
[INFO | process_handler.py:88]	2022-01-05 11:35:17,601	> Successfully disposed device 'CupDispenser'
[INFO | process_handler.py:86]	2022-01-05 11:35:17,602	> Disposing device 'BarcodeReader'...
[INFO | barcode_reader.py:35]	2022-01-05 11:35:17,603	> BarcodeReader - OnDispose
[INFO | barcode_reader.py:37]	2022-01-05 11:35:17,603	> barcode thread end
[INFO | process_handler.py:88]	2022-01-05 11:35:17,604	> Successfully disposed device 'BarcodeReader'
[INFO | process_handler.py:94]	2022-01-05 11:35:17,616	> Shutting down...Done.
[INFO | process_handler.py:33]	2022-01-05 11:35:35,674	> Configurations_
{'robot_dof': 6, 'db_host': '192.168.10.22', 'db_name': 'KIOSK', 'db_user': 'NEUROMEKA', 'db_pwd': 'NEUROMEKA1234', 'db_timeout': 5, 'db_login_timeout': 5, 'db_charset': 'utf8', 'ice_only': 4, 'water_only': 0, 'ice_and_water': 1, 'coffee_map': {'00000001': 0, '00000002': 3, '00000003': 4, '00000004': 1, '00000005': 5, '00000006': 2}, 'coffee_expiry_time': 600, 'cup_disp_packet_len': 11, 'ice_disp_packet_len': 5, 'milk_refresh_duration': 4800, 'lift_delay': 10, 'lift_cup_delay': 1, 'espresso_machine_shot_delay_1': 6, 'espresso_machine_shot_delay_2': 6, 'espresso_machine_long_delay_1': 12, 'espresso_machine_long_delay_2': 12}
[INFO | process_handler.py:33]	2022-01-05 11:36:29,045	> Configurations_
{'robot_dof': 6, 'db_host': '192.168.10.22', 'db_name': 'KIOSK', 'db_user': 'NEUROMEKA', 'db_pwd': 'NEUROMEKA1234', 'db_timeout': 5, 'db_login_timeout': 5, 'db_charset': 'utf8', 'ice_only': 4, 'water_only': 0, 'ice_and_water': 1, 'coffee_map': {'00000001': 0, '00000002': 3, '00000003': 4, '00000004': 1, '00000005': 5, '00000006': 2}, 'coffee_expiry_time': 600, 'cup_disp_packet_len': 11, 'ice_disp_packet_len': 5, 'milk_refresh_duration': 4800, 'lift_delay': 10, 'lift_cup_delay': 1, 'espresso_machine_shot_delay_1': 6, 'espresso_machine_shot_delay_2': 6, 'espresso_machine_long_delay_1': 12, 'espresso_machine_long_delay_2': 12}
[INFO | process_handler.py:98]	2022-01-05 11:36:39,712	> Program started.
[INFO | process_handler.py:43]	2022-01-05 11:36:39,715	> Preparing program...
[INFO | process_handler.py:52]	2022-01-05 11:36:39,720	> initializing device '<class 'devices.kiosk.Kiosk'>'...
[DEBUG | process_handler.py:58]	2022-01-05 11:36:39,720	> Called on_create of device '<class 'devices.kiosk.Kiosk'>'
[INFO | kiosk.py:94]	2022-01-05 11:36:39,721	> Kiosk - OnCreate
[INFO | kiosk.py:94]	2022-01-05 11:36:39,722	> Kiosk - Trying to connect to Database - host: 192.168.10.22, db: KIOSK.
[INFO | kiosk.py:94]	2022-01-05 11:36:39,780	> Kiosk - Successfully connected to Database.
[INFO | kiosk.py:94]	2022-01-05 11:36:39,781	> Kiosk - OnCreate Done.
[DEBUG | process_handler.py:60]	2022-01-05 11:36:39,781	> on_create of device '<class 'devices.kiosk.Kiosk'>' done.
[INFO | process_handler.py:63]	2022-01-05 11:36:39,782	> Successfully initialized. Device name: Kiosk
[INFO | process_handler.py:52]	2022-01-05 11:36:39,783	> initializing device '<class 'devices.ice_disp.IceDispenser'>'...
[DEBUG | process_handler.py:58]	2022-01-05 11:36:39,784	> Called on_create of device '<class 'devices.ice_disp.IceDispenser'>'
[DEBUG | process_handler.py:60]	2022-01-05 11:36:39,786	> on_create of device '<class 'devices.ice_disp.IceDispenser'>' done.
[INFO | process_handler.py:63]	2022-01-05 11:36:39,787	> Successfully initialized. Device name: IceDispenser
[INFO | process_handler.py:52]	2022-01-05 11:36:39,788	> initializing device '<class 'devices.cup_disp.CupDispenser'>'...
[DEBUG | process_handler.py:58]	2022-01-05 11:36:39,788	> Called on_create of device '<class 'devices.cup_disp.CupDispenser'>'
[DEBUG | process_handler.py:60]	2022-01-05 11:36:39,793	> on_create of device '<class 'devices.cup_disp.CupDispenser'>' done.
[INFO | process_handler.py:63]	2022-01-05 11:36:39,793	> Successfully initialized. Device name: CupDispenser
[INFO | process_handler.py:52]	2022-01-05 11:36:39,794	> initializing device '<class 'devices.barcode_reader.BarcodeReader'>'...
[DEBUG | process_handler.py:58]	2022-01-05 11:36:39,795	> Called on_create of device '<class 'devices.barcode_reader.BarcodeReader'>'
[INFO | barcode_reader.py:26]	2022-01-05 11:36:39,796	> BarcodeReader - OnCreate
[INFO | barcode_reader.py:30]	2022-01-05 11:36:39,798	> barcode thread start
[DEBUG | process_handler.py:60]	2022-01-05 11:36:39,800	> on_create of device '<class 'devices.barcode_reader.BarcodeReader'>' done.
[INFO | process_handler.py:63]	2022-01-05 11:36:39,801	> Successfully initialized. Device name: BarcodeReader
[INFO | process_handler.py:75]	2022-01-05 11:36:39,802	> Preparing program...Done.
[INFO | main_logic.py:526]	2022-01-05 11:38:04,809	> Event on_kiosk_listener called. New Menu: AMERICANO, PEID: 2022010500180001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-05 11:38:09,426	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 11:38:09,447	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb5fb70ec>
[INFO | main_logic.py:567]	2022-01-05 11:38:52,469	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 11:38:52,550	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 11:38:52,551	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 11:38:52,652	> Logic state <RECIPE> begin.
[INFO | main_logic.py:363]	2022-01-05 11:39:15,485	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-05 11:39:26,804	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-05 11:39:27,202	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 11:39:27,303	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 11:39:27,304	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-05 11:39:37,752	> di idx 11 : 1
[INFO | main_logic.py:409]	2022-01-05 11:39:43,325	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 11:39:43,327	> Set order state to DONE. PE_ID:2022010500180001
[INFO | main_logic.py:435]	2022-01-05 11:39:43,329	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 11:39:43,330	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-05 11:39:43,431	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 11:39:43,532	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-05 11:39:43,533	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-05 11:39:49,810	> Event on_barcode_listener called. Barcode: 2022010500180001
[INFO | main_logic.py:543]	2022-01-05 11:39:49,811	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 11:39:49,812	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 11:39:49,815	> Barcode: 2022010500180001, PE ID: 2022010500180001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 11:39:49,816	> Expired: False
[INFO | main_logic.py:543]	2022-01-05 11:39:49,820	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-05 11:39:53,755	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-05 11:39:55,572	> Removed cup by customer. Index: 1
[DEBUG | main_logic.py:234]	2022-01-05 11:40:08,331	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010500180001, menu: AMERICANO
[INFO | main_logic.py:241]	2022-01-05 11:40:08,336	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010500180001, menu: AMERICANO
[INFO | main_logic.py:458]	2022-01-05 11:40:17,573	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-05 11:40:17,574	> Logic state <CLEAN> finish.
[INFO | main_logic.py:526]	2022-01-05 11:43:15,239	> Event on_kiosk_listener called. New Menu: AMERICANO, PEID: 2022010500190001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-05 11:43:17,712	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 11:43:17,739	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb5fb76cc>
[INFO | main_logic.py:567]	2022-01-05 11:44:00,758	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 11:44:00,834	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 11:44:00,835	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 11:44:00,936	> Logic state <RECIPE> begin.
[INFO | main_logic.py:363]	2022-01-05 11:44:23,769	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-05 11:44:35,099	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-05 11:44:35,486	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 11:44:35,587	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 11:44:35,588	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-05 11:44:46,035	> di idx 11 : 1
[INFO | main_logic.py:409]	2022-01-05 11:44:51,608	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 11:44:51,609	> Set order state to DONE. PE_ID:2022010500190001
[INFO | main_logic.py:435]	2022-01-05 11:44:51,612	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 11:44:51,613	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-05 11:44:51,714	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 11:44:51,815	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-05 11:44:51,816	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-05 11:45:01,447	> Event on_barcode_listener called. Barcode: 2022010500190001
[INFO | main_logic.py:543]	2022-01-05 11:45:01,448	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 11:45:01,450	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 11:45:01,452	> Barcode: 2022010500190001, PE ID: 2022010500190001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 11:45:01,453	> Expired: False
[INFO | main_logic.py:543]	2022-01-05 11:45:01,458	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-05 11:45:06,544	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-05 11:45:07,529	> Removed cup by customer. Index: 1
[DEBUG | main_logic.py:234]	2022-01-05 11:45:20,352	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010500190001, menu: AMERICANO
[INFO | main_logic.py:241]	2022-01-05 11:45:20,356	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010500190001, menu: AMERICANO
[INFO | main_logic.py:458]	2022-01-05 11:45:25,857	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-05 11:45:25,858	> Logic state <CLEAN> finish.
[INFO | main_logic.py:526]	2022-01-05 12:07:17,646	> Event on_kiosk_listener called. New Menu: ICED_AMERICANO, PEID: 2022010500200001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-05 12:07:18,487	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 12:07:18,513	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb5fb748c>
[INFO | main_logic.py:567]	2022-01-05 12:08:01,934	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 12:08:02,017	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 12:08:02,018	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 12:08:02,119	> Logic state <RECIPE> begin.
[INFO | ice_disp.py:48]	2022-01-05 12:08:05,628	> Event occurred! Event Type: 0, Args: <logics.coffee.Coffee object at 0xb5fb748c>
[INFO | ice_disp.py:50]	2022-01-05 12:08:05,630	> ice serial is already opend!
[INFO | ice_disp.py:106]	2022-01-05 12:08:05,632	> Called CheckIceDispenser
[INFO | ice_disp.py:107]	2022-01-05 12:08:05,633	> ice status check: {packet}
[INFO | ice_disp.py:116]	2022-01-05 12:08:05,645	> Try read packet...
[INFO | ice_disp.py:120]	2022-01-05 12:08:05,648	> reconnet to serialIceDispenser...
[INFO | ice_disp.py:176]	2022-01-05 12:08:05,715	> status check done
[INFO | ice_disp.py:48]	2022-01-05 12:08:12,654	> Event occurred! Event Type: 1, Args: None
[INFO | ice_disp.py:50]	2022-01-05 12:08:12,656	> ice serial is already opend!
[INFO | ice_disp.py:61]	2022-01-05 12:08:12,938	> Close icedisp serial done
[INFO | main_logic.py:363]	2022-01-05 12:08:21,643	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-05 12:08:32,973	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-05 12:08:33,361	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 12:08:33,462	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 12:08:33,462	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-05 12:08:44,078	> di idx 11 : 1
[INFO | main_logic.py:409]	2022-01-05 12:08:49,483	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 12:08:49,485	> Set order state to DONE. PE_ID:2022010500200001
[INFO | main_logic.py:435]	2022-01-05 12:08:49,487	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 12:08:49,488	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-05 12:08:49,589	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 12:08:49,690	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-05 12:08:49,691	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-05 12:09:02,734	> Event on_barcode_listener called. Barcode: 2022010500200001
[INFO | main_logic.py:543]	2022-01-05 12:09:02,736	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 12:09:02,738	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 12:09:02,740	> Barcode: 2022010500200001, PE ID: 2022010500200001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 12:09:02,742	> Expired: False
[INFO | main_logic.py:543]	2022-01-05 12:09:02,746	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-05 12:09:06,697	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-05 12:09:07,680	> Removed cup by customer. Index: 1
[DEBUG | main_logic.py:234]	2022-01-05 12:09:20,450	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010500200001, menu: ICED_AMERICANO
[INFO | main_logic.py:241]	2022-01-05 12:09:20,452	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010500200001, menu: ICED_AMERICANO
[INFO | main_logic.py:458]	2022-01-05 12:09:23,729	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-05 12:09:23,730	> Logic state <CLEAN> finish.
[INFO | main_logic.py:526]	2022-01-05 12:25:21,272	> Event on_kiosk_listener called. New Menu: ICED_AMERICANO, PEID: 2022010500210001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-05 12:25:22,086	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 12:25:22,112	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb4582e2c>
[INFO | main_logic.py:567]	2022-01-05 12:26:05,531	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 12:26:05,615	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 12:26:05,616	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 12:26:05,717	> Logic state <RECIPE> begin.
[INFO | ice_disp.py:48]	2022-01-05 12:26:09,229	> Event occurred! Event Type: 0, Args: <logics.coffee.Coffee object at 0xb4582e2c>
[INFO | ice_disp.py:53]	2022-01-05 12:26:09,237	> create new icedisp serial
[INFO | ice_disp.py:106]	2022-01-05 12:26:09,238	> Called CheckIceDispenser
[INFO | ice_disp.py:107]	2022-01-05 12:26:09,239	> ice status check: {packet}
[INFO | ice_disp.py:116]	2022-01-05 12:26:09,250	> Try read packet...
[INFO | ice_disp.py:120]	2022-01-05 12:26:09,253	> reconnet to serialIceDispenser...
[INFO | ice_disp.py:176]	2022-01-05 12:26:09,320	> status check done
[INFO | ice_disp.py:48]	2022-01-05 12:26:16,213	> Event occurred! Event Type: 1, Args: None
[INFO | ice_disp.py:50]	2022-01-05 12:26:16,214	> ice serial is already opend!
[INFO | ice_disp.py:61]	2022-01-05 12:26:16,493	> Close icedisp serial done
[INFO | main_logic.py:363]	2022-01-05 12:26:25,048	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-05 12:26:36,381	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-05 12:26:36,764	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 12:26:36,865	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 12:26:36,866	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-05 12:26:47,443	> di idx 11 : 1
[INFO | main_logic.py:409]	2022-01-05 12:26:52,888	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 12:26:52,890	> Set order state to DONE. PE_ID:2022010500210001
[INFO | main_logic.py:435]	2022-01-05 12:26:52,892	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 12:26:52,893	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-05 12:26:52,994	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 12:26:53,095	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-05 12:26:53,096	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-05 12:27:04,432	> Event on_barcode_listener called. Barcode: 2022010500210001
[INFO | main_logic.py:543]	2022-01-05 12:27:04,434	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 12:27:04,436	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 12:27:04,438	> Barcode: 2022010500210001, PE ID: 2022010500210001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 12:27:04,439	> Expired: False
[INFO | main_logic.py:543]	2022-01-05 12:27:04,443	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-05 12:27:09,142	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-05 12:27:10,130	> Removed cup by customer. Index: 1
[DEBUG | main_logic.py:234]	2022-01-05 12:27:22,737	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010500210001, menu: ICED_AMERICANO
[INFO | main_logic.py:241]	2022-01-05 12:27:22,741	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010500210001, menu: ICED_AMERICANO
[INFO | main_logic.py:458]	2022-01-05 12:27:27,139	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-05 12:27:27,140	> Logic state <CLEAN> finish.
[INFO | main_logic.py:526]	2022-01-05 12:45:54,301	> Event on_kiosk_listener called. New Menu: ICED_AMERICANO, PEID: 2022010500220001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-05 12:45:56,497	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 12:45:56,505	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb5fb7d0c>
[INFO | main_logic.py:567]	2022-01-05 12:46:39,931	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 12:46:40,021	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 12:46:40,022	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 12:46:40,123	> Logic state <RECIPE> begin.
[INFO | ice_disp.py:48]	2022-01-05 12:46:43,644	> Event occurred! Event Type: 0, Args: <logics.coffee.Coffee object at 0xb5fb7d0c>
[INFO | ice_disp.py:53]	2022-01-05 12:46:43,651	> create new icedisp serial
[INFO | ice_disp.py:106]	2022-01-05 12:46:43,651	> Called CheckIceDispenser
[INFO | ice_disp.py:107]	2022-01-05 12:46:43,652	> ice status check: {packet}
[INFO | ice_disp.py:116]	2022-01-05 12:46:43,663	> Try read packet...
[INFO | ice_disp.py:120]	2022-01-05 12:46:43,666	> reconnet to serialIceDispenser...
[INFO | ice_disp.py:176]	2022-01-05 12:46:43,731	> status check done
[INFO | ice_disp.py:48]	2022-01-05 12:46:50,662	> Event occurred! Event Type: 1, Args: None
[INFO | ice_disp.py:50]	2022-01-05 12:46:50,662	> ice serial is already opend!
[INFO | ice_disp.py:61]	2022-01-05 12:46:50,956	> Close icedisp serial done
[INFO | main_logic.py:363]	2022-01-05 12:46:59,649	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-05 12:47:10,973	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-05 12:47:11,367	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 12:47:11,468	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 12:47:11,469	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-05 12:47:22,103	> di idx 11 : 1
[INFO | main_logic.py:409]	2022-01-05 12:47:27,488	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 12:47:27,490	> Set order state to DONE. PE_ID:2022010500220001
[INFO | main_logic.py:435]	2022-01-05 12:47:27,492	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 12:47:27,492	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-05 12:47:27,594	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 12:47:27,695	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-05 12:47:27,696	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-05 12:47:32,491	> Event on_barcode_listener called. Barcode: 2022010500220001
[INFO | main_logic.py:543]	2022-01-05 12:47:32,494	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 12:47:32,495	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 12:47:32,497	> Barcode: 2022010500220001, PE ID: 2022010500220001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 12:47:32,498	> Expired: False
[INFO | main_logic.py:543]	2022-01-05 12:47:32,504	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-05 12:47:35,912	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-05 12:47:36,897	> Removed cup by customer. Index: 1
[INFO | main_logic.py:172]	2022-01-05 12:47:37,230	> di idx 11 : 1
[INFO | main_logic.py:172]	2022-01-05 12:47:37,313	> di idx 11 : 0
[DEBUG | main_logic.py:234]	2022-01-05 12:47:50,975	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010500220001, menu: ICED_AMERICANO
[INFO | main_logic.py:241]	2022-01-05 12:47:50,978	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010500220001, menu: ICED_AMERICANO
[INFO | main_logic.py:458]	2022-01-05 12:48:01,738	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-05 12:48:01,739	> Logic state <CLEAN> finish.
[INFO | main_logic.py:572]	2022-01-05 12:55:01,144	> Refresh milk called, but
[INFO | main_logic.py:526]	2022-01-05 13:04:21,722	> Event on_kiosk_listener called. New Menu: ICED_AMERICANO, PEID: 2022010500230001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-05 13:04:23,331	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 13:04:23,337	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb45825ec>
[INFO | main_logic.py:567]	2022-01-05 13:05:06,735	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 13:05:06,757	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 13:05:06,758	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 13:05:06,859	> Logic state <RECIPE> begin.
[INFO | ice_disp.py:48]	2022-01-05 13:05:10,377	> Event occurred! Event Type: 0, Args: <logics.coffee.Coffee object at 0xb45825ec>
[INFO | ice_disp.py:53]	2022-01-05 13:05:10,383	> create new icedisp serial
[INFO | ice_disp.py:106]	2022-01-05 13:05:10,384	> Called CheckIceDispenser
[INFO | ice_disp.py:107]	2022-01-05 13:05:10,385	> ice status check: {packet}
[INFO | ice_disp.py:116]	2022-01-05 13:05:10,396	> Try read packet...
[INFO | ice_disp.py:120]	2022-01-05 13:05:10,401	> reconnet to serialIceDispenser...
[INFO | ice_disp.py:176]	2022-01-05 13:05:10,466	> status check done
[INFO | ice_disp.py:48]	2022-01-05 13:05:17,337	> Event occurred! Event Type: 1, Args: None
[INFO | ice_disp.py:50]	2022-01-05 13:05:17,339	> ice serial is already opend!
[INFO | ice_disp.py:61]	2022-01-05 13:05:17,639	> Close icedisp serial done
[INFO | main_logic.py:363]	2022-01-05 13:05:26,184	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-05 13:05:37,497	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-05 13:05:37,901	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 13:05:38,002	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 13:05:38,002	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-05 13:05:48,565	> di idx 11 : 1
[INFO | main_logic.py:409]	2022-01-05 13:05:54,023	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 13:05:54,025	> Set order state to DONE. PE_ID:2022010500230001
[INFO | main_logic.py:435]	2022-01-05 13:05:54,027	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 13:05:54,028	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-05 13:05:54,129	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 13:05:54,230	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-05 13:05:54,231	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-05 13:05:57,298	> Event on_barcode_listener called. Barcode: 2022010500230001
[INFO | main_logic.py:543]	2022-01-05 13:05:57,299	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 13:05:57,301	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 13:05:57,303	> Barcode: 2022010500230001, PE ID: 2022010500230001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 13:05:57,304	> Expired: False
[INFO | main_logic.py:543]	2022-01-05 13:05:57,308	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-05 13:06:01,941	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-05 13:06:02,931	> Removed cup by customer. Index: 1
[DEBUG | main_logic.py:234]	2022-01-05 13:06:15,700	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010500230001, menu: ICED_AMERICANO
[INFO | main_logic.py:241]	2022-01-05 13:06:15,703	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010500230001, menu: ICED_AMERICANO
[INFO | main_logic.py:458]	2022-01-05 13:06:28,271	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-05 13:06:28,271	> Logic state <CLEAN> finish.
[INFO | main_logic.py:526]	2022-01-05 13:08:58,048	> Event on_kiosk_listener called. New Menu: AMERICANO, PEID: 2022010500240001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-05 13:08:59,372	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 13:08:59,377	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb5fb7cec>
[INFO | main_logic.py:567]	2022-01-05 13:09:42,407	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 13:09:42,498	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 13:09:42,499	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 13:09:42,600	> Logic state <RECIPE> begin.
[INFO | main_logic.py:363]	2022-01-05 13:10:05,434	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-05 13:10:16,764	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-05 13:10:17,150	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 13:10:17,251	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 13:10:17,252	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-05 13:10:27,705	> di idx 11 : 1
[INFO | main_logic.py:409]	2022-01-05 13:10:33,271	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 13:10:33,272	> Set order state to DONE. PE_ID:2022010500240001
[INFO | main_logic.py:435]	2022-01-05 13:10:33,275	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 13:10:33,275	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-05 13:10:33,376	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 13:10:33,478	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-05 13:10:33,478	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-05 13:10:35,294	> Event on_barcode_listener called. Barcode: 2022010500240001
[INFO | main_logic.py:543]	2022-01-05 13:10:35,294	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 13:10:35,297	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 13:10:35,299	> Barcode: 2022010500240001, PE ID: 2022010500240001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 13:10:35,299	> Expired: False
[INFO | main_logic.py:543]	2022-01-05 13:10:35,303	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-05 13:10:40,570	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-05 13:10:41,570	> Removed cup by customer. Index: 1
[DEBUG | main_logic.py:234]	2022-01-05 13:10:54,322	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010500240001, menu: AMERICANO
[INFO | main_logic.py:241]	2022-01-05 13:10:54,325	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010500240001, menu: AMERICANO
[INFO | main_logic.py:458]	2022-01-05 13:11:07,519	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-05 13:11:07,520	> Logic state <CLEAN> finish.
[INFO | main_logic.py:526]	2022-01-05 13:25:01,774	> Event on_kiosk_listener called. New Menu: ICED_AMERICANO, PEID: 2022010500250001, OJ_NO: 1
[INFO | main_logic.py:526]	2022-01-05 13:25:01,778	> Event on_kiosk_listener called. New Menu: ICED_AMERICANO, PEID: 2022010500250001, OJ_NO: 1
[INFO | main_logic.py:526]	2022-01-05 13:25:01,782	> Event on_kiosk_listener called. New Menu: ICED_AMERICANO, PEID: 2022010500250001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-05 13:25:03,926	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 13:25:03,953	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb5fde28c>
[INFO | main_logic.py:567]	2022-01-05 13:25:47,372	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 13:25:47,452	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 13:25:47,452	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 13:25:47,554	> Logic state <RECIPE> begin.
[INFO | ice_disp.py:48]	2022-01-05 13:25:51,070	> Event occurred! Event Type: 0, Args: <logics.coffee.Coffee object at 0xb5fde28c>
[INFO | ice_disp.py:53]	2022-01-05 13:25:51,076	> create new icedisp serial
[INFO | ice_disp.py:106]	2022-01-05 13:25:51,077	> Called CheckIceDispenser
[INFO | ice_disp.py:107]	2022-01-05 13:25:51,078	> ice status check: {packet}
[INFO | ice_disp.py:116]	2022-01-05 13:25:51,089	> Try read packet...
[INFO | ice_disp.py:120]	2022-01-05 13:25:51,092	> reconnet to serialIceDispenser...
[INFO | ice_disp.py:176]	2022-01-05 13:25:51,158	> status check done
[INFO | ice_disp.py:48]	2022-01-05 13:25:58,043	> Event occurred! Event Type: 1, Args: None
[INFO | ice_disp.py:50]	2022-01-05 13:25:58,044	> ice serial is already opend!
[INFO | ice_disp.py:61]	2022-01-05 13:25:58,335	> Close icedisp serial done
[INFO | main_logic.py:363]	2022-01-05 13:26:06,880	> Logic state <RECIPE> finish.
[INFO | main_logic.py:304]	2022-01-05 13:26:06,984	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 13:26:07,000	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb5fde02c>
[INFO | main_logic.py:554]	2022-01-05 13:26:18,199	> Event on_coffee_done called.
[INFO | main_logic.py:567]	2022-01-05 13:26:47,963	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 13:26:48,005	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 13:26:48,006	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 13:26:48,107	> Logic state <RECIPE> begin.
[INFO | ice_disp.py:48]	2022-01-05 13:26:51,637	> Event occurred! Event Type: 0, Args: <logics.coffee.Coffee object at 0xb5fde02c>
[INFO | ice_disp.py:53]	2022-01-05 13:26:51,642	> create new icedisp serial
[INFO | ice_disp.py:106]	2022-01-05 13:26:51,643	> Called CheckIceDispenser
[INFO | ice_disp.py:107]	2022-01-05 13:26:51,646	> ice status check: {packet}
[INFO | ice_disp.py:116]	2022-01-05 13:26:51,658	> Try read packet...
[INFO | ice_disp.py:120]	2022-01-05 13:26:51,662	> reconnet to serialIceDispenser...
[INFO | ice_disp.py:176]	2022-01-05 13:26:51,739	> status check done
[INFO | ice_disp.py:48]	2022-01-05 13:26:58,637	> Event occurred! Event Type: 1, Args: None
[INFO | ice_disp.py:50]	2022-01-05 13:26:58,638	> ice serial is already opend!
[INFO | ice_disp.py:61]	2022-01-05 13:26:58,912	> Close icedisp serial done
[INFO | main_logic.py:363]	2022-01-05 13:27:06,633	> Logic state <RECIPE> finish.
[INFO | main_logic.py:315]	2022-01-05 13:27:06,734	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 13:27:06,836	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 13:27:06,837	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-05 13:27:17,461	> di idx 11 : 1
[INFO | main_logic.py:554]	2022-01-05 13:27:17,778	> Event on_coffee_done called.
[INFO | main_logic.py:409]	2022-01-05 13:27:22,857	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 13:27:22,859	> Set order state to DONE. PE_ID:2022010500250001
[INFO | main_logic.py:435]	2022-01-05 13:27:22,861	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 13:27:22,862	> Logic state <LIFT> finish.
[INFO | main_logic.py:315]	2022-01-05 13:27:22,963	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 13:27:23,064	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 13:27:23,065	> CM Slot[1] -> Lift Slot[2]
[INFO | main_logic.py:172]	2022-01-05 13:27:35,836	> di idx 12 : 1
[INFO | main_logic.py:409]	2022-01-05 13:27:41,589	> CM Slot[1] -> Lift Slot[2] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 13:27:41,591	> Set order state to DONE. PE_ID:2022010500250001
[INFO | main_logic.py:435]	2022-01-05 13:27:41,593	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 13:27:41,594	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-05 13:27:41,695	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 13:27:41,796	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-05 13:27:41,797	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:458]	2022-01-05 13:28:15,838	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:448]	2022-01-05 13:28:15,838	> Trying to clean filter - idx: 1 ...
[INFO | main_logic.py:458]	2022-01-05 13:28:56,390	> Trying to clean filter - idx: 1 ... Done.
[INFO | main_logic.py:460]	2022-01-05 13:28:56,391	> Logic state <CLEAN> finish.
[INFO | main_logic.py:319]	2022-01-05 13:28:56,492	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 13:28:56,593	> Logic state <CLEAN> begin.
[INFO | main_logic.py:460]	2022-01-05 13:28:56,593	> Logic state <CLEAN> finish.
[INFO | main_logic.py:535]	2022-01-05 13:29:24,303	> Event on_barcode_listener called. Barcode: 2022010500250001
[INFO | main_logic.py:543]	2022-01-05 13:29:24,304	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 13:29:24,307	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 13:29:24,307	> Barcode: 2022010500250001, PE ID: 2022010500250001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 13:29:24,309	> Expired: False
[INFO | main_logic.py:541]	2022-01-05 13:29:24,313	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 13:29:24,316	> Barcode: 2022010500250001, PE ID: 2022010500250001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 13:29:24,317	> Expired: False
[INFO | main_logic.py:172]	2022-01-05 13:29:27,668	> di idx 11 : 0
[INFO | main_logic.py:172]	2022-01-05 13:29:28,374	> di idx 11 : 1
[INFO | main_logic.py:172]	2022-01-05 13:29:28,414	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-05 13:29:29,412	> Removed cup by customer. Index: 1
[INFO | main_logic.py:172]	2022-01-05 13:29:32,284	> di idx 12 : 0
[INFO | main_logic.py:203]	2022-01-05 13:29:33,278	> Removed cup by customer. Index: 2
[DEBUG | main_logic.py:234]	2022-01-05 13:29:45,230	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010500250001, menu: ICED_AMERICANO
[INFO | main_logic.py:244]	2022-01-05 13:29:45,235	> State changed [2] -> [1], lift_index: 1, PE_ID: 2022010500250001, menu: ICED_AMERICANO
[INFO | main_logic.py:304]	2022-01-05 13:29:45,296	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 13:29:45,318	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb5fde18c>
[DEBUG | main_logic.py:234]	2022-01-05 13:29:46,171	> Removing Coffee confirmed : lift_index: 2, PE_ID: 2022010500250001, menu: ICED_AMERICANO
[INFO | main_logic.py:567]	2022-01-05 13:30:28,735	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 13:30:28,824	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 13:30:28,824	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 13:30:28,925	> Logic state <RECIPE> begin.
[INFO | ice_disp.py:48]	2022-01-05 13:30:32,447	> Event occurred! Event Type: 0, Args: <logics.coffee.Coffee object at 0xb5fde18c>
[INFO | ice_disp.py:53]	2022-01-05 13:30:32,454	> create new icedisp serial
[INFO | ice_disp.py:106]	2022-01-05 13:30:32,455	> Called CheckIceDispenser
[INFO | ice_disp.py:107]	2022-01-05 13:30:32,455	> ice status check: {packet}
[INFO | ice_disp.py:116]	2022-01-05 13:30:32,466	> Try read packet...
[INFO | ice_disp.py:120]	2022-01-05 13:30:32,470	> reconnet to serialIceDispenser...
[INFO | ice_disp.py:176]	2022-01-05 13:30:32,535	> status check done
[INFO | ice_disp.py:48]	2022-01-05 13:30:39,410	> Event occurred! Event Type: 1, Args: None
[INFO | ice_disp.py:50]	2022-01-05 13:30:39,412	> ice serial is already opend!
[INFO | ice_disp.py:61]	2022-01-05 13:30:39,711	> Close icedisp serial done
[INFO | main_logic.py:363]	2022-01-05 13:30:48,251	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-05 13:30:59,579	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-05 13:30:59,967	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 13:31:00,068	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 13:31:00,069	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-05 13:31:10,689	> di idx 11 : 1
[INFO | main_logic.py:409]	2022-01-05 13:31:16,088	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 13:31:16,089	> Set order state to DONE. PE_ID:2022010500250001
[INFO | main_logic.py:435]	2022-01-05 13:31:16,092	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 13:31:16,092	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-05 13:31:16,194	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 13:31:16,295	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-05 13:31:16,296	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-05 13:31:22,875	> Event on_barcode_listener called. Barcode: 2022010500250001
[INFO | main_logic.py:543]	2022-01-05 13:31:22,876	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 13:31:22,878	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 13:31:22,880	> Barcode: 2022010500250001, PE ID: 2022010500250001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 13:31:22,881	> Expired: False
[INFO | main_logic.py:543]	2022-01-05 13:31:22,885	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-05 13:31:26,273	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-05 13:31:27,268	> Removed cup by customer. Index: 1
[INFO | main_logic.py:172]	2022-01-05 13:31:27,392	> di idx 11 : 1
[INFO | main_logic.py:172]	2022-01-05 13:31:27,434	> di idx 11 : 0
[DEBUG | main_logic.py:234]	2022-01-05 13:31:41,231	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010500250001, menu: ICED_AMERICANO
[INFO | main_logic.py:241]	2022-01-05 13:31:41,233	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010500250001, menu: ICED_AMERICANO
[INFO | main_logic.py:458]	2022-01-05 13:31:50,338	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-05 13:31:50,339	> Logic state <CLEAN> finish.
[INFO | main_logic.py:526]	2022-01-05 13:35:04,805	> Event on_kiosk_listener called. New Menu: ICED_AMERICANO, PEID: 2022010500260001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-05 13:35:07,899	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 13:35:07,909	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb458216c>
[INFO | main_logic.py:567]	2022-01-05 13:35:51,306	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 13:35:51,324	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 13:35:51,325	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 13:35:51,426	> Logic state <RECIPE> begin.
[INFO | ice_disp.py:48]	2022-01-05 13:35:54,949	> Event occurred! Event Type: 0, Args: <logics.coffee.Coffee object at 0xb458216c>
[INFO | ice_disp.py:53]	2022-01-05 13:35:54,954	> create new icedisp serial
[INFO | ice_disp.py:106]	2022-01-05 13:35:54,956	> Called CheckIceDispenser
[INFO | ice_disp.py:107]	2022-01-05 13:35:54,956	> ice status check: {packet}
[INFO | ice_disp.py:116]	2022-01-05 13:35:54,969	> Try read packet...
[INFO | ice_disp.py:120]	2022-01-05 13:35:54,972	> reconnet to serialIceDispenser...
[INFO | ice_disp.py:176]	2022-01-05 13:35:55,039	> status check done
[INFO | ice_disp.py:48]	2022-01-05 13:36:01,974	> Event occurred! Event Type: 1, Args: None
[INFO | ice_disp.py:50]	2022-01-05 13:36:01,975	> ice serial is already opend!
[INFO | ice_disp.py:61]	2022-01-05 13:36:02,263	> Close icedisp serial done
[INFO | main_logic.py:363]	2022-01-05 13:36:10,950	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-05 13:36:22,263	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-05 13:36:22,667	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 13:36:22,768	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 13:36:22,769	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-05 13:36:33,344	> di idx 11 : 1
[INFO | main_logic.py:535]	2022-01-05 13:36:36,670	> Event on_barcode_listener called. Barcode: 2022010500260001
[INFO | main_logic.py:543]	2022-01-05 13:36:36,671	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-05 13:36:36,673	> State: False, The slot[1] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-05 13:36:36,674	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:409]	2022-01-05 13:36:38,790	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 13:36:38,792	> Set order state to DONE. PE_ID:2022010500260001
[INFO | main_logic.py:435]	2022-01-05 13:36:38,795	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 13:36:38,795	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-05 13:36:38,897	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 13:36:38,998	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-05 13:36:38,999	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-05 13:36:40,293	> Event on_barcode_listener called. Barcode: 2022010500260001
[INFO | main_logic.py:543]	2022-01-05 13:36:40,297	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 13:36:40,297	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 13:36:40,300	> Barcode: 2022010500260001, PE ID: 2022010500260001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 13:36:40,302	> Expired: False
[INFO | main_logic.py:543]	2022-01-05 13:36:40,305	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:535]	2022-01-05 13:36:40,856	> Event on_barcode_listener called. Barcode: 2022010500260001
[INFO | main_logic.py:543]	2022-01-05 13:36:40,857	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 13:36:40,859	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 13:36:40,862	> Barcode: 2022010500260001, PE ID: 2022010500260001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 13:36:40,862	> Expired: False
[INFO | main_logic.py:543]	2022-01-05 13:36:40,867	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-05 13:37:02,164	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-05 13:37:03,194	> Removed cup by customer. Index: 1
[INFO | main_logic.py:458]	2022-01-05 13:37:13,042	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-05 13:37:13,043	> Logic state <CLEAN> finish.
[DEBUG | main_logic.py:234]	2022-01-05 13:37:15,956	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010500260001, menu: ICED_AMERICANO
[INFO | main_logic.py:241]	2022-01-05 13:37:15,959	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010500260001, menu: ICED_AMERICANO
[INFO | main_logic.py:526]	2022-01-05 13:38:14,013	> Event on_kiosk_listener called. New Menu: AMERICANO, PEID: 2022010500270001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-05 13:38:17,028	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 13:38:17,029	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb5fde60c>
[INFO | main_logic.py:567]	2022-01-05 13:39:00,069	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 13:39:00,152	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 13:39:00,152	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 13:39:00,253	> Logic state <RECIPE> begin.
[INFO | main_logic.py:363]	2022-01-05 13:39:23,086	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-05 13:39:34,413	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-05 13:39:34,802	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 13:39:34,903	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 13:39:34,904	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-05 13:39:45,384	> di idx 11 : 1
[INFO | main_logic.py:409]	2022-01-05 13:39:50,923	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 13:39:50,925	> Set order state to DONE. PE_ID:2022010500270001
[INFO | main_logic.py:435]	2022-01-05 13:39:50,927	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 13:39:50,928	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-05 13:39:51,029	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 13:39:51,130	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-05 13:39:51,131	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-05 13:39:57,300	> Event on_barcode_listener called. Barcode: 2022010500270001
[INFO | main_logic.py:543]	2022-01-05 13:39:57,303	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 13:39:57,304	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 13:39:57,306	> Barcode: 2022010500270001, PE ID: 2022010500270001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 13:39:57,308	> Expired: False
[INFO | main_logic.py:543]	2022-01-05 13:39:57,312	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-05 13:40:01,981	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-05 13:40:02,972	> Removed cup by customer. Index: 1
[DEBUG | main_logic.py:234]	2022-01-05 13:40:15,713	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010500270001, menu: AMERICANO
[INFO | main_logic.py:241]	2022-01-05 13:40:15,717	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010500270001, menu: AMERICANO
[INFO | main_logic.py:458]	2022-01-05 13:40:25,171	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-05 13:40:25,172	> Logic state <CLEAN> finish.
[INFO | main_logic.py:526]	2022-01-05 13:47:20,318	> Event on_kiosk_listener called. New Menu: ICED_AMERICANO, PEID: 2022010500290001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-05 13:47:23,433	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 13:47:23,447	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb45c204c>
[INFO | main_logic.py:567]	2022-01-05 13:48:06,848	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 13:48:06,862	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 13:48:06,863	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 13:48:06,964	> Logic state <RECIPE> begin.
[INFO | ice_disp.py:48]	2022-01-05 13:48:10,496	> Event occurred! Event Type: 0, Args: <logics.coffee.Coffee object at 0xb45c204c>
[INFO | ice_disp.py:53]	2022-01-05 13:48:10,502	> create new icedisp serial
[INFO | ice_disp.py:106]	2022-01-05 13:48:10,503	> Called CheckIceDispenser
[INFO | ice_disp.py:107]	2022-01-05 13:48:10,504	> ice status check: {packet}
[INFO | ice_disp.py:116]	2022-01-05 13:48:10,515	> Try read packet...
[INFO | ice_disp.py:120]	2022-01-05 13:48:10,520	> reconnet to serialIceDispenser...
[INFO | ice_disp.py:176]	2022-01-05 13:48:10,587	> status check done
[INFO | ice_disp.py:48]	2022-01-05 13:48:17,511	> Event occurred! Event Type: 1, Args: None
[INFO | ice_disp.py:50]	2022-01-05 13:48:17,512	> ice serial is already opend!
[INFO | ice_disp.py:61]	2022-01-05 13:48:17,810	> Close icedisp serial done
[INFO | main_logic.py:363]	2022-01-05 13:48:26,490	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-05 13:48:37,807	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-05 13:48:38,207	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 13:48:38,308	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 13:48:38,309	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-05 13:48:48,953	> di idx 11 : 1
[INFO | main_logic.py:409]	2022-01-05 13:48:54,330	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 13:48:54,331	> Set order state to DONE. PE_ID:2022010500290001
[INFO | main_logic.py:435]	2022-01-05 13:48:54,334	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 13:48:54,335	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-05 13:48:54,436	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 13:48:54,537	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-05 13:48:54,538	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-05 13:49:05,970	> Event on_barcode_listener called. Barcode: 2022010500290001
[INFO | main_logic.py:543]	2022-01-05 13:49:05,971	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 13:49:05,973	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 13:49:05,976	> Barcode: 2022010500290001, PE ID: 2022010500290001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 13:49:05,976	> Expired: False
[INFO | main_logic.py:543]	2022-01-05 13:49:05,980	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-05 13:49:09,251	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-05 13:49:10,233	> Removed cup by customer. Index: 1
[DEBUG | main_logic.py:234]	2022-01-05 13:49:23,055	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010500290001, menu: ICED_AMERICANO
[INFO | main_logic.py:241]	2022-01-05 13:49:23,058	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010500290001, menu: ICED_AMERICANO
[INFO | main_logic.py:458]	2022-01-05 13:49:28,579	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-05 13:49:28,580	> Logic state <CLEAN> finish.
[INFO | main_logic.py:526]	2022-01-05 13:52:46,352	> Event on_kiosk_listener called. New Menu: AMERICANO, PEID: 2022010500300001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-05 13:52:51,948	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 13:52:51,957	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb4597c4c>
[INFO | main_logic.py:567]	2022-01-05 13:53:34,966	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 13:53:34,972	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 13:53:34,972	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 13:53:35,073	> Logic state <RECIPE> begin.
[INFO | main_logic.py:363]	2022-01-05 13:53:57,908	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-05 13:54:09,241	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-05 13:54:09,624	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 13:54:09,725	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 13:54:09,726	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-05 13:54:20,198	> di idx 11 : 1
[INFO | main_logic.py:409]	2022-01-05 13:54:25,748	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 13:54:25,750	> Set order state to DONE. PE_ID:2022010500300001
[INFO | main_logic.py:435]	2022-01-05 13:54:25,752	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 13:54:25,753	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-05 13:54:25,854	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 13:54:25,956	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-05 13:54:25,956	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-05 13:54:29,205	> Event on_barcode_listener called. Barcode: 2022010500300001
[INFO | main_logic.py:543]	2022-01-05 13:54:29,207	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 13:54:29,209	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 13:54:29,210	> Barcode: 2022010500300001, PE ID: 2022010500300001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 13:54:29,212	> Expired: False
[INFO | main_logic.py:543]	2022-01-05 13:54:29,215	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-05 13:54:34,565	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-05 13:54:35,556	> Removed cup by customer. Index: 1
[DEBUG | main_logic.py:234]	2022-01-05 13:54:48,318	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010500300001, menu: AMERICANO
[INFO | main_logic.py:241]	2022-01-05 13:54:48,322	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010500300001, menu: AMERICANO
[INFO | main_logic.py:458]	2022-01-05 13:54:59,996	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-05 13:54:59,997	> Logic state <CLEAN> finish.
[INFO | main_logic.py:526]	2022-01-05 13:55:22,465	> Event on_kiosk_listener called. New Menu: AMERICANO, PEID: 2022010500310001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-05 13:55:23,327	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 13:55:23,352	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb459722c>
[INFO | main_logic.py:567]	2022-01-05 13:56:06,391	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 13:56:06,453	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 13:56:06,454	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 13:56:06,555	> Logic state <RECIPE> begin.
[INFO | main_logic.py:363]	2022-01-05 13:56:29,388	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-05 13:56:40,700	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-05 13:56:41,106	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 13:56:41,207	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 13:56:41,207	> CM Slot[0] -> Lift Slot[1]
[INFO | main_logic.py:172]	2022-01-05 13:56:51,678	> di idx 11 : 1
[INFO | main_logic.py:409]	2022-01-05 13:56:57,228	> CM Slot[0] -> Lift Slot[1] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 13:56:57,229	> Set order state to DONE. PE_ID:2022010500310001
[INFO | main_logic.py:435]	2022-01-05 13:56:57,232	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 13:56:57,233	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-05 13:56:57,335	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 13:56:57,436	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-05 13:56:57,436	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-05 13:57:08,595	> Event on_barcode_listener called. Barcode: 2022010500310001
[INFO | main_logic.py:543]	2022-01-05 13:57:08,596	> State: False, The slot[0] is None. Skip this index.
[INFO | main_logic.py:541]	2022-01-05 13:57:08,596	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 13:57:08,600	> Barcode: 2022010500310001, PE ID: 2022010500310001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 13:57:08,601	> Expired: False
[INFO | main_logic.py:543]	2022-01-05 13:57:08,604	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:172]	2022-01-05 13:57:13,010	> di idx 11 : 0
[INFO | main_logic.py:203]	2022-01-05 13:57:14,002	> Removed cup by customer. Index: 1
[DEBUG | main_logic.py:234]	2022-01-05 13:57:26,637	> Removing Coffee confirmed : lift_index: 1, PE_ID: 2022010500310001, menu: AMERICANO
[INFO | main_logic.py:241]	2022-01-05 13:57:26,642	> State changed [2] -> [3], lift_index: 1, PE_ID: 2022010500310001, menu: AMERICANO
[INFO | main_logic.py:458]	2022-01-05 13:57:31,477	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-05 13:57:31,478	> Logic state <CLEAN> finish.
[WARNING | main_logic.py:129]	2022-01-05 14:08:56,819	> Stop button pushed. Requesting stop entire program from the co-routine in the main logic process.
[INFO | process_handler.py:81]	2022-01-05 14:08:56,878	> Shutting down...
[INFO | process_handler.py:86]	2022-01-05 14:08:56,879	> Disposing device 'Kiosk'...
[INFO | kiosk.py:94]	2022-01-05 14:08:56,880	> Kiosk - OnDispose
[INFO | kiosk.py:94]	2022-01-05 14:08:56,880	> Kiosk - Trying to disconnect to Database.
[INFO | kiosk.py:94]	2022-01-05 14:08:56,885	> Kiosk - Successfully disconnected to Database.
[INFO | kiosk.py:94]	2022-01-05 14:08:56,885	> Kiosk - OnDispose Done.
[INFO | process_handler.py:88]	2022-01-05 14:08:56,886	> Successfully disposed device 'Kiosk'
[INFO | process_handler.py:86]	2022-01-05 14:08:56,887	> Disposing device 'IceDispenser'...
[INFO | process_handler.py:88]	2022-01-05 14:08:56,888	> Successfully disposed device 'IceDispenser'
[INFO | process_handler.py:86]	2022-01-05 14:08:56,888	> Disposing device 'CupDispenser'...
[INFO | process_handler.py:88]	2022-01-05 14:08:56,897	> Successfully disposed device 'CupDispenser'
[INFO | process_handler.py:86]	2022-01-05 14:08:56,898	> Disposing device 'BarcodeReader'...
[INFO | barcode_reader.py:35]	2022-01-05 14:08:56,898	> BarcodeReader - OnDispose
[INFO | barcode_reader.py:37]	2022-01-05 14:08:56,899	> barcode thread end
[INFO | process_handler.py:88]	2022-01-05 14:08:56,900	> Successfully disposed device 'BarcodeReader'
[INFO | process_handler.py:94]	2022-01-05 14:08:56,908	> Shutting down...Done.
[INFO | process_handler.py:33]	2022-01-05 14:09:15,800	> Configurations_
{'robot_dof': 6, 'db_host': '192.168.10.22', 'db_name': 'KIOSK', 'db_user': 'NEUROMEKA', 'db_pwd': 'NEUROMEKA1234', 'db_timeout': 5, 'db_login_timeout': 5, 'db_charset': 'utf8', 'ice_only': 4, 'water_only': 0, 'ice_and_water': 1, 'coffee_map': {'00000001': 0, '00000002': 3, '00000003': 4, '00000004': 1, '00000005': 5, '00000006': 2}, 'coffee_expiry_time': 600, 'cup_disp_packet_len': 11, 'ice_disp_packet_len': 5, 'milk_refresh_duration': 4800, 'lift_delay': 10, 'lift_cup_delay': 1, 'espresso_machine_shot_delay_1': 6, 'espresso_machine_shot_delay_2': 6, 'espresso_machine_long_delay_1': 12, 'espresso_machine_long_delay_2': 12}
[INFO | process_handler.py:33]	2022-01-05 14:09:57,022	> Configurations_
{'robot_dof': 6, 'db_host': '192.168.10.22', 'db_name': 'KIOSK', 'db_user': 'NEUROMEKA', 'db_pwd': 'NEUROMEKA1234', 'db_timeout': 5, 'db_login_timeout': 5, 'db_charset': 'utf8', 'ice_only': 4, 'water_only': 0, 'ice_and_water': 1, 'coffee_map': {'00000001': 0, '00000002': 3, '00000003': 4, '00000004': 1, '00000005': 5, '00000006': 2}, 'coffee_expiry_time': 600, 'cup_disp_packet_len': 11, 'ice_disp_packet_len': 5, 'milk_refresh_duration': 4800, 'lift_delay': 10, 'lift_cup_delay': 1, 'espresso_machine_shot_delay_1': 6, 'espresso_machine_shot_delay_2': 6, 'espresso_machine_long_delay_1': 12, 'espresso_machine_long_delay_2': 12}
[INFO | process_handler.py:98]	2022-01-05 14:10:07,728	> Program started.
[INFO | process_handler.py:43]	2022-01-05 14:10:07,730	> Preparing program...
[INFO | process_handler.py:52]	2022-01-05 14:10:07,734	> initializing device '<class 'devices.kiosk.Kiosk'>'...
[DEBUG | process_handler.py:58]	2022-01-05 14:10:07,735	> Called on_create of device '<class 'devices.kiosk.Kiosk'>'
[INFO | kiosk.py:94]	2022-01-05 14:10:07,736	> Kiosk - OnCreate
[INFO | kiosk.py:94]	2022-01-05 14:10:07,736	> Kiosk - Trying to connect to Database - host: 192.168.10.22, db: KIOSK.
[INFO | kiosk.py:94]	2022-01-05 14:10:07,792	> Kiosk - Successfully connected to Database.
[INFO | kiosk.py:94]	2022-01-05 14:10:07,793	> Kiosk - OnCreate Done.
[DEBUG | process_handler.py:60]	2022-01-05 14:10:07,793	> on_create of device '<class 'devices.kiosk.Kiosk'>' done.
[INFO | process_handler.py:63]	2022-01-05 14:10:07,794	> Successfully initialized. Device name: Kiosk
[INFO | process_handler.py:52]	2022-01-05 14:10:07,795	> initializing device '<class 'devices.ice_disp.IceDispenser'>'...
[DEBUG | process_handler.py:58]	2022-01-05 14:10:07,795	> Called on_create of device '<class 'devices.ice_disp.IceDispenser'>'
[DEBUG | process_handler.py:60]	2022-01-05 14:10:07,798	> on_create of device '<class 'devices.ice_disp.IceDispenser'>' done.
[INFO | process_handler.py:63]	2022-01-05 14:10:07,799	> Successfully initialized. Device name: IceDispenser
[INFO | process_handler.py:52]	2022-01-05 14:10:07,800	> initializing device '<class 'devices.cup_disp.CupDispenser'>'...
[DEBUG | process_handler.py:58]	2022-01-05 14:10:07,800	> Called on_create of device '<class 'devices.cup_disp.CupDispenser'>'
[DEBUG | process_handler.py:60]	2022-01-05 14:10:07,804	> on_create of device '<class 'devices.cup_disp.CupDispenser'>' done.
[INFO | process_handler.py:63]	2022-01-05 14:10:07,805	> Successfully initialized. Device name: CupDispenser
[INFO | process_handler.py:52]	2022-01-05 14:10:07,805	> initializing device '<class 'devices.barcode_reader.BarcodeReader'>'...
[DEBUG | process_handler.py:58]	2022-01-05 14:10:07,806	> Called on_create of device '<class 'devices.barcode_reader.BarcodeReader'>'
[INFO | barcode_reader.py:26]	2022-01-05 14:10:07,807	> BarcodeReader - OnCreate
[INFO | barcode_reader.py:30]	2022-01-05 14:10:07,808	> barcode thread start
[DEBUG | process_handler.py:60]	2022-01-05 14:10:07,811	> on_create of device '<class 'devices.barcode_reader.BarcodeReader'>' done.
[INFO | process_handler.py:63]	2022-01-05 14:10:07,812	> Successfully initialized. Device name: BarcodeReader
[INFO | process_handler.py:75]	2022-01-05 14:10:07,814	> Preparing program...Done.
[INFO | main_logic.py:526]	2022-01-05 14:11:06,894	> Event on_kiosk_listener called. New Menu: AMERICANO, PEID: 2022010500320001, OJ_NO: 1
[INFO | main_logic.py:304]	2022-01-05 14:11:08,395	> Logic job retrieved <LogicState.PREPARE>.
[INFO | cup_disp.py:111]	2022-01-05 14:11:08,408	> Event occurred! Event Type: 1, Args: <logics.coffee.Coffee object at 0xb5f8f06c>
[INFO | main_logic.py:567]	2022-01-05 14:11:51,444	> Event on_prepare_done called.
[INFO | main_logic.py:341]	2022-01-05 14:11:51,519	> Logic state <PREPARE_DONE> begin.
[INFO | main_logic.py:342]	2022-01-05 14:11:51,520	> Logic state <PREPARE_DONE> finish.
[INFO | main_logic.py:345]	2022-01-05 14:11:51,621	> Logic state <RECIPE> begin.
[INFO | main_logic.py:363]	2022-01-05 14:12:14,455	> Logic state <RECIPE> finish.
[INFO | main_logic.py:554]	2022-01-05 14:12:25,787	> Event on_coffee_done called.
[INFO | main_logic.py:315]	2022-01-05 14:12:26,172	> Logic job retrieved <LogicState.LIFT>.
[INFO | main_logic.py:366]	2022-01-05 14:12:26,273	> Logic state <LIFT> begin.
[INFO | main_logic.py:391]	2022-01-05 14:12:26,274	> CM Slot[0] -> Lift Slot[0]
[INFO | main_logic.py:172]	2022-01-05 14:12:36,135	> di idx 10 : 1
[INFO | main_logic.py:409]	2022-01-05 14:12:41,293	> CM Slot[0] -> Lift Slot[0] - Logically done.
[INFO | main_logic.py:419]	2022-01-05 14:12:41,295	> Set order state to DONE. PE_ID:2022010500320001
[INFO | main_logic.py:435]	2022-01-05 14:12:41,297	> Clear job appended.
[INFO | main_logic.py:438]	2022-01-05 14:12:41,298	> Logic state <LIFT> finish.
[INFO | main_logic.py:319]	2022-01-05 14:12:41,399	> Logic job retrieved <LogicState.CLEAN>.
[INFO | main_logic.py:441]	2022-01-05 14:12:41,500	> Logic state <CLEAN> begin.
[INFO | main_logic.py:448]	2022-01-05 14:12:41,501	> Trying to clean filter - idx: 0 ...
[INFO | main_logic.py:535]	2022-01-05 14:12:46,419	> Event on_barcode_listener called. Barcode: 2022010500320001
[INFO | main_logic.py:541]	2022-01-05 14:12:46,420	> State: True, position: LIFT
[INFO | main_logic.py:546]	2022-01-05 14:12:46,423	> Barcode: 2022010500320001, PE ID: 2022010500320001, Compare: True
[INFO | main_logic.py:547]	2022-01-05 14:12:46,424	> Expired: False
[INFO | main_logic.py:543]	2022-01-05 14:12:46,430	> State: False, The slot[1] is None. Skip this index.
[INFO | main_logic.py:543]	2022-01-05 14:12:46,433	> State: False, The slot[2] is None. Skip this index.
[INFO | main_logic.py:458]	2022-01-05 14:13:15,543	> Trying to clean filter - idx: 0 ... Done.
[INFO | main_logic.py:460]	2022-01-05 14:13:15,544	> Logic state <CLEAN> finish.
[INFO | main_logic.py:172]	2022-01-05 14:13:28,284	> di idx 10 : 0
[INFO | main_logic.py:203]	2022-01-05 14:13:29,280	> Removed cup by customer. Index: 0
[DEBUG | main_logic.py:234]	2022-01-05 14:13:42,374	> Removing Coffee confirmed : lift_index: 0, PE_ID: 2022010500320001, menu: AMERICANO
[INFO | main_logic.py:241]	2022-01-05 14:13:42,378	> State changed [2] -> [3], lift_index: 0, PE_ID: 2022010500320001, menu: AMERICANO
user@Step-TP:~/release/TasksDeployment/PythonScript/events$ ls
event_args.py     __pycache__   worker.log.1   worker.log.3  worker.log.6  worker.log.9
event_manager.py  scheduler.py  worker.log.10  worker.log.4  worker.log.7  worker.py
__init__.py       worker.log    worker.log.2   worker.log.5  worker.log.8
user@Step-TP:~/release/TasksDeployment/PythonScript/events$  cd ..
user@Step-TP:~/release/TasksDeployment/PythonScript$ ls
config.backup.yml  context.py  examples    order.log           README.md         run_test.py     start.sh
Config.py          devices     indy_utils  process_handler.py  requirements.txt  service
config.yml         events      logics      __pycache__         run.py            service_backup
user@Step-TP:~/release/TasksDeployment/PythonScript$ cd logics
user@Step-TP:~/release/TasksDeployment/PythonScript/logics$ ls
coffee.py  mail.py  main_logic_backup.py  main_logic.py  __pycache__  recipe
user@Step-TP:~/release/TasksDeployment/PythonScript/logics$ vim main_logic.py


Press ENTER or type command to continue
user@Step-TP:~/release/TasksDeployment/PythonScript/logics$ vim main_logic.py
user@Step-TP:~/release/TasksDeployment/PythonScript/logics$ vim main_logic.py
user@Step-TP:~/release/TasksDeployment/PythonScript/logics$ vim main_logic.py
user@Step-TP:~/release/TasksDeployment/PythonScript/logics$ vim main_logic.py
user@Step-TP:~/release/TasksDeployment/PythonScript/logics$ vim main_logic.py
user@Step-TP:~/release/TasksDeployment/PythonScript/logics$ ls
coffee.py  mail.py  main_logic_backup.py  main_logic.py  __pycache__  recipe
user@Step-TP:~/release/TasksDeployment/PythonScript/logics$ cd ..
user@Step-TP:~/release/TasksDeployment/PythonScript$ ls
config.backup.yml  context.py  examples    order.log           README.md         run_test.py     start.sh
Config.py          devices     indy_utils  process_handler.py  requirements.txt  service
config.yml         events      logics      __pycache__         run.py            service_backup
user@Step-TP:~/release/TasksDeployment/PythonScript$ vim Config.py 
user@Step-TP:~/release/TasksDeployment/PythonScript$ vim config.yml
user@Step-TP:~/release/TasksDeployment/PythonScript$ ls
config.backup.yml  context.py  examples    order.log           README.md         run_test.py     start.sh
Config.py          devices     indy_utils  process_handler.py  requirements.txt  service
config.yml         events      logics      __pycache__         run.py            service_backup
user@Step-TP:~/release/TasksDeployment/PythonScript$ cd ..
user@Step-TP:~/release/TasksDeployment$ cd PythonScript
user@Step-TP:~/release/TasksDeployment/PythonScript$ ls
config.backup.yml  context.py  examples    order.log           README.md         run_test.py     start.sh
Config.py          devices     indy_utils  process_handler.py  requirements.txt  service
config.yml         events      logics      __pycache__         run.py            service_backup
user@Step-TP:~/release/TasksDeployment/PythonScript$ cd logics
user@Step-TP:~/release/TasksDeployment/PythonScript/logics$ ls
coffee.py  mail.py  main_logic_backup.py  main_logic.py  __pycache__  recipe
user@Step-TP:~/release/TasksDeployment/PythonScript/logics$ vim main_logic.pyt
user@Step-TP:~/release/TasksDeployment/PythonScript/logics$ vim main_logic.py
user@Step-TP:~/release/TasksDeployment/PythonScript/logics$ vim main_logic.py
user@Step-TP:~/release/TasksDeployment/PythonScript/logics$ vim main_logic.py

  3 from Config import *
  4 from events.scheduler import Job, Scheduler
  5 from events.event_args import EventArgs
  6 from logics.recipe.americano import is_using_milk
  7 from .recipe.event_args import *
  8 from devices.cup_disp import CupDispenser
  9 from devices.ice_disp import IceDispenser
 10 from devices.kiosk import Coffee, Kiosk, KioskEventArgs
 11 from logging import FileHandler, Logger, StreamHandler
 12 from logging.handlers import RotatingFileHandler
 13 import events, logging
 14 from context import Context
 15 from enum import Enum, auto
 16 from queue import Queue, PriorityQueue
 17 from . import recipe
 18 from datetime import datetime as dt, timedelta
 19 import time
 20 from . import mail
 21 import os
 22 import os.path
 23 from fcntl import ioctl
 24 
 25 
 26 test_mode = False
 27 
 28 class LogicState(Enum):
 29     IDLE                = auto()
 30     PREPARE             = auto()
 31     PREPARE_DONE        = auto()
 32     RECIPE              = auto()
 33     RECIPE_DONE         = auto()
 34     LIFT                = auto()
 35     CLEAN               = auto()
                                                                                                    3,1            0%
