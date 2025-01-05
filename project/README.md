**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.
## Quicknote

Reminder:
- start vagrant 
- tunnel the ports 8080 and 3000


## Verify the monitoring installation

*TODO:* run `kubectl` command to show the running pods and services for all components. Take a screenshot of the output and include it here to verify the installation

## Setup the Jaeger and Prometheus source
*TODO:* Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.

## Create a Basic Dashboard
*TODO:* Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.

## Describe SLO/SLI
Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.

- The SLO of *monthly uptime* could for example be to have a 99.9% up time in a given month. For the *request response time* we could set the objective to have 90 % of the requests returned in 200ms or less. SLIs are Service-Level Indicators. This means they should be specific metrics that can allow us to track the the performance of 

SlIs are metrics to measure if we reach of Objectives. so for example we could measure that the service was out for 14 minutes in the last month and that only 82% of the requests were returned in 200ms or less in the last months.

## Creating SLI metrics.
It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs. 

### 1. Monthly Uptime (SLO: 99.9%)
- **SLI:** Percentage of time the service was available (i.e., no downtime) over the course of a given month.
  - **Formula:**  
    \[
    \text{SLI} = \frac{\text{Total Uptime}}{\text{Total Time in Month}} \times 100
    \]
  - This metric provides the proportion of time the service was operational during the month.

### 2. Request Response Time (SLO: average response time < X milliseconds)
- **SLI:** The average time taken to process a request, measured in milliseconds or seconds.
  - **Formula:**  
    \[
    \text{SLI} = \frac{\sum (\text{response times for all requests})}{\text{total number of requests}}
    \]
  - This provides insight into the overall responsiveness of the system.

### 3. Request Success Rate (SLO: Success rate > 99.5%)
- **SLI:** The percentage of successful requests (those that result in a 2xx status code) out of the total number of requests.
  - **Formula:**  
    \[
    \text{SLI} = \frac{\text{Number of Successful Requests}}{\text{Total Number of Requests}} \times 100
    \]
  - This SLI tracks the reliability of the service in terms of successful responses.

### 4. Error Rate (SLO: Error rate < 0.5%)
- **SLI:** The percentage of requests that result in errors (such as 4xx or 5xx status codes) over the total number of requests.
  - **Formula:**  
    \[
    \text{SLI} = \frac{\text{Number of Error Responses}}{\text{Total Number of Requests}} \times 100
    \]
  - This SLI helps monitor the frequency of failures or issues in the system.

### 5. Latency Percentiles (SLO: 95th percentile < X milliseconds)
- **SLI:** The 95th percentile of the request response time, meaning 95% of requests should be answered within this time.
  - **Formula:**  
    \[
    \text{SLI} = \text{Response time at the 95th percentile of all requests}
    \]
  - This helps measure the "tail latency," or the response time for the worst-performing requests, which can be critical in ensuring a good user experience for most users.


## Create a Dashboard to measure our SLIs
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.

## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here. Also provide a (screenshot) sample Python file containing a trace and span code used to perform Jaeger traces on the backend service.

## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.

## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue also include a screenshot of the tracer span to demonstrate how we can user a tracer to locate errors easily.

TROUBLE TICKET

Name:

Date:

Subject:

Affected Area:

Severity:

Description:


## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name four SLIs that you would use to measure the success of this SLO.

## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create a list of 2-3 KPIs to accurately measure these metrics as well as a description of why those KPIs were chosen. We will make a dashboard for this, but first write them down here.

## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  
