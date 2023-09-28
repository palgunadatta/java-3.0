import requests

def jfrog():
    artifactory_url = 'http://54.241.71.156:8082/artifactory/example-repo-local/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'

    path = '/home/ubuntu/JAVA_APP_3.0/target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'

    username = 'admin'
    passkey = ''

    with open(path , 'rb') as file:
        reponse = requests.put(artifactory_url , auth=(username , passkey), data = file)
    
    if reponse.status_code == 201:
        print("\n PUT request successful")
    else:
        print("PUT rquest failed with status code (response.status_code)")
        print("response content:")
        print(response.text)
