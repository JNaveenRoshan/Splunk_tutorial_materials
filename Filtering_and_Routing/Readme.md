


<p align="center">
  <h3 align="center">Filtering and Routing</h3>

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
        <li><a href="#installation">Setup</a></li>
      </ul>
    </li>
    <li><a href="#More Details">More Details</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## User Guide on Filtering and Routing in Splunk





<!-- GETTING STARTED -->
## Getting Started



### Prerequisites

 We need three splunk instances that will act as one heavy forwarder and 2 indexers 

### Setup and Configuration 

1. Let's create an empty sample log file and monitor it continuously 
   ```sh
   cd /opt/splunk/etc/var/log/splunk"
   ```
2. Go to /opt/splunk/etc/system/local location and create outputs.conf if it does exists just add the below code
   ```sh
   [tcpout:errorGroup]
   server=34.27.17.154:9997

   [tcpout:successGroup]
   server=104.198.182.234:9997
   ```
 
3. Create a another file called props.conf
  ```sh
   [test1]
   TRANSFORMS-routing=errorRouting,successRouting
   ```

4. Create a file called transforms.conf
   ```sh
   [errorRouting]
   REGEX=ERROR
   DEST_KEY=_TCP_ROUTING
   FORMAT=errorGroup


   [successRouting]
   REGEX=success
   DEST_KEY=_TCP_ROUTING
   FORMAT=successGroup
   ```
 
 
5. Now configure the forwarding and receiving ports in Indexers and Heavy Forwarder

6. Restart the Heavy Forwarder

7. Add the success events and error events in sample log file and check the Indexers

8. Error Events
  ```sh
   2022-10-30 11:32:00,791 +0000 ERROR	__init__:594 - Socket error communicating with splunkd (error=[Errno 111] Connection refused), path = /servicesNS/nobody/system/web-features/feature:quarantine_files
   ```

9. Success Events
  ```sh
10-30-2022 11:17:01.831 +0000 INFO  SavedSplunker - savedsearch_id="nobody;splunk_archiver;Bucket Copy Trigger", search_type="scheduled", search_streaming=0, user="nobody", app="splunk_archiver", savedsearch_name="Bucket Copy Trigger", priority=default, status=success, digest_mode=1, durable_cursor=0, scheduled_time=1667128620, window_time=0, dispatch_time=1667128620, run_time=1.237, result_count=0, alert_actions="", sid="scheduler__nobody_c3BsdW5rX2FyY2hpdmVy__RMD5473cbac83d6c9db7_at_1667128620_1", suppressed=0, thread_id="AlertNotifierWorker-0", workload_pool=""
   ```


<!-- USAGE EXAMPLES -->
## More Details

Use the below link for the official documentation of Splunk

 please refer to the [Documentation](https://docs.splunk.com/Documentation/Splunk/9.0.1/Forwarding/Routeandfilterdatad)





