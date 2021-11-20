


<p align="center">
  <h3 align="center">How to Send/Forward Data to Indexer</h3>

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
   wget -O splunkforwarder-8.2.3-cd0848707637-linux-2.6-amd64.deb 'https://download.splunk.com/products/universalforwarder/releases/8.2.3/linux/splunkforwarder-8.2.3-cd0848707637-linux-2.6-amd64.deb'
   ```
2. We want to extract the Splunk under the opt directory
   ```sh
   dpkg -i splunkforwarder-8.2.3-cd0848707637-linux-2.6-amd64.deb
   ```
3. There is Universal Forwarder Splunk startup file under the directory /opt/splunk/bin 
   ```sh
   cd /opt/splunk_forwarder/bin
   ```
4. Start the Universal Forwarder Splunk 
   ```sh
   sudo ./splunk start
   ```
5. However Once you accept the terms and agreements you will be asked to create a user name and password which you will use to access the Splunk GUI


<!-- USAGE EXAMPLES -->
## More Details

Use the below link for the official documentation of Universal Forwarder Splunk

 please refer to the [Documentation](https://www.splunk.com/en_us/download/universal-forwarder.html)







[indexAndForward]
index=false

[tcpout]
defaultGroup = my_search_peers
forwardedindex.filter.disable = true
indexAndForward = false

[tcpout:my_search_peers]
server=<ip>:<port>
