

<p align="center">
  <h3 align="center">How to send events to Splunk via HTTP Event Collector</h3>

  <p align="center">
    <br />
    <br />
    <br />
    <a href="https://youtu.be/xTZ0G9kh6Vo">View Tutorial</a>
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
## User Guide on Setting up HTTP Event Collector (HEC) Data Input to receive data 





<!-- GETTING STARTED -->
## Getting Started

To configure HEC data input in Splunk follow these simple steps.

### Prerequisites

 curl is the package we need to send events from one instance to another.Execute the below code in the non splunk instance
  ```sh
  sudo apt install curl
  ```

### Setting up 

1. Open Splunk and Go to Settings-->Data Inputs
  
  
2. Click HTTP Event Collector input and Click Create new
   
   
3. Type the name of the data input whilst type the port number as 8088 and Click next 

  
4. Choose Searching and Reporting App  
   
   
5. Creating a new index,sourcetype are optional


6. Review and Click Sumbit


7.**Note** - A token will be generated.Save the token somewhere safe.


8. In the non splunk instance execute the following command to send the events
   ```sh
   curl -k "https://localhost:8088/services/collector" \ -H "Authorization: Splunk <HEC Token> \-d '{"event": "Pony 1 has left the barn"}{"event": "Pony 2 has left the barn"        {"event": "Pony 3 has left the barn", "nested": {"key1": "value1"}}'
   ```

9.Replace <HEC Token> with the token you saved earlier and replace localhost with the external IP in case of VM instance


<!-- USAGE EXAMPLES -->
## More Details

Use the below link for the official documentation of Splunk

 please refer to the [Documentation](https://docs.splunk.com/Documentation/Splunk/8.2.2/Data/UsetheHTTPEventCollector)

