package inet.examples.inet.DatacenterTopologies;

import inet.networklayer.configurator.ipv4.Ipv4NetworkConfigurator;
import inet.node.inet.Router;
import inet.node.inet.StandardHost;
import ned.DatarateChannel;

network Default
{
    parameters:
        @display("bgb=400,300");
    types:
        channel defaultline extends DatarateChannel { delay = 0.1us; datarate = 1Gbps; per = 0; }
    submodules:
        client: StandardHost { parameters: @display("p=100,150;i=device/laptop;is=s"); gates: pppg[1]; }
        configurator: Ipv4NetworkConfigurator { parameters: @display("p=50,50;i=block/cogwheel;is=s"); }
        router: Router { parameters: @display("p=200,150;i=abstract/router;is=s"); gates: pppg[2]; }
        server: StandardHost { parameters: @display("p=300,150;i=device/server;is=s"); gates: pppg[1]; }
    connections:
        client.pppg[0] <--> defaultline <--> router.pppg[0];
        router.pppg[1] <--> defaultline <--> server.pppg[0];
}