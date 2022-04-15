package inet.examples.inet.DatacenterTopologies;

import inet.networklayer.configurator.ipv4.Ipv4NetworkConfigurator;
import inet.node.inet.Router;
import inet.node.inet.StandardHost;
import ned.DatarateChannel;
import inet.visualizer.integrated.IntegratedVisualizer;

network FatTree
{
    parameters:
        @display("bgb=1200,500");
    types:
        channel defaultline extends DatarateChannel { delay = 1us; datarate = 8Mbps; per = 0; }
        channel infiniteline extends DatarateChannel { delay = 0s; datarate = 1000Gbps; per = 0; }
    submodules:
        agg_00: Router { parameters: @display("p=75,200;i=abstract/router;is=s"); gates: pppg[4]; }
        agg_01: Router { parameters: @display("p=225,200;i=abstract/router;is=s"); gates: pppg[4]; }
        agg_02: Router { parameters: @display("p=375,200;i=abstract/router;is=s"); gates: pppg[4]; }
        agg_03: Router { parameters: @display("p=525,200;i=abstract/router;is=s"); gates: pppg[4]; }
        agg_04: Router { parameters: @display("p=675,200;i=abstract/router;is=s"); gates: pppg[4]; }
        agg_05: Router { parameters: @display("p=825,200;i=abstract/router;is=s"); gates: pppg[4]; }
        agg_06: Router { parameters: @display("p=975,200;i=abstract/router;is=s"); gates: pppg[4]; }
        agg_07: Router { parameters: @display("p=1125,200;i=abstract/router;is=s"); gates: pppg[4]; }
        configurator: Ipv4NetworkConfigurator { parameters: @display("p=50,50;i=block/cogwheel;is=s"); }
        core_00: Router { parameters: @display("p=150,100;i=abstract/router;is=s"); gates: pppg[4]; }
        core_01: Router { parameters: @display("p=450,100;i=abstract/router;is=s"); gates: pppg[4]; }
        core_02: Router { parameters: @display("p=750,100;i=abstract/router;is=s"); gates: pppg[4]; }
        core_03: Router { parameters: @display("p=1050,100;i=abstract/router;is=s"); gates: pppg[4]; }
        edge_00: Router { parameters: @display("p=75,300;i=abstract/router;is=s"); gates: pppg[4]; }
        edge_01: Router { parameters: @display("p=225,300;i=abstract/router;is=s"); gates: pppg[4]; }
        edge_02: Router { parameters: @display("p=375,300;i=abstract/router;is=s"); gates: pppg[4]; }
        edge_03: Router { parameters: @display("p=525,300;i=abstract/router;is=s"); gates: pppg[4]; }
        edge_04: Router { parameters: @display("p=675,300;i=abstract/router;is=s"); gates: pppg[4]; }
        edge_05: Router { parameters: @display("p=825,300;i=abstract/router;is=s"); gates: pppg[4]; }
        edge_06: Router { parameters: @display("p=975,300;i=abstract/router;is=s"); gates: pppg[4]; }
        edge_07: Router { parameters: @display("p=1125,300;i=abstract/router;is=s"); gates: pppg[4]; }
        host_00: Router { parameters: @display("p=37,400;i=device/server;is=s"); gates: pppg[2]; }
        host_01: Router { parameters: @display("p=112,400;i=device/server;is=s"); gates: pppg[2]; }
        host_02: Router { parameters: @display("p=187,400;i=device/server;is=s"); gates: pppg[2]; }
        host_03: Router { parameters: @display("p=262,400;i=device/server;is=s"); gates: pppg[2]; }
        host_04: Router { parameters: @display("p=337,400;i=device/server;is=s"); gates: pppg[2]; }
        host_05: Router { parameters: @display("p=412,400;i=device/server;is=s"); gates: pppg[2]; }
        host_06: Router { parameters: @display("p=487,400;i=device/server;is=s"); gates: pppg[2]; }
        host_07: Router { parameters: @display("p=562,400;i=device/server;is=s"); gates: pppg[2]; }
        host_08: Router { parameters: @display("p=637,400;i=device/server;is=s"); gates: pppg[2]; }
        host_09: Router { parameters: @display("p=712,400;i=device/server;is=s"); gates: pppg[2]; }
        host_10: Router { parameters: @display("p=787,400;i=device/server;is=s"); gates: pppg[2]; }
        host_11: Router { parameters: @display("p=862,400;i=device/server;is=s"); gates: pppg[2]; }
        host_12: Router { parameters: @display("p=937,400;i=device/server;is=s"); gates: pppg[2]; }
        host_13: Router { parameters: @display("p=1012,400;i=device/server;is=s"); gates: pppg[2]; }
        host_14: Router { parameters: @display("p=1087,400;i=device/server;is=s"); gates: pppg[2]; }
        host_15: Router { parameters: @display("p=1162,400;i=device/server;is=s"); gates: pppg[2]; }
        sink_0: StandardHost { parameters: @display("p=1187,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_1: StandardHost { parameters: @display("p=1037,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_2: StandardHost { parameters: @display("p=887,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_3: StandardHost { parameters: @display("p=962,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_4: StandardHost { parameters: @display("p=1112,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_5: StandardHost { parameters: @display("p=812,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_6: StandardHost { parameters: @display("p=512,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_7: StandardHost { parameters: @display("p=737,450;i=block/sink;is=vs"); gates: pppg[1]; }
        source_0: StandardHost { parameters: @display("p=312,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_1: StandardHost { parameters: @display("p=162,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_2: StandardHost { parameters: @display("p=87,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_3: StandardHost { parameters: @display("p=537,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_4: StandardHost { parameters: @display("p=387,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_5: StandardHost { parameters: @display("p=12,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_6: StandardHost { parameters: @display("p=612,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_7: StandardHost { parameters: @display("p=237,450;i=block/source;is=vs"); gates: pppg[1]; }
    connections:
        agg_00.pppg[0] <--> defaultline <--> core_00.pppg[0];
        agg_00.pppg[1] <--> defaultline <--> core_01.pppg[0];
        agg_00.pppg[2] <--> defaultline <--> edge_00.pppg[0];
        agg_00.pppg[3] <--> defaultline <--> edge_01.pppg[0];
        agg_01.pppg[0] <--> defaultline <--> core_02.pppg[0];
        agg_01.pppg[1] <--> defaultline <--> core_03.pppg[0];
        agg_01.pppg[2] <--> defaultline <--> edge_00.pppg[1];
        agg_01.pppg[3] <--> defaultline <--> edge_01.pppg[1];
        agg_02.pppg[0] <--> defaultline <--> core_00.pppg[1];
        agg_02.pppg[1] <--> defaultline <--> core_01.pppg[1];
        agg_02.pppg[2] <--> defaultline <--> edge_02.pppg[0];
        agg_02.pppg[3] <--> defaultline <--> edge_03.pppg[0];
        agg_03.pppg[0] <--> defaultline <--> core_02.pppg[1];
        agg_03.pppg[1] <--> defaultline <--> core_03.pppg[1];
        agg_03.pppg[2] <--> defaultline <--> edge_02.pppg[1];
        agg_03.pppg[3] <--> defaultline <--> edge_03.pppg[1];
        agg_04.pppg[0] <--> defaultline <--> core_00.pppg[2];
        agg_04.pppg[1] <--> defaultline <--> core_01.pppg[2];
        agg_04.pppg[2] <--> defaultline <--> edge_04.pppg[0];
        agg_04.pppg[3] <--> defaultline <--> edge_05.pppg[0];
        agg_05.pppg[0] <--> defaultline <--> core_02.pppg[2];
        agg_05.pppg[1] <--> defaultline <--> core_03.pppg[2];
        agg_05.pppg[2] <--> defaultline <--> edge_04.pppg[1];
        agg_05.pppg[3] <--> defaultline <--> edge_05.pppg[1];
        agg_06.pppg[0] <--> defaultline <--> core_00.pppg[3];
        agg_06.pppg[1] <--> defaultline <--> core_01.pppg[3];
        agg_06.pppg[2] <--> defaultline <--> edge_06.pppg[0];
        agg_06.pppg[3] <--> defaultline <--> edge_07.pppg[0];
        agg_07.pppg[0] <--> defaultline <--> core_02.pppg[3];
        agg_07.pppg[1] <--> defaultline <--> core_03.pppg[3];
        agg_07.pppg[2] <--> defaultline <--> edge_06.pppg[1];
        agg_07.pppg[3] <--> defaultline <--> edge_07.pppg[1];
        edge_00.pppg[2] <--> defaultline <--> host_00.pppg[0];
        edge_00.pppg[3] <--> defaultline <--> host_01.pppg[0];
        edge_01.pppg[2] <--> defaultline <--> host_02.pppg[0];
        edge_01.pppg[3] <--> defaultline <--> host_03.pppg[0];
        edge_02.pppg[2] <--> defaultline <--> host_04.pppg[0];
        edge_02.pppg[3] <--> defaultline <--> host_05.pppg[0];
        edge_03.pppg[2] <--> defaultline <--> host_06.pppg[0];
        edge_03.pppg[3] <--> defaultline <--> host_07.pppg[0];
        edge_04.pppg[2] <--> defaultline <--> host_08.pppg[0];
        edge_04.pppg[3] <--> defaultline <--> host_09.pppg[0];
        edge_05.pppg[2] <--> defaultline <--> host_10.pppg[0];
        edge_05.pppg[3] <--> defaultline <--> host_11.pppg[0];
        edge_06.pppg[2] <--> defaultline <--> host_12.pppg[0];
        edge_06.pppg[3] <--> defaultline <--> host_13.pppg[0];
        edge_07.pppg[2] <--> defaultline <--> host_14.pppg[0];
        edge_07.pppg[3] <--> defaultline <--> host_15.pppg[0];
        host_00.pppg[1] <--> infiniteline <--> source_5.pppg[0];
        host_01.pppg[1] <--> infiniteline <--> source_2.pppg[0];
        host_02.pppg[1] <--> infiniteline <--> source_1.pppg[0];
        host_03.pppg[1] <--> infiniteline <--> source_7.pppg[0];
        host_04.pppg[1] <--> infiniteline <--> source_0.pppg[0];
        host_05.pppg[1] <--> infiniteline <--> source_4.pppg[0];
        host_06.pppg[1] <--> infiniteline <--> sink_6.pppg[0];
        host_07.pppg[1] <--> infiniteline <--> source_3.pppg[0];
        host_08.pppg[1] <--> infiniteline <--> source_6.pppg[0];
        host_09.pppg[1] <--> infiniteline <--> sink_7.pppg[0];
        host_10.pppg[1] <--> infiniteline <--> sink_5.pppg[0];
        host_11.pppg[1] <--> infiniteline <--> sink_2.pppg[0];
        host_12.pppg[1] <--> infiniteline <--> sink_3.pppg[0];
        host_13.pppg[1] <--> infiniteline <--> sink_1.pppg[0];
        host_14.pppg[1] <--> infiniteline <--> sink_4.pppg[0];
        host_15.pppg[1] <--> infiniteline <--> sink_0.pppg[0];
}