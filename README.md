# Cloud Computing Final Project
Brandon Fremin and Shravan Venkatesan

### Reproducing Results

Note: Our project runs on Omnet++ 5.7. To install Omnet++, we used [this guide](https://doc.omnetpp.org/omnetpp/InstallGuide.pdf). We will explain our setup steps below:

1) Download [Omnet++ 5.7](https://omnetpp.org/download/old). This will give you a file called `omnetpp-5.7-windows-x86_64.zip`.
2) Unzip the downloaded file to get the Omnet++ source code. By default, it will be created in a folder called `omnetpp-5.7-windows-x86_64` in the same directory as your zip file.
3) Run a Mingwenv terminal by navigating to the `omnetpp-5.7-windows-x86_64/omnetpp-5.7` directory and running the `mingwenv.cmd` Windows command script. 
4) In the Mingwenv terminal, running the following commands to create the Omnet++ binaries. Building took about 30 minutes on our local laptops:
    ```
    ./configure
    make
    ```
5) Run `omnetpp` in the Mingwenv terminal.
6) When Omnet++ opens, it will ask you to select a working directory. Select `omnetpp-5.7-windows-x86_64/omnetpp-5.7/samples` as your working directory. 
7) Once the editor opens up into the directory above. An screen will be displayed prompting you to install INET. Keep all of the boxes checked and proceed. If you don't have INET installed, see this [link](https://inet.omnetpp.org/Installation.html) for installation steps. Once installed, there should be a folder called `inet4` in your `omnetpp-5.7-windows-x86_64/omnetpp-5.7/samples` directory.
8) Navigate to the following directory: `omnetpp-5.7-windows-x86_64/omnetpp-5.7/samples/inet4/examples/inet`. It's a long way down the tree, but we want our scripts to use the correct relative paths.
9) Create a new folder in this directory. We'll assume it's called `foo` for these instructions. This folder will contain all of our project results and files after our bash script finishes.
10) Now we must set the absolute path variables for the `run.sh` scripts inside this repo. Please set the following according to your machines abosolute paths. We have left examples of Shravan and I's paths commented out in the `run.sh`:
    ```
    # Root of OMNET++
    OMNET_PATH="<path_to_omnet_dir>/omnetpp-5.7-windows-x86_64/omnetpp-5.7"

    # OMNET++ working directory for project. Should have inet support. 
    OMNET_WORKINGDIR_PATH="<path_to_omnet_dir>/omnetpp-5.7-windows-x86_64/omnetpp-5.7/samples/inet4/examples/inet/foo"

    # Package name of OMNET++ working directory. (MUST MATCH WORKING DIRECTORY)
    OMNET_WORKINGDIR_PACKAGE="inet.examples.inet.foo"

    # Python generation script for .ned, .ini, .xml files (path to repo cloned from GitHub. This README is in the SCRIPTS_DIR)
    SCRIPTS_DIR="<path_to_github_dir>"

    # Desired output directory
    OUTPUT_PATH="<path_to_omnet_dir>/omnetpp-5.7-windows-x86_64/omnetpp-5.7/samples/inet4/examples/inet/foo/results"
    ```
11) From any terminal window on your machine, execute the `run.sh` command. It will log each time new tests are run. The entire set of simulations took us on the order of 12 hours to complete. We had to leave it running overnight
12) Several directories will be created within the `omnetpp-5.7-windows-x86_64/omnetpp-5.7/samples/inet4/examples/inet/foo` directory. 
    ```
    foo
        analysis
            experiment1
                analysis.txt  # Aggregate analysis statistics of experiment
                topologies.txt  # Lists all of the topologies for this experiment
                latency_vs_size.png  # Latency vs Size for all flows
                throughput_vs_size.png  # Throughput vs Size for all flows
                throughput_latency_plot.png  # Latency vs Throughput for all trials
                topo1_seed1_flowstats.txt  # Stats about all flows in topo1 during trial 1
                topo1_seed2_flowstats.txt
                ...
                topo2_seed1_flowstats.txt
                topo2_seed2_flowstats.txt
                ...
                topoM_seedN_flowstats.txt
            experiment2
                ...
            ...
        results
            topo1.sca  # scalar statistics from simulation
            topo1.vec  # vector statistics from simulation
            topo1.csv  # scalars and vectors formatted in a CSV files for analysis
            ...
        theoretical
            # SHRAVAN ADD HERE
            # theoretical plots
        topologies.txt  # Lists all of the topologies that Omnet++ needs to simulate
        topo1.ned  # Define network topologies
        topo1.ini  # Define flow patterns and simulation settings
        topo1.xml  # Definre routing tables
        topo1.pkl  # Store Python object to be reference later
        ...
    ```
13) All of the results presented in our final presentation and paper come from the above files. We used fixed RNG seeds to ensure that results are reproducible.