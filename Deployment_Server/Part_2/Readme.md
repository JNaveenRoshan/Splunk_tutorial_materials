

<p align="center">
  <h3 align="center">Setup Deployment Server in Splunk</h3>

  <p align="center">
    <br />
    <br />
    <br />
    <a href="https://youtu.be/-CK7JEM2Q3I">View Tutorial</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Setup</a></li>
      </ul>
    </li>
    <li><a href="#More Details">More Details</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## User Guide on How to Setup Deployment server and push apps onto the Clients





<!-- GETTING STARTED -->
## Getting Started

To get Deployment Server up in Splunk and send apps/data follow these simple steps.

### Prerequisites

 The Prerequisite for this video is to configure the Universal Forwarder as Deployment Client (We need some deployment Client to send data to)
 
 please refer to the [Tutorial](https://youtu.be/A9kiXzU6kfk)

### Configuration

1. In the Deployment Server Go to the below location and create folder naming the app that you want to deploy
   ```sh
   cd /opt/splunk/etc/deployment-apps 
   ```
2. Go to Settings and Click Forwarder Management


3. As you can see there is only one client and now click server class 


4. Click Create one and Type name for the server class
 

5. Add Apps that you want and Add the client


6. Add the client name in include text box (i.e) VM instance name


7. Refresh that tab


8. Click Edit app and select the app and check Restart Splunkd


9. Go to the below location and cd to app name you created and go into default folder(if it doesn't exits create one) 
   ```sh
   cd /opt/splunk/etc/deployment-apps
   mkdir default
   cd default
   nano inputs.conf
   ```
   
   
 10. Use the below code and the file is already available above.
   ```sh
   [monitor:///var/log/]
    disabled=false
    sourcetype=syslog
   ```  

 11. Reload splunk deploy server
 
 
 12. Check the GUI if it says 1 downloaded the it means the app is deployed on client
 
 
 13. Go to uf instance,restart it and go to the deployment apps folder
 
 
 14. Check for the app we created in the deployment server
 
 
 15. Check for the inputs.conf file we created in the deployment server in the default folder
 
 
 16.    
   
<!-- USAGE EXAMPLES -->
## More Details

Use the below link for the official documentation of Deployment Server in SPLUNK

 please refer to the [Documentation](https://docs.splunk.com/Documentation/Splunk/8.2.3/Updating/Aboutdeploymentserver)





