# Start a Flow from Power Automate and Invoke NodeRed at the End

## Components

1. Power Automate 
2. Github Account - Create a New Repoitory in Github for this. sunil390/automate
3. Upswift.io account for portforwarding from rapberry pi - login with google account
4. node-red in raspberry pi 

### Power Automate Setup

1. Select the "Send an email to create GitHub issues" Flow
2. Select the email folder from which the alert to be triggerred to GitHub
3. Set the condition from contains sunil.sukumaran@atos.net
4. Save the flow.

### Upswift Port forwarding.
1. Logged in with gmail id
2. added a project zautomate 
3. Register the raspberry pi device by executing this command in raspberry login ->  sudo wget -O - "https://dashboard.upswift.io/install_upswift" | sudo sh -s jJjF_Nk9cCeGZcMdxPcvhcrVp5qT684LsQ zautomate 
4. Go to Control center remote access 
5. create a new portforwarding session for node-red by forwarding port 1880
6. copy the port-forwarding url

### rapberry pi

1. start the node-red
2. the http listener based flow is reused.

### Github 

1. goto setting of sunil390/automate repository
2. select webhooks
3. set the payload url with the entrypoint mentioned in httplistener in node-red
4. the portforwarding url from upswift.io is used here. 

