

<p align="center">
  <h3 align="center">Installation of Splunk</h3>

  <p align="center">
    <br />
    <br />
    <br />
    <a href="https://www.youtube.com/watch?v=KGWZ_CxJ43g">View Tutorial</a>
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

1. In the Deployment Server Go to the below location and create folder naming the app that you want to deploy 
   ```sh
   cd /opt/splunk/etc/deployment-apps
   ```
2. Go to Settings and Click Forwarder Management
 
 
3. As you can see there is only one client and now click server class 


4. Click Create one and Type name for the server class
 
 
5. Add Apps that you want and Add the client.Add the client name in include text box (i.e) VM instance name

6. Refresh that tab

7. Click Edit app and select the app and check Restart Splunkd

8.  


<!-- USAGE EXAMPLES -->
## More Details

Use the below link for the official documentation of Splunk

 please refer to the [Documentation](https://docs.splunk.com/Documentation/Splunk/8.2.2/Installation/Chooseyourplatform)





