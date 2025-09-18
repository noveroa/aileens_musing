## Kubernetes Monitoring Cluster Components

> How do you monitor resource consumption on Kubernetes? what would you like to monitor?

* node-level metrics  (number of nodes in the cluster, how many of them are healthy)
* performance metrics  (CPU, memory, network, and disc utilization)
* pod-level metrics (number of pods, performance metrics of each pod, CPU and memory consumption on them.)

* One needs a solution that will monitor these metrics, store them, and provide analytics around this data.
    * no kubernetes native, but open-source or proprietary like  Metrics Server, Prometheus, the Elastic Stack,, Datadog and Dynatrace

    * *kubelet* contains a sub component known as the cAdvisor or Container Advisor.
        * _cAdvisor_ is responsible for retrieving performance metrics from pods and exposing them through the kubelet API to make the metrics available
        