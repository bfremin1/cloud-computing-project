package inet.examples.inet.DatacenterTopologies;

import inet.networklayer.configurator.ipv4.Ipv4NetworkConfigurator;
import inet.node.inet.Router;
import inet.node.inet.StandardHost;
import ned.DatarateChannel;
import inet.visualizer.integrated.IntegratedVisualizer;

network Default
{
    parameters:
        @display("bgb=800,500");
    types:
        channel defaultline extends DatarateChannel { delay = 1us; datarate = 8Mbps; per = 0; }
        channel infiniteline extends DatarateChannel { delay = 0s; datarate = 1000Gbps; per = 0; }
    submodules:
        configurator: Ipv4NetworkConfigurator { parameters: @display("p=50,50;i=block/cogwheel;is=s"); }
        core_0: Router { parameters: @display("p=400,125;i=abstract/router;is=s"); gates: pppg[2]; }
        core_1: Router { parameters: @display("p=400,250;i=abstract/router;is=s"); gates: pppg[2]; }
        core_2: Router { parameters: @display("p=400,375;i=abstract/router;is=s"); gates: pppg[2]; }
        host_0: Router { parameters: @display("p=200,250;i=device/server;is=s"); gates: pppg[6]; }
        host_1: Router { parameters: @display("p=600,250;i=device/server;is=s"); gates: pppg[6]; }
        sink_0: StandardHost { parameters: @display("p=625,300;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_1: StandardHost { parameters: @display("p=625,300;i=block/sink;is=vs"); gates: pppg[1]; }
        sink_2: StandardHost { parameters: @display("p=625,300;i=block/sink;is=vs"); gates: pppg[1]; }
        source_0: StandardHost { parameters: @display("p=175,300;i=block/source;is=vs"); gates: pppg[1]; }
        source_1: StandardHost { parameters: @display("p=175,300;i=block/source;is=vs"); gates: pppg[1]; }
        source_2: StandardHost { parameters: @display("p=175,300;i=block/source;is=vs"); gates: pppg[1]; }
        visualizer: IntegratedVisualizer { parameters: @display("p=50,100;i=block/app;is=s"); }
    connections:
        core_0.pppg[0] <--> defaultline <--> host_0.pppg[0];
        core_0.pppg[1] <--> defaultline <--> host_1.pppg[0];
        core_1.pppg[0] <--> defaultline <--> host_0.pppg[1];
        core_1.pppg[1] <--> defaultline <--> host_1.pppg[1];
        core_2.pppg[0] <--> defaultline <--> host_0.pppg[2];
        core_2.pppg[1] <--> defaultline <--> host_1.pppg[2];
        host_0.pppg[3] <--> infiniteline <--> source_0.pppg[0];
        host_0.pppg[4] <--> infiniteline <--> source_1.pppg[0];
        host_0.pppg[5] <--> infiniteline <--> source_2.pppg[0];
        host_1.pppg[3] <--> infiniteline <--> sink_0.pppg[0];
        host_1.pppg[4] <--> infiniteline <--> sink_1.pppg[0];
        host_1.pppg[5] <--> infiniteline <--> sink_2.pppg[0];
}