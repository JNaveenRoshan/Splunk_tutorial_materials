
cd to /opt/splunk/etc/system/local




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
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#More Details">More Details</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## User Guide on Installing Splunk in Linux on Cloud





<!-- GETTING STARTED -->
## Getting Started

To get Splunk up and running follow these simple steps.

### Prerequisites

 We need a package called **wget** to get splunk software from the splunk web server into our machine.If you already have this package please do ignore the below step
  ```sh
  sudo apt install wget
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

<!-- USAGE EXAMPLES -->
## More Details

Use the below link for the official documentation of Universal Forwarder Splunk

 please refer to the [Documentation](https://www.splunk.com/en_us/download/universal-forwarder.html)





