import requests

def jfrog():
    artifactory_url = 'http://54.215.251.107:8082/artifactory/example-repo-local/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'

    file_path = '/home/ubuntu/java-3.0/target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'

    username = 'admin'
    password = 'Datta123@'

    with open(file_path , 'rb') as file:
        response = requests.put(artifactory_url , auth=(username , password), data = file)

    if response.status_code == 201:
        print("\n PUT request successful")
    else:
        print("PUT request failed with status code", response.status_code)
        print("response content:")
        print(response.text)

# Call the jfrog function to execute the upload
jfrog()
