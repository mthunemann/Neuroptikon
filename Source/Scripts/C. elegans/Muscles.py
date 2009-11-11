"""
This script adds all of the muscles and innervations of C. elegans to the current network, also creating the neurons if necessary.

Dataset from "Neuron Connections to Sensory Organs and Body Muscles" section of:
    http://www.wormatlas.org/neuronalwiring.html#Neuronconnections
"""

# Make sure the network of neurons has been loaded.
if not any(network.neurons()):
    execfile('Neurons.py')

muscleData = {
    'MANAL': {'A-P Position': 0.81}, 
    'MDL01': {'A-P Position': 0.06}, 
    'MDL02': {'A-P Position': 0.05}, 
    'MDL03': {'A-P Position': 0.1}, 
    'MDL04': {'A-P Position': 0.07}, 
    'MDL05': {'A-P Position': 0.15}, 
    'MDL06': {'A-P Position': 0.12}, 
    'MDL07': {'A-P Position': 0.21}, 
    'MDL08': {'A-P Position': 0.16}, 
    'MDL09': {'A-P Position': 0.29}, 
    'MDL10': {'A-P Position': 0.25}, 
    'MDL11': {'A-P Position': 0.38}, 
    'MDL12': {'A-P Position': 0.33}, 
    'MDL13': {'A-P Position': 0.47}, 
    'MDL14': {'A-P Position': 0.42}, 
    'MDL15': {'A-P Position': 0.55}, 
    'MDL16': {'A-P Position': 0.51}, 
    'MDL17': {'A-P Position': 0.64}, 
    'MDL18': {'A-P Position': 0.6}, 
    'MDL19': {'A-P Position': 0.72}, 
    'MDL20': {'A-P Position': 0.68}, 
    'MDL21': {'A-P Position': 0.8}, 
    'MDL22': {'A-P Position': 0.79}, 
    'MDL23': {'A-P Position': 0.89}, 
    'MDL24': {'A-P Position': 0.85}, 
    'MDR01': {'A-P Position': 0.06}, 
    'MDR02': {'A-P Position': 0.05}, 
    'MDR03': {'A-P Position': 0.1}, 
    'MDR04': {'A-P Position': 0.07}, 
    'MDR05': {'A-P Position': 0.15}, 
    'MDR06': {'A-P Position': 0.12}, 
    'MDR07': {'A-P Position': 0.21}, 
    'MDR08': {'A-P Position': 0.18}, 
    'MDR09': {'A-P Position': 0.29}, 
    'MDR10': {'A-P Position': 0.25}, 
    'MDR11': {'A-P Position': 0.38}, 
    'MDR12': {'A-P Position': 0.33}, 
    'MDR13': {'A-P Position': 0.47}, 
    'MDR14': {'A-P Position': 0.42}, 
    'MDR15': {'A-P Position': 0.55}, 
    'MDR16': {'A-P Position': 0.51}, 
    'MDR17': {'A-P Position': 0.64}, 
    'MDR18': {'A-P Position': 0.6}, 
    'MDR19': {'A-P Position': 0.72}, 
    'MDR20': {'A-P Position': 0.68}, 
    'MDR21': {'A-P Position': 0.8}, 
    'MDR22': {'A-P Position': 0.79}, 
    'MDR23': {'A-P Position': 0.89}, 
    'MDR24': {'A-P Position': 0.85}, 
    'MVL01': {'A-P Position': 0.06}, 
    'MVL02': {'A-P Position': 0.05}, 
    'MVL03': {'A-P Position': 0.1}, 
    'MVL04': {'A-P Position': 0.08}, 
    'MVL05': {'A-P Position': 0.15}, 
    'MVL06': {'A-P Position': 0.12}, 
    'MVL07': {'A-P Position': 0.2}, 
    'MVL08': {'A-P Position': 0.18}, 
    'MVL09': {'A-P Position': 0.27}, 
    'MVL10': {'A-P Position': 0.22}, 
    'MVL11': {'A-P Position': 0.35}, 
    'MVL12': {'A-P Position': 0.29}, 
    'MVL13': {'A-P Position': 0.44}, 
    'MVL14': {'A-P Position': 0.39}, 
    'MVL15': {'A-P Position': 0.54}, 
    'MVL16': {'A-P Position': 0.48}, 
    'MVL17': {'A-P Position': 0.64}, 
    'MVL18': {'A-P Position': 0.6}, 
    'MVL19': {'A-P Position': 0.73}, 
    'MVL20': {'A-P Position': 0.67}, 
    'MVL21': {'A-P Position': 0.77}, 
    'MVL22': {'A-P Position': 0.81}, 
    'MVL23': {'A-P Position': 0.84}, 
    'MVR01': {'A-P Position': 0.06}, 
    'MVR02': {'A-P Position': 0.05}, 
    'MVR03': {'A-P Position': 0.1}, 
    'MVR04': {'A-P Position': 0.08}, 
    'MVR05': {'A-P Position': 0.14}, 
    'MVR06': {'A-P Position': 0.12}, 
    'MVR07': {'A-P Position': 0.2}, 
    'MVR08': {'A-P Position': 0.17}, 
    'MVR09': {'A-P Position': 0.27}, 
    'MVR10': {'A-P Position': 0.22}, 
    'MVR11': {'A-P Position': 0.35}, 
    'MVR12': {'A-P Position': 0.29}, 
    'MVR13': {'A-P Position': 0.44}, 
    'MVR14': {'A-P Position': 0.39}, 
    'MVR15': {'A-P Position': 0.54}, 
    'MVR16': {'A-P Position': 0.48}, 
    'MVR17': {'A-P Position': 0.64}, 
    'MVR18': {'A-P Position': 0.6}, 
    'MVR19': {'A-P Position': 0.73}, 
    'MVR20': {'A-P Position': 0.67}, 
    'MVR21': {'A-P Position': 0.81}, 
    'MVR22': {'A-P Position': 0.77}, 
    'MVR23': {'A-P Position': 0.84}, 
    'MVR24': {'A-P Position': 0.89}, 
    'MVULVA': {'A-P Position': 0.54}, 
}

