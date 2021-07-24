# Fun Project 

## This fun project has below elements

1. Run REXX in a JCL and pass the Messages as SYSTSIN
2. REXX receives the multiline arguments and calls an http node in node-red
3. The message arrival triggers 3 actions in node-red
    3.1 Send the message to Alexa
    3.2 Play an Audio in the Laptop
    3.3 Post the message in a MS Teams channel using a webhook 

### JCL

```jcl
//IKJEFTJC  JOB REGION=0M,CLASS=S,MSGCLASS=X,        
//            MSGLEVEL=(1,1),NOTIFY=&SYSUID          
//EXAMPLE  EXEC PGM=IKJEFT01,REGION=4096K,DYNAMNBR=30
//SYSPRINT DD  SYSOUT=*                              
//SYSEXEC  DD  DISP=SHR,DSN=IBMUSER.JCLS             
//SYSTSPRT DD  SYSOUT=*                              
//SYSTSIN  DD  *                                     
  NODEREDB                          -                
  LPAR       DCUF                   -                
  SUBSYSTEM  DB2                    -                
  SEVERITY   2                      -                
  MESSAGE TEXT FOLLOWS              -                
  THIS IS THE MESSAGE TO BE ANNOUNCED BY ALEXA       
/*                                                   
```

### REXX Code NODEREDB to be stored in the SYSEXEC Library.

```rexx
/* REXX */                                                             
arg Messages                                                           
/* Server URI (just protocol and host really) */                       
uri = '192.168.2.81'                                                   
/* Server Port (just port                    ) */                      
port = '1880'                                                          
/*********************************************************************/
Address TSO                                                            
/* Make the HWTHTTP host environment available */                      
Call hwtcalls on                                                       
/* Initialise some variables we use */                                 
DiagArea. = ''                                                         
ReturnCode = 0                                                         
ReqHandle = 0                                                          
ConnectHandle = 0                                                      
HttpStatusCode = 0                                                     
HttpReasonCode = 0                                                     
ResponseBody = ''                                                      
RequestPath = '/zEntry'                                                
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
 * Send the Message to Node-red                                        
 */                                                                    
    /* Strip leading and trailing spaces */                            
    textToDisplay = Strip(Messages)                                    
    /* Build the request body */                                       
    requestData = '{' || ,                                             
     '"Message":"'    || textToDisplay || '"'  || ,                    
     '}'                                                               
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
    headerContentType = 'Content-type: application/json'               
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
```

### Node Red Setup

1. Install node.js and node-red <https://nodered.org/docs/getting-started/windows>

2. Import the Flow

