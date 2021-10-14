

<p align="center">
  <h3 align="center">How to delete event as Admin in Splunk</h3>

  <p align="center">
    <br />
    <br />
    <br />
    <a href="https://youtu.be/ojvT8tynm00">View Tutorial</a>
  </p>
</p>






### Installation

1. We need to get the Splunk software into our machine 
   ```sh
   sudo wget -O splunk-8.2.2.1-ae6821b7c64b-Linux-x86_64.tgz 'https://d7wz6hmoaavd0.cloudfront.net/products/splunk/releases/8.2.2.1/linux/splunk-8.2.2.1-ae6821b7c64b-Linux-x86_64.tgz'
   ```
2. We want to extract the Splunk under the opt directory
   ```sh
   tar xzvf splunk-8.2.2.1-ae6821b7c64b-Linux-x86_64.tgz -C /opt
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





