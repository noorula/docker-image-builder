# Docker image builder steps for Valohai

Example steps for using Valohai executions to build Docker images and push them to your (private) registry. The example covers three use cases for different registries (Docker Hub, AWS ECR and GCP Artifact Registry). 

## Prerequisites

- Account (admin) and a valid subscription at [app.valohai.com](https://app.valohai.com).
- A Git repository containing a `valohai.yaml` with at least one step and all the other required code files.
- A Docker registry to push images to.
- A Valohai environment with the docker run argument `--privileged`. Contact Valohai Support (<support@valohai.com>) if you need one added to your organization.
    - Note that privileged containers have root capabilities on the host. This is required for running the Docker daemon inside a Docker container in this example.

## Running the steps

1. Add this repository as a library steps in Valohai. 
2. Navigate to the Create Execution page on Valohai UI. 
3. Choose the correct environment. 
4. Fill in parameters:
    - **docker-tag** - defines the image tag when building and pushing the image.
    - **repository** - required for docker login in AWS and GCP
5. Provide the Dockerfile (choose one):
    - As an input from a data store connected to the project.
    - As the **dockerfile** parameter.
6. Save the credentials as environment variables for authentication:
    - Docker Hub: provide `DHUSERNAME` and `DHPASSWORD`
    - AWS ECR: Allow `ValohaiWorkerRole` to push to the repository you are using.
    - GCP Artifact Registry: create a service account with `Add Service Account Token Creator` and `Artifact Registry Writer` roles and provide the JSON key as `GCPKEY`. 