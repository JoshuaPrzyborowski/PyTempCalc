#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

'''
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Revised BSD License for more details.

    Copyright 2016 Game Maker 2k - https://github.com/GameMaker2k
    Copyright 2016 Joshua Przyborowski - https://github.com/JoshuaPrzyborowski

    $FileInfo: pytempcalc.py - Last Update: 12/18/2016 Ver. 0.3.5 RC 1 - Author: joshuatp $
'''

# http://www.nws.noaa.gov/om/winter/windchill.shtml
# http://www.wpc.ncep.noaa.gov/html/windchill.shtml
# http://www.wpc.ncep.noaa.gov/html/dewrh.shtml
# http://www.wpc.ncep.noaa.gov/html/heatindex.shtml

import math;

__program_name__ = "PyTempCalc";
__project__ = __program_name__;
__project_url__ = "https://gist.github.com/JoshuaPrzyborowski";
__version_info__ = (0, 3, 5, "RC 1", 1);
__version_date_info__ = (2016, 12, 18, "RC 1", 1);
__version_date__ = str(__version_date_info__[0])+"."+str(__version_date_info__[1]).zfill(2)+"."+str(__version_date_info__[2]).zfill(2);
if(__version_info__[4]!=None):
 __version_date_plusrc__ = __version_date__+"-"+str(__version_date_info__[4]);
if(__version_info__[4]==None):
 __version_date_plusrc__ = __version_date__;
if(__version_info__[3]!=None):
 __version__ = str(__version_info__[0])+"."+str(__version_info__[1])+"."+str(__version_info__[2])+" "+str(__version_info__[3]);
if(__version_info__[3]==None):
 __version__ = str(__version_info__[0])+"."+str(__version_info__[1])+"."+str(__version_info__[2]);

def RoundToInt(IntNum):
 return int(round(IntNum));

def ConvertTempUnits(Temperature, InTempUnit = "Fahrenheit", OutTempUnit = "Celsius"):
 InTempUnit = InTempUnit.capitalize();
 OutTempUnit = OutTempUnit.capitalize();
 retval = {};
 if(InTempUnit != "Fahrenheit" and InTempUnit != "Celsius"):
  return False;
 if(OutTempUnit != "Fahrenheit" and OutTempUnit != "Celsius"):
  return False;
 if(InTempUnit == "Fahrenheit" and OutTempUnit == "Celsius"):
  # retvaltmp = float(5.0 / 9.0) * (float(Temperature) - 32.0);
  retvaltmp = float(((float(Temperature) - 32) * 5) / 9);
  retval.update({
  'Fahrenheit': "{:0.2f}".format(float(Temperature)), 
  'Celsius': "{:0.2f}".format(float(retvaltmp)), 
  'Rankine': "{:0.2f}".format(float(Temperature) + float(273.15)), 
  'Kelvin': "{:0.2f}".format(float(retvaltmp) + float(273.15)), 
  'FahrenheitFull': float(Temperature), 
  'CelsiusFull': float(retvaltmp), 
  'RankineFull': float(Temperature) + float(273.15), 
  'KelvinFull': float(retvaltmp) + float(273.15), 
  'FahrenheitRounded': RoundToInt(float(Temperature)), 
  'CelsiusRounded': RoundToInt(float(retvaltmp)), 
  'RankineRounded': RoundToInt(float(Temperature) + float(273.15)), 
  'KelvinRounded': RoundToInt(float(retvaltmp) + float(273.15))
  });
 elif(InTempUnit == "Celsius" and OutTempUnit == "Fahrenheit"):
  # retvaltmp = float(5.0 * 9.0) / (float(Temperature) - 32.0);
  retvaltmp = float(((float(Temperature) * 9) / 5) + 32);
  retval.update({
  'Fahrenheit': "{:0.2f}".format(float(retvaltmp)), 
  'Celsius': "{:0.2f}".format(float(Temperature)), 
  'Rankine': "{:0.2f}".format(float(retvaltmp) + float(273.15)), 
  'Kelvin': "{:0.2f}".format(float(Temperature) + float(273.15)), 
  'FahrenheitFull': float(retvaltmp), 
  'CelsiusFull': float(Temperature), 
  'RankineFull': float(retvaltmp) + float(273.15), 
  'KelvinFull': float(Temperature) + float(273.15), 
  'FahrenheitRounded': RoundToInt(float(retvaltmp)), 
  'CelsiusRounded': RoundToInt(float(Temperature)), 
  'RankineRounded': RoundToInt(float(retvaltmp) + float(273.15)), 
  'KelvinRounded': RoundToInt(float(Temperature) + float(273.15))
  });
 else:
  return False;
 return retval;

