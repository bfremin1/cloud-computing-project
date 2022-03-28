package inet.examples.inet.DatacenterTopologies;

import inet.networklayer.configurator.ipv4.Ipv4NetworkConfigurator;
import inet.node.inet.Router;
import inet.node.inet.StandardHost;
import ned.DatarateChannel;

network Jelly
{
    parameters:
        @display("bgb=800,500");
    types:
        channel defaultline extends DatarateChannel { delay = 0.1us; datarate = 1Gbps; per = 0; }
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
        host_00: StandardHost { parameters: @display("p=600,250;i=device/laptop;is=s"); gates: pppg[1]; }
        host_01: StandardHost { parameters: @display("p=584,326;i=device/laptop;is=s"); gates: pppg[1]; }
        host_02: StandardHost { parameters: @display("p=541,391;i=device/laptop;is=s"); gates: pppg[1]; }
        host_03: StandardHost { parameters: @display("p=476,434;i=device/server;is=s"); gates: pppg[1]; }
        host_04: StandardHost { parameters: @display("p=400,450;i=device/laptop;is=s"); gates: pppg[1]; }
        host_05: StandardHost { parameters: @display("p=323,434;i=device/laptop;is=s"); gates: pppg[1]; }
        host_06: StandardHost { parameters: @display("p=258,391;i=device/laptop;is=s"); gates: pppg[1]; }
        host_07: StandardHost { parameters: @display("p=215,326;i=device/server;is=s"); gates: pppg[1]; }
        host_08: StandardHost { parameters: @display("p=200,250;i=device/laptop;is=s"); gates: pppg[1]; }
        host_09: StandardHost { parameters: @display("p=215,173;i=device/laptop;is=s"); gates: pppg[1]; }
        host_10: StandardHost { parameters: @display("p=258,108;i=device/laptop;is=s"); gates: pppg[1]; }
        host_11: StandardHost { parameters: @display("p=323,65;i=device/server;is=s"); gates: pppg[1]; }
        host_12: StandardHost { parameters: @display("p=399,50;i=device/laptop;is=s"); gates: pppg[1]; }
        host_13: StandardHost { parameters: @display("p=476,65;i=device/laptop;is=s"); gates: pppg[1]; }
        host_14: StandardHost { parameters: @display("p=541,108;i=device/laptop;is=s"); gates: pppg[1]; }
        host_15: StandardHost { parameters: @display("p=584,173;i=device/server;is=s"); gates: pppg[1]; }
    connections:
        core_00.pppg[0] <--> defaultline <--> core_08.pppg[0];
        core_00.pppg[1] <--> defaultline <--> core_09.pppg[0];
        core_00.pppg[2] <--> defaultline <--> core_13.pppg[0];
        core_00.pppg[3] <--> defaultline <--> host_00.pppg[0];
        core_01.pppg[0] <--> defaultline <--> core_09.pppg[1];
        core_01.pppg[1] <--> defaultline <--> core_11.pppg[0];
        core_01.pppg[2] <--> defaultline <--> core_13.pppg[1];
        core_01.pppg[3] <--> defaultline <--> host_01.pppg[0];
        core_02.pppg[0] <--> defaultline <--> core_03.pppg[0];
        core_02.pppg[1] <--> defaultline <--> core_09.pppg[2];
        core_02.pppg[2] <--> defaultline <--> core_12.pppg[0];
        core_02.pppg[3] <--> defaultline <--> host_02.pppg[0];
        core_03.pppg[1] <--> defaultline <--> core_04.pppg[0];
        core_03.pppg[2] <--> defaultline <--> core_06.pppg[0];
        core_03.pppg[3] <--> defaultline <--> host_03.pppg[0];
        core_04.pppg[1] <--> defaultline <--> core_13.pppg[2];
        core_04.pppg[2] <--> defaultline <--> core_15.pppg[0];
        core_04.pppg[3] <--> defaultline <--> host_04.pppg[0];
        core_05.pppg[0] <--> defaultline <--> core_07.pppg[0];
        core_05.pppg[1] <--> defaultline <--> core_10.pppg[0];
        core_05.pppg[2] <--> defaultline <--> core_15.pppg[1];
        core_05.pppg[3] <--> defaultline <--> host_05.pppg[0];
        core_06.pppg[1] <--> defaultline <--> core_07.pppg[1];
        core_06.pppg[2] <--> defaultline <--> core_15.pppg[2];
        core_06.pppg[3] <--> defaultline <--> host_06.pppg[0];
        core_07.pppg[2] <--> defaultline <--> core_08.pppg[1];
        core_07.pppg[3] <--> defaultline <--> host_07.pppg[0];
        core_08.pppg[2] <--> defaultline <--> core_12.pppg[1];
        core_08.pppg[3] <--> defaultline <--> host_08.pppg[0];
        core_09.pppg[3] <--> defaultline <--> host_09.pppg[0];
        core_10.pppg[1] <--> defaultline <--> core_11.pppg[1];
        core_10.pppg[2] <--> defaultline <--> core_14.pppg[0];
        core_10.pppg[3] <--> defaultline <--> host_10.pppg[0];
        core_11.pppg[2] <--> defaultline <--> core_14.pppg[1];
        core_11.pppg[3] <--> defaultline <--> host_11.pppg[0];
        core_12.pppg[2] <--> defaultline <--> core_14.pppg[2];
        core_12.pppg[3] <--> defaultline <--> host_12.pppg[0];
        core_13.pppg[3] <--> defaultline <--> host_13.pppg[0];
        core_14.pppg[3] <--> defaultline <--> host_14.pppg[0];
        core_15.pppg[3] <--> defaultline <--> host_15.pppg[0];
}