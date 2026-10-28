- [Conor Lloyd-Wood] — Recorded, edited, and narrated the demo video (screen capture, 
  editing, voiceover script, and recording).
- [Maneeshka Thakur] — created and implemented the adversarial audit script (attacker.py) and tested port hijacking and heartbeat spoofing. Additionally, contributed to the PDF report by adding to the adversarial audit summary section.

-[Part 2]

- [Conor Lloyd-Wood] — Extended heartbeat.py (Part 1) to implement Task 3,
  Automated Failover Coordination. Refactored heartbeat-check logic into a
  reusable ping_ok() function, added a log() helper for consistent
  timestamped logging to both console and heartbeat.log, and implemented
  trigger_failover(), which automatically spawns backup_service.py the
  moment the missed-heartbeat threshold is crossed and verifies the standby
  is responding before confirming recovery. Tested and verified the full
  [Crash Detected] -> [Failover Triggered] -> [Service Restored] sequence
  with no manual intervention.