def ConvertTempUnitsFromFahrenheitToCelsius(Temperature):
 return ConvertTempUnits(Temperature, "Fahrenheit", "Celsius");

def ConvertTempUnitsFromCelsiusToFahrenheit(Temperature):
 return ConvertTempUnits(Temperature, "Celsius", "Fahrenheit");

def ConvertWindUnits(WindSpeed, InWindUnit = "MPH", OutWindUnit = "KMH"):
 InWindUnit = InWindUnit.upper();
 OutWindUnit = OutWindUnit.upper();
 retval = {};
 if(InWindUnit != "MPH" and InWindUnit != "KMH"):
  return False;
 if(OutWindUnit != "MPH" and OutWindUnit != "KMH"):
  return False;
 if(InWindUnit == "MPH" and OutWindUnit == "KMH"):
  retvaltmp = float(float(WindSpeed) * 1.609344);
  retval.update({
  'MPH': "{:0.2f}".format(float(WindSpeed)), 
  'KMH': "{:0.2f}".format(float(retvaltmp)), 
  'MPHFull': float(WindSpeed), 
  'KMHFull': float(retvaltmp), 
  'MPHRounded': RoundToInt(float(WindSpeed)), 
  'KMHRounded': RoundToInt(float(retvaltmp))
  });
 elif(InWindUnit == "KMH" and OutWindUnit == "MPH"):
  retvaltmp = float(float(WindSpeed) / 1.609344);
  retval.update({
  'MPH': "{:0.2f}".format(float(retvaltmp)), 
  'KMH': "{:0.2f}".format(float(WindSpeed)), 
  'MPHFull': float(retvaltmp), 
  'KMHFull': float(WindSpeed), 
  'MPHRounded': RoundToInt(float(retvaltmp)), 
  'KMHRounded': RoundToInt(float(WindSpeed))
  });
 else:
  return False;
 return retval;

def ConvertWindUnitsFromMPHToKMH(Temperature):
 return ConvertWindUnits(WindSpeed, "MPH", "KMH");

def ConvertWindUnitsFromKMHToMPH(Temperature):
 return ConvertWindUnits(WindSpeed, "KMH", "MPH");

