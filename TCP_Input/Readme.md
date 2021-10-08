

<p align="center">
  <h3 align="center">How to send data to Splunk via TCP</h3>

  <p align="center">
    <br />
    <br />
    <br />
    <a href="https://youtu.be/TiH9s4YM-aQ">View Tutorial</a>
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
        <li><a href="#installation">Setting up Data Input</a></li>
      </ul>
    </li>
    <li><a href="#More Details">More Details</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## User Guide on Setting up TCP Data Input to receive data 





<!-- GETTING STARTED -->
## Getting Started

To configure TCP data input in Splunk follow these simple steps.

### Prerequisites

 netcat is the package we need to send data from one instance to another.Execute the below code in the non splunk instance
  ```sh
  sudo apt install netcat
  ```

### Setting up 

1. Open Splunk and Go to Settings-->Data Inputs
  
  
2. Click TCP input and Click Create new
   
   
3. Type port number 514 and Click next 
  
  
4. Choose Searching and Reporting App  
   
   
5. Creating a new index,sourcetype are optional


6. Review and Click Sumbit


  **Note** - Always remember to create the firewall rule to access the port


7. In the non splunk instance execute the following command to send the data to splunk
   ```sh
   cat <location of file> | nc <IP address> <Port number>
   ```

<!-- USAGE EXAMPLES -->
## More Details

Use the below link for the official documentation of Splunk

 please refer to the [Documentation](https://docs.splunk.com/Documentation/SplunkCloud/latest/Data/Monitornetworkports)





