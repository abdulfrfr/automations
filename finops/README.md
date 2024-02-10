Hey there, as you leverage the cloud for efficiency and effective operations, you would not want to pay for services you do not need, especially as DevOps Engineers, the cloud being our best place, we tend to want optimize our cloud usage, paying for what is used and using only what is needed, and that is where FinOps practices comes in, helping us with a practice for cost optimization.

Today we will be talking about a FinOps Tool called KubeCost Cloud. This tool being one of the best tools for cost optimization has some unique feature to help you optimize your cloud usage potenitally. This tool is specifically best used for our Kubernetes Cluster. Integrating this tool to your cluster is as simple as signing up from your web application and running a line of command on your cluster and you are all set. With the below command you can integrate kubecost cloud into your cluster and start using it immediately.

```
helm upgrade --install kubecost-cloud \
--repo https://kubecost.github.io/kubecost-cloud-agent/ kubecost-cloud-agent \
--namespace kubecost-cloud --create-namespace \
-f https://raw.githubusercontent.com/kubecost/kubecost-cloud-agent/main/values-cloud-agent.yaml \
--set imageVersion="lunar-sandwich.v0.1.2" \
--set cloudAgentKey="eyJ0ZWFtSWQiOiI5MTFmMmI4OS03ODFjLTQ1MmItOTYyMS0yMjBhZjRkZjA2MGQifQ==" \
--set cloudAgentClusterId="cluster-1" \
--set cloudReportingServer="collector.app.kubecost.com:31357" \
--set networkCosts.enabled=true

```

Running the above command on your will fetch some resources from helm chart, create a new namespace for the resources and deploy the required resources needed for kubecost to work for you. All resources and information will then be accessed form your dashboard on their application.


**KubeCost Pricing Capabilities**
Now one very interesting and very useful theory about kubecost cloud, is how much details it bring out of your cluster to help you optimize your cost, it goes through every corner of your application, each namespace, each pods and all. Kubecost cloud, gives you and overview of your cost spending, price of each resource you have deployed in your cluster and also gives a break down of every single resources from the cluster level down to the pod level.
Below are some images showing how kubecost shows our resource cost in details...

![overview](<Screenshot from 2024-01-30 17-21-35.png>)
Above is a screenshot that shows an overview of the total amount a cluster is taking

![namespace](<Screenshot from 2024-01-30 17-21-51.png>)
Above shows all the namespaces in our cluster and how much is consumes from each namespace

![network](<Screenshot from 2024-01-30 17-22-04.png>)
We can also see the nwtworks services and resources we have deployed and how much they consume

![Cluster](<Screenshot from 2024-01-30 17-30-41.png>)
Now clicking into a cluster we can see the all the available namespaces and it cost, hovering over the chart there also shows us how which namespace is costing how much

![deployment](<Screenshot from 2024-01-30 17-23-34.png>)
Now we have clicked into our default namespace and we can see each resources we have in that namespace, here we have two deployments

![pod](<Screenshot from 2024-01-30 17-34-48.png>)
Clicking into our first deployment we can also see above the pod we have inside the deployment and it cost and we can also click on the pod to see further info like what our cluster is running on, which image we are running and much more as seen below

![pod info](<Screenshot from 2024-01-30 17-36-03.png>)