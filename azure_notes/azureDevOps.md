

# Azure DevOps. https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/linux-agent?view=azure-devops&tabs=IP-V4

Azure CI/CD can integrate with docker and the azure container registry.

for a basic Azure pipeline YAML:

## key concepts:
* Trigger ---> Pipeline --> Stages (Jobs/ Agents) ---> Steps (script, task, task,.. (publish build artifact/deploy/invoke REST API...)))

* Trigger 
    * when the pipeline be kicked off (git commit, build schedule..), can be by paths thus focusing on a single microservice vs all in one repo
* Stages
    * Build, Publish, Test, Rest
    * Can have 1+ jobs, ultiple runners
* Steps
* Variables .. 

```sh
# Docker
# Build and push an image to Azure Container Registry
# https://docs.microsoft.com/azure/devops/pipelines/languages/docker

trigger:
#- main # the branch of the code repository or you can use branch/apath, here by path for a single directory within the repo /results
    paths:
        include:
        - result/*



resources:
- repo: self 

variables:
  # Container registry service connection established during pipeline creation
  dockerRegistryServiceConnection: '92eb0536-90c1-4ae0-aab9-348871add3b6'
  ## name of the project
  imageRepository: 'votingapplication'. 
  ## the azure container registry
  containerRegistry: 'noveroazuredevops.azurecr.io'
  ## docker file path in the repo
  dockerfilePath: '$(Build.SourcesDirectory)/result/Dockerfile'
  tag: '$(Build.BuildId)'

  # Agent VM image name
  vmImageName: 'ubuntu-latest'

stages:
- stage: Build
  displayName: Build and push stage
  jobs:
  - job: Build
    displayName: Build
    pool:
      vmImage: $(vmImageName)
    steps:
    - task: Docker@2
      displayName: Build and push an image to container registry
      inputs:
        command: buildAndPush
        repository: $(imageRepository)
        dockerfile: $(dockerfilePath)
        containerRegistry: $(dockerRegistryServiceConnection)
        tags: |
          $(tag)
```