```json
[{"id":"524fe5c0.a70e5c","type":"tab","label":"zIOT","disabled":false,"info":""},{"id":"d81c15e2.524f78","type":"ui_base","theme":{"name":"theme-light","lightTheme":{"default":"#0094CE","baseColor":"#0094CE","baseFont":"-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen-Sans,Ubuntu,Cantarell,Helvetica Neue,sans-serif","edited":true,"reset":false},"darkTheme":{"default":"#097479","baseColor":"#097479","baseFont":"-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen-Sans,Ubuntu,Cantarell,Helvetica Neue,sans-serif","edited":false},"customTheme":{"name":"Untitled Theme 1","default":"#4B7930","baseColor":"#4B7930","baseFont":"-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen-Sans,Ubuntu,Cantarell,Helvetica Neue,sans-serif"},"themeState":{"base-color":{"default":"#0094CE","value":"#0094CE","edited":false},"page-titlebar-backgroundColor":{"value":"#0094CE","edited":false},"page-backgroundColor":{"value":"#fafafa","edited":false},"page-sidebar-backgroundColor":{"value":"#ffffff","edited":false},"group-textColor":{"value":"#1bbfff","edited":false},"group-borderColor":{"value":"#ffffff","edited":false},"group-backgroundColor":{"value":"#ffffff","edited":false},"widget-textColor":{"value":"#111111","edited":false},"widget-backgroundColor":{"value":"#0094ce","edited":false},"widget-borderColor":{"value":"#ffffff","edited":false},"base-font":{"value":"-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen-Sans,Ubuntu,Cantarell,Helvetica Neue,sans-serif"}},"angularTheme":{"primary":"indigo","accents":"blue","warn":"red","background":"grey","palette":"light"}},"site":{"name":"Node-RED Dashboard","hideToolbar":"false","allowSwipe":"false","lockMenu":"false","allowTempTheme":"true","dateFormat":"DD/MM/YYYY","sizes":{"sx":48,"sy":48,"gx":6,"gy":6,"cx":6,"cy":6,"px":0,"py":0}}},{"id":"2be4ecceb4fdbc89","type":"alexa-remote-account","name":"","authMethod":"proxy","proxyOwnIp":"192.168.2.81","proxyPort":"3456","cookieFile":"D:\\Z\\Alexa","refreshInterval":"3","alexaServiceHost":"pitangui.amazon.com","amazonPage":"amazon.com","acceptLanguage":"en-US","userAgent":"","useWsMqtt":"on","autoInit":"on"},{"id":"c7dc0a18.2c9288","type":"template","z":"524fe5c0.a70e5c","name":"TeamsMessageBuild","field":"payload","fieldType":"msg","format":"handlebars","syntax":"mustache","template":"{\n  \"@context\": \"https://schema.org/extensions\",\n  \"@type\": \"MessageCard\",\n  \"themeColor\": \"0072C6\",\n  \"title\": \"Node-RED to Teams\",\n  \"text\": \"There is an Incident from Mainframe\"\n}","output":"str","x":340,"y":100,"wires":[["bc1662fd.9545e"]]},{"id":"bc1662fd.9545e","type":"http request","z":"524fe5c0.a70e5c","name":"","method":"POST","ret":"txt","paytoqs":"ignore","url":"https://atos365.webhook.office.com/webhookb2/e6ac63b9-669b-4f26-bba5-4b0a37fa8ff3@33440fc6-b7c7-412c-bb73-0e70b0198d5a/IncomingWebhook/f3923ae196ad4bdfb2f5451a2248950a/788daa90-58da-4246-b1ab-7de9e262496d","tls":"","persist":false,"proxy":"","authType":"","x":590,"y":100,"wires":[[]]},{"id":"5b199649.a8ad08","type":"http in","z":"524fe5c0.a70e5c","name":"zListener","url":"/zEntry","method":"post","upload":false,"swaggerDoc":"","x":80,"y":300,"wires":[["4ef25165.b2dc2","63a752a9.7bdd0c","1eaccced9bc5756c","c7dc0a18.2c9288"]]},{"id":"4ef25165.b2dc2","type":"template","z":"524fe5c0.a70e5c","name":"ResponceMsg","field":"payload","fieldType":"msg","format":"handlebars","syntax":"mustache","template":"Sweets from Node-RED: {{payload}} !","output":"str","x":400,"y":300,"wires":[["795d3737.d353e8"]]},{"id":"795d3737.d353e8","type":"http response","z":"524fe5c0.a70e5c","name":"Responce","statusCode":"","headers":{},"x":600,"y":300,"wires":[]},{"id":"63a752a9.7bdd0c","type":"http request","z":"524fe5c0.a70e5c","name":"Download mp3","method":"GET","ret":"bin","paytoqs":"ignore","url":"https://quz1yp-a.akamaihd.net/downloads/ringtones/files/dl/mp3/kannodu-kannodu-kannoram-49034-51958-53676.mp3","tls":"","persist":false,"proxy":"","authType":"","x":340,"y":220,"wires":[["2539fbce.cb39a4"]],"info":"https://quz1yp-a.akamaihd.net/downloads/ringtones/files/dl/mp3/kannodu-kannodu-kannoram-49034-51958-53676.mp3\n\n"},{"id":"2539fbce.cb39a4","type":"play audio","z":"524fe5c0.a70e5c","name":"","voice":"21","x":570,"y":220,"wires":[]},{"id":"1eaccced9bc5756c","type":"split","z":"524fe5c0.a70e5c","name":"Array to Message","splt":"\\n","spltType":"str","arraySplt":1,"arraySpltType":"len","stream":false,"addname":"","x":310,"y":400,"wires":[["be15d2f960bd4334","8849c1508ea12e63"]]},{"id":"8849c1508ea12e63","type":"debug","z":"524fe5c0.a70e5c","name":"","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"false","statusVal":"","statusType":"auto","x":610,"y":480,"wires":[]},{"id":"be15d2f960bd4334","type":"alexa-remote-routine","z":"524fe5c0.a70e5c","name":"","account":"2be4ecceb4fdbc89","routineNode":{"type":"speak","payload":{"type":"announcement","text":{"type":"msg","value":"payload"},"devices":["G090XG0793742RWP"]}},"x":610,"y":400,"wires":[[]]}]
```


