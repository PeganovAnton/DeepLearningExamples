WORKSPACE=${1:-"/workspace/rn50v15_tf"}
DATA_DIR=${2:-"/data"}

bash ${WORKSPACE}/resnet50v1.5/training/GENERIC.sh ${WORKSPACE} ${DATA_DIR} \
    8 250 256 amp --mixup=0.2 