def WindChill(Temperature, WindSpeed, TempUnit = "Fahrenheit", WindUnit = "MPH"):
 TempUnit = TempUnit.capitalize();
 WindUnit = WindUnit.upper();
 windchillret = {};
 if(TempUnit != "Fahrenheit" and TempUnit != "Celsius"):
  return False;
 if(WindUnit != "MPH" and WindUnit != "KMH"):
  return False;
 if(TempUnit == "Fahrenheit" and WindUnit == "MPH"):
  windchill = float(35.74 + 0.6215 * float(Temperature) - 35.75 * math.pow(float(WindSpeed), 0.16) + 0.4275 * float(Temperature) * math.pow(float(WindSpeed), 0.16));
  windchillret.update({
  'Fahrenheit': "{:0.2f}".format(float(windchill)), 
  'Celsius': "{:0.2f}".format(float(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['CelsiusFull'])), 
  'Rankine': "{:0.2f}".format(float(windchill) + float(273.15)), 
  'Kelvin': "{:0.2f}".format(float(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['KelvinFull'])), 
  'FahrenheitFull': float(windchill), 
  'CelsiusFull': float(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['CelsiusFull']), 
  'RankineFull': float(windchill) + float(273.15), 
  'KelvinFull': float(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['KelvinFull']), 
  'FahrenheitRounded': RoundToInt(float(windchill)), 
  'CelsiusRounded': RoundToInt(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['CelsiusFull']), 
  'RankineRounded': RoundToInt(float(windchill) + float(273.15)), 
  'KelvinRounded': RoundToInt(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['KelvinFull'])
  });
 if(TempUnit == "Fahrenheit" and WindUnit == "KMH"):
  WindSpeed = 0.621371 * float(WindSpeed);
  windchill = float(35.74 + 0.6215 * float(Temperature) - 35.75 * math.pow(float(WindSpeed), 0.16) + 0.4275 * float(Temperature) * math.pow(float(WindSpeed), 0.16));
  windchillret.update({
  'Fahrenheit': "{:0.2f}".format(float(windchill)), 
  'Celsius': "{:0.2f}".format(float(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['CelsiusFull'])), 
  'Rankine': "{:0.2f}".format(float(windchill) + float(273.15)), 
  'Kelvin': "{:0.2f}".format(float(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['KelvinFull'])), 
  'FahrenheitFull': float(windchill), 
  'CelsiusFull': float(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['CelsiusFull']), 
  'RankineFull': float(windchill) + float(273.15), 
  'KelvinFull': float(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['KelvinFull']), 
  'FahrenheitRounded': RoundToInt(float(windchill)), 
  'CelsiusRounded': RoundToInt(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['CelsiusFull']), 
  'RankineRounded': RoundToInt(float(windchill) + float(273.15)), 
  'KelvinRounded': RoundToInt(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['KelvinFull'])
  });
 if(TempUnit == "Celsius" and WindUnit == "KMH"):
  windchill = float(13.12 + 0.6215 * float(Temperature) - 11.37 * math.pow(float(WindSpeed), 0.16) + 0.3965 * float(Temperature) * math.pow(float(WindSpeed), 0.16));
  windchillret.update({
  'Celsius': "{:0.2f}".format(float(windchill)), 
  'Fahrenheit': "{:0.2f}".format(float(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['FahrenheitFull'])), 
  'Rankine': "{:0.2f}".format(float(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['RankineFull'])), 
  'Kelvin': "{:0.2f}".format(float(windchill) + float(273.15)), 
  'CelsiusFull': float(windchill), 
  'FahrenheitFull': float(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['FahrenheitFull']), 
  'RankineFull': float(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['RankineFull']), 
  'KelvinFull': float(windchill) + float(273.15), 
  'CelsiusRounded': RoundToInt(float(windchill)), 
  'FahrenheitRounded': RoundToInt(ConvertTempUnits(float(windchill)), "Celsius", "Fahrenheit")['FahrenheitFull'], 
  'RankineRounded': RoundToInt(ConvertTempUnits(float(windchill)), "Celsius", "Fahrenheit")['RankineFull'], 
  'KelvinRounded': RoundToInt(float(windchill) + float(273.15))
  });
 if(TempUnit == "Celsius" and WindUnit == "MPH"):
  WindSpeed = 1.609344 * float(WindSpeed);
  windchill = float(13.12 + 0.6215 * float(Temperature) - 11.37 * math.pow(float(WindSpeed), 0.16) + 0.3965 * float(Temperature) * math.pow(float(WindSpeed), 0.16));
  windchillret.update({
  'Celsius': "{:0.2f}".format(float(windchill)), 
  'Fahrenheit': "{:0.2f}".format(float(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['FahrenheitFull'])), 
  'Rankine': "{:0.2f}".format(float(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['RankineFull'])), 
  'Kelvin': "{:0.2f}".format(float(windchill) + float(273.15)), 
  'CelsiusFull': float(windchill), 
  'FahrenheitFull': float(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['FahrenheitFull']), 
  'RankineFull': float(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['RankineFull']), 
  'KelvinFull': float(windchill) + float(273.15), 
  'CelsiusRounded': RoundToInt(float(windchill)), 
  'FahrenheitRounded': RoundToInt(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['FahrenheitFull']), 
  'RankineRounded': RoundToInt(ConvertTempUnits(float(windchill)), "Celsius", "Fahrenheit")['RankineFull'], 
  'KelvinRounded': RoundToInt(float(windchill) + float(273.15))
  });
 return windchillret;

