


<p align="center">
  <h3 align="center">Masking Data in Splunk</h3>

  <p align="center">
    <br />
    <br />
    <br />
    <a href="https://youtu.be/UNGz5gEF62E">View Tutorial</a>
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
        <li><a href="#Masking">Masking</a></li>
      </ul>
    </li>
    <li><a href="#More Details">More Details</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## User Guide on Installing Splunk in Linux on Cloud





<!-- GETTING STARTED -->
## Getting Started

To Mask the data in the backend of the Splunk follow these simple steps.

### Prerequisites

 Create a file called accounts.log in the location /var/log (This file is available above)
  ```sh
  nano accounts.log
  ```
  
  Copy and paste the below contents in the file
   ```sh
  ss=123456789, cc=1234-5678-9012-3456
  ss=123456790, cc=2234-5678-9012-3457
  ss=123456791, cc=3234-5678-9012-3458
  ss=123456792, cc=4234-5678-9012-3459
  ```

### Masking

1. In Splunk go to Settings and in the Files & Directories section Click Add new 
 
2. Choose the Location of the file accounts.log
   ```sh
   /var/log/
   ```
3. Click Next,Then under Break Events Select Every Line and Save sourcetype as SSN-CC 
 
4. Click Next and Select App context as Search & Reporting
   
5. Click Review and Submit

6. Go to the directory
   ```sh
   cd /opt/splunk/etc/system/local
   ```
   
7. Create a file named props.conf
   ```sh
   nano props.conf
   ```

8. Copy and Paste the below contents inside the props.conf file
   ```sh
   [SSN-CC]
   SEDCMD-Anon = s/ss=\d{5}(\d{4})/ss=xxxxx\1/g s/cc=(\d{4}-){3}(\d{4})/cc=xxxx-xxxx-xxxx-\2/g
   ```
   
9. Restart Splunk
   ```sh
   sudo ./splunk restart
   ```
   
10. Now go to /var/log/ and create a new file named acc2.log and copy the below contents into the file(However this file is available above) 
   ```sh
   ss=123456789, cc=1234-5678-9012-3456
   ss=123456790, cc=2234-5678-9012-3457
   ss=123456791, cc=3234-5678-9012-3458
   ss=123456792, cc=4234-5678-9012-3459
   ss=123456789, cc=1234-5678-9012-3456
   ss=123456790, cc=2234-5678-9012-3457
   ss=123456791, cc=3234-5678-9012-3458
   ss=123456792, cc=4234-5678-9012-3459
   ```
   
11. In Splunk go to Settings and in the Files & Directories section Click Add new 
 
12. Choose the Location of the file acc2.log
   ```sh
   /var/log/
   ```
13. Click Next,Then under Break Events Select Every Line and Save sourcetype as SSN-CC (Whenever you choose this Sourcetype by default all the events will be masked)
 
14. Click Next and Select App context as Search & Reporting
   
15. Click Review and Submit

<!-- USAGE EXAMPLES -->
## More Details

Use the below link for the official documentation of Splunk

 please refer to the [Documentation](https://docs.splunk.com/Documentation/Splunk/8.2.2/Data/Anonymizedata)





