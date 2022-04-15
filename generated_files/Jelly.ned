package inet.examples.inet.DatacenterTopologies;

import inet.networklayer.configurator.ipv4.Ipv4NetworkConfigurator;
import inet.node.inet.Router;
import inet.node.inet.StandardHost;
import ned.DatarateChannel;
import inet.visualizer.integrated.IntegratedVisualizer;

network Jelly
{
    parameters:
        @display("bgb=1200,500");
    types:
        channel defaultline extends DatarateChannel { delay = 1us; datarate = 8Mbps; per = 0; }
        channel infiniteline extends DatarateChannel { delay = 0s; datarate = 1000Gbps; per = 0; }
    submodules:
        configurator: Ipv4NetworkConfigurator { parameters: @display("p=50,50;i=block/cogwheel;is=s"); }
        core_00: Router { parameters: @display("p=750,250;i=abstract/router;is=s"); gates: pppg[4]; }
        core_01: Router { parameters: @display("p=738,307;i=abstract/router;is=s"); gates: pppg[4]; }
        core_02: Router { parameters: @display("p=706,356;i=abstract/router;is=s"); gates: pppg[4]; }
        core_03: Router { parameters: @display("p=657,388;i=abstract/router;is=s"); gates: pppg[4]; }
        core_04: Router { parameters: @display("p=600,400;i=abstract/router;is=s"); gates: pppg[4]; }
        core_05: Router { parameters: @display("p=542,388;i=abstract/router;is=s"); gates: pppg[4]; }
        core_06: Router { parameters: @display("p=493,356;i=abstract/router;is=s"); gates: pppg[4]; }
        core_07: Router { parameters: @display("p=461,307;i=abstract/router;is=s"); gates: pppg[4]; }
        core_08: Router { parameters: @display("p=450,250;i=abstract/router;is=s"); gates: pppg[4]; }
        core_09: Router { parameters: @display("p=461,192;i=abstract/router;is=s"); gates: pppg[4]; }
        core_10: Router { parameters: @display("p=493,143;i=abstract/router;is=s"); gates: pppg[4]; }
        core_11: Router { parameters: @display("p=542,111;i=abstract/router;is=s"); gates: pppg[4]; }
        core_12: Router { parameters: @display("p=600,100;i=abstract/router;is=s"); gates: pppg[4]; }
        core_13: Router { parameters: @display("p=657,111;i=abstract/router;is=s"); gates: pppg[4]; }
        core_14: Router { parameters: @display("p=706,143;i=abstract/router;is=s"); gates: pppg[4]; }
        core_15: Router { parameters: @display("p=738,192;i=abstract/router;is=s"); gates: pppg[4]; }
        host_00: Router { parameters: @display("p=800,250;i=device/server;is=s"); gates: pppg[2]; }
        host_01: Router { parameters: @display("p=784,326;i=device/server;is=s"); gates: pppg[2]; }
        host_02: Router { parameters: @display("p=741,391;i=device/server;is=s"); gates: pppg[2]; }
        host_03: Router { parameters: @display("p=676,434;i=device/server;is=s"); gates: pppg[2]; }
        host_04: Router { parameters: @display("p=600,450;i=device/server;is=s"); gates: pppg[2]; }
        host_05: Router { parameters: @display("p=523,434;i=device/server;is=s"); gates: pppg[2]; }
        host_06: Router { parameters: @display("p=458,391;i=device/server;is=s"); gates: pppg[2]; }
        host_07: Router { parameters: @display("p=415,326;i=device/server;is=s"); gates: pppg[2]; }
        host_08: Router { parameters: @display("p=400,250;i=device/server;is=s"); gates: pppg[2]; }
        host_09: Router { parameters: @display("p=415,173;i=device/server;is=s"); gates: pppg[2]; }
        host_10: Router { parameters: @display("p=458,108;i=device/server;is=s"); gates: pppg[2]; }
        host_11: Router { parameters: @display("p=523,65;i=device/server;is=s"); gates: pppg[2]; }
        host_12: Router { parameters: @display("p=600,50;i=device/server;is=s"); gates: pppg[2]; }
        host_13: Router { parameters: @display("p=676,65;i=device/server;is=s"); gates: pppg[2]; }
        host_14: Router { parameters: @display("p=741,108;i=device/server;is=s"); gates: pppg[2]; }
        host_15: Router { parameters: @display("p=784,173;i=device/server;is=s"); gates: pppg[2]; }
        sink_0: StandardHost { parameters: @display("p=820,367;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_1: StandardHost { parameters: @display("p=717,29;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_2: StandardHost { parameters: @display("p=406,408;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_3: StandardHost { parameters: @display("p=575,498;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_4: StandardHost { parameters: @display("p=758,443;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_5: StandardHost { parameters: @display("p=624,1;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_6: StandardHost { parameters: @display("p=379,132;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_7: StandardHost { parameters: @display("p=482,470;i=block/sink;is=vs"); gates: pppg[1]; }
        source_0: StandardHost { parameters: @display("p=758,56;i=block/source;is=vs"); gates: pppg[1]; }
        source_1: StandardHost { parameters: @display("p=406,91;i=block/source;is=vs"); gates: pppg[1]; }
        source_2: StandardHost { parameters: @display("p=379,367;i=block/source;is=vs"); gates: pppg[1]; }
        source_3: StandardHost { parameters: @display("p=820,132;i=block/source;is=vs"); gates: pppg[1]; }
        source_4: StandardHost { parameters: @display("p=351,274;i=block/source;is=vs"); gates: pppg[1]; }
        source_5: StandardHost { parameters: @display("p=717,470;i=block/source;is=vs"); gates: pppg[1]; }
        source_6: StandardHost { parameters: @display("p=848,225;i=block/source;is=vs"); gates: pppg[1]; }
        source_7: StandardHost { parameters: @display("p=482,29;i=block/source;is=vs"); gates: pppg[1]; }
    connections:
        core_00.pppg[0] <--> defaultline <--> core_01.pppg[0];
        core_00.pppg[1] <--> defaultline <--> core_10.pppg[0];
        core_00.pppg[2] <--> defaultline <--> core_11.pppg[0];
        core_00.pppg[3] <--> defaultline <--> host_00.pppg[0];
        core_01.pppg[1] <--> defaultline <--> core_06.pppg[0];
        core_01.pppg[2] <--> defaultline <--> core_07.pppg[0];
        core_01.pppg[3] <--> defaultline <--> host_01.pppg[0];
        core_02.pppg[0] <--> defaultline <--> core_04.pppg[0];
        core_02.pppg[1] <--> defaultline <--> core_08.pppg[0];
        core_02.pppg[2] <--> defaultline <--> core_12.pppg[0];
        core_02.pppg[3] <--> defaultline <--> host_02.pppg[0];
        core_03.pppg[0] <--> defaultline <--> core_09.pppg[0];
        core_03.pppg[1] <--> defaultline <--> core_12.pppg[1];
        core_03.pppg[2] <--> defaultline <--> core_13.pppg[0];
        core_03.pppg[3] <--> defaultline <--> host_03.pppg[0];
        core_04.pppg[1] <--> defaultline <--> core_10.pppg[1];
        core_04.pppg[2] <--> defaultline <--> core_11.pppg[1];
        core_04.pppg[3] <--> defaultline <--> host_04.pppg[0];
        core_05.pppg[0] <--> defaultline <--> core_06.pppg[1];
        core_05.pppg[1] <--> defaultline <--> core_09.pppg[1];
        core_05.pppg[2] <--> defaultline <--> core_13.pppg[1];
        core_05.pppg[3] <--> defaultline <--> host_05.pppg[0];
        core_06.pppg[2] <--> defaultline <--> core_14.pppg[0];
        core_06.pppg[3] <--> defaultline <--> host_06.pppg[0];
        core_07.pppg[1] <--> defaultline <--> core_08.pppg[1];
        core_07.pppg[2] <--> defaultline <--> core_12.pppg[2];
        core_07.pppg[3] <--> defaultline <--> host_07.pppg[0];
        core_08.pppg[2] <--> defaultline <--> core_15.pppg[0];
        core_08.pppg[3] <--> defaultline <--> host_08.pppg[0];
        core_09.pppg[2] <--> defaultline <--> core_14.pppg[1];
        core_09.pppg[3] <--> defaultline <--> host_09.pppg[0];
        core_10.pppg[2] <--> defaultline <--> core_14.pppg[2];
        core_10.pppg[3] <--> defaultline <--> host_10.pppg[0];
        core_11.pppg[2] <--> defaultline <--> core_15.pppg[1];
        core_11.pppg[3] <--> defaultline <--> host_11.pppg[0];
        core_12.pppg[3] <--> defaultline <--> host_12.pppg[0];
        core_13.pppg[2] <--> defaultline <--> core_15.pppg[2];
        core_13.pppg[3] <--> defaultline <--> host_13.pppg[0];
        core_14.pppg[3] <--> defaultline <--> host_14.pppg[0];
        core_15.pppg[3] <--> defaultline <--> host_15.pppg[0];
        host_00.pppg[1] <--> infiniteline <--> source_6.pppg[0];
        host_01.pppg[1] <--> infiniteline <--> sink_0.pppg[0];
        host_02.pppg[1] <--> infiniteline <--> sink_4.pppg[0];
        host_03.pppg[1] <--> infiniteline <--> source_5.pppg[0];
        host_04.pppg[1] <--> infiniteline <--> sink_3.pppg[0];
        host_05.pppg[1] <--> infiniteline <--> sink_7.pppg[0];
        host_06.pppg[1] <--> infiniteline <--> sink_2.pppg[0];
        host_07.pppg[1] <--> infiniteline <--> source_2.pppg[0];
        host_08.pppg[1] <--> infiniteline <--> source_4.pppg[0];
        host_09.pppg[1] <--> infiniteline <--> sink_6.pppg[0];
        host_10.pppg[1] <--> infiniteline <--> source_1.pppg[0];
        host_11.pppg[1] <--> infiniteline <--> source_7.pppg[0];
        host_12.pppg[1] <--> infiniteline <--> sink_5.pppg[0];
        host_13.pppg[1] <--> infiniteline <--> sink_1.pppg[0];
        host_14.pppg[1] <--> infiniteline <--> source_0.pppg[0];
        host_15.pppg[1] <--> infiniteline <--> source_3.pppg[0];
}