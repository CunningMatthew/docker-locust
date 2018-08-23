# docker-locust

Docker Image for a [Locust](http://locust.io/).

# Running in K8s

kubectl create configmap locust-config --from-file=locust_test/

kubectl create -f locust-master-deployment.yaml

kubectl expose deployment locust-master-deployment --type=LoadBalancer

kubectl create -f locust-worker-deployment.yaml

# Reloading Configuration

kubectl scale deployment locust-master-deployment --replicas=0

kubectl scale deployment locust-worker-deployment --replicas=0

kubectl scale deployment locust-master-deployment --replicas=1

kubectl scale deployment locust-worker-deployment --replicas=6

# Configuring minikube to run locally

Set up a new virtual switch in Hyper-V Manager on windows that was configured to the external network

Started my minikube instance using the command `minikube start --vm-driver hyperv --hyperv-virtual-switch "minikube_switch"`

Got the IP of my minikube deployment by using the command `minikube ip`

Enabled ingress on the minikube instance by using the command `minikube addons enable ingress`

# Notes from the field

These quantities of requests can cause unprepared kubernetes environments (my minikube, for example) to completely stop responding to requests as all networking infrastructure can be consumed.

I tried using an ingress instance originally, but I get much better graphs and reporting out of a direct loadbalancer.
