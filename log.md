aio@gaio-Aspire-A515-56:~/SAGEDRAL-ML-Smart-Adaptive-Guardian-for-Detection-Response-and-Adaptive-Learning-ML$ sudo cat /var/log/sagedral-ml.log
2026-10-03 19:18:14,619 [INFO] sagedral_ml.main: === Starting SAGEDRAL-ML NIDPS System ===
2026-10-03 19:18:14,633 [INFO] sagedral_ml.detection.ml: Successfully loaded ML detection models.
2026-10-03 19:18:14,679 [INFO] sagedral_ml.ips.response: nftables table 'inet sagedral' initialized.
2026-10-03 19:18:14,724 [WARNING] sagedral_ml.database.connection: alembic.ini not found at /opt/sagedral-ml/venv/lib/python3.12/site-packages/alembic.ini; using create_all compatibility path.
2026-10-03 19:18:14,742 [INFO] sagedral_ml.detection.signature: Loaded 0 custom signature rules from database.
2026-10-03 19:18:14,742 [INFO] sagedral_ml.main: Loaded 0 custom signature rule(s) from database.
2026-10-03 19:18:14,744 [INFO] sagedral_ml.ips.response: Reconciling 0 active blocked IPs from database...
2026-10-03 19:18:14,744 [INFO] sagedral_ml.ips.response: IPS reconcile complete: success=0, skipped_whitelisted=0, failed=0
2026-10-03 19:18:14,744 [INFO] sagedral_ml.main: Processing worker thread started.
2026-10-03 19:18:14,744 [INFO] sagedral_ml.main: Starting packet capture on interface 'enxc817f57cadc8' (explicit='enxc817f57cadc8')
2026-10-03 19:18:14,745 [INFO] sagedral_ml.main: Starting FastAPI Web Server & Dashboard at http://0.0.0.0:8000
2026-10-03 19:18:14,759 [INFO] sagedral_ml.capture.sniffer: AF_PACKET PACKET_RX_RING started on enxc817f57cadc8 (4096 frames).
2026-10-03 19:18:14,760 [INFO] sagedral_ml.main: Capture thread active on 'enxc817f57cadc8' (restart #0)
2026-10-03 19:18:14,773 [INFO] sagedral_ml.api: Initializing SAGEDRAL-ML API server...
2026-10-03 19:18:14,774 [WARNING] sagedral_ml.database.connection: alembic.ini not found at /opt/sagedral-ml/venv/lib/python3.12/site-packages/alembic.ini; using create_all compatibility path.
2026-10-03 19:18:14,777 [INFO] sagedral_ml.auth.security: Admin user 'admin' sudah ada. Skip seeding.
2026-10-03 19:18:15,396 [INFO] sagedral_ml.api.websocket: WebSocket client connected. Total active connections: 1
2026-10-03 19:18:15,406 [INFO] sagedral_ml.api.websocket: WebSocket client connected. Total active connections: 2
2026-10-03 19:18:15,412 [INFO] sagedral_ml.api.websocket: WebSocket client connected. Total active connections: 3
2026-10-03 19:18:15,418 [INFO] sagedral_ml.api.websocket: WebSocket client connected. Total active connections: 4
2026-10-03 19:18:15,421 [INFO] sagedral_ml.api.websocket: WebSocket client connected. Total active connections: 5
2026-10-03 19:18:15,424 [INFO] sagedral_ml.api.websocket: WebSocket client connected. Total active connections: 6
2026-10-03 19:18:15,428 [INFO] sagedral_ml.api.websocket: WebSocket client connected. Total active connections: 7
2026-10-03 19:18:15,431 [INFO] sagedral_ml.api.websocket: WebSocket client connected. Total active connections: 8
2026-10-03 19:18:16,520 [INFO] sagedral_ml.api.websocket: WebSocket client connected. Total active connections: 9
2026-10-03 19:18:16,909 [INFO] sagedral_ml.api.websocket: WebSocket client connected. Total active connections: 10
2026-10-03 19:18:17,753 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.118.4', 50292, 443, 6) (pkts=7)
2026-10-03 19:18:17,765 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.005577328278574953, final_score=0.003346396967144972, is_threat=False, action=ALLOW
2026-10-03 19:18:17,834 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.118.4', '10.10.10.2', 443, 50292, 6) (pkts=1)
2026-10-03 19:18:17,836 [INFO] sagedral_ml.detection.decision: Decision for 172.217.118.4: sig_score=0.0, ml_score=0.006122575298292739, final_score=0.0036735451789756436, is_threat=False, action=ALLOW
2026-10-03 19:18:17,914 [INFO] sagedral_ml.api.websocket: WebSocket client connected. Total active connections: 11
2026-10-03 19:18:27,307 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('72.153.5.60', '10.10.10.2', 443, 50268, 6) (pkts=1)
2026-10-03 19:18:27,310 [INFO] sagedral_ml.detection.decision: Decision for 72.153.5.60: sig_score=0.0, ml_score=0.006122575298292739, final_score=0.0036735451789756436, is_threat=False, action=ALLOW
2026-10-03 19:18:30,442 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.112.4', 50229, 443, 6) (pkts=3)
2026-10-03 19:18:30,444 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.005412055482057169, final_score=0.0032472332892343014, is_threat=False, action=ALLOW
2026-10-03 19:18:30,445 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.112.4', 50229, 443, 6) (pkts=3)
2026-10-03 19:18:30,445 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.03229144455996398, final_score=0.019374866735978387, is_threat=False, action=ALLOW
2026-10-03 19:18:30,508 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.112.4', '10.10.10.2', 443, 50229, 6) (pkts=1)
2026-10-03 19:18:30,510 [INFO] sagedral_ml.detection.decision: Decision for 172.217.112.4: sig_score=0.0, ml_score=0.006122575298292739, final_score=0.0036735451789756436, is_threat=False, action=ALLOW
2026-10-03 19:18:30,512 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.112.4', '10.10.10.2', 443, 50229, 6) (pkts=1)
2026-10-03 19:18:30,515 [INFO] sagedral_ml.detection.decision: Decision for 172.217.112.4: sig_score=0.0, ml_score=0.006122575298292739, final_score=0.0036735451789756436, is_threat=False, action=ALLOW
2026-10-03 19:18:52,372 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.118.4', 50282, 443, 6) (pkts=4)
2026-10-03 19:18:52,375 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.006158347598924968, final_score=0.003695008559354981, is_threat=False, action=ALLOW
2026-10-03 19:18:52,471 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.118.4', '10.10.10.2', 443, 50282, 6) (pkts=3)
2026-10-03 19:18:52,474 [INFO] sagedral_ml.detection.decision: Decision for 172.217.118.4: sig_score=0.0, ml_score=0.005713624548923921, final_score=0.0034281747293543525, is_threat=False, action=ALLOW
2026-10-03 19:18:56,067 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.70.132', 50288, 443, 6) (pkts=4)
2026-10-03 19:18:56,069 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.006158347598924968, final_score=0.003695008559354981, is_threat=False, action=ALLOW
2026-10-03 19:18:56,148 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.70.132', '10.10.10.2', 443, 50288, 6) (pkts=3)
2026-10-03 19:18:56,150 [INFO] sagedral_ml.detection.decision: Decision for 172.217.70.132: sig_score=0.0, ml_score=0.005713624548923921, final_score=0.0034281747293543525, is_threat=False, action=ALLOW
2026-10-03 19:19:11,206 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.118.4', 50272, 443, 6) (pkts=4)
2026-10-03 19:19:11,208 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.006158347598924968, final_score=0.003695008559354981, is_threat=False, action=ALLOW
2026-10-03 19:19:11,310 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.118.4', '10.10.10.2', 443, 50272, 6) (pkts=3)
2026-10-03 19:19:11,312 [INFO] sagedral_ml.detection.decision: Decision for 172.217.118.4: sig_score=0.0, ml_score=0.005713624548923921, final_score=0.0034281747293543525, is_threat=False, action=ALLOW
2026-10-03 19:19:23,690 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '4.150.223.97', 50281, 443, 6) (pkts=3)
2026-10-03 19:19:23,692 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.005412055482057169, final_score=0.0032472332892343014, is_threat=False, action=ALLOW
2026-10-03 19:19:36,176 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '4.150.223.97', 50279, 443, 6) (pkts=5)
2026-10-03 19:19:36,179 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.005412055482057169, final_score=0.0032472332892343014, is_threat=False, action=ALLOW
2026-10-03 19:19:41,519 [INFO] sagedral_ml.api: SAGEDRAL-ML API server shutdown.
2026-10-03 19:19:41,519 [INFO] sagedral_ml.main: Signal received: shutting down SAGEDRAL-ML...
2026-10-03 19:19:41,613 [INFO] sagedral_ml.main: Processing worker thread exiting.
2026-10-03 19:19:41,786 [INFO] sagedral_ml.main: Capture thread exiting.
2026-10-03 19:19:44,624 [INFO] sagedral_ml.main: === Starting SAGEDRAL-ML NIDPS System ===
2026-10-03 19:19:44,637 [INFO] sagedral_ml.detection.ml: Successfully loaded ML detection models.
2026-10-03 19:19:44,686 [INFO] sagedral_ml.ips.response: nftables table 'inet sagedral' initialized.
2026-10-03 19:19:44,732 [WARNING] sagedral_ml.database.connection: alembic.ini not found at /opt/sagedral-ml/venv/lib/python3.12/site-packages/alembic.ini; using create_all compatibility path.
2026-10-03 19:19:44,749 [INFO] sagedral_ml.detection.signature: Loaded 0 custom signature rules from database.
2026-10-03 19:19:44,749 [INFO] sagedral_ml.main: Loaded 0 custom signature rule(s) from database.
2026-10-03 19:19:44,750 [INFO] sagedral_ml.ips.response: Reconciling 0 active blocked IPs from database...
2026-10-03 19:19:44,750 [INFO] sagedral_ml.ips.response: IPS reconcile complete: success=0, skipped_whitelisted=0, failed=0
2026-10-03 19:19:44,751 [INFO] sagedral_ml.main: Processing worker thread started.
2026-10-03 19:19:44,751 [INFO] sagedral_ml.main: Starting packet capture on interface 'enxc817f57cadc8' (explicit='enxc817f57cadc8')
2026-10-03 19:19:44,751 [INFO] sagedral_ml.main: Starting FastAPI Web Server & Dashboard at http://0.0.0.0:8000
2026-10-03 19:19:44,771 [INFO] sagedral_ml.capture.sniffer: AF_PACKET PACKET_RX_RING started on enxc817f57cadc8 (4096 frames).
2026-10-03 19:19:44,771 [INFO] sagedral_ml.main: Capture thread active on 'enxc817f57cadc8' (restart #0)
2026-10-03 19:19:44,778 [INFO] sagedral_ml.api: Initializing SAGEDRAL-ML API server...
2026-10-03 19:19:44,779 [WARNING] sagedral_ml.database.connection: alembic.ini not found at /opt/sagedral-ml/venv/lib/python3.12/site-packages/alembic.ini; using create_all compatibility path.
2026-10-03 19:19:44,782 [INFO] sagedral_ml.auth.security: Admin user 'admin' sudah ada. Skip seeding.
2026-10-03 19:19:44,937 [INFO] sagedral_ml.api.websocket: WebSocket client connected. Total active connections: 1
2026-10-03 19:19:45,429 [INFO] sagedral_ml.api.websocket: WebSocket client connected. Total active connections: 2
2026-10-03 19:19:45,433 [INFO] sagedral_ml.api.websocket: WebSocket client connected. Total active connections: 3
2026-10-03 19:19:45,440 [INFO] sagedral_ml.api.websocket: WebSocket client connected. Total active connections: 4
2026-10-03 19:19:45,444 [INFO] sagedral_ml.api.websocket: WebSocket client connected. Total active connections: 5
2026-10-03 19:19:45,446 [INFO] sagedral_ml.api.websocket: WebSocket client connected. Total active connections: 6
2026-10-03 19:19:45,449 [INFO] sagedral_ml.api.websocket: WebSocket client connected. Total active connections: 7
2026-10-03 19:19:45,453 [INFO] sagedral_ml.api.websocket: WebSocket client connected. Total active connections: 8
2026-10-03 19:19:45,456 [INFO] sagedral_ml.api.websocket: WebSocket client connected. Total active connections: 9
2026-10-03 19:19:45,459 [INFO] sagedral_ml.api.websocket: WebSocket client connected. Total active connections: 10
2026-10-03 19:19:47,434 [INFO] sagedral_ml.api.websocket: WebSocket client connected. Total active connections: 11
2026-10-03 19:19:52,000 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.118.4', '10.10.10.2', 443, 50204, 6) (pkts=1)
2026-10-03 19:19:52,013 [INFO] sagedral_ml.detection.decision: Decision for 172.217.118.4: sig_score=0.0, ml_score=0.006122575298292739, final_score=0.0036735451789756436, is_threat=False, action=ALLOW
2026-10-03 19:19:52,014 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.118.4', 50204, 443, 6) (pkts=3)
2026-10-03 19:19:52,015 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.03229144455996398, final_score=0.019374866735978387, is_threat=False, action=ALLOW
2026-10-03 19:19:52,076 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.118.4', '10.10.10.2', 443, 50204, 6) (pkts=1)
2026-10-03 19:19:52,078 [INFO] sagedral_ml.detection.decision: Decision for 172.217.118.4: sig_score=0.0, ml_score=0.006122575298292739, final_score=0.0036735451789756436, is_threat=False, action=ALLOW
2026-10-03 19:19:53,954 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('150.171.110.97', '10.10.10.2', 443, 50293, 6) (pkts=3)
2026-10-03 19:19:53,956 [INFO] sagedral_ml.detection.decision: Decision for 150.171.110.97: sig_score=0.0, ml_score=0.009430748642857511, final_score=0.0056584491857145066, is_threat=False, action=ALLOW
2026-10-03 19:19:53,957 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '150.171.110.97', 50293, 443, 6) (pkts=2)
2026-10-03 19:19:53,959 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.006735505057332356, final_score=0.0040413030343994134, is_threat=False, action=ALLOW
2026-10-03 19:20:24,156 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('52.123.129.14', '10.10.10.2', 443, 50294, 6) (pkts=1)
2026-10-03 19:20:24,158 [INFO] sagedral_ml.detection.decision: Decision for 52.123.129.14: sig_score=0.0, ml_score=0.006122575298292739, final_score=0.0036735451789756436, is_threat=False, action=ALLOW
2026-10-03 19:20:48,072 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.118.4', 50296, 443, 6) (pkts=1000)
2026-10-03 19:20:48,076 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.048455726387398486, final_score=0.02907343583243909, is_threat=False, action=ALLOW
2026-10-03 19:20:55,739 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '91.189.91.97', 39686, 80, 6) (pkts=6)
2026-10-03 19:20:55,742 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.08526101748370411, final_score=0.051156610490222465, is_threat=False, action=ALLOW
2026-10-03 19:20:55,742 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('91.189.91.97', '10.10.10.2', 80, 39686, 6) (pkts=1)
2026-10-03 19:20:55,743 [INFO] sagedral_ml.detection.decision: Decision for 91.189.91.97: sig_score=0.0, ml_score=0.006122575298292739, final_score=0.0036735451789756436, is_threat=False, action=ALLOW
2026-10-03 19:20:55,743 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '91.189.91.97', 39686, 80, 6) (pkts=2)
2026-10-03 19:20:55,744 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.10729536647158561, final_score=0.06437721988295136, is_threat=False, action=ALLOW
2026-10-03 19:20:56,053 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('91.189.91.97', '10.10.10.2', 80, 39686, 6) (pkts=1)
2026-10-03 19:20:56,055 [INFO] sagedral_ml.detection.decision: Decision for 91.189.91.97: sig_score=0.0, ml_score=0.006122575298292739, final_score=0.0036735451789756436, is_threat=False, action=ALLOW
2026-10-03 19:20:56,056 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('91.189.91.97', '10.10.10.2', 80, 39686, 6) (pkts=1)
2026-10-03 19:20:56,058 [INFO] sagedral_ml.detection.decision: Decision for 91.189.91.97: sig_score=0.0, ml_score=0.006122575298292739, final_score=0.0036735451789756436, is_threat=False, action=ALLOW
2026-10-03 19:20:59,760 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.118.4', 50289, 443, 6) (pkts=1000)
2026-10-03 19:20:59,761 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.07579740884602564, final_score=0.04547844530761538, is_threat=False, action=ALLOW
2026-10-03 19:21:04,993 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.118.4', 50296, 443, 6) (pkts=1000)
2026-10-03 19:21:04,998 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.04500792772019535, final_score=0.02700475663211721, is_threat=False, action=ALLOW
2026-10-03 19:21:11,410 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.118.4', 50296, 443, 6) (pkts=1000)
2026-10-03 19:21:11,414 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.04500792772019535, final_score=0.02700475663211721, is_threat=False, action=ALLOW
2026-10-03 19:21:15,054 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:21:15,054 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:21:15,054 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.010888203058543083, final_score=0.006532921835125849, is_threat=False, action=ALLOW
2026-10-03 19:21:15,055 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.010888203058543083, final_score=0.006532921835125849, is_threat=False, action=ALLOW
2026-10-03 19:21:15,055 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.010888203058543083, final_score=0.006532921835125849, is_threat=False, action=ALLOW
2026-10-03 19:21:15,055 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.005412055482057169, final_score=0.0032472332892343014, is_threat=False, action=ALLOW
2026-10-03 19:21:15,055 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.01016695710115561, final_score=0.006100174260693366, is_threat=False, action=ALLOW
2026-10-03 19:21:15,056 [INFO] sagedral_ml.detection.decision: Decision for fe80::4223:82a:8259:fdde: sig_score=0.0, ml_score=0.05969060557934208, final_score=0.035814363347605245, is_threat=False, action=ALLOW
2026-10-03 19:21:15,056 [INFO] sagedral_ml.detection.decision: Decision for 192.168.88.18: sig_score=0.0, ml_score=0.05969060557934208, final_score=0.035814363347605245, is_threat=False, action=ALLOW
2026-10-03 19:21:15,056 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:21:15,056 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:21:18,242 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.118.4', 50296, 443, 6) (pkts=1000)
2026-10-03 19:21:18,245 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.04500792772019535, final_score=0.02700475663211721, is_threat=False, action=ALLOW
2026-10-03 19:21:25,567 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.112.4', 50287, 443, 6) (pkts=13)
2026-10-03 19:21:25,572 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0054116947627556936, final_score=0.003247016857653416, is_threat=False, action=ALLOW
2026-10-03 19:21:25,580 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.112.4', 50287, 443, 6) (pkts=3)
2026-10-03 19:21:25,583 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.03229144455996398, final_score=0.019374866735978387, is_threat=False, action=ALLOW
2026-10-03 19:21:25,641 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.112.4', '10.10.10.2', 443, 50287, 6) (pkts=1)
2026-10-03 19:21:25,644 [INFO] sagedral_ml.detection.decision: Decision for 172.217.112.4: sig_score=0.0, ml_score=0.006122575298292739, final_score=0.0036735451789756436, is_threat=False, action=ALLOW
2026-10-03 19:21:25,645 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.112.4', '10.10.10.2', 443, 50287, 6) (pkts=1)
2026-10-03 19:21:25,647 [INFO] sagedral_ml.detection.decision: Decision for 172.217.112.4: sig_score=0.0, ml_score=0.006122575298292739, final_score=0.0036735451789756436, is_threat=False, action=ALLOW
2026-10-03 19:21:27,360 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.118.4', 50291, 443, 6) (pkts=1000)
2026-10-03 19:21:27,363 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.07579740884602564, final_score=0.04547844530761538, is_threat=False, action=ALLOW
2026-10-03 19:21:34,803 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.118.4', 50296, 443, 6) (pkts=1000)
2026-10-03 19:21:34,805 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.04500792772019535, final_score=0.02700475663211721, is_threat=False, action=ALLOW
2026-10-03 19:21:45,086 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:21:45,086 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.01016695710115561, final_score=0.006100174260693366, is_threat=False, action=ALLOW
2026-10-03 19:21:45,086 [INFO] sagedral_ml.detection.decision: Decision for fe80::bc2b:9333:90a:dab8: sig_score=0.0, ml_score=0.9585319979911209, final_score=0.5751191987946725, is_threat=True, action=ALERT
2026-10-03 19:21:45,090 [INFO] sagedral_ml.detection.decision: Decision for 192.168.88.245: sig_score=0.0, ml_score=0.9289579408600622, final_score=0.5573747645160373, is_threat=True, action=ALERT
2026-10-03 19:21:45,096 [INFO] sagedral_ml.detection.decision: Decision for 192.168.88.245: sig_score=0.0, ml_score=0.02155674709742763, final_score=0.012934048258456577, is_threat=False, action=ALLOW
2026-10-03 19:21:45,096 [INFO] sagedral_ml.detection.decision: Decision for fe80::bc2b:9333:90a:dab8: sig_score=0.0, ml_score=0.02155674709742763, final_score=0.012934048258456577, is_threat=False, action=ALLOW
2026-10-03 19:21:45,096 [INFO] sagedral_ml.detection.decision: Decision for fe80::bc2b:9333:90a:dab8: sig_score=0.0, ml_score=0.008626266912121355, final_score=0.005175760147272813, is_threat=False, action=ALLOW
2026-10-03 19:21:45,097 [INFO] sagedral_ml.detection.decision: Decision for 192.168.88.245: sig_score=0.0, ml_score=0.008251085736842865, final_score=0.004950651442105719, is_threat=False, action=ALLOW
2026-10-03 19:21:45,097 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:21:45,097 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:21:45,097 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:21:45,098 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:21:45,098 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:21:46,674 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.118.4', 50296, 443, 6) (pkts=1000)
2026-10-03 19:21:46,681 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.04500792772019535, final_score=0.02700475663211721, is_threat=False, action=ALLOW
2026-10-03 19:21:46,956 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.118.4', 50291, 443, 6) (pkts=1000)
2026-10-03 19:21:46,959 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.07579740884602564, final_score=0.04547844530761538, is_threat=False, action=ALLOW
2026-10-03 19:21:53,439 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.118.4', 50296, 443, 6) (pkts=1000)
2026-10-03 19:21:53,444 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.04500792772019535, final_score=0.02700475663211721, is_threat=False, action=ALLOW
2026-10-03 19:22:08,559 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.118.4', '10.10.10.2', 443, 50289, 6) (pkts=1000)
2026-10-03 19:22:08,564 [INFO] sagedral_ml.detection.decision: Decision for 172.217.118.4: sig_score=0.0, ml_score=0.09581036052543766, final_score=0.057486216315262594, is_threat=False, action=ALLOW
2026-10-03 19:22:09,389 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.117.4', 60132, 443, 6) (pkts=57)
2026-10-03 19:22:09,392 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.006770801183912594, final_score=0.004062480710347556, is_threat=False, action=ALLOW
2026-10-03 19:22:10,200 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.118.4', 50296, 443, 6) (pkts=1000)
2026-10-03 19:22:10,206 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.04500792772019535, final_score=0.02700475663211721, is_threat=False, action=ALLOW
2026-10-03 19:22:15,159 [INFO] sagedral_ml.detection.decision: Decision for 192.168.88.245: sig_score=0.0, ml_score=0.03537498040725834, final_score=0.021224988244355, is_threat=False, action=ALLOW
2026-10-03 19:22:15,159 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:22:15,159 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.005774457704507509, final_score=0.003464674622704505, is_threat=False, action=ALLOW
2026-10-03 19:22:15,159 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.01016695710115561, final_score=0.006100174260693366, is_threat=False, action=ALLOW
2026-10-03 19:22:15,160 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.005774457704507509, final_score=0.003464674622704505, is_threat=False, action=ALLOW
2026-10-03 19:22:15,160 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:22:15,160 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:22:15,160 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:22:15,160 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:22:15,160 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:22:15,160 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:22:15,585 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.118.4', 50291, 443, 6) (pkts=1000)
2026-10-03 19:22:15,587 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.048455726387398486, final_score=0.02907343583243909, is_threat=False, action=ALLOW
2026-10-03 19:22:16,770 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.118.4', 50296, 443, 6) (pkts=1000)
2026-10-03 19:22:16,778 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.04500792772019535, final_score=0.02700475663211721, is_threat=False, action=ALLOW
2026-10-03 19:22:26,432 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.118.4', '10.10.10.2', 443, 50291, 6) (pkts=303)
2026-10-03 19:22:26,435 [INFO] sagedral_ml.detection.decision: Decision for 172.217.118.4: sig_score=0.0, ml_score=0.017276111097139023, final_score=0.010365666658283413, is_threat=False, action=ALLOW
2026-10-03 19:22:26,655 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.118.4', '10.10.10.2', 443, 50291, 6) (pkts=3)
2026-10-03 19:22:26,656 [INFO] sagedral_ml.detection.decision: Decision for 172.217.118.4: sig_score=0.0, ml_score=0.005713624548923921, final_score=0.0034281747293543525, is_threat=False, action=ALLOW
2026-10-03 19:22:27,146 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.115.4', 50308, 443, 6) (pkts=49)
2026-10-03 19:22:27,148 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.00955247523849631, final_score=0.005731485143097786, is_threat=False, action=ALLOW
2026-10-03 19:22:27,210 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.115.4', '10.10.10.2', 443, 50308, 6) (pkts=3)
2026-10-03 19:22:27,213 [INFO] sagedral_ml.detection.decision: Decision for 172.217.115.4: sig_score=0.0, ml_score=0.005713624548923921, final_score=0.0034281747293543525, is_threat=False, action=ALLOW
2026-10-03 19:22:28,777 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.118.4', '10.10.10.2', 443, 50296, 6) (pkts=1000)
2026-10-03 19:22:28,782 [INFO] sagedral_ml.detection.decision: Decision for 172.217.118.4: sig_score=0.0, ml_score=0.01827985786871909, final_score=0.010967914721231454, is_threat=False, action=ALLOW
2026-10-03 19:22:30,564 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.115.4', 50303, 443, 6) (pkts=20)
2026-10-03 19:22:30,567 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.00857320215810379, final_score=0.0051439212948622744, is_threat=False, action=ALLOW
2026-10-03 19:22:30,668 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.115.4', '10.10.10.2', 443, 50303, 6) (pkts=1)
2026-10-03 19:22:30,670 [INFO] sagedral_ml.detection.decision: Decision for 172.217.115.4: sig_score=0.0, ml_score=0.006122575298292739, final_score=0.0036735451789756436, is_threat=False, action=ALLOW
2026-10-03 19:22:31,081 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.117.4', 50306, 443, 6) (pkts=21)
2026-10-03 19:22:31,084 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.00857320215810379, final_score=0.0051439212948622744, is_threat=False, action=ALLOW
2026-10-03 19:22:31,161 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.117.4', '10.10.10.2', 443, 50306, 6) (pkts=1)
2026-10-03 19:22:31,165 [INFO] sagedral_ml.detection.decision: Decision for 172.217.117.4: sig_score=0.0, ml_score=0.006122575298292739, final_score=0.0036735451789756436, is_threat=False, action=ALLOW
2026-10-03 19:22:35,821 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.115.4', 50302, 443, 6) (pkts=66)
2026-10-03 19:22:35,823 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.00955247523849631, final_score=0.005731485143097786, is_threat=False, action=ALLOW
2026-10-03 19:22:35,902 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.115.4', '10.10.10.2', 443, 50302, 6) (pkts=1)
2026-10-03 19:22:35,906 [INFO] sagedral_ml.detection.decision: Decision for 172.217.115.4: sig_score=0.0, ml_score=0.006122575298292739, final_score=0.0036735451789756436, is_threat=False, action=ALLOW
2026-10-03 19:22:44,062 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.118.4', 50289, 443, 6) (pkts=567)
2026-10-03 19:22:44,065 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.09760172970591209, final_score=0.058561037823547255, is_threat=False, action=ALLOW
2026-10-03 19:22:44,149 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.118.4', '10.10.10.2', 443, 50289, 6) (pkts=3)
2026-10-03 19:22:44,151 [INFO] sagedral_ml.detection.decision: Decision for 172.217.118.4: sig_score=0.0, ml_score=0.005713624548923921, final_score=0.0034281747293543525, is_threat=False, action=ALLOW
2026-10-03 19:22:45,718 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:22:45,719 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:22:45,719 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:22:45,720 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:22:45,720 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:22:45,720 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.00602942933497465, final_score=0.0036176576009847895, is_threat=False, action=ALLOW
2026-10-03 19:22:45,720 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:22:50,307 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.118.4', 50296, 443, 6) (pkts=1000)
2026-10-03 19:22:50,313 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.04500792772019535, final_score=0.02700475663211721, is_threat=False, action=ALLOW
2026-10-03 19:22:55,744 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '64.233.170.188', 50263, 5228, 6) (pkts=9)
2026-10-03 19:22:55,746 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.020441271410491044, final_score=0.012264762846294627, is_threat=False, action=ALLOW
2026-10-03 19:22:55,746 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '74.125.130.188', 50262, 5228, 6) (pkts=9)
2026-10-03 19:22:55,748 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.014093950540423785, final_score=0.00845637032425427, is_threat=False, action=ALLOW
2026-10-03 19:22:55,749 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.194.188', 50264, 5228, 6) (pkts=9)
2026-10-03 19:22:55,750 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.014093950540423785, final_score=0.00845637032425427, is_threat=False, action=ALLOW
2026-10-03 19:22:56,182 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '4.213.25.242', 50265, 443, 6) (pkts=15)
2026-10-03 19:22:56,184 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.007201737338377244, final_score=0.0043210424030263464, is_threat=False, action=ALLOW
2026-10-03 19:22:56,328 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('4.213.25.242', '10.10.10.2', 443, 50265, 6) (pkts=2)
2026-10-03 19:22:56,330 [INFO] sagedral_ml.detection.decision: Decision for 4.213.25.242: sig_score=0.0, ml_score=0.005665511121566175, final_score=0.003399306672939705, is_threat=False, action=ALLOW
2026-10-03 19:22:56,348 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '64.233.170.188', 50263, 5228, 6) (pkts=1)
2026-10-03 19:22:56,350 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.008251085736842865, final_score=0.004950651442105719, is_threat=False, action=ALLOW
2026-10-03 19:22:56,351 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.194.188', 50264, 5228, 6) (pkts=1)
2026-10-03 19:22:56,353 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.008251085736842865, final_score=0.004950651442105719, is_threat=False, action=ALLOW
2026-10-03 19:22:56,353 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '74.125.130.188', 50262, 5228, 6) (pkts=1)
2026-10-03 19:22:56,355 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.008251085736842865, final_score=0.004950651442105719, is_threat=False, action=ALLOW
2026-10-03 19:22:56,417 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('74.125.130.188', '10.10.10.2', 5228, 50262, 6) (pkts=1)
2026-10-03 19:22:56,419 [INFO] sagedral_ml.detection.decision: Decision for 74.125.130.188: sig_score=0.0, ml_score=0.006122575298292739, final_score=0.0036735451789756436, is_threat=False, action=ALLOW
2026-10-03 19:22:56,419 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('64.233.170.188', '10.10.10.2', 5228, 50263, 6) (pkts=1)
2026-10-03 19:22:56,421 [INFO] sagedral_ml.detection.decision: Decision for 64.233.170.188: sig_score=0.0, ml_score=0.006122575298292739, final_score=0.0036735451789756436, is_threat=False, action=ALLOW
2026-10-03 19:22:56,427 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.194.188', '10.10.10.2', 5228, 50264, 6) (pkts=1)
2026-10-03 19:22:56,435 [INFO] sagedral_ml.detection.decision: Decision for 172.217.194.188: sig_score=0.0, ml_score=0.006122575298292739, final_score=0.0036735451789756436, is_threat=False, action=ALLOW
2026-10-03 19:22:58,003 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '140.82.112.25', 50253, 443, 6) (pkts=21)
2026-10-03 19:22:58,006 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.00783890734829821, final_score=0.004703344408978926, is_threat=False, action=ALLOW
2026-10-03 19:22:58,007 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '140.82.112.25', 50253, 443, 6) (pkts=1)
2026-10-03 19:22:58,008 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.007315437736022871, final_score=0.004389262641613723, is_threat=False, action=ALLOW
2026-10-03 19:22:58,683 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '52.230.60.54', 50318, 443, 6) (pkts=39)
2026-10-03 19:22:58,689 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.00955247523849631, final_score=0.005731485143097786, is_threat=False, action=ALLOW
2026-10-03 19:22:58,760 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('52.230.60.54', '10.10.10.2', 443, 50318, 6) (pkts=1)
2026-10-03 19:22:58,766 [INFO] sagedral_ml.detection.decision: Decision for 52.230.60.54: sig_score=0.0, ml_score=0.006122575298292739, final_score=0.0036735451789756436, is_threat=False, action=ALLOW
2026-10-03 19:22:59,139 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '72.145.35.108', 50317, 443, 6) (pkts=12)
2026-10-03 19:22:59,145 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.006911816440455512, final_score=0.004147089864273307, is_threat=False, action=ALLOW
2026-10-03 19:22:59,268 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '140.82.112.26', 50310, 443, 6) (pkts=20)
2026-10-03 19:22:59,273 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.00857320215810379, final_score=0.0051439212948622744, is_threat=False, action=ALLOW
2026-10-03 19:22:59,381 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '52.230.60.54', 50319, 443, 6) (pkts=48)
2026-10-03 19:22:59,386 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.00955247523849631, final_score=0.005731485143097786, is_threat=False, action=ALLOW
2026-10-03 19:22:59,417 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('72.145.35.108', '10.10.10.2', 443, 50317, 6) (pkts=1)
2026-10-03 19:22:59,423 [INFO] sagedral_ml.detection.decision: Decision for 72.145.35.108: sig_score=0.0, ml_score=0.006122575298292739, final_score=0.0036735451789756436, is_threat=False, action=ALLOW
2026-10-03 19:22:59,470 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('52.230.60.54', '10.10.10.2', 443, 50319, 6) (pkts=1)
2026-10-03 19:22:59,475 [INFO] sagedral_ml.detection.decision: Decision for 52.230.60.54: sig_score=0.0, ml_score=0.006122575298292739, final_score=0.0036735451789756436, is_threat=False, action=ALLOW
2026-10-03 19:22:59,586 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('140.82.112.26', '10.10.10.2', 443, 50310, 6) (pkts=2)
2026-10-03 19:22:59,594 [INFO] sagedral_ml.detection.decision: Decision for 140.82.112.26: sig_score=0.0, ml_score=0.0093516283670393, final_score=0.00561097702022358, is_threat=False, action=ALLOW
2026-10-03 19:22:59,595 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '140.82.112.26', 50310, 443, 6) (pkts=1)
2026-10-03 19:22:59,598 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.007315437736022871, final_score=0.004389262641613723, is_threat=False, action=ALLOW
2026-10-03 19:22:59,598 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '140.82.112.26', 50310, 443, 6) (pkts=1)
2026-10-03 19:22:59,600 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.007315437736022871, final_score=0.004389262641613723, is_threat=False, action=ALLOW
2026-10-03 19:23:00,546 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '74.125.200.188', 50315, 5228, 6) (pkts=28)
2026-10-03 19:23:00,552 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.02087713811737735, final_score=0.01252628287042641, is_threat=False, action=ALLOW
2026-10-03 19:23:00,553 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '142.251.175.188', 50316, 5228, 6) (pkts=26)
2026-10-03 19:23:00,558 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.02087713811737735, final_score=0.01252628287042641, is_threat=False, action=ALLOW
2026-10-03 19:23:00,558 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '142.251.12.188', 50314, 5228, 6) (pkts=28)
2026-10-03 19:23:00,573 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.02087713811737735, final_score=0.01252628287042641, is_threat=False, action=ALLOW
2026-10-03 19:23:00,871 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '74.125.200.188', 50315, 5228, 6) (pkts=1)
2026-10-03 19:23:00,873 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.008251085736842865, final_score=0.004950651442105719, is_threat=False, action=ALLOW
2026-10-03 19:23:00,873 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '142.251.12.188', 50314, 5228, 6) (pkts=1)
2026-10-03 19:23:00,875 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.008251085736842865, final_score=0.004950651442105719, is_threat=False, action=ALLOW
2026-10-03 19:23:00,875 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '142.251.175.188', 50316, 5228, 6) (pkts=1)
2026-10-03 19:23:00,880 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.008251085736842865, final_score=0.004950651442105719, is_threat=False, action=ALLOW
2026-10-03 19:23:00,947 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('74.125.200.188', '10.10.10.2', 5228, 50315, 6) (pkts=1)
2026-10-03 19:23:00,956 [INFO] sagedral_ml.detection.decision: Decision for 74.125.200.188: sig_score=0.0, ml_score=0.006122575298292739, final_score=0.0036735451789756436, is_threat=False, action=ALLOW
2026-10-03 19:23:00,957 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('142.251.12.188', '10.10.10.2', 5228, 50314, 6) (pkts=1)
2026-10-03 19:23:00,960 [INFO] sagedral_ml.detection.decision: Decision for 142.251.12.188: sig_score=0.0, ml_score=0.006122575298292739, final_score=0.0036735451789756436, is_threat=False, action=ALLOW
2026-10-03 19:23:00,960 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('142.251.175.188', '10.10.10.2', 5228, 50316, 6) (pkts=1)
2026-10-03 19:23:00,964 [INFO] sagedral_ml.detection.decision: Decision for 142.251.175.188: sig_score=0.0, ml_score=0.006122575298292739, final_score=0.0036735451789756436, is_threat=False, action=ALLOW
2026-10-03 19:23:01,941 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '8.8.8.8', 50328, 443, 6) (pkts=7)
2026-10-03 19:23:01,946 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.006948670288941394, final_score=0.004169202173364836, is_threat=False, action=ALLOW
2026-10-03 19:23:02,069 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('8.8.8.8', '10.10.10.2', 443, 50328, 6) (pkts=2)
2026-10-03 19:23:02,073 [INFO] sagedral_ml.detection.decision: Decision for 8.8.8.8: sig_score=0.0, ml_score=0.019081441925470993, final_score=0.011448865155282595, is_threat=False, action=ALLOW
2026-10-03 19:23:02,198 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('8.8.8.8', '10.10.10.2', 443, 50328, 6) (pkts=1)
2026-10-03 19:23:02,203 [INFO] sagedral_ml.detection.decision: Decision for 8.8.8.8: sig_score=0.0, ml_score=0.028212465511618892, final_score=0.016927479306971336, is_threat=False, action=ALLOW
2026-10-03 19:23:02,371 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '8.8.8.8', 50328, 443, 6) (pkts=2)
2026-10-03 19:23:02,378 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.005412055482057169, final_score=0.0032472332892343014, is_threat=False, action=ALLOW
2026-10-03 19:23:03,113 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '8.8.8.8', 50322, 443, 6) (pkts=16)
2026-10-03 19:23:03,117 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.005857772275696004, final_score=0.0035146633654176023, is_threat=False, action=ALLOW
2026-10-03 19:23:03,199 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('8.8.8.8', '10.10.10.2', 443, 50322, 6) (pkts=3)
2026-10-03 19:23:03,204 [INFO] sagedral_ml.detection.decision: Decision for 8.8.8.8: sig_score=0.0, ml_score=0.0065127921415337985, final_score=0.0039076752849202786, is_threat=False, action=ALLOW
2026-10-03 19:23:03,227 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('8.8.8.8', '10.10.10.2', 443, 50322, 6) (pkts=1)
2026-10-03 19:23:03,233 [INFO] sagedral_ml.detection.decision: Decision for 8.8.8.8: sig_score=0.0, ml_score=0.028212465511618892, final_score=0.016927479306971336, is_threat=False, action=ALLOW
2026-10-03 19:23:03,234 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '8.8.8.8', 50322, 443, 6) (pkts=1)
2026-10-03 19:23:03,239 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.007315437736022871, final_score=0.004389262641613723, is_threat=False, action=ALLOW
2026-10-03 19:23:04,384 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '8.8.8.8', 50328, 443, 6) (pkts=3)
2026-10-03 19:23:04,392 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.010042047191588483, final_score=0.006025228314953089, is_threat=False, action=ALLOW
2026-10-03 19:23:07,017 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.118.4', '10.10.10.2', 443, 50296, 6) (pkts=1000)
2026-10-03 19:23:07,020 [INFO] sagedral_ml.detection.decision: Decision for 172.217.118.4: sig_score=0.0, ml_score=0.01827985786871909, final_score=0.010967914721231454, is_threat=False, action=ALLOW
2026-10-03 19:23:09,369 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '4.237.22.38', 50327, 443, 6) (pkts=16)
2026-10-03 19:23:09,374 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.00955247523849631, final_score=0.005731485143097786, is_threat=False, action=ALLOW
2026-10-03 19:23:15,398 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.010888203058543083, final_score=0.006532921835125849, is_threat=False, action=ALLOW
2026-10-03 19:23:15,398 [INFO] sagedral_ml.detection.decision: Decision for fe80::e768:ba7:72ab:4d10: sig_score=0.0, ml_score=0.9585319979911209, final_score=0.5751191987946725, is_threat=True, action=ALERT
2026-10-03 19:23:15,401 [INFO] sagedral_ml.detection.decision: Decision for 192.168.88.20: sig_score=0.0, ml_score=0.9289579408600622, final_score=0.5573747645160373, is_threat=True, action=ALERT
2026-10-03 19:23:15,403 [INFO] sagedral_ml.detection.decision: Decision for 192.168.88.20: sig_score=0.0, ml_score=0.02088911987500819, final_score=0.012533471925004912, is_threat=False, action=ALLOW
2026-10-03 19:23:15,403 [INFO] sagedral_ml.detection.decision: Decision for fe80::e768:ba7:72ab:4d10: sig_score=0.0, ml_score=0.02155674709742763, final_score=0.012934048258456577, is_threat=False, action=ALLOW
2026-10-03 19:23:15,404 [INFO] sagedral_ml.detection.decision: Decision for fe80::e768:ba7:72ab:4d10: sig_score=0.0, ml_score=0.008626266912121355, final_score=0.005175760147272813, is_threat=False, action=ALLOW
2026-10-03 19:23:15,404 [INFO] sagedral_ml.detection.decision: Decision for 192.168.88.20: sig_score=0.0, ml_score=0.008251085736842865, final_score=0.004950651442105719, is_threat=False, action=ALLOW
2026-10-03 19:23:15,404 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:23:15,404 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:23:15,404 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:23:15,404 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:23:15,404 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:23:15,806 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.115.4', 50304, 443, 6) (pkts=1000)
2026-10-03 19:23:15,812 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.07579740884602564, final_score=0.04547844530761538, is_threat=False, action=ALLOW
2026-10-03 19:23:19,196 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.115.4', 50307, 443, 6) (pkts=1000)
2026-10-03 19:23:19,201 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.07579740884602564, final_score=0.04547844530761538, is_threat=False, action=ALLOW
2026-10-03 19:23:23,715 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.118.4', 50296, 443, 6) (pkts=1000)
2026-10-03 19:23:23,724 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.04500792772019535, final_score=0.02700475663211721, is_threat=False, action=ALLOW
2026-10-03 19:23:32,395 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '4.237.22.38', 50326, 443, 6) (pkts=30)
2026-10-03 19:23:32,400 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.00955247523849631, final_score=0.005731485143097786, is_threat=False, action=ALLOW
2026-10-03 19:23:32,637 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('4.237.22.38', '10.10.10.2', 443, 50326, 6) (pkts=2)
2026-10-03 19:23:32,643 [INFO] sagedral_ml.detection.decision: Decision for 4.237.22.38: sig_score=0.0, ml_score=0.0093516283670393, final_score=0.00561097702022358, is_threat=False, action=ALLOW
2026-10-03 19:23:32,644 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '4.237.22.38', 50326, 443, 6) (pkts=1)
2026-10-03 19:23:32,649 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.007315437736022871, final_score=0.004389262641613723, is_threat=False, action=ALLOW
2026-10-03 19:23:32,650 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '4.237.22.38', 50326, 443, 6) (pkts=1)
2026-10-03 19:23:32,654 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.007315437736022871, final_score=0.004389262641613723, is_threat=False, action=ALLOW
2026-10-03 19:23:40,377 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.118.4', 50296, 443, 6) (pkts=1000)
2026-10-03 19:23:40,388 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.04500792772019535, final_score=0.02700475663211721, is_threat=False, action=ALLOW
2026-10-03 19:23:43,833 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.115.4', 50304, 443, 6) (pkts=1000)
2026-10-03 19:23:43,840 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.05377938018866268, final_score=0.032267628113197604, is_threat=False, action=ALLOW
2026-10-03 19:23:45,934 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:23:45,934 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:23:45,934 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.007315437736022871, final_score=0.004389262641613723, is_threat=False, action=ALLOW
2026-10-03 19:23:45,934 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.007315437736022871, final_score=0.004389262641613723, is_threat=False, action=ALLOW
2026-10-03 19:23:45,934 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.007315437736022871, final_score=0.004389262641613723, is_threat=False, action=ALLOW
2026-10-03 19:23:45,935 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.007315437736022871, final_score=0.004389262641613723, is_threat=False, action=ALLOW
2026-10-03 19:23:45,935 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.007315437736022871, final_score=0.004389262641613723, is_threat=False, action=ALLOW
2026-10-03 19:23:45,935 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:23:45,935 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:23:45,935 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:23:45,935 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:23:45,935 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:23:45,935 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:23:45,935 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.007315437736022871, final_score=0.004389262641613723, is_threat=False, action=ALLOW
2026-10-03 19:23:54,616 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '4.237.22.38', 50327, 443, 6) (pkts=3)
2026-10-03 19:23:54,620 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.005412055482057169, final_score=0.0032472332892343014, is_threat=False, action=ALLOW
2026-10-03 19:23:57,158 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.70.132', 50309, 443, 6) (pkts=46)
2026-10-03 19:23:57,164 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.00955247523849631, final_score=0.005731485143097786, is_threat=False, action=ALLOW
2026-10-03 19:23:57,212 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.118.4', 50296, 443, 6) (pkts=1000)
2026-10-03 19:23:57,216 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.04500792772019535, final_score=0.02700475663211721, is_threat=False, action=ALLOW
2026-10-03 19:23:57,272 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.70.132', '10.10.10.2', 443, 50309, 6) (pkts=3)
2026-10-03 19:23:57,282 [INFO] sagedral_ml.detection.decision: Decision for 172.217.70.132: sig_score=0.0, ml_score=0.005713624548923921, final_score=0.0034281747293543525, is_threat=False, action=ALLOW
2026-10-03 19:23:58,774 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.115.4', '10.10.10.2', 443, 50307, 6) (pkts=1000)
2026-10-03 19:23:58,778 [INFO] sagedral_ml.detection.decision: Decision for 172.217.115.4: sig_score=0.0, ml_score=0.0878612567114892, final_score=0.05271675402689352, is_threat=False, action=ALLOW
2026-10-03 19:24:03,771 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.118.4', 50296, 443, 6) (pkts=1000)
2026-10-03 19:24:03,773 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.04500792772019535, final_score=0.02700475663211721, is_threat=False, action=ALLOW
2026-10-03 19:24:07,320 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.115.4', '10.10.10.2', 443, 50307, 6) (pkts=1000)
2026-10-03 19:24:07,327 [INFO] sagedral_ml.detection.decision: Decision for 172.217.115.4: sig_score=0.0, ml_score=0.0878612567114892, final_score=0.05271675402689352, is_threat=False, action=ALLOW
2026-10-03 19:24:10,401 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.118.4', 50296, 443, 6) (pkts=1000)
2026-10-03 19:24:10,404 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.04500792772019535, final_score=0.02700475663211721, is_threat=False, action=ALLOW
2026-10-03 19:24:15,575 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:24:15,575 [INFO] sagedral_ml.detection.decision: Decision for 0.0.0.0: sig_score=0.0, ml_score=0.9336129879284328, final_score=0.5601677927570596, is_threat=True, action=ALERT
2026-10-03 19:24:15,577 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.005774457704507509, final_score=0.003464674622704505, is_threat=False, action=ALLOW
2026-10-03 19:24:15,577 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.006436119836727569, final_score=0.003861671902036541, is_threat=False, action=ALLOW
2026-10-03 19:24:15,578 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.006436119836727569, final_score=0.003861671902036541, is_threat=False, action=ALLOW
2026-10-03 19:24:15,578 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.005774457704507509, final_score=0.003464674622704505, is_threat=False, action=ALLOW
2026-10-03 19:24:15,578 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.006436119836727569, final_score=0.003861671902036541, is_threat=False, action=ALLOW
2026-10-03 19:24:15,578 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.005774457704507509, final_score=0.003464674622704505, is_threat=False, action=ALLOW
2026-10-03 19:24:15,578 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.006436119836727569, final_score=0.003861671902036541, is_threat=False, action=ALLOW
2026-10-03 19:24:15,578 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.005774457704507509, final_score=0.003464674622704505, is_threat=False, action=ALLOW
2026-10-03 19:24:15,578 [INFO] sagedral_ml.detection.decision: Decision for fe80::bc2b:9333:90a:dab8: sig_score=0.0, ml_score=0.9776068885284274, final_score=0.5865641331170564, is_threat=True, action=ALERT
2026-10-03 19:24:15,578 [INFO] sagedral_ml.detection.decision: Decision for 192.168.88.245: sig_score=0.0, ml_score=0.9621099799926967, final_score=0.577265987995618, is_threat=True, action=ALERT
2026-10-03 19:24:15,578 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.006436119836727569, final_score=0.003861671902036541, is_threat=False, action=ALLOW
2026-10-03 19:24:15,579 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.005857772275696004, final_score=0.0035146633654176023, is_threat=False, action=ALLOW
2026-10-03 19:24:15,579 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.006436119836727569, final_score=0.003861671902036541, is_threat=False, action=ALLOW
2026-10-03 19:24:15,579 [INFO] sagedral_ml.detection.decision: Decision for fe80::bc2b:9333:90a:dab8: sig_score=0.0, ml_score=0.022153477471153163, final_score=0.013292086482691897, is_threat=False, action=ALLOW
2026-10-03 19:24:15,579 [INFO] sagedral_ml.detection.decision: Decision for 192.168.88.245: sig_score=0.0, ml_score=0.00670047843155625, final_score=0.00402028705893375, is_threat=False, action=ALLOW
2026-10-03 19:24:15,579 [INFO] sagedral_ml.detection.decision: Decision for ::: sig_score=0.0, ml_score=0.8916651395466639, final_score=0.5349990837279983, is_threat=True, action=ALERT
2026-10-03 19:24:15,582 [INFO] sagedral_ml.detection.decision: Decision for fe80::bc2b:9333:90a:dab8: sig_score=0.0, ml_score=0.9423260523042929, final_score=0.5653956313825758, is_threat=True, action=ALERT
2026-10-03 19:24:15,582 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:24:15,583 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:24:15,585 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:24:15,585 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.007315437736022871, final_score=0.004389262641613723, is_threat=False, action=ALLOW
2026-10-03 19:24:15,585 [INFO] sagedral_ml.detection.decision: Decision for fe80::bc2b:9333:90a:dab8: sig_score=0.0, ml_score=0.8916651395466639, final_score=0.5349990837279983, is_threat=True, action=ALERT
2026-10-03 19:24:15,586 [INFO] sagedral_ml.detection.decision: Decision for fe80::bc2b:9333:90a:dab8: sig_score=0.0, ml_score=0.02692353008474288, final_score=0.01615411805084573, is_threat=False, action=ALLOW
2026-10-03 19:24:15,586 [INFO] sagedral_ml.detection.decision: Decision for fe80::bc2b:9333:90a:dab8: sig_score=0.0, ml_score=0.008626266912121355, final_score=0.005175760147272813, is_threat=False, action=ALLOW
2026-10-03 19:24:15,586 [INFO] sagedral_ml.detection.decision: Decision for 192.168.88.245: sig_score=0.0, ml_score=0.008251085736842865, final_score=0.004950651442105719, is_threat=False, action=ALLOW
2026-10-03 19:24:15,586 [INFO] sagedral_ml.detection.decision: Decision for 192.168.88.245: sig_score=0.0, ml_score=0.05046847008617974, final_score=0.03028108205170784, is_threat=False, action=ALLOW
2026-10-03 19:24:15,586 [INFO] sagedral_ml.detection.decision: Decision for fe80::bc2b:9333:90a:dab8: sig_score=0.0, ml_score=0.0507904975520282, final_score=0.030474298531216918, is_threat=False, action=ALLOW
2026-10-03 19:24:15,586 [INFO] sagedral_ml.detection.decision: Decision for 192.168.88.245: sig_score=0.0, ml_score=0.05046847008617974, final_score=0.03028108205170784, is_threat=False, action=ALLOW
2026-10-03 19:24:15,586 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:24:15,586 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.005634533297682234, final_score=0.00338071997860934, is_threat=False, action=ALLOW
2026-10-03 19:24:15,822 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.08064287812855137, final_score=0.048385726877130816, is_threat=False, action=ALLOW
2026-10-03 19:24:15,822 [INFO] sagedral_ml.detection.decision: Decision for fe80::bc2b:9333:90a:dab8: sig_score=0.0, ml_score=0.0507904975520282, final_score=0.030474298531216918, is_threat=False, action=ALLOW
2026-10-03 19:24:15,822 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.010888203058543083, final_score=0.006532921835125849, is_threat=False, action=ALLOW
2026-10-03 19:24:15,822 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:24:15,822 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.005412055482057169, final_score=0.0032472332892343014, is_threat=False, action=ALLOW
2026-10-03 19:24:15,822 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.007315437736022871, final_score=0.004389262641613723, is_threat=False, action=ALLOW
2026-10-03 19:24:15,822 [INFO] sagedral_ml.detection.decision: Decision for fe80::bc2b:9333:90a:dab8: sig_score=0.0, ml_score=0.03866797793988492, final_score=0.02320078676393095, is_threat=False, action=ALLOW
2026-10-03 19:24:15,822 [INFO] sagedral_ml.detection.decision: Decision for 192.168.88.245: sig_score=0.0, ml_score=0.03799429298238382, final_score=0.02279657578943029, is_threat=False, action=ALLOW
2026-10-03 19:24:15,822 [INFO] sagedral_ml.detection.decision: Decision for fe80::bc2b:9333:90a:dab8: sig_score=0.0, ml_score=0.008626266912121355, final_score=0.005175760147272813, is_threat=False, action=ALLOW
2026-10-03 19:24:15,823 [INFO] sagedral_ml.detection.decision: Decision for 192.168.88.245: sig_score=0.0, ml_score=0.008251085736842865, final_score=0.004950651442105719, is_threat=False, action=ALLOW
2026-10-03 19:24:15,823 [INFO] sagedral_ml.detection.decision: Decision for 192.168.88.245: sig_score=0.0, ml_score=0.11356050246229075, final_score=0.06813630147737446, is_threat=False, action=ALLOW
2026-10-03 19:24:15,823 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.010888203058543083, final_score=0.006532921835125849, is_threat=False, action=ALLOW
2026-10-03 19:24:15,823 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.006806035187718846, final_score=0.004083621112631307, is_threat=False, action=ALLOW
2026-10-03 19:24:15,823 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.007315437736022871, final_score=0.004389262641613723, is_threat=False, action=ALLOW
2026-10-03 19:24:15,823 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.007315437736022871, final_score=0.004389262641613723, is_threat=False, action=ALLOW
2026-10-03 19:24:15,823 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:24:15,823 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.005903031552830177, final_score=0.003541818931698106, is_threat=False, action=ALLOW
2026-10-03 19:24:15,823 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.08064287812855137, final_score=0.048385726877130816, is_threat=False, action=ALLOW
2026-10-03 19:24:15,823 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:24:15,823 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.08064287812855137, final_score=0.048385726877130816, is_threat=False, action=ALLOW
2026-10-03 19:24:15,823 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:24:15,823 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:24:15,823 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:24:15,823 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:24:15,823 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.01016695710115561, final_score=0.006100174260693366, is_threat=False, action=ALLOW
2026-10-03 19:24:15,823 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.006436119836727569, final_score=0.003861671902036541, is_threat=False, action=ALLOW
2026-10-03 19:24:15,823 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:24:15,824 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:24:15,824 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.08064287812855137, final_score=0.048385726877130816, is_threat=False, action=ALLOW
2026-10-03 19:24:15,824 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:24:22,227 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.118.4', 50296, 443, 6) (pkts=1000)
2026-10-03 19:24:22,229 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.04500792772019535, final_score=0.02700475663211721, is_threat=False, action=ALLOW
2026-10-03 19:24:23,730 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.115.4', 50337, 443, 6) (pkts=29)
2026-10-03 19:24:23,735 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.00857320215810379, final_score=0.0051439212948622744, is_threat=False, action=ALLOW
2026-10-03 19:24:23,814 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.115.4', '10.10.10.2', 443, 50337, 6) (pkts=1)
2026-10-03 19:24:23,821 [INFO] sagedral_ml.detection.decision: Decision for 172.217.115.4: sig_score=0.0, ml_score=0.006122575298292739, final_score=0.0036735451789756436, is_threat=False, action=ALLOW
2026-10-03 19:24:28,526 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.115.4', 50304, 443, 6) (pkts=1000)
2026-10-03 19:24:28,531 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.048455726387398486, final_score=0.02907343583243909, is_threat=False, action=ALLOW
2026-10-03 19:24:30,068 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '118.215.85.134', 50320, 443, 6) (pkts=1)
2026-10-03 19:24:30,074 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.007315437736022871, final_score=0.004389262641613723, is_threat=False, action=ALLOW
2026-10-03 19:24:30,149 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('118.215.85.134', '10.10.10.2', 443, 50320, 6) (pkts=2)
2026-10-03 19:24:30,155 [INFO] sagedral_ml.detection.decision: Decision for 118.215.85.134: sig_score=0.0, ml_score=0.0093516283670393, final_score=0.00561097702022358, is_threat=False, action=ALLOW
2026-10-03 19:24:30,156 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '118.215.85.134', 50320, 443, 6) (pkts=1)
2026-10-03 19:24:30,161 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.007315437736022871, final_score=0.004389262641613723, is_threat=False, action=ALLOW
2026-10-03 19:24:30,162 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '118.215.85.134', 50320, 443, 6) (pkts=1)
2026-10-03 19:24:30,166 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.007315437736022871, final_score=0.004389262641613723, is_threat=False, action=ALLOW
2026-10-03 19:24:33,886 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.118.4', 50296, 443, 6) (pkts=1000)
2026-10-03 19:24:33,893 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.04500792772019535, final_score=0.02700475663211721, is_threat=False, action=ALLOW
2026-10-03 19:24:36,110 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.115.4', '10.10.10.2', 443, 50307, 6) (pkts=1000)
2026-10-03 19:24:36,121 [INFO] sagedral_ml.detection.decision: Decision for 172.217.115.4: sig_score=0.0, ml_score=0.030067672898803344, final_score=0.018040603739282006, is_threat=False, action=ALLOW
2026-10-03 19:24:40,537 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.118.4', 50296, 443, 6) (pkts=1000)
2026-10-03 19:24:40,545 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.04500792772019535, final_score=0.02700475663211721, is_threat=False, action=ALLOW
2026-10-03 19:24:46,105 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.005774457704507509, final_score=0.003464674622704505, is_threat=False, action=ALLOW
2026-10-03 19:24:46,105 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.005774457704507509, final_score=0.003464674622704505, is_threat=False, action=ALLOW
2026-10-03 19:24:46,106 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:24:46,106 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:24:46,106 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:24:46,106 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:24:46,106 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:24:46,106 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:24:49,962 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.115.4', '10.10.10.2', 443, 50307, 6) (pkts=1000)
2026-10-03 19:24:49,967 [INFO] sagedral_ml.detection.decision: Decision for 172.217.115.4: sig_score=0.0, ml_score=0.030067672898803344, final_score=0.018040603739282006, is_threat=False, action=ALLOW
2026-10-03 19:24:52,475 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.118.4', 50296, 443, 6) (pkts=1000)
2026-10-03 19:24:52,480 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.04500792772019535, final_score=0.02700475663211721, is_threat=False, action=ALLOW
2026-10-03 19:24:58,349 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.115.4', 50345, 443, 6) (pkts=20)
2026-10-03 19:24:58,354 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.00857320215810379, final_score=0.0051439212948622744, is_threat=False, action=ALLOW
2026-10-03 19:24:58,426 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.115.4', '10.10.10.2', 443, 50345, 6) (pkts=1)
2026-10-03 19:24:58,433 [INFO] sagedral_ml.detection.decision: Decision for 172.217.115.4: sig_score=0.0, ml_score=0.006122575298292739, final_score=0.0036735451789756436, is_threat=False, action=ALLOW
2026-10-03 19:24:58,929 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.118.4', 50296, 443, 6) (pkts=1000)
2026-10-03 19:24:58,936 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.04500792772019535, final_score=0.02700475663211721, is_threat=False, action=ALLOW
2026-10-03 19:25:01,462 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '52.168.117.171', 50331, 443, 6) (pkts=1)
2026-10-03 19:25:01,467 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.007315437736022871, final_score=0.004389262641613723, is_threat=False, action=ALLOW
2026-10-03 19:25:01,702 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '4.237.22.38', 50348, 443, 6) (pkts=33)
2026-10-03 19:25:01,708 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.00857320215810379, final_score=0.0051439212948622744, is_threat=False, action=ALLOW
2026-10-03 19:25:01,787 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('52.168.117.171', '10.10.10.2', 443, 50331, 6) (pkts=1)
2026-10-03 19:25:01,793 [INFO] sagedral_ml.detection.decision: Decision for 52.168.117.171: sig_score=0.0, ml_score=0.006122575298292739, final_score=0.0036735451789756436, is_threat=False, action=ALLOW
2026-10-03 19:25:01,950 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('4.237.22.38', '10.10.10.2', 443, 50348, 6) (pkts=5)
2026-10-03 19:25:01,958 [INFO] sagedral_ml.detection.decision: Decision for 4.237.22.38: sig_score=0.0, ml_score=0.009800606269676613, final_score=0.005880363761805968, is_threat=False, action=ALLOW
2026-10-03 19:25:01,959 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '4.237.22.38', 50348, 443, 6) (pkts=1)
2026-10-03 19:25:01,964 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.007315437736022871, final_score=0.004389262641613723, is_threat=False, action=ALLOW
2026-10-03 19:25:01,964 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '4.237.22.38', 50348, 443, 6) (pkts=1)
2026-10-03 19:25:01,971 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.007315437736022871, final_score=0.004389262641613723, is_threat=False, action=ALLOW
2026-10-03 19:25:08,715 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.115.4', '10.10.10.2', 443, 50307, 6) (pkts=1000)
2026-10-03 19:25:08,717 [INFO] sagedral_ml.detection.decision: Decision for 172.217.115.4: sig_score=0.0, ml_score=0.09581036052543766, final_score=0.057486216315262594, is_threat=False, action=ALLOW
2026-10-03 19:25:09,991 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.115.4', 50307, 443, 6) (pkts=1000)
2026-10-03 19:25:10,001 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.04500792772019535, final_score=0.02700475663211721, is_threat=False, action=ALLOW
2026-10-03 19:25:10,797 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.118.4', '10.10.10.2', 443, 50296, 6) (pkts=1000)
2026-10-03 19:25:10,804 [INFO] sagedral_ml.detection.decision: Decision for 172.217.118.4: sig_score=0.0, ml_score=0.01827985786871909, final_score=0.010967914721231454, is_threat=False, action=ALLOW
2026-10-03 19:25:11,623 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.115.4', 50307, 443, 6) (pkts=1000)
2026-10-03 19:25:11,626 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.04500792772019535, final_score=0.02700475663211721, is_threat=False, action=ALLOW
2026-10-03 19:25:11,955 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '4.237.22.38', 50353, 443, 6) (pkts=16)
2026-10-03 19:25:11,962 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.00857320215810379, final_score=0.0051439212948622744, is_threat=False, action=ALLOW
2026-10-03 19:25:13,317 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '92.223.78.30', 50336, 80, 6) (pkts=8)
2026-10-03 19:25:13,322 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.28188771436350735, final_score=0.1691326286181044, is_threat=False, action=ALLOW
2026-10-03 19:25:13,571 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('92.223.78.30', '10.10.10.2', 80, 50336, 6) (pkts=1)
2026-10-03 19:25:13,576 [INFO] sagedral_ml.detection.decision: Decision for 92.223.78.30: sig_score=0.0, ml_score=0.006122575298292739, final_score=0.0036735451789756436, is_threat=False, action=ALLOW
2026-10-03 19:25:16,217 [INFO] sagedral_ml.detection.decision: Decision for fe80::bc2b:9333:90a:dab8: sig_score=0.0, ml_score=0.038136923481217166, final_score=0.0228821540887303, is_threat=False, action=ALLOW
2026-10-03 19:25:16,218 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:25:16,218 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.006436119836727569, final_score=0.003861671902036541, is_threat=False, action=ALLOW
2026-10-03 19:25:16,218 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.005774457704507509, final_score=0.003464674622704505, is_threat=False, action=ALLOW
2026-10-03 19:25:16,218 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.007315437736022871, final_score=0.004389262641613723, is_threat=False, action=ALLOW
2026-10-03 19:25:16,218 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.010888203058543083, final_score=0.006532921835125849, is_threat=False, action=ALLOW
2026-10-03 19:25:16,218 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.010888203058543083, final_score=0.006532921835125849, is_threat=False, action=ALLOW
2026-10-03 19:25:16,218 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:25:16,218 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:25:16,218 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:25:16,218 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:25:16,218 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.005774457704507509, final_score=0.003464674622704505, is_threat=False, action=ALLOW
2026-10-03 19:25:16,218 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:25:16,218 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:25:16,218 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:25:16,218 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.005774457704507509, final_score=0.003464674622704505, is_threat=False, action=ALLOW
2026-10-03 19:25:16,218 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.006436119836727569, final_score=0.003861671902036541, is_threat=False, action=ALLOW
2026-10-03 19:25:24,348 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '52.123.128.14', 50340, 443, 6) (pkts=24)
2026-10-03 19:25:24,353 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.006436119836727569, final_score=0.003861671902036541, is_threat=False, action=ALLOW
2026-10-03 19:25:35,238 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '4.237.22.38', 50352, 443, 6) (pkts=32)
2026-10-03 19:25:35,244 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.00955247523849631, final_score=0.005731485143097786, is_threat=False, action=ALLOW
2026-10-03 19:25:35,490 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('4.237.22.38', '10.10.10.2', 443, 50352, 6) (pkts=2)
2026-10-03 19:25:35,494 [INFO] sagedral_ml.detection.decision: Decision for 4.237.22.38: sig_score=0.0, ml_score=0.019175187434439054, final_score=0.011505112460663432, is_threat=False, action=ALLOW
2026-10-03 19:25:35,498 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('4.237.22.38', '10.10.10.2', 443, 50352, 6) (pkts=1)
2026-10-03 19:25:35,503 [INFO] sagedral_ml.detection.decision: Decision for 4.237.22.38: sig_score=0.0, ml_score=0.006122575298292739, final_score=0.0036735451789756436, is_threat=False, action=ALLOW
2026-10-03 19:25:35,504 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '4.237.22.38', 50352, 443, 6) (pkts=1)
2026-10-03 19:25:35,508 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.007315437736022871, final_score=0.004389262641613723, is_threat=False, action=ALLOW
2026-10-03 19:25:44,079 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.66.158.149', '10.10.10.2', 443, 49430, 6) (pkts=201)
2026-10-03 19:25:44,085 [INFO] sagedral_ml.detection.decision: Decision for 172.66.158.149: sig_score=0.0, ml_score=0.00821948326605176, final_score=0.0049316899596310556, is_threat=False, action=ALLOW
2026-10-03 19:25:44,175 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.66.158.149', '10.10.10.2', 443, 49430, 6) (pkts=2)
2026-10-03 19:25:44,182 [INFO] sagedral_ml.detection.decision: Decision for 172.66.158.149: sig_score=0.0, ml_score=0.006556957923124409, final_score=0.003934174753874645, is_threat=False, action=ALLOW
2026-10-03 19:25:46,336 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:25:46,336 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.01016695710115561, final_score=0.006100174260693366, is_threat=False, action=ALLOW
2026-10-03 19:25:46,337 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.007315437736022871, final_score=0.004389262641613723, is_threat=False, action=ALLOW
2026-10-03 19:25:46,337 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:25:46,337 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:25:46,337 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:25:46,337 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:25:46,337 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:25:46,337 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:25:51,998 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.118.4', 50266, 443, 6) (pkts=110)
2026-10-03 19:25:52,004 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.010099682113273724, final_score=0.006059809267964234, is_threat=False, action=ALLOW
2026-10-03 19:25:52,004 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.118.4', 50266, 443, 6) (pkts=3)
2026-10-03 19:25:52,006 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.03229144455996398, final_score=0.019374866735978387, is_threat=False, action=ALLOW
2026-10-03 19:25:52,084 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.118.4', '10.10.10.2', 443, 50266, 6) (pkts=1)
2026-10-03 19:25:52,090 [INFO] sagedral_ml.detection.decision: Decision for 172.217.118.4: sig_score=0.0, ml_score=0.006122575298292739, final_score=0.0036735451789756436, is_threat=False, action=ALLOW
2026-10-03 19:25:52,091 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.118.4', '10.10.10.2', 443, 50266, 6) (pkts=1)
2026-10-03 19:25:52,096 [INFO] sagedral_ml.detection.decision: Decision for 172.217.118.4: sig_score=0.0, ml_score=0.006122575298292739, final_score=0.0036735451789756436, is_threat=False, action=ALLOW
2026-10-03 19:25:57,228 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '4.237.22.38', 50353, 443, 6) (pkts=3)
2026-10-03 19:25:57,234 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.005412055482057169, final_score=0.0032472332892343014, is_threat=False, action=ALLOW
2026-10-03 19:26:01,309 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '91.189.91.57', 47368, 80, 6) (pkts=13)
2026-10-03 19:26:01,314 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.09939954854448099, final_score=0.05963972912668859, is_threat=False, action=ALLOW
2026-10-03 19:26:01,420 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '91.189.91.57', 47368, 80, 6) (pkts=2)
2026-10-03 19:26:01,426 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.10729536647158561, final_score=0.06437721988295136, is_threat=False, action=ALLOW
2026-10-03 19:26:16,490 [INFO] sagedral_ml.detection.decision: Decision for 192.168.88.245: sig_score=0.0, ml_score=0.06552721783217035, final_score=0.0393163306993022, is_threat=False, action=ALLOW
2026-10-03 19:26:16,490 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.01016695710115561, final_score=0.006100174260693366, is_threat=False, action=ALLOW
2026-10-03 19:26:16,490 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:26:16,490 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:26:16,490 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.007315437736022871, final_score=0.004389262641613723, is_threat=False, action=ALLOW
2026-10-03 19:26:16,490 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:26:16,490 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.007315437736022871, final_score=0.004389262641613723, is_threat=False, action=ALLOW
2026-10-03 19:26:16,490 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:26:16,490 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:26:16,490 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.005774457704507509, final_score=0.003464674622704505, is_threat=False, action=ALLOW
2026-10-03 19:26:16,490 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:26:16,490 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:26:16,490 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.010888203058543083, final_score=0.006532921835125849, is_threat=False, action=ALLOW
2026-10-03 19:26:16,490 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.009773348883757738, final_score=0.005864009330254643, is_threat=False, action=ALLOW
2026-10-03 19:26:16,491 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:26:16,491 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.11204361524048004, final_score=0.06722616914428801, is_threat=False, action=ALLOW
2026-10-03 19:26:26,173 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.117.4', 50305, 443, 6) (pkts=56)
2026-10-03 19:26:26,181 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.00955247523849631, final_score=0.005731485143097786, is_threat=False, action=ALLOW
2026-10-03 19:26:26,182 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.117.4', 50305, 443, 6) (pkts=3)
2026-10-03 19:26:26,187 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.03229144455996398, final_score=0.019374866735978387, is_threat=False, action=ALLOW
2026-10-03 19:26:26,252 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.117.4', '10.10.10.2', 443, 50305, 6) (pkts=1)
2026-10-03 19:26:26,258 [INFO] sagedral_ml.detection.decision: Decision for 172.217.117.4: sig_score=0.0, ml_score=0.006122575298292739, final_score=0.0036735451789756436, is_threat=False, action=ALLOW
2026-10-03 19:26:26,259 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.117.4', '10.10.10.2', 443, 50305, 6) (pkts=1)
2026-10-03 19:26:26,263 [INFO] sagedral_ml.detection.decision: Decision for 172.217.117.4: sig_score=0.0, ml_score=0.006122575298292739, final_score=0.0036735451789756436, is_threat=False, action=ALLOW
2026-10-03 19:26:29,198 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.70.132', 50350, 443, 6) (pkts=38)
2026-10-03 19:26:29,203 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.00955247523849631, final_score=0.005731485143097786, is_threat=False, action=ALLOW
2026-10-03 19:26:29,292 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.70.132', '10.10.10.2', 443, 50350, 6) (pkts=3)
2026-10-03 19:26:29,298 [INFO] sagedral_ml.detection.decision: Decision for 172.217.70.132: sig_score=0.0, ml_score=0.005713624548923921, final_score=0.0034281747293543525, is_threat=False, action=ALLOW
2026-10-03 19:26:32,891 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.112.4', 50351, 443, 6) (pkts=35)
2026-10-03 19:26:32,897 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.00955247523849631, final_score=0.005731485143097786, is_threat=False, action=ALLOW
2026-10-03 19:26:32,990 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.112.4', '10.10.10.2', 443, 50351, 6) (pkts=3)
2026-10-03 19:26:32,995 [INFO] sagedral_ml.detection.decision: Decision for 172.217.112.4: sig_score=0.0, ml_score=0.005713624548923921, final_score=0.0034281747293543525, is_threat=False, action=ALLOW
2026-10-03 19:26:41,315 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.118.4', '10.10.10.2', 443, 50296, 6) (pkts=358)
2026-10-03 19:26:41,320 [INFO] sagedral_ml.detection.decision: Decision for 172.217.118.4: sig_score=0.0, ml_score=0.012616006829667167, final_score=0.0075696040978003, is_threat=False, action=ALLOW
2026-10-03 19:26:41,397 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.118.4', '10.10.10.2', 443, 50296, 6) (pkts=3)
2026-10-03 19:26:41,399 [INFO] sagedral_ml.detection.decision: Decision for 172.217.118.4: sig_score=0.0, ml_score=0.005713624548923921, final_score=0.0034281747293543525, is_threat=False, action=ALLOW
2026-10-03 19:26:46,637 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:26:46,637 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:26:46,637 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:26:46,638 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:26:46,638 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:26:46,638 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.005774457704507509, final_score=0.003464674622704505, is_threat=False, action=ALLOW
2026-10-03 19:27:02,033 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '8.8.8.8', 50321, 443, 6) (pkts=48)
2026-10-03 19:27:02,038 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.00857320215810379, final_score=0.0051439212948622744, is_threat=False, action=ALLOW
2026-10-03 19:27:02,107 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('8.8.8.8', '10.10.10.2', 443, 50321, 6) (pkts=1)
2026-10-03 19:27:02,113 [INFO] sagedral_ml.detection.decision: Decision for 8.8.8.8: sig_score=0.0, ml_score=0.006122575298292739, final_score=0.0036735451789756436, is_threat=False, action=ALLOW
2026-10-03 19:27:16,691 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.01016695710115561, final_score=0.006100174260693366, is_threat=False, action=ALLOW
2026-10-03 19:27:16,691 [INFO] sagedral_ml.detection.decision: Decision for 91.189.91.57: sig_score=0.0, ml_score=0.006122575298292739, final_score=0.0036735451789756436, is_threat=False, action=ALLOW
2026-10-03 19:27:16,691 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:27:16,692 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:27:16,692 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:27:16,692 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:27:16,692 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:27:16,692 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:27:16,692 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.0052138709725219915, final_score=0.003128322583513195, is_threat=False, action=ALLOW
2026-10-03 19:27:20,119 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '20.184.175.14', 50335, 443, 6) (pkts=111)
2026-10-03 19:27:20,125 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.019089544267828565, final_score=0.011453726560697139, is_threat=False, action=ALLOW
2026-10-03 19:27:26,624 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.115.4', 50307, 443, 6) (pkts=203)
2026-10-03 19:27:26,643 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.02502262216074615, final_score=0.01501357329644769, is_threat=False, action=ALLOW
2026-10-03 19:27:26,650 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('10.10.10.2', '172.217.115.4', 50304, 443, 6) (pkts=371)
2026-10-03 19:27:26,654 [INFO] sagedral_ml.detection.decision: Decision for 10.10.10.2: sig_score=0.0, ml_score=0.09760172970591209, final_score=0.058561037823547255, is_threat=False, action=ALLOW
2026-10-03 19:27:26,692 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.115.4', '10.10.10.2', 443, 50307, 6) (pkts=5)
2026-10-03 19:27:26,697 [INFO] sagedral_ml.detection.decision: Decision for 172.217.115.4: sig_score=0.0, ml_score=0.006812395764375385, final_score=0.004087437458625231, is_threat=False, action=ALLOW
2026-10-03 19:27:26,738 [INFO] sagedral_ml.features.extractor: Flow completed and queued: ('172.217.115.4', '10.10.10.2', 443, 50304, 6) (pkts=3)
2026-10-03 19:27:26,743 [INFO] sagedral_ml.detection.decision: Decision for 172.217.115.4: sig_score=0.0, ml_score=0.005713624548923921, final_score=0.0034281747293543525, is_threat=False, action=ALLOW
2026-10-03 19:27:28,556 [INFO] sagedral_ml.api: SAGEDRAL-ML API server shutdown.
2026-10-03 19:27:28,556 [INFO] sagedral_ml.main: Signal received: shutting down SAGEDRAL-ML...
2026-10-03 19:27:28,587 [INFO] sagedral_ml.main: Processing worker thread exiting.
2026-10-03 19:27:28,988 [INFO] sagedral_ml.main: Capture thread exiting.
2026-10-03 19:31:06,397 [INFO] sagedral_ml.main: === Starting SAGEDRAL-ML NIDPS System ===
2026-10-03 19:31:06,397 [INFO] sagedral_ml.main: Logging initialized: Level=INFO | File=/var/log/sagedral-ml.log
2026-10-03 19:31:06,415 [INFO] sagedral_ml.detection.ml: Successfully loaded ML detection models.
2026-10-03 19:31:06,472 [INFO] sagedral_ml.ips.response: nftables table 'inet sagedral' initialized.
2026-10-03 19:52:00,601 [INFO] sagedral_ml.main: === Starting SAGEDRAL-ML NIDPS System ===
2026-10-03 19:52:00,601 [INFO] sagedral_ml.main: Logging initialized: Level=INFO | File=/var/log/sagedral-ml.log
2026-10-03 19:52:00,622 [INFO] sagedral_ml.detection.ml: Successfully loaded ML detection models.
2026-10-03 19:52:00,675 [INFO] sagedral_ml.ips.response: nftables table 'inet sagedral' initialized.
2026-10-03 19:54:14,909 [INFO] sagedral_ml.main: === Starting SAGEDRAL-ML NIDPS System ===
2026-10-03 19:54:14,909 [INFO] sagedral_ml.main: Logging initialized: Level=INFO | File=/var/log/sagedral-ml.log
2026-10-03 19:54:14,927 [INFO] sagedral_ml.detection.ml: Successfully loaded ML detection models.
2026-10-03 19:54:14,984 [INFO] sagedral_ml.ips.response: nftables table 'inet sagedral' initialized.
gaio@gaio-Aspire-A515-56:~/SAGEDRAL-ML-Smart-Adaptive-Guardian-for-Detection-Response-and-Adaptive-Learning-ML$ 