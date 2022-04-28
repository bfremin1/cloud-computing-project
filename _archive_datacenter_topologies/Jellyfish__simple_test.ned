package inet.examples.inet.datacenter_topologies;

import inet.networklayer.configurator.ipv4.Ipv4NetworkConfigurator;
import inet.node.inet.Router;
import inet.node.inet.StandardHost;
import ned.DatarateChannel;
import inet.visualizer.integrated.IntegratedVisualizer;

network Jellyfish__simple_test
{
    parameters:
        @display("bgb=1200,500");
    types:
        channel defaultline extends DatarateChannel { delay = 100us; datarate = 8Mbps; per = 0; }
        channel infiniteline extends DatarateChannel { delay = 0s; datarate = 1000Gbps; per = 0; }
    submodules:
        configurator: Ipv4NetworkConfigurator { parameters: @display("p=50,50;i=block/cogwheel;is=s"); }
        core_00: Router { parameters: @display("p=725,250;i=abstract/router;is=s"); gates: pppg[4]; }
        core_01: Router { parameters: @display("p=688,338;i=abstract/router;is=s"); gates: pppg[4]; }
        core_02: Router { parameters: @display("p=600,375;i=abstract/router;is=s"); gates: pppg[4]; }
        core_03: Router { parameters: @display("p=511,338;i=abstract/router;is=s"); gates: pppg[4]; }
        core_04: Router { parameters: @display("p=475,250;i=abstract/router;is=s"); gates: pppg[4]; }
        core_05: Router { parameters: @display("p=511,161;i=abstract/router;is=s"); gates: pppg[4]; }
        core_06: Router { parameters: @display("p=600,125;i=abstract/router;is=s"); gates: pppg[4]; }
        core_07: Router { parameters: @display("p=688,161;i=abstract/router;is=s"); gates: pppg[4]; }
        core_08: Router { parameters: @display("p=650,250;i=abstract/router;is=s"); gates: pppg[4]; }
        core_09: Router { parameters: @display("p=600,300;i=abstract/router;is=s"); gates: pppg[4]; }
        core_10: Router { parameters: @display("p=550,250;i=abstract/router;is=s"); gates: pppg[4]; }
        core_11: Router { parameters: @display("p=600,200;i=abstract/router;is=s"); gates: pppg[4]; }
        host_00: Router { parameters: @display("p=800,250;i=device/server;is=s"); gates: pppg[12]; }
        host_01: Router { parameters: @display("p=741,391;i=device/server;is=s"); gates: pppg[13]; }
        host_02: Router { parameters: @display("p=600,450;i=device/server;is=s"); gates: pppg[12]; }
        host_03: Router { parameters: @display("p=458,391;i=device/server;is=s"); gates: pppg[13]; }
        host_04: Router { parameters: @display("p=400,250;i=device/server;is=s"); gates: pppg[5]; }
        host_05: Router { parameters: @display("p=458,108;i=device/server;is=s"); gates: pppg[9]; }
        host_06: Router { parameters: @display("p=600,50;i=device/server;is=s"); gates: pppg[9]; }
        host_07: Router { parameters: @display("p=741,108;i=device/server;is=s"); gates: pppg[5]; }
        sink_000: StandardHost { parameters: @display("p=807,111;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_001: StandardHost { parameters: @display("p=807,111;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_002: StandardHost { parameters: @display("p=807,111;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_003: StandardHost { parameters: @display("p=807,111;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_004: StandardHost { parameters: @display("p=461,42;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_005: StandardHost { parameters: @display("p=461,42;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_006: StandardHost { parameters: @display("p=461,42;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_007: StandardHost { parameters: @display("p=461,42;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_008: StandardHost { parameters: @display("p=461,42;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_009: StandardHost { parameters: @display("p=461,42;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_010: StandardHost { parameters: @display("p=461,42;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_011: StandardHost { parameters: @display("p=461,42;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_012: StandardHost { parameters: @display("p=392,388;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_013: StandardHost { parameters: @display("p=392,388;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_014: StandardHost { parameters: @display("p=392,388;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_015: StandardHost { parameters: @display("p=392,388;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_016: StandardHost { parameters: @display("p=392,388;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_017: StandardHost { parameters: @display("p=392,388;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_018: StandardHost { parameters: @display("p=392,388;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_019: StandardHost { parameters: @display("p=392,388;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_020: StandardHost { parameters: @display("p=392,388;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_021: StandardHost { parameters: @display("p=392,388;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_022: StandardHost { parameters: @display("p=392,388;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_023: StandardHost { parameters: @display("p=392,388;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_024: StandardHost { parameters: @display("p=551,495;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_025: StandardHost { parameters: @display("p=551,495;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_026: StandardHost { parameters: @display("p=551,495;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_027: StandardHost { parameters: @display("p=551,495;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_028: StandardHost { parameters: @display("p=551,495;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_029: StandardHost { parameters: @display("p=551,495;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_030: StandardHost { parameters: @display("p=551,495;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_031: StandardHost { parameters: @display("p=551,495;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_032: StandardHost { parameters: @display("p=551,495;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_033: StandardHost { parameters: @display("p=551,495;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_034: StandardHost { parameters: @display("p=551,495;i=block/sink;is=vs"); gates: pppg[1]; }
        source_000: StandardHost { parameters: @display("p=354,298;i=block/source;is=vs"); gates: pppg[1]; }
        source_001: StandardHost { parameters: @display("p=354,298;i=block/source;is=vs"); gates: pppg[1]; }
        source_002: StandardHost { parameters: @display("p=354,298;i=block/source;is=vs"); gates: pppg[1]; }
        source_003: StandardHost { parameters: @display("p=354,298;i=block/source;is=vs"); gates: pppg[1]; }
        source_004: StandardHost { parameters: @display("p=551,4;i=block/source;is=vs"); gates: pppg[1]; }
        source_005: StandardHost { parameters: @display("p=551,4;i=block/source;is=vs"); gates: pppg[1]; }
        source_006: StandardHost { parameters: @display("p=551,4;i=block/source;is=vs"); gates: pppg[1]; }
        source_007: StandardHost { parameters: @display("p=551,4;i=block/source;is=vs"); gates: pppg[1]; }
        source_008: StandardHost { parameters: @display("p=551,4;i=block/source;is=vs"); gates: pppg[1]; }
        source_009: StandardHost { parameters: @display("p=551,4;i=block/source;is=vs"); gates: pppg[1]; }
        source_010: StandardHost { parameters: @display("p=551,4;i=block/source;is=vs"); gates: pppg[1]; }
        source_011: StandardHost { parameters: @display("p=551,4;i=block/source;is=vs"); gates: pppg[1]; }
        source_012: StandardHost { parameters: @display("p=807,388;i=block/source;is=vs"); gates: pppg[1]; }
        source_013: StandardHost { parameters: @display("p=807,388;i=block/source;is=vs"); gates: pppg[1]; }
        source_014: StandardHost { parameters: @display("p=807,388;i=block/source;is=vs"); gates: pppg[1]; }
        source_015: StandardHost { parameters: @display("p=807,388;i=block/source;is=vs"); gates: pppg[1]; }
        source_016: StandardHost { parameters: @display("p=807,388;i=block/source;is=vs"); gates: pppg[1]; }
        source_017: StandardHost { parameters: @display("p=807,388;i=block/source;is=vs"); gates: pppg[1]; }
        source_018: StandardHost { parameters: @display("p=807,388;i=block/source;is=vs"); gates: pppg[1]; }
        source_019: StandardHost { parameters: @display("p=807,388;i=block/source;is=vs"); gates: pppg[1]; }
        source_020: StandardHost { parameters: @display("p=807,388;i=block/source;is=vs"); gates: pppg[1]; }
        source_021: StandardHost { parameters: @display("p=807,388;i=block/source;is=vs"); gates: pppg[1]; }
        source_022: StandardHost { parameters: @display("p=807,388;i=block/source;is=vs"); gates: pppg[1]; }
        source_023: StandardHost { parameters: @display("p=807,388;i=block/source;is=vs"); gates: pppg[1]; }
        source_024: StandardHost { parameters: @display("p=845,201;i=block/source;is=vs"); gates: pppg[1]; }
        source_025: StandardHost { parameters: @display("p=845,201;i=block/source;is=vs"); gates: pppg[1]; }
        source_026: StandardHost { parameters: @display("p=845,201;i=block/source;is=vs"); gates: pppg[1]; }
        source_027: StandardHost { parameters: @display("p=845,201;i=block/source;is=vs"); gates: pppg[1]; }
        source_028: StandardHost { parameters: @display("p=845,201;i=block/source;is=vs"); gates: pppg[1]; }
        source_029: StandardHost { parameters: @display("p=845,201;i=block/source;is=vs"); gates: pppg[1]; }
        source_030: StandardHost { parameters: @display("p=845,201;i=block/source;is=vs"); gates: pppg[1]; }
        source_031: StandardHost { parameters: @display("p=845,201;i=block/source;is=vs"); gates: pppg[1]; }
        source_032: StandardHost { parameters: @display("p=845,201;i=block/source;is=vs"); gates: pppg[1]; }
        source_033: StandardHost { parameters: @display("p=845,201;i=block/source;is=vs"); gates: pppg[1]; }
        source_034: StandardHost { parameters: @display("p=845,201;i=block/source;is=vs"); gates: pppg[1]; }
    connections:
        core_00.pppg[0] <--> defaultline <--> core_02.pppg[0];
        core_00.pppg[1] <--> defaultline <--> core_06.pppg[0];
        core_00.pppg[2] <--> defaultline <--> core_09.pppg[0];
        core_00.pppg[3] <--> defaultline <--> host_00.pppg[0];
        core_01.pppg[0] <--> defaultline <--> core_03.pppg[0];
        core_01.pppg[1] <--> defaultline <--> core_10.pppg[0];
        core_01.pppg[2] <--> defaultline <--> core_11.pppg[0];
        core_01.pppg[3] <--> defaultline <--> host_01.pppg[0];
        core_02.pppg[1] <--> defaultline <--> core_05.pppg[0];
        core_02.pppg[2] <--> defaultline <--> core_07.pppg[0];
        core_02.pppg[3] <--> defaultline <--> host_02.pppg[0];
        core_03.pppg[1] <--> defaultline <--> core_08.pppg[0];
        core_03.pppg[2] <--> defaultline <--> core_10.pppg[1];
        core_03.pppg[3] <--> defaultline <--> host_03.pppg[0];
        core_04.pppg[0] <--> defaultline <--> core_05.pppg[1];
        core_04.pppg[1] <--> defaultline <--> core_08.pppg[1];
        core_04.pppg[2] <--> defaultline <--> core_10.pppg[2];
        core_04.pppg[3] <--> defaultline <--> host_04.pppg[0];
        core_05.pppg[2] <--> defaultline <--> core_11.pppg[1];
        core_05.pppg[3] <--> defaultline <--> host_05.pppg[0];
        core_06.pppg[1] <--> defaultline <--> core_07.pppg[1];
        core_06.pppg[2] <--> defaultline <--> core_11.pppg[2];
        core_06.pppg[3] <--> defaultline <--> host_06.pppg[0];
        core_07.pppg[2] <--> defaultline <--> core_09.pppg[1];
        core_07.pppg[3] <--> defaultline <--> host_07.pppg[0];
        core_08.pppg[2] <--> defaultline <--> core_09.pppg[2];
        core_08.pppg[3] <--> defaultline <--> core_11.pppg[3];
        core_09.pppg[3] <--> defaultline <--> core_10.pppg[3];
        host_00.pppg[10] <--> infiniteline <--> source_033.pppg[0];
        host_00.pppg[11] <--> infiniteline <--> source_034.pppg[0];
        host_00.pppg[1] <--> infiniteline <--> source_024.pppg[0];
        host_00.pppg[2] <--> infiniteline <--> source_025.pppg[0];
        host_00.pppg[3] <--> infiniteline <--> source_026.pppg[0];
        host_00.pppg[4] <--> infiniteline <--> source_027.pppg[0];
        host_00.pppg[5] <--> infiniteline <--> source_028.pppg[0];
        host_00.pppg[6] <--> infiniteline <--> source_029.pppg[0];
        host_00.pppg[7] <--> infiniteline <--> source_030.pppg[0];
        host_00.pppg[8] <--> infiniteline <--> source_031.pppg[0];
        host_00.pppg[9] <--> infiniteline <--> source_032.pppg[0];
        host_01.pppg[10] <--> infiniteline <--> source_021.pppg[0];
        host_01.pppg[11] <--> infiniteline <--> source_022.pppg[0];
        host_01.pppg[12] <--> infiniteline <--> source_023.pppg[0];
        host_01.pppg[1] <--> infiniteline <--> source_012.pppg[0];
        host_01.pppg[2] <--> infiniteline <--> source_013.pppg[0];
        host_01.pppg[3] <--> infiniteline <--> source_014.pppg[0];
        host_01.pppg[4] <--> infiniteline <--> source_015.pppg[0];
        host_01.pppg[5] <--> infiniteline <--> source_016.pppg[0];
        host_01.pppg[6] <--> infiniteline <--> source_017.pppg[0];
        host_01.pppg[7] <--> infiniteline <--> source_018.pppg[0];
        host_01.pppg[8] <--> infiniteline <--> source_019.pppg[0];
        host_01.pppg[9] <--> infiniteline <--> source_020.pppg[0];
        host_02.pppg[10] <--> infiniteline <--> sink_033.pppg[0];
        host_02.pppg[11] <--> infiniteline <--> sink_034.pppg[0];
        host_02.pppg[1] <--> infiniteline <--> sink_024.pppg[0];
        host_02.pppg[2] <--> infiniteline <--> sink_025.pppg[0];
        host_02.pppg[3] <--> infiniteline <--> sink_026.pppg[0];
        host_02.pppg[4] <--> infiniteline <--> sink_027.pppg[0];
        host_02.pppg[5] <--> infiniteline <--> sink_028.pppg[0];
        host_02.pppg[6] <--> infiniteline <--> sink_029.pppg[0];
        host_02.pppg[7] <--> infiniteline <--> sink_030.pppg[0];
        host_02.pppg[8] <--> infiniteline <--> sink_031.pppg[0];
        host_02.pppg[9] <--> infiniteline <--> sink_032.pppg[0];
        host_03.pppg[10] <--> infiniteline <--> sink_021.pppg[0];
        host_03.pppg[11] <--> infiniteline <--> sink_022.pppg[0];
        host_03.pppg[12] <--> infiniteline <--> sink_023.pppg[0];
        host_03.pppg[1] <--> infiniteline <--> sink_012.pppg[0];
        host_03.pppg[2] <--> infiniteline <--> sink_013.pppg[0];
        host_03.pppg[3] <--> infiniteline <--> sink_014.pppg[0];
        host_03.pppg[4] <--> infiniteline <--> sink_015.pppg[0];
        host_03.pppg[5] <--> infiniteline <--> sink_016.pppg[0];
        host_03.pppg[6] <--> infiniteline <--> sink_017.pppg[0];
        host_03.pppg[7] <--> infiniteline <--> sink_018.pppg[0];
        host_03.pppg[8] <--> infiniteline <--> sink_019.pppg[0];
        host_03.pppg[9] <--> infiniteline <--> sink_020.pppg[0];
        host_04.pppg[1] <--> infiniteline <--> source_000.pppg[0];
        host_04.pppg[2] <--> infiniteline <--> source_001.pppg[0];
        host_04.pppg[3] <--> infiniteline <--> source_002.pppg[0];
        host_04.pppg[4] <--> infiniteline <--> source_003.pppg[0];
        host_05.pppg[1] <--> infiniteline <--> sink_004.pppg[0];
        host_05.pppg[2] <--> infiniteline <--> sink_005.pppg[0];
        host_05.pppg[3] <--> infiniteline <--> sink_006.pppg[0];
        host_05.pppg[4] <--> infiniteline <--> sink_007.pppg[0];
        host_05.pppg[5] <--> infiniteline <--> sink_008.pppg[0];
        host_05.pppg[6] <--> infiniteline <--> sink_009.pppg[0];
        host_05.pppg[7] <--> infiniteline <--> sink_010.pppg[0];
        host_05.pppg[8] <--> infiniteline <--> sink_011.pppg[0];
        host_06.pppg[1] <--> infiniteline <--> source_004.pppg[0];
        host_06.pppg[2] <--> infiniteline <--> source_005.pppg[0];
        host_06.pppg[3] <--> infiniteline <--> source_006.pppg[0];
        host_06.pppg[4] <--> infiniteline <--> source_007.pppg[0];
        host_06.pppg[5] <--> infiniteline <--> source_008.pppg[0];
        host_06.pppg[6] <--> infiniteline <--> source_009.pppg[0];
        host_06.pppg[7] <--> infiniteline <--> source_010.pppg[0];
        host_06.pppg[8] <--> infiniteline <--> source_011.pppg[0];
        host_07.pppg[1] <--> infiniteline <--> sink_000.pppg[0];
        host_07.pppg[2] <--> infiniteline <--> sink_001.pppg[0];
        host_07.pppg[3] <--> infiniteline <--> sink_002.pppg[0];
        host_07.pppg[4] <--> infiniteline <--> sink_003.pppg[0];
}