muscles = {}
for muscleName, properties in muscleData.iteritems():
    muscle = network.createMuscle(name = muscleName)
    muscle.addAttribute('A-P Position', Attribute.DECIMAL_TYPE, properties['A-P Position'])
    if muscleName not in ('MANAL', 'MVULVA'):
        muscle.addAttribute('Face', Attribute.STRING_TYPE, muscleName[1])
        muscle.addAttribute('Side', Attribute.STRING_TYPE, muscleName[2])
    muscles[muscleName] = muscle

innervationData = [
    ('ADEL', 'MDL05', 1), 
    ('AS01', 'MDL05', 3.25), 
    ('AS01', 'MDR05', 3.25), 
    ('AS01', 'MDL08', 3.25), 
    ('AS01', 'MDR08', 3.25), 
    ('AS02', 'MDL08', 2.75), 
    ('AS02', 'MDR08', 2.75), 
    ('AS02', 'MDL07', 2.75), 
    ('AS02', 'MDR07', 2.75), 
    ('AS03', 'MDL10', 3), 
    ('AS03', 'MDR10', 3), 
    ('AS03', 'MDL09', 3), 
    ('AS03', 'MDR09', 3), 
    ('AS04', 'MDL12', 2.25), 
    ('AS04', 'MDR12', 2.25), 
    ('AS04', 'MDL11', 2.25), 
    ('AS04', 'MDR11', 2.25), 
    ('AS05', 'MDL11', 2.5), 
    ('AS05', 'MDR11', 2.5), 
    ('AS05', 'MDL14', 2.5), 
    ('AS05', 'MDR14', 2.5), 
    ('AS06', 'MDL14', 2.5), 
    ('AS06', 'MDR14', 2.5), 
    ('AS06', 'MDL13', 2.5), 
    ('AS06', 'MDR13', 2.5), 
    ('AS07', 'MDL13', 2.708333333), 
    ('AS07', 'MDR13', 2.708333333), 
    ('AS07', 'MDL16', 2.708333333), 
    ('AS07', 'MDR16', 2.708333333), 
    ('AS08', 'MDL15', 2.708333333), 
    ('AS08', 'MDR15', 2.708333333), 
    ('AS08', 'MDL18', 2.708333333), 
    ('AS08', 'MDR18', 2.708333333), 
    ('AS09', 'MDL20', 2.708333333), 
    ('AS09', 'MDR20', 2.708333333), 
    ('AS09', 'MDL17', 2.708333333), 
    ('AS09', 'MDR17', 2.708333333), 
    ('AS10', 'MDL20', 2.708333333), 
    ('AS10', 'MDR20', 2.708333333), 
    ('AS10', 'MDL19', 2.708333333), 
    ('AS10', 'MDR19', 2.708333333), 
    ('AS11', 'MDL22', 2.708333333), 
    ('AS11', 'MDR22', 2.708333333), 
    ('AS11', 'MDL21', 2.708333333), 
    ('AS11', 'MDR21', 2.708333333), 
    ('AVFL', 'MVL12', 1), 
    ('AVFL', 'MVL11', 1), 
    ('AVFR', 'MVL14', 2), 
    ('AVFR', 'MVR14', 2), 
    ('AVKR', 'MVL10', 2), 
    ('AVL', 'MVL10', 5), 
    ('AVL', 'MVR10', 5), 
    ('CEPVL', 'MVL03', 1), 
    ('CEPVR', 'MVR04', 1), 
    ('DA01', 'MDL08', 8), 
    ('DA01', 'MDR08', 8), 
    ('DA02', 'MDL08', 1.875), 
    ('DA02', 'MDR08', 1.875), 
    ('DA02', 'MDL07', 1.875), 
    ('DA02', 'MDR07', 1.875), 
    ('DA02', 'MDL10', 1.875), 
    ('DA02', 'MDR10', 1.875), 
    ('DA02', 'MDL09', 1.875), 
    ('DA02', 'MDR09', 1.875), 
    ('DA03', 'MDL10', 5), 
    ('DA03', 'MDR10', 5), 
    ('DA03', 'MDL09', 5), 
    ('DA03', 'MDR09', 5), 
    ('DA03', 'MDL12', 5), 
    ('DA03', 'MDR12', 5), 
    ('DA04', 'MDL12', 4.333333333), 
    ('DA04', 'MDR12', 4.333333333), 
    ('DA04', 'MDL11', 4.333333333), 
    ('DA04', 'MDR11', 4.333333333), 
    ('DA04', 'MDL14', 4.333333333), 
    ('DA04', 'MDR14', 4.333333333), 
    ('DA05', 'MDL14', 4.25), 
    ('DA05', 'MDR14', 4.25), 
    ('DA05', 'MDL13', 4.25), 
    ('DA05', 'MDR13', 4.25), 
    ('DA06', 'MDL12', 4), 
    ('DA06', 'MDR12', 4), 
    ('DA06', 'MDL11', 4), 
    ('DA06', 'MDR11', 4), 
    ('DA06', 'MDL14', 4), 
    ('DA06', 'MDR14', 4), 
    ('DA06', 'MDL13', 4), 
    ('DA06', 'MDR13', 4), 
    ('DA06', 'MDL16', 4), 
    ('DA06', 'MDR16', 4), 
    ('DA07', 'MDL15', 4), 
    ('DA07', 'MDR15', 4), 
    ('DA07', 'MDL18', 4), 
    ('DA07', 'MDR18', 4), 
    ('DA07', 'MDL17', 4), 
    ('DA07', 'MDR17', 4), 
    ('DA08', 'MDL20', 4), 
    ('DA08', 'MDR20', 4), 
    ('DA08', 'MDL19', 4), 
    ('DA08', 'MDR19', 4), 
    ('DA08', 'MDL17', 4), 
    ('DA08', 'MDR17', 4), 
    ('DA09', 'MDL21', 4), 
    ('DA09', 'MDR21', 4), 
    ('DA09', 'MDL19', 4), 
    ('DA09', 'MDR19', 4), 
    ('DA09', 'MDL22', 4), 
    ('DA09', 'MDR22', 4), 
    ('DB01', 'MDL08', 0.75), 
    ('DB01', 'MDR08', 0.75), 
    ('DB01', 'MDL07', 0.75), 
    ('DB01', 'MDR07', 0.75), 
    ('DB02', 'MDL10', 3), 
    ('DB02', 'MDR10', 3), 
    ('DB02', 'MDL09', 3), 
    ('DB02', 'MDR09', 3), 
    ('DB02', 'MDL12', 3), 
    ('DB02', 'MDR12', 3), 
    ('DB02', 'MDL11', 3), 
    ('DB02', 'MDR11', 3), 
    ('DB03', 'MDL12', 3.125), 
    ('DB03', 'MDR12', 3.125), 
    ('DB03', 'MDL11', 3.125), 
    ('DB03', 'MDR11', 3.125), 
    ('DB03', 'MDL14', 3.125), 
    ('DB03', 'MDR14', 3.125), 
    ('DB03', 'MDL13', 3.125), 
    ('DB03', 'MDR13', 3.125), 
    ('DB04', 'MDL14', 2.6), 
    ('DB04', 'MDR14', 2.6), 
    ('DB04', 'MDL13', 2.6), 
    ('DB04', 'MDR13', 2.6), 
    ('DB04', 'MDL16', 2.6), 
    ('DB04', 'MDR16', 2.6), 
    ('DB05', 'MDL15', 2.6), 
    ('DB05', 'MDR15', 2.6), 
    ('DB05', 'MDL18', 2.6), 
    ('DB05', 'MDR18', 2.6), 
    ('DB05', 'MDL17', 2.6), 
    ('DB05', 'MDR17', 2.6), 
    ('DB06', 'MDL17', 2.6), 
    ('DB06', 'MDR17', 2.6), 
    ('DB06', 'MDL20', 2.6), 
    ('DB06', 'MDR20', 2.6), 
    ('DB06', 'MDL19', 2.6), 
    ('DB06', 'MDR19', 2.6), 
    ('DB07', 'MDL22', 2.6), 
    ('DB07', 'MDR22', 2.6), 
    ('DB07', 'MDL21', 2.6), 
    ('DB07', 'MDR21', 2.6), 
    ('DB07', 'MDL19', 2.6), 
    ('DB07', 'MDR19', 2.6), 
    ('DD01', 'MDL08', 4.25), 
    ('DD01', 'MDR08', 4.25), 
    ('DD01', 'MDL07', 4.25), 
    ('DD01', 'MDR07', 4.25), 
    ('DD01', 'MDL10', 4.25), 
    ('DD01', 'MDR10', 4.25), 
    ('DD01', 'MDL09', 4.25), 
    ('DD01', 'MDR09', 4.25), 
    ('DD02', 'MDL09', 4.666666667), 
    ('DD02', 'MDR09', 4.666666667), 
    ('DD02', 'MDL12', 4.666666667), 
    ('DD02', 'MDR12', 4.666666667), 
    ('DD02', 'MDL11', 4.666666667), 
    ('DD02', 'MDR11', 4.666666667), 
    ('DD03', 'MDL11', 5.333333333), 
    ('DD03', 'MDR11', 5.333333333), 
    ('DD03', 'MDL14', 5.333333333), 
    ('DD03', 'MDR14', 5.333333333), 
    ('DD03', 'MDL13', 5.333333333), 
    ('DD03', 'MDR13', 5.333333333), 
    ('DD04', 'MDL13', 4.7), 
    ('DD04', 'MDR13', 4.7), 
    ('DD04', 'MDL16', 4.7), 
    ('DD04', 'MDR16', 4.7), 
    ('DD04', 'MDL15', 4.7), 
    ('DD04', 'MDR15', 4.7), 
    ('DD05', 'MDL18', 4.7), 
    ('DD05', 'MDR18', 4.7), 
    ('DD05', 'MDL17', 4.7), 
    ('DD05', 'MDR17', 4.7), 
    ('DD05', 'MDL20', 4.7), 
    ('DD05', 'MDR20', 4.7), 
    ('DD06', 'MDL22', 4.7), 
    ('DD06', 'MDR22', 4.7), 
    ('DD06', 'MDL21', 4.7), 
    ('DD06', 'MDR21', 4.7), 
    ('DD06', 'MDL19', 4.7), 
    ('DD06', 'MDR19', 4.7), 
    ('DVB', 'MANAL', 5), 
    ('HSNL', 'MVULVA', 7), 
    ('HSNR', 'MVULVA', 6), 
    ('IL1DL', 'MDL02', 1.666666667), 
    ('IL1DL', 'MDL01', 1.666666667), 
    ('IL1DL', 'MDL04', 1.666666667), 
    ('IL1DR', 'MDR02', 3.5), 
    ('IL1DR', 'MDR01', 3.5), 
    ('IL1L', 'MDL01', 2.6), 
    ('IL1L', 'MDL03', 2.6), 
    ('IL1L', 'MDL05', 2.6), 
    ('IL1L', 'MVL01', 2.6), 
    ('IL1L', 'MVL03', 2.6), 
    ('IL1R', 'MDR01', 3.25), 
    ('IL1R', 'MDR03', 3.25), 
    ('IL1R', 'MVR01', 3.25), 
    ('IL1R', 'MVR03', 3.25), 
    ('IL1VL', 'MVL02', 4.5), 
    ('IL1VL', 'MVL01', 4.5), 
    ('IL1VR', 'MVR02', 5), 
    ('IL1VR', 'MVR01', 5), 
    ('PDA', 'MDL21', 2), 
    ('PDB', 'MVL22', 1), 
    ('PDB', 'MVR21', 1), 
    ('PVNL', 'MVL09', 3), 
    ('PVNR', 'MVL12', 1.5), 
    ('PVNR', 'MVL13', 1.5), 
    ('RID', 'MDL14', 1.5), 
    ('RID', 'MDL21', 1.5), 
    ('RIML', 'MDR05', 2), 
    ('RIML', 'MVR05', 2), 
    ('RIMR', 'MDL05', 1), 
    ('RIMR', 'MDL07', 1), 
    ('RIMR', 'MVL05', 1), 
    ('RIMR', 'MVL07', 1), 
    ('RIVL', 'MVR06', 1.333333333), 
    ('RIVL', 'MVR05', 1.333333333), 
    ('RIVL', 'MVR08', 1.333333333), 
    ('RIVR', 'MVR04', 1), 
    ('RIVR', 'MVR06', 1), 
    ('RIVR', 'MVL06', 1), 
    ('RIVR', 'MVL05', 1), 
    ('RIVR', 'MVL08', 1), 
    ('RMDDL', 'MDR02', 1.333333333), 
    ('RMDDL', 'MDR01', 1.333333333), 
    ('RMDDL', 'MDR04', 1.333333333), 
    ('RMDDL', 'MDR03', 1.333333333), 
    ('RMDDL', 'MDR08', 1.333333333), 
    ('RMDDL', 'MVR01', 1.333333333), 
    ('RMDDR', 'MDL02', 1.428571429), 
    ('RMDDR', 'MDL01', 1.428571429), 
    ('RMDDR', 'MDR04', 1.428571429), 
    ('RMDDR', 'MDL04', 1.428571429), 
    ('RMDDR', 'MDL03', 1.428571429), 
    ('RMDDR', 'MVR02', 1.428571429), 
    ('RMDDR', 'MVR01', 1.428571429), 
    ('RMDL', 'MDR01', 1.222222222), 
    ('RMDL', 'MDR03', 1.222222222), 
    ('RMDL', 'MDL03', 1.222222222), 
    ('RMDL', 'MDL05', 1.222222222), 
    ('RMDL', 'MVR01', 1.222222222), 
    ('RMDL', 'MVL01', 1.222222222), 
    ('RMDL', 'MVR03', 1.222222222), 
    ('RMDL', 'MVR05', 1.222222222), 
    ('RMDL', 'MVR07', 1.222222222), 
    ('RMDR', 'MDL03', 0.8), 
    ('RMDR', 'MDL05', 0.8), 
    ('RMDR', 'MDR05', 0.8), 
    ('RMDR', 'MVL03', 0.8), 
    ('RMDR', 'MVL05', 0.8), 
    ('RMDVL', 'MDR01', 1), 
    ('RMDVL', 'MVR02', 1), 
    ('RMDVL', 'MVR01', 1), 
    ('RMDVL', 'MVL04', 1), 
    ('RMDVL', 'MVR04', 1), 
    ('RMDVL', 'MVR03', 1), 
    ('RMDVL', 'MVR06', 1), 
    ('RMDVL', 'MVR05', 1), 
    ('RMDVL', 'MVR08', 1), 
    ('RMDVR', 'MDL01', 0.818181818), 
    ('RMDVR', 'MVL02', 0.818181818), 
    ('RMDVR', 'MVL01', 0.818181818), 
    ('RMDVR', 'MVL04', 0.818181818), 
    ('RMDVR', 'MVR04', 0.818181818), 
    ('RMDVR', 'MVL03', 0.818181818), 
    ('RMDVR', 'MVR06', 0.818181818), 
    ('RMDVR', 'MVL06', 0.818181818), 
    ('RMDVR', 'MVL05', 0.818181818), 
    ('RMDVR', 'MVR08', 0.818181818), 
    ('RMDVR', 'MVL08', 0.818181818), 
    ('RMED', 'MVL02', 2), 
    ('RMED', 'MVR02', 2), 
    ('RMED', 'MVL04', 2), 
    ('RMED', 'MVR04', 2), 
    ('RMED', 'MVL06', 2), 
    ('RMEL', 'MDR01', 3), 
    ('RMEL', 'MDR03', 3), 
    ('RMEL', 'MVR01', 3), 
    ('RMEL', 'MVR03', 3), 
    ('RMER', 'MDL01', 5), 
    ('RMER', 'MDL03', 5), 
    ('RMER', 'MVL01', 5), 
    ('RMEV', 'MDR02', 1), 
    ('RMEV', 'MDL02', 1), 
    ('RMEV', 'MDR04', 1), 
    ('RMEV', 'MDL04', 1), 
    ('RMEV', 'MDL06', 1), 
    ('RMFL', 'MDR03', 1), 
    ('RMFL', 'MVR01', 1), 
    ('RMFL', 'MVR03', 1), 
    ('RMGL', 'MDL05', 2), 
    ('RMGL', 'MVL05', 2), 
    ('RMGR', 'MDR05', 1), 
    ('RMGR', 'MVR05', 1), 
    ('RMGR', 'MVR07', 1), 
    ('RMHL', 'MDR01', 2.666666667), 
    ('RMHL', 'MDR03', 2.666666667), 
    ('RMHL', 'MVR01', 2.666666667), 
    ('RMHR', 'MDL01', 1.75), 
    ('RMHR', 'MDL03', 1.75), 
    ('RMHR', 'MDL05', 1.75), 
    ('RMHR', 'MVL01', 1.75), 
    ('SMBDL', 'MDR02', 1.6), 
    ('SMBDL', 'MDR01', 1.6), 
    ('SMBDL', 'MDR04', 1.6), 
    ('SMBDL', 'MDR03', 1.6), 
    ('SMBDL', 'MDR06', 1.6), 
    ('SMBDR', 'MDL02', 1.666666667), 
    ('SMBDR', 'MDR04', 1.666666667), 
    ('SMBDR', 'MDL04', 1.666666667), 
    ('SMBDR', 'MDL03', 1.666666667), 
    ('SMBDR', 'MDL06', 1.666666667), 
    ('SMBDR', 'MDR08', 1.666666667), 
    ('SMBVL', 'MVL02', 0.857142857), 
    ('SMBVL', 'MVL01', 0.857142857), 
    ('SMBVL', 'MVL04', 0.857142857), 
    ('SMBVL', 'MVL03', 0.857142857), 
    ('SMBVL', 'MVL06', 0.857142857), 
    ('SMBVL', 'MVL05', 0.857142857), 
    ('SMBVL', 'MVL08', 0.857142857), 
    ('SMBVR', 'MVR02', 1), 
    ('SMBVR', 'MVR01', 1), 
    ('SMBVR', 'MVR04', 1), 
    ('SMBVR', 'MVR03', 1), 
    ('SMBVR', 'MVR06', 1), 
    ('SMBVR', 'MVR07', 1), 
    ('SMDDL', 'MDR02', 0.454545455), 
    ('SMDDL', 'MDR04', 0.454545455), 
    ('SMDDL', 'MDL04', 0.454545455), 
    ('SMDDL', 'MDR03', 0.454545455), 
    ('SMDDL', 'MDR06', 0.454545455), 
    ('SMDDL', 'MDL06', 0.454545455), 
    ('SMDDL', 'MDR05', 0.454545455), 
    ('SMDDL', 'MDL08', 0.454545455), 
    ('SMDDL', 'MDR07', 0.454545455), 
    ('SMDDL', 'MVL02', 0.454545455), 
    ('SMDDL', 'MVL04', 0.454545455), 
    ('SMDDR', 'MDR04', 0.428571429), 
    ('SMDDR', 'MDL04', 0.428571429), 
    ('SMDDR', 'MDR06', 0.428571429), 
    ('SMDDR', 'MDL06', 0.428571429), 
    ('SMDDR', 'MDL05', 0.428571429), 
    ('SMDDR', 'MDL08', 0.428571429), 
    ('SMDDR', 'MVR02', 0.428571429), 
    ('SMDVL', 'MVR02', 0.5), 
    ('SMDVL', 'MVR04', 0.5), 
    ('SMDVL', 'MVR03', 0.5), 
    ('SMDVL', 'MVL03', 0.5), 
    ('SMDVL', 'MVR06', 0.5), 
    ('SMDVL', 'MVL06', 0.5), 
    ('SMDVR', 'MVL02', 1), 
    ('SMDVR', 'MVL04', 1), 
    ('SMDVR', 'MVL03', 1), 
    ('SMDVR', 'MVR07', 1), 
    ('URADL', 'MDL02', 2), 
    ('URADL', 'MDL04', 2), 
    ('URADL', 'MDL03', 2), 
    ('URADR', 'MDR02', 2.333333333), 
    ('URADR', 'MDR01', 2.333333333), 
    ('URADR', 'MDR03', 2.333333333), 
    ('URAVL', 'MVL02', 2.25), 
    ('URAVL', 'MVL01', 2.25), 
    ('URAVL', 'MVL04', 2.25), 
    ('URAVL', 'MVL03', 2.25), 
    ('URAVR', 'MVR02', 2), 
    ('URAVR', 'MVR01', 2), 
    ('URAVR', 'MVR04', 2), 
    ('URAVR', 'MVR03', 2), 
    ('VA01', 'MVR08', 2.75), 
    ('VA01', 'MVL08', 2.75), 
    ('VA01', 'MVL07', 2.75), 
    ('VA01', 'MVR07', 2.75), 
    ('VA02', 'MVL07', 4.75), 
    ('VA02', 'MVR07', 4.75), 
    ('VA02', 'MVL10', 4.75), 
    ('VA02', 'MVR10', 4.75), 
    ('VA03', 'MVL10', 4.833333333), 
    ('VA03', 'MVR10', 4.833333333), 
    ('VA03', 'MVL09', 4.833333333), 
    ('VA03', 'MVR09', 4.833333333), 
    ('VA03', 'MVL12', 4.833333333), 
    ('VA03', 'MVR12', 4.833333333), 
    ('VA04', 'MVL12', 6.25), 
    ('VA04', 'MVR12', 6.25), 
    ('VA04', 'MVL11', 6.25), 
    ('VA04', 'MVR11', 6.25), 
    ('VA05', 'MVL11', 4.75), 
    ('VA05', 'MVR11', 4.75), 
    ('VA05', 'MVL14', 4.75), 
    ('VA05', 'MVR14', 4.75), 
    ('VA06', 'MVL14', 5), 
    ('VA06', 'MVR14', 5), 
    ('VA06', 'MVL13', 5), 
    ('VA06', 'MVR13', 5), 
    ('VA07', 'MVL13', 3.857142857), 
    ('VA07', 'MVR13', 3.857142857), 
    ('VA07', 'MVL16', 3.857142857), 
    ('VA07', 'MVR16', 3.857142857), 
    ('VA07', 'MVL15', 3.857142857), 
    ('VA07', 'MVR15', 3.857142857), 
    ('VA07', 'MVULVA', 3.857142857), 
    ('VA08', 'MVL16', 5.75), 
    ('VA08', 'MVR16', 5.75), 
    ('VA08', 'MVL15', 5.75), 
    ('VA08', 'MVR15', 5.75), 
    ('VA09', 'MVL15', 4.675675676), 
    ('VA09', 'MVR15', 4.675675676), 
    ('VA09', 'MVL18', 4.675675676), 
    ('VA09', 'MVR18', 4.675675676), 
    ('VA10', 'MVL17', 4.675675676), 
    ('VA10', 'MVR17', 4.675675676), 
    ('VA10', 'MVL18', 4.675675676), 
    ('VA10', 'MVR18', 4.675675676), 
    ('VA11', 'MVL19', 4.675675676), 
    ('VA11', 'MVR19', 4.675675676), 
    ('VA11', 'MVL20', 4.675675676), 
    ('VA11', 'MVR20', 4.675675676), 
    ('VA12', 'MVL21', 4.675675676), 
    ('VA12', 'MVR22', 4.675675676), 
    ('VA12', 'MVL22', 4.675675676), 
    ('VA12', 'MVR21', 4.675675676), 
    ('VB01', 'MVR08', 1.25), 
    ('VB01', 'MVL08', 1.25), 
    ('VB01', 'MVL07', 1.25), 
    ('VB01', 'MVR07', 1.25), 
    ('VB02', 'MVL07', 3.25), 
    ('VB02', 'MVR07', 3.25), 
    ('VB02', 'MVL10', 3.25), 
    ('VB02', 'MVR10', 3.25), 
    ('VB02', 'MVL09', 3.25), 
    ('VB02', 'MVR09', 3.25), 
    ('VB02', 'MVL12', 3.25), 
    ('VB02', 'MVR12', 3.25), 
    ('VB03', 'MVL12', 5.833333333), 
    ('VB03', 'MVR12', 5.833333333), 
    ('VB03', 'MVL11', 5.833333333), 
    ('VB03', 'MVR11', 5.833333333), 
    ('VB03', 'MVL14', 5.833333333), 
    ('VB03', 'MVR14', 5.833333333), 
    ('VB04', 'MVL11', 5), 
    ('VB04', 'MVR11', 5), 
    ('VB04', 'MVL14', 5), 
    ('VB04', 'MVR14', 5), 
    ('VB05', 'MVL14', 5.5), 
    ('VB05', 'MVR14', 5.5), 
    ('VB05', 'MVL13', 5.5), 
    ('VB05', 'MVR13', 5.5), 
    ('VB06', 'MVL16', 5.6), 
    ('VB06', 'MVR16', 5.6), 
    ('VB06', 'MVL15', 5.6), 
    ('VB06', 'MVR15', 5.6), 
    ('VB06', 'MVULVA', 5.6), 
    ('VB07', 'MVL15', 4.682926829), 
    ('VB07', 'MVR15', 4.682926829), 
    ('VB08', 'MVL18', 5.333333333), 
    ('VB08', 'MVR18', 5.333333333), 
    ('VB08', 'MVL17', 5.333333333), 
    ('VB08', 'MVR17', 5.333333333), 
    ('VB08', 'MVL20', 5.333333333), 
    ('VB08', 'MVR20', 5.333333333), 
    ('VB09', 'MVL17', 6), 
    ('VB09', 'MVR17', 6), 
    ('VB09', 'MVL20', 6), 
    ('VB09', 'MVR20', 6), 
    ('VB10', 'MVL20', 4.682926829), 
    ('VB10', 'MVR20', 4.682926829), 
    ('VB10', 'MVL19', 4.682926829), 
    ('VB10', 'MVR19', 4.682926829), 
    ('VB11', 'MVL21', 4.682926829), 
    ('VB11', 'MVR22', 4.682926829), 
    ('VB11', 'MVL22', 4.682926829), 
    ('VB11', 'MVR21', 4.682926829), 
    ('VC01', 'MVULVA', 6), 
    ('VC02', 'MVULVA', 10), 
    ('VC03', 'MVULVA', 11), 
    ('VC04', 'MVULVA', 7), 
    ('VC05', 'MVULVA', 2), 
    ('VC06', 'MVULVA', 1), 
    ('VD01', 'MVR05', 3), 
    ('VD01', 'MVL05', 3), 
    ('VD01', 'MVR08', 3), 
    ('VD01', 'MVL08', 3), 
    ('VD02', 'MVL07', 5.5), 
    ('VD02', 'MVR07', 5.5), 
    ('VD02', 'MVL10', 5.5), 
    ('VD02', 'MVR10', 5.5), 
    ('VD03', 'MVL09', 5.75), 
    ('VD03', 'MVR09', 5.75), 
    ('VD03', 'MVL12', 5.75), 
    ('VD03', 'MVR12', 5.75), 
    ('VD04', 'MVL12', 6.25), 
    ('VD04', 'MVR12', 6.25), 
    ('VD04', 'MVL11', 6.25), 
    ('VD04', 'MVR11', 6.25), 
    ('VD05', 'MVL14', 13), 
    ('VD05', 'MVR14', 13), 
    ('VD06', 'MVL14', 4.5), 
    ('VD06', 'MVR14', 4.5), 
    ('VD06', 'MVL13', 4.5), 
    ('VD06', 'MVR13', 4.5), 
    ('VD06', 'MVL16', 4.5), 
    ('VD06', 'MVR16', 4.5), 
    ('VD07', 'MVL16', 4.8), 
    ('VD07', 'MVR16', 4.8), 
    ('VD07', 'MVL15', 4.8), 
    ('VD07', 'MVR15', 4.8), 
    ('VD07', 'MVULVA', 4.8), 
    ('VD08', 'MVL15', 12.5), 
    ('VD08', 'MVR15', 12.5), 
    ('VD09', 'MVL18', 7), 
    ('VD09', 'MVR18', 7), 
    ('VD09', 'MVL17', 7), 
    ('VD09', 'MVR17', 7), 
    ('VD10', 'MVL17', 5.5), 
    ('VD10', 'MVR17', 5.5), 
    ('VD10', 'MVL20', 5.5), 
    ('VD10', 'MVR20', 5.5), 
    ('VD11', 'MVL20', 5.744186047), 
    ('VD11', 'MVR20', 5.744186047), 
    ('VD11', 'MVL19', 5.744186047), 
    ('VD11', 'MVR19', 5.744186047), 
    ('VD12', 'MVL19', 3.25), 
    ('VD12', 'MVR19', 3.25), 
    ('VD12', 'MVL21', 3.25), 
    ('VD12', 'MVR22', 3.25), 
    ('VD13', 'MVL21', 5.744186047), 
    ('VD13', 'MVR22', 5.744186047), 
    ('VD13', 'MVL22', 5.744186047), 
    ('VD13', 'MVR21', 5.744186047), 
    ('VD13', 'MVL23', 5.744186047), 
    ('VD13', 'MVR23', 5.744186047), 
    ('VD13', 'MVR24', 5.744186047), 
    ('VB11', 'MVL23', 4.682926829), 
    ('VB11', 'MVR23', 4.682926829), 
    ('VB11', 'MVR24', 4.682926829), 
    ('VA12', 'MVL23', 4.675675676), 
    ('VA12', 'MVR23', 4.675675676), 
    ('VA12', 'MVR24', 4.675675676), 
    ('DD06', 'MDL24', 4.7), 
    ('DD06', 'MDL23', 4.7), 
    ('DD06', 'MDR24', 4.7), 
    ('DD06', 'MDR23', 4.7), 
    ('DB07', 'MDL24', 2.6), 
    ('DB07', 'MDL23', 2.6), 
    ('DB07', 'MDR24', 2.6), 
    ('DB07', 'MDR23', 2.6), 
    ('DA09', 'MDL24', 4), 
    ('DA09', 'MDL23', 4), 
    ('DA09', 'MDR24', 4), 
    ('DA09', 'MDR23', 4), 
    ('AS11', 'MDL24', 2.708333333), 
    ('AS11', 'MDL23', 2.708333333), 
    ('AS11', 'MDR24', 2.708333333), 
    ('AS11', 'MDR23', 2.708333333)
]

for neuron, muscle, weight in innervationData:
    neuron = network.findNeuron(neuron)
    if neuron != None:
        neuron.innervate(muscles[muscle]).addAttribute('Count', Attribute.DECIMAL_TYPE, weight)
