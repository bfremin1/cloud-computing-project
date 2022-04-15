# Root of OMNET++
OMNET_PATH="/c/Users/shrav/Documents/_Docs_/JHU/Classes/omnetpp-5.7-windows-x86_64/omnetpp-5.7"
# Root of OMNET++ working directory for project. Should have inet support. 
OMNET_WORKINGDIR_PATH="/c/Users/shrav/Documents/_Docs_/JHU/Classes/omnetpp-5.7-windows-x86_64/omnetpp-5.7/samples/inet4/examples/inet/cc_datacenter";
# Package name of OMNET++ working directory. 
OMNET_WORKINGDIR_PACKAGE="inet.examples.inet.cc_datacenter;"
# Python generation script for .ned, .ini, .xml files
GENERATOR_PATH="/c/Users/shrav/Documents/_Docs_/JHU/Classes/cloud-computing-project/main.py";
# Desired output directory
OUTPUT_PATH="/c/Users/shrav/Documents/_Docs_/JHU/Classes/omnetpp-5.7-windows-x86_64/omnetpp-5.7/samples/inet4/examples/inet/cc_datacenter/results"

echo "********** Running topology generation script... **********"
python $GENERATOR_PATH $OMNET_WORKINGDIR_PATH $OMNET_WORKINGDIR_PACKAGE

echo "********** Making inet4 module... **********"
cd "${OMNET_PATH}/samples/inet4"
make MODE=release -j8 all

cd "${OMNET_WORKINGDIR_PATH}"
cat "${OMNET_WORKINGDIR_PATH}/topologies.txt" | while read TOPO; do
    echo "********** Running ${TOPO} simulation... **********"
    ${OMNET_PATH}/bin/opp_run.exe -r 0 -m -u Cmdenv -n "${OMNET_PATH}/samples/inet4/src;${OMNET_PATH}/samples/inet4/tutorials;${OMNET_PATH}/samples/inet4/showcases" --image-path="${OMNET_PATH}/samples/inet4/images" -l "${OMNET_PATH}/samples/inet4/src/INET" "${OMNET_WORKINGDIR_PATH}/${TOPO}.ini" --output-scalar-file="${OUTPUT_PATH}/${TOPO}.sca" --output-vector-file="${OUTPUT_PATH}/${TOPO}.vec"
done

echo "********** Collecting results... **********"
cd "${OUTPUT_PATH}"
scavetool x *.sca *.vec -o "${OUTPUT_PATH}/results.csv"

echo "********** Done. :D **********"
