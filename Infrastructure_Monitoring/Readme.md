<p align="center">
  <h3 align="center">Infrastructure Monitoring in Splunk</h3>

  <p align="center">
    <br />
    <br />
    <br />
    <a href="https://youtu.be/B-xBFE6ISRs">View Tutorial</a>
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
        <li><a href="#installation">Procedure</a></li>
      </ul>
    </li>
    <li><a href="#More Details">More Details</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## User Guide on Setting up Infrastructure Monitoring in Splunk 





<!-- GETTING STARTED -->
## Getting Started

To get Splunk Infrastructure Monitoring up and running follow these simple steps.

### Prerequisites

1. Go to Apps and Click Find more Apps


2. Search for Splunk as infrastructure instance and install the splunk for infrastructure app


3. When popped up use splunk account credentials and click login and install


4. Click Restart now to restart Splunk


5. Go to Apps and Click Find More Apps and search for splunk for infrastructure and install the add on


6. Once installed restart splunk
  ```sh
  ./splunk restart
  ```

### Procedure

1. Go to Setting->Forwarding and receiving and Click Add new under Configure receiving 


2. Add 9997 as listening port and Click Save


3. Go to Settings->Data Inputs and select HTTP Event and Click the Global Settings and enable all tokens then click save


4. Click create new and type name for HTTP and click next and Now select the sourcetype as en_metrics
 
 
5. Click Review and Once the token is created and copy the token it will be used later


6. Go to the below location
  ```sh
   cd /opt/splunk/etc/system/local
   ```
   
7. Edit the file named inputs.conf and if it doesn’t exists create one
  ```sh
   nano inputs.conf
   ```
   
8. Copy the below code and paste it in the file (File is already available above).Replace the sourcetype IAS with the sourcetype you created when creating HTTP input
  ```sh
   [http://IAS]
   disabled = 0
   index = em_metrics
   indexes = em_metrics
   sourcetype = em_metrics
   token = <your token >
   ```
   
9. Restart the splunk
  ```sh
   ./splunk restart
   ```

10. Go to Find More Apps and click Splunk App for Infrastructure and Click Add new Entity and type the appropriate details in the asked text boxs


11. Copy the code under the Collect tab and copy that in your command line in the splunk instance that you want to monitor 


12. Check for the update and it might take some time and Once the install is done your output will say that you got one entity


13. Click Take a Look now and Click the entity name and Click Analysis



<!-- USAGE EXAMPLES -->
## More Details

Use the below link for the official documentation of Splunk Infrastructure Monitoring

 please refer to the [Documentation](https://docs.splunk.com/Observability/infrastructure/intro-to-infrastructure.html)





