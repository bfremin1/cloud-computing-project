# Cloud Computing Final Project
Brandon Fremin (bfremin1@jhu.edu) and Shravan Venkatesan (svenka16@jhu.edu)

### Reproducing Results Locally

Note: Our project runs on Omnet++ 5.7. To install Omnet++, we used [this guide](https://doc.omnetpp.org/omnetpp/InstallGuide.pdf). We will explain our setup steps below:

1) Download [Omnet++ 5.7](https://omnetpp.org/download/old). This will give you a file called `omnetpp-5.7-windows-x86_64.zip`.
2) Unzip the downloaded file to get the Omnet++ source code. By default, it will be created in a folder called `omnetpp-5.7-windows-x86_64` in the same directory as your zip file.
3) Run a Mingwenv terminal by navigating to the `omnetpp-5.7-windows-x86_64/omnetpp-5.7` directory and running the `mingwenv.cmd` Windows command script. 
4) In the Mingwenv terminal, running the following commands to create the Omnet++ binaries. Building took about 30 minutes on our local laptops. *IMPORTANT NOTE*: if any directory in your abosulte path with a space in it, the make with not succeed. This took us a while to debug.
    ```
    ./configure
    make
    ```
5) Run `omnetpp` in the Mingwenv terminal.
6) When Omnet++ opens, it will ask you to select a working directory. Select `omnetpp-5.7-windows-x86_64/omnetpp-5.7/samples` as your working directory. 
7) Once the editor opens up into the directory above. An screen will be displayed prompting you to install INET. Keep all of the boxes checked and proceed. If you don't have INET installed, see this [link](https://inet.omnetpp.org/Installation.html) for installation steps. Once installed, there should be a folder called `inet4` in your `omnetpp-5.7-windows-x86_64/omnetpp-5.7/samples` directory.
8)  Navigate to the following directory: `omnetpp-5.7-windows-x86_64/omnetpp-5.7/samples/inet4/examples/inet`. It's a long way down the tree, but we want our scripts to use the correct relative paths.
9)  Create a new folder in this directory. We'll assume it's called `foo` for these instructions. This folder will contain all of our project results and files after our bash script finishes.
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
11) Now that Omnet++ is set up, pip should come with the default Mingwenv terminal. Pip install the following libraries that we use in our Python scripts:
    ```
    pip install matplotlib
    pip install numpy
    pip install pandas
    pip install pickle
    pip install networkx
    ```
12) From any terminal window on your machine, execute the `run.sh` command. It will log each time new tests are run. The entire set of simulations took us on the order of 12 hours to complete. We had to leave it running overnight
13) Several directories will be created within the `omnetpp-5.7-windows-x86_64/omnetpp-5.7/samples/inet4/examples/inet/foo` directory. 
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
            topoI_seedJ.sca  # scalar statistics from simulation
            topoI_seedJ.vec  # vector statistics from simulation
            topoI_seedJ.csv  # scalars and vectors formatted in a CSV files for analysis
            ...
        paths
            plot.png  # path length distributions
            ...
        bisections
            plot.png  # bisection bandwidth graphs
            ...
        topologies.txt  # Lists all of the topologies that Omnet++ needs to simulate
        topoI_seedJ.ned  # Define network topologies
        topoI_seedJ.ini  # Define flow patterns and simulation settings
        topoI_seedJ.xml  # Definre routing tables
        topoI_seedJ.pkl  # Store Python object to be reference later
        ...
    ```
14) All of the results presented in our final presentation and paper come from the above files. We used fixed RNG seeds to ensure that results are reproducible.

### Reproducing Results on Google Cloud VM

1) If you have not yet received an invitation from Google to join out Google Cloud VM, please send Brandon or Shravan your gmail, so we can add you and give you privileges.
2) Once you have access to our Google Cloud VM, go to this [link](https://console.cloud.google.com/compute/instances?project=cloud-computing-dc-topologies) which lists our VM instances in Google Cloud.
3) We only have one VM isntance named `omnetpp-jellyfish`. Click the SSH button to open an SSH terminal into that VM.
4) Run the following:
    ```
    cd /cloud-computing-project
    export PATH=/omnetpp-5.7/bin/:$PATH
    ./run.sh
    ```
5) After about 12 hours, you can find all of our results in the directory `/omnetpp-5.7/samples/inet4/examples/inet/datacenter_topologies` in the same structure described by step 13 above.