/* REXX */                                                                      
/* Server URI (just protocol and host really) */                                
uri = '192.168.2.28'                                                            
/* Server Port (just port                    ) */                               
port = '8428'                                                                   
/* Name of data set containing the text to post */                              
msgDataset = 'IBMUSER.TEST.MESSAGE'                                             
/*********************************************************************/         
/* Main application starts here.                                     */         
/*********************************************************************/         
/* Provide access to TSO commands */                                            
Address TSO                                                                     
/* Make the HWTHTTP host environment available */                               
Call hwtcalls on                                                                
/* Initialise some variables we use */                                          
DiagArea. = ''                                                                  
Messages. = ''                                                                  
ReturnCode = 0                                                                  
ReqHandle = 0                                                                   
ConnectHandle = 0                                                               
HttpStatusCode = 0                                                              
HttpReasonCode = 0                                                              
ResponseBody = ''                                                               
/* RequestPath = '/api/v1/import/csv?format=2:metric:ask,3:metric:bid,1:label:ticke
r,4:label:market,5:time:rfc3339' */                                                
RequestPath = '/api/v1/import/csv?format=4:metric:msu_capacity,5:metric:day_msu_
mean,6:metric:yr_msu_mean,7:metric:percent_change,2:label:client,3:label:machine
_model,1:time:rfc3339'                                                 
/*                                                                              
 * Initialise the environment.                                                  
 */                                                                             
/* Initialise some HWT constants */                                             
Address hwthttp "hwtconst" "ReturnCode" "DiagArea."                             
If ReturnCode \= 0 Then Call ShowError "hwtconst"                               
/*                                                                              
 * Initialise a connection                                                      
 */                                                                             
/* Tell HWT we are creating a connection handle */                              
HandleType = HWTH_HANDLETYPE_CONNECTION                                         
Address hwthttp "hwthinit" "ReturnCode" ,                                       
                "HandleType" "ConnectHandle" "DiagArea."                        
If ReturnCode \= 0 Then Call ShowError "hwthinit (connection)"        
/*                                                                    
 * Setup the connection options                                       
 */                                                                   
/* Uncomment to enable debug messages */                              
/* Call SetConnOpt "HWTH_OPT_VERBOSE", "HWTH_VERBOSE_ON" */           
/* Connection URI (hostname really) */                                
Call SetConnOpt "HWTH_OPT_URI", uri                                   
/* Connection Port (hostname really) */                               
Call SetConnOpt "HWTH_OPT_PORT", port                                 
/* Timeout on the send after 10 seconds */                            
Call SetConnOpt "HWTH_OPT_SNDTIMEOUTVAL", 10                          
/* Timeout on the receive after 10 seconds */                         
Call SetConnOpt "HWTH_OPT_RCVTIMEOUTVAL", 10                          
/* Perform the connect */                                             
Address hwthttp "hwthconn" "ReturnCode" "ConnectHandle" "DiagArea."   
If ReturnCode \= 0 Then Call ShowError "hwthconn"                     
/*                                                                    
 * Pull in messages to be emitted to VM    as a stem variable.        
 */                                                                   
/* Open the data set containing the message data */                   
Address TSO "ALLOCATE DA('" || msgDataset || "') FILE(MESSAGES) OLD"  
/* Check this allocate worked OK */                                   
If RC \= 0 Then Exit 12                                               
/* Read in all the records */                                         
Address MVS "EXECIO * DISKR MESSAGES (STEM Messages. FINIS"           
/* Do an empty write to clear the data set */                         
Address MVS "EXECIO 0 DISKW MESSAGES (OPEN FINIS"                     
/* Close the message data set */                                      
Address TSO "FREE FILE(MESSAGES)"                                     
/*                                                                    
 * Loop through each line in the file and send each as a separate     
 * Slack notification.                                                
 */                                                                   
