package inet.examples.inet.DatacenterTopologies;

import inet.networklayer.configurator.ipv4.Ipv4NetworkConfigurator;
import inet.node.inet.Router;
import inet.node.inet.StandardHost;
import ned.DatarateChannel;

network VL2
{
    parameters:
        @display("bgb=800,500");
    types:
        channel defaultline extends DatarateChannel { delay = 0.1us; datarate = 1Gbps; per = 0; }
    submodules:
        agg_00: Router { parameters: @display("p=100,200;i=abstract/router;is=s"); gates: pppg[4]; }
        agg_01: Router { parameters: @display("p=300,200;i=abstract/router;is=s"); gates: pppg[4]; }
        agg_02: Router { parameters: @display("p=500,200;i=abstract/router;is=s"); gates: pppg[4]; }
        agg_03: Router { parameters: @display("p=700,200;i=abstract/router;is=s"); gates: pppg[4]; }
        configurator: Ipv4NetworkConfigurator { parameters: @display("p=50,50;i=block/cogwheel;is=s"); }
        core_00: Router { parameters: @display("p=200,100;i=abstract/router;is=s"); gates: pppg[4]; }
        core_01: Router { parameters: @display("p=600,100;i=abstract/router;is=s"); gates: pppg[4]; }
        host_00: StandardHost { parameters: @display("p=25,400;i=device/laptop;is=s"); gates: pppg[1]; }
        host_01: StandardHost { parameters: @display("p=75,400;i=device/laptop;is=s"); gates: pppg[1]; }
        host_02: StandardHost { parameters: @display("p=125,400;i=device/laptop;is=s"); gates: pppg[1]; }
        host_03: StandardHost { parameters: @display("p=175,400;i=device/server;is=s"); gates: pppg[1]; }
        host_04: StandardHost { parameters: @display("p=225,400;i=device/laptop;is=s"); gates: pppg[1]; }
        host_05: StandardHost { parameters: @display("p=275,400;i=device/laptop;is=s"); gates: pppg[1]; }
        host_06: StandardHost { parameters: @display("p=325,400;i=device/laptop;is=s"); gates: pppg[1]; }
        host_07: StandardHost { parameters: @display("p=375,400;i=device/server;is=s"); gates: pppg[1]; }
        host_08: StandardHost { parameters: @display("p=425,400;i=device/laptop;is=s"); gates: pppg[1]; }
        host_09: StandardHost { parameters: @display("p=475,400;i=device/laptop;is=s"); gates: pppg[1]; }
        host_10: StandardHost { parameters: @display("p=525,400;i=device/laptop;is=s"); gates: pppg[1]; }
        host_11: StandardHost { parameters: @display("p=575,400;i=device/server;is=s"); gates: pppg[1]; }
        host_12: StandardHost { parameters: @display("p=625,400;i=device/laptop;is=s"); gates: pppg[1]; }
        host_13: StandardHost { parameters: @display("p=675,400;i=device/laptop;is=s"); gates: pppg[1]; }
        host_14: StandardHost { parameters: @display("p=725,400;i=device/laptop;is=s"); gates: pppg[1]; }
        host_15: StandardHost { parameters: @display("p=775,400;i=device/server;is=s"); gates: pppg[1]; }
        tor_00: Router { parameters: @display("p=100,300;i=abstract/router;is=s"); gates: pppg[6]; }
        tor_01: Router { parameters: @display("p=300,300;i=abstract/router;is=s"); gates: pppg[6]; }
        tor_02: Router { parameters: @display("p=500,300;i=abstract/router;is=s"); gates: pppg[6]; }
        tor_03: Router { parameters: @display("p=700,300;i=abstract/router;is=s"); gates: pppg[6]; }
    connections:
        agg_00.pppg[0] <--> defaultline <--> core_00.pppg[0];
        agg_00.pppg[1] <--> defaultline <--> core_01.pppg[0];
        agg_00.pppg[2] <--> defaultline <--> tor_00.pppg[0];
        agg_00.pppg[3] <--> defaultline <--> tor_01.pppg[0];
        agg_01.pppg[0] <--> defaultline <--> core_00.pppg[1];
        agg_01.pppg[1] <--> defaultline <--> core_01.pppg[1];
        agg_01.pppg[2] <--> defaultline <--> tor_00.pppg[1];
        agg_01.pppg[3] <--> defaultline <--> tor_01.pppg[1];
        agg_02.pppg[0] <--> defaultline <--> core_00.pppg[2];
        agg_02.pppg[1] <--> defaultline <--> core_01.pppg[2];
        agg_02.pppg[2] <--> defaultline <--> tor_02.pppg[0];
        agg_02.pppg[3] <--> defaultline <--> tor_03.pppg[0];
        agg_03.pppg[0] <--> defaultline <--> core_00.pppg[3];
        agg_03.pppg[1] <--> defaultline <--> core_01.pppg[3];
        agg_03.pppg[2] <--> defaultline <--> tor_02.pppg[1];
        agg_03.pppg[3] <--> defaultline <--> tor_03.pppg[1];
        host_00.pppg[0] <--> defaultline <--> tor_00.pppg[2];
        host_01.pppg[0] <--> defaultline <--> tor_00.pppg[3];
        host_02.pppg[0] <--> defaultline <--> tor_00.pppg[4];
        host_03.pppg[0] <--> defaultline <--> tor_00.pppg[5];
        host_04.pppg[0] <--> defaultline <--> tor_01.pppg[2];
        host_05.pppg[0] <--> defaultline <--> tor_01.pppg[3];
        host_06.pppg[0] <--> defaultline <--> tor_01.pppg[4];
        host_07.pppg[0] <--> defaultline <--> tor_01.pppg[5];
        host_08.pppg[0] <--> defaultline <--> tor_02.pppg[2];
        host_09.pppg[0] <--> defaultline <--> tor_02.pppg[3];
        host_10.pppg[0] <--> defaultline <--> tor_02.pppg[4];
        host_11.pppg[0] <--> defaultline <--> tor_02.pppg[5];
        host_12.pppg[0] <--> defaultline <--> tor_03.pppg[2];
        host_13.pppg[0] <--> defaultline <--> tor_03.pppg[3];
        host_14.pppg[0] <--> defaultline <--> tor_03.pppg[4];
        host_15.pppg[0] <--> defaultline <--> tor_03.pppg[5];
}