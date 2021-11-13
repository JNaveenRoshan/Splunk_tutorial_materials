

<p align="center">
  <h3 align="center">Installation of Universal Forwarder Splunk</h3>

  <p align="center">
    <br />
    <br />
    <br />
    <a href="https://www.youtube.com/watch?v=KGWZ_CxJ43g"></a>
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

### Installation

1. We need to get the Splunk software into our machine 
   ```sh
   wget -O splunkforwarder-8.2.3-cd0848707637-Linux-armv8.tgz 'https://download.splunk.com/products/universalforwarder/releases/8.2.3/linux/splunkforwarder-8.2.3-cd0848707637-Linux-armv8.tgz'
   ```
2. We want to extract the Splunk under the opt directory
   ```sh
   sudo tar zxvf splunkforwarder-8.2.3-cd0848707637-Linux-armv8.tgz -C /opt
   ```
3. There is splunk startup file under the directory /opt/splunk/bin 
   ```sh
   cd /opt/splunk/bin
   ```
4. Start the Splunk 
   ```sh
   sudo ./splunk start
   ```
5. However you will be asked to create a user name and password which you will use to access the Splunk GUI

6. Once everything is done you need to open a browser and type the below code to access the Splunk (However the **localhost** in the below code must be changed to the respective IP when using VMs) 
   ```sh
   localhost:8000

<!-- USAGE EXAMPLES -->
## More Details

Use the below link for the official documentation of Splunk

 please refer to the [Documentation](https://docs.splunk.com/Documentation/Splunk/8.2.2/Installation/Chooseyourplatform)





