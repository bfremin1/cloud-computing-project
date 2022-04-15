package inet.examples.inet.DatacenterTopologies;

import inet.networklayer.configurator.ipv4.Ipv4NetworkConfigurator;
import inet.node.inet.Router;
import inet.node.inet.StandardHost;
import ned.DatarateChannel;
import inet.visualizer.integrated.IntegratedVisualizer;

network Jelly
{
    parameters:
        @display("bgb=800,500");
    types:
        channel defaultline extends DatarateChannel { delay = 1us; datarate = 8Mbps; per = 0; }
        channel infiniteline extends DatarateChannel { delay = 0s; datarate = 1000Gbps; per = 0; }
    submodules:
        configurator: Ipv4NetworkConfigurator { parameters: @display("p=50,50;i=block/cogwheel;is=s"); }
        core_00: Router { parameters: @display("p=550,250;i=abstract/router;is=s"); gates: pppg[4]; }
        core_01: Router { parameters: @display("p=538,307;i=abstract/router;is=s"); gates: pppg[4]; }
        core_02: Router { parameters: @display("p=506,356;i=abstract/router;is=s"); gates: pppg[4]; }
        core_03: Router { parameters: @display("p=457,388;i=abstract/router;is=s"); gates: pppg[4]; }
        core_04: Router { parameters: @display("p=400,400;i=abstract/router;is=s"); gates: pppg[4]; }
        core_05: Router { parameters: @display("p=342,388;i=abstract/router;is=s"); gates: pppg[4]; }
        core_06: Router { parameters: @display("p=293,356;i=abstract/router;is=s"); gates: pppg[4]; }
        core_07: Router { parameters: @display("p=261,307;i=abstract/router;is=s"); gates: pppg[4]; }
        core_08: Router { parameters: @display("p=250,250;i=abstract/router;is=s"); gates: pppg[4]; }
        core_09: Router { parameters: @display("p=261,192;i=abstract/router;is=s"); gates: pppg[4]; }
        core_10: Router { parameters: @display("p=293,143;i=abstract/router;is=s"); gates: pppg[4]; }
        core_11: Router { parameters: @display("p=342,111;i=abstract/router;is=s"); gates: pppg[4]; }
        core_12: Router { parameters: @display("p=400,100;i=abstract/router;is=s"); gates: pppg[4]; }
        core_13: Router { parameters: @display("p=457,111;i=abstract/router;is=s"); gates: pppg[4]; }
        core_14: Router { parameters: @display("p=506,143;i=abstract/router;is=s"); gates: pppg[4]; }
        core_15: Router { parameters: @display("p=538,192;i=abstract/router;is=s"); gates: pppg[4]; }
        host_00: Router { parameters: @display("p=600,250;i=device/server;is=s"); gates: pppg[2]; }
        host_01: Router { parameters: @display("p=584,326;i=device/server;is=s"); gates: pppg[2]; }
        host_02: Router { parameters: @display("p=541,391;i=device/server;is=s"); gates: pppg[2]; }
        host_03: Router { parameters: @display("p=476,434;i=device/server;is=s"); gates: pppg[2]; }
        host_04: Router { parameters: @display("p=400,450;i=device/server;is=s"); gates: pppg[2]; }
        host_05: Router { parameters: @display("p=323,434;i=device/server;is=s"); gates: pppg[2]; }
        host_06: Router { parameters: @display("p=258,391;i=device/server;is=s"); gates: pppg[2]; }
        host_07: Router { parameters: @display("p=215,326;i=device/server;is=s"); gates: pppg[2]; }
        host_08: Router { parameters: @display("p=200,250;i=device/server;is=s"); gates: pppg[2]; }
        host_09: Router { parameters: @display("p=215,173;i=device/server;is=s"); gates: pppg[2]; }
        host_10: Router { parameters: @display("p=258,108;i=device/server;is=s"); gates: pppg[2]; }
        host_11: Router { parameters: @display("p=323,65;i=device/server;is=s"); gates: pppg[2]; }
        host_12: Router { parameters: @display("p=399,50;i=device/server;is=s"); gates: pppg[2]; }
        host_13: Router { parameters: @display("p=476,65;i=device/server;is=s"); gates: pppg[2]; }
        host_14: Router { parameters: @display("p=541,108;i=device/server;is=s"); gates: pppg[2]; }
        host_15: Router { parameters: @display("p=584,173;i=device/server;is=s"); gates: pppg[2]; }
        sink_0: StandardHost { parameters: @display("p=151,225;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_1: StandardHost { parameters: @display("p=179,132;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_2: StandardHost { parameters: @display("p=241,56;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_3: StandardHost { parameters: @display("p=327,10;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_4: StandardHost { parameters: @display("p=424,1;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_5: StandardHost { parameters: @display("p=517,29;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_6: StandardHost { parameters: @display("p=593,91;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_7: StandardHost { parameters: @display("p=639,177;i=block/sink;is=vs"); gates: pppg[1]; }
        source_0: StandardHost { parameters: @display("p=648,225;i=block/source;is=vs"); gates: pppg[1]; }
        source_1: StandardHost { parameters: @display("p=639,322;i=block/source;is=vs"); gates: pppg[1]; }
        source_2: StandardHost { parameters: @display("p=593,408;i=block/source;is=vs"); gates: pppg[1]; }
        source_3: StandardHost { parameters: @display("p=517,470;i=block/source;is=vs"); gates: pppg[1]; }
        source_4: StandardHost { parameters: @display("p=424,498;i=block/source;is=vs"); gates: pppg[1]; }
        source_5: StandardHost { parameters: @display("p=327,489;i=block/source;is=vs"); gates: pppg[1]; }
        source_6: StandardHost { parameters: @display("p=241,443;i=block/source;is=vs"); gates: pppg[1]; }
        source_7: StandardHost { parameters: @display("p=179,367;i=block/source;is=vs"); gates: pppg[1]; }
    connections:
        core_00.pppg[0] <--> defaultline <--> core_02.pppg[0];
        core_00.pppg[1] <--> defaultline <--> core_03.pppg[0];
        core_00.pppg[2] <--> defaultline <--> core_12.pppg[0];
        core_00.pppg[3] <--> defaultline <--> host_00.pppg[0];
        core_01.pppg[0] <--> defaultline <--> core_03.pppg[1];
        core_01.pppg[1] <--> defaultline <--> core_13.pppg[0];
        core_01.pppg[2] <--> defaultline <--> core_15.pppg[0];
        core_01.pppg[3] <--> defaultline <--> host_01.pppg[0];
        core_02.pppg[1] <--> defaultline <--> core_04.pppg[0];
        core_02.pppg[2] <--> defaultline <--> core_11.pppg[0];
        core_02.pppg[3] <--> defaultline <--> host_02.pppg[0];
        core_03.pppg[2] <--> defaultline <--> core_05.pppg[0];
        core_03.pppg[3] <--> defaultline <--> host_03.pppg[0];
        core_04.pppg[1] <--> defaultline <--> core_05.pppg[1];
        core_04.pppg[2] <--> defaultline <--> core_11.pppg[1];
        core_04.pppg[3] <--> defaultline <--> host_04.pppg[0];
        core_05.pppg[2] <--> defaultline <--> core_06.pppg[0];
        core_05.pppg[3] <--> defaultline <--> host_05.pppg[0];
        core_06.pppg[1] <--> defaultline <--> core_12.pppg[1];
        core_06.pppg[2] <--> defaultline <--> core_14.pppg[0];
        core_06.pppg[3] <--> defaultline <--> host_06.pppg[0];
        core_07.pppg[0] <--> defaultline <--> core_08.pppg[0];
        core_07.pppg[1] <--> defaultline <--> core_11.pppg[2];
        core_07.pppg[2] <--> defaultline <--> core_14.pppg[1];
        core_07.pppg[3] <--> defaultline <--> host_07.pppg[0];
        core_08.pppg[1] <--> defaultline <--> core_10.pppg[0];
        core_08.pppg[2] <--> defaultline <--> core_15.pppg[1];
        core_08.pppg[3] <--> defaultline <--> host_08.pppg[0];
        core_09.pppg[0] <--> defaultline <--> core_10.pppg[1];
        core_09.pppg[1] <--> defaultline <--> core_13.pppg[1];
        core_09.pppg[2] <--> defaultline <--> core_14.pppg[2];
        core_09.pppg[3] <--> defaultline <--> host_09.pppg[0];
        core_10.pppg[2] <--> defaultline <--> core_15.pppg[2];
        core_10.pppg[3] <--> defaultline <--> host_10.pppg[0];
        core_11.pppg[3] <--> defaultline <--> host_11.pppg[0];
        core_12.pppg[2] <--> defaultline <--> core_13.pppg[2];
        core_12.pppg[3] <--> defaultline <--> host_12.pppg[0];
        core_13.pppg[3] <--> defaultline <--> host_13.pppg[0];
        core_14.pppg[3] <--> defaultline <--> host_14.pppg[0];
        core_15.pppg[3] <--> defaultline <--> host_15.pppg[0];
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