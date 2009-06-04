# Connectivity and layout from:
#   "Information processing in the primate visual system: an integrated systems perspective."
#   Van Essen DC, Anderson CH, Felleman DJ.
#   Science. 1992 Jan 24;255(5043):419-23. Review.
#   <http://dx.doi.org/10.1126/science.1734518>


# Create the regions

region1 = network.createRegion(abbreviation = 'HC', name = 'Hippocampus')
region2 = network.createRegion(abbreviation = 'ERC', name = 'Entorhinal cortex')
region3 = network.createRegion(abbreviation = '36', name = 'Brodmann area 36')
region4 = network.createRegion(abbreviation = '46', name = 'Brodmann area 46')
region5 = network.createRegion(abbreviation = 'TF', name = 'parahippocampal cortex TF')
region6 = network.createRegion(abbreviation = 'TH', name = 'parahippocampal cortex TH')
region7 = network.createRegion(abbreviation = 'STPa', name = 'STPa')
region8 = network.createRegion(abbreviation = 'AITd', name = 'AITd')
region9 = network.createRegion(abbreviation = 'AITv', name = 'AITv')
region10 = network.createRegion(abbreviation = '7b', name = 'Brodmann area 7b')
region11 = network.createRegion(abbreviation = '7a', name = 'Brodmann area 7a')
region12 = network.createRegion(abbreviation = 'FEF', name = 'Frontal eye field')
region13 = network.createRegion(abbreviation = 'STPp', name = 'STPp')
region14 = network.createRegion(abbreviation = 'CIT Region', name = 'CIT Region')
region15 = network.createRegion(abbreviation = 'CITd', parentRegion = region14, name = 'CITd')
region16 = network.createRegion(abbreviation = 'CIT', parentRegion = region14, name = 'CIT CIT')
region17 = network.createRegion(abbreviation = 'CITv', parentRegion = region14, name = 'CITv')
region18 = network.createRegion(abbreviation = 'VIP', name = 'VIP')
region19 = network.createRegion(abbreviation = 'LIP', name = 'LIP')
region20 = network.createRegion(abbreviation = 'MSTl', name = 'MSTl')
region21 = network.createRegion(abbreviation = 'MSTd', name = 'MSTd')
region22 = network.createRegion(abbreviation = 'FST', name = 'FST')
region23 = network.createRegion(abbreviation = 'PIT Region', name = 'PIT Region')
region24 = network.createRegion(abbreviation = 'PITd', parentRegion = region23, name = 'PITd')
region25 = network.createRegion(abbreviation = 'PIT', parentRegion = region23, name = 'PIT PIT')
region26 = network.createRegion(abbreviation = 'PITv', parentRegion = region23, name = 'PITv')
region27 = network.createRegion(abbreviation = 'DP', name = 'DP')
region28 = network.createRegion(abbreviation = 'VOT', name = 'VOT')
region29 = network.createRegion(abbreviation = 'MDP', name = 'MDP')
region30 = network.createRegion(abbreviation = 'MIP', name = 'MIP')
region31 = network.createRegion(abbreviation = 'PO', name = 'PO')
region32 = network.createRegion(abbreviation = 'MT', name = 'MT')
region33 = network.createRegion(abbreviation = 'V4t', name = 'V4t')
region34 = network.createRegion(abbreviation = 'v4Area', name = 'V4 Region')
region35 = network.createRegion(abbreviation = 'P-B', parentRegion = region34, name = 'P-B V4')
region36 = network.createRegion(abbreviation = 'V4', parentRegion = region34, name = 'V4')
region37 = network.createRegion(abbreviation = 'P-I', parentRegion = region34, name = 'P-I V4')
region38 = network.createRegion(abbreviation = 'PIP', name = 'PIP')
region39 = network.createRegion(abbreviation = 'V3A', name = 'V3A')
region40 = network.createRegion(abbreviation = 'V3', name = 'V3')
region41 = network.createRegion(abbreviation = 'VP', name = 'VP')
region42 = network.createRegion(abbreviation = 'v2Area', name = 'V2 Region')
region43 = network.createRegion(abbreviation = ' M', parentRegion = region42, name = 'M V2')
region44 = network.createRegion(abbreviation = 'V2', parentRegion = region42, name = 'V2')
region45 = network.createRegion(abbreviation = 'P-B', parentRegion = region42, name = 'P-B V2')
region46 = network.createRegion(abbreviation = 'P-I', parentRegion = region42, name = 'P-I V2')
region47 = network.createRegion(abbreviation = 'PULV', name = 'Pulvinar')
region48 = network.createRegion(abbreviation = 'v1Area', name = 'V1 Region')
region49 = network.createRegion(abbreviation = ' M', parentRegion = region48, name = 'Magnocellular V1')
region50 = network.createRegion(abbreviation = 'V1', parentRegion = region48, name = 'V1')
region51 = network.createRegion(abbreviation = 'P-B', parentRegion = region48, name = 'P-B V1')
region52 = network.createRegion(abbreviation = 'P-I', parentRegion = region48, name = 'P-I V1')
region53 = network.createRegion(abbreviation = 'LGN', name = 'Lateral geniculate nucleus')
region54 = network.createRegion(abbreviation = ' M LGN', parentRegion = region53, name = 'Magnocellular LGN')
region55 = network.createRegion(abbreviation = 'I LGN', parentRegion = region53, name = 'I LGN')
region56 = network.createRegion(abbreviation = 'P LGN', parentRegion = region53, name = 'Parvocellular LGN')
region57 = network.createRegion(abbreviation = 'SC', name = 'Superior colliculus')
region58 = network.createRegion(abbreviation = 'Retina', name = 'Retina')
region59 = network.createRegion(abbreviation = ' M Ret', parentRegion = region58, name = 'Magnocellular Retina')
region60 = network.createRegion(abbreviation = 'P Ret', parentRegion = region58, name = 'Parvocellular Retina')
region61 = network.createRegion(abbreviation = 'other', parentRegion = region58, name = 'other Retina')