Do i = 1 To Messages.0                                                
    /* Strip leading and trailing spaces */                           
    textToDisplay = Strip(Messages.i)                                 
    /* Build the request body */                                      
    requestData = textToDisplay                                         
    /* Confirm the request body */                                      
    Say requestData                                                     
    /* Initialise the request */                                        
    HandleType = HWTH_HANDLETYPE_HTTPREQUEST                            
    Address hwthttp "hwthinit" "ReturnCode" ,                           
                    "HandleType" "ReqHandle" "DiagArea."                
    If ReturnCode \= 0 Then Call ShowError "hwthinit (request)"         
    /*                                                                  
     * Setup the request options                                        
     */                                                                 
    /* Setup list of headers */                                         
    sList = 0                                                           
    headerContentType = 'Content-type: text/csv'                        
    Address hwthttp "hwthslst" "ReturnCode" ,                           
                    "ReqHandle" "HWTH_SLST_NEW" "sList" ,               
                    "headerContentType" "DiagArea."                     
    If ReturnCode \= 0 Then Call ShowError "hwthslst (new)"             
    /* HTTP GET request */                                              
    Call SetReqOpt "HWTH_OPT_REQUESTMETHOD", "HWTH_HTTP_REQUEST_POST"   
    /* Request path */                                                  
    Call SetReqOpt "HWTH_OPT_URI", requestPath                          
    /* Use the HTTP headers list we have created */                     
    Call SetReqOpt "HWTH_OPT_HTTPHEADERS", sList                        
    /* Translate to ASCII outbound please */                            
    Call SetReqOpt "HWTH_OPT_TRANSLATE_REQBODY", ,                      
                   "HWTH_XLATE_REQBODY_E2A"                             
    /* Translate to EBCDIC inbound please */                            
    Call SetReqOpt "HWTH_OPT_TRANSLATE_RESPBODY", ,                     
                   "HWTH_XLATE_RESPBODY_A2E"                            
    /*                                                                  
      The following options take a reference to the internal Rexx       
      string buffer, but Rexx does not allow us to pass arguments by    
      references and we can therefore not use the handy SetReqOpt       
      subroutine used above.                                            
    */                                                                  
    /* Use the request body we created earlier */                       
    Address hwthttp "hwthset" "ReturnCode" "ReqHandle" ,                
            "HWTH_OPT_REQUESTBODY" "requestData" "DiagArea."             
    If ReturnCode \= 0 Then                                              
        Call ShowError "hwthset HWTH_OPT_REQUESTBODY"                    
    /* Grab the response data into here */                               
    Address hwthttp "hwthset" "ReturnCode" "ReqHandle" ,                 
            "HWTH_OPT_RESPONSEBODY_USERDATA" "ResponseBody" "DiagArea."  
    If ReturnCode \= 0 Then                                              
        Call ShowError "hwthset HWTH_OPT_RESPONSEBODY_USERDATA"          
    /* Perform the request */                                            
    Address hwthttp "hwthrqst" "ReturnCode" ,                            
                    "ConnectHandle" "ReqHandle" ,                        
                    "HttpStatusCode" "HttpReasonCode" "DiagArea."        
    If ReturnCode \= 0 Then Call ShowError "hwthrqst"                    
    /* Check for good HTTP response */                                   
    If HttpStatusCode \= 200 Then Do                                     
        /* Dump out the HTTP response code */                            
        Say "HTTP status" HttpStatusCode                                 
        /* Dump out the HTTP reason code */                              
        Say "HTTP reason" HttpReasonCode                                 
        /* Dump out the response body */                                 
        Say "Response" ResponseBody                                      
    End                                                                  
    /* Free the request headers */                                       
    Address hwthttp "hwthslst" "ReturnCode" ,                            
                    "ReqHandle" "HWTH_SLST_FREE" "sList" ,               
                    "headerContentType" "DiagArea."                      
    If ReturnCode \= 0 Then Call ShowError "hwthslst (free)"             
    /* Reset the request for next use */                                 
    Address hwthttp "hwthrset" "ReturnCode" ,                            
                    "ReqHandle" "DiagArea."                              
    If ReturnCode \= 0 Then Call ShowError "hwthrset (free)"             
End /* End of Messages.i loop */                                         
/* All complete */                                                       
Exit 0                                                                   
/*********************************************************************/  
/*                                                                   */  
/* Routine to remove the drudgery of setting HTTP connection options */  
/*                                                                   */  
/*********************************************************************/ 
SetConnOpt:                                                             
/* Input arguments */                                                   
@optName  = Arg(1)                                                      
@optValue = Arg(2)                                                      
/* Clear current status */                                              
ReturnCode = -1                                                         
DiagArea. = ''                                                          
/* Perform the call */                                                  
Address hwthttp "hwthset" "ReturnCode" "ConnectHandle" ,                
                "@optName" "@optValue" "DiagArea."                      
/* Check for good return */                                             
If ReturnCode \= 0 Then Call ShowError "hwthset (conn) " || @optName    
/* All complete */                                                      
Return                                                                  
/*********************************************************************/ 
/*                                                                   */ 
/* Routine to remove the drudgery of setting HTTP request options    */ 
/*                                                                   */ 
/*********************************************************************/ 
SetReqOpt:                                                              
/* Input arguments */                                                   
@optName  = Arg(1)                                                      
@optValue = Arg(2)                                                      
/* Clear current status */                                              
ReturnCode = -1                                                         
DiagArea. = ''                                                          
/* Perform the call */                                                  
Address hwthttp "hwthset" "ReturnCode" "ReqHandle" ,                    
                "@optName" "@optValue" "DiagArea."                      
/* Check for good return */                                             
If ReturnCode \= 0 Then Call ShowError "hwthset (req) " || @optName     
/* All complete */                                                      
Return                                                                  
/*********************************************************************/ 
/*                                                                   */ 
/* Displays the diagnostic data following a bad function call and    */ 
/* terminates the runtime with RC=8.                                 */ 
/*                                                                   */ 
/*********************************************************************/ 
ShowError: Procedure Expose ReturnCode DiagArea.                        
/* Pull in the function name and diagnostic data */                     
@fn = Arg(1)                                                            
/* Keep track of the sign of the return code (D2X must be 0 or +ve) */  
If ReturnCode >= 0 Then SignReturnCode = '' ; Else SignReturnCode = '-' 
/* Say what went wrong */                                               
Say @fn || ,                                                            
    ": RC " || ReturnCode || ,                                          
    "=" || SignReturnCode || "'" || D2X(ABS(ReturnCode)) || "'x"        
/* Dump out the error */                                                
Say "Service =" DiagArea.HWTH_Service                                   
Say "Reason  =" DiagArea.HWTH_ReasonCode                                
Say "Desc    =" Strip(DiagArea.HWTH_ReasonDesc,,'00'x)                  
/* Terminate the runtime */                                             
Exit 8                                                                  
Return                                                                  
