'''
Created on Jun 1, 2015

@author: Bumsub
'''

import FileIO.Excel as excel
import Web.APIs.Geocoding as geocode


if __name__ == '__main__':

    result = excel.excelRead("Texas.xlsx", "Sheet1")
    #print(type(str(result[0][1].value)))
    #print(str(result[0][1].value))
    
    geocodingResult = geocode.geocodeList(result)
    
    #print(geocodingResult)
  
    excel.excelWriteOnExistingFile("Texas.xlsx", "Sheet1", "I", geocodingResult)
    
    print("Success")
    
    