def WindChillFahrenheitMPH(Temperature, WindSpeed):
 return WindChill(Temperature, WindSpeed, "Fahrenheit", "MPH");

def WindChillFahrenheitKMH(Temperature, WindSpeed):
 return WindChill(Temperature, WindSpeed, "Fahrenheit", "KMH");

def WindChillCelsiusKMH(Temperature, WindSpeed):
 return WindChill(Temperature, WindSpeed, "Celsius", "KMH");

def WindChillCelsiusMPH(Temperature, WindSpeed):
 return WindChill(Temperature, WindSpeed, "Celsius", "MPH");

def WindChillGenXML(TempUnit = "Fahrenheit", WindUnit = "MPH", OutputFile = "-"):
 TempUnit = TempUnit.capitalize();
 WindUnit = WindUnit.upper();
 mintemp = -45;
 maxtemp = 40;
 tempstart = 40;
 minwind = 5;
 maxwind = 60;
 windstart = 5;
 windchillout = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!DOCTYPE noaawcc [\n<!ELEMENT noaawcc (wcc)*>\n<!ELEMENT wcc EMPTY>\n<!ATTLIST wcc windspeedmph CDATA #REQUIRED>\n<!ATTLIST wcc windspeedkhm CDATA #REQUIRED>\n<!ATTLIST wcc temperaturef CDATA #IMPLIED>\n<!ATTLIST wcc temperaturec CDATA #IMPLIED>\n<!ATTLIST wcc temperaturer CDATA #IMPLIED>\n<!ATTLIST wcc temperaturek CDATA #IMPLIED>\n<!ATTLIST wcc windchillf CDATA #IMPLIED>\n<!ATTLIST wcc windchillc CDATA #IMPLIED>\n<!ATTLIST wcc windchillr CDATA #IMPLIED>\n<!ATTLIST wcc windchillk CDATA #IMPLIED>\n<!ATTLIST wcc frostbitemin CDATA #IMPLIED>\n]>\n<noaawcc>\n";
 while(windstart <= maxwind):
  tempstart = 40;
  while(tempstart >= mintemp):
   getwcval = WindChill(tempstart, windstart, TempUnit, WindUnit);
   if(TempUnit == "Fahrenheit"):
    gettuval = ConvertTempUnits(tempstart, "Fahrenheit", "Celsius");
   if(TempUnit == "Celsius"):
    gettuval = ConvertTempUnits(tempstart, "Celsius", "Fahrenheit");
   if(WindUnit == "MPH"):
    getwuval = ConvertWindUnits(tempstart, "MPH", "KMH");
   if(WindUnit == "KMH"):
    getwuval = ConvertWindUnits(tempstart, "KMH", "MPH");
   if((windstart == 5 and tempstart <= 40 and tempstart >= -5) or 
      (windstart == 10 and tempstart <= 40 and tempstart >= 0) or 
      (windstart == 15 and tempstart <= 40 and tempstart >= 5) or 
      (windstart == 20 and tempstart <= 40 and tempstart >= 5) or 
      (windstart == 25 and tempstart <= 40 and tempstart >= 5) or 
      (windstart == 30 and tempstart <= 40 and tempstart >= 10) or 
      (windstart == 35 and tempstart <= 40 and tempstart >= 10) or 
      (windstart == 40 and tempstart <= 40 and tempstart >= 10) or 
      (windstart == 45 and tempstart <= 40 and tempstart >= 10) or 
      (windstart == 50 and tempstart <= 40 and tempstart >= 10) or 
      (windstart == 55 and tempstart <= 40 and tempstart >= 15) or 
      (windstart == 60 and tempstart <= 40 and tempstart >= 15)):
    windchillout = windchillout + " <wcc windspeedmph=\""+str(getwuval['MPHRounded'])+"\" windspeedkhm=\""+str(getwuval['KMHRounded'])+"\" temperaturef=\""+str(gettuval['FahrenheitRounded'])+"\" temperaturec=\""+str(gettuval['CelsiusRounded'])+"\" temperaturer=\""+str(gettuval['RankineRounded'])+"\" temperaturek=\""+str(gettuval['KelvinRounded'])+"\" windchillf=\""+str(getwcval['FahrenheitRounded'])+"\" windchillc=\""+str(getwcval['CelsiusRounded'])+"\" windchillr=\""+str(getwcval['RankineRounded'])+"\" windchillk=\""+str(getwcval['KelvinRounded'])+"\" frostbitemin=\"-1\" />\n";
   if((windstart == 5 and tempstart <= -10 and tempstart >= -35) or 
      (windstart == 10 and tempstart <= -5 and tempstart >= -20) or 
      (windstart == 15 and tempstart <= 0 and tempstart >= -15) or 
      (windstart == 20 and tempstart <= 0 and tempstart >= -10) or 
      (windstart == 25 and tempstart <= 0 and tempstart >= -5) or 
      (windstart == 30 and tempstart <= 5 and tempstart >= -5) or 
      (windstart == 35 and tempstart <= 5 and tempstart >= 0) or 
      (windstart == 40 and tempstart <= 5 and tempstart >= 0) or 
      (windstart == 45 and tempstart <= 5 and tempstart >= 0) or 
      (windstart == 50 and tempstart <= 5 and tempstart >= 0) or 
      (windstart == 55 and tempstart <= 10 and tempstart >= 5) or 
      (windstart == 60 and tempstart <= 10 and tempstart >= 5)):
    windchillout = windchillout + " <wcc windspeedmph=\""+str(getwuval['MPHRounded'])+"\" windspeedkhm=\""+str(getwuval['KMHRounded'])+"\" temperaturef=\""+str(gettuval['FahrenheitRounded'])+"\" temperaturec=\""+str(gettuval['CelsiusRounded'])+"\" temperaturer=\""+str(gettuval['RankineRounded'])+"\" temperaturek=\""+str(gettuval['KelvinRounded'])+"\" windchillf=\""+str(getwcval['FahrenheitRounded'])+"\" windchillc=\""+str(getwcval['CelsiusRounded'])+"\" windchillr=\""+str(getwcval['RankineRounded'])+"\" windchillk=\""+str(getwcval['KelvinRounded'])+"\" frostbitemin=\"30\" />\n";
   if((windstart == 5 and tempstart <= -40 and tempstart >= -45) or 
      (windstart == 10 and tempstart <= -25 and tempstart >= -45) or 
      (windstart == 15 and tempstart <= -20 and tempstart >= -35) or 
      (windstart == 20 and tempstart <= -15 and tempstart >= -30) or 
      (windstart == 25 and tempstart <= -10 and tempstart >= -25) or 
      (windstart == 30 and tempstart <= -10 and tempstart >= -20) or 
      (windstart == 35 and tempstart <= -5 and tempstart >= -15) or 
      (windstart == 40 and tempstart <= -5 and tempstart >= -15) or 
      (windstart == 45 and tempstart <= -5 and tempstart >= -10) or 
      (windstart == 50 and tempstart <= -5 and tempstart >= -10) or 
      (windstart == 55 and tempstart <= 0 and tempstart >= -10) or 
      (windstart == 60 and tempstart <= 0 and tempstart >= 0)):
    windchillout = windchillout + " <wcc windspeedmph=\""+str(getwuval['MPHRounded'])+"\" windspeedkhm=\""+str(getwuval['KMHRounded'])+"\" temperaturef=\""+str(gettuval['FahrenheitRounded'])+"\" temperaturec=\""+str(gettuval['CelsiusRounded'])+"\" temperaturer=\""+str(gettuval['RankineRounded'])+"\" temperaturek=\""+str(gettuval['KelvinRounded'])+"\" windchillf=\""+str(getwcval['FahrenheitRounded'])+"\" windchillc=\""+str(getwcval['CelsiusRounded'])+"\" windchillr=\""+str(getwcval['RankineRounded'])+"\" windchillk=\""+str(getwcval['KelvinRounded'])+"\" frostbitemin=\"10\" />\n";
   if((windstart == 15 and tempstart <= -40 and tempstart >= -45) or 
      (windstart == 20 and tempstart <= -35 and tempstart >= -45) or 
      (windstart == 25 and tempstart <= -30 and tempstart >= -45) or 
      (windstart == 30 and tempstart <= -25 and tempstart >= -45) or 
      (windstart == 35 and tempstart <= -20 and tempstart >= -45) or 
      (windstart == 40 and tempstart <= -20 and tempstart >= -45) or 
      (windstart == 45 and tempstart <= -15 and tempstart >= -45) or 
      (windstart == 50 and tempstart <= -15 and tempstart >= -45) or 
      (windstart == 55 and tempstart <= -15 and tempstart >= -45) or 
      (windstart == 60 and tempstart <= -10 and tempstart >= -45)):
    windchillout = windchillout + " <wcc windspeedmph=\""+str(getwuval['MPHRounded'])+"\" windspeedkhm=\""+str(getwuval['KMHRounded'])+"\" temperaturef=\""+str(gettuval['FahrenheitRounded'])+"\" temperaturec=\""+str(gettuval['CelsiusRounded'])+"\" temperaturer=\""+str(gettuval['RankineRounded'])+"\" temperaturek=\""+str(gettuval['KelvinRounded'])+"\" windchillf=\""+str(getwcval['FahrenheitRounded'])+"\" windchillc=\""+str(getwcval['CelsiusRounded'])+"\" windchillr=\""+str(getwcval['RankineRounded'])+"\" windchillk=\""+str(getwcval['KelvinRounded'])+"\" frostbitemin=\"5\" />\n";
   tempstart = tempstart - 5;
  windstart = windstart + 5;
 windchillout = windchillout + "</noaawcc>\n";
 if(OutputFile!="-"):
  wcof = open(OutputFile, 'w');
  wcof.write(windchillout);
  wcof.close();
 return windchillout;

def WindChillGenXMLFahrenheitMPH(Temperature, WindSpeed):
 return WindChillGenXML("Fahrenheit", "MPH", OutputFile);

def WindChillGenXMLFahrenheitKMH(Temperature, WindSpeed):
 return WindChillGenXML("Fahrenheit", "KMH", OutputFile);

def WindChillGenXMLCelsiusKMH(Temperature, WindSpeed):
 return WindChillGenXML("Celsius", "KMH", OutputFile);

def WindChillGenXMLCelsiusMPH(Temperature, WindSpeed):
 return WindChillGenXML("Celsius", "MPH", OutputFile);

def HeatIndexByDewPoint(Temperature, DewPointTemp, TempUnit = "Fahrenheit"):
 TempUnit = TempUnit.capitalize();
 heatindexret = {};
 if(TempUnit != "Fahrenheit" and TempUnit != "Celsius"):
  return False;
 if(TempUnit == "Celsius"):
  Temperature = ConvertTempUnits(float(Temperature), "Celsius", "Fahrenheit")['FahrenheitFull'];
  DewPointTemp = ConvertTempUnits(float(DewPointTemp), "Celsius", "Fahrenheit")['FahrenheitFull'];
  TempUnit = "Fahrenheit";
 if(TempUnit == "Fahrenheit"):
  tc2 = ConvertTempUnits(float(Temperature), "Fahrenheit", "Celsius")['CelsiusFull'];
  tdc2 = ConvertTempUnits(float(DewPointTemp), "Fahrenheit", "Celsius")['CelsiusFull'];
  vaporpressure = 6.11 * (math.pow(10, 7.5 * (tdc2 / (237.7 + tdc2))));
  satvaporpressure = 6.11 * (math.pow(10, 7.5 * (tc2 / (237.7 + tc2))));
  RHumidity2 = RoundToInt(100.0 * (vaporpressure / satvaporpressure));
  hitemp = 61.0 + ((Temperature - 68.0) * 1.2) + (RHumidity2 * 0.094);
  fptemp = float(Temperature);
  hifinal = 0.5 * (fptemp + hitemp);
  if(hifinal > 79.0):
   hi = -42.379 + 2.04901523 * float(Temperature) + 10.14333127 * RHumidity2 - 0.22475541 * float(Temperature) * RHumidity2 - 6.83783 * (math.pow(10, -3)) * (math.pow(float(Temperature), 2)) - 5.481717 * (math.pow(10, -2)) * (math.pow(RHumidity2, 2)) + 1.22874 * (math.pow(10, -3)) * (math.pow(float(Temperature), 2)) * RHumidity2 + 8.5282 * (math.pow(10, -4)) * float(Temperature) * (math.pow(RHumidity2, 2)) - 1.99 * (math.pow(10, -6)) * (math.pow(float(Temperature), 2)) * (math.pow(RHumidity2,2));
   if((RHumidity2 <= 13.0) and (Temperature >= 80.0) and (Temperature <= 112.0)):
    adj1 = (13.0 - RHumidity2) / 4.0;
    adj2 = math.sqrt((17.0 - math.abs(Temperature - 95.0)) / 17.0);
    adj = adj1 * adj2;
    hi = hi - adj;
   elif((RHumidity2 > 85.0) and (Temperature >= 80.0) and (Temperature <= 87.0)):
    adj1 = (RHumidity2 - 85.0) / 10.0;
    adj2 = (87.0 - float(Temperature)) / 5.0;
    adj = adj1 * adj2;
    hi = hi + adj;
  else:
   hi = hifinal;
 heatindexret.update({
 'Fahrenheit': "{:0.2f}".format(float(hi)), 
 'Celsius': "{:0.2f}".format(float(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['CelsiusFull'])), 
 'Rankine': "{:0.2f}".format(float(hi) + float(273.15)), 
 'Kelvin': "{:0.2f}".format(float(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['KelvinFull'])), 
 'FahrenheitFull': float(hi), 
 'CelsiusFull': float(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['CelsiusFull']), 
 'RankineFull': float(hi) + float(273.15), 
 'KelvinFull': float(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['KelvinFull']), 
 'FahrenheitRounded': RoundToInt(float(hi)), 
 'CelsiusRounded': RoundToInt(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['CelsiusFull']), 
 'RankineRounded': RoundToInt(float(hi) + float(273.15)), 
 'KelvinRounded': RoundToInt(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['KelvinFull'])
 });
 return heatindexret;

def HeatIndexByDewPointFahrenheit(Temperature, DewPointTemp):
 return HeatIndexByDewPoint(Temperature, DewPointTemp, "Fahrenheit");

def HeatIndexByDewPointCelsius(Temperature, DewPointTemp):
 return HeatIndexByDewPoint(Temperature, DewPointTemp, "Celsius");

def HeatIndexByRelativeHumidity(Temperature, Humidity, TempUnit = "Fahrenheit"):
 TempUnit = TempUnit.capitalize();
 heatindexret = {};
 if(TempUnit != "Fahrenheit" and TempUnit != "Celsius"):
  return False;
 if(TempUnit == "Celsius"):
  Temperature = ConvertTempUnits(float(Temperature), "Celsius", "Fahrenheit")['FahrenheitFull'];
  TempUnit = "Fahrenheit";
 if(TempUnit == "Fahrenheit"):
  hitemp = 61.0 + ((float(Temperature) - 68.0) * 1.2) + (float(Humidity) * 0.094);
  fptemp = float(float(Temperature));
  hifinal = 0.5 * (fptemp + hitemp);
  if(hifinal > 79.0):
   hi = -42.379 + 2.04901523 * float(Temperature) + 10.14333127 * float(Humidity) - 0.22475541 * float(Temperature) * float(Humidity) - 6.83783 * (math.pow(10, -3)) * (math.pow(float(Temperature), 2)) - 5.481717 * (math.pow(10, -2)) * (math.pow(float(Humidity), 2))+1.22874 * (math.pow(10, -3)) * (math.pow(float(Temperature), 2)) * float(Humidity)+8.5282 * (math.pow(10, -4)) * float(Temperature) * (math.pow(float(Humidity), 2)) - 1.99 * (math.pow(10, -6)) * (math.pow(float(Temperature), 2)) * (math.pow(float(Humidity),2));
   if((float(Humidity) <= 13) and (float(Temperature) >= 80.0) and (float(Temperature) <= 112.0)):
    adj1 = (13.0 - float(Humidity)) / 4.0;
    adj2 = math.sqrt((17.0 - math.abs(float(Temperature) - 95.0)) / 17.0);
    adj = adj1 * adj2;
    hi = hi - adj;
   elif ((float(Humidity) > 85.0) and (float(Temperature) >= 80.0) and (float(Temperature) <= 87.0)):
    adj1 = (float(Humidity) - 85.0) / 10.0;
    adj2 = (87.0 - float(Temperature)) / 5.0;
    adj = adj1 * adj2;
    hi = hi + adj;
  else:
   hi = hifinal;
 heatindexret.update({
 'Fahrenheit': "{:0.2f}".format(float(hi)), 
 'Celsius': "{:0.2f}".format(float(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['CelsiusFull'])), 
 'Rankine': "{:0.2f}".format(float(hi) + float(273.15)), 
 'Kelvin': "{:0.2f}".format(float(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['KelvinFull'])), 
 'FahrenheitFull': float(hi), 
 'CelsiusFull': float(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['CelsiusFull']), 
 'RankineFull': float(hi) + float(273.15), 
 'KelvinFull': float(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['KelvinFull']), 
 'FahrenheitRounded': RoundToInt(float(hi)), 
 'CelsiusRounded': RoundToInt(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['CelsiusFull']), 
 'RankineRounded': RoundToInt(float(hi) + float(273.15)), 
 'KelvinRounded': RoundToInt(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['KelvinFull'])
 });
 return heatindexret;

def HeatIndexByRelativeHumidityFahrenheit(Temperature, Humidity):
 return HeatIndexByRelativeHumidity(Temperature, Humidity, "Fahrenheit");

def HeatIndexByRelativeHumidityCelsius(Temperature, Humidity):
 return HeatIndexByRelativeHumidity(Temperature, Humidity, "Celsius");

def RelativeHumidity(Temperature, DewPointTemp, TempUnit = "Fahrenheit"):
 TempUnit = TempUnit.capitalize();
 relativehumidityret = {};
 if(TempUnit != "Fahrenheit" and TempUnit != "Celsius"):
  return False;
 if(TempUnit == "Celsius"):
  Temperature = ConvertTempUnits(float(Temperature), "Celsius", "Fahrenheit")['FahrenheitFull'];
  DewPointTemp = ConvertTempUnits(float(DewPointTemp), "Celsius", "Fahrenheit")['FahrenheitFull'];
  TempUnit = "Fahrenheit";
 if(TempUnit == "Fahrenheit"):
  a = float(Temperature);
  b = float(DewPointTemp);
  a_c = ConvertTempUnits(float(a), "Fahrenheit", "Celsius")['CelsiusFull'];
  b_c = ConvertTempUnits(float(b), "Fahrenheit", "Celsius")['CelsiusFull'];
  c = 6.11 * math.pow(10, ((7.5 * a_c / (237.7 + a_c))));
  d = 6.11 * math.pow(10, ((7.5 * b_c / (237.7 + b_c))));
  e = (d / c) * 100;
  f = (round(e * 100)) / 100;
  ffull = (e * 100) / 100;
 relativehumidityret.update({
 'RelativeHumidity': "{:0.2f}".format(float(ffull)), 
 'RelativeHumidityRounded': RoundToInt(float(ffull)), 
 'RelativeHumidityFull': float(ffull)
 });
 return relativehumidityret;

def RelativeHumidityFahrenheit(Temperature, DewPointTemp):
 return RelativeHumidity(Temperature, DewPointTemp, "Fahrenheit");

def RelativeHumidityCelsius(Temperature, Humidity):
 return RelativeHumidity(Temperature, DewPointTemp, "Celsius");