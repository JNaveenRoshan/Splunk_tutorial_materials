


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
## User Guide on Sending data to Indexer from Splunk


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

 We need a setup Indexer as a search peer in Search head
 
 please refer to the [Tutorial](https://www.splunk.com/en_us/download/universal-forwarder.html)
 

### Installation

1. In the backend of the Search head go to the local folder
   ```sh
   cd /opt/splunk/etc/system/local
   ```
2. Create a file named outputs.conf(This file is available above)
   ```sh
   nano outputs.conf
   ```
3. Add the following lines to that file
   ```sh
   [indexAndForward]
   index=false

    [tcpout]
    defaultGroup = my_search_peers
    forwardedindex.filter.disable = true
    indexAndForward = false

    [tcpout:my_search_peers]
    server=<ip>:<port>

   ```
   
4. Restart the Splunk 
   ```sh
   sudo ./splunk start
   ```
5. Now Check the data in Indexer which is been sent by the Search Head










