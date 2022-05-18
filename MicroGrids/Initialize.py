from pathlib import Path

import pandas as pd


def Initialize_years(model, i):
    '''
    This function returns the value of each year of the project. 
    
    :param model: Pyomo model as defined in the Model_Creation script.
    
    :return: The year i.
    '''
    return i


Energy_Demand = pd.read_excel(Path(__file__).parent / "Example/Demand.xls")  # open the energy demand file
Energy_Demand.set_index(['Unnamed: 0'], drop=True, inplace=True)


def Initialize_Demand(model, i, t):
    '''
    This function returns the value of the energy demand from a system for each period of analysis from a excel file.
    
    :param model: Pyomo model as defined in the Model_Creation script.
        
    :return: The energy demand for the period t.     
        
    '''
    return float(Energy_Demand[i][t])


PV_Energy = pd.read_excel(Path(__file__).parent / "Example/PV_Energy.xls")  # open the PV energy yield file
PV_Energy.set_index(['Unnamed: 0'], drop=True, inplace=True)
_ = None


def Initialize_PV_Energy(model, i, t):
    '''
    This function returns the value of the energy yield by one PV under the characteristics of the system 
    analysis for each period of analysis from a excel file.
    
    :param model: Pyomo model as defined in the Model_Creation script.
    
    :return: The energy yield of one PV for the period t.
    '''
    return float(PV_Energy[i][t])


def Initialize_Demand_Dispatch(model, t):
    '''
    This function returns the value of the energy demand from a system for each period of analysis from a excel file.
    
    :param model: Pyomo model as defined in the Model_Creation script.
        
    :return: The energy demand for the period t.     
        
    '''
    return float(Energy_Demand[1][t])


def Initialize_PV_Energy_Dispatch(model, t):
    '''
    This function returns the value of the energy yield by one PV under the characteristics of the system 
    analysis for each period of analysis from a excel file.
    
    :param model: Pyomo model as defined in the Model_Creation script.
    
    :return: The energy yield of one PV for the period t.
    '''
    return float(PV_Energy[1][t])


def Marginal_Cost_Generator_1(model):
    return model.Diesel_Cost / (model.Low_Heating_Value * model.Generator_Effiency)


def Start_Cost(model):
    return model.Marginal_Cost_Generator_1 * model.Generator_Nominal_Capacity * model.Cost_Increase


def Marginal_Cost_Generator(model):
    return (
                       model.Marginal_Cost_Generator_1 * model.Generator_Nominal_Capacity - model.Start_Cost_Generator) / model.Generator_Nominal_Capacity


def Max_Power_Battery_Charge(model):
    '''
    This constraint calculates the Maximum power of charge of the battery. Taking in account the 
    capacity of the battery and a time frame in which the battery has to be fully loaded.
    
    :param model: Pyomo model as defined in the Model_creation library.
    '''
    return model.Battery_Nominal_Capacity / model.Maximun_Battery_Charge_Time


def Max_Power_Battery_Discharge(model):
    '''
    This constraint calculates the Maximum power of discharge of the battery. Taking in account 
    the capacity of the battery and a time frame in which the battery can be fully discharge.
    
    :param model: Pyomo model as defined in the Model_creation library.
    '''
    return model.Battery_Nominal_Capacity / model.Maximun_Battery_Discharge_Time
