package inet.examples.inet.datacenter_topologies;

import inet.networklayer.configurator.ipv4.Ipv4NetworkConfigurator;
import inet.node.inet.Router;
import inet.node.inet.StandardHost;
import ned.DatarateChannel;
import inet.visualizer.integrated.IntegratedVisualizer;

network VL2_8_8_1_seed6_jitter
{
    parameters:
        @display("bgb=1200,500");
    types:
        channel defaultline extends DatarateChannel { delay = 100us; datarate = 8Mbps; per = 0; }
        channel infiniteline extends DatarateChannel { delay = 0s; datarate = 1000Gbps; per = 0; }
        channel torline extends DatarateChannel { delay = 100us; datarate = 4Mbps; per = 0; }
    submodules:
        agg_00: Router { parameters: @display("p=75,200;i=abstract/router;is=s"); gates: pppg[8]; }
        agg_01: Router { parameters: @display("p=225,200;i=abstract/router;is=s"); gates: pppg[8]; }
        agg_02: Router { parameters: @display("p=375,200;i=abstract/router;is=s"); gates: pppg[8]; }
        agg_03: Router { parameters: @display("p=525,200;i=abstract/router;is=s"); gates: pppg[8]; }
        agg_04: Router { parameters: @display("p=675,200;i=abstract/router;is=s"); gates: pppg[8]; }
        agg_05: Router { parameters: @display("p=825,200;i=abstract/router;is=s"); gates: pppg[8]; }
        agg_06: Router { parameters: @display("p=975,200;i=abstract/router;is=s"); gates: pppg[8]; }
        agg_07: Router { parameters: @display("p=1125,200;i=abstract/router;is=s"); gates: pppg[8]; }
        configurator: Ipv4NetworkConfigurator { parameters: @display("p=50,50;i=block/cogwheel;is=s"); }
        core_00: Router { parameters: @display("p=150,100;i=abstract/router;is=s"); gates: pppg[8]; }
        core_01: Router { parameters: @display("p=450,100;i=abstract/router;is=s"); gates: pppg[8]; }
        core_02: Router { parameters: @display("p=750,100;i=abstract/router;is=s"); gates: pppg[8]; }
        core_03: Router { parameters: @display("p=1050,100;i=abstract/router;is=s"); gates: pppg[8]; }
        host_00: Router { parameters: @display("p=37,400;i=device/server;is=s"); gates: pppg[11]; }
        host_01: Router { parameters: @display("p=112,400;i=device/server;is=s"); gates: pppg[11]; }
        host_02: Router { parameters: @display("p=187,400;i=device/server;is=s"); gates: pppg[11]; }
        host_03: Router { parameters: @display("p=262,400;i=device/server;is=s"); gates: pppg[11]; }
        host_04: Router { parameters: @display("p=337,400;i=device/server;is=s"); gates: pppg[11]; }
        host_05: Router { parameters: @display("p=412,400;i=device/server;is=s"); gates: pppg[11]; }
        host_06: Router { parameters: @display("p=487,400;i=device/server;is=s"); gates: pppg[11]; }
        host_07: Router { parameters: @display("p=562,400;i=device/server;is=s"); gates: pppg[11]; }
        host_08: Router { parameters: @display("p=637,400;i=device/server;is=s"); gates: pppg[11]; }
        host_09: Router { parameters: @display("p=712,400;i=device/server;is=s"); gates: pppg[11]; }
        host_10: Router { parameters: @display("p=787,400;i=device/server;is=s"); gates: pppg[11]; }
        host_11: Router { parameters: @display("p=862,400;i=device/server;is=s"); gates: pppg[11]; }
        host_12: Router { parameters: @display("p=937,400;i=device/server;is=s"); gates: pppg[11]; }
        host_13: Router { parameters: @display("p=1012,400;i=device/server;is=s"); gates: pppg[11]; }
        host_14: Router { parameters: @display("p=1087,400;i=device/server;is=s"); gates: pppg[11]; }
        host_15: Router { parameters: @display("p=1162,400;i=device/server;is=s"); gates: pppg[11]; }
        sink_000: StandardHost { parameters: @display("p=587,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_001: StandardHost { parameters: @display("p=587,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_002: StandardHost { parameters: @display("p=587,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_003: StandardHost { parameters: @display("p=587,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_004: StandardHost { parameters: @display("p=587,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_005: StandardHost { parameters: @display("p=587,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_006: StandardHost { parameters: @display("p=587,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_007: StandardHost { parameters: @display("p=587,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_008: StandardHost { parameters: @display("p=587,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_009: StandardHost { parameters: @display("p=587,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_010: StandardHost { parameters: @display("p=437,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_011: StandardHost { parameters: @display("p=437,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_012: StandardHost { parameters: @display("p=437,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_013: StandardHost { parameters: @display("p=437,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_014: StandardHost { parameters: @display("p=437,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_015: StandardHost { parameters: @display("p=437,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_016: StandardHost { parameters: @display("p=437,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_017: StandardHost { parameters: @display("p=437,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_018: StandardHost { parameters: @display("p=437,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_019: StandardHost { parameters: @display("p=437,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_020: StandardHost { parameters: @display("p=1187,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_021: StandardHost { parameters: @display("p=1187,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_022: StandardHost { parameters: @display("p=1187,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_023: StandardHost { parameters: @display("p=1187,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_024: StandardHost { parameters: @display("p=1187,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_025: StandardHost { parameters: @display("p=1187,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_026: StandardHost { parameters: @display("p=1187,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_027: StandardHost { parameters: @display("p=1187,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_028: StandardHost { parameters: @display("p=1187,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_029: StandardHost { parameters: @display("p=1187,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_030: StandardHost { parameters: @display("p=887,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_031: StandardHost { parameters: @display("p=887,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_032: StandardHost { parameters: @display("p=887,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_033: StandardHost { parameters: @display("p=887,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_034: StandardHost { parameters: @display("p=887,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_035: StandardHost { parameters: @display("p=887,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_036: StandardHost { parameters: @display("p=887,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_037: StandardHost { parameters: @display("p=887,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_038: StandardHost { parameters: @display("p=887,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_039: StandardHost { parameters: @display("p=887,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_040: StandardHost { parameters: @display("p=512,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_041: StandardHost { parameters: @display("p=512,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_042: StandardHost { parameters: @display("p=512,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_043: StandardHost { parameters: @display("p=512,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_044: StandardHost { parameters: @display("p=512,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_045: StandardHost { parameters: @display("p=512,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_046: StandardHost { parameters: @display("p=512,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_047: StandardHost { parameters: @display("p=512,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_048: StandardHost { parameters: @display("p=512,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_049: StandardHost { parameters: @display("p=512,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_050: StandardHost { parameters: @display("p=662,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_051: StandardHost { parameters: @display("p=662,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_052: StandardHost { parameters: @display("p=662,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_053: StandardHost { parameters: @display("p=662,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_054: StandardHost { parameters: @display("p=662,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_055: StandardHost { parameters: @display("p=662,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_056: StandardHost { parameters: @display("p=662,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_057: StandardHost { parameters: @display("p=662,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_058: StandardHost { parameters: @display("p=662,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_059: StandardHost { parameters: @display("p=662,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_060: StandardHost { parameters: @display("p=287,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_061: StandardHost { parameters: @display("p=287,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_062: StandardHost { parameters: @display("p=287,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_063: StandardHost { parameters: @display("p=287,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_064: StandardHost { parameters: @display("p=287,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_065: StandardHost { parameters: @display("p=287,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_066: StandardHost { parameters: @display("p=287,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_067: StandardHost { parameters: @display("p=287,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_068: StandardHost { parameters: @display("p=287,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_069: StandardHost { parameters: @display("p=287,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_070: StandardHost { parameters: @display("p=737,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_071: StandardHost { parameters: @display("p=737,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_072: StandardHost { parameters: @display("p=737,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_073: StandardHost { parameters: @display("p=737,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_074: StandardHost { parameters: @display("p=737,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_075: StandardHost { parameters: @display("p=737,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_076: StandardHost { parameters: @display("p=737,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_077: StandardHost { parameters: @display("p=737,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_078: StandardHost { parameters: @display("p=737,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_079: StandardHost { parameters: @display("p=737,450;i=block/sink;is=vs"); gates: pppg[1]; }
        source_000: StandardHost { parameters: @display("p=162,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_001: StandardHost { parameters: @display("p=162,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_002: StandardHost { parameters: @display("p=162,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_003: StandardHost { parameters: @display("p=162,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_004: StandardHost { parameters: @display("p=162,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_005: StandardHost { parameters: @display("p=162,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_006: StandardHost { parameters: @display("p=162,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_007: StandardHost { parameters: @display("p=162,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_008: StandardHost { parameters: @display("p=162,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_009: StandardHost { parameters: @display("p=162,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_010: StandardHost { parameters: @display("p=1062,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_011: StandardHost { parameters: @display("p=1062,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_012: StandardHost { parameters: @display("p=1062,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_013: StandardHost { parameters: @display("p=1062,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_014: StandardHost { parameters: @display("p=1062,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_015: StandardHost { parameters: @display("p=1062,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_016: StandardHost { parameters: @display("p=1062,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_017: StandardHost { parameters: @display("p=1062,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_018: StandardHost { parameters: @display("p=1062,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_019: StandardHost { parameters: @display("p=1062,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_020: StandardHost { parameters: @display("p=12,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_021: StandardHost { parameters: @display("p=12,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_022: StandardHost { parameters: @display("p=12,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_023: StandardHost { parameters: @display("p=12,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_024: StandardHost { parameters: @display("p=12,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_025: StandardHost { parameters: @display("p=12,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_026: StandardHost { parameters: @display("p=12,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_027: StandardHost { parameters: @display("p=12,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_028: StandardHost { parameters: @display("p=12,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_029: StandardHost { parameters: @display("p=12,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_030: StandardHost { parameters: @display("p=312,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_031: StandardHost { parameters: @display("p=312,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_032: StandardHost { parameters: @display("p=312,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_033: StandardHost { parameters: @display("p=312,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_034: StandardHost { parameters: @display("p=312,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_035: StandardHost { parameters: @display("p=312,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_036: StandardHost { parameters: @display("p=312,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_037: StandardHost { parameters: @display("p=312,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_038: StandardHost { parameters: @display("p=312,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_039: StandardHost { parameters: @display("p=312,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_040: StandardHost { parameters: @display("p=762,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_041: StandardHost { parameters: @display("p=762,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_042: StandardHost { parameters: @display("p=762,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_043: StandardHost { parameters: @display("p=762,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_044: StandardHost { parameters: @display("p=762,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_045: StandardHost { parameters: @display("p=762,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_046: StandardHost { parameters: @display("p=762,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_047: StandardHost { parameters: @display("p=762,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_048: StandardHost { parameters: @display("p=762,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_049: StandardHost { parameters: @display("p=762,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_050: StandardHost { parameters: @display("p=87,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_051: StandardHost { parameters: @display("p=87,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_052: StandardHost { parameters: @display("p=87,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_053: StandardHost { parameters: @display("p=87,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_054: StandardHost { parameters: @display("p=87,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_055: StandardHost { parameters: @display("p=87,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_056: StandardHost { parameters: @display("p=87,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_057: StandardHost { parameters: @display("p=87,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_058: StandardHost { parameters: @display("p=87,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_059: StandardHost { parameters: @display("p=87,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_060: StandardHost { parameters: @display("p=987,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_061: StandardHost { parameters: @display("p=987,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_062: StandardHost { parameters: @display("p=987,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_063: StandardHost { parameters: @display("p=987,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_064: StandardHost { parameters: @display("p=987,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_065: StandardHost { parameters: @display("p=987,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_066: StandardHost { parameters: @display("p=987,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_067: StandardHost { parameters: @display("p=987,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_068: StandardHost { parameters: @display("p=987,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_069: StandardHost { parameters: @display("p=987,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_070: StandardHost { parameters: @display("p=912,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_071: StandardHost { parameters: @display("p=912,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_072: StandardHost { parameters: @display("p=912,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_073: StandardHost { parameters: @display("p=912,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_074: StandardHost { parameters: @display("p=912,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_075: StandardHost { parameters: @display("p=912,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_076: StandardHost { parameters: @display("p=912,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_077: StandardHost { parameters: @display("p=912,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_078: StandardHost { parameters: @display("p=912,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_079: StandardHost { parameters: @display("p=912,450;i=block/source;is=vs"); gates: pppg[1]; }
        tor_00: Router { parameters: @display("p=37,300;i=device/switch;is=s"); gates: pppg[3]; }
        tor_01: Router { parameters: @display("p=112,300;i=device/switch;is=s"); gates: pppg[3]; }
        tor_02: Router { parameters: @display("p=187,300;i=device/switch;is=s"); gates: pppg[3]; }
        tor_03: Router { parameters: @display("p=262,300;i=device/switch;is=s"); gates: pppg[3]; }
        tor_04: Router { parameters: @display("p=337,300;i=device/switch;is=s"); gates: pppg[3]; }
        tor_05: Router { parameters: @display("p=412,300;i=device/switch;is=s"); gates: pppg[3]; }
        tor_06: Router { parameters: @display("p=487,300;i=device/switch;is=s"); gates: pppg[3]; }
        tor_07: Router { parameters: @display("p=562,300;i=device/switch;is=s"); gates: pppg[3]; }
        tor_08: Router { parameters: @display("p=637,300;i=device/switch;is=s"); gates: pppg[3]; }
        tor_09: Router { parameters: @display("p=712,300;i=device/switch;is=s"); gates: pppg[3]; }
        tor_10: Router { parameters: @display("p=787,300;i=device/switch;is=s"); gates: pppg[3]; }
        tor_11: Router { parameters: @display("p=862,300;i=device/switch;is=s"); gates: pppg[3]; }
        tor_12: Router { parameters: @display("p=937,300;i=device/switch;is=s"); gates: pppg[3]; }
        tor_13: Router { parameters: @display("p=1012,300;i=device/switch;is=s"); gates: pppg[3]; }
        tor_14: Router { parameters: @display("p=1087,300;i=device/switch;is=s"); gates: pppg[3]; }
        tor_15: Router { parameters: @display("p=1162,300;i=device/switch;is=s"); gates: pppg[3]; }
    connections:
        agg_00.pppg[0] <--> defaultline <--> core_00.pppg[0];
        agg_00.pppg[1] <--> defaultline <--> core_01.pppg[0];
        agg_00.pppg[2] <--> defaultline <--> core_02.pppg[0];
        agg_00.pppg[3] <--> defaultline <--> core_03.pppg[0];
        agg_00.pppg[4] <--> torline <--> tor_00.pppg[0];
        agg_00.pppg[5] <--> torline <--> tor_01.pppg[0];
        agg_00.pppg[6] <--> torline <--> tor_02.pppg[0];
        agg_00.pppg[7] <--> torline <--> tor_03.pppg[0];
        agg_01.pppg[0] <--> defaultline <--> core_00.pppg[1];
        agg_01.pppg[1] <--> defaultline <--> core_01.pppg[1];
        agg_01.pppg[2] <--> defaultline <--> core_02.pppg[1];
        agg_01.pppg[3] <--> defaultline <--> core_03.pppg[1];
        agg_01.pppg[4] <--> torline <--> tor_00.pppg[1];
        agg_01.pppg[5] <--> torline <--> tor_01.pppg[1];
        agg_01.pppg[6] <--> torline <--> tor_02.pppg[1];
        agg_01.pppg[7] <--> torline <--> tor_03.pppg[1];
        agg_02.pppg[0] <--> defaultline <--> core_00.pppg[2];
        agg_02.pppg[1] <--> defaultline <--> core_01.pppg[2];
        agg_02.pppg[2] <--> defaultline <--> core_02.pppg[2];
        agg_02.pppg[3] <--> defaultline <--> core_03.pppg[2];
        agg_02.pppg[4] <--> torline <--> tor_04.pppg[0];
        agg_02.pppg[5] <--> torline <--> tor_05.pppg[0];
        agg_02.pppg[6] <--> torline <--> tor_06.pppg[0];
        agg_02.pppg[7] <--> torline <--> tor_07.pppg[0];
        agg_03.pppg[0] <--> defaultline <--> core_00.pppg[3];
        agg_03.pppg[1] <--> defaultline <--> core_01.pppg[3];
        agg_03.pppg[2] <--> defaultline <--> core_02.pppg[3];
        agg_03.pppg[3] <--> defaultline <--> core_03.pppg[3];
        agg_03.pppg[4] <--> torline <--> tor_04.pppg[1];
        agg_03.pppg[5] <--> torline <--> tor_05.pppg[1];
        agg_03.pppg[6] <--> torline <--> tor_06.pppg[1];
        agg_03.pppg[7] <--> torline <--> tor_07.pppg[1];
        agg_04.pppg[0] <--> defaultline <--> core_00.pppg[4];
        agg_04.pppg[1] <--> defaultline <--> core_01.pppg[4];
        agg_04.pppg[2] <--> defaultline <--> core_02.pppg[4];
        agg_04.pppg[3] <--> defaultline <--> core_03.pppg[4];
        agg_04.pppg[4] <--> torline <--> tor_08.pppg[0];
        agg_04.pppg[5] <--> torline <--> tor_09.pppg[0];
        agg_04.pppg[6] <--> torline <--> tor_10.pppg[0];
        agg_04.pppg[7] <--> torline <--> tor_11.pppg[0];
        agg_05.pppg[0] <--> defaultline <--> core_00.pppg[5];
        agg_05.pppg[1] <--> defaultline <--> core_01.pppg[5];
        agg_05.pppg[2] <--> defaultline <--> core_02.pppg[5];
        agg_05.pppg[3] <--> defaultline <--> core_03.pppg[5];
        agg_05.pppg[4] <--> torline <--> tor_08.pppg[1];
        agg_05.pppg[5] <--> torline <--> tor_09.pppg[1];
        agg_05.pppg[6] <--> torline <--> tor_10.pppg[1];
        agg_05.pppg[7] <--> torline <--> tor_11.pppg[1];
        agg_06.pppg[0] <--> defaultline <--> core_00.pppg[6];
        agg_06.pppg[1] <--> defaultline <--> core_01.pppg[6];
        agg_06.pppg[2] <--> defaultline <--> core_02.pppg[6];
        agg_06.pppg[3] <--> defaultline <--> core_03.pppg[6];
        agg_06.pppg[4] <--> torline <--> tor_12.pppg[0];
        agg_06.pppg[5] <--> torline <--> tor_13.pppg[0];
        agg_06.pppg[6] <--> torline <--> tor_14.pppg[0];
        agg_06.pppg[7] <--> torline <--> tor_15.pppg[0];
        agg_07.pppg[0] <--> defaultline <--> core_00.pppg[7];
        agg_07.pppg[1] <--> defaultline <--> core_01.pppg[7];
        agg_07.pppg[2] <--> defaultline <--> core_02.pppg[7];
        agg_07.pppg[3] <--> defaultline <--> core_03.pppg[7];
        agg_07.pppg[4] <--> torline <--> tor_12.pppg[1];
        agg_07.pppg[5] <--> torline <--> tor_13.pppg[1];
        agg_07.pppg[6] <--> torline <--> tor_14.pppg[1];
        agg_07.pppg[7] <--> torline <--> tor_15.pppg[1];
        host_00.pppg[0] <--> infiniteline <--> source_020.pppg[0];
        host_00.pppg[10] <--> defaultline <--> tor_00.pppg[2];
        host_00.pppg[1] <--> infiniteline <--> source_021.pppg[0];
        host_00.pppg[2] <--> infiniteline <--> source_022.pppg[0];
        host_00.pppg[3] <--> infiniteline <--> source_023.pppg[0];
        host_00.pppg[4] <--> infiniteline <--> source_024.pppg[0];
        host_00.pppg[5] <--> infiniteline <--> source_025.pppg[0];
        host_00.pppg[6] <--> infiniteline <--> source_026.pppg[0];
        host_00.pppg[7] <--> infiniteline <--> source_027.pppg[0];
        host_00.pppg[8] <--> infiniteline <--> source_028.pppg[0];
        host_00.pppg[9] <--> infiniteline <--> source_029.pppg[0];
        host_01.pppg[0] <--> infiniteline <--> source_050.pppg[0];
        host_01.pppg[10] <--> defaultline <--> tor_01.pppg[2];
        host_01.pppg[1] <--> infiniteline <--> source_051.pppg[0];
        host_01.pppg[2] <--> infiniteline <--> source_052.pppg[0];
        host_01.pppg[3] <--> infiniteline <--> source_053.pppg[0];
        host_01.pppg[4] <--> infiniteline <--> source_054.pppg[0];
        host_01.pppg[5] <--> infiniteline <--> source_055.pppg[0];
        host_01.pppg[6] <--> infiniteline <--> source_056.pppg[0];
        host_01.pppg[7] <--> infiniteline <--> source_057.pppg[0];
        host_01.pppg[8] <--> infiniteline <--> source_058.pppg[0];
        host_01.pppg[9] <--> infiniteline <--> source_059.pppg[0];
        host_02.pppg[0] <--> infiniteline <--> source_000.pppg[0];
        host_02.pppg[10] <--> defaultline <--> tor_02.pppg[2];
        host_02.pppg[1] <--> infiniteline <--> source_001.pppg[0];
        host_02.pppg[2] <--> infiniteline <--> source_002.pppg[0];
        host_02.pppg[3] <--> infiniteline <--> source_003.pppg[0];
        host_02.pppg[4] <--> infiniteline <--> source_004.pppg[0];
        host_02.pppg[5] <--> infiniteline <--> source_005.pppg[0];
        host_02.pppg[6] <--> infiniteline <--> source_006.pppg[0];
        host_02.pppg[7] <--> infiniteline <--> source_007.pppg[0];
        host_02.pppg[8] <--> infiniteline <--> source_008.pppg[0];
        host_02.pppg[9] <--> infiniteline <--> source_009.pppg[0];
        host_03.pppg[0] <--> infiniteline <--> sink_060.pppg[0];
        host_03.pppg[10] <--> defaultline <--> tor_03.pppg[2];
        host_03.pppg[1] <--> infiniteline <--> sink_061.pppg[0];
        host_03.pppg[2] <--> infiniteline <--> sink_062.pppg[0];
        host_03.pppg[3] <--> infiniteline <--> sink_063.pppg[0];
        host_03.pppg[4] <--> infiniteline <--> sink_064.pppg[0];
        host_03.pppg[5] <--> infiniteline <--> sink_065.pppg[0];
        host_03.pppg[6] <--> infiniteline <--> sink_066.pppg[0];
        host_03.pppg[7] <--> infiniteline <--> sink_067.pppg[0];
        host_03.pppg[8] <--> infiniteline <--> sink_068.pppg[0];
        host_03.pppg[9] <--> infiniteline <--> sink_069.pppg[0];
        host_04.pppg[0] <--> infiniteline <--> source_030.pppg[0];
        host_04.pppg[10] <--> defaultline <--> tor_04.pppg[2];
        host_04.pppg[1] <--> infiniteline <--> source_031.pppg[0];
        host_04.pppg[2] <--> infiniteline <--> source_032.pppg[0];
        host_04.pppg[3] <--> infiniteline <--> source_033.pppg[0];
        host_04.pppg[4] <--> infiniteline <--> source_034.pppg[0];
        host_04.pppg[5] <--> infiniteline <--> source_035.pppg[0];
        host_04.pppg[6] <--> infiniteline <--> source_036.pppg[0];
        host_04.pppg[7] <--> infiniteline <--> source_037.pppg[0];
        host_04.pppg[8] <--> infiniteline <--> source_038.pppg[0];
        host_04.pppg[9] <--> infiniteline <--> source_039.pppg[0];
        host_05.pppg[0] <--> infiniteline <--> sink_010.pppg[0];
        host_05.pppg[10] <--> defaultline <--> tor_05.pppg[2];
        host_05.pppg[1] <--> infiniteline <--> sink_011.pppg[0];
        host_05.pppg[2] <--> infiniteline <--> sink_012.pppg[0];
        host_05.pppg[3] <--> infiniteline <--> sink_013.pppg[0];
        host_05.pppg[4] <--> infiniteline <--> sink_014.pppg[0];
        host_05.pppg[5] <--> infiniteline <--> sink_015.pppg[0];
        host_05.pppg[6] <--> infiniteline <--> sink_016.pppg[0];
        host_05.pppg[7] <--> infiniteline <--> sink_017.pppg[0];
        host_05.pppg[8] <--> infiniteline <--> sink_018.pppg[0];
        host_05.pppg[9] <--> infiniteline <--> sink_019.pppg[0];
        host_06.pppg[0] <--> infiniteline <--> sink_040.pppg[0];
        host_06.pppg[10] <--> defaultline <--> tor_06.pppg[2];
        host_06.pppg[1] <--> infiniteline <--> sink_041.pppg[0];
        host_06.pppg[2] <--> infiniteline <--> sink_042.pppg[0];
        host_06.pppg[3] <--> infiniteline <--> sink_043.pppg[0];
        host_06.pppg[4] <--> infiniteline <--> sink_044.pppg[0];
        host_06.pppg[5] <--> infiniteline <--> sink_045.pppg[0];
        host_06.pppg[6] <--> infiniteline <--> sink_046.pppg[0];
        host_06.pppg[7] <--> infiniteline <--> sink_047.pppg[0];
        host_06.pppg[8] <--> infiniteline <--> sink_048.pppg[0];
        host_06.pppg[9] <--> infiniteline <--> sink_049.pppg[0];
        host_07.pppg[0] <--> infiniteline <--> sink_000.pppg[0];
        host_07.pppg[10] <--> defaultline <--> tor_07.pppg[2];
        host_07.pppg[1] <--> infiniteline <--> sink_001.pppg[0];
        host_07.pppg[2] <--> infiniteline <--> sink_002.pppg[0];
        host_07.pppg[3] <--> infiniteline <--> sink_003.pppg[0];
        host_07.pppg[4] <--> infiniteline <--> sink_004.pppg[0];
        host_07.pppg[5] <--> infiniteline <--> sink_005.pppg[0];
        host_07.pppg[6] <--> infiniteline <--> sink_006.pppg[0];
        host_07.pppg[7] <--> infiniteline <--> sink_007.pppg[0];
        host_07.pppg[8] <--> infiniteline <--> sink_008.pppg[0];
        host_07.pppg[9] <--> infiniteline <--> sink_009.pppg[0];
        host_08.pppg[0] <--> infiniteline <--> sink_050.pppg[0];
        host_08.pppg[10] <--> defaultline <--> tor_08.pppg[2];
        host_08.pppg[1] <--> infiniteline <--> sink_051.pppg[0];
        host_08.pppg[2] <--> infiniteline <--> sink_052.pppg[0];
        host_08.pppg[3] <--> infiniteline <--> sink_053.pppg[0];
        host_08.pppg[4] <--> infiniteline <--> sink_054.pppg[0];
        host_08.pppg[5] <--> infiniteline <--> sink_055.pppg[0];
        host_08.pppg[6] <--> infiniteline <--> sink_056.pppg[0];
        host_08.pppg[7] <--> infiniteline <--> sink_057.pppg[0];
        host_08.pppg[8] <--> infiniteline <--> sink_058.pppg[0];
        host_08.pppg[9] <--> infiniteline <--> sink_059.pppg[0];
        host_09.pppg[0] <--> infiniteline <--> sink_070.pppg[0];
        host_09.pppg[10] <--> defaultline <--> tor_09.pppg[2];
        host_09.pppg[1] <--> infiniteline <--> sink_071.pppg[0];
        host_09.pppg[2] <--> infiniteline <--> sink_072.pppg[0];
        host_09.pppg[3] <--> infiniteline <--> sink_073.pppg[0];
        host_09.pppg[4] <--> infiniteline <--> sink_074.pppg[0];
        host_09.pppg[5] <--> infiniteline <--> sink_075.pppg[0];
        host_09.pppg[6] <--> infiniteline <--> sink_076.pppg[0];
        host_09.pppg[7] <--> infiniteline <--> sink_077.pppg[0];
        host_09.pppg[8] <--> infiniteline <--> sink_078.pppg[0];
        host_09.pppg[9] <--> infiniteline <--> sink_079.pppg[0];
        host_10.pppg[0] <--> infiniteline <--> source_040.pppg[0];
        host_10.pppg[10] <--> defaultline <--> tor_10.pppg[2];
        host_10.pppg[1] <--> infiniteline <--> source_041.pppg[0];
        host_10.pppg[2] <--> infiniteline <--> source_042.pppg[0];
        host_10.pppg[3] <--> infiniteline <--> source_043.pppg[0];
        host_10.pppg[4] <--> infiniteline <--> source_044.pppg[0];
        host_10.pppg[5] <--> infiniteline <--> source_045.pppg[0];
        host_10.pppg[6] <--> infiniteline <--> source_046.pppg[0];
        host_10.pppg[7] <--> infiniteline <--> source_047.pppg[0];
        host_10.pppg[8] <--> infiniteline <--> source_048.pppg[0];
        host_10.pppg[9] <--> infiniteline <--> source_049.pppg[0];
        host_11.pppg[0] <--> infiniteline <--> sink_030.pppg[0];
        host_11.pppg[10] <--> defaultline <--> tor_11.pppg[2];
        host_11.pppg[1] <--> infiniteline <--> sink_031.pppg[0];
        host_11.pppg[2] <--> infiniteline <--> sink_032.pppg[0];
        host_11.pppg[3] <--> infiniteline <--> sink_033.pppg[0];
        host_11.pppg[4] <--> infiniteline <--> sink_034.pppg[0];
        host_11.pppg[5] <--> infiniteline <--> sink_035.pppg[0];
        host_11.pppg[6] <--> infiniteline <--> sink_036.pppg[0];
        host_11.pppg[7] <--> infiniteline <--> sink_037.pppg[0];
        host_11.pppg[8] <--> infiniteline <--> sink_038.pppg[0];
        host_11.pppg[9] <--> infiniteline <--> sink_039.pppg[0];
        host_12.pppg[0] <--> infiniteline <--> source_070.pppg[0];
        host_12.pppg[10] <--> defaultline <--> tor_12.pppg[2];
        host_12.pppg[1] <--> infiniteline <--> source_071.pppg[0];
        host_12.pppg[2] <--> infiniteline <--> source_072.pppg[0];
        host_12.pppg[3] <--> infiniteline <--> source_073.pppg[0];
        host_12.pppg[4] <--> infiniteline <--> source_074.pppg[0];
        host_12.pppg[5] <--> infiniteline <--> source_075.pppg[0];
        host_12.pppg[6] <--> infiniteline <--> source_076.pppg[0];
        host_12.pppg[7] <--> infiniteline <--> source_077.pppg[0];
        host_12.pppg[8] <--> infiniteline <--> source_078.pppg[0];
        host_12.pppg[9] <--> infiniteline <--> source_079.pppg[0];
        host_13.pppg[0] <--> infiniteline <--> source_060.pppg[0];
        host_13.pppg[10] <--> defaultline <--> tor_13.pppg[2];
        host_13.pppg[1] <--> infiniteline <--> source_061.pppg[0];
        host_13.pppg[2] <--> infiniteline <--> source_062.pppg[0];
        host_13.pppg[3] <--> infiniteline <--> source_063.pppg[0];
        host_13.pppg[4] <--> infiniteline <--> source_064.pppg[0];
        host_13.pppg[5] <--> infiniteline <--> source_065.pppg[0];
        host_13.pppg[6] <--> infiniteline <--> source_066.pppg[0];
        host_13.pppg[7] <--> infiniteline <--> source_067.pppg[0];
        host_13.pppg[8] <--> infiniteline <--> source_068.pppg[0];
        host_13.pppg[9] <--> infiniteline <--> source_069.pppg[0];
        host_14.pppg[0] <--> infiniteline <--> source_010.pppg[0];
        host_14.pppg[10] <--> defaultline <--> tor_14.pppg[2];
        host_14.pppg[1] <--> infiniteline <--> source_011.pppg[0];
        host_14.pppg[2] <--> infiniteline <--> source_012.pppg[0];
        host_14.pppg[3] <--> infiniteline <--> source_013.pppg[0];
        host_14.pppg[4] <--> infiniteline <--> source_014.pppg[0];
        host_14.pppg[5] <--> infiniteline <--> source_015.pppg[0];
        host_14.pppg[6] <--> infiniteline <--> source_016.pppg[0];
        host_14.pppg[7] <--> infiniteline <--> source_017.pppg[0];
        host_14.pppg[8] <--> infiniteline <--> source_018.pppg[0];
        host_14.pppg[9] <--> infiniteline <--> source_019.pppg[0];
        host_15.pppg[0] <--> infiniteline <--> sink_020.pppg[0];
        host_15.pppg[10] <--> defaultline <--> tor_15.pppg[2];
        host_15.pppg[1] <--> infiniteline <--> sink_021.pppg[0];
        host_15.pppg[2] <--> infiniteline <--> sink_022.pppg[0];
        host_15.pppg[3] <--> infiniteline <--> sink_023.pppg[0];
        host_15.pppg[4] <--> infiniteline <--> sink_024.pppg[0];
        host_15.pppg[5] <--> infiniteline <--> sink_025.pppg[0];
        host_15.pppg[6] <--> infiniteline <--> sink_026.pppg[0];
        host_15.pppg[7] <--> infiniteline <--> sink_027.pppg[0];
        host_15.pppg[8] <--> infiniteline <--> sink_028.pppg[0];
        host_15.pppg[9] <--> infiniteline <--> sink_029.pppg[0];
}