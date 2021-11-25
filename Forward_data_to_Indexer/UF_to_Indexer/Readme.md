


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
        <li><a href="#installation">Procedure</a></li>
      </ul>
    </li>
    <li><a href="#More Details">More Details</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## User Guide on Sending data to Indexer from Splunk Universal Forwarder


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

 We need to Install Splunk Universal Forwarder
 
 Please refer to the [Tutorial](https://youtu.be/69u2AFs5Gxw)
 

### Installation

1. Go to the backend of the universal forwarder I mean the command line interface


2. Run the following lines 
   ```sh
   ./splunk add forward-server  <IP>:<port>
   ```
4. Provide the necessary credentials 

5. Restart the Splunk 
   ```sh
   sudo ./splunk start
   ```
6. Now Check the data in Indexer whether the data is sent by the Universal Forwarder












