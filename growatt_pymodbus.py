# import the server implementation
import time
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
 
# choose the serial client
client = ModbusClient(method='rtu', port='COM1', baudrate=9600, stopbits=1, parity='N', bytesize=8, timeout=1)
while 1:
    client.connect()
    #read_input_register(address, lenght, slave_address)
    #Lectura de variables modbus
    # SPH Mode
    rr = client.read_input_registers(0,1, unit = 1)
    sphState=float(rr.registers[0])
    rr = client.read_input_registers(118,1, unit = 1)
    priority=float(rr.registers[0])
    rr = client.read_input_registers(119,1, unit = 1)
    BatType=float(rr.registers[0])
    rr = client.read_input_registers(1000,1, unit = 1)
    SysMode=float(rr.registers[0])
    # Solar panel 1
    rr = client.read_input_registers(3,1, unit = 1)
    pv1_volts=float(rr.registers[0])*0.1
    rr = client.read_input_registers(4,1, unit = 1)
    pv1_current=float(rr.registers[0])*0.1
    rr = client.read_input_registers(5,2, unit = 1)
    pv1_W=float((rr.registers[0]<<16)|(rr.registers[1]))*0.1
    # Solar panel 2
    rr = client.read_input_registers(7,1, unit = 1)
    pv2_volts=float(rr.registers[0])*0.1
    rr = client.read_input_registers(8,1, unit = 1)
    pv2_current=float(rr.registers[0])*0.1
    rr = client.read_input_registers(9,2, unit = 1)
    pv2_W=float((rr.registers[0]<<16)|(rr.registers[1]))*0.1
    # Solar panel 3
    rr = client.read_input_registers(11,1, unit = 1)
    pv3_volts=float(rr.registers[0])*0.1
    rr = client.read_input_registers(12,1, unit = 1)
    pv3_current=float(rr.registers[0])*0.1
    rr = client.read_input_registers(13,2, unit = 1)
    pv3_W=float((rr.registers[0]<<16)|(rr.registers[1]))*0.1

    # Inverter temperature 
    rr = client.read_input_registers(93,1, unit = 1)
    temp=float(rr.registers[0])*0.1
    rr = client.read_input_registers(94,1, unit = 1)
    tempIPM=float(rr.registers[0])*0.1
    rr = client.read_input_registers(95,1, unit = 1)
    tempB=float(rr.registers[0])*0.1

    #Output power 
    rr = client.read_input_registers(101,1, unit = 1)
    ROutPow=float(rr.registers[0])
    rr = client.read_input_registers(102,1, unit = 1)
    OutMPow=float(rr.registers[0])*0.1
    ## Grid message 
    # Phase A
    rr = client.read_input_registers(38,1, unit = 1)
    GridAVol=float(rr.registers[0])*0.1
    rr = client.read_input_registers(39,1, unit = 1)
    GridACur=float(rr.registers[0])*0.1
    rr = client.read_input_registers(40,2, unit = 1)
    GridAPow=float((rr.registers[0]<<16)|(rr.registers[1]))*0.1

    # Phase B
    rr = client.read_input_registers(42,1, unit = 1)
    GridBVol=float(rr.registers[0])*0.1
    rr = client.read_input_registers(43,1, unit = 1)
    GridBCur=float(rr.registers[0])*0.1
    rr = client.read_input_registers(44,2, unit = 1)
    GridBPow=float((rr.registers[0]<<16)|(rr.registers[1]))*0.1

    # Phase C
    rr = client.read_input_registers(46,1, unit = 1)
    GridCVol=float(rr.registers[0])*0.1
    rr = client.read_input_registers(47,1, unit = 1)
    GridCCur=float(rr.registers[0])*0.1
    rr = client.read_input_registers(48,2, unit = 1)
    GridCPow=float((rr.registers[0]<<16)|(rr.registers[1]))*0.1

    # Reactive power
    rr = client.read_input_registers(230,2, unit = 1)
    ApOutP=float((rr.registers[0]<<16)|(rr.registers[1]))*0.1
    rr = client.read_input_registers(232,2, unit = 1)
    rePow=float((rr.registers[0]<<16)|(rr.registers[1]))*0.1
    rr = client.read_input_registers(234,2, unit = 1)
    rePowN=float((rr.registers[0]<<16)|(rr.registers[1]))*0.1
    rr = client.read_input_registers(236,2, unit = 1)
    rePowT=float((rr.registers[0]<<16)|(rr.registers[1]))*0.1

    # Battery Messague 
    rr = client.read_input_registers(1013,1, unit = 1)
    v_Bat=float(rr.registers[0])*0.1
    rr = client.read_input_registers(1014,1, unit = 1)
    SOC=float(rr.registers[0])
    rr = client.read_input_registers(1040,1, unit = 1)
    BatTemp=float(rr.registers[0])*0.1

    #Battery form BMS
    rr = client.read_input_registers(1082,1, unit = 1)
    StatusBMS=float(rr.registers[0])*0.1
    rr = client.read_input_registers(1086,1, unit = 1)
    SOCBMS=float(rr.registers[0])
    rr = client.read_input_registers(1087,1, unit = 1)
    BatVolBMS=float(rr.registers[0])*0.1
    rr = client.read_input_registers(1088,1, unit = 1)
    BatCurBMS=float(rr.registers[0])*0.1
    rr = client.read_input_registers(1089,1, unit = 1)
    BatTemBMS=float(rr.registers[0])*0.1
    rr = client.read_input_registers(1090,1, unit = 1)
    BattMaxCharCur=float(rr.registers[0])*0.1
    rr = client.read_input_registers(1095,1, unit = 1)
    CyBatBMS=float(rr.registers[0])
    rr = client.read_input_registers(1096,1, unit = 1)
    SOH=float(rr.registers[0])

    # Genetation energy
    # Solar Energy
    rr = client.read_input_registers(59,2, unit = 1)
    pvEneTod=float((rr.registers[0]<<16)|(rr.registers[1]))*0.1   
    rr = client.read_input_registers(91,2, unit = 1)
    pvEneTot=float((rr.registers[0]<<16)|(rr.registers[1]))*0.1  

    # Grid Energy 
    rr = client.read_input_registers(53,2, unit = 1)
    energy_today=float((rr.registers[0]<<16)|(rr.registers[1]))*0.1
    rr = client.read_input_registers(55,2, unit = 1)
    energy_total=float((rr.registers[0]<<16)|(rr.registers[1]))*0.1
    rr = client.read_input_registers(116,2, unit = 1)
    EacGrLod=float((rr.registers[0]<<16)|(rr.registers[1]))*0.1
    # Work time total 
    rr = client.read_input_registers(57,2, unit = 1)
    totGenTim=float((rr.registers[0]<<16)|(rr.registers[1]))*0.5

    # Battery Energy 
    rr = client.read_input_registers(1052,2, unit = 1)
    DiscETod=float((rr.registers[0]<<16)|(rr.registers[1]))*0.1 
    rr = client.read_input_registers(1054,2, unit = 1)
    DiscETot=float((rr.registers[0]<<16)|(rr.registers[1]))*0.1  
    rr = client.read_input_registers(1056,2, unit = 1)
    CharETod=float((rr.registers[0]<<16)|(rr.registers[1]))*0.1  
    rr = client.read_input_registers(1058,2, unit = 1)
    CharETot=float((rr.registers[0]<<16)|(rr.registers[1]))*0.1  
    # Charge by grid
    rr = client.read_input_registers(112,2, unit = 1)
    ACcharTod=float((rr.registers[0]<<16)|(rr.registers[1]))*0.1 
    rr = client.read_input_registers(114,2, unit = 1)
    ACcharTot=float((rr.registers[0]<<16)|(rr.registers[1]))*0.1    

    # Import energy
    rr = client.read_input_registers(1044,2, unit = 1)
    EUserTod=float((rr.registers[0]<<16)|(rr.registers[1]))*0.1 
    rr = client.read_input_registers(1046,2, unit = 1)
    EUserTot=float((rr.registers[0]<<16)|(rr.registers[1]))*0.1  

    # Export energy
    rr = client.read_input_registers(1048,2, unit = 1)
    e_to_grid_today=float((rr.registers[0]<<16)|(rr.registers[1]))*0.1 
    rr = client.read_input_registers(1050,2, unit = 1)
    e_to_grid_total=float((rr.registers[0]<<16)|(rr.registers[1]))*0.1 

    # Consumption energy
    rr = client.read_input_registers(1060,2, unit = 1)
    ELoadTod=float((rr.registers[0]<<16)|(rr.registers[1]))*0.1 
    rr = client.read_input_registers(1062,2, unit = 1)
    ELoadTot=float((rr.registers[0]<<16)|(rr.registers[1]))*0.1 

    # Grid and panel power
    rr = client.read_input_registers(35,2, unit = 1)
    GridPow=float((rr.registers[0]<<16)|(rr.registers[1]))*0.1 
    rr = client.read_input_registers(37,2, unit = 1)
    GridFreq=float((rr.registers[0]<<16)|(rr.registers[1]))*0.01 
    rr = client.read_input_registers(1,2, unit = 1)
    PanPow=float((rr.registers[0]<<16)|(rr.registers[1]))*0.1 
    rr = client.read_input_registers(1081,2, unit = 1)
    PowFac=float((rr.registers[0]<<16)|(rr.registers[1]))*0.1 

    # Import power
    rr = client.read_input_registers(1021,2, unit = 1)
    ImpPow=float((rr.registers[0]<<16)|(rr.registers[1]))*0.1 
    # Export power
    rr = client.read_input_registers(1029,2, unit = 1)
    ExpPow=float((rr.registers[0]<<16)|(rr.registers[1]))*0.1 
    # Consumption power
    rr = client.read_input_registers(1037,2, unit = 1)
    LoadPow=float((rr.registers[0]<<16)|(rr.registers[1]))*0.1 
    # Disc and charge power
    rr = client.read_input_registers(1009,2, unit = 1)
    DiscPow=float((rr.registers[0]<<16)|(rr.registers[1]))*0.1 
    rr = client.read_input_registers(1011,2, unit = 1)
    CharPow=float((rr.registers[0]<<16)|(rr.registers[1]))*0.1 
    # Add 
    rr = client.read_input_registers(100,1, unit = 1)
    IPF=float(rr.registers[0]) 
    rr = client.read_input_registers(104,1, unit = 1)
    DerMode=float(rr.registers[0])
    rr = client.read_input_registers(1064,1, unit = 1)
    ExpAppPow=float(rr.registers[0])
    rr = client.read_input_registers(1124,1, unit = 1)
    ACcharTod=float(rr.registers[0])

    #Escribiendo en el archivo de texto
    archi1=open("modbus_logs.txt","a")
    archi1.write("**********************************************************************************\n")
    archi1.write(time.strftime("%c") + "\n")
    # SPH Mode
    archi1.write("sph Status: "+ str(sphState) + "V \n")
    archi1.write("sph Status: "+ str(priority) + "V \n")
    archi1.write("sph Status: "+ str(BatType) + "V \n")
    archi1.write("sph Status: "+ str(SysMode) + "V \n")
    # Solar panel 1
    archi1.write("PV1 Volt: "+ str(pv1_volts) + "V \n")
    archi1.write("PV1 Curr: "+ str(pv1_current) + "A \n")
    archi1.write("PV1 Power: "+ str(pv1_W) + "W \n")
    # Solar panel 2
    archi1.write("PV2 Volt: "+ str(pv2_volts) + "V \n")
    archi1.write("PV2 Curr: "+ str(pv2_current) + "A \n")
    archi1.write("PV2 Power: "+ str(pv2_W) + "W \n")
    # Solar panel 3
    archi1.write("PV3 Volt: "+ str(pv3_volts) + "V \n")
    archi1.write("PV3 Curr: "+ str(pv3_current) + "A \n")
    archi1.write("PV3 Power: "+ str(pv3_W) + "W \n")
    # Inverter temperature 
    archi1.write("Inverter temp: "+ str(temp) + "V \n")
    archi1.write("Temp IPM: "+ str(tempIPM) + "A \n")
    archi1.write("Temp B: "+ str(tempB) + "W \n")
    # Output power
    archi1.write("ROutPow: "+ str(ROutPow) + "A \n")
    archi1.write("OutMPow: "+ str(OutMPow) + "W \n")
    # Grid message
    # Phase A
    archi1.write("Grid A Voltage: "+ str(GridAVol) + "V \n")
    archi1.write("Grid A Current: "+ str(GridACur) + "A \n")
    archi1.write("Grid A Power: "+ str(GridAPow) + "W \n")
    # Phase B
    archi1.write("Grid B Voltage: "+ str(GridBVol) + "V \n")
    archi1.write("Grid B Current: "+ str(GridBCur) + "A \n")
    archi1.write("Grid B Power: "+ str(GridBPow) + "W \n")
    # Phase C
    archi1.write("Grid C Voltage: "+ str(GridCVol) + "V \n")
    archi1.write("Grid C Current: "+ str(GridCCur) + "A \n")
    archi1.write("Grid C Power: "+ str(GridCPow) + "W \n")
    # Reactive power
    archi1.write("ApOutP: "+ str(ApOutP) + "w \n")
    archi1.write("rePow: "+ str(rePow) + "W \n")
    archi1.write("rePowN: "+ str(rePowN) + "w \n")
    archi1.write("rePowT: "+ str(rePowT) + "W \n")
    #Battery Messague 
    archi1.write("BattVol: "+ str(v_Bat) + "V \n")
    archi1.write("SOC: "+ str(SOC) + "% \n")
    archi1.write("BatTemp: "+ str(BatTemp) + "°C \n")
    #Battery form BMS
    archi1.write("StatusBMS: "+ str(StatusBMS) + "N/A \n")
    archi1.write("SOCBMS: "+ str(SOCBMS) + "% \n")
    archi1.write("BatVolBMS: "+ str(BatVolBMS) + "V \n")
    archi1.write("BatCurBMS: "+ str(BatCurBMS) + "A \n")
    archi1.write("BatTemBMS: "+ str(BatTemBMS) + "°C \n")
    archi1.write("BattMaxCharCur: "+ str(BattMaxCharCur) + "A \n")
    archi1.write("CyBatBMS: "+ str(CyBatBMS) + "N/A \n")
    archi1.write("SOH: "+ str(SOH) + "% \n")
    # Genetation energy
    # Solar Energy
    archi1.write("pvEneTod Energy today: "+ str(pvEneTod) + "kWH \n")
    archi1.write("pvEneTot Energy total: "+ str(pvEneTot) + "kWH \n")
    # Grid Energy
    archi1.write("EacGrTod Energy today: "+ str(energy_today) + "kWH \n")
    archi1.write("EacGrTot Energy total: "+ str(energy_total) + "kWH \n")
    archi1.write("EacGrLod Energy load: "+ str(EacGrLod) + "kWH \n")
    archi1.write("totGenTim Work time: "+ str(totGenTim) + "s \n")
    # Battery energy
    archi1.write("DiscETod Disc Energy today: "+ str(DiscETod) + "kWH \n")
    archi1.write("DiscETod Disc Energy total: "+ str(DiscETot) + "kWH \n")
    archi1.write("CharETod char Energy load: "+ str(CharETod) + "kWH \n")
    archi1.write("CharETot char energy total: "+ str(CharETot) + "KWH \n")
    # Charge by grid
    archi1.write("ACcharTod Charge battery from grid: "+ str(ACcharTod) + "kWH \n")
    archi1.write("ACcharTot Charge battery from grid: "+ str(ACcharTot) + "kWH \n")
     # Import energy
    archi1.write("EUserTod import Energy: "+ str(EUserTod) + "kWH \n")
    archi1.write("EUserTot import Energy: "+ str(EUserTot) + "kWH \n")
    # Export energy
    archi1.write("EGridTod export Energy: "+ str(e_to_grid_today) + "kWH \n")
    archi1.write("EGridTot export Energy: "+ str(e_to_grid_total) + "kWH \n")
    # Consumption energy
    archi1.write("ELoadTod energy load today: "+ str(ELoadTod) + "kWH \n")
    archi1.write("ELoadTot Energy load total: "+ str(ELoadTot) + "kWH \n")
    # Grid and panel power
    archi1.write("GridPow grid power: "+ str(GridPow) + "W \n")
    archi1.write("GridFreq frecuencia: "+ str(GridFreq) + "Hz \n")
    archi1.write("PanPow panel power: "+ str(PanPow) + "W \n")
    archi1.write("PowFac factor power: "+ str(PowFac) + "W \n")
    # Import power
    archi1.write("ImpPow import power: "+ str(ImpPow) + "W \n")
    # Export power
    archi1.write("ExpPow export power: "+ str(ExpPow) + "W \n")
    # Consumption power
    archi1.write("LoadPow load power: "+ str(LoadPow) + "W \n")
    # Disc and charge power
    archi1.write("DiscPow disc power: "+ str(DiscPow) + "W \n")
    archi1.write("CharPow char power: "+ str(CharPow) + "W \n")
    #Aadd
    archi1.write("IPF: "+ str(IPF) + "W \n")
    archi1.write("Dering mode: "+ str(DerMode) + "N/A \n")
    archi1.write("ExpAppPow export apparent power: "+ str(ExpAppPow) + "W \n")
    archi1.write("ACcharTod: "+ str(ACcharTod) + "W \n")
    archi1.close()
    client.close()
    time.sleep(5)