package inet.examples.inet.DatacenterTopologies;

import inet.networklayer.configurator.ipv4.Ipv4NetworkConfigurator;
import inet.node.inet.Router;
import inet.node.inet.StandardHost;
import ned.DatarateChannel;
import inet.visualizer.integrated.IntegratedVisualizer;

network FatTree
{
    parameters:
        @display("bgb=800,500");
    types:
        channel defaultline extends DatarateChannel { delay = 1us; datarate = 8Mbps; per = 0; }
        channel infiniteline extends DatarateChannel { delay = 0s; datarate = 1000Gbps; per = 0; }
    submodules:
        agg_00: Router { parameters: @display("p=50,200;i=abstract/router;is=s"); gates: pppg[4]; }
        agg_01: Router { parameters: @display("p=150,200;i=abstract/router;is=s"); gates: pppg[4]; }
        agg_02: Router { parameters: @display("p=250,200;i=abstract/router;is=s"); gates: pppg[4]; }
        agg_03: Router { parameters: @display("p=350,200;i=abstract/router;is=s"); gates: pppg[4]; }
        agg_04: Router { parameters: @display("p=450,200;i=abstract/router;is=s"); gates: pppg[4]; }
        agg_05: Router { parameters: @display("p=550,200;i=abstract/router;is=s"); gates: pppg[4]; }
        agg_06: Router { parameters: @display("p=650,200;i=abstract/router;is=s"); gates: pppg[4]; }
        agg_07: Router { parameters: @display("p=750,200;i=abstract/router;is=s"); gates: pppg[4]; }
        configurator: Ipv4NetworkConfigurator { parameters: @display("p=50,50;i=block/cogwheel;is=s"); }
        core_00: Router { parameters: @display("p=100,100;i=abstract/router;is=s"); gates: pppg[4]; }
        core_01: Router { parameters: @display("p=300,100;i=abstract/router;is=s"); gates: pppg[4]; }
        core_02: Router { parameters: @display("p=500,100;i=abstract/router;is=s"); gates: pppg[4]; }
        core_03: Router { parameters: @display("p=700,100;i=abstract/router;is=s"); gates: pppg[4]; }
        edge_00: Router { parameters: @display("p=50,300;i=abstract/router;is=s"); gates: pppg[4]; }
        edge_01: Router { parameters: @display("p=150,300;i=abstract/router;is=s"); gates: pppg[4]; }
        edge_02: Router { parameters: @display("p=250,300;i=abstract/router;is=s"); gates: pppg[4]; }
        edge_03: Router { parameters: @display("p=350,300;i=abstract/router;is=s"); gates: pppg[4]; }
        edge_04: Router { parameters: @display("p=450,300;i=abstract/router;is=s"); gates: pppg[4]; }
        edge_05: Router { parameters: @display("p=550,300;i=abstract/router;is=s"); gates: pppg[4]; }
        edge_06: Router { parameters: @display("p=650,300;i=abstract/router;is=s"); gates: pppg[4]; }
        edge_07: Router { parameters: @display("p=750,300;i=abstract/router;is=s"); gates: pppg[4]; }
        host_00: Router { parameters: @display("p=25,400;i=device/server;is=s"); gates: pppg[2]; }
        host_01: Router { parameters: @display("p=75,400;i=device/server;is=s"); gates: pppg[2]; }
        host_02: Router { parameters: @display("p=125,400;i=device/server;is=s"); gates: pppg[2]; }
        host_03: Router { parameters: @display("p=175,400;i=device/server;is=s"); gates: pppg[2]; }
        host_04: Router { parameters: @display("p=225,400;i=device/server;is=s"); gates: pppg[2]; }
        host_05: Router { parameters: @display("p=275,400;i=device/server;is=s"); gates: pppg[2]; }
        host_06: Router { parameters: @display("p=325,400;i=device/server;is=s"); gates: pppg[2]; }
        host_07: Router { parameters: @display("p=375,400;i=device/server;is=s"); gates: pppg[2]; }
        host_08: Router { parameters: @display("p=425,400;i=device/server;is=s"); gates: pppg[2]; }
        host_09: Router { parameters: @display("p=475,400;i=device/server;is=s"); gates: pppg[2]; }
        host_10: Router { parameters: @display("p=525,400;i=device/server;is=s"); gates: pppg[2]; }
        host_11: Router { parameters: @display("p=575,400;i=device/server;is=s"); gates: pppg[2]; }
        host_12: Router { parameters: @display("p=625,400;i=device/server;is=s"); gates: pppg[2]; }
        host_13: Router { parameters: @display("p=675,400;i=device/server;is=s"); gates: pppg[2]; }
        host_14: Router { parameters: @display("p=725,400;i=device/server;is=s"); gates: pppg[2]; }
        host_15: Router { parameters: @display("p=775,400;i=device/server;is=s"); gates: pppg[2]; }
        sink_0: StandardHost { parameters: @display("p=450,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_1: StandardHost { parameters: @display("p=500,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_2: StandardHost { parameters: @display("p=550,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_3: StandardHost { parameters: @display("p=600,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_4: StandardHost { parameters: @display("p=650,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_5: StandardHost { parameters: @display("p=700,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_6: StandardHost { parameters: @display("p=750,450;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_7: StandardHost { parameters: @display("p=800,450;i=block/sink;is=vs"); gates: pppg[1]; }
        source_0: StandardHost { parameters: @display("p=0,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_1: StandardHost { parameters: @display("p=50,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_2: StandardHost { parameters: @display("p=100,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_3: StandardHost { parameters: @display("p=150,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_4: StandardHost { parameters: @display("p=200,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_5: StandardHost { parameters: @display("p=250,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_6: StandardHost { parameters: @display("p=300,450;i=block/source;is=vs"); gates: pppg[1]; }
        source_7: StandardHost { parameters: @display("p=350,450;i=block/source;is=vs"); gates: pppg[1]; }
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
        host_00.pppg[1] <--> infiniteline <--> source_0.pppg[0];
        host_01.pppg[1] <--> infiniteline <--> source_1.pppg[0];
        host_02.pppg[1] <--> infiniteline <--> source_2.pppg[0];
        host_03.pppg[1] <--> infiniteline <--> source_3.pppg[0];
        host_04.pppg[1] <--> infiniteline <--> source_4.pppg[0];
        host_05.pppg[1] <--> infiniteline <--> source_5.pppg[0];
        host_06.pppg[1] <--> infiniteline <--> source_6.pppg[0];
        host_07.pppg[1] <--> infiniteline <--> source_7.pppg[0];
        host_08.pppg[1] <--> infiniteline <--> sink_0.pppg[0];
        host_09.pppg[1] <--> infiniteline <--> sink_1.pppg[0];
        host_10.pppg[1] <--> infiniteline <--> sink_2.pppg[0];
        host_11.pppg[1] <--> infiniteline <--> sink_3.pppg[0];
        host_12.pppg[1] <--> infiniteline <--> sink_4.pppg[0];
        host_13.pppg[1] <--> infiniteline <--> sink_5.pppg[0];
        host_14.pppg[1] <--> infiniteline <--> sink_6.pppg[0];
        host_15.pppg[1] <--> infiniteline <--> sink_7.pppg[0];
}