# Create the pathways

region59.addPathwayToRegion(region54, sendsOutput = True, receivesInput = False)
region60.addPathwayToRegion(region56, sendsOutput = True, receivesInput = False)
region61.addPathwayToRegion(region57, sendsOutput = True, receivesInput = False)
region57.addPathwayToRegion(region55, sendsOutput = True, receivesInput = False)
region57.addPathwayToRegion(region47, sendsOutput = True, receivesInput = False)
region54.addPathwayToRegion(region49, sendsOutput = True, receivesInput = True)
region56.addPathwayToRegion(region51, sendsOutput = True, receivesInput = True)
region56.addPathwayToRegion(region52, sendsOutput = True, receivesInput = True)
region49.addPathwayToRegion(region40, sendsOutput = True, receivesInput = True)
region49.addPathwayToRegion(region32, sendsOutput = True, receivesInput = True)
region49.addPathwayToRegion(region43, sendsOutput = True, receivesInput = False)
region50.addPathwayToRegion(region38, sendsOutput = True, receivesInput = False)
region50.addPathwayToRegion(region31, sendsOutput = True, receivesInput = False)
region50.addPathwayToRegion(region20, sendsOutput = True, receivesInput = False)
region50.addPathwayToRegion(region33, sendsOutput = True, receivesInput = True)
region50.addPathwayToRegion(region39, sendsOutput = True, receivesInput = True)
region50.addPathwayToRegion(region36, sendsOutput = True, receivesInput = True)
region50.addPathwayToRegion(region47, sendsOutput = True, receivesInput = False)
region51.addPathwayToRegion(region45, sendsOutput = True, receivesInput = False)
region52.addPathwayToRegion(region46, sendsOutput = True, receivesInput = False)
region47.addPathwayToRegion(region44, sendsOutput = True, receivesInput = False)
region43.addPathwayToRegion(region40, sendsOutput = True, receivesInput = True)
region43.addPathwayToRegion(region32, sendsOutput = True, receivesInput = True)
region44.addPathwayToRegion(region38, sendsOutput = True, receivesInput = False)
region44.addPathwayToRegion(region31, sendsOutput = True, receivesInput = False)
region44.addPathwayToRegion(region18, sendsOutput = True, receivesInput = False)
region44.addPathwayToRegion(region20, sendsOutput = True, receivesInput = False)
region44.addPathwayToRegion(region21, sendsOutput = True, receivesInput = False)
region44.addPathwayToRegion(region22, sendsOutput = True, receivesInput = True)
region44.addPathwayToRegion(region33, sendsOutput = True, receivesInput = False)
region44.addPathwayToRegion(region28, sendsOutput = True, receivesInput = True)
region44.addPathwayToRegion(region39, sendsOutput = True, receivesInput = True)
region44.addPathwayToRegion(region41, sendsOutput = True, receivesInput = True)
region45.addPathwayToRegion(region35, sendsOutput = True, receivesInput = True)
region46.addPathwayToRegion(region37, sendsOutput = True, receivesInput = True)
region40.addPathwayToRegion(region44, sendsOutput = True, receivesInput = False)
region40.addPathwayToRegion(region18, sendsOutput = True, receivesInput = False)
region40.addPathwayToRegion(region38, sendsOutput = True, receivesInput = False)
region40.addPathwayToRegion(region19, sendsOutput = True, receivesInput = False)
region40.addPathwayToRegion(region21, sendsOutput = True, receivesInput = False)
region40.addPathwayToRegion(region12, sendsOutput = True, receivesInput = False)
region40.addPathwayToRegion(region22, sendsOutput = True, receivesInput = True)
region40.addPathwayToRegion(region33, sendsOutput = True, receivesInput = True)
region40.addPathwayToRegion(region32, sendsOutput = True, receivesInput = True)
region40.addPathwayToRegion(region36, sendsOutput = True, receivesInput = True)
region40.addPathwayToRegion(region39, sendsOutput = True, receivesInput = True)
region40.addPathwayToRegion(region5, sendsOutput = True, receivesInput = False)
region40.addPathwayToRegion(region41, sendsOutput = True, receivesInput = True)
region41.addPathwayToRegion(region32, sendsOutput = True, receivesInput = True)
region41.addPathwayToRegion(region38, sendsOutput = True, receivesInput = False)
region41.addPathwayToRegion(region18, sendsOutput = True, receivesInput = False)
region41.addPathwayToRegion(region31, sendsOutput = True, receivesInput = False)
region41.addPathwayToRegion(region21, sendsOutput = True, receivesInput = False)
region41.addPathwayToRegion(region19, sendsOutput = True, receivesInput = False)
region41.addPathwayToRegion(region22, sendsOutput = True, receivesInput = True)
region41.addPathwayToRegion(region28, sendsOutput = True, receivesInput = True)
region41.addPathwayToRegion(region12, sendsOutput = True, receivesInput = False)
region41.addPathwayToRegion(region36, sendsOutput = True, receivesInput = False)
region41.addPathwayToRegion(region39, sendsOutput = True, receivesInput = True)
region41.addPathwayToRegion(region5, sendsOutput = True, receivesInput = False)
region39.addPathwayToRegion(region36, sendsOutput = True, receivesInput = True)
region39.addPathwayToRegion(region32, sendsOutput = True, receivesInput = True)
region39.addPathwayToRegion(region22, sendsOutput = True, receivesInput = True)
region39.addPathwayToRegion(region21, sendsOutput = True, receivesInput = False)
region39.addPathwayToRegion(region20, sendsOutput = True, receivesInput = False)
region39.addPathwayToRegion(region31, sendsOutput = True, receivesInput = False)
region39.addPathwayToRegion(region27, sendsOutput = True, receivesInput = False)
region39.addPathwayToRegion(region12, sendsOutput = True, receivesInput = False)
region39.addPathwayToRegion(region19, sendsOutput = True, receivesInput = False)
region29.addPathwayToRegion(region11, sendsOutput = True, receivesInput = False)
region29.addPathwayToRegion(region31, sendsOutput = True, receivesInput = False)
region36.addPathwayToRegion(region33, sendsOutput = True, receivesInput = True)
region36.addPathwayToRegion(region32, sendsOutput = True, receivesInput = True)
region36.addPathwayToRegion(region22, sendsOutput = True, receivesInput = True)
region36.addPathwayToRegion(region24, sendsOutput = True, receivesInput = True)
region36.addPathwayToRegion(region26, sendsOutput = True, receivesInput = True)
region36.addPathwayToRegion(region15, sendsOutput = True, receivesInput = True)
region36.addPathwayToRegion(region17, sendsOutput = True, receivesInput = True)
region36.addPathwayToRegion(region9, sendsOutput = True, receivesInput = True)
region36.addPathwayToRegion(region5, sendsOutput = True, receivesInput = True)
region36.addPathwayToRegion(region6, sendsOutput = True, receivesInput = True)
region36.addPathwayToRegion(region38, sendsOutput = True, receivesInput = True)
region36.addPathwayToRegion(region19, sendsOutput = True, receivesInput = True)
region36.addPathwayToRegion(region27, sendsOutput = True, receivesInput = True)
region36.addPathwayToRegion(region4, sendsOutput = True, receivesInput = False)
region36.addPathwayToRegion(region28, sendsOutput = True, receivesInput = True)
region28.addPathwayToRegion(region24, sendsOutput = True, receivesInput = False)
region28.addPathwayToRegion(region26, sendsOutput = True, receivesInput = False)
region33.addPathwayToRegion(region32, sendsOutput = True, receivesInput = True)
region33.addPathwayToRegion(region22, sendsOutput = True, receivesInput = True)
region33.addPathwayToRegion(region20, sendsOutput = True, receivesInput = True)
region33.addPathwayToRegion(region31, sendsOutput = True, receivesInput = False)
region33.addPathwayToRegion(region21, sendsOutput = True, receivesInput = True)
region33.addPathwayToRegion(region12, sendsOutput = True, receivesInput = False)
region32.addPathwayToRegion(region22, sendsOutput = True, receivesInput = True)
region32.addPathwayToRegion(region21, sendsOutput = True, receivesInput = True)
region32.addPathwayToRegion(region20, sendsOutput = True, receivesInput = True)
region32.addPathwayToRegion(region31, sendsOutput = True, receivesInput = True)
region32.addPathwayToRegion(region38, sendsOutput = True, receivesInput = True)
region32.addPathwayToRegion(region19, sendsOutput = True, receivesInput = True)
region32.addPathwayToRegion(region18, sendsOutput = True, receivesInput = True)
region32.addPathwayToRegion(region12, sendsOutput = True, receivesInput = True)
region32.addPathwayToRegion(region4, sendsOutput = True, receivesInput = False)
region22.addPathwayToRegion(region25, sendsOutput = True, receivesInput = True)
region22.addPathwayToRegion(region13, sendsOutput = True, receivesInput = True)
region22.addPathwayToRegion(region5, sendsOutput = True, receivesInput = True)
region22.addPathwayToRegion(region6, sendsOutput = True, receivesInput = False)
region22.addPathwayToRegion(region21, sendsOutput = True, receivesInput = True)
region22.addPathwayToRegion(region20, sendsOutput = True, receivesInput = True)
region22.addPathwayToRegion(region19, sendsOutput = True, receivesInput = True)
region22.addPathwayToRegion(region18, sendsOutput = True, receivesInput = True)
region22.addPathwayToRegion(region12, sendsOutput = True, receivesInput = True)
region22.addPathwayToRegion(region11, sendsOutput = True, receivesInput = False)
region24.addPathwayToRegion(region17, sendsOutput = True, receivesInput = True)
region24.addPathwayToRegion(region8, sendsOutput = True, receivesInput = True)
region24.addPathwayToRegion(region9, sendsOutput = True, receivesInput = True)
region25.addPathwayToRegion(region21, sendsOutput = True, receivesInput = True)
region25.addPathwayToRegion(region12, sendsOutput = True, receivesInput = False)
region25.addPathwayToRegion(region4, sendsOutput = True, receivesInput = False)
region26.addPathwayToRegion(region17, sendsOutput = True, receivesInput = True)
region26.addPathwayToRegion(region8, sendsOutput = True, receivesInput = True)
region26.addPathwayToRegion(region9, sendsOutput = True, receivesInput = True)
region26.addPathwayToRegion(region6, sendsOutput = True, receivesInput = True)
region26.addPathwayToRegion(region5, sendsOutput = True, receivesInput = True)
region15.addPathwayToRegion(region8, sendsOutput = True, receivesInput = True)
region15.addPathwayToRegion(region9, sendsOutput = True, receivesInput = True)
region16.addPathwayToRegion(region12, sendsOutput = True, receivesInput = True)
region16.addPathwayToRegion(region4, sendsOutput = True, receivesInput = True)
region17.addPathwayToRegion(region8, sendsOutput = True, receivesInput = True)
region17.addPathwayToRegion(region9, sendsOutput = True, receivesInput = True)
region17.addPathwayToRegion(region5, sendsOutput = True, receivesInput = True)
region8.addPathwayToRegion(region7, sendsOutput = True, receivesInput = True)
region8.addPathwayToRegion(region11, sendsOutput = True, receivesInput = True)
region8.addPathwayToRegion(region4, sendsOutput = True, receivesInput = True)
region8.addPathwayToRegion(region12, sendsOutput = True, receivesInput = True)
region9.addPathwayToRegion(region6, sendsOutput = True, receivesInput = True)
region9.addPathwayToRegion(region5, sendsOutput = True, receivesInput = True)
region13.addPathwayToRegion(region7, sendsOutput = True, receivesInput = True)
region13.addPathwayToRegion(region5, sendsOutput = True, receivesInput = True)
region13.addPathwayToRegion(region6, sendsOutput = True, receivesInput = True)
region13.addPathwayToRegion(region21, sendsOutput = True, receivesInput = True)
region13.addPathwayToRegion(region20, sendsOutput = True, receivesInput = True)
region13.addPathwayToRegion(region12, sendsOutput = True, receivesInput = True)
region13.addPathwayToRegion(region4, sendsOutput = True, receivesInput = True)
region7.addPathwayToRegion(region5, sendsOutput = True, receivesInput = True)
region7.addPathwayToRegion(region6, sendsOutput = True, receivesInput = True)
region7.addPathwayToRegion(region4, sendsOutput = True, receivesInput = True)
region5.addPathwayToRegion(region21, sendsOutput = True, receivesInput = True)
region5.addPathwayToRegion(region11, sendsOutput = True, receivesInput = True)
region5.addPathwayToRegion(region3, sendsOutput = True, receivesInput = True)
region5.addPathwayToRegion(region4, sendsOutput = True, receivesInput = True)
region5.addPathwayToRegion(region2, sendsOutput = True, receivesInput = True)
region6.addPathwayToRegion(region11, sendsOutput = True, receivesInput = True)
region6.addPathwayToRegion(region3, sendsOutput = True, receivesInput = True)
region6.addPathwayToRegion(region4, sendsOutput = True, receivesInput = True)
region6.addPathwayToRegion(region2, sendsOutput = True, receivesInput = True)
region21.addPathwayToRegion(region31, sendsOutput = True, receivesInput = True)
region21.addPathwayToRegion(region19, sendsOutput = True, receivesInput = True)
region21.addPathwayToRegion(region18, sendsOutput = True, receivesInput = True)
region21.addPathwayToRegion(region27, sendsOutput = True, receivesInput = True)
region21.addPathwayToRegion(region11, sendsOutput = True, receivesInput = True)
region21.addPathwayToRegion(region12, sendsOutput = True, receivesInput = True)
region20.addPathwayToRegion(region31, sendsOutput = True, receivesInput = True)
region20.addPathwayToRegion(region19, sendsOutput = True, receivesInput = True)
region20.addPathwayToRegion(region18, sendsOutput = True, receivesInput = True)
region20.addPathwayToRegion(region27, sendsOutput = True, receivesInput = True)
region20.addPathwayToRegion(region11, sendsOutput = True, receivesInput = True)
region20.addPathwayToRegion(region12, sendsOutput = True, receivesInput = True)
region31.addPathwayToRegion(region19, sendsOutput = True, receivesInput = True)
region31.addPathwayToRegion(region18, sendsOutput = True, receivesInput = True)
region31.addPathwayToRegion(region38, sendsOutput = True, receivesInput = True)
region31.addPathwayToRegion(region30, sendsOutput = True, receivesInput = True)
region31.addPathwayToRegion(region27, sendsOutput = True, receivesInput = True)
region31.addPathwayToRegion(region11, sendsOutput = True, receivesInput = True)
region31.addPathwayToRegion(region12, sendsOutput = True, receivesInput = True)
region38.addPathwayToRegion(region27, sendsOutput = True, receivesInput = True)
region38.addPathwayToRegion(region19, sendsOutput = True, receivesInput = True)
region38.addPathwayToRegion(region11, sendsOutput = True, receivesInput = True)
region19.addPathwayToRegion(region18, sendsOutput = True, receivesInput = True)
region19.addPathwayToRegion(region27, sendsOutput = True, receivesInput = True)
region19.addPathwayToRegion(region11, sendsOutput = True, receivesInput = True)
region19.addPathwayToRegion(region12, sendsOutput = True, receivesInput = True)
region19.addPathwayToRegion(region4, sendsOutput = True, receivesInput = True)
region18.addPathwayToRegion(region11, sendsOutput = True, receivesInput = True)
region18.addPathwayToRegion(region12, sendsOutput = True, receivesInput = True)
region30.addPathwayToRegion(region11, sendsOutput = True, receivesInput = False)
region27.addPathwayToRegion(region11, sendsOutput = True, receivesInput = True)
region27.addPathwayToRegion(region12, sendsOutput = True, receivesInput = True)
region27.addPathwayToRegion(region3, sendsOutput = True, receivesInput = True)
region27.addPathwayToRegion(region4, sendsOutput = True, receivesInput = True)
region11.addPathwayToRegion(region12, sendsOutput = True, receivesInput = True)
region11.addPathwayToRegion(region3, sendsOutput = True, receivesInput = True)
region11.addPathwayToRegion(region4, sendsOutput = True, receivesInput = True)
region11.addPathwayToRegion(region10, sendsOutput = True, receivesInput = True)
region12.addPathwayToRegion(region4, sendsOutput = True, receivesInput = True)
region4.addPathwayToRegion(region3, sendsOutput = True, receivesInput = True)
region4.addPathwayToRegion(region2, sendsOutput = True, receivesInput = True)
region3.addPathwayToRegion(region2, sendsOutput = True, receivesInput = True)
region10.addPathwayToRegion(region3, sendsOutput = True, receivesInput = True)
region2.addPathwayToRegion(region1, sendsOutput = True, receivesInput = True)

