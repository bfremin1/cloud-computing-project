# Root of OMNET++

OMNET_PATH="/omnetpp-5.7" # Google Cloud VM
#OMNET_PATH="/c/Users/shrav/Documents/_Docs_/JHU/Classes/omnetpp-5.7-windows-x86_64/omnetpp-5.7"  # Shravan
#OMNET_PATH="/c/Users/bfrem/Documents/CloudComputing/omnetpp-5.7-windows-x86_64/omnetpp-5.7"  # Brandon

# Root of OMNET++ working directory for project. Should have inet support.
OMNET_WORKINGDIR_PATH="/omnetpp-5.7/samples/inet-4.2.9/examples/inet/datacenter_topologies" # Google Cloud VM
#OMNET_WORKINGDIR_PATH="/c/Users/shrav/Documents/_Docs_/JHU/Classes/omnetpp-5.7-windows-x86_64/omnetpp-5.7/samples/inet4/examples/inet/cc_datacenter";  # Shravan
#OMNET_WORKINGDIR_PATH="$OMNET_PATH/samples/inet4/examples/inet/DatacenterTopologies"  # Brandon

# Package name of OMNET++ working directory.
OMNET_WORKINGDIR_PACKAGE="inet.examples.inet.datacenter_topologies" # Google Cloud VM
#OMNET_WORKINGDIR_PACKAGE="inet.examples.inet.cc_datacenter"  # Shravan
#OMNET_WORKINGDIR_PACKAGE="inet.examples.inet.DatacenterTopologies"  # Brandon

# Python generation script for .ned, .ini, .xml files
SCRIPTS_DIR="/cloud-computing-project" # Google Cloud VM
#SCRIPTS_DIR="/c/Users/shrav/Documents/_Docs_/JHU/Classes/cloud-computing-project"  # Shravan
#SCRIPTS_DIR="/c/Users/bfrem/BlueFloor/Assets/cloud-computing-project"  # Brandon

# Desired output directory
OUTPUT_PATH="${OMNET_WORKINGDIR_PATH}/results" # Google Cloud VM
#OUTPUT_PATH="${OMNET_WORKINGDIR_PATH}/results"  # Shravan
#OUTPUT_PATH="$OMNET_WORKINGDIR_PATH/results"  # Brandon

if [[ ":$PATH:" != *"${OMNET_PATH}/bin"* ]]; then
    PATH="${OMNET_PATH}/bin:${PATH}"
fi

echo "********** Running topology generation script... **********"

mkdir -p "${OMNET_WORKINGDIR_PATH}"
mkdir -p "${OMNET_WORKINGDIR_PATH}/results"
mkdir -p "${OMNET_WORKINGDIR_PATH}/analysis"
python3 $SCRIPTS_DIR/m_omnetpp_file_generator.py $OMNET_WORKINGDIR_PATH $OMNET_WORKINGDIR_PACKAGE

echo "********** Making inet4 module... **********"
cd "${OMNET_PATH}/samples/inet-4.2.9"
make MODE=release -j8 all

cd "${OMNET_WORKINGDIR_PATH}"
while read -r -a line; do
    TOPO=${line[0]}
    echo "********** Running ${TOPO} simulation... **********"
    ${OMNET_PATH}/bin/opp_run -r 0 -m -u Cmdenv -n "../../;../../../src;../../../tutorials;../../../showcases" --image-path="$../../../images" -l "../../../src/INET" "${TOPO}.ini" --output-scalar-file="${OUTPUT_PATH}/${TOPO}.sca" --output-vector-file="${OUTPUT_PATH}/${TOPO}.vec" --cmdenv-express-mode=true
done < "${OMNET_WORKINGDIR_PATH}/topologies.txt"

while read -r -a line; do
    TOPO=${line[0]}
    echo "********** Collecting ${TOPO} results... **********"
    cd "${OUTPUT_PATH}"
    scavetool x ${TOPO}.sca ${TOPO}.vec -o "${OUTPUT_PATH}/${TOPO}.csv"
done < "${OMNET_WORKINGDIR_PATH}/topologies.txt"

echo "********** Analyzing results... **********"
python3 $SCRIPTS_DIR/m_omnetpp_result_analyzer.py $OMNET_WORKINGDIR_PATH hide-plots

echo "********** Generating path length distributions... **********"

mkdir -p "${OMNET_WORKINGDIR_PATH}/paths"
python3 $SCRIPTS_DIR/m_path_length_dist.py "${OMNET_WORKINGDIR_PATH}/paths"

echo "********** Generating bisection bandwidth plots... **********"

mkdir -p "${OMNET_WORKINGDIR_PATH}/bisections"
python3 $SCRIPTS_DIR/m_bisection_bandwidth.py "${OMNET_WORKINGDIR_PATH}/bisections"

echo "********** Done. :D **********"
