# Root of OMNET++
OMNET_PATH="/c/Users/shrav/Documents/_Docs_/JHU/Classes/omnetpp-5.7-windows-x86_64/omnetpp-5.7"  # Shravan
#OMNET_PATH="/c/Users/bfrem/Documents/CloudComputing/omnetpp-5.7-windows-x86_64/omnetpp-5.7"  # Brandon

# Root of OMNET++ working directory for project. Should have inet support. 
OMNET_WORKINGDIR_PATH="/c/Users/shrav/Documents/_Docs_/JHU/Classes/omnetpp-5.7-windows-x86_64/omnetpp-5.7/samples/inet4/examples/inet/cc_datacenter";  # Shravan
#OMNET_WORKINGDIR_PATH="$OMNET_PATH/samples/inet4/examples/inet/DatacenterTopologies"  # Brandon

# Package name of OMNET++ working directory. 
OMNET_WORKINGDIR_PACKAGE="inet.examples.inet.cc_datacenter"  # Shravan
#OMNET_WORKINGDIR_PACKAGE="inet.examples.inet.DatacenterTopologies"  # Brandon

# Python generation script for .ned, .ini, .xml files
SCRIPTS_DIR="/c/Users/shrav/Documents/_Docs_/JHU/Classes/cloud-computing-project"  # Shravan
#SCRIPTS_DIR="/c/Users/bfrem/BlueFloor/Assets/cloud-computing-project"  # Brandon

# Desired output directory
OUTPUT_PATH="/c/Users/shrav/Documents/_Docs_/JHU/Classes/omnetpp-5.7-windows-x86_64/omnetpp-5.7/samples/inet4/examples/inet/cc_datacenter/results"  # Shravan
#OUTPUT_PATH="$OMNET_WORKINGDIR_PATH/results"  # Brandon

echo "********** Running topology generation script... **********"
python $SCRIPTS_DIR/m_omnetpp_file_generator.py $OMNET_WORKINGDIR_PATH $OMNET_WORKINGDIR_PACKAGE

echo "********** Making inet4 module... **********"
cd "${OMNET_PATH}/samples/inet4"
make MODE=release -j8 all

cd "${OMNET_WORKINGDIR_PATH}"
while read -r -a line; do
    TOPO=${line[0]}
    echo "********** Running ${TOPO} simulation... **********"
    ${OMNET_PATH}/bin/opp_run.exe -r 0 -m -u Cmdenv -n "../../;../../../src;../../../tutorials;../../../showcases" --image-path="$../../../images" -l "../../../src/INET" "${TOPO}.ini" --output-scalar-file="${OUTPUT_PATH}/${TOPO}.sca" --output-vector-file="${OUTPUT_PATH}/${TOPO}.vec" --cmdenv-express-mode=true
done < "${OMNET_WORKINGDIR_PATH}/topologies.txt"

while read -r -a line; do
    TOPO=${line[0]}
    echo "********** Collecting ${TOPO} results... **********"
    cd "${OUTPUT_PATH}"
    scavetool x ${TOPO}.sca ${TOPO}.vec -o "${OUTPUT_PATH}/${TOPO}.csv"
done < "${OMNET_WORKINGDIR_PATH}/topologies.txt"

echo "********** Analyzing results... **********"
python $SCRIPTS_DIR/m_omnetpp_result_analyzer.py $OMNET_WORKINGDIR_PATH hide-plots

echo "********** Done. :D **********"
