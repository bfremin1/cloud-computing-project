package inet.examples.inet.DatacenterTopologies;

import inet.networklayer.configurator.ipv4.Ipv4NetworkConfigurator;
import inet.node.inet.Router;
import inet.node.inet.StandardHost;
import ned.DatarateChannel;

network FatTree
{
    parameters:
        @display("bgb=800,500");
    types:
        channel defaultline extends DatarateChannel { delay = 0.1us; datarate = 1Gbps; per = 0; }
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
}