# Create a display

display.setBackgroundColor((0.72156900000000002, 0.76862699999999995, 0.80000000000000004, 1.0))
display.setDefaultFlowColor((0.0, 0.0, 0.0, 1.0))
display.setDefaultFlowSpread(0.1)
display.setViewDimensions(2)
display.setShowRegionNames(True)
display.setShowNeuronNames(False)
display.setShowFlow(False)
display.setUseGhosts(True)
display.setUseMouseOverSelecting(False)

display.setVisiblePosition(region1, (0.0, 0.0, 0.0), fixed = True)
display.setVisibleSize(region1, (0.050000000000000003, 0.029999999999999999, 0.10000000000000001))
display.setVisibleColor(region1, (0.98039215686299996, 0.87450980392199995, 1.0))
display.setVisiblePosition(region2, (0.0, -0.050000000000000003, 0.0), fixed = True)
display.setVisibleSize(region2, (0.050000000000000003, 0.029999999999999999, 0.10000000000000001))
display.setVisibleColor(region2, (0.93333333333299995, 0.93333333333299995, 1.0))
display.setVisiblePosition(region3, (-0.14999999999999999, -0.10000000000000001, 0.0), fixed = True)
display.setVisibleSize(region3, (0.050000000000000003, 0.029999999999999999, 0.10000000000000001))
display.setVisibleColor(region3, (0.89803921568599998, 1.0, 0.81568627450999998))
display.setVisiblePosition(region4, (-0.050000000000000003, -0.10000000000000001, 0.0), fixed = True)
display.setVisibleSize(region4, (0.050000000000000003, 0.029999999999999999, 0.10000000000000001))
display.setVisibleColor(region4, (0.50196078431400004, 0.14509803921600001, 0.16078431372499999))
display.setVisiblePosition(region5, (0.050000000000000003, -0.10000000000000001, 0.0), fixed = True)
display.setVisibleSize(region5, (0.050000000000000003, 0.029999999999999999, 0.10000000000000001))
display.setVisibleColor(region5, (0.52156862745099997, 0.58431372549000005, 1.0))
display.setVisiblePosition(region6, (0.14999999999999999, -0.10000000000000001, 0.0), fixed = True)
display.setVisibleSize(region6, (0.050000000000000003, 0.029999999999999999, 0.10000000000000001))
display.setVisibleColor(region6, (0.57254901960799998, 0.67058823529400002, 1.0))
display.setVisiblePosition(region7, (0.070000000000000007, -0.14999999999999999, 0.0), fixed = True)
display.setVisibleSize(region7, (0.050000000000000003, 0.029999999999999999, 0.10000000000000001))
display.setVisibleColor(region7, (1.0, 0.80784313725500001, 0.72156862745100003))
display.setVisiblePosition(region8, (0.14999999999999999, -0.14999999999999999, 0.0), fixed = True)
display.setVisibleSize(region8, (0.050000000000000003, 0.029999999999999999, 0.10000000000000001))
display.setVisibleColor(region8, (0.67058823529400002, 1.0, 0.69019607843099995))
display.setVisiblePosition(region9, (0.23000000000000001, -0.14999999999999999, 0.0), fixed = True)
display.setVisibleSize(region9, (0.050000000000000003, 0.029999999999999999, 0.10000000000000001))
display.setVisibleColor(region9, (0.56862745098, 0.47058823529400001, 1.0))
display.setVisiblePosition(region10, (-0.25, -0.20000000000000001, 0.0), fixed = True)
display.setVisibleSize(region10, (0.050000000000000003, 0.029999999999999999, 0.10000000000000001))
display.setVisibleColor(region10, (1.0, 0.90980392156900003, 0.83137254902000002))
display.setVisiblePosition(region11, (-0.14999999999999999, -0.20000000000000001, 0.0), fixed = True)
display.setVisibleSize(region11, (0.050000000000000003, 0.029999999999999999, 0.10000000000000001))
display.setVisibleColor(region11, (1.0, 0.75294117647100001, 0.38039215686299999))
display.setVisiblePosition(region12, (-0.050000000000000003, -0.20000000000000001, 0.0), fixed = True)
display.setVisibleSize(region12, (0.050000000000000003, 0.029999999999999999, 0.10000000000000001))
display.setVisibleColor(region12, (0.513725490196, 0.55294117647100005, 0.64705882352900002))
display.setVisiblePosition(region13, (0.050000000000000003, -0.20000000000000001, 0.0), fixed = True)
display.setVisibleSize(region13, (0.050000000000000003, 0.029999999999999999, 0.10000000000000001))
display.setVisibleColor(region13, (1.0, 0.75294117647100001, 0.38039215686299999))
display.setVisiblePosition(region14, (0.20000000000000001, -0.20000000000000001, 0.0), fixed = True)
display.setVisibleSize(region14, (0.20000000000000001, 0.029999999999999999, 0.10000000000000001))
display.setLabel(region14, '')
display.setVisibleColor(region14, (0.811764705882, 0.86666666666699999, 1.0))
display.setArrangedAxis(region14, 'largest')
display.setArrangedSpacing(region14, 0.01)
display.setVisiblePosition(region15, (-0.32999999999999996, 0.0, 0.0), fixed = True)
display.setVisibleSize(region15, (0.32000000000000001, 0.8666666666666667, 0.95999999999999996), absolute = False)
display.setVisibleColor(region15, (0.65882352941199995, 0.81568627450999998, 1.0))
display.setVisiblePosition(region16, (2.7755575615628914e-17, 0.0, 0.0), fixed = True)
display.setVisibleSize(region16, (0.32000000000000001, 0.8666666666666667, 0.95999999999999996), absolute = False)
display.setVisibleColor(region16, (0.65882352941199995, 0.81568627450999998, 1.0))
display.setVisiblePosition(region17, (0.33000000000000007, 0.0, 0.0), fixed = True)
display.setVisibleSize(region17, (0.32000000000000001, 0.8666666666666667, 0.95999999999999996), absolute = False)
display.setVisibleColor(region17, (0.65882352941199995, 0.81568627450999998, 1.0))
display.setVisiblePosition(region18, (-0.34999999999999998, -0.25, 0.0), fixed = True)
display.setVisibleSize(region18, (0.050000000000000003, 0.029999999999999999, 0.10000000000000001))
display.setVisibleColor(region18, (1.0, 0.52941176470600004, 0.26274509803899998))
display.setVisiblePosition(region19, (-0.25, -0.25, 0.0), fixed = True)
display.setVisibleSize(region19, (0.050000000000000003, 0.029999999999999999, 0.10000000000000001))
display.setVisibleColor(region19, (1.0, 0.93333333333299995, 0.65098039215699999))
display.setVisiblePosition(region20, (-0.14999999999999999, -0.25, 0.0), fixed = True)
display.setVisibleSize(region20, (0.050000000000000003, 0.029999999999999999, 0.10000000000000001))
display.setVisibleColor(region20, (1.0, 0.52941176470600004, 0.26274509803899998))
display.setVisiblePosition(region21, (-0.050000000000000003, -0.25, 0.0), fixed = True)
display.setVisibleSize(region21, (0.050000000000000003, 0.029999999999999999, 0.10000000000000001))
display.setVisibleColor(region21, (1.0, 0.109803921569, 0.90588235294099995))
display.setVisiblePosition(region22, (0.050000000000000003, -0.25, 0.0), fixed = True)
display.setVisibleSize(region22, (0.050000000000000003, 0.029999999999999999, 0.10000000000000001))
display.setVisibleColor(region22, (1.0, 0.75294117647100001, 0.38039215686299999))
display.setVisiblePosition(region23, (0.20000000000000001, -0.25, 0.0), fixed = True)
display.setVisibleSize(region23, (0.20000000000000001, 0.029999999999999999, 0.10000000000000001))
display.setLabel(region23, '')
display.setVisibleColor(region23, (0.811764705882, 0.86666666666699999, 1.0))
display.setArrangedAxis(region23, 'largest')
display.setArrangedSpacing(region23, 0.01)
display.setVisiblePosition(region24, (-0.32999999999999996, 0.0, 0.0), fixed = True)
display.setVisibleSize(region24, (0.32000000000000001, 0.8666666666666667, 0.95999999999999996), absolute = False)
display.setVisibleColor(region24, (0.59607843137299998, 0.69803921568600003, 1.0))
display.setVisiblePosition(region25, (2.7755575615628914e-17, 0.0, 0.0), fixed = True)
display.setVisibleSize(region25, (0.32000000000000001, 0.8666666666666667, 0.95999999999999996), absolute = False)
display.setVisibleColor(region25, (0.59607843137299998, 0.69803921568600003, 1.0))
display.setVisiblePosition(region26, (0.33000000000000007, 0.0, 0.0), fixed = True)
display.setVisibleSize(region26, (0.32000000000000001, 0.8666666666666667, 0.95999999999999996), absolute = False)
display.setVisibleColor(region26, (0.59607843137299998, 0.69803921568600003, 1.0))
display.setVisiblePosition(region27, (-0.20000000000000001, -0.29999999999999999, 0.0), fixed = True)
display.setVisibleSize(region27, (0.050000000000000003, 0.029999999999999999, 0.10000000000000001))
display.setVisibleColor(region27, (1.0, 0.50588235294100004, 0.78431372549))
display.setVisiblePosition(region28, (0.29999999999999999, -0.29999999999999999, 0.0), fixed = True)
display.setVisibleSize(region28, (0.050000000000000003, 0.029999999999999999, 0.10000000000000001))
display.setVisibleColor(region28, (0.30588235294100002, 0.36078431372500003, 1.0))
display.setVisiblePosition(region29, (-0.34999999999999998, -0.34999999999999998, 0.0))
display.setVisibleSize(region29, (0.050000000000000003, 0.029999999999999999, 0.10000000000000001))
display.setVisibleColor(region29, (1.0, 0.37647058823500001, 0.52941176470600004))
display.setVisiblePosition(region30, (-0.25, -0.34999999999999998, 0.0), fixed = True)
display.setVisibleSize(region30, (0.050000000000000003, 0.029999999999999999, 0.10000000000000001))
display.setVisibleColor(region30, (1.0, 0.38431372548999998, 0.66666666666700003))
display.setVisiblePosition(region31, (-0.14999999999999999, -0.34999999999999998, 0.0), fixed = True)
display.setVisibleSize(region31, (0.050000000000000003, 0.029999999999999999, 0.10000000000000001))
display.setVisibleColor(region31, (1.0, 0.38431372548999998, 0.66666666666700003))
display.setVisiblePosition(region32, (-0.050000000000000003, -0.34999999999999998, 0.0), fixed = True)
display.setVisibleSize(region32, (0.050000000000000003, 0.029999999999999999, 0.10000000000000001))
display.setVisibleColor(region32, (1.0, 0.078431372548999997, 0.61960784313700001))
display.setVisiblePosition(region33, (0.050000000000000003, -0.34999999999999998, 0.0), fixed = True)
display.setVisibleSize(region33, (0.050000000000000003, 0.029999999999999999, 0.10000000000000001))
display.setVisibleColor(region33, (1.0, 0.65882352941199995, 0.73725490196099996))
display.setVisiblePosition(region34, (0.25, -0.34999999999999998, 0.0), fixed = True)
display.setVisibleSize(region34, (0.20000000000000001, 0.029999999999999999, 0.10000000000000001))
display.setLabel(region34, '')
display.setVisibleColor(region34, (0.811764705882, 0.86666666666699999, 1.0))
display.setArrangedAxis(region34, 'largest')
display.setArrangedSpacing(region34, 0.01)
display.setVisiblePosition(region35, (-0.32999999999999996, 0.0, 0.0), fixed = True)
display.setVisibleSize(region35, (0.32000000000000001, 0.8666666666666667, 0.95999999999999996), absolute = False)
display.setVisibleColor(region35, (0.23529411764700001, 0.31764705882400002, 1.0))
display.setVisiblePosition(region36, (2.7755575615628914e-17, 0.0, 0.0), fixed = True)
display.setVisibleSize(region36, (0.32000000000000001, 0.8666666666666667, 0.95999999999999996), absolute = False)
display.setVisibleColor(region36, (0.23529411764700001, 0.31764705882400002, 1.0))
display.setVisiblePosition(region37, (0.33000000000000007, 0.0, 0.0), fixed = True)
display.setVisibleSize(region37, (0.32000000000000001, 0.8666666666666667, 0.95999999999999996), absolute = False)
display.setVisibleColor(region37, (0.23529411764700001, 0.31764705882400002, 1.0))
display.setVisiblePosition(region38, (-0.14999999999999999, -0.40000000000000002, 0.0), fixed = True)
display.setVisibleSize(region38, (0.050000000000000003, 0.029999999999999999, 0.10000000000000001))
display.setVisibleColor(region38, (1.0, 0.43137254902, 0.57647058823499997))
display.setVisiblePosition(region39, (0.25, -0.40000000000000002, 0.0), fixed = True)
display.setVisibleSize(region39, (0.050000000000000003, 0.029999999999999999, 0.10000000000000001))
display.setVisibleColor(region39, (0.84313725490199998, 0.36078431372500003, 1.0))
display.setVisiblePosition(region40, (-0.10000000000000001, -0.45000000000000001, 0.0), fixed = True)
display.setVisibleSize(region40, (0.050000000000000003, 0.029999999999999999, 0.10000000000000001))
display.setVisibleColor(region40, (1.0, 0.44313725490200001, 0.44313725490200001))
display.setVisiblePosition(region41, (0.20000000000000001, -0.45000000000000001, 0.0), fixed = True)
display.setVisibleSize(region41, (0.050000000000000003, 0.029999999999999999, 0.10000000000000001))
display.setVisibleColor(region41, (0.674509803922, 0.37254901960800002, 1.0))
display.setVisiblePosition(region42, (-0.050000000000000003, -0.5, 0.0), fixed = True)
display.setVisibleSize(region42, (0.29999999999999999, 0.029999999999999999, 0.10000000000000001))
display.setLabel(region42, '')
display.setVisibleColor(region42, (0.811764705882, 0.86666666666699999, 1.0))
display.setArrangedAxis(region42, 'largest')
display.setArrangedSpacing(region42, 0.005)
display.setVisiblePosition(region43, (-0.37312499999999998, 0.0, 0.0), fixed = True)
display.setVisibleSize(region43, (0.24374999999999999, 0.90000000000000002, 0.96999999999999997), absolute = False)
display.setVisibleColor(region43, (1.0, 0.41176470588199998, 0.58823529411800002))
display.setVisiblePosition(region44, (-0.124375, 0.0, 0.0), fixed = True)
display.setVisibleSize(region44, (0.24374999999999999, 0.90000000000000002, 0.96999999999999997), absolute = False)
display.setVisibleColor(region44, (1.0, 0.41176470588199998, 0.58823529411800002))
display.setVisiblePosition(region45, (0.124375, 0.0, 0.0), fixed = True)
display.setVisibleSize(region45, (0.24374999999999999, 0.90000000000000002, 0.96999999999999997), absolute = False)
display.setVisibleColor(region45, (1.0, 0.41176470588199998, 0.58823529411800002))
display.setVisiblePosition(region46, (0.37312499999999998, 0.0, 0.0), fixed = True)
display.setVisibleSize(region46, (0.24374999999999999, 0.90000000000000002, 0.96999999999999997), absolute = False)
display.setVisibleColor(region46, (1.0, 0.41176470588199998, 0.58823529411800002))
display.setVisiblePosition(region47, (0.25, -0.55000000000000004, 0.0), fixed = True)
display.setVisibleSize(region47, (0.050000000000000003, 0.029999999999999999, 0.10000000000000001))
display.setVisibleColor(region47, (0.701960784314, 0.701960784314, 0.701960784314))
display.setVisiblePosition(region48, (-0.050000000000000003, -0.59999999999999998, 0.0), fixed = True)
display.setVisibleSize(region48, (0.29999999999999999, 0.029999999999999999, 0.10000000000000001))
display.setLabel(region48, '')
display.setVisibleColor(region48, (0.811764705882, 0.86666666666699999, 1.0))
display.setArrangedAxis(region48, 'largest')
display.setArrangedSpacing(region48, 0.005)
display.setVisiblePosition(region49, (-0.37312499999999998, 0.0, 0.0), fixed = True)
display.setVisibleSize(region49, (0.24374999999999999, 0.90000000000000002, 0.96999999999999997), absolute = False)
display.setVisibleColor(region49, (1.0, 0.23137254902000001, 0.42745098039200002))
display.setVisiblePosition(region50, (-0.124375, 0.0, 0.0), fixed = True)
display.setVisibleSize(region50, (0.24374999999999999, 0.90000000000000002, 0.96999999999999997), absolute = False)
display.setVisibleColor(region50, (1.0, 0.23137254902000001, 0.42745098039200002))
display.setVisiblePosition(region51, (0.124375, 0.0, 0.0), fixed = True)
display.setVisibleSize(region51, (0.24374999999999999, 0.90000000000000002, 0.96999999999999997), absolute = False)
display.setVisibleColor(region51, (1.0, 0.23137254902000001, 0.42745098039200002))
display.setVisiblePosition(region52, (0.37312499999999998, 0.0, 0.0), fixed = True)
display.setVisibleSize(region52, (0.24374999999999999, 0.90000000000000002, 0.96999999999999997), absolute = False)
display.setVisibleColor(region52, (1.0, 0.23137254902000001, 0.42745098039200002))
display.setVisiblePosition(region53, (-0.050000000000000003, -0.65000000000000002, 0.0), fixed = True)
display.setVisibleSize(region53, (0.29999999999999999, 0.029999999999999999, 0.10000000000000001))
display.setLabel(region53, '')
display.setVisibleColor(region53, (0.811764705882, 0.86666666666699999, 1.0))
display.setArrangedAxis(region53, 'largest')
display.setArrangedSpacing(region53, 0.005)
display.setVisiblePosition(region54, (-0.33166666666666667, 0.0, 0.0), fixed = True)
display.setVisibleSize(region54, (0.32666666666666666, 0.90000000000000002, 0.96999999999999997), absolute = False)
display.setVisibleColor(region54, (0.59999999999999998, 0.59999999999999998, 0.59999999999999998))
display.setVisiblePosition(region55, (0.0, 0.0, 0.0), fixed = True)
display.setVisibleSize(region55, (0.32666666666666666, 0.90000000000000002, 0.96999999999999997), absolute = False)
display.setVisibleColor(region55, (0.59999999999999998, 0.59999999999999998, 0.59999999999999998))
display.setVisiblePosition(region56, (0.33166666666666667, 0.0, 0.0), fixed = True)
display.setVisibleSize(region56, (0.32666666666666666, 0.90000000000000002, 0.96999999999999997), absolute = False)
display.setVisibleColor(region56, (0.59999999999999998, 0.59999999999999998, 0.59999999999999998))
display.setVisiblePosition(region57, (0.25, -0.69999999999999996, 0.0), fixed = True)
display.setVisibleSize(region57, (0.050000000000000003, 0.029999999999999999, 0.10000000000000001))
display.setVisibleColor(region57, (0.59999999999999998, 0.59999999999999998, 0.59999999999999998))
display.setVisiblePosition(region58, (-0.050000000000000003, -0.75, 0.0))
display.setVisibleSize(region58, (0.29999999999999999, 0.029999999999999999, 0.10000000000000001))
display.setLabel(region58, '')
display.setVisibleColor(region58, (0.811764705882, 0.86666666666699999, 1.0))
display.setArrangedAxis(region58, 'largest')
display.setArrangedSpacing(region58, 0.005)
display.setVisiblePosition(region59, (-0.33166666666666667, 0.0, 0.0), fixed = True)
display.setVisibleSize(region59, (0.32666666666666666, 0.90000000000000002, 0.96999999999999997), absolute = False)
display.setVisibleColor(region59, (0.72156862745100003, 0.72156862745100003, 0.72156862745100003))
display.setVisiblePosition(region60, (0.0, 0.0, 0.0), fixed = True)
display.setVisibleSize(region60, (0.32666666666666666, 0.90000000000000002, 0.96999999999999997), absolute = False)
display.setVisibleColor(region60, (0.72156862745100003, 0.72156862745100003, 0.72156862745100003))
display.setVisiblePosition(region61, (0.33166666666666667, 0.0, 0.0), fixed = True)
display.setVisibleSize(region61, (0.32666666666666666, 0.90000000000000002, 0.96999999999999997), absolute = False)
display.setVisibleColor(region61, (0.72156862745100003, 0.72156862745100003, 0.72156862745100003))

for pathway in network.pathways():
	display.setVisibleColor(pathway, (1.0, 1.0, 1.0))
	display.setVisibleWeight(pathway, 1.0)
	display.setVisibleTexture(pathway, None)

display.centerView()
