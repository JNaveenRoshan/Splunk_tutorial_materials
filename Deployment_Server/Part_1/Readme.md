

<p align="center">
  <h3 align="center">Configure Universal Forwarder as Deployment Client</h3>

  <p align="center">
    <br />
    <br />
    <br />
    <a href=""></a>
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
        <li><a href="#installation">Configuration</a></li>
      </ul>
    </li>
    <li><a href="#More Details">More Details</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## User Guide on Configuring Universal Forwarder as Deployment Client


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

We need the universal forwarder installed and running.

### Installation

1. We need to go to the bin location
   ```sh
   cd /opt/splunkforwarder/bin
   ```
2. Let the forwarder know the IP of the deployment server
   ```sh
   ./splunk set deploy-poll <IP>:8089
   ```
3. Please provide the necessary user credits and hit enter

4. Restart the Universal Forwarder 
   ```sh
   ./splunk restart
   ```
5. You can go and see the clients in the deployment server 


<!-- USAGE EXAMPLES -->
## More Details

Use the below link for the official documentation of Universal Forwarder as Deployment Client

 please refer to the [Documentation](https://www.splunk.com/en_us/blog/platform/adding-a-deployment-server-forwarder-management-to-a-new-or-existing-splunk-cloud-or-splunk-enterprise-deployment.html)





