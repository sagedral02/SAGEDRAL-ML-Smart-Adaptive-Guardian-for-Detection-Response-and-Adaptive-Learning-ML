"""
Unit tests for FlowRecord and 28-feature extraction vector generator.
"""

import time
from sagedral_ml.features.models import FlowRecord


def test_flow_record_feature_vector():
    flow = FlowRecord(
        src_ip="192.168.1.50",
        dst_ip="10.0.0.1",
        src_port=54321,
        dst_port=80,
        protocol=6,
        start_time=100.0,
        end_time=105.0,
    )

    # Forward packet
    flow.add_packet(pkt_len=100, header_len=40, flags={"SYN": True}, is_forward=True, timestamp=100.0)
    # Backward packet
    flow.add_packet(pkt_len=200, header_len=40, flags={"SYN": True, "ACK": True}, is_forward=False, timestamp=101.0)
    # Forward packet
    flow.add_packet(pkt_len=150, header_len=40, flags={"ACK": True, "PSH": True}, is_forward=True, timestamp=102.0)

    vec = flow.to_feature_vector()

    assert len(vec) == 28
    assert vec["duration"] == 2.0  # end_time updated by last packet at t=102.0, start=100.0
    assert vec["total_fwd_packets"] == 2
    assert vec["total_bwd_packets"] == 1
    assert vec["total_fwd_bytes"] == 250
    assert vec["total_bwd_bytes"] == 200
    assert vec["syn_flag_count"] == 2
    assert vec["ack_flag_count"] == 2
    assert vec["psh_flag_count"] == 1
    assert vec["protocol"] == 6
    assert vec["dst_port"] == 80


def test_single_packet_zero_duration_rate():
    flow = FlowRecord(
        src_ip="192.168.88.251",
        dst_ip="224.0.0.252",
        src_port=5355,
        dst_port=5355,
        protocol=17,
        start_time=100.0,
        end_time=100.0,
    )
    flow.add_packet(pkt_len=75, header_len=28, flags={}, is_forward=True, timestamp=100.0)

    vec = flow.to_feature_vector()
    assert vec["total_fwd_packets"] == 1
    assert vec["flow_packets_per_sec"] == 0.0
    assert vec["flow_bytes_per_sec"] == 0.0

