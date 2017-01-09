                                                                                                                                                                                     
#!/bin/bash                                                                                                                                                                          
                                                                                                                                                                                     
from subprocess import PIPE, Popen                                                                                                                                                   
from sys import exit                                                                                                                                                                 
                                                                                                                                                                                     
# Regular                                                                                                                                                                            
txtblk='\033[30m' # Black                                                                                                                                                            
txtred='\033[31m' # Red                                                                                                                                                              
txtgrn='\033[32m' # Green                                                                                                                                                            
txtylw='\033[33m' # Yellow                                                                                                                                                           
txtblu='\033[34m' # Blue                                                                                                                                                             
txtpur='\033[35m' # Purple                                                                                                                                                           
txtcyn='\033[36m' # Cyan                                                                                                                                                             
txtwht='\033[0m' # White                                                                                                                                                             
                                                                                                                                                                                     
endpnts = ['Teams','News','Standings','Scores','Schedule','Videos','Stats','AllGames','FAQ','Terms_and_Info','Home']                                                                 
                                                                                                                                                                                     
def test_url(url):                                                                                                                                                                   
    p = Popen(['curl', '-i',url], stdout=PIPE, stderr=PIPE)                                                                                                                          
    output, err = p.communicate()                                                                                                                                                    
    if p.returncode != 0:                                                                                                                                                            
        return 1                                                                                                                                                                     
    elif output.lower().find("not a valid path") is not -1:                                                                                                                          
        return 1                                                                                                                                                                     
    elif output.lower().find("N/A") is not -1:                                                                                                                                       
        return 1                                                                                                                                                                     
    else:                                                                                                                                                                            
        return 0                                                                                                                                                                     
                                                                                                                                                                                     
#base_url='http://ec2-52-7-194-101.compute-1.amazonaws.com'                                                                                                                          
base_url = 'localhost'                                                                                                                                                               
port = '4001'                                                                                                                                                                        
                                                                                                                                                                                     
ret_val = 0                                                                                                                                                                          
                                                                                                                                                                                     
for pnt in endpnts:                                                                                                                                                                  
    url=base_url+":"+port+"/"+pnt                                                                                                                                                    
    print txtylw + "Testing endpoint "+ url + txtwht                                                                                                                                 
    result = test_url(url)                                                                                                                                                           
    if result:                                                                                                                                                                       
        print txtred + "ERROR" + txtwht                                                                                                                                              
        ret_val = 1                                                                                                                                                                  
    else:                                                                                                                                                                            
        print txtgrn + "SUCCESS" + txtwht                                                                                                                                            
                                                                                                                                                                                     
exit(ret_val)                                                                                                                                                                        
                